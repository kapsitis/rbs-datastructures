Worksheet 06: Search Trees
=================================


Concepts and Facts
-----------------------

**Definition:**
  A tree is named *Binary Search Tree* (BST) if the nodes satisfy the *order invariant*:
  Let :math:`x` be a node in a binary search tree. If :math:`y` is a node in the left subtree
  of :math:`x`, then :math:`y.key \leq x.key`. If :math:`z` is a node in the right subtree of :math:`x`, then
  :math:`z.key \geq x.key`.

**Definition:** 
  In a binary tree, the *inorder predecessor* of a node :math:`v` is a node :math:`u` 
  iff :math:`v` directly follows :math:`u` in the inorder traversal of the nodes.   
  Similarly, the *inorder successor* of a node :math:`v` is :math:`w` iff 
  :math:`w` directly follows :math:`v` in the inorder traversal. 

To delete an internal node from a BST (having both left and right children), 
you can replace it either by the inorder predecessor or the inorder successor. 


**Definition:** 
  The *height* of a node in a tree is defined by induction: 

  * Null trees (empty trees) have height :math:`-1`
  * Leaves (single node trees) have height :math:`0`
  * Any node :math:`v` has height :math:`h(v) = \max(h(v_{\text{left}}), h(v_{\text{right}}))+1`
  
**Definition:** 
  A binary search tree is called  an *AVL tree* iff each node :math:`v` is balanced. Namely, 
  the heights of both its subtrees do not differ by more than :math:`1`. 

  .. math:: 
  
    |h(v_{\text{left}}) - h(v_{\text{right}})| \leq 1

To see, if a tree is an AVL tree (the representation invariant must be preserved even 
after we insert or delete something!) we need to store the balance inside the tree node. 
Such additional information is called graph/tree node augmentation. 
(Augmentations are used by many algorithms and data structures. 
AVL trees needing the height is just one example.)




Problems 
---------

.. multiway trees encoded as binary trees
.. traversal order
..  https://www.geeksforgeeks.org/iterative-postorder-traversal-using-stack/


.. _search-trees-P1:

**Problem 1:** 
  Even binary trees that are not complete can be represented as arrays -- their nodes written out 
  layer by layer just like a complete tree in a heap. If any node in the tree is missing, 
  it is replaced by
  :math:`\Lambda`. The last non-empty node in the tree is
  the last element of the array.  
  Draw the trees corresponding to the following arrays (here :math:`a,b,c` are variable letters stored in the nodes).
  Distinguish the left and right children clearly.   
  
  **(A)**
    :math:`\mathtt{int\;a[\,]\;=\;\{1,2,3,7,\Lambda,5\}};`
	
  **(B)**
    :math:`\mathtt{int\;a[\,]\;=\;\{1, 2, 4, a, \Lambda, \Lambda, 6, b, \Lambda, \Lambda, \Lambda, \Lambda, \Lambda, \Lambda, c\};}`
    
  **(C)** 
    Write a  pseudocode to check, if the input array represents a binary tree (return True), or it is 
    inconsistent (for example, there are non-empty children under some :math:`\Lambda`).

  **(D)** 
	Write a pseudocode to count the internal nodes and the leaves, if you receive an array as an input. 

  **(E)**
  	Write a pseudocode to list the vertices of this tree in the post-order traversal order.



.. only:: Internal 

  **Answer:** 
  
  **(A)**

    .. image:: figs-search-trees/example-binary-tree.png
       :width: 2in
      
  :math:`\square`
  

.. _search-trees-P2: 
  
**Problem 2:**   
  Non-binary ordered trees  can be encoded as binary trees (using a bijective encoding function). 
  See `<https://bit.ly/3khnC0p>`_ for details.
  (If in a general tree the node :math:`w` is the first child of :math:`v`, 
  then in the corresponding binary tree :math:`w` becomes the *left child* of :math:`v`. 
  If :math:`w` is the sibling to the right of :math:`v`, then in the corresponding binary tree 
  :math:`w` is the *right child* of :math:`v`.)
  In this problem we use *bracket representations* for all trees (see `<https://bit.ly/425tzVa>`_).
  
  
  **(A)**
    Consider the following general tree: :math:`\mathtt{A (B (E) (F) (G)) (C) (D (H) (I) (J))}`. 
	
	Draw this multiway/general tree. Encode it as the binary tree and draw it. 
	
  **(B)** 
    :math:`\mathtt{A (B (E () (F (J () (K)) ())) (C () (D (G () (H (L (N) (M)) (I)) ()))) ()}`.

    Given the binary tree, restore the original general tree. 


  **(C)**
    Consider the binary tree from (B); list its nodes in their in-order DFS traversal order.


  **(D)**
    What is the depth of the node :math:`N` (defined above) in the new (general) tree?



  
