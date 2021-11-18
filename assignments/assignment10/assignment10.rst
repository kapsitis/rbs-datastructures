Written Assignment 10
======================

.. image:: figs-maximum-flow/flow-graph.png
   :width: 3in

**(A)**
  Run Edmonds-Karp algorithm on the graph shown above. 
  Every edge in the picture is labeled with a number showing the *capacity* of that edge.
  
  For every phase highlight the the augmenting path (or simply list its vertices), 
  find the *residual flow* of this augmenting graph. 
  Draw a copy of the original graph where the residual flow is added.
  Namely, every age is labeled by two numbers ``f/c`` -- the actual flow ``f`` (after adding
  the residual flow obtained in this step) and also the capacity ``c`` of the edge (it never changes).
  
  During the next phase, show the next residual graph, highlight the augmenting path, find the residual flow. 
  And next to that residual graph show a new copy of the original graph with updated flow numbers. 
  Thus, every phase shows two oriented graphs: 
  
  * The current residual graph (initially -- it is simply the given graph with all flows equal to 0). 
    It only displays edge capacities and **not** flows (but it may include *reversed edges*).
    In this graph you can search (in BFS order) and highlight the augmenting path.
  * The original graph with all the flows added. In this graph you must also show the flows
    using the notation with two numbers ``f/c``.
  
  .. note:: 
    In Edmonds-Karp algorithm visiting the successors of the source vertex :math:`s` in the BFS order
    needs to know the ordering. Assume that all the vertices are arranged in alphabetical order.
  
**(B)**
  Redraw the original graph with all the maximum flows (use the same two-number labels for edges ``f/c``). 
  Show the min-cut which prevents any further augmenting paths (either highlight with 
  another color, or simply list the partition of graph's vertices into two disjoint sets that describe the cut).