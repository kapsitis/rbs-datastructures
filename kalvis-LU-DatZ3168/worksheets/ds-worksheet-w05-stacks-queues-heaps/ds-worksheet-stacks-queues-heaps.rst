Worksheet Week 05: Stacks, Queues, Priority Queues
======================================================

Introduction
--------------

Abstract data types (supported API methods to interact with a data structure) should be distinguished
from the implementation of the data structure (using C++ constructs like arrays, pointers,
custom objects etc.). Implemented data structures can support the 
API methods while preserving *representation invariant*. 
Representation invariant is some property or several properties that are preserved 
in a data structure -- as it performs the methods from the datastructure. 

For example, an array-based stack, if ``stack.length = 5``, 
then we should have :math:`0 \leq \text{size} \leq 5` at all times. 
Or a singly linked list should not have any loops and should end with a null pointer
and connect all the elements. 

Violating the representation invariant makes the data structure inconsistent and unusable. 
If an API method is run on an inconsistent data structure, there are no expectations
(program can crash, loop forever or produce any result). On the other hand, if an API 
method is called on a consistent state


Priority Queues
----------------

API methods: 

| :math:`\text{\sc PriorityQueue}()` -- create empty priority queue. 
| :math:`Q.\text{\sc insert}(item)` -- insert an item (with any key).
| :math:`Q.\text{\sc extractMin}()` -- remove and return the element with the minimum key.

Priority queues can be implemented in various ways: 

* Maintain an ordered list. 
* Maintain an unordered list (add elements in any order)
* Maintain a heap. 

Heap Implementation
^^^^^^^^^^^^^^^^^^^^

**Definition:** 
  A binary tree is called a *complete tree* if it has all layers filled in 
  (node counts in the layers :math:`1,2,4,8,\ldots`), except, perhaps, the last layer, 
  which is filled in from the left to the right. 

Complete trees are convenient to be stored as linear arrays. 

**Heaps:** 
  A binary tree storing nodes with numeric key values is called a *minimum heap*, if it satisfies 
  the following representation invariant: 

  * The binary tree is a complete binary tree. 
  * Each parent node in the tree has key that cannot be larger than the 



Problems
------------


