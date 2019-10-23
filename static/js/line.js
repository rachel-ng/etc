var csv = "data/data.csv";

d3.csv(csv, processRow).then(processData);

function processRow (row, index, columnKeys) {
    let time = row["date"];
    let split_time = row["date"].split("T")[1].split(":");
    row["orig_time"] = parseInt(split_time);
    row["date"] = d3.isoParse(time);
    row["offset"] = row["orig_time"] - parseInt(row["date"].toTimeString().split(" ")[0].split(":")[0]);
    row["fixed_time"] = row["orig_time"] + row["offset"];
    row["date"] = d3.isoParse(time.substr(0,11) + row["fixed_time"] + time.substr(13)) ;
    row["num"] = parseInt(row["num"]);
    return row;
}

function processData (data) {
    console.log(data, data.columns)

    let offset;
    var dataset = data.map(function(d) { 
        let split_time = d["date"].toTimeString().split(" ")[0].split(":");
        let dct = {"x": d["date"], "y": (parseInt(split_time[0]) * 60) + parseInt(split_time[1])};
        Object.entries(d).forEach(([key, val]) => {
            dct[key] = val;
        });
        offset = dct["offset"];
        return dct;
    });
    
    var minHour = d3.min(dataset, function(d) { return d["fixed_time"];}) - offset;
    console.log(minHour);
    if (minHour > 3) {
        minHour -= 1;
    }
    if (minHour > 12) {
        minHour = 9;
    }
    console.log(minHour);
    
    var maxHour = d3.max(dataset, function(d) { return d["fixed_time"];}) - offset;
    console.log(maxHour);
    if (maxHour > 18) {
        maxHour += 1;
    }
    if (maxHour < 16) {
        maxHour = 17;
    }
    console.log(maxHour);


    /*var padding = 0; // 3.6e+6 * ;//1.08e+8;

    var minDate = d3.min(dataset, function(d) { return d["date"].getTime() - padding; }),
        maxDate = d3.max(dataset, function(d) { return d["date"].getTime() + padding; });
    */

    var timeStamps = ["12:00 AM", "1:00 AM", "2:00 AM", "3:00 AM", "4:00 AM", "5:00 AM", "6:00 AM", "7:00 AM", "8:00 AM", "9:00 AM", "10:00 AM", "11:00 AM", "12:00 PM", "1:00 PM", "2:00 PM", "3:00 PM", "4:00 PM", "5:00 PM", "6:00 PM", "7:00 PM", "8:00 PM", "9:00 PM", "10:00 PM", "11:00 PM", "12:00 AM"];
    
    // 2. Use the margin convention practice 
    var margin = {top: 50, right: 50, bottom: 50, left: 50}
      , width = window.innerWidth*.8 - margin.left - margin.right // Use the window's width 
      , height = window.innerHeight - margin.top - margin.bottom; // Use the window's height

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

    // Define the div for the tooltip
    var div = d3.select("body").append("div")	
        .attr("class", "tooltip")				
        .style("opacity", 0);

    // 1. Add the SVG to the page and employ #2
    var svg = d3.select("body").append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
      .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    // 3. Call the x axis in a group tag
    svg.append("g")
        .attr("class", "x axis")
        .attr("transform", "translate(0," + height + ")")
        .call(d3.axisBottom(x).tickFormat(function(i){
            let xformat = d3.timeFormat("%b %e");
            return xformat(i);
        })); // Create an axis component with d3.axisBottom

    // 4. Call the y axis in a group tag
    svg.append("g")
        .attr("class", "y axis")
        .call(d3.axisLeft(y).tickValues(d3.range(25).map(function(n){return n * 60;})).tickFormat(function(i){return timeStamps[i/60];}));// Create an axis component with d3.axisLeft

   // 9. Append the path, bind the data, and call the line generator 
    svg.append("path")
        .datum(dataset) // 10. Binds data to the line 
        .attr("class", "line") // Assign a class for styling 
        .attr("d", line); // 11. Calls the line generator 

    // 12. Appends a circle for each datapoint 
    svg.selectAll(".dot")
        .data(dataset)
        .enter().append("circle") // Uses the enter().append() method
        .attr("class", "dot") // Assign a class for styling
        .attr("cx", function(d, i) { return x(d.x) })
        .attr("cy", function(d) { return y(d.y) })
        .attr("r", 5)
        .on("mouseover", function(a, b, c) { 
            console.log(a) 
       		div.transition()		
                .duration(150)		
                .style("opacity", .75);	
            div.html("<br/>"  + a["date"])	
                .style("left", (d3.event.pageX + 25) + "px")		
                .style("top", (d3.event.pageY - 50) + "px"); 
        })
        .on("mouseout", function(d){
		div.transition()		
            .duration(200)		
            .style("opacity", 0);	
		})
}
