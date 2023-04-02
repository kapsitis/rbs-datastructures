Worksheet 03: ADTs and Implementations
=============================================

An abstract data type (ADTs) provide standard names for 
operations to interact with a certain data structure. 
ADTs should be distinguished
from the implementation of the data structure -- the same 
ADT operations can be supported in multiple ways with 
programming constructs like arrays, pointers, custom objects etc.
Abstract Data Types (just as any other API interfaces) let us ignore 
implementation details when using them in other algorithms. 



Concepts and Facts
----------------------

**Definition:** 
  A data container :math:`C` that stores items imposes *extrinsic order* iff this 
  container ensures predictable order of how they can be visited or retrieved. 
  Namely, for any two elements :math:`a,b \in C`, either that :math:`a` *preceeds* :math:`b`
  or :math:`a` *succeeds* :math:`b` in this container. 


**Example:** 
  Items stored in a linked list or in an array can be visited in a predictable order 
  such as :math:`A[0], A[1], \ldots`. 
  This extrinsic order does not need to be related with possible ordering of items themselves
  (items in an array are not always stored in increasing or decreasing order). 

**Definition:** 
  Items :math:`a,b` stored in a data container have *intrinsic order* iff they can be compared 
  by themselves. Such as :math:`a = b`, :math:`a < b`, or :math:`a > b`. 
  (Some data structures such as Binary Search Trees (BSTs) store keys according to their intrinsic order). 


There may be data structures (such as sets stored in a hashtable) that do not use either intrinsic or extrinsic order. 
We can iterate over such containers, but will get the elements in some unpredictable order. 

**Definition:** 
  A data structure is *immutable*, if it cannot change its state after its creation   
  Other data structures that can be changed are called *mutable*. 

**Example:**
  A ``string`` data structure is immutable in many programming languages -- a string object stays 
  unchanged throughout its lifetime. Appending new characters or modifying the string is 
  possible, but the result is always a new string object. 

Immutable data structures 
can be easily passed as parameters to functions (just by copying its address or 
reference, but without cloning the data). Immutable data structures also can serve as keys
in larger data structures.
 
**Definition:** 
  Some property for a mutable data structure is a *representation invariant*, if it is necessary for 
  any consistent state of this data structure and it is preserved during the ADT operations. 
  Namely, if the property was true before the operation (insertion, deletion etc.), then it must be also true 
  after that operation. It is thus *unchangeable* or *invariant*. 
  
Violating the representation invariant makes the data structure inconsistent and unusable. 
If an API method is run on an inconsistent data structure, there are no expectations
(program can crash, loop forever or produce any result).

**Example:** 
  Some mutable data structures (such as ``java.util.HashSet``) allow to insert other 
  mutable objects such as ``ArrayList`` objects  into the hashtable.
  If some object is modified after being inserted, it is not rehashed and its location becomes invalid. 
  At that time the representation invariant of the hashtable is broken -- the object cannot
  be located in its appropriate hashing bucket anymore. 


**Definition**
  A *stack* is a data structure with extrinsic order -- it allows to access (to read or to delete) the element which was 
  the latest to be inserted (LIFO policy). A stack supports the following operations:

  | :math:`S.\text{\sc initialize}()`  :math:`\;\;\;\;\;` :math:`\textcolor{teal}{\text{\em (create a new empty stack or clear existing contents)}}`
  | :math:`S.\text{\sc push}(x)`  :math:`\;\;\;\;\;` :math:`\textcolor{teal}{\text{\em (add item $x$ to the top of the stack)}}`
  | :math:`S.\text{\sc pop}()` :math:`\;\;\;\;\;` :math:`\textcolor{teal}{\text{\em (remove and return an item from the top of the stack)}}`
  | :math:`S.\text{\sc isEmpty}()` :math:`\;\;\;\;\;` :math:`\textcolor{teal}{\text{\em (true iff the stack is empty)}}`  

  Optionally stacks can support some non-essential operations (can be expressed with the above operations considered essential): 

  | :math:`S.\text{\sc top}()` :math:`\;\;\;\;\;` :math:`\textcolor{teal}{\text{\em (return, but do not remove the top element)}}` 
  | :math:`S.\text{\sc size}()` :math:`\;\;\;\;\;` :math:`\textcolor{teal}{\text{\em (return the number of elements in the stack)}}`

  In practice stacks may also need :math:`S.\text{\sc isFull}()` operation to find, if the container has place for one more item. 
  Abstract stacks may assume that the stack is never full. 

