Midterm Exam 2
===============

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

.. note:: 
  Midterm 2 contains 5 questions.
  Questions written on paper should be photographed and uploaded as JPEG or PDF. 
  Question 5 should be submitted as C++ source file in a separate folder.


.. "2D" "3B" "4A" "5B" "6D"


.. 2.D. Estimate the time complexity of a tree operation given input data distribution.

**Question 1:**

  Alice sends messages to Bob using only eight voiced consonants from this alphabet:
  :math:`\{ B, D, G, J, N, R, V, Z \}`. Each consontant is encoded 
  as a sequence of bits (0s and 1s) using the binary tree shown below:
  
  .. figure:: figs/huffman-tree.png
     :width: 3in
     :alt: Binary Tree with codes
	 
     A Binary Tree used by Alice to encode 8 consonant letters.
  
  For example, ``VZJ`` is encoded as ``1110.11111.11110`` 
  (``V`` becomes ``1110``, ``Z``  becomes ``11111`` and
  ``J`` becomes ``11110``). Each code is obtained by 
  following the edges from the root to the respective leaf in this tree.
  
  **(A)**
    Show how Alice can encode the following 8-letter word:
    :math:`\mathtt{BRBDNGNG}`. How many bits does it use?
    (Please separate the codes of individual letters with dots for better readability.)
  
  **(B)** 
    In Alice's language the probabilities of letters are the following: 
	
    =====  =====  =====  =====  =====  =====  =====  =====	
    ``R``  ``N``  ``D``  ``G``  ``B``  ``V``  ``J``  ``Z``
    32%    28%    14%    11%    9%     4%     1%     1%
    =====  =====  =====  =====  =====  =====  =====  =====	

    Find the expected value of the total bits (0s and 1s) that she uses in order to send a random 10-letter word to Bob.
    (The letters in a random word are chosen independently according to the probabilities given above).




.. 3.B. Verify some properties of binary search trees assuming their element counts.

**Question 2:** 

  Some binary tree :math:`T` has exactly :math:`32` internal nodes.

  **(A)** 
    Can tree :math:`T` be a full binary tree? (In a full binary tree every node has either 
    two children or no children at all.)
    Can tree :math:`T` be a perfect binary tree? (In a perfect binary tree 
    all leaves have the same depth.)
	
  **(B)** 
    What is the largest and the smallest value for :math:`n` -- the total number of nodes in the 
    tree :math:`T`? Explain your estimates.
	
  **(C)** 
   What is the largest and the smallest value for :math:`h` -- the height of :math:`T`? 
   Explain your estimates.
 

.. 4.A. Use priority queue ADT to implement and analyze simple algorithms.

**Question 3:**
  
  Minimum Priority Queue has this ADT (Abstract Data Type): 
  
  =============================  ========================  =======================================================================
  `PQ.getEmpty()`                :math:`\Theta(1)`         // initialize ``PQ`` to an empty priority queue
  `void PQ.insert(E item)`       :math:`\Theta(\log_2 n)`  // insert ``item`` into the priority queue ``PQ``.
  `E PQ.min()`                   :math:`\Theta(1)`         // return an item with minimum key value, do not modify ``PQ``.
  `void PQ.removeMin()`          :math:`\Theta(\log_2 n)`  // remove an item with minimum key from ``PQ``
  `int PQ.size()`                :math:`\Theta(1)`         // return the number of items in the priority queue ``PQ``
  =============================  ========================  =======================================================================

  Every function in this ADT has its time complexity written in the 2nd column -- it corresponds to the heap implementation.
  
  Consider the following pseudocode. Denote the number of items in the original list ``L`` by :math:`n` 
  (assume that :math:`n \geq 10` and all items in this list have different keys). 
  
  | :math:`\text{\sc ProcessList}(L)`:
  |   `PQ.getEmpty()`
  |   **foreach** `item` **in** `L`:
  |     `PQ.insert(item)`
  |   **while** `PQ.size() > 5`: 
  |     `PQ.removeMin()`
  |   **return** `PQ.min()`

  **(A)**
    Describe in English what does the function :math:`\text{\sc ProcessList}(L)` return. 
	
  **(B)**
    Express the time complexity of this algorithm in Big-:math:`\Theta` notation: Find a
    function :math:`g(n)` such that the time complexity of :math:`\text{\sc ProcessList}(L)` is
    :math:`\Theta(g(n))`. 
	

.. 5.B.Use and analyze Merge sort.

**Question 4:**
  
  We have a 1-based array with 11 elements: :math:`A[1],\ldots,A[11]`. 
  We want to sort it efficiently. 
  Consider the following Merge sort pseudocode: 
  
  | :math:`\text{\sc MergeSort}(A,p,r)`:
  | :math:`1\;\;` **if** :math:`p < r`
  | :math:`2\;\;\;\;\;\;\;\;` :math:`q = \left\lfloor (p+r)/2 \right\rfloor`
  | :math:`3\;\;\;\;\;\;\;\;` :math:`\text{\sc MergeSort}(A,p,r)`
  | :math:`4\;\;\;\;\;\;\;\;` :math:`\text{\sc MergeSort}(A,q+1,r)`
  | :math:`5\;\;\;\;\;\;\;\;` :math:`\text{\sc Merge}(A,p,q,r)`
  
  Assume that initially you call this function as :math:`\text{\sc MergeSort(A,1,11)}`, 
  where :math:`p = 1` and :math:`r = 11` are the left and the right endpoint of the 
  array being sorted (it includes both ends). 
  
  What is the total number of calls to :math:`\text{\sc MergeSort}` for this array 
  (this includes the initial call as well as the 
  recursive calls on lines 3 and 4 of this pseudocode). 

.. 6.D. (C++ code) Use inheritance and virtual functions.

**Question 5:** 

  Complete the C++ program that converts a tree into a string using function 
  ``toString()``. A tree can be built from two types of objects: 
  objects of class ``Leaf`` and objects of class ``Internal``.
  They are both inherited from a common parent class ``Node``. 
  All nodes have attribute ``label``. 
  Moreover, ``Internal`` nodes have attribute ``children`` of
  type ``list<Node*>`` -- it is a list of pointers to the child nodes
  (either leaves or other internal nodes).
  
  .. literalinclude:: figs/virtual_functions.cpp

  
  A tree that is a leaf is converted to a string: the value of ``label``.
  A tree that is an internal node is converted to a string as the parent's label followed by 
  all the subtrees under that parent -- they are all separated by single spaces and 
  enclosed in parentheses.
  
  Here is the expected output from the program:
  
  .. code-block:: text
  
    AAA

    (AA BB CC)

    (A (B (C D E) (F G (H I J))) (K (L M)))
	
  In this task you can complete the functions ``toString()`` and possibly make other
  changes. You should not modify the method ``main()``; your code should preserve the 
  inheritance relations between ``Node``, ``Leaf`` and ``Internal``. 
  Solutions that use "hard-coded" output that does not depend on the 
  values and structures defined in ``main()`` will not be considered valid.
  
	



  