.. only:: Internal 
  
  **Answer:** 
  
  **(A)**
    The general tree is given on Figure :ref:`general-tree-no-color`.

    .. _general-tree-no-color:
    .. figure:: figs-search-trees/general-tree-no-color.png
       :width: 2in

       Multiway Tree

  
    **Encoding Step 1**
      Redraw edges (only connect each node with its first child and also to
      the sibling to the right). To see clearly which edges will be left-going, and
      which are right-going, can color them differently. See
      Figure :ref:`colored-binary-tree1-reordered`.


    .. _colored-binary-tree1-reordered:
    .. figure:: figs-search-trees/colored-binary-tree1-reordered.png
       :width: 2in

       Tree with Horizontal Edges



    **Encoding Step 2**
      Adjust the levels in the new binary tree so that it takes
      a more conventional look (left children to the left, right children to the right).
      See Figure :ref:`colored-binary-tree1`.


    .. _colored-binary-tree1:
    .. figure:: figs-search-trees/colored-binary-tree1.png
       :width: 1.5in

       Encoded Binary Tree
  
  **(B)**
    The binary tree looks like this: 


    .. _binary-tree-problem:
    .. figure:: figs-search-trees/binary-tree-problem.png
       :width: 1.5in

       Binary tree for Question 6.1.1
  
	Restored tree can be obtained, if one colors the edges and 
	turns the left children into first children, and the right children 
	to siblings.
  
  .. note::  
    See `Encoding general trees as binary trees <https://en.wikipedia.org/wiki/Binary_tree#Encoding_general_trees_as_binary_trees>`_
    or `<https://bit.ly/3kdyg8n>`_.
  
  
  
  :math:`\square`
  



.. _search-trees-P3:

**Problem 3:**
  Let :math:`B_n` denote how many different BSTs for :math:`n` different keys there exist (all the trees should have correct order invariant).
  We have :math:`B_1 = 1` (one node only makes one tree). And :math:`B_2 = 2`.
  
  Draw all the binary search trees to store numbers :math:`\{1,2,3 \}`
  and also the numbers :math:`\{ 1,2,3,4 \}`. 
  
  Find the values :math:`B_3` and :math:`B_4` (the number of binary search trees).


**Problem 7:**
  Consider the binary tree shown below.

  .. image:: figs-search-trees/bst-search.png
     :width: 2in

  Every key in this tree is being searched with the same probability.
  Find the expected number of pointers that are followed as we search for a random key in this tree.
  (For example, searching the key at the root means following :math:`1` pointer, searching the key that is a child
  of the root means following :math:`2` pointers and so on.)


.. _search-trees-P4:

**Problem 4:**
  Consider the following Binary Search Tree (BST). 
  
  .. image:: figs-search-trees/binary-search-tree.png
     :width: 2in

  Let :math:`a,b` be the first two digits of your Student ID. Compute the following numbers: 
  
  .. math:: 
  
    \begin{array}{l}
    X = 2a, \\
    Y = 20+b, \\
    Z = 3b, \\
    S = b, \\
    T = 2(a+b) \;\text{mod}\; 40 \\
    U = (a+b) \;\text{mod}\; 10\\
	\end{array}
	
  Run the following commands on this BST (and draw the intermediate trees whenever there is the "show" command): 

  | :math:`BST.\text{\sc insert}(X)`
  | :math:`BST.\text{\sc insert}(Y)`
  | :math:`BST.\text{\sc delete}(20)`
  | :math:`BST.\text{\sc show}()`
  | :math:`BST.\text{\sc insert}(Z)`
  | :math:`BST.\text{\sc insert}(S)`
  | :math:`BST.\text{\sc delete}(13)`
  | :math:`BST.\text{\sc show}()`
  | :math:`BST.\text{\sc insert}(T)`
  | :math:`BST.\text{\sc insert}(U)`
  | :math:`BST.\text{\sc delete}(X)`
  | :math:`BST.\text{\sc show}()`
  
  Ignore a command, if it asks to insert a key that already exists or deletes 
  a key that does not exist. 


.. _search-trees-P5:

**Question 5:**
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
    


.. _search-trees-P6:

**Problem 6:**
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



.. many rotations: https://cs.stackexchange.com/questions/97975/how-many-rotations-after-avl-insertion-and-deletion
.. https://stackoverflow.com/questions/13367981/what-is-the-minimum-sized-avl-tree-where-a-deletion-causes-2-rotations



.. _search-trees-P7:

**Problem 7:**
  Assume that a Binary Search Tree :math:`T` is created by inserting the following keys into an empty tree: 
  :math:`[39, 20, 65, 11, 29, 50, 26]` (in the given order). 

  **(A)**
    Do the following actions on this tree one after another: 
    :math:`T.\text{\sc insert}(22)`, :math:`T.\text{\sc insert}(60)`, :math:`T.\text{\sc delete}(11)`. 

  **(B)**
    Suggest a sequence of inserts/deletes for the original tree :math;`T` (with :math:`7` nodes) so that 
    the last delete operation in that sequence causes two rotations. 
