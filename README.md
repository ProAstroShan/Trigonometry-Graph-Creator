# Trigonometry-Graph-Creator
## About
This is a program that creates the graphs of the 3 core trigonometry functions [sin(x), cos(x), tan(x)], and another 3 of their reciprocal functions [sec(x), cosec(x), cot(x)].

## Methodology
- Creates an interval of numbers between 0 and 10, with 1000 spaces between them. The greater the number of these intervals, the smoother the graph, but also the larger the runtime. So, I feel that 1000 is a good compromise for quality and speed. This interval acts as the x-axis
- Applies the core trigonometry functions to the interval of numbers, to obtain the raw y-coordinate of the points for these functions. However these points may include asymptodes that can skew the graph, that must be removed
- The points that may be near the asymptodes are detected by finding out if the y-coordinates of the points is greater than 10, since normal points do not have a y-coordinate this high.
- These points are replaced with np.nan, since matplotlib does not plot points with a coordinate being np.nan, so the asyptodes do not ruin the graph
- The graphs are finally plotted with the 6 lists of y-coordinate for the graphs

## Running of algorithm
- Install Python
- Run graph_creator.py
- The output can be seen in "Trigonometry_Graphs.png"
