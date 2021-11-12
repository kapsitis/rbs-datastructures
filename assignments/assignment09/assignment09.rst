Written Assignment 09
======================

.. |_| unicode:: 0xA0 
   :trim:

Let :math:`G(V,E)` be an *undirected* graph. Let :math:`w:E\rightarrow{}\mathbf{Z}` 
be a function assigning integer weights to all the graph's edges and
let :math:`r` be the root vertex that will start to grow the minimum spanning tree (MST).
Every vertex :math:`v \in V` stores :math:`v.key` -- the sorting key for a prioirty queue of all vertices. 
A vertex also stores :math:`v.p` -- 
its "parent" (the parent vertex in the ultimate MST; it is assigned only once). 
Prim's algorithm to find the minimum spanning tree in :math:`G`
is given by the following pseudocode: 

| :math:`\text{\sc MstPrim}(G,w,r)`:
|     **for** **each** vertex :math:`u \in V`: 
|         :math:`u.key = \infty`
|         :math:`u.p = \text{\sc Null}`
|     :math:`r.d = 0`
|     :math:`Q = \text{\sc MinimumHeap(V)}` |_| |_| |_| |_| |_| |_| *(Insert all vertices in a priority queue)*
|     **while** :math:`Q \neq \emptyset`:
|         :math:`u=\text{\sc ExtractMin}(Q)` |_| |_| |_| |_| |_| |_| *(pick a vertex closest to the MST built so far)*
|         **for** **each** :math:`v \in \text{\sc Adj}(G,u)`:
|             **if** :math:`v \in Q` **and** :math:`w(u,v) < v.key`
|                 :math:`v.p = u`
|                 :math:`v.key = w(u,v)`



Denote the last three digits of your Student ID by :math:`a,b,c`.
Student ID often looks like this: :math:`\mathtt{201RDBabc}`, where
:math:`a,b,c` are digits. 
Compute three more digits :math:`x,y,z`:

.. math::

  \left\{ \begin{array}{l}
  x = (b + 4)\ \text{mod}\ 10\\
  y = (c + 4)\ \text{mod}\ 10\\
  z = (a + b + c)\ \text{mod}\ 10\\
  \end{array} \right.

In this task the input graph :math:`G = (V,E)` is given by its adjacency matrix: 

.. math::

  M_G = \left( \begin{array}{ccccccccc}
  0 & 7 & 4 & 3 & 0 & 7 & 0 & 7 & 0 \\
  7 & 0 & 0 & 0 & 0 & y & 5 & 0 & 6 \\
  4 & 0 & 0 & 0 & 0 & 0 & 2 & 0 & 6 \\
  3 & 0 & 0 & 0 & z & 5 & 0 & 0 & 0 \\
  0 & 0 & 0 & z & 0 & 2 & 8 & 0 & 0 \\
  7 & y & 0 & 5 & 2 & 0 & 0 & 0 & 3 \\
  0 & 5 & 2 & 0 & 8 & 0 & 0 & x & 0 \\
  7 & 0 & 0 & 0 & 0 & 0 & x & 0 & 0 \\
  0 & 6 & 6 & 0 & 0 & 3 & 0 & 0 & 0 \\
  \end{array} \right). 




**(A)**
  In your graph replace :math:`x,y,z` with your values 
  calculated from the Student ID. 
  Run Prim's algorithm about the shortest paths. 
  After each phase show the set of vertices of MST
  (those currently deleted from the MST), and
  also those values of :math:`v.key` and :math:`v.p`, 
  if they are modified during that phase. 	


**(B)**
  Summarize the result: Draw the MST obtained as the 
  result of Prim's algorithm, find its total weight. 