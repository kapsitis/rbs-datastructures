Assignment 01: Solution
========================

**Question1:**

  .. image:: figs/threepowers-solution.png
     :width: 250 px


  Unfortunately, there was a typo
  and a mismatch between the picture and the code.
  The code computes overflown value of :math:`3^{25}` (but the image
  in your assignment was, in fact, the binary representation of :math:`3^{24}`).
  
  Here are full values in hexadecimal notation: 
  
  .. math::
  
    \left\{ \begin{array}{l}
	3^{24} = \mathtt{0x41c21cb8e1} \\
	3^{25} = \mathtt{0xc546562aa3} \\
	\end{array} \right.

  After they are truncated (so that only the youngest 4 bytes remain),
  we get ``pow`` value ``0xc21cb8e1`` or value ``0x46562aa3``
  respectively. 
  
  .. note: 
    The purpose of the exercise was to remind about hexadecimal. 
	You will get full points - no matter which number you 
	converted into hexadecimal. 
	It relies on applying a table; see 
	explanation in `<https://bit.ly/2V9AFud>`_. 
	
  The sign depends on what is the fourth byte from the right
  (see purple arrows in the figure above). In particular, 
  multiplying :math:`3` with itself 24 times would appear to be *negative*, 
  but multiplying it with itself 25 times would appear to be *positive*.
  Here is a full program:
  
  .. code-block:: cpp
  
    #include <iostream>
  
    using namespace std;
    int main() {
        int pow = 1;	
        for (int i = 0; i < 25; i++) { pow *= 3; }
        int val = 0x46562aa3;  // Write a 4-byte hex value to get "Success"
        if (pow == val) { cout << "Success\n"; }
				
        if (pow < 0) { cout << "3^25 is negative" << endl; }
        if (pow > 0) { cout << "3^25 is positive" << endl; }
        if (pow == 0) { cout << "3^25 is zero" << endl; }

        // Optionally, you can also print "pow"  
        // as hexadecimal and as decimal to inspect.
        cout << "pow(as hex) = " << std::hex << pow << endl;
        cout << "pow(as dec) = " << std::dec << pow << endl;
    }
	
  The output is the following: 
  
  .. code-block:: text
    
    Success
    3^25 is positive
    pow(as hex) = 46562aa3
    pow(as dec) = 1180052131

  .. note::
     Operating with large numbers on ``int`` variables 
     may cause frequent overflows and unpredictable switches 
     between positive and negative values. 
	
	
	


**Question2:**

  The loop executes three times. 
  At the end of every loop iteration it ignores up to 1024 characters
  (or less than 1024 - until it reads the first newline ``\n`` character). 
  
  .. image:: figs/input-solution.png
     :width: 150 px
    
  Therefore, after all input operations 
  are complete, the third row is processed and the values are the following: 
  
  .. code-block:: text
  
     a = 13, b = 14, c = 15






**Question3:**

  .. image:: figs/assignment01-flowchart.png
     :width: 250 px  

  The C++ code snippet to implement this flowchart is the following:
  
  .. code-block:: cpp
  
    char ch = g1();
    while (ch == 'A') {
        ch = g2();
        if (ch == 'B') continue;
        ch = g3();
    }

  The big loop compares loop variable ``ch`` to some value at the beginning
  (this indicates that it is the ``while`` loop). Moreover, there is 
  a special case when we jump back to the beginning of the loop 
  with ``continue``. 

