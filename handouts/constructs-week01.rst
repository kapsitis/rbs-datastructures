C++ Language Constructs: Week01
===============================

Simplistic C++ Programs
-----------------------

C++ allows procedural-style programs (just like C). 
Input and output is done using stream-operators 


A Minimal C++ Program
^^^^^^^^^^^^^^^^^^^^^

Program ``sample01.cpp`` adds two integer numbers, prints their sum. 
Pay attention to the signature of ``main()`` method (it should returns integer); 
near the end there is an optional line ``return 0`` which means that 
the process exited normally. 

.. literalinclude:: samples-week01/sample01.cpp
   :language: cpp
   :emphasize-lines: 4,10


Sample standard input (``STDIN``) for this program: 

.. code-block:: none

  3 5

Sample standard output (``STDOUT``) for this program and the input:

.. code-block:: none

  Enter two numbers:
  3 + 5 = 8
  

Reading Input with "while" Loop
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Program ``sample02.cpp`` reads and adds all positive numbers on a single line; it ignores all input 
after the first negative number or zero (as well as all input on subsequent lines). 

* It reads standard input line by line; command ``getline`` reads everything up to a newline symbol into 
  a ``string`` variable ``line``. 
* It builds  a string-stream object ``lineStream`` to read from this input.
* It starts reading integer numbers from this input (every integer ends with some whitespace). 
* It exits the loop as soon as the end of the first line is reached (or there is a negative number in the input). 


.. literalinclude:: samples-week01/sample02.cpp
   :language: cpp
   :emphasize-lines: 9,10,12

  
Sample standard input (``STDIN``) for this program: 

.. code-block:: none

  3 5 7 9 -1 3 3 3
  2 4 6

Sample standard output (``STDOUT``) for this program and the input:

.. code-block:: none

  Total is 24



Reading Input with "for" Loop
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Program ``sample03.cpp`` asks the user to input the count of numbers ``n``. 
After that it reads all ``n`` integers and adds them up. 
Note that the ``for`` loop consists of three parts separated with semicolons
(initialization of the loop variable, 
loop condition and increment that is done after each loop iteration). 


.. literalinclude:: samples-week01/sample03.cpp
   :language: cpp
   :emphasize-lines: 11

  
Sample standard input (``STDIN``) for this program: 

.. code-block:: none

  10
  1 2 3 4 5 6 7 8 9 10


Sample standard output (``STDOUT``) for this program and the input:

.. code-block:: none

  Enter the count of numbers: 
  Enter 10 integers: 
  The total of 10 numbers is 55



Fixed-size Arrays
-----------------

.. code-block:: cpp

  const int m = 3;
  const int n = 4;
  int arr[m][n]={{3, 8, 4, 6},
                 {2, 7, 1, 5},
                 {0, 9, -1, 2}};




Integer Data Types
------------------

Register overflow happens silently without warning: 

.. code-block:: cpp

  int numbers[5] = {1000000001, 1000000002, 
                    1000000003, 1000000004, 1000000005};
  int sz = sizeof(numbers)/sizeof(int);  // assigns array size (=5).
  int iTotal;             // 4 byte register (signed)
  long unsigned luTotal;  // 4 bytes register (unsigned)
  long long llTotal;      // 8 bytes register (signed)
  for (int i = 0; i < sz; i++) {
    intTotal += numbers[i];
	luTotal += numbers[i];
	llTotal += numbers[i];
	cout << i << "-th partial sum is " << intTotal << "(int), "
      << luTotal << "(long unsigned), " 
      << llTotal << "(long long)." << endl;	
  }


Float Data Types
-----------------

.. code-block:: cpp

  int success = 4;
  int total = 7; 
  cout << "Wrong proportion: " << 1.0*(success/total) << endl;
  cout << "Correct proportion: " << (1.0*success/total) << endl;
  // output exactly 6 decimal places: 
  cout << fixed << setprecision(6) << (1.0*success/total) << endl;
  

Text Data Types 
---------------

.. code-block:: cpp

  int n = 5;
  void staircase(int n) {
    for (int i = 1; i <= n; i++) {
      string spaces(n-i,' ');
      string hashes(2*i, '#');
      cout << "'" << spaces << hashes << spaces << "'" << endl;	  
    }
  }

This will output the following triangle: 

.. code-block:: 

  '    ##    '
  '   ####   '
  '  ######  '
  ' ######## '
  '##########'
  



Vectors
-------

Vectors are list-like objects that can hold objects of the same type, for example, 
``vector<int>`` means a vector of ``int`` variables (4-byte integer numbers).
See `Initialize a vector in C++ <https://www.geeksforgeeks.org/initialize-a-vector-in-cpp-different-ways/>`_.

.. code-block:: cpp

  // initialize a vector with the given elements
  vector<int> primes{2,3,5,7,11,13,17,19,23,29};
    

.. code-block:: cpp

  int vectorSumAsArray(vector<int> v) {
    int result = 0;	
    for (int i = 0; i < v.size(); i++) {
      result += v[i];
    }
    return result;
  }

If you want to access vector without using "array syntax" (``v[i]``), 
you can use method ``v.at(i)`` to access :math:`i`-th element of a vector. 
In this case we have a square-sized 
vector of vectors and add up the elements on its diagonal:

.. code-block:: cpp

  int diagonalDifference(vector<vector<int>> vv) {
    int diag = 0;
    for (int i = 0; i < arr.size(); i++) {
      diag += arr.at(i).at(i);
    }
    return diag;
  }




Here is another method to operate with vectors: create iterator and loop over it.
For vectors it is not much different from the above method (accessing vector like an array). 
But for some data structures iterator is more flexible as it does not need to know the size 
of the data structure.

.. code-block:: cpp

  int vectorSumWithIter(vector<int> v) {
    int result = 0;
    for (vector<int>::iterator it = v.begin(); it != v.end(); ++it) {
      result += *it;
    }
    return result;
  }
  


Exercises
----------

1. Input file contains a positive array size :math:`n` and after that there are :math:`n` 
   integers. Find the count of sign flips (when a positive number 
   is immediately followed by a negative number or vice versa). 
   
**Input:** ``0 -2 0 -10 2 -1 0 0 3 2 -3``
   
**Output:** ``3``
   
*Explanation:* ``10`` is followed by ``2``, ``2`` is followed by ``-1``, ``2`` is followed by ``-3``.
   
2. Input file contains positive integers :math:`m` and :math:`n`; after that there are :math:`m \cdot n` 
   integers - a rectangular matrix with :math:`m` rows and :math:`n` columns; the matrix is input row
   by row. 
   
   Replace every matrix element :math:`a_{ij}` by the smallest element of a submatrix 
   :math:`A’(i,j)` (this submatrix has size :math:`i \times j`; it is located in the upper left corner 
   of the original matrix :math:`A`. 
   
**Input:** 

.. code:: none

   3 4
   3 8 4 6
   2 7 1 5
   0 9 -1 2
   
**Output:** 

.. code:: none
   
   3 4
   3 3 3 3
   2 2 1 1
   0 0 -1 -1

Is it possible to compute the result without allocating new memory to hold :math:`O(mn)` integers?
   
.. 1sem/A4_uzd/main.cpp

3. The input contains :math:`n`, the count of numbers followed by :math:`n` integers. 
   Find the smallest integer and also find, how many numbers are equal to this smallest integer. 