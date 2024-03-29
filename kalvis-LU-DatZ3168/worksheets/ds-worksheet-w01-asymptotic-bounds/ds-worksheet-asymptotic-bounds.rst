Worksheet 01: Asymptotic Bounds
==================================

Why study the asymptotic bounds or the "Big-O notation"?
Efficiency of algorithms is largely determined by their behavior 
for large inputs. It is not easy to describe the speed of an algorithm 
for every single input, so it is described by some "smooth" function :math:`f(n)` -- 
an estimate from above of how fast the algorithm is for inputs of length :math:`n`.


Concepts and Facts
---------------------

Informally, *asymptotic* means the behavior as some parameter goes to infinity; 
upper and lower *bounds* are inequalities satisfied by something.

**Definition:** 
  The *runtime upper bound* (also called the *worst-case running time*)
  for the given algorithm is a function
  :math:`T\,:\,\mathbf{N} \mapsto \mathbf{N}` that equals to the maximum possible 
  number of elementary steps needed to complete the 
  algorithm for any input of length :math:`n`.  
  
  (Here :math:`\mathbf{N}` is the set of all nonnegative integers.)
  

Introductory Questions:

  * What is the worst running time to multiply two square matrices of size :math:`n \times n`?  What is the size of input in this case?
  * Let :math:`T(n)` be a numeric algorithm receiving single natural numbers as input. 
    Does the runtime upper bound function change, if the input numbers are provided in binary (instead of decimal) notation? 
  * Is :math:`T(n)` a non-decreasing function (i.e. do longer inputs always imply a longer running time)?
  * What counts as an elementary step in the runtime upper bound definition? 
    (Any CPU instruction? One line in a pseudocode? One comparison in a sorting algorithm?)


**Definition (Big-O):** 
  Let :math:`g \colon \mathbb{N} \rightarrow \mathbb{R}_{0+}` be a function from natural numbers (non-negative integers)
  to non-negative real numbers.
  Then :math:`O(g)` is the set of all functions :math:`f \colon \mathbb{N} \rightarrow \mathbb{R}^{0+}`
  such that there exist real constants :math:`c>0` and :math:`n_0 \in \mathbb{N}` satisfying
  
  .. math:: 
  
    0 \leq f(n) \leq c \cdot g(n)\;\; \mbox{for all}\;\; n \geq n_0.


**Definition (Big-Omega):**
  Let :math:`g \colon \mathbb{N} \rightarrow \mathbb{R}_{0+}` be a function from natural numbers to non-negative real numbers. 
  Then :math:`\Omega(g(n))` is the set of all functions :math:`f \colon \mathbb{N} \rightarrow \mathbb{R}`
  such that there exist real constants :math:`c>0` and :math:`n_0 \in \mathbb{N}` satisfying
  :math:`{\displaystyle  \forall n \in \mathbb{N}\ \big( n \geq n_0 \rightarrow f(n) \geq c \cdot g(n) \big).}`

**Definition (Big-Theta):**
  Let :math:`g \colon \mathbb{N} \rightarrow \mathbb{R}_{0+}` be a function from natural numbers to non-negative real numbers. 
  Then :math:`\Theta(g)` is the set of all functions :math:`f: \mathbb{N} \to \mathbb{R}`
  such that there exist positive constants :math:`c_1, c_2 > 0` and :math:`n_0 \in \mathbb{N}` satisfying

  .. math::

    \forall n \in \mathbb{N}\ \big( n \geq n_0 \rightarrow  0 \leq   c_1 \cdot g(n) \leq  f(n) \leq c_2 \cdot g(n) \big).

**Definition (Asymptotic bounds):** 
  * If :math:`f(n) \in O(g(n))`, :math:`g(n)` is also called 
    *asymptotic upper bound* of :math:`f(n)`.
  * If :math:`f(n) \in \Omega(g(n))`, then :math:`g(n)` is called 
    *asymptotic lower bound* of :math:`f(n)`.
  * If :math:`f(n) \in \Theta(g(n))`, then :math:`g(n)` is called 
    *asymptotic growth order* of :math:`f(n)`.

Some bounds can be established without using the 
definitions of the Big-O, Big-Omega, and Big-Theta concepts directly. 

