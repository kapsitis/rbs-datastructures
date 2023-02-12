Worksheet Week 01: Asymptotic Bounds
======================================

Introduction
--------------

**Goal:**  
  The focus of this course is efficiency -- creating algorithms that can work on
  large input data and handle complex structures sufficiently fast.


**Why use Big-O Notation?** 
  It is convenient to measure speed of algorithms -- for example, to find the best algorithms for 
  a given problem. Or to find out which problems are easy (have fast algorithms) and which ones are hard 
  (have only slow or unfeasible algorithms). 
  
  * Measuring the speed should not depend on the speed of the computing hardware -- do not care about constant factors. 
  * Measuring the speed should not depend on how fast it works on very short inputs. (One can "cheat" for short inputs -- 
    just remember a large lookup table containing values for inputs of length :math:`n < n_0` with precomputed correct answers.
    Clearly, this does not tell us anything about the performance of this algorithm for arbitrary inputs.)
  * Measuring the speed should be conceptually easy, it should not take into account insignificant optimizations or count too many extra factors. 
    
**Example:** 
  Energy needed to lift a stone of mass :math:`m` to the height :math:`h` is :math:`mgh`. (Is this 
  the best-case estimate? The worst-case estimate? The exact value?)


Running Time as a Complexity Measure
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**The Worst Running Time function:** 
  Given an algorithm, denote by :math:`T(n)` 
  the number of elementary steps that are needed to complete the algorithm for any input of length :math:`n`.
  (It can be called the *upper bound* of the running time.)
  
**Discussions on the Worst-Case Running Time:**

  * Is :math:`T(n)` the upper bound also for inputs shorter than :math:`n`?
  * Is :math:`T(n)` a non-decreasing function (i.e. do longer inputs always imply a longer running time)?
  * What counts as an elementary step? (Any CPU instruction? One line in a pseudocode? One comparison in a sorting algorithm?)
  * Let :math:`T(n)` be a numeric algorithm receiving single natural numbers as input. 
    Does the worst running time function change, if the input numbers are provided in binary (instead of decimal) notation? 
  * What is the worst running time to multiply two square matrices of size :math:`n \times n`? 
    What is the size of input in this case?

Sometimes it is common to have :math:`n` as some important parameter of the input data (not necessarily the exact size of its encoding). 
For matrix tasks -- the size of the matrices :math:`n`. For graph problems -- the number of vertices :math:`n` and the number of edges :math:`m`. 

**Example:**
  In order to multiply two :math:`n \times n` matrices using the "school algorithm", we spend :math:`n` multiplications 
  and :math:`n-1` additions to calculate one entry in the result matrix. For example: 

  .. math::

    c_{ij} = a_{i1} \cdot b_{1j} + a_{i2} \cdot b_{12} + \ldots + a_{in} \cdot b_{nj}  = \sum_{k=1}^{n}  {ik} \cdot b_{kj}.

  That is :math:`O(n)` time. To complete the calculation for the entire matrix :math:`C = A\cdot B` we 
  should compute :math:`n^2` such entries (for each pair :math:`i,j \in \{ 1, \ldots, n`). 
  So the total running time for matrix multiplication is :math:`O(n^3)`. 

**Note 1:**
  In strong accordance to the definition of the runtime, we should take into account that the lengh of input 
  for a matrix muliplication task is :math:`2n^2` -- you need to input two matrices of size :math:`n \times n`. 
  If we denote this input length by :math:`m = 2n^2`, then the running time becomes
  :math:`O(n^3) = O(m^{1.5}) = O(m \sqrt{m})`, so it no longer looks as terrible. 
  In theory books people still express the running time for matrix multiplication in terms of 
  matrix size (not the square of the matrix size) -- just because it is a more convenient parameter. 

