Programming Task 5, Part 1
============================

Place your files in the directory ``ds-workspace-YourName/lab5-1``, push it to your GitHub repository.
The following files should be present in your repository: 

* ``lab5-1\src\RabinKarpMain.cpp`` (main method reading text input and producing output as described below)
* Any additional C++ files in the same subdirectory (extension ``*.cpp``) or header files (extension ``*.h``)
  to implement Rabin-Karp algorithm for finding n-grams in the given text (compared to an n-gram corpus). 


**Implementation Guidelines**

* You should only use data structures implemented by you: 
  Your solution may use external libraries (``iostream``, ``iomanip``, ``fstream``, ``sstream`` or ``string``) 
  for basic input and output processing. It should NOT use any imports of STL or Boost data structures, 
  ``algorithm`` or similar data processing libraries.
* Your program should process every input data file defined below in less than 10 seconds -- 
  otherwise the grading script would assume that it loops forever.
* Your program should have no memory leaks.



Description
-------------

During the *training phase* your algorithm inputs a collection of texts that should 
be protected from leaking or plagiarizing. 
These texts are first converted to lower-case 
and space-normalized -- so they only contain 26 Latin letters
and single spaces. 

During the *recognition phase* your algorithm inputs one more text, 
it is also space-normalized -- and it should report all 

During the next stage the algorithm receives a text to verify. 
It applies the

used to initialize a hash table 
with Rabin-Karp rolling hash values. 


**The Desired Outcome:**   

Your task is to build an efficient program that receives the genealogy data for 
one or more family trees, and it finds the two favorite relative aliens for any given alien upon 
receiving a query. You should also be able to print the subtree under the given top living ancestor
as a parenthesized tree expression (for debugging purposes). 



**Input representation:** 

We add nodes one at a time. Commands can come at any order 
(but if we add a child, its parent must be added -- 
otherwise it should be reported as an error). 
In-between the commands (that gradually build a "forest" of one or more trees) we 
can add query commands to find the *favorite relatives* for a given node 
in the tree that has been built so far. 

The input file contains one of these five commands that build 
a collection of genealogy trees:


1. Specify a *Top living ancestor* of some alien family tree (it has no living parents). 
2. Specify the *Left-handed child* for a parent. 
3. Specify the *Right-handed child* for a parent. 
4. Erase some alien from the genealogy tree. The descendants of the erased alien stay in the alien data structure.
5. Query for the favorite relatives of a given alien. 
6. Print the subtree under some given alien as a parenthesized expression. The alien is not necessarily 
   a top living ancestor of a tree -- in this case the command prints just the subtree under him/her.
7. Finish your work. 

The syntax for all these commands looks like this:

.. code-block:: text
  
  T Ancestor
  ...
  L Parent Child
  ...
  R Parent Child
  ...
  E Alien
  ...
  ? Alien
  ...
  P Alien
  ...
  F



* ``T Ancestor`` creates a new tree, here ``Ancestor`` is an identifier for an alien that is becoming the 
  *top living ancestor* of this new genealogy tree.
* ``Ancestor`` may stay the only node in his tree; then both his favorite relatives are nonexistent.
* ``L Parent Child`` is the command to specify the left-handed ``Child`` for a ``Parent``. 
* ``R Parent Child`` is the command to specify the right-handed child for a parent.
* ``E Alien`` is the command to erase some ``Alien`` with the specified number. Erasing does not "cascade"; 
  the children of an erased alien become top living ancestors of their respective subtrees.
* ``? Alien`` is the command to query the favorite relatives of a given ``Alien``. 
* ``P Alien`` is the command to print the subtree with ``Alien`` as its root. Tree is printed
  as a parenthesized expression of node identifiers (non-existent children of internal nodes are denoted
  by ``0``). 
* Any identificator for a an alien (``Ancestor``, ``Parent``, ``Child``, ``Alien``) 
  is an integer number from the interval :math:`[1;\,10\,000])`.

The input data is valid - regarding the format and the limitations defined above. 
Some tree editing commands may refer to nodes that cannot be inserted (such commands should be ignored and 
an error message printed). If a tree editing command succeeds, then a new node is added (or erased or 
queried or a subtree is printed).




**Output representation:** 

Depending on the input file the output file contains output for every query command 
and also every command that ends in failure. 
(Successful tree editing commands are silently executed, they do not produce any output.) 

.. code-block::

  LineNum: PrevFav NextFav
  ...
  LineNum: (I1 (I2 0 L3) (I4 (I5 L6 L7) 0))
  ...
  LineNum: error0
  ...
  LineNum: error1
  ...
  LineNum: error2
  ...
  LineNum: error3
  ...
  LineNum: error4
  ...
  LineNum: error5


Explanations for this syntax:

* ``LineNum`` is the line number in the input file that caused this output -- it can be a query command, 
  a print command or any other command that caused an error. (Successful commands 
  of tree editing do not produce any output.)
* ``PrevFav`` is the immediately preceding alien (in *inorder* DFS traversal order) 
  for the given ``Alien``, when we run the query command ``? Alien``. 
  Therefore, it is one of the two favorite relatives of the ``Alien``.
  If there is no previous node, output ``0``.
* ``NextFav`` is the immediately following alien (in *inorder* DFS traversal order) 
  for the given ``Alien``, when we run the query command ``? Alien``. If there is no next alien, output ``0``.
* ``I1``, ``I2``, ``L3`` -- identifiers for internal nodes and leaves in a tree printed out by ``P I1`` command. 
  Leaves are printed just as their identifiers. Internal nodes are printed as a parenthesized expressions: ``(I1 leftSubtree rightSubtree)``.
  If some internal node does not have its left or its right subtree, print ``0`` in that slot.
* ``error0`` -- alien with identifier ``Alien`` does not exist, when we run the query or print commands ``? Alien`` or ``P Alien``.
* ``error1`` -- ``Parent`` and ``Child`` are the same.
* ``error2`` -- ``Parent`` does not exist in any family tree.
* ``error3`` -- ``Child`` is already used in some family tree.
* ``error4`` -- ``Parent`` already has a left-handed child in the family tree.
* ``error5`` -- ``Parent`` already has a right-handed child in the family tree.
* ``error6`` -- ``Ancestor`` cannot start a new tree, since is already used in some family tree.


If a command causes multiple errors at once, print the one with the smallest number. 






Input Data Samples
--------------------


**Sample input** ``test01.txt``:
  
.. literalinclude:: figs/test01in.txt
   :linenos:


**Expected output** ``expected01.txt``:

.. literalinclude:: figs/expected01.txt


.. figure:: figs/aliens01.png
   :width: 3in 
   :alt: Alien Genealogy 1
   
   Alien genealogy forest: **test01** after Line 4 and Line 8


**Sample input** ``test02.txt``:
  
.. literalinclude:: figs/test02in.txt
   :linenos:


**Expected output** ``expected02.txt``:

.. literalinclude:: figs/expected02.txt


.. figure:: figs/aliens02.png
   :width: 4in 
   :alt: Alien Genealogy 2
   
   Alien genealogy forest: **test02** after Line 15 and Line 20

