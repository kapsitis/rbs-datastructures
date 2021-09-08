C++ Arrays, Classes: Week02
===========================

C++ Arrays
-----------------------

Array Declaration Examples
^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. literalinclude:: samples-week02/sample01.cpp
   :language: cpp

Arrays as Function Parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. literalinclude:: samples-week02/sample02.cpp
   :language: cpp
   :emphasize-lines: 5


A more robust way to find array size (works for all sorts of pointers)
is to specify additional parameter to the function - the length of the array in question: 

.. code-block:: cpp

  int countELL(char* arg, int size) {
      int count = 0; 
      for (int i = 0; i < size; i++) {
          if (arg[i] == 'l' || arg[i] == 'L' ) { count++; }
      }
      return count;
  }


Const Declarations, References etc.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. literalinclude:: samples-week02/sample03.cpp
   :language: cpp








Multi-Dimensional Arrays
--------------------------


.. code-block:: cpp

  const int m = 3;
  const int n = 4;
  int arr[m][n]={{3, 8, 4, 6},
                 {2, 7, 1, 5},
                 {0, 9, -1, 2}};

