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
  :math:`\{ \mathtt{B}, \mathtt{D}, \mathtt{G}, \mathtt{J}, \mathtt{N}, \mathtt{R}, \mathtt{V}, \mathtt{Z} \}`. Each consontant is encoded 
  as a sequence of bits (0s and 1s) using the binary tree shown below:
  
  .. figure:: figs/huffman-tree.png
     :width: 3in
     :alt: Binary Tree with codes
	 
     A Binary Tree used by Alice to encode 8 consonant letters.
  
  For example, :math:`\mathtt{VZJ}` is encoded as ``1110.11111.11110`` 
  (:math:`\mathtt{V}` becomes :math:`\mathtt{1110}`, :math:`\mathtt{Z}`  
  becomes :math:`\mathtt{11111}` and
  :math:`\mathtt{J}` becomes :math:`\mathtt{11110}`). Each code is obtained by 
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

    Find the expected value of the total number of bits (0s and 1s) that she uses in order to send a random 10-letter word to Bob.
    (The letters in a random word are chosen independently according to the probabilities given above).

.. only:: Internal

  **Answer:**
    
  **(A)**
    :math:`\mathtt{BRBDNGNG}` becomes the following sequence of bits:
	
    .. math::
	
      \mathtt{110.00.110.100.01.101.01.101}
	
    The total length of this sequence is 21 bits (not counting the separating dots). 
    It is indeed sufficient to send just this sequence: :math:`\mathtt{110001101000110101101}`
    for Bob to be able to decode it.
	
    .. note::
      Even without the separating dots this sequence can be deciphered: Every time we start 
      at the root of the tree and see where it finishes. For example, the sequence 
      :math:`110` ends with a leaf denoting letter "B" (it cannot be continued as 
      the code :math:`110` is not a prefix for any other letter). 
      Such codes are named *prefix codes* and the method to build an efficient 
      prefix tree is called *Huffman coding*. 



  **(B)** 
    Each of the letters :math:`a` has a fixed-length code; let us denote it by :math:`\ell(a)`. 
    Let :math:`X` be a random variable that shows the number of bits used to encode a *single* letter
    from that alphabet of 8 letters. We can find :math:`E(X)` by adding code lengths multiplied 
    by letter probabilities: 
	
    .. math::

      \begin{array}{lcl}
      E(X) & = & P(\mathtt{R}) \cdot \ell(\mathtt{R}) + P(\mathtt{N}) \cdot \ell(\mathtt{N}) + 
      P(\mathtt{D}) \cdot \ell(\mathtt{D}) + P(\mathtt{G}) \cdot \ell(\mathtt{G}) + \\      
      & + & P(\mathtt{B}) \cdot \ell(\mathtt{B}) + P(\mathtt{V}) \cdot \ell(\mathtt{V}) + 
      P(\mathtt{J}) \cdot \ell(\mathtt{J}) + P(\mathtt{Z}) \cdot \ell(\mathtt{Z}) = \\
      & = & 0.32 \cdot 2 + 0.28 \cdot 2 + 0.14 \cdot 3 + 0.11 \cdot 3 + 0.09 \cdot 3 + 0.04 \cdot 4 + 0.01 \cdot 5 + 0.01 \cdot 5 = \\
      & = & 2.48 \\
      \end{array}
	  
	
    The expected value for encoding :math:`10` letters is ten times larger: :math:`24.8`. 	
	
  :math:`\square`



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
   

.. only:: Internal

  **Answer:**
  
  **(A)** 
    The tree can be a full binary tree. Consider the following construction: first create 
    the simplest full binary tree only containing one node (it is its root, 
    but it is also a leaf). Every time some leaf gets two children, it becomes an internal node and there are two new
    leaves -- in total the tree gains one internal node and one leaf node. So, the number of leaves is always 
    larger than the number of internal nodes (by exactly one). So a tree with :math:`32` internal nodes
    would have exactly :math:`33` leaves.
	
    No tree with :math:`32` internal nodes can be a perfect binary tree. In perfect trees the number 
    of internal nodes can be :math:`0` or :math:`1`, or :math:`3`, or :math:`7`, and so on. 
    In general, a perfect tree of height :math:`H` would have exactly :math:`2^H - 1` internal nodes
    (and :math:`2^H` leaves). But :math:`32` cannot be represented as :math:`2^H-1` for any integer :math:`H`.
	
  **(B)** 
    If a tree has :math:`i` internal nodes, then it can have up to :math:`i+1` leaves (it has exactly 
    :math:`i+1` leaves, if it is a full tree -- see explanation in the above item). 
    On the other hand, any tree with :math:`i` internal nodes should have at least one leaf -- the node
    where parent-child relationships end. A tree can have exactly one leaf (if any internal node has exactly 
    one child -- so all the nodes make a long chain with :math:`i` internal nodes and one leaf). 
	
    In case if :math:`i =32` we get the maximum number of nodes :math:`n = i + (i+1) = 32 + 33 = 65`. 
    And the minimum number of nodes is :math:`i+1 = 33`. 
	
  **(C)**
    Consider a perfect tree with all leaves at the depth :math:`5`. It would have :math:`2^5 = 32` leaves, 
    but just :math:`31` internal nodes. To create one more internal node we must have at least two leaves at
    the depth :math:`6`, so the smallest value of :math:`h` is :math:`h=6`. 

    On the other hand, the very skinny tree -- just a chain of vertices with one leaf at the end -- would have
    height :math:`h = 32`. (One cannot get a taller tree, since there must be at least one vertex at every 
    depth; one cannot skip levels.) 	
	
	
  :math:`\square`
	
 

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
	

