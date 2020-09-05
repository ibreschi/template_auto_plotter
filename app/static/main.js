// In this file we should add the different ways to display data
//

const svg = d3.select('#svg');

svg.append('circle')
  .attr('cx', 200)
  .attr('cy', 200)
  .attr('r', 90)
  .style('fill', 'green')
