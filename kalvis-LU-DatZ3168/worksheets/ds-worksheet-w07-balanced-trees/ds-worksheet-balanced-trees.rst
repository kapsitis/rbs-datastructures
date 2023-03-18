Worksheet, Week 07: Balanced Trees
=================================


AVL Trees
-----------------------------------------

Define a height of a node in a tree by induction: 

* Null trees (empty trees) have height :math:`-1`
* Leaves (single node trees) have height :math:`0`
* Any node :math:`v` has height :math:`h(v) = \max(h(v_{\text{left} + h(v_{\text{right})))+1`

AVL tree is such that each node :math:`v` 
is balanced: :math:`|h(v_{\text{left}) - h(v_{\text{right})| \leq 1` - the heights of its subtrees
do not differ by more than :math:`1`. 


**Problem 1:**
  Let :math:`T_n` be an AVL tree of height :math:`n` with the
  smallest possible number of nodes. For example :math:`|T_0| = 1`
  (just one node is an AVL tree of height :math:`0`); :math:`|T_1| = 2`
  (a root with one child only is an AVL tree of height :math:`1` of the smallest size) and so on.

  **(A)**
    Draw example AVL trees :math:`T_2`, :math:`T_3`, :math:`T_4`.

  **(B)**
    Denote the smallest 
    Suggest a method how to  :math:`|T_n|`
    (recurrent formula expresses the number :math:`|T_n|` using
    the previous numbers :math:`|T_k|` with :math:`k < n`).




.. many rotations: https://cs.stackexchange.com/questions/97975/how-many-rotations-after-avl-insertion-and-deletion
.. https://stackoverflow.com/questions/13367981/what-is-the-minimum-sized-avl-tree-where-a-deletion-causes-2-rotations


**Problem 2:**
  Assume that a Binary Search Tree :math:`T` is created by inserting the following keys into an empty tree: 
  :math:`[39, 20, 65, 11, 29, 50, 26]`. 

  **(A)**
    Do the following actions on this tree one after another: 
    :math:`T.insert(22)`, :math:`T.insert(60)`, :math:`T.delete(11)`. 

  **(B)**
    Suggest a sequence of inserts/deletes for the original tree :math;`T` (with :math:`7` nodes) so that 
    the last delete operation in that sequence causes two rotations. 
  


(2,4) Trees
----------------------------







Red-Black Trees
-----------------------------

**Definition:**
  A tree is named a *Red-Black Tree*, if it is a Binary Search Tree,
  every node is either red or black (extra boolean flag stores this color) and
  it satisfies these *red-black invariants*:

  Root property
    The root is black.

  External property
    Every leaf (a node with NULL key) is also black.

  Internal property
    If a node is red, then both its children are black.

  Depth property
    For each node, all simple paths from the node to descendant leaves contain the
    same number of black nodes.


  .. note::
    See Figure :ref:`red-black-tree`; leaves with NIL keys have
    black-height equal to :math:`0`. As we move to the root, we increment
    the black-height :math:`h_\text{black}` whenever the path crosses some black node.
    The Depth property guarantees that each internal node gets the same black-height, no matter
    which path from a leaf to a root we choose.



**Problem 5:**

  .. _red-black-tree:
  .. figure:: figs-search-trees/red-black-tree.png
     :width: 5in

     Sample Red-Black Tree


  **(A)**
    Compute the following three key values (:math:`u`, :math:`v`, and :math:`w`):

    .. math::

      \left\{ \begin{array}{l}
      u = 3(a+b)+2\\
      v = 3(b+c)+1\\
      w = 3(c+a)\\
      \end{array} \right.

    Here :math:`a,b,c` are the last :math:`3` digits of your Student ID.

    Verify the "black height" of every node in the graph -- all NULL leaves have black height equal to zero.
    Any other node has black height equal to the number of black nodes that are on some descendant path.
    (According to the depth property -- the black height of any node should not depend on the path to the leaf
    we chose.)


  **(B)**
    Show how the tree looks after the nodes :math:`u`, :math:`v` and :math:`w` (in this order)
    are inserted in the Red-Black Tree shown in Figure :ref:`red-black-tree`.

    If any of the values :math:`u,v,w` coincide with existing nodes, they
    should not be inserted. (Red-Black trees and BSTs in general can handle duplicates; but here
    we assume that it stores a map/set with unique keys.)

    Show the intermediate steps -- the tree after each successive inserted node.
    Clearly show, which are the red/black vertices in the submitted answers.


  .. note::

    Check that your inserts preserve the BST order invariant (along with all the Red-Black
    tree invariants). Secondly, try to follow the standard algorithm when inserting new nodes
    (still, preserving the invariants is more important).










