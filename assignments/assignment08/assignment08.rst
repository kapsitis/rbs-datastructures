Written Assignment 08
=====================

.. |_| unicode:: 0xA0 
   :trim:


Let :math:`G(V,E)` be a directed graph. Let :math:`w:E\rightarrow{}\mathbf{Z}` 
be a function assigning integer weights to all the graph's edges and let :math:`s \in V` be
the source vertex.
Every vertex :math:`v \in V` stores :math:`v.d` -- the current estimate of 
the distance from the source. A vertex also stores :math:`v.p` --
its "parent" (the last vertex on the shortest path before reaching :math:`v`). 
Bellman-Ford algorithm to find the minimum distance from :math:`s` to all the other 
vertices is given by the following pseudocode: 

| :math:`\text{\sc BellmanFord}(G,w,s)`:
|     **for** **each** vertex :math:`v \in V`: |_| |_| |_| |_| |_| |_| *(initialize vertices to run shortest paths)*
|         :math:`v.d = \infty`
|         :math:`v.p = \text{\sc Null}`
|     :math:`s.d = 0` |_| |_| |_| |_| |_| |_| *(the distance from source vertex to itself is 0)*
|     **for** :math:`i=1` **to** :math:`|V|-1` |_| |_| |_| |_| |_| |_| *(repeat* :math:`|V|-1` *times)*
|         **for** **each** edge :math:`(u,v) \in E`
|             **if** :math:`v.d > u.d + w(u,v)`: |_| |_| |_| |_| |_| |_| *(relax an edge, if necessary)*
|                 :math:`v.d = u.d + w(u,v)`
|                 :math:`v.p = u`



.. figure:: figs-shortest-paths/bellman-ford-graph.png
   :width: 2.5in
   :alt: Directed Graph
	 
   A directed graph for Bellman-Ford Algorithm


In this task the input graph is shown in Fig.1. 

**(A)**
  In your graph use the vertex :math:`s=v_0` as the *source vertex* 
  for Bellman-Ford algorithm.
  Create a table showing the changes
  to all the distances to the vertices of the given graph every time a successful edge
  relaxing happens and some distance is reduced.
  You should run :math:`n-1` phases of the Bellman-Ford algorithm
  (where :math:`n` is the number of vertices). You can also stop earlier, if 
  no further edge relaxations can happen.
  
  .. note::
    Please make sure to release the edges in the lexicographical order. 
    For example, in a single phase the edge :math:`(v_1,v_4)` is
    relaxed before the edge :math:`(v_2,v_1)`, since 
    :math:`v_1` precedes :math:`v_2`. 
	
	


**(B)**
  Summarize the result: For each vertex
  tell what is its minimum distance from the source. 
  Also tell what is the shortest path how to get there. 
  
**(C)**
  Does the input graph contain negative cycles?
  Justify your answer.


.. If w(v4,v2)=-6 and not -5, then there is a negative loop.
.. v4  (-6)  v2  (1)  v3  (-4)  v5  (5)  v1  (3)  v4

