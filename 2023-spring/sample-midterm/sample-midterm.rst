Sample Midterm
================

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



**Problem 2 (Tree for Rotations):**
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