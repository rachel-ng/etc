var csv = "data/data.csv";

d3.csv(csv, processRow).then(processData);

function processRow (row, index, columnKeys) {
    var split_time = row["date"].split("T")[1].split(":");
    row["orig_time"] = parseInt(split_time);
    row["date"] = d3.isoParse(row["date"]);
    row["page_time_start"] = d3.isoParse(row["page_time_start"]); 
    row["page_time_end"] = d3.isoParse(row["page_time_end"]); 
    row["offset"] = row["orig_time"] - parseInt(row["date"].toTimeString().split(" ")[0].split(":")[0]);
    row["date"] = d3.timeHour.offset(row["date"],row["offset"]);
    if (row["page_time_start"]) {
        row["page_time_start"] = d3.timeHour.offset(row["page_time_start"], row["offset"]); 
        row["page_time_end"] = d3.timeHour.offset(row["page_time_end"], row["offset"]); 
    }
    row["num"] = parseInt(row["num"]);
    if (row["num"] > last) {
        last = row["num"];
    }
    return row;
}

function processData (data) {
    console.log(data, data.columns)

    var dataset = data.map(function(d) { 
        if (d["page_time_end"]) {
            var a = d["page_time_end"];
            var day = new Date(a.getFullYear(), a.getMonth(), a.getDate(), 12);
            console.log(a);
            console.log(day);
            var dct = {"x": d["date"], 
            "y": (d["date"].getHours() * 60) + d["date"].getMinutes(), 
            "x1": day, 
            "y1": (d["page_time_end"].getHours() * 60) + d["page_time_end"].getMinutes(), 
            "y2": (d["page_time_start"].getHours() * 60) + d["page_time_start"].getMinutes()}; 
        }
        else {
            var dct = {"x": d["date"], 
            "y": (d["date"].getHours() * 60) + d["date"].getMinutes(),
            "y1": 0, 
            "y2": 0};
        }
        Object.entries(d).forEach(([key, val]) => {
            dct[key] = val;
        });
        return dct;
    });
   
    console.log(dataset);

    var minHour = d3.min(dataset, function(d) { return d["date"].getHours();});
    if (minHour > 3) {
        minHour -= 1;
    }
    
    var maxHour = d3.max(dataset, function(d) { return d["date"].getHours();}) + 1;
    if (maxHour > 20) {
        maxHour = 24;
    }
    else if (maxHour >= 17) {
        maxHour += 1; 
    }
    else if (maxHour < 17) {
        maxHour = 17;
    }
    
    console.log(minHour);
    console.log(maxHour);

    var x = d3.scaleTime()
        .range([0, width]) // output
        .domain(d3.extent(dataset, function(d) { return d.x; }))
        .nice();
    
    var z = d3.scaleBand()
        .domain(dataset.map((d)=> {return d["x"];}))
        .range([0, width])
        .padding(0.85);

    var y = d3.scaleLinear()
        .domain([minHour * 60, maxHour * 60]) // input 
        .range([height, 0]);// output 
    
    var line = d3.line()
        .x(function(d) { return x(d.x); }) 
        .y(function(d) { return y(d.y); })
        .curve(d3.curveMonotoneX)

    var area = d3.area()
        .x(function(d) { return x(d.x); })
        .y0(height)
        .y1(function(d) { return y(d.y); })
        .curve(d3.curveMonotoneX) // apply smoothing to the line

    var div = d3.select("body").append("div")	
        .attr("class", "tooltip")				
        .style("opacity", 0);

    var svg = d3.select("#chart").append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
            .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    svg.append("g")
        .attr("class", "x axis")
        .attr("transform", "translate(0," + height + ")")
        .call(d3.axisBottom(x).tickFormat(function(i){
            return mdformat(i);
        })); 
 
    svg.append("g")
        .attr("class", "y axis")
        .call(d3.axisLeft(y)
            .tickValues(d3.range(minHour, maxHour + 1).map(function(n){return n * 60;}))
            .tickFormat(function(i){
                return timeStamps[i/60];
            }));

    var gradient = dataset.map((d) => { return {offset: x(d.x)/width, color: colors[d.status]}; });
    var revgradient = dataset.map((d) => { return {offset: x(d.x)/width, color: colors[d.status]}; }).reverse();
    var a = Object.keys(colors).map((d)=> { return gradient[gradient.map(function(d) { return d.color; }).indexOf(colors[d])]; });
    var b = Object.keys(colors).map((d)=> { return revgradient[revgradient.map(function(d) { return d.color; }).indexOf(colors[d])]; });
    var off = a.concat(b.filter((item) => a.indexOf(item) < 0)).sortBy("offset");
    //console.log(off);
    
    var uniq = {};
    var offset = off.filter(obj => !uniq[obj.offset] && (uniq[obj.offset] = true));
    // console.log(offset);
    
    var means = {};
    Object.values(colors).map((d) => {
        let c = offset.filter(i=>i["color"] == d); 
        let a = 0;
        c.forEach((i) => { a += i["offset"]; });
        means[d] = a / c.length;
    });
    // console.log(means);

    var offsets = offset.map((d) => { return {offset: (d["offset"] + means[d["color"]]) / 2, color: d["color"]}; });
    // console.log(offsets);

    svg.append("linearGradient")
        .attr("id", "area-gradient")
        .attr("gradientUnits", "userSpaceOnUse")
        .attr("x1", '0%').attr("y1", '0%') 
        .attr("x2", '100%').attr("y2", '0%') 
    .selectAll("stop")
        .data(offsets)
    .enter().append("stop")
        .attr("offset", function(d) { return d.offset; })
        .attr("stop-color", function(d) { return d.color; });
      
    svg.append("path").datum(dataset)
        .attr("class", "area")
        .attr("d", area);

    svg.selectAll(".dot")
        .data(dataset)
        .enter().append("circle") 
        .attr("class", function(d){
            var c = "dot ";
            c += d["status"];
            return c;
        })
        .attr("cx", function(d) { return x(d.x) })
        .attr("cy", function(d) { return y(d.y) })
        .attr("r", function(d) {
            if (d["num"] == last) {
                return 10;   
            }
            else {
                return 7.5;
            }
        })
        .on("mouseover", function(a, b, c) { 
       		div.transition()		
                .duration(150)		
                .style("opacity", .9);	
            div.html("<div class='container'><div class='row'><div class='col'><span class='icon' style='left: 0; text-align: center; background-color: " + status_colors[a["status"]] + "'>" + a["num"] + "</span></div><div class='row'><div class='col-sm details'>" + a["details"] + "<br>" + mdformat(a["date"]) + " " + tformat(a["date"]) + "</div></div></div>"
                )	
                .style("left", (d3.event.pageX + 25) + "px")		
                .style("top", (d3.event.pageY - 50) + "px"); 
        })
        .on("mouseout", function(d){
		div.transition()		
            .duration(200)		
            .style("opacity", 0);	
		})

	svg.selectAll(".bar")
        .data(dataset)
        .enter().append("rect")
         .attr("class", function(d){
            var c = "bar ";
            c += d["status"];
            return c;
        })
        .attr("x", function (d) { 
            console.log(d);
            console.log(d.x1);
            return x(d.x1) - 5; 
        })
        .attr("y", function (d) { return y(d.y1); })
        .attr("rx", 5)// z.bandwidth() / 2)
        .attr("ry", 5)//z.bandwidth() / 2)
        .attr("width", 10)//z.bandwidth())
        .attr("height", function (d) { return y(d.y2) - y(d.y1); })
        .on("mouseover", function(a, b, c) { 
            let time = a["page_time_end"] - a["page_time_start"];
            let convertm = 1000 * 60;
            let converth = 1000 * 3600;
            div.transition()		
                .duration(150)		
                .style("opacity", .9);	
            div.html("<div class='container'><div class='row'><div class='col'><span class='icon' style='left: 0; text-align: center; background-color: " + status_colors[a["status"]] + "'>" + a["num"] + "</span><br>" + Math.floor(time / converth) + ":" + Math.floor((time % converth) / convertm) + "</div><div class='row'><div class='col-sm details'>" + a["details"] + "<br>" + mdformat(a["date"]) + " " + tformat(a["date"]) + "<br>" + tformat(a["page_time_start"]) + " - " + tformat(a["page_time_end"]) + "</div></div></div>"
                )	
                .style("left", (d3.event.pageX + 25) + "px")		
                .style("top", (d3.event.pageY - 50) + "px"); 
        })
        .on("mouseout", function(d){
		div.transition()		
            .duration(200)		
            .style("opacity", 0);	
		})
}