**Note 2:** 
  There exist faster algorithms than the "school algorithm". For example,
  `Strassen algorithm <https://en.wikipedia.org/wiki/Strassen_algorithm>`_. 
  It has runtime :math:`O(n^{\log_2 7}) \approx O(n^{2.807})` where :math:`n` is the size of the matrices being multiplied. 
  The exponent :math:`\log_2 7` is smaller/better than :math:`\log_2 8 = 3`. 
  To see actual performance gains (where Strassen algorithm is faster than the "school algorithm"), 
  the matrices should be huge -- the size of matrix :math:`n` is multiple thousand. 

  In 2022 the fastest bound for matrix multiplication was discovered. It is :math:`O(n^{2.37188})`; 
  see `Matrix Multiplication Algorithm <https://en.wikipedia.org/wiki/Matrix_multiplication_algorithm>`_.


**Note 3:** 
  Matrix multiplication is of large practical importance (computer graphics, neural networks, etc). 
  The theory of Big-O notation disregards constant factors -- runtime of  :math:`T(n) = n^3` or 
  :math:`T(n) = 1000n^3` or :math:`T(n) = 0.001n^3` is considered to be of the same "cubic complexity". 
  But in practice it is common to use 
  GPU (massive parallel computations) to multiply matrices. Parallelism can  
  only speed up an algorithm by a constant factor, but sometimes even constant factors matter.


Definitions
^^^^^^^^^^^^^

**Definition of Big-O:** 
  Let :math:`g \colon \mathbb{N} \rightarrow \mathbb{R}_{0+}` be a function from natural numbers (non-negative integers)
  to non-negative real numbers.
  Then :math:`O(g)` is the set of all functions :math:`f \colon \mathbb{N} \rightarrow \mathbb{R}^{0+}`
  such that there exist real constants :math:`c>0` and :math:`n_0 \in \mathbb{N}` satisfying
  
  .. math:: 
  
    0 \leq f(n) \leq c \cdot g(n)\;\; \mbox{for all}\;\; n \geq n_0.


**Definition of Big-Omega:**
  Let :math:`g \colon \mathbb{N} \rightarrow \mathbb{R}_{0+}` be a function from natural numbers to non-negative real numbers. 
  Then :math:`\Omega(g(n))` is the set of all functions :math:`f \colon \mathbb{N} \rightarrow \mathbb{R}`
  such that there exist real constants :math:`c>0` and :math:`n_0 \in \mathbb{N}` satisfying
  :math:`{\displaystyle  \forall n \in \mathbb{N}\ \big( n \geq n_0 \rightarrow f(n) \geq c \cdot g(n) \big).}`

**Definition of Big Theta:**
  Let :math:`g \colon \mathbb{N} \rightarrow \mathbb{R}_{0+}` be a function from natural numbers to non-negative real numbers. 
  Then :math:`\Theta(g)` is the set of all functions :math:`f: \mathbb{N} \to \mathbb{R}`
  such that there exist positive constants :math:`c_1, c_2 > 0` and :math:`n_0 \in \mathbb{N}` satisfying

  .. math::

    \forall n \in \mathbb{N}\ \big( n \geq n_0 \rightarrow  0 \leq   c_1 \cdot g(n) \leq  f(n) \leq c_2 \cdot g(n) \big).


Informally, the following terms are also usable:

* If :math:`f(n) \in O(g(n))`, then :math:`g(n)` is called *asymptotic upper bound* of :math:`f(n)`.
* If :math:`f(n) \in \Omega(g(n))`, then :math:`g(n)` is called *asymptotic lower bound* of :math:`f(n)`.
* If :math:`f(n) \in \Theta(g(n))`, then :math:`g(n)` is called *asymptotic growth order* of :math:`f(n)`.


All these concepts (Big-O, Big-Omega, Big-Theta) are related to calculus (real analysis); it is functional behavior as :math:`n \rightarrow \infty`.
Predicting the speed of an algorithm for short input lengths :math:`n`, the dependence on :math:`n` is typically
quite complex (and we cannot ignore "lower order"  terms). As :math:`n` becomes very large,
only the "dominant parts" in the expression :math:`f(n)` matter.


Properties of Big-O, Big-Omega, Big-Theta
--------------------------------------------

**Big-O and Limit of the Ratio:**
  If the following limit exists and is finite:

  .. math::

    \lim\limits_{n \rightarrow \infty} \frac{f(n)}{g(n)} = C < + \infty,

  then :math:`f(n)` is in :math:`O(g(n))`.


