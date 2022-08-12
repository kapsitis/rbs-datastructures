Written Assignment01
=======================

Questions 1,2,3 are done in class on paper (or submitted to ORTUS by remote students). 
Question 4: Please submit by Friday, September 3, 2021 to the class GitHub repository. 

**Question1:**

  .. image:: figs/threepowers.png
     :width: 250 px


  As shown in the figure, the number :math:`3^{25}=847288609443`: takes five bytes (but C++ ``int`` 
  variable only has 4 bytes). 
  What 4-byte integer value ``val`` is equal to this power? 

  .. code-block:: cpp
  
    int pow = 1;
    for (int i = 0; i < 25; i++) { pow *= 3; }
    int val = 0x...;  // Write a 4-byte hex value to get "Success"
    if (pow == val) { cout << "Success\n"; }
	

  (1A) Find hex value for ``int val`` to equal :math:`3^{25}`: __________
  
  (1B) What is the sign of ``val`` (positive or negative and why?): __________


**Question2:**
  
  .. code-block:: cpp
  
    int a, b, c;
    for (int i = 0; i < 3; i++) {
      cin >> a >> b >> c; 
      cin.ignore(1024,'\n');
    }

  The input file looks like this: 
  
  .. code-block:: text
  
     1 2 3 4 5 6
     7 8 9 10 11 12
     13 14 15 16 17 18
     19 20 21 22 23 24
  
  What values will be assigned to the variables ``a,b,c`` after 
  the input/output operations are complete. 


**Question3:**
  Write a C++ code snippet that implements the flowchart given in the Figure.

  .. image:: figs/assignment01-flowchart.png
     :width: 250 px  


**Question4 (submit by Friday):**
  Write a C++ program that reads positive integers from the standard input (and exits when it sees the integer ``0`` in input). 
  For each positive integer it swaps the 2nd and the 3rd digit (from the right). 
  Number left unchanged, if it has less than three digits. 
  
  **Sample Input** 
  
  .. code-block:: text
  
    123456789 42 8 0
  
  **Sample Output** 
  
  .. code-block:: text
  
    123456879 42 8
  
  
