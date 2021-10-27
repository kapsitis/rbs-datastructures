Midterm Exam 2, October 28, 2021
=================================

.. 1. Write algorithms with List, Stack or Queue ADTs
.. 1A. Given a list/stack/queue algorithm pseudocode, find its time complexity.
.. 1B. Given an algorithm pseudocode, draw the list state at a certain moment.
.. 1C. Given a problem description, implement the algorithm at ADT Level to implement it.
.. 1D. Write algorithms and estimate the time complexity of algorithms processing expressions.

.. 2. Use properties of rooted, ordered trees, traverse their nodes
.. 2A. Given some tree properties and element counts, calculate or estimate other counts.
.. 2B. Use Tree ADT to implement some algorithms to manipulate trees.
.. 2C. Use tree traversal to solve related algorithmic problems.
.. 2D. Estimate the time complexity of a tree operation given input data distribution.

.. 3. Manipulate binary search trees (BST)
.. 3A. Perform insert and delete operations in arbitrary binary search tree. 
.. 3B. Verify some properties of binary search trees assuming their element counts.
.. 3C. Use binary trees to encode another structure such as a multiway tree.
.. 3D. Build AVL trees, perform rotations, run insert and delete operations.

.. 4. Use and analyze priority queues and heaps
.. 4A. Use priority queue ADT to implement and analyze simple algorithms.
.. 4B. Store binary trees into arrays.
.. 4C. Perform and analyze heap operations for insert and delete.
.. 4D. Use and analyze Heapsort.

.. 5. Use and analyze sorting algorithms
.. 5A. Use and analyze Selection sort, Insertion sort, Bubble sort algorithms.
.. 5B. Use and analyze Merge sort. 
.. 5C. Use and analyze Quicksort algorithms.
.. 5D. Use and analyze Radix sort and Counting sort.

.. 6. (C++ code) Use STL structures, implement custom inheritance and polymorphism
.. 6A. (C++ code) Use STL classes for lists, stacks, queues with iterators.
.. 6B. (C++ code) Use STL classes for tree-related operations. 
.. 6C. (C++ code) Use STL classes for priority queue operations.
.. 6D. (C++ code) Use inheritance and virtual functions. 
.. 6E. (C++ code) Use polymorphism and template classes or functions.


.. "6E" "4C" "5A" "2A" "3A"


.. 1A. Given a list/stack/queue algorithm pseudocode, find its time complexity.

.. **Question 0:**
..  Consider the following code (given a pseudocode - it erases elements that fall under a filter; then reverses the list.). 
..  Show what is the result if you run it on an example list. 
..  What is the time complexity.
.. 2A. Given some tree properties and element counts, calculate or estimate other counts.

*The last question should be submitted as the C++ source file in a separate folder.*

**Question 1:**

  Consider a tree :math:`T` with the following properties: 
  
  * :math:`T` has exactly :math:`12` internal nodes, 
  * Every internal node of :math:`T` has one or two children. 
  * The average number of children for an internal node is exactly :math:`1.5`. 
  * Tree :math:`T` is built from ``TNode`` structures:
  
  .. code-block:: cpp
  
    struct TNode { int info; TNode* left; TNode* right; };
  
  **(A)**
    What is the number of leaves in tree :math:`T`?

  **(B)**
    What is the number of ``NULL`` values among all the ``TNode.left`` and ``TNode.right`` pointers
    used to build the tree :math:`T`?
	
  **(C)**
    What is the largest and the smallest value of the height of the tree :math:`T`. 
    (Write your estimates for minimum height and maximum height, and explain why these
    estimates cannot be improved.)
	
  .. note::
    We define *height* of a tree as the number of edges to traverse on the path that connects its
    root with the deepmost leaf. (In particular, a tree with just the root node has height 0, 
    but a tree with the root and a single child leaf has height 1.) 
    


.. 3A. Perform insert and delete operations in arbitrary binary search tree. 

**Question 2:**

  .. image:: figs/bst-tree.png
     :width: 5in

  **(A)**
    Draw the Binary Search tree shown in figure after node :math:`21` is deleted. 
	
  **(B)**
    Draw the Binary Search tree obtained in (A) after node :math:`35` is deleted. 

  .. note::
    Deletion is done by replacing the node to be deleted by its inorder successor. 



.. 4D. Use and analyze Heapsort.

**Question 3B:** 
  An array of :math:`10` elements is used to initialize a minimum heap (as the first stage of 
  the Heap sort algorithm): 
  
  .. math::
  
    \{ 5, 3, 7, 10, 1, 2, 9, 8, 6, 4 \}

  Assume that the minimum heap is initialized in the most efficient way (inserting elements
  level by level -- starting from the bottom levels). 
  
  **(A)**
    How many levels will the heap tree have? (The root of the heap is considered :math:`L_0` -- level zero.
    the last level is denoted by :math:`L_{k-1}`. Just find the number :math:`k` for this array.)
  
  **(B)**
    Draw the intermediate states of the heap after each level is filled in. Represent the heap as a binary tree. 
    (If some level :math:`L_k` is only partially filled and contains less than :math:`2^k` nodes, 
    please draw all the nodes as little circles, but leave the unused nodes empty.)

  **(C)** 
    What is the total count of comparisons (:math:`a < b`) that is necessary to build the final
    minimum heap?


.. 5A. Use and analyze Selection sort, Insertion sort, Bubble sort algorithms.

**Question 4:**

  .. image:: figs/bubblesort.png
     :width: 4in

  The image shows Bubble sort algorithm for a 0-based array :math:`A[0]\ldots{}A[n-1]` of :math:`n` elements.

  **(A)** 
    How many comparisons (``A[i-1] > A[i]``) in this algorithm are used to sort the following array (where 
    :math:`A[0] = 9` and :math:`A[9] = 8`: 
	
	.. math::
	  
      \{ 9, 0, 1, 2, 3, 4, 5, 6, 7, 8 \}
	  
  **(B)**  
    How many comparisons (``A[i-1] > A[i]``) in this algorithm are used to sort the following array (where 
    :math:`A[0] = 1` and :math:`A[9] = 0`: 
	
	.. math::
	  
      \{ 1, 2, 3, 4, 5, 6, 7, 8, 9, 0 \}

.. 6E. (C++ code) Use polymorphism and template classes or functions.

**Question 5:** 
  Create a C++ program that inputs :math:`100` space-separated positive integers. 
  It should output the first :math:`5` largest of them (also separating them with spaces). 
  Use ``std::priority_queue`` to implement this.
  