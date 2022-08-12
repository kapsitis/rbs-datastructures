Written Assignment 12
======================

**Introduction:**	
  Let :math:`[c_1,\ldots,c_m]` be a list of :math:`m` characters in the alphabet :math:`\mathcal{A}` 
  of all the first 256 Unicode symbols (Latin-1 charset or ISO 8859-1 code table).  
  The picture below shows Microsoft's implementation of the
  ISO 8859-1 (Latin-1) -- it was taken from `<https://bit.ly/30GRuj0>`_.
  
  
  .. figure:: figs-rolling-hash/fnt-mswin.png
     :width: 3.5in
     :alt: ISO 8859-1 charset 

     Caption
  
  
  A rolling hash function is defined by a polynomial: 
  
  .. math:: 
  
    \left\{ \begin{array}{l} 
    h([]) = 0,\\
    h([c_1,\ldots,c_m]) = \left( c_1 a^{m-1} + c_2 a^{m-2} + \ldots + c_{m-1} a^1 + c_m a^0 \right)\,\text{mod}\,q 
    \end{array}
    \right.

  In this formula the numeric base :math:`a = 256` (its powers are used in the polynomial above), and the remainders are modulo :math:`q = 29`.



**(A)**
  Consider the following text: 
  
  .. code-block:: text

    RDBabc Lorem ipsum dolor...

  Replace the lower-case letters "a", "b" and "c" in the above text by the digits in your Student ID.
  For example, if your student ID ends with ``RDB389``, then your text is   
  ``"RDB389 Lorem ipsum dolor..."``
  


**(B)**
  We build a hash value for the window size :math:`m=4` and call the respective rolling hash ADT functions. 
  For example, if your student ID ends with ``RDB389``, you make the following calls:
  
  | Line 1: :math:`rH` ``:=`` :math:`\text{\sc RollingHash}(\mathtt{[]})`
  | Line 2: :math:`rH.\text{\sc append}(\mathtt{R})`
  | Line 3: :math:`rH.\text{\sc append}(\mathtt{D})`
  | Line 4: :math:`rH.\text{\sc append}(\mathtt{B})`
  | Line 5: :math:`rH.\text{\sc append}(\mathtt{3})`
  | Line 6: :math:`rH.\text{\sc skip}(\mathtt{R})`
  | Line 7: :math:`rH.\text{\sc append}(\mathtt{8})`
  | Line 8: :math:`rH.\text{\sc skip}(\mathtt{D})`
  | Line 9: :math:`rH.\text{\sc append}(\mathtt{9})`
  
  
  Show the value of the rolling hash after each line in :math:`[1;7]`. Show how to compute each value 
  from the previous one (without re-evaluating the polynomial formula every time).   
  Fill in the following table to show your results:
  
  ============  =============  ==============
  Line number   Expression     Numeric Value
  Line 1
  Line 2
  Line 3
  Line 4
  Line 5
  Line 6
  Line 7
  Line 8
  Line 9
  ============  =============  ==============
  

**(C)** 
  Compute the value :math:`h([\mathtt{B}, \mathtt{3}, \mathtt{8}, \mathtt{9}])` directly to check your result. 
  (Once again, replace the digits "3", "8", "9" with your actual Student ID digits.) 

