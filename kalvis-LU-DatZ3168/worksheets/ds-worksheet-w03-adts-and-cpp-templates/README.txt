Define lists; consider array-lists (amortised complexity); also linked lists of various types. 
After that define ADTs. 
Describe how to implement fixed-size and container classes in C++ or Python. 

Introduction
---------------

Some stuff from Python: 

```
L = ["Cacophony", "Imbibe", "Writhe", "Ubiquitous", "Paradox"]
S = {"Cacophony", "Imbibe", "Writhe", "Ubiquitous", "Paradox"}
```





**Questions**

1. Is a list in Python ordered? (I.e. can we visit its elements in a predictable order?)
   Is a set in Python ordered?
2. Assume that you want to store a large alphabetically sorted dictionary in Python to enable 
   binary search (it has :math:`O(\log n)` runtime).
   Is it a set of words or a list of words?
3. Occasionally we need to insert new words in that Python data structure. 
   What precautions should be taken to avoid 


Discuss concepts: 

* *Extrinsic order:* (imposed by they way data structure is built) vs. *intrinsic order* (wholly depends 
  on the properties of the items themselves). List by definition is ordered (as a sequence of 
  items :math:`a_0,a_1,\ldots,a_{n-1}`); it can also be sorted. Set is ordered, but there are no 
  *extrinsic* indices to access its elements. 
* *Representation invariant:*  
* *Mutable data structure:* (). 
  Immutable objects are easier to pass as arguments to functions (passing a reference is always fine). 
  They make functions more *mathematical* and easier to debug. 





```
for item in sorted(S):
    print(i)
elevation = dict()
elevation[(0,0)] = 3
elevation[(0,1)] = 4

other_dict = { [0,0]: 3, [0,1]: 4} 
# What is "unhashable type"?

a = [0, 1]
a.insert(1,a)
a[1][1][0]
a[1][1][1]
```



Lists -- Redundant, but Convenient ADTs
-------------------------------------------


# Constructor: Create an empty list
List<T> L() 
# Initializer list: Create a list with some elements in it                    
List<T> L { item1:T, item2:T }   
# Insertion: Inserts an element at a specified position in the list.
L.insert(index:int, item:T)
# Deletion: Deletes the element at a specified position in the list. 
L.delete(index:int)
# Traversal: Accesses each element in the list List<T> in its order
for item in L { do something with the item }
# Search: Finds the position of the first entry of item (>= initialPosition)
find(item:T): int
find(item:T, initialPosition: int): int
# Access the item at a specified position
get(index:int): T 
# Concatenation: Combines two lists into a single list
concatenate(L1:List<T>, L2:List<T>): List<T>
# Sorting: Rearranges the list in sorted order
L.sort(): void
# Getting a sorted copy: Return a sorted copy of the list, but do not change the list
L.sortedCopy(): List<T>
# Slicing: Extract a fragment of the list from startPos (inclusive) to endPos (exclusive)
L.slice(startPos:int, endPos:int)
# Size: Returns the number of elements in the list.
L.size(): int



Examples in Python and C++ STD
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^




Mutable vs. Immutable Lists
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Mutable lists only: 

**Insertion:**
  Inserting an element at a specific position in the list

**Deletion:** 
  Removing an element from a specific position in the list

**Append elements:** 
  Adding an element to the end of the list

**Sorting elements (within the list):**
  Arranging the elements in a specified order

Both mutable and immutable lists support these operations: 

**Accessing elements:** 
  Retrieving elements at specific positions in the list

**Finding elements:**
  Searching for the first occurrence of an element in the list

**Copy-Sorting elements:** 
  Return a new list with elements arranged in a specified order

**Slicing:**
  Creating a new list that contains a range of elements from the original list

**Filtering:** 
  Creating a new list that contains only the elements that satisfy a certain condition

**Mapping:** 
  Creating a new list that contains the results of applying a 
  function to each element of the original list.




ADTs vs. Data Structures 
---------------------------

Some Classical ADTs 

- Sequence 
- Stack
- Queue
- Double-ended queue (DEQueue)
- Iterator

- Singly Linked Lists
- Doubly Linked Lists
- Array Lists
- Circular Arrays


Sequence ADT
^^^^^^^^^^^^^^




Stack ADT
^^^^^^^^^^



Queue ADT
^^^^^^^^^^^


Double-Ended Queue (DEQueue) ADT
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Iterator ADT
^^^^^^^^^^^^^^

In an iterator with :math:`n` items, the cursor typically has :math:`n+1` valid states (it can be 
right before any of the elements, or it can be at the very end). Iterators are convenient 
to write iterative **for** loops or otherwise process items one by one (as in bulk insert operations, 
reading items from an input buffer, etc.). 


