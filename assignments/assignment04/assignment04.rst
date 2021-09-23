Written Assignment04
=======================

Questions 1,2 are done in class (or submitted remotely). Question 3 is submitted by Friday, 
Septeber 24, 2021 by checking it into GitHub repository, directory ``assignment-week04``.


**Question1:**
  Lists ``listA`` and ``listB`` contain integers ``a[i]`` and ``b[i]`` respectively for 
  :math:`i \in \mathbb{N}_{<7}`, where :math:`\mathbb{N}_{<7} = \{ 0,1,2,3,4,5,6 \}`. We run this code
  to filter out elements from ``listA`` satisfying some property:

  .. code-block:: cpp

    #include <iostream>
    #include <list>
    using namespace std;	
    bool R(int a, int b) { /* Compute some binary relation R(a,b) */ }
 
    int main() {
        list<int> listA({ 2, 8, 7, 5, 3, 1, 4 });
        list<int> listB({ 11, 7, 6, 3, 2, 10, 14 });
        list<int> listC; 
        for (int a: listA) {
            bool valid = true;
            for (int b: listB) {
                valid = valid && R(a,b);
            }
            if (valid) { 
                listC.push_back(a); 
            }
        }
        for (int c: listC) { cout << c << " "; }
        cout << endl;
    }
         
  What elements from ``listA`` are added to the container ``listC``? Select one answer and explain your choice.
  
  **(A)** 
    :math:`\mathtt{listC} = \left\{ a[i] \;\mid\; i \in \mathbb{N}_{<7} \wedge \exists j \in \mathbb{N}_{<7}\ (R(a[i], b[j])) \right\}`.
  
  **(B)** 
    :math:`\mathtt{listC} = \left\{ a[i] \;\mid\; i \in \mathbb{N}_{<7} \wedge \forall j \in \mathbb{N}_{<7}\ (R(a[i], b[j])) \right\}`.
  
  **(C)** 
    :math:`\mathtt{listC} = \left\{ a[i] \;\mid\; i \in \mathbb{N}_{<7} \wedge R(a[i], b[i]) \right\}`.
	
  **(D)**
    :math:`\mathtt{listC} = \left\{ a[i] \;\mid\; i \in \mathbb{N}_{<7} \wedge \neg R(a[i], b[i]) \right\}`.



**Question 2:**
  Stack is physically stored in an array of length ``6`` (see Figure).
  It's initial size is ``2``. It has two elements pushed in: 
  ``A`` (the first one) and ``B`` (the current "top" of the stack). 
  Every ``push(x)`` command writes the new element ``x`` to the right of the 
  current "top", then increments ``size`` by 1. 
  Command ``pop()`` decrements ``size`` by 1, but does not erase anything from
  the array (inactive/ignorable elements in the array are shaded). 
  
  Show the final state of the stack's array (as well as its ``size`` and the
  value of ``ch``) after the code snippet in the Figure is executed.
  To visualize the actual size of the stack, please shade the elements in 
  ``array[]`` that do not belong to the stack (or were popped already). 
  
  .. image:: figs/stack-structure.png
     :width: 3in
  



**Question 3:**
  (Programming task to be submitted by Friday.)
  Write a generic ``filterOdd()`` function that receives a list of ``string`` or ``int``, 
  and returns a filtered list containing just the values that are either odd integers or odd-length strings.

  .. code-block:: cpp
  
    #include <iostream>
    #include <list>
    #include <string>

    using namespace std;

    bool isOdd(int arg) { /*  your code here   */ } 
    bool isOddLength(string arg) { /* your code here */ } 

    list<E> filterOdd(list<E> arg) {
        /* your code here */
    }

    int main() {
        list<int> listA({2, 8, 7, 5, 3, 1, 4});
        list<string> listB({"A", "AA", "AAA", "AAAA"});

        // should return list [7,5,3,1]
        list<int> filteredA = filterOdd(listA);
        for (int a: filteredA) { 
            cout << a << " "; 
        } 
        cout << endl;
		
        // should return list ["A", "AAA"]
        list<string> filteredB = filterOdd(listB);
        for (string b: filteredB) { 
            cout << b << " ";
        } 
        cout << endl;
    }
	

