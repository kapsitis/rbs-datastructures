Worksheet Week 05: Stacks, Queues, Priority Queues
======================================================




Problems
------------


**Problem 1: (Stack Implementation as Array):**
  Stack is implemented as an array. In our case the array has size :math:`n = 5`.
  Stack contains integer numbers; initially the array has
  the following content.
  
  .. image:: figs-stacks-and-queues/stack-structure.png
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
  

  .. image:: figs-stacks-and-queues/queue-structure.png
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
  


**Problemm 3:**
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
  
  .. image:: figs-stacks-and-queues/midterm-queue-structure.png
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

  .. image:: figs-trees-and-heaps/heap-problem.png
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
    