# Traversal: Accesses the next element in the iterator and moves 1 step ahead
it.next()
# Checking for more elements: Checks if there are more elements without moving 1 step ahead
it.hasNext():
# Removing the current element: Removes the current element from the data structure, point to the next one
it.remove();
# Peeking the current element: Returns the current element without moving the iterator 1 step ahead
it.peek()
# Rewinding: Resets the iterator to the beginning of the data structure (right before the 1st element)
it.rewind()
# Skipping: Skips a specified number of elements in the data structure.
it.skip(n:int)
# Filtering: Filters elements in the data structure based on a given predicate.
it.filter(predicate:{item:T => isValid:Boolean})
# Mapping: (Lazy) apply of a given function to each element, returns another iterator. 
it.map(mapFunction:{item:T => value:U})





Case Study: Matching Parentheses
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``` text
correct: ( ) ( ( ) ) { ( [ ( ) ] ) }	
correct: ( ( ( ) ( ( ) ) { ( [ ( ) ] ) }	
incorrect: ) ( ( ) ) { ( [ ( ) ] ) }	
incorrect: ( { [ ] ) }	
incorrect: (
```

**Input:** 
  An array :math:`X` of :math:`n` tokens, each of which is either a grouping symbol, a
  variable, an arithmetic operator, or a number. 

**Output:** 
  True if and only if all the grouping symbols in :math:`X` match



| :math:`\text{\sc ParenMatch}(X[0..n-1])`:
| :math:`\;\;\;\;\;` :math:`S = \text{\sc emptyStack}()`
| :math:`\;\;\;\;\;` **for** :math:`i` **in** range(:math:`n`):
| :math:`\;\;\;\;\;\;\;\;\;\;` **if** :math:`X[i]` is an opening parenthesis:
| :math:`\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;` :math:`S.\text{\sc push}(X[i])`
| :math:`\;\;\;\;\;\;\;\;\;\;` **else** **if** :math:`X[i]` is a closing parenthesis:
| :math:`\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;` **if** :math:`S.\text{\sc empty}()`:
| :math:`\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;` **return** :math:`\text{\sc false}` *(nothing to match with)*
| :math:`\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;` **if** :math:`S.pop()` does not match the type of :math:`X[i]`:
| :math:`\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;` **return** :math:`\text{\sc false}` *(wrong type of parenthesis)* 
| :math:`\;\;\;\;\;` **if** :math:`S.\text{\sc empty}()`:
| :math:`\;\;\;\;\;\;\;\;\;\;` **return** :math:`\text{\sc true}` *(every symbol matched)* 
| :math:`\;\;\;\;\;` **else** 
| :math:`\;\;\;\;\;\;\;\;\;\;` **return** :math:`\text{\sc false}` *(some symbols were never matched)*






Case Study: Evaluation of Postfix Notation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``` text
# infix notation
2 * (17 - 1) + 3 * 4
# postfix notation
2  17  1  -  *  3  4  *  +
```


| :math:`\text{\sc PostorderEvaluate}(E: array[0..n-1])`: Int
| :math:`\;\;\;\;\;` :math:`stack = emptyStack()`
| :math:`\;\;\;\;\;` **for** :math:`i` **from** :math:`1` **to** :math:`n`:
| :math:`\;\;\;\;\;\;\;\;\;\;` **if** :math:`\text{\sc isNumber}(E[i])`:
| :math:`\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;` :math:`stack.\text{\sc push}(E[i])`
| :math:`\;\;\;\;\;\;\;\;\;\;` **else:**
| :math:`\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;` :math:`x1 = stack.\text{\sc pop}()`
| :math:`\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;` :math:`x2 = stack.\text{\sc pop}()`
| :math:`\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;` :math:`res = \text{\sc ApplyOp}(E[i], x1, x2)`
| :math:`\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;` :math:`stack.\text{\sc push}(res)`

**Question:** 
  Given the pseudocode for `\text{\sc PostorderEvaluate}(E)`, 
  write the current state of the stack right after the :math:`E[6]`, 
  i.e. the number :math:`4` is insered.


Case Study: Backtracker Object as ADT
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Here is an object-oriented way to solve Sudoku, 
N-Queens problem, and many more combinatorial tasks. 


In this example a backtracker object is a sort of iterator 
designed to visited all nodes of a rooted tree in the DFS order 
and display the first valid solution (or all valid solutions).  
Backtracker is usually inefficient (exponential time algorithm), 
but it can become more efficient, if it can establish early on that 
in the given subtree there are no more solutions (for example, 
one of the rules has been violated). 