**Big-O is transitive:**
  If :math:`f(n) \in O(g(n))` and :math:`g(n) \in O(h(n))`, then :math:`f(n) \in O(h(n))`.

**Sum of two functions:**
  If :math:`f(n) \in O(h(n))` and :math:`g(n) \in O(h(n))`, then :math:`f(n) + g(n) = O(h(n))`.

**Asymptotic Growth of Polynomials:**
  Any :math:`k`-th degree polynomial :math:`P(n) = a_k n^k + a_{k-1} n^{k-1} + \ldots + a_1 n + a_0` is in :math:`O(n^k)`.


**The Ordering of Polynomials:**
  Let :math:`k,j` be real numbers, :math:`n` a natural number.  
  The function :math:`n^k` is in :math:`O(n^{k+j})` for any positive :math:`j`. 

**Logarithms of any base:**
  If :math:`a,b > 1` are any real numbers, then :math:`\log_a n` is in :math:`O(log_b n)`. 

  **Proof:**
    The last result directly follows from the formula to change the base of a logarithm: 
    
    .. math:: 
      
      \forall a,b,m > 1 \left( \log_a b = \frac{ \log_m b }{ \log_m a } \right).


  **Note:**
    It is common to just one base (usually, it is base :math:`2` or
    base :math:`e` of the natural logarithm), and write just :math:`O(\log n)` 
    without specifying base at all. Formally speaking :math:`\log n` in our 
    course denotes :math:`\log_2 n`. 
    
    In other contexts (outside Big-O notation, 
    where constant factors matter)
    the base of logarithm cannot be omitted. 






Problems
------------

**Problem 1:**
  Are the following statement true or false? 
  Prove or disprove them using the definitions of :math:`O(g(n))`, :math:`\Omega(g(n))` or :math:`\Theta(g(n))`:

  **(A)**
    :math:`f(n) = 13n + 7` is in :math:`\Theta(n)`. 

  **(B)**
    :math:`f(n) = 3n^2 - 100n + 6` is in :math:`O(n^2)`. (Verify the definition 
    that :math:`f(n) \in O(g(n))`, where :math:`g(n) = n^2`.)

  **(C)**
    :math:`f(n) = 3n^2 + 100n + 6000` is in :math:`O(n^2)`.

  **(D)**
    :math:`f(n) = 3n^2 - 100n + 6` is in :math:`O(n \sqrt{n})`.


.. only:: Internal 

  **Answer:** 
  
  **(A)**
    True. Select :math:`c_1 = 13`, :math:`c_2 = 14`, :math:`n_0 = 7`. We should verify 

    .. math:: 

      0 \leq c_1 \cdot n \leq f(n) \leq c_2 \cdot n. 

    Indeed, :math:`13n \leq 13n + 7`, since :math:`0 \leq 7`. 

    Also, :math:`13n + 7 \leq 14n`, since :math:`7 \leq n` (whenever :math:`n \geq n_0 = 7`). 

  **(B)**
    True. Select :math:`c = 3` and :math:`n_0 = 34`. 
    Let us verify the inequalities: 

    .. math:: 
      
      0 \leq 3n^2 - 100n + 6 \leq 3n^2. 

    For :math:`n \geq 34`, then 
    
    .. math::

      3n^2  - 100n + 6 \;\geq\; 3 \cdot 34 \cdot n - 100n + 6 = 2n + 6 \geq 0. 

    So, the expression is non-negative for sufficiently large :math:`n` (:math:`n \geq 34`).  

    The other inequality :math:`3n^2 - 100n + 6 \leq 3n^2`, since 
    :math:`-100n + 6 \leq 0` and :math:`6 \leq 100n`. 

  **(C)**
    True. Select :math:`c = 5` and :math:`n_0 = 100`.
    At this point (when :math:`n \geq 100`) you can prove that :math:`100n \leq n^2` and 
    :math:`6000 \leq n^2` and also :math:`3n^2 \leq 3n^2`. Add all three inequalities to get 
    :math:`3n^2 + 100n + 6000 \leq 5n^2`. 

  **(D)**
    False. To disprove that :math:`f(n) = 3n^2 - 100n + 6` is not in :math:`O(g(n))`
    where :math:`g(n) = n\sqrt{n}`, we show how to find an example value :math:`n \geq n_0`
    such that :math:`3n^2 - 100n + 6 > c \cdot n\sqrt{n}` for any positive constants 
    :math:`n_0, c`. 

    First, notice that :math:`3n^2 - 100 n + 6` is in :math:`\Omega(n^2)`, for example
    :math:`3n^2 - 100 n + 6 > n^2` whenever :math:`n \geq 34`.

    Let us consider some positive constant :math:`c`. 
    Then :math:`n^2 \geq c n \sqrt{n}` can be rewritten as :math:`\sqrt{n} \geq c` or :math:`n \geq c^2`. 
    Once you consider natural numbers :math:`n \geq \max(34,c^2)`, you will have 
    **both** inequalities :math:`3n^2 - 100 n + 6 \geq n^2` and 
    :math:`n^2 > c n \sqrt{n}`; combining them gives :math:`3n^2 - 100 n + 6 > c n \sqrt{n}`. 
  
  :math:`\square`



