Worksheet 08: Sorting
=============================

Various sorting algorithms are introduced here, because they 
illustrate algorithm building paradigms (*Anany Levitin. 
Introduction to the design & analysis of algorithms*). 
Depending on the context different sorting algorithms may be needed. 


Concepts and Facts
---------------------

**Statement (lower bound for sorting):** 
  Any general sorting algorithm receiving an input of :math:`n` distinct 
  items and producing a sorted output of these items (without assuming anything 
  additional about the input) needs at least :math:`\lceil \log_2 n! \rceil` 
  comparisons. 
  
**Proof:** 
  Any decision tree with :math:`k` levels (i.e. a sorting algorithm making 
  :math:`k` comparisons, can distinguish at most :math:`2^k` different cases. 
  On the other hand, there are :math:`n!` different ways how :math:`n` sortable items 
  can be arranged in the input. Thus we must have :math:`2^k \geq n!` or 
  :math:`k \geq \lceil \log_2 n! \rceil`. 
  (See `Comparison Sort <https://en.wikipedia.org/wiki/Comparison_sort#Number_of_comparisons_required_to_sort_a_list>`_.)

**Definition:** 
  A sorting algorithm is called *stable* iff any two items with equal keys 
  are not swapped: (and thus preserve their initial order). 
  Algorithms that are not guaranteed to preserve such order are *unstable*. 
  
**Definition:** 
  A sorting algorithm that does not need to know the number of sortable items 
  ahead of the time is called *online*. Those algorithms that receive full sortable 
  array right at the start are called *offline*. 
  
**Definition:** 
  A sorting algorithm is called in-place, iff it uses just the original array 
  to store the sortable items (plus some local variables). 
  Sorting algorithms that need to allocate new memory for the sortable items are 
  *outplace*. 
  


**MergeSort algorithm:** 
  This algorithm is a typical illustration of the Divide and Conquer paradigm.

  | :math:`\text{\sc MergeSort}(A,p,r)`:
  | :math:`1\;\;` **if** :math:`p < r`
  | :math:`2\;\;\;\;\;\;\;\;` :math:`q = \left\lfloor (p+r)/2 \right\rfloor`
  | :math:`3\;\;\;\;\;\;\;\;` :math:`\text{\sc MergeSort}(A,p,q)`
  | :math:`4\;\;\;\;\;\;\;\;` :math:`\text{\sc MergeSort}(A,q+1,r)`
  | :math:`5\;\;\;\;\;\;\;\;` :math:`\text{\sc Merge}(A,p,q,r)`

MergeSort is outplace algorithm -- it may waste memory, if run on large arrays. 
On the other hand, MergeSort is nearly optimal regarding the number of comparisons needed, 
so it may be helpful, if comparing two items takes much time. 



**Quicksort algorithm:**
  QuickSort has several flavors; this is one of the easiest, but it sometimes
  needs one extra swap -- see Line 13. 
  This variant of Quicksort always uses the leftmost element of the input area as a pivot -- 
  it is easy to understand, but may be inefficient, if the input array is nearly sorted already. 
  More advanced Quicksort flavors are randomized or choose the pivot differently.

  | :math:`\text{\sc Quicksort}(A[\ell\;\ldots\;r])`:
  | 1. :math:`\;\;\;\;\;` **if** :math:`\ell < r`:
  | 2. :math:`\;\;\;\;\;\;\;\;\;\;` :math:`i = \ell` :math:`\;\;\;\;\;\;\;\;\;` :math:`\textcolor{teal}{\text{\em ($i$ increases from the left, searches elements $\geq$ than pivot)}}`
  | 3. :math:`\;\;\;\;\;\;\;\;\;\;` :math:`j = r+1`	:math:`\;\;` :math:`\textcolor{teal}{\text{\em ($j$ decreases from the right, searches elements $\leq$ than pivot.)}}`
  | 4. :math:`\;\;\;\;\;\;\;\;\;\;` :math:`v = A[\ell]` :math:`\;\;\;\;` :math:`\textcolor{teal}{\text{\em ($v$ is the pivot.)}}`
  | 5. :math:`\;\;\;\;\;\;\;\;\;\;` **while** :math:`i<j`:
  | 6. :math:`\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;` :math:`i = i+1`
  | 7. :math:`\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;` **while** :math:`i<r` **and** :math:`A[i]<v`:
  | 8. :math:`\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;` :math:`i = i+1`
  | 9. :math:`\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;` :math:`j = j-1`
  | 10. :math:`\;\;\;\;\;\;\;\;\;\;\;\;\;` **while** :math:`j>\ell` **and** :math:`A[j]>v`:
  | 11. :math:`\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;` :math:`j = j-1`
  | 12. :math:`\;\;\;\;\;\;\;\;\;\;\;\;\;` :math:`A[i] \leftrightarrow A[j]`
  | 13. :math:`\;\;\;\;\;\;\;\;` :math:`A[i] \leftrightarrow A[j]` :math:`\;\;` :math:`\textcolor{teal}{\text{\em (Undo the extra swap at the end)}}`
  | 14. :math:`\;\;\;\;\;\;\;\;` :math:`A[j] \leftrightarrow A[\ell]` :math:`\;\;` :math:`\textcolor{teal}{\text{\em (Move pivot to its proper place)}}`
  | 15. :math:`\;\;\;\;\;\;\;\;` :math:`\text{\sc Quicksort}(A[\ell\;\ldots\;j-1])`
  | 16. :math:`\;\;\;\;\;\;\;\;` :math:`\text{\sc Quicksort}(A[j+1\;\ldots\;r])`
   
Quicksort algorithm has good characteristics for nearly all inputs -- it sorts in place (does not need much memory), 
it usually is quite optimal and also easy to implement. 
It may behave badly for certain special inputs (for example, if the input array is nearly sorted already). 

  | :math:`\text{\sc BubbleSort}(A[0 \ldots n-1])`:
  | 1. :math:`\;\;\;\;\;` **do**:
  | 2. :math:`\;\;\;\;\;\;\;\;\;\;` :math:`swapped = \text{\sc False}`
  | 3. :math:`\;\;\;\;\;\;\;\;\;\;` **for** :math:`i` **in** :math:`\text{\sc range}(1,n)`: :math:`\;\;` :math:`\textcolor{teal}{\text{\em (from $1$ to $n-1$ inclusive)}}`
  | 4. :math:`\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;` **if** :math:`A[i-1] > A[i]`:
  | 5. :math:`\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;` :math:`A[i-1] \leftrightarrow A[i]`
  | 6. :math:`\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;` :math:`swapped = \text{\sc True}`
  | 7. :math:`\;\;\;\;\;` **while** :math:`swapped`:





Problems
-----------


.. _sorting-P1:

**Problem 1:** 

  **(A)** 
    Find the :math:`O(g(n))` for the following function: :math:`\log_2 n!``. 
	
  **(B)** 
    What is the lower bound of comparisons needed to sort an array of :math:`5` 
    elements (assume they are all different)? 
	


..   (*4.D. Use and analyze Heapsort.*)

.. _sorting-P2:

**Problem 2:** 
  An array of :math:`10` elements is used to initialize a minimum heap (as the first stage of 
  the Heap sort algorithm): 
  
  .. math::
  
    \{ 5, 3, 7, 10, 1, 2, 9, 8, 6, 4 \}

  Assume that the minimum heap is initialized in the most efficient way (inserting elements
  level by level -- starting from the bottom levels). All slots are filled in with the elements
  of the 10-element array in the order they arrive.
  
  
  **(A)**
    How many levels will the heap tree have? (The root of the heap is considered :math:`L_0` -- level zero.
    the last level is denoted by :math:`L_{k-1}`. Just find the number :math:`k` for this array.)
  
  **(B)**
    Draw the intermediate states of the heap after each level is filled in. Represent the heap as a binary tree. 
    (If some level :math:`L_k` is only partially filled and contains less than :math:`2^k` nodes, 
    please draw all the nodes as little circles, but leave the unused nodes empty.)

  **(C)** 
    What is the total count of comparisons (:math:`a < b`) that is necessary to build the final
    minimum heap? (In this part you can assume the worst case time complexity -- 
    it is not necessarily achieved for the array given above.)
	

.. only:: Internal	

  **Answer:** 
  
  **(A)** 
    10 elements need a tree with four levels (complete tree with 10 nodes). The last level :math:`L_3` 
    will have just three nodes filled in. 

  **(B)**
    See the picture with all four stages of adding elements (unused slots are gray; the nodes that 
    swap their places during the downheap operations are shown in pink). 
	
    .. image:: figs-sorting/heap-stages.png
       :width: 4in
	   
  
  **(C)**
    In a downheap operation (when you add a new node on top of two other nodes), you first need to compare 
    the two siblings, then compare their parent with the smallest of the two siblings (and if it is larger than 
    its child, then swap). So every time some node moves one level down, you need to spend at most two comparisons. 
	
    .. image:: figs-sorting/heap-heights.png
       :width: 2in
    	
    For our complete tree (with five grayed out slots in the last level), 
    the worst case happens, if every node inserted at height :math:`h` needs to spend :math:`2h` comparisons to travel to the
    very bottom (if we assume the worst case -- that it is larger than everything that has been inserted so far).
    So the total number of comparisons is :math:`2 \cdot (1 + 1 + 1 + 2 + 3) = 16`. 
    In general, this time should grow as :math:`O(n)`, where :math:`n` is the number of items in the heap being built.
      	
  :math:`\square`
  
  

.. _sorting-P3:

**Problem 3:**

  **(A)**
    Run this pseudocode for one invocation :math:`\text{\textsc{QuickSort}}(A[0..11])`,
    where the table to sort is the following:

    .. math::

      13, 0, 23, 1, 8, 9, 29, 16, 8, 24, 6, 11.

    Draw the state of the array every time you swap two
    elements (i.e. execute :math:`A[k_1] \leftrightarrow A[k_2]` for any :math:`k_1,k_2`).

  **(B)**
    Continue with the first recursive call of :math:`\text{\textsc{QuickSort}}()`
    (the original call :math:`\text{\textsc{QuickSort}}(A[0..11])` is assumed to be the
    :math:`0^{\text{th}}` call of this function).
    Draw the state of the array every time you swap two elements.

  **(C)**
    Decide which is the second recursive call of
    :math:`\text{\textsc{QuickSort}}()` and draw the state
    of the array every time you swap two elements.
    Show the end-result
    after this second recursive call at the very end.


.. only:: Internal 

  **Answer:**
  
    Your answer can be simple lists of numbers (without any grid lines or additional
    markings). Just try to keep the lists of numbers aligned.


  **(A)**
    Swaps during the :math:`0^{\text{th}}` call:

    .. image:: figs-sorting/arrays-part1.png
       :width: 4in


  **(B)**
    Since this example contains two elements equal to :math:`8`,
    we added subscripts to them (to show clearly, where every one is being swapped).
    As integer numbers they are fully identical to the Quicksort algorithm.
    (Still, the Quicksort algorithm does redundant swaps on them.)

    Swaps during the first recursive call.

    .. image:: figs-sorting/arrays-part2.png
       :width: 4in


  **(C)**
    Notice that the second recursive call happens within the
    first recursive call (sorting the left side of the left half).

    Swaps during the second recursive call:

    .. image:: figs-sorting/arrays-part3.png
       :width: 4in


  :math:`\square`





..  (*5.A. Use and analyze Selection sort, Insertion sort, Bubble sort algorithms.*)

.. _sorting-P4:

**Problem 4:**


  Consider the BubbleSort algorithm (see the beginning of the worksheet) for a 0-based array :math:`A[0]\ldots{}A[n-1]` of :math:`n` elements.

  **(A)** 
    How many comparisons (``A[i-1] > A[i]``) in this algorithm are used to sort the given array. 
    Show the state of the array after each ``for`` loop in the pseudocode is finished. 
	
    .. math::
	  
       A[0]=9,\; 0,\; 1,\; 2,\; 3,\; 4,\; 5,\; 6,\; 7,\; A[9]=8.
	  
  **(B)**  
    How many comparisons (``A[i-1] > A[i]``) in this algorithm are used to sort the following array: 
	
    .. math::
	  
      A[0]=1,\; 2,\; 3,\; 4,\; 5,\; 6,\; 7,\; 8,\; 9,\; A[9]= 0.


.. only:: Internal 

  **Answer:**

  **(A)** 
    18 comparisons, 2 executions of the **for** loop: 
	
    After the first **for** loop the array is sorted: 
  
    .. math::
	  
      A[0]=0,\; 1,\; 2,\; 3,\; 4,\; 5,\; 6,\; 7,\; 8,\; A[9]=9.
	
    After the second **for** loop and 9 more comparisons no further swaps occur and the algorithm stops.
    The array is still the same:	
	
    .. math::
	  
      A[0]=0,\; 1,\; 2,\; 3,\; 4,\; 5,\; 6,\; 7,\; 8,\; A[9]=9.

  **(B)** 
    
    90 comparisons, 10 executions of the **for** loop: 
	
    After the first **for** loop:

    .. math::
	  
      A[0]=1,\; 2,\; 3,\; 4,\; 5,\; 6,\; 7,\; 8,\; 0,\; A[9]= 9.

    After the second **for** loop:
	
    .. math::
	  
      A[0]=1,\; 2,\; 3,\; 4,\; 5,\; 6,\; 7,\; 0,\; 8,\; A[9]= 9.

    After the ninth **for** loop: 
	
    .. math::
	  
      A[0]=0,\; 1,\; 2,\; 3,\; 4,\; 5,\; 6,\; 7,\; \; 8,\; A[9]= 9.
	
    After the tenth **for** loop the array stays the same and the algorithm stops:
	
    .. math::
	  
      A[0]=0,\; 1,\; 2,\; 3,\; 4,\; 5,\; 6,\; 7,\; \; 8,\; A[9]= 9.


    .. note:: 
      Small values near the end of the list will slow down the Bubble sort considerably. 
      The authors of an accelerated Bubble-sort variant (Comb sort) call such values *turtles*.
      See `<https://bit.ly/3mmS6C4>`_.


  :math:`\square`


.. _sorting-P5:

**Problem 5:**
  
  We have a 1-based array with 11 elements: :math:`A[1],\ldots,A[11]`. 
  We want to sort it efficiently. 
  Run the MergeSort on this array (see the beginning of the worksheet). 
  
  Assume that initially you call this function as :math:`\text{\sc MergeSort(A,1,11)}`, 
  where :math:`p = 1` and :math:`r = 11` are the left and the right endpoint of the 
  array being sorted (it includes both ends). 
  
  **(A)**
    What is the total number of calls to :math:`\text{\sc MergeSort}` for this array 
    (this includes the initial call as well as the 
    recursive calls on lines 3 and 4 of this pseudocode). 
	
  **(B)**
    How many comparisons are needed (in the worst case) to sort an array of 
    :math:`11` items by the MergeSort algorithm? 
	
  **(C)** 
    Evaluate :math:`\log_2 11!` using Stirling's formula or a direct computation. 
    What is the theoretical lower bound on the number of comparisons to sort :math:`11` items?
  
  
  
.. only:: Internal

  **Answer:**
  
  .. image:: figs-sorting/mergesort-calls.png
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
  

.. _sorting-P6:

**Problem 6:** 

  **(A)** 
    Some algorithm receives :math:`n` items as its input and then calls
    function :math:`f(x_1,x_2,x_3,x_4)`
    for any ordered quadruplet :math:`x_1, x_2, x_3, x_4` received in the input. 
    Assume that :math:`f(\ldots)` runs in constant time. Find the time complexity of the whole algorithm. 
	
  **(B)** 
    Some algorithm receives :math:`n` items as its input and then calls a function 
    :math:`f` on all subsets of 
    the received items having size :math:`\lfloor n/4 \rfloor`. 
    Assume that :math:`f(\ldots)` runs in constant time. Find the time complexity of the whole algorithm. 

