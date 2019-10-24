var csv = "data/data.csv";

d3.csv(csv, processRow).then(processData);

function processRow (row, index, columnKeys) {
    var time = row["date"];
    var split_time = row["date"].split("T")[1].split(":");
    var d = 0;
    row["orig_time"] = parseInt(split_time);
    row["date"] = d3.isoParse(time);
    console.log(row["date"]);
    row["offset"] = row["orig_time"] - parseInt(row["date"].toTimeString().split(" ")[0].split(":")[0]);
    if (row["offset"] + row["date"].getHours() >= 24) {
        d += 1;
        row["offset"] = row["offset"] % 24;
    }
    let day = row["date"];
    console.log(day);
    day.setHours(row["fixed_time"]);
    console.log(day);
    day.setDate(day.getDate() + d);
    console.log(day);
    row["date"] = day; 
    row["num"] = parseInt(row["num"]);
    if (row["num"] > last) {
        last = row["num"];
    }
    return row;
}

function processData (data) {
    console.log(data, data.columns)

    var offset;
    var dataset = data.map(function(d) { 
        console.log(d);
        var split_time = d["date"].toTimeString().split(" ")[0].split(":");
        var dct = {"x": d["date"], "y": (parseInt(split_time[0]) * 60) + parseInt(split_time[1])};
        Object.entries(d).forEach(([key, val]) => {
            dct[key] = val;
        });
        offset = dct["offset"];
        return dct;
    });
    
    var minHour = d3.min(dataset, function(d) { return d["fixed_time"];}) - offset;
    if (minHour > 3) {
        minHour -= 1;
    }
    if (minHour > 12) {
        minHour = 9;
    }
    
    var maxHour = d3.max(dataset, function(d) { return d["fixed_time"];}) - offset;
    if (maxHour > 18 && maxHour < 24) {
        maxHour += 1; 
    }
    if (maxHour < 18) {
        maxHour = 17;
    }


    console.log(minHour);
    console.log(maxHour);

    /*var padding = 0; // 3.6e+6 * ;//1.08e+8;

    var minDate = d3.min(dataset, function(d) { return d["date"].getTime() - padding; }),
        maxDate = d3.max(dataset, function(d) { return d["date"].getTime() + padding; });
    */
   
    // 2. Use the margin convention practice 
    // 5. X scale will use the index of our data
    var x = d3.scaleTime()
        .range([0, width]) // output
        .domain(d3.extent(dataset, function(d) { return d.x; }))
        .nice();

    // 6. Y scale will use the randomly generate number 
    var y = d3.scaleLinear()
        .domain([minHour * 60, maxHour * 60]) // input 
        .range([height, 0]);// output 
    
    // 7. d3's line generator
    var line = d3.line()
        .x(function(d) { return x(d.x); }) // set the x values for the line generator
        .y(function(d) { return y(d.y); }) // set the y values for the line generator 
        .curve(d3.curveMonotoneX) // apply smoothing to the line

    var area = d3.area()
        .x(function(d) { return x(d.x); })
        .y0(height)
        .y1(function(d) { return y(d.y); })
        .curve(d3.curveMonotoneX) // apply smoothing to the line

        // Define the div for the tooltip
    var div = d3.select("body").append("div")	
        .attr("class", "tooltip")				
        .style("opacity", 0);

    // 1. Add the SVG to the page and employ #2
    var svg = d3.select("#chart").append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
            .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    // 3. Call the x axis in a group tag
    svg.append("g")
        .attr("class", "x axis")
        .attr("transform", "translate(0," + height + ")")
        .call(d3.axisBottom(x).tickFormat(function(i){
            return mdformat(i);
        })); // Create an axis component with d3.axisBottom

    // 4. Call the y axis in a group tag
    svg.append("g")
        .attr("class", "y axis")
        .call(d3.axisLeft(y)
            .tickValues(d3.range(25).map(function(n){return n * 60;}))
            .tickFormat(function(i){
                console.log(timeStamps[i/60]);
                return timeStamps[i/60];
            }));

    var gradient = dataset.map((d) => { 
        return {offset: x(d.x)/width, color: colors[d.status]};
    });
    var revgradient = dataset.map((d) => { 
        return {offset: x(d.x)/width, color: colors[d.status]};
    }).reverse();
    var a = Object.keys(colors).map((d)=> {
        return gradient[gradient.map(function(d) { return d.color; }).indexOf(colors[d])];
    });
    var b = Object.keys(colors).map((d)=> {
        return revgradient[revgradient.map(function(d) { return d.color; }).indexOf(colors[d])];
    });
    var off = a.concat(b.filter((item) => a.indexOf(item) < 0)).sortBy("offset");
    console.log(off);
    
    var uniq = {};
    var offset = off.filter(obj => !uniq[obj.offset] && (uniq[obj.offset] = true));
    //offset[0]["offset"] = 0; 
    //offset[offset.length - 1]["offset"] = 1;
    console.log(offset);
    
    var means = {};
    Object.values(colors).map((d) => {
        let c = offset.filter(i=>i["color"] == d); 
        let a = 0;
        c.forEach((i) => {
            a += i["offset"];
        });
        means[d] = a / c.length;
    });
    console.log(means);

    var offsets = offset.map((d) => {
        return {offset: (d["offset"] + means[d["color"]]) / 2, color: d["color"]}; 
    });
    console.log(offsets);

    svg.append("linearGradient")
        .attr("id", "area-gradient")
        .attr("gradientUnits", "userSpaceOnUse")
        .attr("x1", '0%').attr("y1", '0%') 
        .attr("x2", '100%').attr("y2", '0%') 
  // x1 = 100% (red will be on right horz) / y1 = 100% (red will be on bottom vert)
  // x2 = 100% (red will be on left horz) / y2 = 100% (red will be on top vert)
  // mixed values will change the angle of the linear gradient. Adjust as needed.
    .selectAll("stop")
        .data(offsets)
        //.data(offset)
    .enter().append("stop")
        .attr("offset", function(d) { return d.offset; })
        .attr("stop-color", function(d) { return d.color; });
      
    // 9. Append the path, bind the data, and call the line generator 
    svg.append("path").datum(dataset) // 10. Binds data to the line 
        .attr("class", "area")
        .attr("d", area);
    //svg.append("path").datum(dataset) // 10. Binds data to the line 
    //    .attr("class", "line") // Assign a class for styling 
    //    .attr("d", line); // 11. Calls the line generator 

    // 12. Appends a circle for each datapoint 
    svg.selectAll(".dot")
        .data(dataset)
        .enter().append("circle") // Uses the enter().append() method
        .attr("class", function(d){
            var c = "dot ";
            c += d["status"];
            return c;
        })
        .attr("cx", function(d) { return x(d.x) })
        .attr("cy", function(d) { return y(d.y) })
        .attr("r", function(d) {
            if (d["num"] == last) {
                return 15;   
            }
            else {
                return 10;
            }
        })
        .on("mouseover", function(a, b, c) { 
            console.log(a) 
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
}