**Problem 2:**
  Let us have a zero-based dictionary :math:`D` with :math:`n` items
  from :math:`D[0]` to :math:`D[n-1]`.

  | :math:`\text{\sc LinearSearch}(D,w)`
  | 1. :math:`\;\;\;\;\;` **for** :math:`i` **in** :math:`\text{\sc range}(0,n)`:
  | 2. :math:`\;\;\;\;\;\;\;\;\;\;` **if** :math:`w` ``==`` :math:`D[i]`:
  | 3. :math:`\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;` **return** :math:`\text{\sc found}` :math:`w` at location :math:`i`
  | 4. :math:`\;\;\;\;\;` **return** :math:`\text{\sc not found}`

  Let :math:`T(n)` be the worst-case running time for this algorithm. 
  Find some asymptotic upper bound for :math:`T(n)` -- the "smallest" set :math:`O(g(n))` such that 
  :math:`T(n)` is in :math:`O(g(n))`. 

.. only:: Internal 

  **Answer:**

    You can pick :math:`g(n) = n` and argue that :math:`T(n)` is in :math:`O(n)`, i.e. 
    the search time is linear in size of the array :math:`n`.

    If you can assume that the dictionary :math:`D` contains entries in a sorted order, you could 
    use binary search instead. It has much better runtime complexity: 
    :math:`T(n) = \log_2 n`. 
  
  :math:`\square`


**Problem 3:**
  What is the worst running time to find, if the given input :math:`m` is a prime number. 
  Assume that the input :math:`m` is written in decimal notation using :math:`n` digits. 

  Primality testing is done by the following algorithm testing divisibility by  
  all numbers :math:`d \in \{ 2,3,\ldots,\lfloor \sqrt{m} \rfloor \}`: 

  | :math:`\text{\sc isPrime}(m)`
  | 1. :math:`\;\;\;\;\;` **for** :math:`d` **in** :math:`\text{\sc range}(2, \sqrt{m} + 1)`:
  | 2. :math:`\;\;\;\;\;\;\;\;\;\;` **if** :math:`m` ``%`` :math:`d` ``==`` :math:`0`:
  | 3. :math:`\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;` **return** :math:`\text{\sc false}`
  | 4. :math:`\;\;\;\;\;` **return** :math:`\text{\sc true}`

.. only:: Internal 

  **Answer:**

  Consider the number :math:`m` containing, say, :math:`n = 100` digits. 
  In this case :math:`m \leq 10^{100}` and :math:`\sqrt{m} \leq 10^{50}`. 
  To check, if such number is a prime number (in the worst case), 
  we need to make about :math:`10^{50}` operations. 

  In general, the time complexity of this algorithm is :math:`O\left( 10^{\frac{n}{2}} \right)`.
  We see that the algorithm is extremely inefficient for (moderately) long inputs.
  On the other hand, checking primality of 100-digit numbers can be done 
  very fast using an efficient, but probabilistic algorithm by Rabin-Miller. 
  Here is Python code to find the largest 100-digit prime number: 

  .. code-block:: python

    import sympy

    for i in range(1, 1000):
        if sympy.isprime(10**100 - i):
            print('Prime number 10**100-{}'.format(i))
   

  Output looks like this: 

  .. code-block:: text

    Prime number 10**100-797
    Prime number 10**100-911
  

  :math:`\square` 