**Properties of the asymptotic bounds:** 

  **Dominant term:** 
    If :math:`f(n) = f_1(n) + f_2(n)`, 
    where :math:`f_2(n) < f_1(n)` for all sufficiently large :math:`n`, then :math:`O(f(n))` and :math:`O(f_1(n))` are the same.

    Consequently, if :math:`f(n) = f_1(n) + f_2(n) + \ldots + f_k(n)` can be written as a finite sum of other functions, 
    then the fastest growing one determines 
    the asymptotic growth order of the entire sum :math:`f(n)`
  
  **Additivity:** 
    If :math:`f_1(n)` is in :math:`O(g_1(n))` and :math:`f_2(n)` is in :math:`g_2(n)`, then :math:`f_1(n) + f_2(n)` is in 
    :math:`O(\max(g_1(n), g_2(n)))`. 
    Typically, one of the :math:`g_1(n)` or :math:`g_2(n)` is asymptotically larger than the other (say, :math:`g_1(n)>g_2(n)` for 
    all sufficiently large :math:`n`),  and instead of :math:`O(\max(g_1(n), g_2(n)))` we can simply take :math:`O(g_1(n))`. 

  **Multiplicativity:** 
    If :math:`f(n)` is in :math:`O(g(n))` and :math:`c>0` is a positive constant, then :math:`c\cdot f(n)` is also in :math:`O(g(n))`.

  **Transitivity:** 
    If :math:`f(n)` is in :math:`O(g(n))` and :math:`g(n)` is in :math:`O(h(n))`, then :math:`f(n)` is also in :math:`O(h(n))`.

  **Polynomial Dominance:** 
    For any positive integer :math:`k`, :math:`n^k`` is dominated by :math:`cn^k` for all :math:`n \geq n0` and some constant :math:`c`.

  **Big-O and the Limit of the Ratio:**
    If the following limit exists and is finite:

    .. math::
 
      \lim\limits_{n \rightarrow \infty} \frac{f(n)}{g(n)} = C < + \infty,

   then :math:`f(n)` is in :math:`O(g(n))`.


**Theorem (Changing the Base of Logarithm):**
  If :math:`a,b > 1` are real numbers, then :math:`\log_a n` is in :math:`\Theta(log_b n)`. 

  **Proof:**
    The last result directly follows from the formula to change the base of a logarithm: 
    
    .. math:: 
      
      \forall a,b,m > 1 \left( \log_a b = \frac{ \log_m b }{ \log_m a } \right).


.. note:: 
  It is common to just one base (usually, it is base :math:`2` or
  base :math:`e` of the natural logarithm), and write just :math:`O(\log n)` 
  without specifying base at all. Formally, :math:`\log n` in our 
  course denotes :math:`\log_2 n`. 
    
  In other contexts (where constant factors matter)
  the base of logarithm cannot be omitted. 






Problems
------------

.. _asymptotic-bounds-P1:

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



.. _asymptotic-bounds-P2:

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


.. _asymptotic-bounds-P3:

**Problem 3:**
  What is the worst running time to find, if the given input :math:`m` is a prime number. 
  Assume that the input :math:`m` is written in decimal notation using :math:`n` digits. 

  Primality testing is done by the following algorithm testing divisibility by  
  all numbers :math:`d \in \{ 2,3,\ldots,\lfloor \sqrt{m} \rfloor \}`: 

  | :math:`\text{\sc isPrime}(m)`
  | 1. :math:`\;\;\;\;\;` **for** :math:`d` **in** :math:`\text{\sc range}(2, \sqrt{m} + 1)`:
  | 2. :math:`\;\;\;\;\;\;\;\;\;\;` **if** :math:`m` ``%`` :math:`d` ``==`` :math:`0`:
  | 3. :math:`\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;` **return** :math:`\text{\sc False}`
  | 4. :math:`\;\;\;\;\;` **return** :math:`\text{\sc True}`

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


.. _asymptotic-bounds-P4:

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


.. _asymptotic-bounds-P5:

**Problem 5:**
  Order these functions in increasing order regarding Big-O complexity
  (:math:`f_i` is considered "not larger" than :math:`f_j` iff :math:`f_i \in O(f_j)`.

  * :math:`f_1(n) = n^{0.9999} \log_2 n`
  * :math:`f_2(n) = 10000n`
  * :math:`f_3(n) = 1.0001^n`
  * :math:`f_4(n) = n^2`


.. _asymptotic-bounds-P6:

**Problem 6:**
  Order these functions in increasing order regarding Big-O complexity:

  * :math:`f_1(n) = 2^{2^{10000}}`
  * :math:`f_2(n) = 2^{10000n}`
  * :math:`f_3(n) = \binom{n}{2} = C_n^2`
  * :math:`f_4(n) = \binom{n}{\lfloor n/2 \rfloor}`
  * :math:`f_5(n) = \binom{n}{n-2}`
  * :math:`f_6(n) = n!`
  * :math:`f_7(n) = n\sqrt{n}`


.. _asymptotic-bounds-P7:

**Problem 7:**
  Order these functions in increasing order regarding Big-O complexity:

  * :math:`f_1(n) = n^{\sqrt{n}}`
  * :math:`f_2(n) = 2^n`
  * :math:`f_3(n) = n^{10} \cdot 2^{n/2}`
  * :math:`{\displaystyle \sum\limits_{i = 1}^{n} (i + 1)}`.
	

.. _asymptotic-bounds-P8:

**Problem 8:**
  A black box :math:`\mathcal{B}` receives two numbers :math:`k_1,k_2 \in \{ 1,\ldots,n \}` 
  as inputs and returns a value :math:`v = \mathcal{B}(k_1,k_2)` after :math:`O(1)` time. 
  What is the worst-case time complexity to find the maximum possible value 
  :math:`v = \mathcal{B}(k_1,k_2)` for any two inputs.
  
  What if the black box receives permutations of :math:`n` elements as its inputs?



