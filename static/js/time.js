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
            var dct = {"x": d["date"], 
            "y": (d["date"].getHours() * 60) + d["date"].getMinutes(), 
            "x1": d["page_time_end"], 
            "y1": (d["page_time_end"].getHours() * 60) + d["page_time_end"].getMinutes(), 
            "y2": (d["page_time_start"].getHours() * 60) + d["page_time_start"].getMinutes()}; 
        }
        else {
            var dct = {"x": d["date"], 
            "y": (d["date"].getHours() * 60) + d["date"].getMinutes(),
            "y1": 0, 
            "y2": 0};
        }

        /*
        if (d["page_time_end"]) {
            var dct = {"x": d["page_time_end"], 
            "y3": (d["date"].getHours() * 60) + d["date"].getMinutes()};
            "y": (d["page_time_end"].getHours() * 60) + d["page_time_end"].getMinutes(), 
            "y1": (d["page_time_start"].getHours() * 60) + d["page_time_start"].getMinutes(), 
        }
        else {
            var dct = {"x": d["date"], 
            "y3": (d["date"].getHours() * 60) + d["date"].getMinutes()};
            "y": 0, 
            "y1": 0, 
        }
        */
        Object.entries(d).forEach(([key, val]) => {
            dct[key] = val;
        });
        return dct;
    });

    console.log(dataset);

    var minHour = d3.min(dataset, function(d) { 
        if(d["page_time_start"]) {
            return d["page_time_start"].getHours();
        }
    });
    if (minHour > 3) {
        minHour -= 1;
    }
    
    var maxHour = d3.max(dataset, function(d) { 
        if(d["page_time_end"]) {
            return d["page_time_end"].getHours();
        }
    }) + 1;
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


    var svg = d3.select("#chart").append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
            .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    var x = d3.scaleTime()
        .range([0, width]) // output
        .domain(d3.extent(dataset, function(d) { return d.x; }))
        .nice();

    var y = d3.scaleLinear()
        .domain([minHour * 60, maxHour * 60])
        .range([height, 0]);
    
    var div = d3.select("body").append("div")	
        .attr("class", "tooltip")				
        .style("opacity", 0);

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

	svg.selectAll(".bar")
        .data(dataset)
        .enter().append("rect")
         .attr("class", function(d){
            console.log(d);
            var c = "bar ";
            c += d["status"];
            return c;
        })
        .attr("x", function (d) { return x(d.x) - 5; })
        .attr("y", function (d) { return y(d.y1); })
        .attr("rx", 5)
        .attr("ry", 5)
        .attr("width", 10) 
        .attr("height", function (d) { return y(d.y2) - y(d.y1); })
        .on("mouseover", function(a, b, c) { 
            let time = a["page_time_end"] - a["page_time_start"];
            let convertm = 1000 * 60;
            let converth = 1000 * 3600;
       		div.transition()		
                .duration(150)		
                .style("opacity", .9);	
            div.html("<div class='container'><div class='row'><div class='col'><span class='icon' style='left: 0; text-align: center; background-color: " + status_colors[a["status"]] + "'>" + a["num"] + "</span><br>" + Math.floor(time / converth) + ":" + Math.floor(time % converth / convertm) + "</div><div class='row'><div class='col-sm details'>" + a["details"] + "<br>" + mdformat(a["date"]) + " " + tformat(a["date"]) + "</div></div></div>"
                )	
                .style("left", (d3.event.pageX + 25) + "px")		
                .style("top", (d3.event.pageY - 50) + "px"); 
        })
        .on("mouseout", function(d){
		div.transition()		
            .duration(200)		
            .style("opacity", 0);	
		})
/*
    svg.selectAll(".dot")
        .data(dataset)
        .enter().append("circle") // Uses the enter().append() method
        .attr("class", function(d){
            var c = "dot time ";
            c += d["status"];
            return c;
        })
        .attr("cx", function(d) { return x(d.x) + ((x.bandwidth())/ 2)})
        .attr("cy", function(d) { return y(d.y) })
        .attr("r", x.bandwidth())
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
*/
}
