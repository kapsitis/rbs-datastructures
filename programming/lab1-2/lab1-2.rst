Programming Task 1, Part 2
============================

Place all the files in the directory ``ds-workspace-YourName/lab1-2``, 
commit and push it to your GitHub repository.

sample6.cpp: Finding a Peak in an Array of Pairs
-------------------------------------------------

Create a C++ program that reads a :math:`N` pairs --- elements of
type ``struct`` containing one string and another integer: ``{string s, int a}``
into a dynamically created array. 

The program should output any index in this array that contains a "peak" 
and also the number of times it called function ``compare`` on two pairs. 

**Definition of a Peak:** 
  In an array of pairs :math:`p_0,\ldots,p_{N-1}` an element :math:`p_i`
  is called a *peak* iff :math:`p_{i-1} \leq p_i` and :math:`p_{i+1} \leq p_i`. 
  In the case when :math:`i=0` or :math:`i=N-1` (and some of the neighbors do not
  exist, we only check the inequality with those neighbors that do exist). 

**Definition of order relation**
  Pair :math:`p_i=(s_i,a_i)` is less or equal than pair :math:`p_j=(s_j,a_j)` (write :math:`p_i \leq p_j`)
  iff either the string :math:`s_i` alphabetically precedes the string :math:`s_j`
  or both strings are equal, and the integers in both pairs 
  satisfy :math:`a_i \leq a_j`. 

.. note::
  The order relation of pairs where we first compare the first elements (and in case when they 
  are equal compare the second elements and so on) is called *lexicographic order*. 
  This ordering is used in this exercise. See `<https://bit.ly/3z6RoMt>`_.



.. code-block:: cpp

  #include <iostream>
  #include <string> 

  struct StrInt { string s; int a; };

  static int numOfCompareCalls = 0;

  // This function should return 0, if both structs are equal
  // It should return a negative number, if the struct "A" is less than "B"
  // It should return a positive number, if "A" is more than "B"
  int compare(StrInt A, StrInt B) {
    numOfCompareCalls++; // increment the counter of calls
    // ...
    // Your implementation of the comparison itself
    // ... 
  }

  // Your implementation of main()
  int main() {
    // Read number N from the standard input
    // Read N pairs from the standard input
    // Your efficient implementation of the peak function
    // ... 
    // On the last line output the number of calls 	
  }	


**Guidelines for your Implementation:**

  * All comparisons during peak finding should only use function ``compare`` 
    (this allows to track the number of comparisons). 
  * You can use ``string`` class in C++ (but avoid any predefined data 
    structures such as STL classes, ``vector`` types and so on).
  * Your algorithm of peak finding should be more efficient than linear search, 
    i.e. for large :math:`N` it should use considerably less than :math:`N` comparisons. 
    (Since reading :math:`N` from the standard input would still take :math:`O(n)` time, 
    the easiest way to measure efficiency is to count the ``compare()`` calls 
    in the static variable ``numOfCompareCalls``. 


	
**Constraints:** 

  * The total count of string-integer pairs :math:`N \in \{ 2, \ldots 10000 \}`.
  * Any string in a pair contains only alphanumeric ASCII characters (uppercase or lowercase Latin letters or digits).
  * Any string in a pair has length between :math:`1` and :math:`20`.
  * Any integer in a pair is between :math:`0` and :math:`10^9`.
  
  

	
**Sample Input:**
  
  .. code-block:: text

    10
    Chen 4
    Huang 2
    Li 6
    Liu 7
    Wang 0
    Wu 9
    Yang 6
    Zhang 5
    Zhou 4
    Zhao 7

**Sample Output:**
  
  .. code-block:: text
    
    PeakLocation 8	
    PeakValue (Zhou,4)
    Comparisons 7
	  
**Explanation:**
  In the given array of 10 elements there is only one peak (element that is next to last). 
  We output its location (its index in the zero-based array), the string-integer pair itself in parentheses, 
  and also the number of comparisons used. (Your number of comparisons may differ, but 
  for large :math:`N` it should not equal :math:`N` or :math:`N-1` (this would be considered
  inefficient).
  

