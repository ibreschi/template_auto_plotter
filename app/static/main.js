// In this file we should add the different ways to display data
//

const svg = d3.select('#svg');

svg.append('circle')
  .attr('cx', 200)
  .attr('cy', 200)
  .attr('r', 90)
  .style('fill', 'green');

// This should contain all the code to display <A> type of data
const As = d3.selectAll('.A');
As.append("circle")
  .attr("cx", 100)
  .attr("cy", 100)
  .attr("r", 40)
  .style("fill", "blue");

// This should contain all the code to display <B> type of data
const Bs = d3.selectAll('.B');
Bs.append("rect")
  .attr("width", 50)
  .attr("height", 100)
  .style("fill", "red");