**Problem 4:** 
  Answer the following Yes/No questions: 

  **(A)**
    For any :math:`g(n)`, is the set of functions :math:`\Theta(g(n))` the intersection of :math:`O(g(n))` and :math:`\Omega(g(n))`? 
	
  **(B)**
    Does every function :math:`f(n)` defined for all natural numbers and taking positive values 
    belong to the set :math:`Omega(1)`?
	
  **(C)** 
    Let :math:`f(n), g(n)` be two functions from natural numbers to non-negative real numbers. 
    Is it true that we have either :math:`f(n)` in :math:`O(g(n))` or :math:`g(n)` in :math:`f(n)` (or both)? 

  **(D)**
    Does the definition of :math:`f(n)` in :math:`O(g(n))` make sense, if :math:`f(n)` and :math:`g(n)` 
    can take negative values? 

  **(E)**
    Are these two sets of functions :math:`O(\log_2 n)` and :math:`O(\log_{10} n)` the same? If not, find 
    which one is larger (contains more functions)?

  **(F)** 
    Let :math:`f(n)` be a function from natural numbers to non-negative real numbers. 
    Do we always have that :math:`f(n)` is in :math:`O(f(n))`, and :math:`f(n)` is in :math:`\Omega(f(n))` and :math:`f(n)` is in :math:`\Theta(f(n))`? 
    (In other words, is being in Big-O, in Big-Omega and in Big-Theta a reflexive relation?)
	
  **(G)** 
    Let :math:`f(n),g(n),h(n)` be functions from natural numbers to non-negative real numbers.
    It is known that :math:`f(n)` is in :math:`O(g(n))` and also :math:`g(n)` is in :math:`h(n)`. 
    Can we always imply that :math:`f(n)` is in :math:`O(h(n))`. 
    (In other words, is being in Big-O, in Big-Omega and in Big-Theta a transitive relation?)
	
  **(H)** 
    Let :math:`f(n),g(n)` be functions from natural numbers to non-negative real numbers. 
    It is known that :math:`f(n)` is in :math:`\Theta(g(n))`. 
    Can we always imply that :math:`g(n)` is in :math:`\Theta(f(n))`? 
    (In other words, is being in Big-Theta an equivalence relation?)
	
  **(I)**
    A function :math:`f(n)` is defined for natural arguments and takes natural values. 
    It is known that :math:`f(n)` is in :math:`O(1)`. 
    Is it true that :math:`f(n)` is a constant function: :math:`f(n) = C` for all :math:`n \in \mathbf{N}`.

 