**Definition**
  A *queue* is a data structure with extrinsic order -- it allows to access (seeing or deleting) the single element which was 
  the first to be inserted (FIFO policy). A queue supports the following operations:

  | :math:`Q.\text{\sc initialize}()`  :math:`\;\;\;\;\;` :math:`\textcolor{teal}{\text{\em (create a new empty queue or clear existing contents)}}`
  | :math:`Q.\text{\sc enqueue}(x)`  :math:`\;\;\;\;\;` :math:`\textcolor{teal}{\text{\em (add item $x$ to the end of the queue)}}`
  | :math:`Q.\text{\sc dequeue}()` :math:`\;\;\;\;\;` :math:`\textcolor{teal}{\text{\em (remove and return an item from the front of the queue)}}`
  | :math:`Q.\text{\sc isEmpty}()` :math:`\;\;\;\;\;` :math:`\textcolor{teal}{\text{\em (true iff the queue is empty)}}`  
  

  Optionally queues can support other operations, but many queue applications do not need them:
  
  | :math:`Q.\text{\sc front}()` :math:`\;\;\;\;\;` :math:`\textcolor{teal}{\text{\em (return the front element in the queue without dequeuing)}}`
  | :math:`S.\text{\sc size}()` :math:`\;\;\;\;\;` :math:`\textcolor{teal}{\text{\em (return the number of elements in the queue)}}`
  
  
**Definition:** 
  A *double-ended queue* or a *deque* is a data structure with extrinsic order allowing elements to 
  be added to the front (as in a stack) and also to the back (as in a queue). It supports the following operations: 
  
  | :math:`D.\text{\sc initialize}()`  :math:`\;\;\;\;\;` :math:`\textcolor{teal}{\text{\em (create a new empty deque or clear existing contents)}}`
  | :math:`D.\text{\sc pushFront}(x)`  :math:`\;\;\;\;\;` :math:`\textcolor{teal}{\text{\em (add item $x$ to the front of the deque)}}`
  | :math:`D.\text{\sc popFront}()` :math:`\;\;\;\;\;` :math:`\textcolor{teal}{\text{\em (remove and return an item from the front of the deque)}}`
  | :math:`D.\text{\sc pushBack}(x)`  :math:`\;\;\;\;\;` :math:`\textcolor{teal}{\text{\em (add item $x$ to the back of the deque)}}`
  | :math:`D.\text{\sc popBack}()` :math:`\;\;\;\;\;` :math:`\textcolor{teal}{\text{\em (remove and return an item from the back of the deque)}}`
  | :math:`D.\text{\sc front}()` :math:`\;\;\;\;\;` :math:`\textcolor{teal}{\text{\em (return the front element in the deque without removing it)}}`
  | :math:`D.\text{\sc back}()` :math:`\;\;\;\;\;` :math:`\textcolor{teal}{\text{\em (return the back element in the deque without removing it)}}`  
  | :math:`D.\text{\sc isEmpty}()` :math:`\;\;\;\;\;` :math:`\textcolor{teal}{\text{\em (true iff the deque is empty)}}`  
  | :math:`D.\text{\sc size}()` :math:`\;\;\;\;\;` :math:`\textcolor{teal}{\text{\em (return the number of elements in the deque)}}`

  Optionally, a deque can be used to search for an item :math:`x` with a given key :math:`x.k` or to find the predecessor or 
  successor of an item :math:`x` by its pointer/reference. 

  | :math:`D.\text{\sc search}(k)` :math:`\;\;\;\;\;` :math:`\textcolor{teal}{\text{\em (return an item $x$ with key $k$ or "nil")}}`
  | :math:`D.\text{\sc predecessor}(x)` :math:`\;\;\;\;\;` :math:`\textcolor{teal}{\text{\em (return the predecessor of $x$)}}`
  | :math:`D.\text{\sc successor}(x)` :math:`\;\;\;\;\;` :math:`\textcolor{teal}{\text{\em (return the successor of $x$)}}`
  

