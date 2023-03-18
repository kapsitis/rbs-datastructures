Review Topics for Midterm and Final 
=====================================

**Asymptotic Growth Rate:**
  Comparing functions defined analytically. Comparing recurrent sequences. 
  Analyzing time complexity of algorithms from their pseudocode. 

  1. Analyzing functions and sequences

      A. Given an closed expression of a function, find its :math:`\Theta(g(n))` growth rate
         in its simplest form. 
      B. Compare two functions in terms of their asymptotic growth rate. 
      C. Given a recurrent sequence, define its asymptotic growth rate. 

  2. Analyzing computer code

      A. Use the assumptions about common data structures (lists, sets, dictionaries) in Python. 
      B. Express time complexity for a code snippet *from the inside out*.
      C. Memory leaks in C++ and Valgrind reports.

  3. Analyzing recursive code

      A. Write a recurrence to express time complexity of a recursive algorithm. 
      B. Solve recurrence using the Master's theorem.  

  4. Find Asymptotic Growth Rate for Other Complexity Measures

      A. Evaluate the space complexity for an algorithm. 
      B. Evaluate the amortized complexity, if some operation is applied many times. 
      C. Evaluate the number of comparisons needed for sorting, searching or ranking algorithms. 



**ADTs and Implmentations:**

  1. Define datastructures in terms of ADTs, compare implementation alternatives.

      A. Express dependent ADT operations in terms of simpler ADT operations. 
      B. Given a list/stack/queue algorithm pseudocode, find its time complexity.
      C. Given a problem description, implement the algorithm at ADT Level to implement it.
      D. Unit-tests to check the correctness of behavior of ADTs. 




**Lists, Stacks, Queues:** 


  1. Typical implementations for Lists, Stacks, Queues. 

      A. Given an algorithm pseudocode, draw the list state at a certain moment.

  2. Algorithms using Lists, Stacks or Queues.

      A. Write algorithms and estimate the time complexity of algorithms processing expressions.

**Tree-like Structrues:** 

  1. Tree Concepts, Traversals and Applications 

  2. Priority Queues and Heaps. 

  3. Backtracking algorithms. 

  



**N-ary Search Trees:** 

  1. Regular BSTs 

      A. Inserting, deleting and finding nodes. 
      B. Reason about the expected height of a BST, if you insert keys in random order 
         and related results.

  2. AVL Trees   

  3. 2-3 Trees and Red-Black Trees

  4. Create and Use Augmented Trees. *Ideally, the extra information 
     for any node can be computed in constant time -- using 
     other attributes of the node and its children*. 
     
      A. Consider different ways to augment trees ()
      B. Computing :math:`\text{\sc rank}(v)` -- how many nodes :math:`w`
         in the given tree satisfy the inequality :math:`w.key \leq v.key`. 
      C. Computing :math:`\text{\sc count}(a,b)` the information 


.. Lower bounds for sorting, if you have coins of different colors. 

**Sorting:** 

  1. The lower bound for sorting algorithms.

      A. Stirling's formula. 
      B. Counting comparisons in a decision tree. 

  2. Efficient sorting algorithms: 
  
      A. Mergesort, 
      B. Heapsort, 
      C. Quicksort, 
      D. Sorting in STL. 

  3. Sorting under special assumptions: 

      A. Radix sort. 
      B. Counting sort.

