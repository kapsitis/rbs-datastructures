Written Assignment 13
======================

**Introduction:**	
  This task is about Knuth-Morris-Pratt algorithm -- creating 
  the data structure (a *prefix table*) for the given pattern and showing how it is 
  used to search that pattern in a text. 

..  You will also run a Finite State Acceptor to show how the 
..  state transitions are being done while searching for the pattern.
  
  Please refer to the KMP sample (see *Handout 13: KMP String Search* in ORTUS)
  for an example how to process a pattern into a prefix function
  and how to run a KMP algorithm.

.. https://youtu.be/GTJr8OvyEVQ ; 8:00

**(A)**
  Build the prefix function for the following pattern: 
  :math:`\mathtt{KLMNKLMK}`. 
  Write the values of prefix function in a table 
  and show, how this table was constructed.


**(B)** 
  Show how this works on the following text: 
  :math:`T = \mathtt{KLMOKLMNKLOKLMNKLMNKLMK}`. 
  Draw a table showing every shift of the pattern that 
  was tested and circle those letters that were actually compared. 
                   
  



