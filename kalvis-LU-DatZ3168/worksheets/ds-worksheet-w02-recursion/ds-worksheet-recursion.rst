Worksheet Week 01: Asymptotic Bounds
======================================

Introduction
--------------


Running Time as a Complexity Measure
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Properties of Big-O, Big-Omega, Big-Theta
--------------------------------------------


Problems
------------


**Problem 5:** 
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
	  
