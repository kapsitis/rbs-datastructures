Written Assignment 11
======================

**Introduction:**
  In this task you will build a small hashtable to 
  store trade volume between some countries. 
  (All data is taken from a trade visualizaton 
  app OEC made by MIT -- 
  `<https://oec.world/en/profile/country/ltu>`_.)
  

  .. image:: figs-hashtables/graph-to-hash.png
     :width: 2.5in  

  Each edge of the above graph is hashed as a map entry that
  maps a pair of country names to a real number (export volume
  in billions USD in year 2019). 
    
  We will use Python's prehashing for pairs of strings, but 
  will build our own hash table with :math:`7` slots. 
  Run Python 3.8 or newer and check that you can 
  compute hash values for pairs of strings as shown 
  in the screenshot below. If you use older Python or do not 
  set ``PYTHONHASHSEED`` to ``0``, the function ``hash()`` 
  produces wrong values.
  
  .. image:: figs-hashtables/screenshot.png
     :width: 5in  



**(A)**
  Draw a hashtable with exactly 7 slots (enumerated as T[0], T[1], and so on, up to T[6]). 
  Insert the following 6 items into this hashtable (keys are pairs of country names): 

  .. code-block:: text

    { ('Lithuania', 'Poland'): 2.49, 
      ('Lithuania', 'Ukraine'): 1.2, 
      ('Poland', 'Lithuania'): 3.93, 
      ('Poland', 'Ukraine'): 1.2, 
      ('Ukraine', 'Lithuania'): 0.34, 
      ('Ukraine', 'Poland'): 2.75 }

  If there are any collisions between the hash values, add the additional hash values to a linked list using *chaining*.
  Each item in the linked list contains a key-value pair and also a link to the next item.

**(B)** 
  What is the expected lookup time, if we randomly search any of the 6 country pairs. Finding
  an item in a hash table takes 1 time unit; following a link in a linked list also takes 1 time unit.
  
  
**(C)**
  What is the expected lookup time, if a 7-slot hashtable is randomly filled with 6 keys (each key has equal
  probability to be in any of the slots). Find this lookup time rounded up to one tenth (one decimal digit
  precision).