.. only:: Internal

  **Answer:** 
  
  **(A)** 
    The algorithm keeps removing items until :math:`PQ.size()` ``==`` :math:`5`.
    This means that only the five largest items remain in the priority queue.
    After that we return the minimum of the remaining elements. 
	
    For this reason the function :math:`\text{\sc ProcessList}(L)` will return 
    the 5th largest element of the list :math:`L`.
	
  **(B)**
    For large values of :math:`n` there will be :math:`n-5` operations :math:`PQ.removeMin()`. 
    Each operation takes :math:`O(\log_2 n)` time. 
    Therefore the total time of this algorithm is :math:`O(n \log_2 n)`. Big-O notation is 
    the upper estimate.
	
    Let us show that also the lower estimate (Big-Omega notation) is :math:`\Omega(n \log_2 n)`. 	
    One could argue that as the queue becomes shorter the :math:`removeMin()` will gradually become 
    faster. But this does not change the lower estimate of time complexity, as there will be 
    at least one half of the :math:`removeMin()` calls -- namely, :math:`n/2` calls; 
    and every one will operate on a heap of size at least :math:`n/2`, and
    its logarithm is :math:`\log_2 (n/2) = 	\log_2 n - 1`. 
    Product of :math:`n/2` and :math:`(\log_2 n - 1)` is :math:`\Omega(n \log_2 n)`.
	
    Since both estimates are the same, the complexity of algorithm is :math:`\Theta(n \log_2 n)`. 
    

  :math:`\square`

	

.. 5.B.Use and analyze Merge sort.

**Question 4:**
  
  We have a 1-based array with 11 elements: :math:`A[1],\ldots,A[11]`. 
  We want to sort it efficiently. 
  Consider the following Merge sort pseudocode: 
  
  | :math:`\text{\sc MergeSort}(A,p,r)`:
  | :math:`1\;\;` **if** :math:`p < r`
  | :math:`2\;\;\;\;\;\;\;\;` :math:`q = \left\lfloor (p+r)/2 \right\rfloor`
  | :math:`3\;\;\;\;\;\;\;\;` :math:`\text{\sc MergeSort}(A,p,q)`
  | :math:`4\;\;\;\;\;\;\;\;` :math:`\text{\sc MergeSort}(A,q+1,r)`
  | :math:`5\;\;\;\;\;\;\;\;` :math:`\text{\sc Merge}(A,p,q,r)`
  
  Assume that initially you call this function as :math:`\text{\sc MergeSort(A,1,11)}`, 
  where :math:`p = 1` and :math:`r = 11` are the left and the right endpoint of the 
  array being sorted (it includes both ends). 
  
  What is the total number of calls to :math:`\text{\sc MergeSort}` for this array 
  (this includes the initial call as well as the 
  recursive calls on lines 3 and 4 of this pseudocode). 
  
  
  
.. only:: Internal

  **Answer:**
  
  .. image:: figs/mergesort-calls.png
     :width: 4in
	 
  The recursive calls of :math:`\text{\sc MergeSort}` are shown in the figure -- 
  just the parameters :math:`p,r` for each call. 
  For example, :math:`\text{\sc MergeSort}(A,1,11)` computes :math:`q = \lfloor (1+11)/2 \rfloor = 6`, 
  and causes two more calls to :math:`\text{\sc MergeSort}(A,1,6)` and :math:`\text{\sc MergeSort}(A,7,11)`
  respectively. On the other hand, if :math:`p = r`, then the recursive calls do not happen (one-element 
  list is already sorted). So there are exactly :math:`11` external nodes (leaves) in the 
  recursion tree. 
  
  Since the tree of calls is full, it also has :math:`10` internal nodes (shown pink in the picture).
  The total number of these nodes is :math:`10 + 11 = 21`. 
  
  :math:`\square`
  
  

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
  
.. only:: Internal

  **Answer:**
  
  A possible solution to this task is shown in the code below:

  .. literalinclude:: figs/virtual_functions_solved.cpp

  Make sure that you declare ``toString()`` function in the superclass ``Node`` as 
  virtual. Also -- it may be convenient to use ``stringstream`` class to 
  accumulate output (and only at the very end convert it to a C++ ``string`` object). 
  Another alternative would be -- concatenate many strings in the function ``Internal::toString()``.
  

  