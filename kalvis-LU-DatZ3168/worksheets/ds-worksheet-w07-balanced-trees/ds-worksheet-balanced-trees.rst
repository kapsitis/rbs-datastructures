Worksheet, Week 07: Balanced Trees
=================================


AVL Trees
-----------------------------------------

**Question 1:**
  Let :math:`T_n` be an AVL tree of height :math:`n` with the
  smallest possible number of nodes. For example :math:`|T_0| = 1`
  (just one node is an AVL tree of height :math:`0`); :math:`|T_1| = 2`
  (a root with one child only is an AVL tree of height :math:`1`) and so on.

  **(A)**
    Draw AVL trees :math:`T_2`, :math:`T_3`, :math:`T_4` and :math:`T_5`.

  **(B)**
    Write a recurrence to find the number of nodes :math:`|T_n|`
    (recurrent formula expresses the number :math:`|T_n|` using
    the previous numbers :math:`|T_k|` with :math:`k < n`).


**Problem 2:**
  Let :math:`T` be some (unknown) BST tree that also satisfied the AVL balancing requirement.
  After :math:`k` nodes were inserted (without any re-balancing actions) the tree :math:`T'` now looks as
  in the image below.

  .. image:: figs-search-trees/tree-for-rotations.png
     :width: 3in

  **(A)**
    Find the smallest value of :math:`k` -- the nodes that were inserted into the original :math:`T`
    to get :math:`T'`.

  **(B)**
    Show the tree after :math:`\text{\sc LeftRotate}(T',x)` -- the left rotation around the node :math:`x`.
    Is the resulting tree an AVL tree now?




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



**Question 6.6.1 (Insert Nodes in a Red-Black Tree):**

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







**Question 6.1.2 (Binary Trees):**

  Define a new integer number :math:`N \in \{0,1,2,\ldots,9 \}` from the digits of your Student ID:

  .. math::

    N \;=\; (a + b) \;\text{mod}\; 10.


  **(A)**
    Redraw the binary tree in Figure;
    replace letters :math:`a,b` with your values. We denote this tree by :math:`B`.

  **(B)**
    List all the nodes of :math:`B` in their in-order DFS traversal order.

  **(C)**
    Draw a general tree (denoted by :math:`G`) that is obtained
    by decoding the tree :math:`B`.
    See `Encoding general trees as binary trees <https://en.wikipedia.org/wiki/Binary_tree#Encoding_general_trees_as_binary_trees>`_
    or `<https://bit.ly/3kdyg8n>`_.

  **(D)**
    What is the depth of the node with number :math:`N` (defined above) in the new tree :math:`G`?


  .. figure:: figs-search-trees/heptagonal-nodes.png
     :width: 3in
     :alt: Binary tree

     Binary tree :math:`B` for inorder traversal and converting to a general tree :math:`G`




