Written Assignment 09
======================

.. |_| unicode:: 0xA0 
   :trim:

Let :math:`G(V,E)` be an *undirected* graph. Let :math:`w:E\rightarrow{}\mathbf{Z}` 
be a function assigning integer weights to all the graph's edges and
let :math:`r` be the root vertex that will start to grow the minimum spanning tree (MST).
Every vertex :math:`v \in V` stores :math:`v.key` -- the key for a priority queue (initially containing
all the vertices). 
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

  M_G = \left( \begin{array}{cccccccc}
  0 & 0 & 5 & 8 & y & 0 & 0 & 0 \\
  0 & 0 & 3 & 7 & 0 & z & 0 & 0 \\
  5 & 3 & 0 & 3 & 0 & 0 & 0 & 0 \\
  8 & 7 & 3 & 0 & 1 & 7 & 0 & 0 \\
  y & 0 & 0 & 1 & 0 & 6 & 9 & 6 \\
  0 & z & 0 & 7 & 6 & 0 & x & 2 \\
  0 & 0 & 0 & 0 & 9 & x & 0 & 7 \\
  0 & 0 & 0 & 0 & 6 & 2 & 7 & 0 \\
  \end{array} \right). 

**(A)**
  Draw the graph as a diagram with nodes and edges.
  Replace :math:`x,y,z` with values
  calculated from your Student ID.
  Label the vertices with letters
  :math:`A,B,C,D,E,F,G,H` (they correspond 
  to the consecutive rows and columns in the matrix).
  
  If you wish, you can use the following layout
  (edges are not shown, but the vertice positions allow
  to draw the edges without much intersection). 
  But you can use any other layout as well. 
  
  .. image:: figs-mst/mst-vertices.png
     :width: 3in


**(B)**
  Run Prim's algorithm to find MST using
  :math:`r = A` as the root.
  If you do not have time to redraw the graph many times, 
  just show the table with :math:`v.key` 
  values after each phase. 
  (No need to show :math:`v.p`, as the parents do not change
  and they are easy to find once you have the final rooted tree drawn.)
  The top of the table would look like this (it shows Phase 0 -- 
  the key values before any edges have been added).
  
  ======  =========  ==============  ==============  ==============  ==============  ==============  ==============  ==============
  Phase   A          B               C               D               E               F               G               H
  0       :math:`0`  :math:`\infty`  :math:`\infty`  :math:`\infty`  :math:`\infty`  :math:`\infty`  :math:`\infty`  :math:`\infty`
  ======  =========  ==============  ==============  ==============  ==============  ==============  ==============  ==============
  

**(C)**
  Summarize the result: Draw the MST obtained as the 
  result of Prim's algorithm, find its total weight. 