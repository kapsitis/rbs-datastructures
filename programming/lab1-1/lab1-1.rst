Programming Task 1, Part 1
============================

Do as many of the questions as you can.
Follow the naming conventions of the source files as this 
directly affects the grading process.


**Exercise 01**
  Create a C++ program that reads an array of integers (3 rows, 5 columns) into a two-dimensional array. 
  It should scan this array in the row-major order and find the value and the location of the largest number (and output its row and column).

  Your function should support the following call (you cannot change it): 
  
  .. code-block:: cpp
  
    #include <iostream> 
  
    // your implementation of findMax(...)
  
    int main() {
      int arr[3][5]; 
      // input the 3x5 array
	 
	  int i, j; 
	  val maxValue = findMax(arr, i, j); 
	  cout << "MaxValue = " << maxValue
	    << " found at arr[" << i << "," << j << "]" << endl;
    }



**Exercise02** 
  Write a C++ program that reads positive integers from the standard input 
  (and exits when it sees the integer ``0`` in input). 
  For each positive integer it swaps the 2nd and the 3rd digit (**from the left**). 
  Number left unchanged, if it has less than three digits.
  
  **Guideline:** Only use arithmetic operations and loops (do not use ``string``
  objects or other external libraries). 
  
  **Sample Input** 
  
  .. code-block:: text
  
    123456789 102 42 8 0
  
  **Sample Output** 
  
  .. code-block:: text
  
    132456789 12 42 8
  
 