Deques are often implemented as doubly linked lists with front and back pointers 
(and the current size maintained in a separate variable). In this case pushing and popping items happens in constant time, 
searching requires scanning through the list in :math:`O(n)` time. And predecessors/successors can be found by following the 
``next`` and ``prev`` pointers.   
  
STL class ``vector`` in C++ supports the deque operations, but 
also allows random access just as in array (returning an element by its index). Similar things are supported by Python lists
or by :math:``java.util.List`` interface. Such data structures are more powerful than either stacks, queues or deques -- 
they behave like arrays (without strict limit on size). 

















Problems
----------

.. _adts-and-implementations-P1:

**Problem 1:** 
  In some Python's implementations, the dynamic array is grown by :math:`n/8` whenever 
  the list overflows. Assume that :math:`r` is the ratio between inserts and 
  reads for this dynamic array. Find the value :math:`r` for which this growth 
  factor is the optimal one.
 

.. _adts-and-implementations-P2:
 
**Problem 2:** 
  Reverse the order of elements in stack :math:`S` in the following ways:
  
  **(A)** 
    Use two additional stacks, but no auxiliary variables.
	
  **(B)**
    Use one additional stack and some additional non-array variables (i.e. cannot use lists, sequences, stacks or queues).


.. _adts-and-implementations-P3:

**Problem 3:** 
  Read elements from an iterator and place them on a stack :math:`S` in ascending order using one 
  additional stack and some additional non-array variables.


.. _adts-and-implementations-P4:	

**Problem 4:** 
  Given a data structure implementing the
  Sequence ADT, show how to use it to implement the Set interface. 
  (Your implementation does not need to be efficient.)


.. _adts-and-implementations-P5:

**Problem 5:** 
  What are the costs for each ADT operation, if a queue is implemented 
  as dynamic array?


.. _adts-and-implementations-P6:

**Problem 6:** 
  Which operations become asymptotically faster, if list ADT is implemented as a doubly linked 
  list (instead of a singly linked list)? 
   

.. _adts-and-implementations-P7:

**Problem 7: (Stack Implementation as Array):**
  Stack is implemented as an array. In our case the array has size :math:`n = 5`.
  Stack contains integer numbers; initially the array has
  the following content.
  
  .. image:: figs-adts-and-implementations/stack-structure.png
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
  
.. only:: Internal

  **Answer:** 
  
    The figure below shows stack memory states after each of the 8 operations above are completed:
    
    .. image:: figs-adts-and-implementations/stack-solution.png
       :width: 2.2in
    
  
  :math:`\square`


.. _adts-and-implementations-P8:

**Problem 8 (Queue Implementation as a Circular Array):**
  A queue is implemented as an array with ``size`` elements; it has two
  extra variables ``front`` (pointer to the first element) and ``length``
  (the current number of elements in the queue). Current state is shown in the figure:
  

  .. image:: figs-adts-and-implementations/queue-structure.png
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
  
.. only:: Internal

  **Answer:** 
  
    The figure below shows queue memory states after each of the operations above are completed:
    
    .. image:: figs-adts-and-implementations/queue-solution.png
       :width: 2.3in
    
  
  :math:`\square`


.. _adts-and-implementations-P9:

