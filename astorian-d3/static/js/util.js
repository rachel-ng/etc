var csv = "data/data.csv";

var margin = {top: 50, right: 50, bottom: 50, left: 50};
var width = window.innerWidth*.7 - margin.left - margin.right; // Use the window's width 
var height = window.innerHeight*.7 - margin.top - margin.bottom; // Use the window's height

var last = 0;

var timeStamps = ["12:00 AM", "1:00 AM", "2:00 AM", "3:00 AM", "4:00 AM", "5:00 AM", "6:00 AM", "7:00 AM", "8:00 AM", "9:00 AM", "10:00 AM", "11:00 AM", "12:00 PM", "1:00 PM", "2:00 PM", "3:00 PM", "4:00 PM", "5:00 PM", "6:00 PM", "7:00 PM", "8:00 PM", "9:00 PM", "10:00 PM", "11:00 PM", "12:00 AM"];


var colors = {"bidded": "#2AC869", "intending": "#F8CF23", "reviewing": "#E46E00", "not-bidding": "#D91B03"};
var status_colors = {"bidded": "#2AC869", "intending": "#F8CF23", "reviewing": "#A2A2A5", "not-bidding": "#D91B03"};
var statuses = ["", "not bidding", "reviewing", "intending", "bidded"];
var stat = {"not-bidding": 1, "reviewing": 2, "intending": 3, "bidded": 4};

var mdformat = d3.timeFormat("%b %e");
var tformat = d3.timeFormat("%I:%M %p");
 


Array.prototype.sortBy = function(p) {
    return this.slice(0).sort(function(a,b) {
      return (a[p] > b[p]) ? 1 : (a[p] < b[p]) ? -1 : 0;
    });
}

function newDate (a, m, d, h) {
    return new Date(a.getFullYear(), a.getMonth() + m, a.getDate() + d, h);
}

