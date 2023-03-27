Worksheet, Week 08: Sorting
=============================



Problems
-----------


**QuickSort Algorithm:**
  This variant of Quicksort uses the leftmost element of the input area as a pivot.
  It is taken from the lecture slides. There are other Quicksort flavors (randomized or choosing a pivot differently).

  .. math::

    \begin{array}{rl}
     & \text{\textsc{Quicksort}}(A[\ell\;\ldots\;r]):\\
    1 & \text{\textbf{if\ }} l<r:\\
    2 & \hspace{.5cm} i = \ell \;\;\;\;\;\;\;\;\; \textcolor{teal}{\text{\em ($i$ increases from the left and searches elements $\geq$ than pivot)}}\\
    3 & \hspace{.5cm} j = r+1	\;\; \textcolor{teal}{\text{\em ($j$ decreases from the right and searches elements $\leq$ than pivot.)}}\\
    4 & \hspace{.5cm} v = A[\ell] \;\;\;\; \textcolor{teal}{\text{\em ($v$ is the pivot.)}}\\
    5 & \hspace{.5cm} \text{\textbf{while\ }} i<j:\\
    6 & \hspace{1.0cm} i = i+1\\
    7 & \hspace{1.0cm} \text{\textbf{while\ }} i<r \text{\textbf{\ and\ }} A[i]<v:\\
    8 & \hspace{1.5cm} i = i+1\\
    9 & \hspace{1.0cm} j = j-1\\
    10 & \hspace{1.0cm} \text{\textbf{while\ }} j>\ell \text{\textbf{\ and\ }} A[j]>v:\\
    11 & \hspace{1.5cm} j = j-1\\
    12 & \hspace{1.0cm} A[i] \leftrightarrow A[j] \;\; \textcolor{teal}{\text{\em (Undo the extra swap at the end)}}\\
    13 & \hspace{0.5cm} A[i] \leftrightarrow A[j] \;\; \textcolor{teal}{\text{\em (Undo the extra swap at the end)}}\\
    14 & \hspace{0.5cm} A[j] \leftrightarrow A[\ell] \;\; \textcolor{teal}{\text{\em (Move pivot to its proper place)}}\\
    15 & \hspace{0.5cm} \text{\textsc{Quicksort}}(A[\ell\;\ldots\;j-1])\\
    16 & \hspace{0.5cm} \text{\textsc{Quicksort}}(A[j+1\;\ldots\;r])\\
    \end{array}





..   (*4.D. Use and analyze Heapsort.*)

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


**Problem 4:**

  .. image:: figs-sorting/bubblesort.png
     :width: 4in

  The image shows Bubble sort pseudocode for a 0-based array :math:`A[0]\ldots{}A[n-1]` of :math:`n` elements.

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



**Problem 5:**
  
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
  
  **(A)**
    What is the total number of calls to :math:`\text{\sc MergeSort}` for this array 
    (this includes the initial call as well as the 
    recursive calls on lines 3 and 4 of this pseudocode). 
	
  **(B)**
    How many comparisons are needed (in the worst case) to sort an array of :math:`11` items 
	by the MergeSort algorithm? 
	
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
  
  