**Problem 9:** 
  We suggest a specialized Abstract Data Type (ADT) named ``Backtracker``
  which can be used to solve backtracking tasks such as N-Queens problem, 
  Sudoku and other combinatorial tasks. 

  A backtracker object stores some (partially solved) instance of a backtracking 
  problem, and an external driver can use it to visit all nodes rooted tree in the DFS order. 
  As soon as it sees a complete valid solution, the solution can be output. 
  Sometimes we want to find all solutions, if there exist more than one.   
  *Backtracking is typically an inefficient exponential time algorithm, 
  but it can be improved, if it can establish early that in the   
  given subtree there are no more solutions.* 

  Here is the ADT: 

  | *(Initialize Backtracker with its initial state, e.g. an empty chessboard)*
  | :math:`B = \text{\sc Backtracker}(s:\text{\em State})`
  | *(Get available moves at the given level, e.g. all queen positions for some vertical)*
  | :math:`B.\text{\sc moves}(\text{\em level}:int):\text{\sc List}<\text{Move}>`
  | *(Is the move valid in the given state, e.g. is the chosen position attacked by earlier queens)*
  | :math:`B.\text{\sc valid}(\text{\em level}:int, \text{\em move}:Move):\text{\sc Boolean}`
  | *(Record the move to the backtracker, e.g. add one more chosen queen position)*
  | :math:`B.\text{\sc record}(\text{\em level}:int, \text{\em move}:Move)`
  | *(Opposite to record -- undo the move, e.g. remove the latest queen position)*
  | :math:`B.\text{\sc undo}(\text{\em level}:int, \text{\em move}:Move)`
  | *(Is the search successfully completed, e.g. all N queens already placed?)*
  | :math:`B.\text{\sc done}(\text{\em level}:int):\text{\sc Boolean}`
  | *(Output the successful solution for the Backtracker object, e.g. print the chessboard)*
  | :math:`B.\text{\sc output}()`


  **(A)**
    Write the pseudocode for a function :math:`\text{\sc attempt}(b:\text{\sc Backtracker}, \text{\em level}:\text{\sc Int})` so as to 
    find the first solution starting with the backtracker object on 
    level :math:`\text{\em level}`. 
    
  **(B)** 
    Modify the function :math:`\text{\sc attempt}(b:\text{\sc Backtracker}, \text{\em level}:\text{\sc Int})` so that it does not stop until 
    it outputs all valid solutions. 

.. only:: Internal 

  **Answer:** 
  
  **(A)**
    Here is the  code to find just one solution for a backtracker: 
    
    | :math:`\text{\sc attempt}(b:\text{\sc Backtracker}, \text{\em level}:Int):Bool`
    | :math:`\;\;\;\;\;` :math:`\text{\em successful} = \text{\sc False}`
    | :math:`\;\;\;\;\;` :math:`\text{\em moves} = b.\text{\sc moves}(level)`
    | :math:`\;\;\;\;\;` **for** :math:`\text{\em move}` **in** :math:`\text{\em moves}`:
    | :math:`\;\;\;\;\;\;\;\;\;\;` **if** :math:`b.\text{\sc valid}(\text{\em level}, \text{\em move})`: 
    | :math:`\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;` :math:`b.\text{\sc record}(\text{\em level}, \text{\em move})`: 
    | :math:`\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;` **if** :math:`b.\text{\sc done}(\text{\em level})`: 
    | :math:`\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;` :math:`\text{\em successful} = \text{\sc True}`: 
    | :math:`\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;` **else**: 
    | :math:`\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;` :math:`\text{\em successful} = \text{\sc attempt}(\text{\em b}, \text{\em level})`
    | :math:`\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;` **if** **not** :math:`\text{\em successful}`: 
    | :math:`\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;` :math:`b.\text{\sc undo}(\text{\em level}, \text{\em move})`
    | :math:`\;\;\;\;\;\;\;\;\;\;` **if** :math:`\text{\sc successful}`: 
    | :math:`\;\;\;\;\;` **return** :math:`\text{\em successful}`
    

    See Robert E. Noonan. `An Object-Oriented View on Backtracking <https://dl.acm.org/doi/pdf/10.1145/331795.331886>`_ 

  :math:`\square`