**Problem 1: (Stack Implementation as Array):**
  Stack is implemented as an array. In our case the array has size :math:`n = 5`.
  Stack contains integer numbers; initially the array has
  the following content.
  
  .. image:: figs-stacks-queues-heaps/stack-structure.png
     :width: 2.2in
      
  Stack has the physical representation with :math:`\mathtt{length}=2`
  (the number of elements in the stack), :math:`\mathtt{size}=5`
  (maximal number of elements contained in the stack).
  We have the following fragment:
  
  .. code-block:: cpp
  
    pop();
    push(21);
    push(22);
    pop();
    push(23);
    push(24);
    pop();
    push(25);
    

  Draw the state of the array after every command.
  (Every ``push(elt)`` command assigns a new element into the element ``array[length]``,
  then increments ``length`` by :math:`1`.
  The command ``pop()`` does not modify the array, but decreases ``length`` by :math:`1`.
  
  If the command cannot be executed (``pop()`` on an empty stack; ``push(elt)`` on a full stack),
  then the stack structure does not change at all (``array`` or ``length`` are not modified).
  To help imagine the state of this stack, you can shade those cells that do not belong to the array.
  



**Problem 2 (Queue Implementation as a Circular Array):**
  A queue is implemented as an array with ``size`` elements; it has two
  extra variables ``front`` (pointer to the first element) and ``length``
  (the current number of elements in the queue). Current state is shown in the figure:
  

  .. image:: figs-stacks-queues-heaps/queue-structure.png
     :width: 2.3in
      

  Enumeration of array elements starts with :math:`0`. The array is filled in a circular
  fashion. The command ``enqueue(elt)`` inserts a new element at
  
  .. math::
    (\mathtt{front}+\mathtt{length})\;\mbox{mod}\;\mathtt{size},
    
  where "mod" means the remainder when dividing by ``size``. It also increments the
  ``length`` element.
  
  The command ``dequeue()`` does not change anything in the array, but increments
  ``front`` by :math:`1` and decreases :math:`length` by :math:`1`. Thus the queue becomes shorter by :math:`1`.
  

  .. code-block:: cpp
  
    dequeue();
    enqueue(21);
    dequeue();
    enqueue(22);
    enqueue(23);
    enqueue(24);
    dequeue();
    

  Show the state of the array after every command -- ``array, length, front``
  variables after every line. (Shade the unused cells.)
  


**Problem 3:**
  Denote :math:`a,b,c` to be the last :math:`3` digits of your Student ID, and compute the following numbers:
  
  * :math:`F = ((a+b+c)\;\operatorname{mod}\;3) + 2`
  * :math:`\mathtt{x1} = (a+b+c)\;\operatorname{mod}\;10`
  * :math:`\mathtt{x2} = ((a+b) \cdot 2)\;\operatorname{mod}\;10`
  * :math:`\mathtt{x3} = ((b+c) \cdot 3)\;\operatorname{mod}\;10`
  * :math:`\mathtt{x4} = ((c+a) \cdot 7)\;\operatorname{mod}\;10`
  

  The queue :math:`Q` is implemented as an array of size :math:`N=6`; its elements
  have indices from :math:`\{0,1,2,3,4,5\}`.
  
  Initially the queue parameters are these:
  
  * :math:`\mathtt{Q.front} = \mathtt{F}`,
  * :math:`\mathtt{Q.length} = 4`,
  * :math:`\mathtt{Q.size} = 6`,
  
  And the content of the array is the following:
  
  .. image:: figs-stacks-queues-heaps/midterm-queue-structure.png
     :width: 2in
      

  Somebody runs the following code on this queue:
  
  .. code-block:: cpp
  
    Q.enqueue(x1)
    Q.enqueue(x2)
    Q.dequeue()
    Q.dequeue()
    // show the state of Q
    Q.enqueue(x3)
    Q.enqueue(x4)
    Q.dequeue()
    // show the state of Q
    

  After Line 4 (and at the very end) show the current state of the queue :math:`\mathtt{Q}`.
  The state should display the content of the array and also the values of
  :math:`\mathtt{Q.front}` and :math:`\mathtt{Q.length}`.
  
  You can use shading, if it helps to visualize the array cells that are not
  currently used by your queue.
  

  .. note::
    Painting something gray is not required (since front/length indicate the state of your queue anyway).
    But painting cells gray may be helpful, if you want to visualize where your queue has the useful values
    (and what is some old garbage -- you can shade it over).
    


**Problem 4:**

  **(A)**
    Assume that heap is implemented as a
    0-based array (the root element is ``H[0]``), and the
    heap supports :math:`\text{\sc DeleteMin(H)}` operation that
    removes the minimum element (and returns the heap into
    consistent state).

    Find, if the heap property holds in the following array:

    .. math::

      H[0]=6, 17, 25, 20, 15, 26, 30, 22, 33, 31, 20.


    If it is not satisfied, find, which two keys
    you could swap in this array so that the heap property is satisfied again.
    Write the correct sequence of array :math:`H`.

  .. note::
    A *consistent state* in a minimum heap means that
    the key in parent does not exceed keys in left and right child.



  **(B)**
    Assume that heap is implemented as a
    0-based array (the root element is ``H[0]``), and the
    heap supports :math:`\text{\sc DeleteMax(H)}` operation that
    removes the maximum element.

    If the heap does not satisfy invariant (in a consistent
    max-heap, every parent
    should always be at least as big as both children), then show how to
    swap two nodes to make it correct.

    .. math::

     96, 67, 94, 10, 67, 68, 69,  9, 10, 11, 50, 67.


**Problem 5 (Insert into a min-heap):**
  Show what is the final state of a heap after you insert number :math:`6` into
  the following minimum-heap (represented as a zero-based array):

  .. math::

    9, 18, 28, 23, 20, 29, 33, 25, 36, 34, 23.


**Problem 6 (Delete maximum from a Max-Heap):**
  Show what is the final state of a heap after you remove the maximum from
  the following heap (represented as a zero-based array):

  .. math::

    96, 67, 94, 10, 67, 68, 69,  9, 10, 11, 50, 67.


**Problem 7 (Removing from Maximum Heap):**
  Here is an array for a Max-Heap:

  .. image:: figs-stacks-queues-heaps/heap-problem.png
     :width: 3in

  The image shows array used to store Maximum Heap
  (a data structure allowing inserts and removal of the maximum element).
  The array starts with the :math:`0`-th element
  (and any parent node in such tree should always be at least as big as
  any of its children).

  **(A)**
    Draw the initial heap based on this array.
    Heap should be drawn as a complete binary tree.

  **(B)**
    Run the command :math:`\text{\sc DeleteMax}(H)`
    on this initial heap. Draw the resulting binary tree (after the heap
    invariant is restored -- any parent node is
    at least as big as its children). Draw the binary tree image you get.

  **(C)**
    On the tree that you got in the previous step (B)
    run the command :math:`\text{\sc Insert}(H,x)`,
    where :math:`x = a+b+c` is the sum of the last three digits of your student ID.
    Draw the binary tree image you get.

  **(D)**
    Show the array for the binary tree you got in the previous step (C)
    (i.e. right after the :math:`\text{\sc DeleteMax}(H)` and :math:`\text{\sc Insert}(H,x)` commands
    have been executed).



**Problem 8:** 
  A *multiset* (or a *bag*) is any collection of items similar to a *set*, which can contain 
  multiple copies of the same item. For example, :math:`X = \{ 2,2,2,3,3,5 \}` is a multiset.
  The 2-quantile (also known as the *median*) for a multiset :math:`X = \{ x_1,x_2,\ldots,x_k \}` is the number :math:`m` satisfying 
  the following probability inequalities (where :math:`x_i` is a randomly picked element from the multiset :math:`X` -- each element is selected 
  with the same probability):
  
  .. math:: 
  
    P(x_i < m) \leq \frac{1}{2},\;\;\text{and}\;\; P(x_i \leq m) \geq \frac{1}{2}. 
	
  Suggest an efficient data structure to store "median-maintained multisets" :math:`X` containing integer numbers that support 
  the following operations: 
  
  **Insert:** 
    Add a new element :math:`x` to the multiset :math:`X`. 

  **ExtractMedian:**
    Remove and return the median from the multiset :math:`X`, if it belongs to :math:`X`. 

  **Median:** 
    Return the median from the multiset without removing it.
	
  **Size:** 
    Return the number of elements in the multiset.



.. note:: 
  In Python you can compute this flavor of median like this: 
  
  .. code-block:: python
  
    import pandas as pd
	a = pd.Series([1,2,3,4])
	a.quantile(0.5, 'lower')  # should return 2
	# statistics.median([1,2,3,4]) would be 2.5
	

**Problem 9:** 
  Run the Huffman algorithm to build prefix codes for a five-letter alphabet 
  :math:`\{ A, B, C, D, E, F \}`, where the respective frequencies are :math:`\{ 45, 13, 12, 16, 9, 5 \}`.
  
