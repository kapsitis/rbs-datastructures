Programming Task 1, Part 1
============================

When doing the exercises follow the following guidelines: 

  * Create C++ files matching the exercise names: ``sample1.cpp``, 
    ``sample2.cpp``, ``sample3.cpp``, ``sample4.cpp``, ``sample5.cpp``. 
    Follow the problem-specific guidelines (which functions to implement and so on).
  * Use arrays, pointers and variables of basic types whenever possible. 
    Avoid using external data-structure libraries (such as STL). 
    You still need some external libraries --- ``iostream``
    (possibly, also ``sstream`` or ``iomanip``) for input/output. 
  * Place all the files in the directory ``ds-workspace-YourName/lab1-1``.
  * Commit and push your repository to GitHub. 
    Tag this programming task as ``submit-lab1-1``. 


sample1.cpp: Maximum Element in a 2D Array
------------------------------------------

Create a C++ program that reads an :math:`3 \times 5` array of integers from the standard input.
It scans this array in the row-major order and finds the maximum value. 
It outputs this maximum value, its row and column number. 
If maximum repeated multiple times, output the last position where it was encountered. 

The ``main()`` method for your function should look like this:

.. code-block:: cpp

  #include <iostream> 

  // your implementation of findMax(...)

  int main() {
    int arr[3][5]; 
    for (int i = 0; i < 3; i++)
      for (int j = 0; j < 5; j++) 
        cin >> arr[i][j];
    int i, j; 
    int maxValue = findMax(arr, i, j); 
    cout << maxValue << " " << i << " " << j << endl;
  }
	
**Constraints:** 

  * :math:`-10^9 \leq arr[i][j] \leq 10^9` for :math:`i \in \{ 0,1,2 \}`, :math:`j \in \{ 0,1,2,3,4 \}`
	
**Sample Input:**
  
  .. code-block:: text

    4 6 7 2 5
    6 7 0 4 4
    5 7 3 6 1

**Sample Output:**
  
  .. code-block:: text
      
    7 2 1	  
	  
**Explanation:**
  The maximum element in the array is ``7``. 
  The last place where it appears is ``arr[2][1] = 7`` (3rd row, 2nd position).
  


sample2.cpp: Finding Closest Pairs
-----------------------------------

There is an array :math:`A` of length :math:`2n`. 
We build two new arrays :math:`B` and :math:`C` (both of length :math:`n`) from the elements of :math:`A`.
We repeat the following step :math:`n` times:

**Step Description:** 
  Among the elements of :math:`A` that are still unused in either :math:`B` or :math:`C`
  find those :math:`A[i]` and :math:`A[j]` which are the "closest". 
  Namely, find two indices for which the absolute value
  :math:`{\displaystyle \left| A[i] - A[j] \right|}` is minimal. If there are multiple
  pairs :math:`i,j` where :math:`A[i],A[j]` are closest, select the pair with the
  smallest :math:`i` (and, if the same :math:`i` participates in multiple closest pairs, then 
  also pick the smallest :math:`j`). 
	
  Once you have the "closest" :math:`A[i]` and :math:`A[j]`,
  insert the smallest one into :math:`B` and the largest one into
  :math:`C` (or append the same number to both arrays, if they 
  were equal). Both :math:`B` and :math:`C` are filled from the left
  to the right.	

  Create a C++ program that reads an an array :math:`A` of even length
  (All its :math:`2n` elements are space separated positive integers. 
  It terminates with a single :math:`0`.)
  Output arrays :math:`B` and :math:`C` as two lines of
  integers.
  
**Constraints:** 

  * :math:`n \leq 1000`,
  * :math:`1 \leq A[i] \leq 10^9` for all :math:`i \in \{ 0,\ldots,2n-1\}`.
	
**Sample Input:**
  
  .. code-block:: text
	
    3 10 5 5 8 12 0	  
	  
**Sample Output:**

  .. code-block:: text
    
    5 8 3 
    5 10 12 

**Explanation:** 
    
  * During the first step we remove :math:`A[2]=5` and :math:`A[3]=5`. 
  * During the second step we remove :math:`A[1]=10` and :math:`A[4]=8`. 
  * During the third step we remove :math:`A[0]=3` and :math:`A[5]=12`.
	


sample3.cpp: Editing of Char Arrays
------------------------------------

Make a C++ program that reads lines into char arrays from standard input 
(until there is an empty line -- two newline symbols in a row). 
Each line is processed and whenever there is a character ``arg[i]``
equal to some capital letter (A-Z) 
immediately preceeded by another capital letter ``arg[i-1]``
and ``arg[i-1]`` is **not** alphabetically before ``arg[i]``, 
then ``arg[i]`` is removed. 
The algorithm leaves all lower-case
letters, digits and special characters unchanged. 
(*The deletion is reapplied while there are any not-in-order 
capital letters next to each other --- the following letter is always removed. 
Ultimately, all the the sequences of 
capital letters are in strictly increasing alphabetical order.*)

The algorithm should process the C-strings (arrays of type ``char*`` and 
edit its argument in place without creating another array). The algorithm of deleting characters has
the following prototype:
  
  .. code-block:: cpp
  
    void eraseChars(char* arg); 
	
