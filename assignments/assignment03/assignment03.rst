Written Assignment03
=======================

Questions 1,2 are done in class (or submitted remotely). Question 3 is submitted by Friday, 
Septeber 17, 2021 by checking it into GitHub repository, directory ``assignment-week03``.


**Question1:**
  
  Fill in the table. 
  For each of the given functions find a valid upper asymptotic bound (:math:`O(g(n))` or 
  Big-O notation), and also a valid lower asymptotic bound (:math:`\Omega(g(n))` or 
  Big-Omega notation). 
  Try to make both bounds tight and use the simplest possible functions :math:`g(n)` in both notations. 
  
  .. https://sublime-and-sphinx-guide.readthedocs.io/en/latest/tables.html  
  
  .. list-table:: 
     :widths: 43 25 32
     :header-rows: 1

     * - Function to analyze
       - Upper bound (Big-O)
       - Lower bound (Big-Omega)
     * - :math:`f(n) = (15n)^7`
       - 
       - 
     * - :math:`f(n) = 0.5n^2 + (10 + \sin n)n^{1.5}+999`
       - 
       - 
     * - :math:`f(n) = n \cdot (1 + \sin n)`
       -
       - 
     * - :math:`f(n) = \log_{\log_2 3} \left( (\log_2 n)^{100} \right)`
       - 
       - 
  
  

**Question2:**

  Assume that array ``A`` contains :math:`n` values, function ``Random()`` 
  generates a random number between :math:`0` and :math:`n-1` in constant time, but 
  ``sort()`` sorts an array of size :math:`n` in :math:`\Theta(n \cdot \log n)` steps. 


  
  .. code-block:: text
  
    for (i=0; i<n; i++) {
      for (j=0; j<n; j++) {
        A[j] = Random(n);
      }
      sort(A, n);
    }  

  Determine a function :math:`g(n)` such that the 
  execution time of the above code is :math:`\Theta(g(n))`. 
  Assume that all variables and arrays have type ``int``.


**Question3 (submit by Friday):**

  Below is a code using the built-in function ``std::sort``
  (from the module ``algorithm`` 
  to sort pairs of integers in ascending order using 
  a user-defined comparison function ``Pair_cmp``. 
  
  A pair :math:`(a_1,b_1)` is less or equal to another pair :math:`(a_2,b_2)` 
  iff any one of the two conditions holds: 
  
    * either :math:`a_1 < a_2`
    * or :math:`a_1 = a_2` and :math:`b_1 \leq b_2`.

  Declare a ``struct`` type ``Pair`` and a function to perform comparison 
  between two pairs. See `<https://bit.ly/3kbeq0t>`_ for a code example
  that passes a custom function to the ``std::sort`` algorithm.
  
  .. code-block:: cpp
  
    #include <iostream>
    #include <vector>
    #include <algorithm>
	
    // Your definition of struct Pair	

    bool Pair_cmp(Pair const &left, Pair const &right) {
      // print out the pair you are comparing: "(...,...) vs. (...,...)" 
      // do the comparison itself. Return true iff left <= right
    }

    int main() {
      vector<Pair> vv{
        {7, 2}, {7, 7}, {5, 5}, {3, 4}, {5, 1}, {7, 3}, {3, 6}};
      std::sort(vv.begin(), vv.end(), Pair_cmp);
      for (vector<Pair>::iterator it = vv.begin(); it != vv.end(); ++it) {
        Pair_print(*it);
        cout << " ";
      }
      cout << endl;
    }

  **Sample Output:**  

  .. code-block:: text
  
    (7,2) vs. (7,7)
    (5,1) vs. (7,2)
    (3,6) vs. (5,1)
    (5,5) vs. (3,6)
    (5,5) vs. (7,7)
    (5,5) vs. (7,2)
    (5,5) vs. (5,1)
    (7,3) vs. (3,6)
    (7,3) vs. (7,7)
    (7,3) vs. (7,2)
    (3,4) vs. (3,6)
    (3,4) (3,6) (5,1) (5,5) (7,2) (7,3) (7,7)
	
  .. note::
    Count how many comparisons were used by ``std::sort`` algorithm to sort the vector of 7 elements. 
    (It depends on your input data and the comparison algorithm; it could differ from the sample 
    output shown above.) The observed number of comparisons is often between :math:`11` and :math:`19`.
    The theoretical minimum	of comparisons to sort a 7-element array is :math:`\left\lceil \log_2 (7!) \right\rceil = 13`. 
    See `<https://bit.ly/3ElXbl9>`_.