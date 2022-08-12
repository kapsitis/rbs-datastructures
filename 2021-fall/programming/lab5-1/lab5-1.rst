Programming Task 5, Part 1
============================

Place your files in the directory ``ds-workspace-YourName/lab5-1``, push it to your GitHub repository.
The following files should be present in your repository: 

* ``lab5-1\src\TextAnalysisMain.cpp`` (main method reading text input and producing output as described below)
* ``lab5-1\src\StringMatcher.cpp`` and ``lab5-1\src\StringMatcher.h`` implementing some variant of string matching
  algorithms. 
* Any additional C++ or header files in ``lab5-1\src``.


**Implementation Guidelines**

* You can use external libraries, if necessary. 
  String matching with hashing (such as Rabin-Karp algorithm) 
  is recommended as many other solutions may not scale well for large inputs.
* Your program should process every input data file defined below in less than 10 seconds -- 
  otherwise the grading script would assume that it loops forever.
* Your program should have no memory leaks.


Description
-------------

An absent-minded professor used to write essays on his laptop
and he did not know about GitHub.
He stored every new revision of an essay in a separate file.
The files had similar name prefixes, but suffixes were all different. 
For example, ``ThePowerOfStructuredLife_v6.txt``, 
``ThePowerOfStructuredLife_new.txt``,
``ThePowerOfStructuredLife_newest.txt``, 
``ThePowerOfStructuredLife_submitted.txt``, 
``ThePowerOfStructuredLife_most_recent_revision.txt``.
At some point his laptop died, the files were recovered from a backup, 
but the original timestamps were all gone. As a result the professor did 
not know how these revisions of the same essay relate to each other and
which document is the most complete.

To help solve versioning issues for himself and everyone else he decided to 
create a software to compare some revision of a file with some other revisions 
and measure the number of overlaps. 

Overlaps of the "testable" file (for example, ``Example01_test.txt``)
are searched in "training" files in one or more directories (for example, all ``*.txt`` files
under ``Example01``). Namely, we use the "sliding window" technique -- 
consider all the :math:`m`-character substrings in the testable file. 
If the testable file :math:`T` has size :math:`N` chars, then there
are exactly :math:`N-m+1` ways to locate the sliding window. 
We use the Python notation -- :math:`T[a:b]` denotes a substring of all chars from 
:math:`T[a]` (inclusive) to :math:`T[b]` (exclusive). In particular:

* :math:`T[0:m]` (includes all chars from :math:`T[0]` to :math:`T[m-1]`)
* :math:`T[1:m+1]` (all chars from :math:`T[1]` to :math:`T[m]`), and so on... 
* :math:`T[N-m:N]` (all chars from :math:`T[N-m]` to :math:`T[N-1]`)

Every sequence of :math:`m` consecutive characters from some file will be called 
an :math:`m`-gram. 
Some of these :math:`m`-grams can be found in "training" files. 
If there are :math:`C` consecutive matches of :math:`m`-grams
(for example, :math:`[k_1:k_1+m]`, :math:`\ldots`, :math:`k_1 + C-1:k_1 + C +m - 1]`), 
then they make one *cluster* of length :math:`m+C-1` 
and we output the interval :math:`k_1:k_1 + C + m - 1`.
It may happen that these :math:`m`-grams are, in fact, present in different "training" files, 
but they are still considered a single cluster.
Any overlaps shorter than the `m`-character window are not detected and should not be reported.




**The Desired Outcome:**

The program should output a report showing the percentage of overlaps (from the total size of the file). 
It should also show the begin (inclusive) and end (exclusive) of every overlap. 

.. note:: 
  The "testable" file may be located in the same directory as the "training" files -- it is often convenient to 
  keep all these files together.
  In such case the testable file itself should be excluded from the training set (otherwise we would 
  have :math:`100\%` overlap between the testable file and the training set). 
  
.. note:: 
  Since spacing and formatting in files can differ, string searching often happens after 
  *space normalization* (all whitespace characters -- newlines, tabs, carriage returns are converted to 
  spaces and also multiple separating spaces are converted into a single space). 
  To keep things simple you can assume that all the files to be analyzed (and also used for training) 
  are already space-normalized. 
  

**Limitations:** 

* The testable file is up to :math:`10^4 = 10000` characters.
* The total size of all training files is up to :math:`10^6 = 1000000` characters. 
* In this task you can assume that all files are space-normalized -- they contain 
  ASCII characters (upper-case and lower-case Latin letters, digits, special characters, 
  but there are no tabs or newlines; all words are separated by single spaces).
  Also, testable/training files cannot start or end with a space.



**Input representation:** 

.. code-block:: text

  Test <Path-to-Testable-File>
  Train <Directory1>
  ...
  Train <DirectoryN>
  Extensions <ext1> <ext2> ... <extK>
  Window <m>
  
Explanation of the parameters:

* ``<Path-to-Testable-File>`` -- path to the file being tested (relative to the current directory of EXE).
* ``<Directory1>``, ``<DirectoryN>`` -- all the directories to visit to train the string recognition algorithm.
* ``<ext1>``, ``<extK>`` -- file extensions that should be included in the training set.
* ``<m>`` -- the size of window to check. 



**Output representation:** 

.. code-block:: text

  Length <length-chars>
  Overlap <overlap-chars>
  Percentage <DD.D>%
  <begin1>:<end1>
  ...
  <beginZ>:<endZ>
  
Explanation of the parameters: 

* ``<length-chars>`` -- the total number of chars in the testable file. 
* ``<overlap-chars>`` -- the total number of chars in all the clusters. 
* ``<DD.D>`` -- overlap divided by total length (multiplied by :math:`100\%` and rounded to the closest tenth)
* ``<beginK>``, ``<endK>`` -- the begin (inclusive) and end (exclusive) positions for all the clusters. 



Input Data Samples
--------------------

**Sample input** ``test01.txt``

.. code-block:: 

  Test samples01/file1.txt
  Train samples01
  Extensions txt
  Window 4
  
Assume that the directory ``samples01`` contains ``3`` files: 

**File** ``samples01/file1.txt``

.. code-block:: text

  aaaa bbbb cccc dddd cccc xxxx yyyy zzzz abcd bb cc x yyy

**File** ``samples01/file2.txt``

.. code-block:: text

  aaaa bbbb cccc dddd

**File** ``samples01/file3.txt``

.. code-block:: text

  ccc xxxx yyyy zzzz

**Sample output** ``expected01.txt``

.. code-block:: text

  Length 56
  Overlap 49
  Percentage 87.5%
  0:39
  45:50
  51:56
  

To see what are the overlapping clusters, see the following diagram (all chars in the testable file 
that belong to some cluster have a "+" sign above them): 

.. code-block:: text

  +++++++++++++++++++++++++++++++++++++++      +++++ +++++
  aaaa bbbb cccc dddd cccc xxxx yyyy zzzz abcd bb cc x yyy
  