**Constraints:** 

  * Number of non-empty lines up to :math:`1000`.
  * Length of lines in the file up to :math:`1000`.
	
**Sample Input:**

  .. code-block:: text
	
    ABCA-IHGxDEFD
    321.ABB.AAB.BAA.ZZYWA.123
	  
**Sample Output:**

  .. code-block:: text
	
    ABC-IxDEF
    321.AB.AB.B.Z.123

**Explanation:** 
  Lower-case letters (such as ``x``), digits or punctuation does not change, 
  but contiguous capitalized fragments such as 
  ``ABCA``, ``IHG``, ``DEFD``, ``ABB``, ``AAB``, ``BAA``
  are being filtered: All characters that do not follow alphabetically 
  the earlier ones, are eliminated.


sample4.cpp: Editing Linked Lists
----------------------------------

There is a list of :math:`n` integer numbers :math:`a_i` (:math:`i=0,\ldots,n-1`) 
implemented as a linked list of ``Node`` objects. 
``Node`` has the following type: 
  
  .. code-block:: cpp
  
    struct Node { int info; Node* next; }; 

Each number in the list is stored in the ``info`` attribute.
Assume that the first node is pointed to by variable ``Node* listHead``. 
Implement a procedure with the following prototype: 

  .. code-block:: cpp
  
    void changeList(Node* listHead);

It swaps the fist element of the list with the last one. Then it 
deletes all nodes with ``info`` field equal to ``0``. 

.. note::
  In order to use the linked list for processing the elements, you 
  should avoid storing intermediate results in arrays (as well as vectors or similar data structures).
  Just a few extra variables taking a constant amount of memory should be enough.
  Also, the more appropriate way to rearrange a linked list is
  to redraw the pointers (rather to modify ``info`` fields of ``Node``
  objects).


**Constraints:** 

  * :math:`n < 10000`,
  * :math:`0 \leq a_i \leq 10^9`, (:math:`i=0,\ldots,n-1`).

**Sample Input:**

  .. code-block:: text
	
    9
    1 2 0 3 0 0 4 0 5
	  
**Sample Output:**

  .. code-block:: text
	
    5 2 3 4 1
	
**Explanation:** 
  The first line of the input contains the number of integers to read (:math:`n=9` in this case).
  After exchanging the first and the last elements, we get the list :math:`\{5,2,0,3,0,0,4,0,1\}`.
  After removing all zeroes we get the final list :math:`\{5,2,3,4,1\}`.
  
  If the input list starts or ends with a zero, these are removed as well. For example :math:`\{1,0,2,3,0\}`
  would at first become :math:`\{0,0,2,3,1\}`, and then :math:`\{2,3,1\}`.




sample5.cpp: Fitting Permutation
---------------------------------

Two arrays :math:`A` and :math:`B` contain :math:`n` positive integers
each. Let :math:`t` be positive integer -- named the *threshold*. 
Arrays :math:`A` and :math:`B` are in a relation: :math:`(A,B) \in R` if there exists
a permutation :math:`B'` of the array :math:`B` (a way to reorder elements 
of :math:`B`) such that :math:`A[i] + B'[i] \geq t` for all :math:`i = 0,\ldots,n-1`.

Write a C++ program that reads lines from the standard input and determines, 
if for a given thershold :math:`t` and two arrays :math:`A,B`, the 
pair :math:`(A,B)` is in relation :math:`R`.

Lines come in groups of three: The first line in 
each group contains a threshold number :math:`t`, 
followed by a list :math:`n` space-separated positive integers 
(representing array :math:`A`) and
then another :math:`n` space-separated positive integers (representing array :math:`B`). 
After that there is another group of three lines (possibly, with different values of :math:`t` and 
array length :math:`n`) and so on. Input is finished when there is a line containing just the digit ``0``.

**Constraints:** 

  * At most :math:`1000` subproblems (groups of three lines).,
  * :math:`1 \leq n \leq 1000`,
  * :math:`1 \leq t \leq 10^9`,
  * :math:`1 \leq A[i], B[i] \leq 10^9`.

**Sample Input**

.. code-block:: text

  11
  5 6 3 8 9
  8 2 6 5 6
  23
  12 14 12 7
  10 11 9 20
  0

**Sample Output:**
  
.. code-block:: text

  true
  false
	
**Explanation**  
  The first two arrays :math:`A = \{ 5,6,3,8,9 \}` and :math:`B = \{ 8,2,6,5,6 \}`
  are in the relation for threshold :math:`t = 11`. 
  For example, we can rearrange elements of the second array :math:`B' = \{ 6,5,8,6,2 \}`. 
  In this case :math:`A[i] + B'[i] = \{ 11,11,11,14,11 \}`

  The second two arrays  :math:`A = \{ 12, 14, 12, 7 \}` and :math:`B = \{ 10, 11, 9, 20 \}`
  are not in the relation for threshold :math:`t = 23`. 
  There are three numbers in :math:`A` (12,12,7) that would need to be added with numbers at least
  :math:`11` to add up to :math:`23`. On the other hand, there are just two 
  numbers :math:`\geq 11` in :math:`B`.
	

..  .. note:: 
..    Algorithmic tasks of this kind are known from other sources as well. 
..    See `HackerRank: Permuting Two Arrays <https://bit.ly/3tk8dlY>`_. 
  
  
 