| *(Initialize Backtracker with its initial state)*
| :math:`B = \text{\sc Backtracker}(s:\text{\em State})`
| *(Get moves available from the current state at the given tree level)*
| :math:`B.\text{\sc moves}(\text{\em level}:int):\text{\sc Iterator}<\text{Move}>`
| *(Is the move valid for the given backtracker state)*
| :math:`B.\text{\sc valid}(\text{\em level}:int, \text{\em move}:Move):\text{\sc Boolean}`
| *(Record the move to the backtracker -- move down in the search tree)*
| :math:`B.\text{\sc record}(}(\text{\em level}:int, \text{\em move}:Move)`
| *(Opposite to record -- undo the move to move up in the search tree)*
| :math:`B.\text{\sc undo}(}(\text{\em level}:int, \text{\em move}:Move)`
| *(Is the search successfully completed?)*
| :math:`B.\text{\sc done}(\text{\em level}:int):\text{\sc Boolean}`
| *(Output the successful state of the Backtracker object)*
| :math:`B.\text{\sc output}()`

Write the pseudocode for a function :math:`\text{\sc attempt}(\text{\em level}:int)` so as to 
find the first solution (or all solutions) starting with the backtracker object on 
level :math:`\text{\em level}`. 







Problems
----------

1. In some Python's implementations, the dynamic array is grown by :math:`n/8` whenever 
   the list overflows. Assume that :math:`r` is the ratio between inserts and 
   reads for this dynamic array. Find the value :math:`r` for which this growth 
   factor is the optimal one. 

2. Given a data structure implementing the
   Sequence ADT, show how to use it to implement the Set interface. 
   (Your implementation does not need to be efficient.)

3. What are the costs for each ADT operation, if a priority queue is implemented 
   as dynamic array?

4. Which operations become asymptotically faster, if list ADT is implemented as a doubly linked 
   list (instead of a singly linked list)? 

5. Write a pseudocode to implement the following two operations on the Backtracker object: 

   **(A)**
     :math:`\text{\sc findFirstSolution}(b:\text{\sc Backtracker})` -- a function that returns the
     first solution (in fact -- any 1 solution) for the given backtracker object. 

   **(B)**
     :math:`\text{\sc findAllSolutions}(b:\text{\sc Backtracker})`


**Problem 6:** 
  `Koch snowflake <https://en.wikipedia.org/wiki/Koch_snowflake>`_ consists of three sides. 
  Each side connects two vertices of an equilateral triangle :math:`ABC`. Consider, for example, 
  two points :math:`A` and :math:`B` and the edge connecting them :math:`e`.

  If the length of :math:`e` is :math:`1` unit or shorter, then :math:`AB` is connected by a straight line 
  segment. Otherwise, the segment :math:`AB` is subdivided into three equal parts: :math:`e_1, e_2, e_3`. 
  The middle part is complemented with two more line segments :math:`f_1` and :math:`g_1` to make 
  another equilateral triangle (with side length three times smaller than the :math:`ABC`). 
  Finally, the Koch snoflake's edge algorithm is called on each of the segments :math:`e_1, f_2, g_2, e_3`
  recursively. 
  
  The initial call for :math:`e = AB` is :math:`\text{\sc SnowflakeEdge}(e,0)`, where :math:`d = 0` is the initial depth 
  in the recursion tree. 
  Here is the pseudocode for the algorithm: 


  | :math:`\text{\sc SnowflakeEdge}(e, d): 
  | :math:`\;\;\;\;\;` **if** :math:`|e| \leq 1`:
  | :math:`\;\;\;\;\;\;\;\;\;\;` draw a straight edge :math:`e`
  | :math:`\;\;\;\;\;` **else**: 
  | :math:`\;\;\;\;\;\;\;\;\;\;` Split :math:`e` into three equal parts :math:`e_1, e_2, e_3`
  | :math:`\;\;\;\;\;\;\;\;\;\;` Construct a regular triangle out of edges :math:`e_2, f_2, g_2` to the "outside"
  | :math:`\;\;\;\;\;\;\;\;\;\;` :math:`\text{\sc SnowflakeEdge}(e_1, d+1)`
  | :math:`\;\;\;\;\;\;\;\;\;\;` :math:`\text{\sc SnowflakeEdge}(f_2, d+1)`
  | :math:`\;\;\;\;\;\;\;\;\;\;` :math:`\text{\sc SnowflakeEdge}(g_2, d+1)`
  | :math:`\;\;\;\;\;\;\;\;\;\;` :math:`\text{\sc SnowflakeEdge}(e_3, d+1)`

  In this algorithm we assume that the Koch snowflake is drawn as vector graphics on a device 
  with infinite resolution. 

  **(A)**
    How 