.. only:: Internal 

  **Answer:**

  **(A)**
    True. We need to prove in two directions. 

    **(1)** 
      If :math:`f(n) \in O(g(n))` and :math:`f(n) \in \Omega(g(n))`, then also :math:`f(n) \in \Theta(g(n))`. 

      Indeed, if we have :math:`f(n)` bound from above by :math:`c_1 \cdot g(n)` for all :math:`n \geq n_1`, 
      and also :math:`f(n)` bound from below by :math:`c_2 \cdot g(n)` for all :math:`n \geq n_2`, then 
      we also have :math:`c_1 g(n) \leq f(n) \leq c_2 g(n)` as soon as :math:`n \geq \max(n_1,n_2)`.

      This means that for all sufficiently large :math:`n` all the values :math:`f(n)` will be bound from both sides
      which is same as :math:`f(n) \in \Theta(g(n))`. 

    **(2)** 
      If :math:`f(n) \in \Theta(g(n))` then both :math:`f(n) \in \O(g(n))` and  :math:`f(n) \in \Omega(g(n))`
      must hold. 

      Indeed, if there are constants :math:`c_1, c_2` such that for all :math:`n \geq n_0` we have 
      :math:`c_1 g(n) \leq f(n) \leq c_2 g(n)`, then the function :math:`f(n)` is bound from above and from below. 
      I.e. it belongs to :math:`O(g(n))` and :math:`\Omega(g(n))` where the same constants can be used.  

  **(B)**
    False. You could take any function :math:`f(n) = \frac{1}{n}`. In this case all the values are non-negative, 
    but there does not exist a positive constant :math:`c` such that all the values :math:`\frac{1}{n} \geq c \cdot 1`
    (in fact these values converge to :math:`0`). 

    Class :math:`\Omega(1)` includes only those functions that have a positive (or infinite)
    lower limit. See `Lower Limit <https://mathworld.wolfram.com/LowerLimit.html>`_. 

  **(C)**
    False. Most functions encountered in algorithm analysis are comparable, using Big-O notation: 
    namely, either :math:`g(n)` bounds :math:`f(n)` from above (for all sufficiently large :math:`n`) or 
    vice versa.  

    But it is not difficult to build functions that are not comparable. For example, 

    .. math:: 

      \left\{ \begin{array}{l}
        f(n) = n \\
        g(n) = n^(1 + \sin n) \\
        \end{array} \right\}

    Here the function :math:`g(n)` is not monotonous (it takes "random" values between :math:`n^0` and :math:`n^2`). 
    It is also possible to create two functions that are monotonous (non-decreasing) and still incomparable 
    so that :math:`f(n) \not\in O(g(n))` and also :math:`g(n) \not\in O(f(n))`. 

  **(D)**
    True. All the definitions still make sense, if functions :math:`f(n)` and :math:`g(n)` can take 
    negative values. The important requirement is that functions :math:`f(n)` and :math:`g(n)` be
    *asymptotically non-negative* -- i.e. they only take finitely many negative values. 
    In this case :math:`n_0` can be selected sufficiently large, so that :math:`0 \geq f(n)` and 
    :math:`0 < g(n)` whenever :math:`n > n_0`. (Which means that negative values :math:`f(n)<0` etc. 
    can be simply ignored as the arguments :math:`n` are not sufficiently large.)



  :math:`\square`



**Problem 5:**
  Order these functions in increasing order regarding Big-O complexity
  (:math:`f_i` is considered "not larger" than :math:`f_j` iff :math:`f_i \in O(f_j)`.

  * :math:`f_1(n) = n^{0.9999} \log_2 n`
  * :math:`f_2(n) = 10000n`
  * :math:`f_3(n) = 1.0001^n`
  * :math:`f_4(n) = n^2`


**Problem 6:**
  Order these functions in increasing order regarding Big-O complexity:

  * :math:`f_1(n) = 2^{2^{10000}}`
  * :math:`f_2(n) = 2^{10000n}`
  * :math:`f_3(n) = \binom{n}{2} = C_n^2`
  * :math:`f_4(n) = \binom{n}{\lfloor n/2 \rfloor}`
  * :math:`f_5(n) = \binom{n}{n-2}`
  * :math:`f_6(n) = n!`
  * :math:`f_7(n) = n\sqrt{n}`

**Problem 7:**
  Order these functions in increasing order regarding Big-O complexity:

  * :math:`f_1(n) = n^{\sqrt{n}}`
  * :math:`f_2(n) = 2^n`
  * :math:`f_3(n) = n^{10} \cdot 2^{n/2}`
  * :math:`{\displaystyle \sum\limits_{i = 1}^{n} (i + 1)}`.
	
	

**Problem 8:**
  A black box :math:`\mathcal{B}` receives two numbers :math:`k_1,k_2 \in \{ 1,\ldots,n \}` 
  as inputs and returns a value :math:`v = \mathcal{B}(k_1,k_2)`. 
  What is the worst-case time complexity to find the maximum possible value 
  :math:`v = \mathcal{B}(k_1,k_2)` for any two inputs.
  
  What if the black box receives permutations of :math:`n` elements as its inputs?



