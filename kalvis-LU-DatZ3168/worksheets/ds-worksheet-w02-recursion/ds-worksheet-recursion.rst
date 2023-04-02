Worksheet Week 02: Recursion
===============================

There is a proverb: *To understand recursion, you must first understand recursion*. 
Recursion allows to analyze algorithms, to find their runtime even in 
complex cases. 


Concepts and Facts
----------------------


**Definition:** 
  A Fibonacci sequence is defined by the following recurrent formula: 


  .. math:: 
  
    F(n) = \left\{ \begin{array}{ll}
    0 & \mbox{if $n = 0$,}\\
    1 & \mbox{if $n = 1$,}\\
    F(n-1) + F(n - 2) & \mbox{if $n > 1$.}\\
    \end{array} \right.

**Statement:** 
  For every nonnegative integer :math:`n` the Fibonacci number :math:`F(n)` can be 
  computed by the following expression: 

  .. math:: 

    F(n) = \frac{1}{\sqrt{5}} \left( \left( \frac{1 + \sqrt{5}}{2} \right)^{\!n} - \left( \frac{1 - \sqrt{5}}{2} \right)^{\!n} \right).


Such expressions are named *closed formulas*, since they can be evaluated directly, without repeating recurrent formula many times. 
See its proof -- <https://brilliant.org/wiki/linear-recurrence-relations/>`_. 
The expression shows that (apart from an expression :math:`((1 - \sqrt{5})/2)^n` that goes to :math:`0`) Fibonacci numbers grow 
as a geometric series. 


**Definition:** 
  A factorial for any non-negative integer is defined by the following recurrent formula: 

  .. math:: 

    n! = \left\{ \begin{array}{ll}
    1 & \mbox{if $n = 0$,}\\
    n \cdot (n-1)! & \mbox{if $n > 0$.}\\
    \end{array} \right.

**Statement:** 
  Factorials for large :math:`n` satisfy 
  `Stirling's approximation <https://en.wikipedia.org/wiki/Stirling%27s_approximation>`_: 

  .. math:: 

    n! \sim \sqrt{2\pi n} \left( \frac{n}{e} \right)^n. 

.. note::
  The asymptotic equality :math:`f(n) \sim g(n)` for two positive functions :math:`f(n),g(n)` 
  denotes that the ratio :math:`f(n)/g(n)` has limit :math:`1` as :math:`n \rightarrow \infty`. 
  Such relation also would imply that :math:`f(n)` and :math:`g(n)` are in Big-Theta of each other. 
  In fact, :math:`f(n) \sim g(n)` is stronger than Big-Theta, since :math:`f(n) \in \Theta(g(n))` does allow 
  any finite and bounded ratios :math:`f(n)/g(n)`. 


**Definition:**
  Function code that invokes itself (with different arguments to avoid infinite loops) 
  is called a *function implemented with recursion*. 
  
  
**Example:** 
  This is a straightforward recursive implementation of factorial: 

  .. code-block:: python 

    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)

  For large ``n`` this implementation is problematic, since it keeps too many function calls 
  on the activation stack. 
  Therefore in practice factorial is usually implemented without recursion (one can multiply the numbers in a loop), 
  or using a tail recursion. 
  
**Definition:** 
  Function code that contain recursive call in just one place and the recursive call is 
  the entire return expression of the function is called *function implemented with tail-recursion*. 


**Example:** 
  Here is tail-recursive factorial: 

  .. code-block:: python 

    def factorial_tail(n, result): 
        if n == 0:
            return result
        else:
            return factorial_tail(n - 1, n * result)

Algorithms using divide-and-conquer paradigm (such as MergeSort, Quicksort)
may call themselves multiple times. In these cases we must be very careful regarding 
the depth of recursion tree as the number of function calls grows exponentially. 
Here is an extremely inefficient algorithm to compute Fibonacci numbers: 
any call to ``fibonacci_bad(n)`` (where :math:`n \geq 2`) leads to two more calls. 
Such implementations are called *excessive recursion*. 

**Example:** 


  .. code-block:: python
    
    def fibonacci_bad(n):
        if n <= 1:
            return n
        else:
            return fibonacci_bad(n - 1) + fibonacci_bad(n - 2)








**Master Theorem:**
  Let :math:`f(n)` be an increasing function that satisfies the recurrence relation:

  .. math::

    f(n) = a \cdot f \left( \frac{n}{b} \right) + cn^d

  Here we assume that :math:`n = b^k`, where :math:`k` is a positive integer, :math:`a \geq 1`,
  :math:`b>1` is an integer, :math:`c,d` are real numbers (where :math:`c>0` and :math:`d \geq 0`).
  Then the asymptotic growth for :math:`f(n)` can be found like this:

  .. math::

    f(n)\ \mbox{is in}\ \left\{ \begin{array}{ll}
    O(n^d), & \mbox{if $a < b^d$,}\\
    O(n^d \log n), & \mbox{if $a = b^d$,}\\
    O(n^{\log_b a}), & \mbox{if $a > b^d$.}\\
    \end{array} \right.


This theorem can be used to find the asymptotic runtime for recursive algorithms. 




**Example (Binary Search):** 
  Binary search searches items in a sorted array of :math:`n` elements: 
  :math:`A[0]<A[1]<\ldots<A[n-2]<A[n-1]`.
  At every point it maintains a search interval :math:`[\ell, r]` so that the searchable item :math:`w`
  satisfies inequalities :math:`D[\ell] < w < D[r]`.
  The initial call is :math:`\text{\sc BinarySearch}(A,0,n-1,w)`.
  After that the binary search calls itself recursively on shorter intervals:


  | :math:`\text{\sc BinarySearch}(D,\ell, r, w)`
  | 1. :math:`\;\;\;\;\;` **if** :math:`\ell > r`:
  | 2. :math:`\;\;\;\;\;\;\;\;\;\;` **return** :math:`\text{\sc not found}` :math:`w`
  | 3. :math:`\;\;\;\;\;` :math:`m = \lfloor (\ell + r)/2 \rfloor`
  | 4. :math:`\;\;\;\;\;` **if** :math:`w` ``==`` :math:`D[m]`:
  | 5. :math:`\;\;\;\;\;\;\;\;\;\;` **return** :math:`\text{\sc found}` :math:`w` at location :math:`m`
  | 6. :math:`\;\;\;\;\;` **else** **if** :math:`w < D[m]`:
  | 7. :math:`\;\;\;\;\;\;\;\;\;\;` **return** :math:`\text{\sc BinarySearch}(D,\ell, m-1, w)`
  | 8. :math:`\;\;\;\;\;` **else**:
  | 9. :math:`\;\;\;\;\;\;\;\;\;\;` **return** :math:`\text{\sc BinarySearch}(D,m+1, r, w)`

  Denote the  runtime of this algorithm on an array of length :math:`n` by :math:`T(n)`. 
  Denote by a constant :math:`K` the upper bound
  of the time necessary to compute the middlepoint :math:`m` on Line 3 and to do all the comparisons. 
  Use the Master's theorem to find the time complexity for :math:`T(n)`. 
  
  
.. only:: Internal 

  **Answer:** 
  
    The runtime :math:`T(n)` satisfies the following recurrence: 
  
    .. math:: 
  
      T(n) = \left\{ \begin{array}{ll}
      K, & \mbox{if $n = 1$,}\\
      K + T(\lfloor n/2 \rfloor), & \mbox{if $n > 1$.}\\
      \end{array} \right.
    
    In the Master's theorem :math:`a = 1`, :math:`b = 2`, :math:`c = K`, :math:`d = 0`. 
    Since :math:`a = b^d`, we have :math:`T(n) \in O(n^d \log n) = O(\log n)`. 
    We conclude that the :math:`\text{\sc BinarySearch}(\ldots)` algorithm runs in 
    logarithmic time :math:`O(\log n)`, where :math:`n` is the length of the array. 
  
  :math:`\square`





  
**Example (Hanoi Tower):** 
  You need to move a set of disks (enumerated :math:`1,2,\ldots,n` from smallest to largest) 
  from one peg to another, one disk at a time, while obeying the rule that a larger disk 
  cannot be placed on top of a smaller disk. You have altogether three pegs: ``from_peg`` is the peg, 
  where all the disks are placed originally (smallest disk :math:`1` at the top); ``to_peg`` is the peg, 
  where these disks must end up at the very end. And there is also ``aux_peg`` -- auxiliary peg that 
  can be used during the movements, but should be freed at the end. 

  .. code-block:: python 

    def tower_of_hanoi(n, from_peg, to_peg, aux_peg):
        if n == 1:
            print("Move disk 1 from peg {} to peg {}".format(from_peg, to_peg))
            return

        tower_of_hanoi(n-1, from_peg, aux_peg, to_peg)
        print("Move disk {} from peg {} to peg {}".format(n, from_peg, to_peg))
        tower_of_hanoi(n-1, aux_peg, to_peg, from_peg)


  The input of this algorithm is :math:`n` (the number of disks), its output is a valid schedule describing valid movements of the disks.   
  Let :math:`H(n)` denote the running time of this algorithm expressed as the number of ``print()`` statements. 
  Express :math:`H(n)` (the number of disk movements in the algorithm)
  in terms of previous values :math:`H(m)`, where :math:`m < n`. Solve the recursion and find a closed formula 
  for :math:`H(n)`. 

.. only:: Internal 

  **Answer:**
  
    The runtime :math:`H(n)` satisfies the following recurrence:
  
    .. math:: 
  
      H(n) = \left\{ \begin{array}{ll}
      1, & \mbox{if $n = 1$,}\\
      1 + 2 \cdot H(n-1), & \mbox{if $n > 1$.}\\
      \end{array} \right.  
  
    In this case Master's theorem cannot be applied, since :math:`H(n)` is expressed via :math:`H(n-1)` 
    rather than in terms of :math:`H(n/b)` for some constant :math:`b`. 
    Fortunately, :math:`H(n)` can be evaluated directly. 
    
    Observe that :math:`H(1) = 1`, :math:`H(1) = 1 + 2 \cdot H(1) = 3`, :math:`H(3) = 1 + 2 \cdot H(2) = 7`, and so on. 
    We observe that :math:`H(n) = 2^n - 1`. This can be proven by induction. 
    
    **Base:** 
      :math:`n = 1`. In this case :math:`H(1) = 1`, and also :math:`H(1) = 2^1 - 1`; so the formula :math:`H(n) = 2^n - 1` is 
      true in this case. 
      
    **Inductive Hypothesis:** 
      Assume that for :math:`n = k` disks the number of print statements is indeed :math:`H(k) = 2^{k} - 1`. 
      
    **Induction Step:** 
      We now prove that the statement is also true for :math:`n = k+1`. In this case :math:`H(k+1) = 1 + 2 \cdot H(k)` by 
      the given recurrent formula. On the other hand, by inductive hypothesis, 
      
      .. math:: 
      
        H(k+1) = 1 + 2 \cdot (2^k - 1) = 1 + 2 \cdot 2^k - 2 = 2^{k+1} + 1 - 2 = 2^{k+1} - 1. 
        
      We now see that :math:`H(k+1) = 2^{k+1} - 1`, which means that the formula :math:`H(n) = 2^n - 1` is also true 
      for :math:`n = k+1`. Inductive step is completed. 
      
  :math:`\square`
    


**Example (Karatsuba Multiplication Algorithm):** 
  Given two non-negative integer numbers of the same length :math:`n` (written in binary), 
  write an algorithm to multiply these numbers. 
  Consider an algorithm that is faster than the "school algorithm" (it would multiply two 
  numbers of length :math:`n` in :math:`O(n^2)` time):  
  
  | :math:`\text{\sc Karatsuba}(n_1, n_2)`
  | 1. :math:`\;\;\;\;\;` if :math:`(n_1 < 10)` **or** :math:`(n_2 < 10)`:
  | 2. :math:`\;\;\;\;\;\;\;\;\;\;` **return** :math:`n_1 \cdot n_2` :math:`\;\;\;\;\;` (*fall back to traditional multiplication*)
  | 3. :math:`\;\;\;\;\;` :math:`m = \max(\text{\sc size}(n_1), \text{\sc size}(n_2))`
  | 4. :math:`\;\;\;\;\;` :math:`m_2 = \lfloor m/2 \rfloor`
  | 5. :math:`\;\;\;\;\;` :math:`h_1, \ell_1 = \text{\sc splitAt}(n_1, m_2)`
  | 6. :math:`\;\;\;\;\;` :math:`h_2, \ell_2 = \text{\sc splitAt}(n_2, m_2)`
  | :math:`\;\;\;\;\;\;\;\;\;\;` (*Three recursive calls of Karatsuba's algorithm.*)
  | 7. :math:`\;\;\;\;\;` :math:`z_0 = \text{\sc Karatsuba}(\ell_1, \ell_2)`
  | 8. :math:`\;\;\;\;\;` :math:`z_1 = \text{\sc Karatsuba}(\ell_1 + h_1, \ell_2 + h_2)`
  | 9. :math:`\;\;\;\;\;` :math:`z_2 = \text{\sc Karatsuba}(h_1, h_2)`
  | 12. :math:`\;\;\;\;\;` :math:`y = z_1 - z_2 - z_0`
  | 13. :math:`\;\;\;\;\;` **return** :math:`(z_2 \cdot 10^{2 \cdot m_2}) + (y \cdot 10^{m_2}) + z_0`


  By :math:`T(n)` denote the runtime of Karatsuba's algorithm 
  on two numbers having length :math:`n` each. (Assume that non-recursive parts take some constant time :math:`K`.) 
  Provide the asymptotic bound extimate for :math:`K(n)`. 

  .. note::  
    We typically assume that addition and multiplication take :math:`\Theta(1)` time 
    as they are CPU operations. But multiplication of very long numbers cannot be done in constant time. 
    Instead assume that operations on individual bits
    are done in constant time. Things like Boolean operations, bit arithmetic, checking conditional statements.
 
.. only:: Internal

  **Answer:** 
  
    In this algorithm one call causes three recursive calls; each call has arguments that are half the size.
    It means that :math:`T(n) = 3 \cdot T(n/2) + K`. 
  
    In Master's theorem we would have :math:`a =3`, :math:`b = 2`, :math:`c = K`, :math:`d = 0`. 
    In this case :math:`a > b^d`, so :math:`{\displaystyle T(n) \in O\left( n^{\log_b a} \right) = O\left( n^{\log_2 3} \right)}`. 
    So the time complexity of this is :math:`O(n^{1.58})` which is significantly better than :math:`O(n^2)`. 
  
  
  :math:`\square`











Problems
------------

**Problem 1:** 
  Answer the following questions regarding the asymptotic behavior of functions. 

  **(A)**
    Have students generate 10 functions and order them based on asymptotic growth.

  **(B)**
    Find a tight asymptotic bound for :math:`\binom{n^2}{3168}`, and write it using the simplest notation possible. 

  **(C)**
    Find a simple, tight asymptotic bound for  :math:`f(n) = \log_2 \left( \sqrt{n}^{\sqrt{n}} \right) - \log_{10} \left(  \sqrt[3]{n}^{\sqrt[3]{n}}  \right)`. 

  **(D)** 
    Is :math:`2^n` in :math:`\Theta\left( 3^n \right)`? Is :math:`2^{2^{n+1}}` in :math:`\Theta\left( 2^{2^n} \right)`?

  **(E)**
    Show that :math:`(\log n)^a` is in :math:`O(n^b)` for all positive constants :math:`a`` and :math:`b`.

  **(F)**
    Let :math:`f(n) = \left( \log_2 n \right)^{\sqrt{n}}` and :math:`g(n) = \left( \log_{10} n \right)^{\sqrt{n}}`. 
    Is :math:`f(n)` in :math:`\Theta(g(n))`? 

  **(G)**
    Show that :math:`(\log n)^{\log n}` is in :math:`\Omega(n)`.

  **(H)**
    Is :math:`(2n)!` in :math:`O(n!)`? Is :math:`\sqrt{(2n)!}` in :math:`O(\sqrt{n!})`? Is :math:`\sqrt{\log_2((2n)!)}` in 
    :math:`\sqrt{\log_2(n!)}`



**Problem 2:** 
  Consider Euclid algorithm to find the greatest common divisor (written around 300 B.C. in *Elements*): 
  
  | :math:`\text{\sc EuclidGCD}(a,b)`
  | 1. :math:`\;\;\;\;\;` **if** :math:`b` ``==`` :math:`0`:
  | 2. :math:`\;\;\;\;\;\;\;\;\;\;` **return** :math:`a`
  | 3. :math:`\;\;\;\;\;` **else**:
  | 4. :math:`\;\;\;\;\;\;\;\;\;\;` **return** :math:`\text{\sc EuclidGCD}(b, a\;\text{mod}\;b)`

  It is known that for a given input length :math:`n` the worst-case running time is to run the algorithm on 
  subsequent Fibonacci numbers: :math:`F_m` and :math:`F_{m-1}`, where :math:`F_m` is the largest Fibonacci number of length 
  not exceeding :math:`n`. 
  

  Write a precise estimate (without using unknown constant factors as in Big-O notation) on how many calls of 
  :math:`\text{\sc EuclidGCD}(a,b)` are needed, if both inputs have length not exceeding :math:`n`. 

  .. note:: 
    
    Imagine that both arguments to the Euclid algorithm are two natural numbers :math:`a,b` containing up to :math:`100` digits each. 
    Estimate the maximum number of recursive calls until the grater common divisor is found. 





**Problem 3:** 
  Given a sequence :math:`a_i` (:math:`i = 0,\ldots,n-1`) we call its element :math:`a_i` a *peak*
  iff it is a local maximum (at least as big as any of its neighbors):

  .. math::

    a_i \geq a_{i-1}\;\;\text{and}\;\; a_i \geq a_{i+1}

  (In case if :math:`i=0` or :math:`i = n-1`, one of these neighbors does not exist; and in such cases we
  only compare :math:`a_i` with neighbors that do exist.)
  
  **(A)**
    Suggest an algorithm to find some peak in the given array :math:`A[0],\ldots,A[n-1]` and find its worst-case running time. 
  
  **(B)**
    Suggest an algorithm that is faster than linear time to find peaks in an array. Namely, its worst-case running time should satisfy the limit: 
	
	.. math::
	
	  \lim_{n \rightarrow \infty} \frac{T(n)}{n} = 0. 
	  


**Question 4:**
  Select the correct asymptotic complexity of an algorithm with runtime
  :math:`T(n, n)` where

  .. math::

    \left\{ \begin{array}{l}
    T(x, c) = \Theta(x)\;\mbox{for $c \leq 2$},\\
    T(c, y) = \Theta(y)\;\mbox{for $c \leq 2$, and},\\
    T(x, y) = \Theta(x + y) + T(\lfloor x/2 \rfloor, \lfloor y/2 \rfloor)\;\mbox{otherwise}.\\
    \end{array} \right.

  a. :math:`\Theta(\log n)`.
  b. :math:`\Theta(n)`.
  c. :math:`\Theta(n \log n)`.
  d. :math:`\Theta(n log^2 n)`.
  e. :math:`\Theta(n^2)`.
  f. :math:`\Theta(2^n)`.


**Question 5:** 
  Just like the tail-recursive factorial, write a tail-recursive Fibonacci program. This way you will also avoid excessive recursion -- 
  exponential increase of the number of recursive calls. 

  To achive this, you may need to pass multiple parameters in the recursive call to the recursive Fibonacci function.


.. only:: Internal

  **Answer:** 

  
  .. code-block:: python 

    # Tail Recursive function to calculate nth Fibonacci number
    def fibonacci_tail(n, a, b) -> int:
        if n == 0:
            return a
        else:
            return fibonacci_tail_recursive(n - 1, b, a + b)

    # Shows how to initialize the function's fibonacci_tail(...) arguments:
    def fibonacci_tail(n: int) -> int:
        return fibonacci_tail_recursive(n, 0, 1)
      
  :math:`\square`





**Question 6:** 
  It is known that Taylor series for :math:`y = \sin x`) is given by formula: 

  .. math:: 

    \lim_{n \rightarrow \infty} S(x,n) = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \ldots = \sin x. 

  The series converges for every :math:`x \in \mathbb{R}`.   
  Write a tail-recursive function that for any argument :math:`x` computes the approximation for :math:`\sin x`
  by adding up the first 50 terms of the Taylor series. 
  The use of global variables is not allowed -- all data manipulation should be done with local variables 
  function calls and their return values. 
  Your solution should use as few multiplications and divisions as possible. 
  

.. only:: Internal 

  **Answer:** 
  
    As the global variables are not allowed, we can accumulate the partial sum 
    as one of the arguments passed to the recursive method calls. 
    
    .. math:: 

      S(n, x) = \left\{ \begin{array}{ll}
      x & \mbox{if $n = 0$,}\\
      S(n - 1, x) + \frac{(-1)^n \cdot x^{2n-1}}{(2n-1)!} & \mbox{if $n > 0$.}\\
      \end{array} \right.

    For a constant :math:`x` build the sequence :math:`S(0,x), S(1,x), S(2,x), \ldots` using the recursive calls. 
    You can write a recursive function in pseudocode that computes :math:`S(50,x)`. 
    
    This answer is incomplete as the number of multiplications and divisions is not minimized.  
    In fact, computing :math:`x^{2n-1}` would require many multiplications; same as :math:`(2n-1)!`. 
    So you can try to optimize this further. 

  :math:`\square`    


