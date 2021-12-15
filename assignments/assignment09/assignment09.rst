Written Assignment 09
======================

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
|     :math:`Q = \text{\sc MinimumHeap(V)}` :math:`\;\;\;\;\;` *(Insert all vertices in a priority queue)*
|     **while** :math:`Q \neq \emptyset`:
|         :math:`u=\text{\sc ExtractMin}(Q)` :math:`\;\;\;\;\;` *(pick a vertex closest to the MST built so far)*
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
  the initial state before any edges have been added).
  
  =====================  ==============  ==============  ==============  ==============  ==============  ==============  ==============  ==============
  Phase                               A               B               C               D               E               F               G               H
  0 (initial state)           :math:`0`  :math:`\infty`  :math:`\infty`  :math:`\infty`  :math:`\infty`  :math:`\infty`  :math:`\infty`  :math:`\infty`
  =====================  ==============  ==============  ==============  ==============  ==============  ==============  ==============  ==============
  

**(C)**
  Summarize the result: Draw the MST obtained as the 
  result of Prim's algorithm, find its total weight. 
  

.. only:: Internal

  **Answer:**

  **(A)**
    As an example, consider Student ID with these last 3 digits: :math:`(a,b,c) = (7,8,9)`.
    Compute the values of :math:`x,y,z`:
    
    .. math::
    
      \left\{ \begin{array}{l}
      x = (b + 4)\ \text{mod}\ 10 = 2,\\
      y = (c + 4)\ \text{mod}\ 10 = 3,\\
      z = (a + b + c)\ \text{mod}\ 10 = 4.\\
      \end{array} \right.

    Let us draw the graph with edges (including those labeled by :math:`x = 2`, :math:`y=3`, :math:`z = 4`). 
        
    .. image:: figs-mst/mst-original-graph.png
       :width: 3in
  

  **(B)**
    We show the values of vertices in the priority queue (the value shows the minimum distance to some vertex in the tree built so 
    far using Prim's algorithm). The vertices that have been extracted (removed) from the queue show :math:`-` instead of the key value.
  
    =====================  ==============  ==============  ==============  ==============  ==============  ==============  ==============  ==============
    Phase                               A               B               C               D               E               F               G               H
    0 (initial state)           :math:`0`  :math:`\infty`  :math:`\infty`  :math:`\infty`  :math:`\infty`  :math:`\infty`  :math:`\infty`  :math:`\infty`
    1 (extract :math:`A`)       :math:`-`  :math:`\infty`       :math:`5`       :math:`8`       :math:`3`  :math:`\infty`  :math:`\infty`  :math:`\infty`
    2 (extract :math:`E`)       :math:`-`  :math:`\infty`       :math:`5`       :math:`1`       :math:`-`       :math:`6`       :math:`9`       :math:`6`
    3 (extract :math:`D`)       :math:`-`       :math:`7`       :math:`3`       :math:`-`       :math:`-`       :math:`6`       :math:`9`       :math:`6`
    4 (extract :math:`C`)       :math:`-`       :math:`3`       :math:`-`       :math:`-`       :math:`-`       :math:`6`       :math:`9`       :math:`6`
    5 (extract :math:`B`)       :math:`-`       :math:`-`       :math:`-`       :math:`-`       :math:`-`       :math:`4`       :math:`9`       :math:`6`
    6 (extract :math:`F`)       :math:`-`       :math:`-`       :math:`-`       :math:`-`       :math:`-`       :math:`-`       :math:`2`       :math:`2`
    7 (extract :math:`G`)       :math:`-`       :math:`-`       :math:`-`       :math:`-`       :math:`-`       :math:`-`       :math:`-`       :math:`2`
    8 (extract :math:`H`)       :math:`-`       :math:`-`       :math:`-`       :math:`-`       :math:`-`       :math:`-`       :math:`-`       :math:`-`
    =====================  ==============  ==============  ==============  ==============  ==============  ==============  ==============  ==============

    .. note::
      During Phase 7 there are two vertices of the same priority value (:math:`G` and :math:`H`). We select :math:`G` which is alphabetically earlier
      and add the edge :math:`(F,G)` to the MST. In this situation the order how edges :math:`(F,G)` and  :math:`(F,H)` does not matter much. 
      In some other graphs the choice of edges (for equal keys in the priority queue) can lead to major differences in subsequent steps -- and 
      there may exist multiple MSTs. 


  **(C)**
    Every time we extract a vertex from the priority queue in (B), we set its parent to the other end of the edge that was safe to add at this step. 
    Below is the picture of the resulting MST (tree edges shown bold and light-gray, all the other edges are shown as dashed).
  
    .. image:: figs-mst/mst-tree.png
       :width: 3in
    
  :math:`\square`