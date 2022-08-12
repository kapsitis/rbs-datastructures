Written Assignment02
=======================

Questions 1,2 are done in class (or submitted remotely). Question 3 is submitted by Friday, 
Septeber 10, 2021 by checking it into GitHub repository, directory ``assignment-week02``.


**Question1:**
  
  .. code-block:: cpp
    
    int a[] = {1, 2, 3}, 
    int* p = a;
    *p++; 
    (*p++)++;
    (*p)++;
    cout << a[0] << " " << a[1] << " " << a[2] << endl;
	

  What is printed out by this code snippet?
  

**Question2:**

  Nodes of a singly linked list are implemented using the following ``struct`` type: 
  
  .. code-block:: cpp
  
    struct Node { int info; Node* next; }; 
  
  A linked list contains at least :math:`4` nodes. 
  Implement a function ``void checkAndDeleteThirdNode(Node*& arg) { ... }`` to satisfy these requirements:
  
    * The parameter ``arg`` of the function initially points to the very first node in the list.
    * Set the parameter ``arg`` of this function to point to the third node. 
    * Check, if ``info`` field of the 4th node equals :math:`17`. 
      If it does, remove the 4th node from the list.

  What is a possible body of this function?  (Select one correct answer and briefly explain your choice.)
  
  .. code-block:: text
	 
    // Answer (A) 
    arg = arg -> next -> next -> next -> next; 
    if (arg -> info == 17) { arg -> next = arg -> next -> next; }
	 
  .. code-block:: text

    // Answer (B) 
    arg = arg -> next -> next -> next; 
    if (arg -> info == 17) { arg -> next = arg; }

  .. code-block:: text

    // Answer (C) 
    arg = arg -> next -> next -> next -> next; 
    if (arg -> info == 17){ arg -> next = arg -> next -> next; }

  .. code-block:: text

    // Answer (D) 
    arg = arg -> next -> next;
    if (arg -> next -> info == 17) { arg -> next = arg -> next -> next; }

  


**Question3 (submit by Friday):**

  Below is a code of a parent class ``Human`` and a child class ``Manager``. 
  The main difference in their behavior is the method ``adjustEnergy()``
  (for humans who are not managers it adds ``10`` and for managers it multiplies 
  the existing energy by ``2``). 
  
  .. code-block:: text
  
    class Human { 
      protected: 
        string name;
        int energyPoints; 
      public:    
        Human(string name, int energyPoints) {
          this->name = name;
          this->energyPoints = energyPoints;
          cout << "Creating H(" << name << ")" << endl;
        }
        ~Human() { cout << "Freeing H(" << name << ")" << endl; }
        string toString() {
          return "H " + name +  " " +  to_string(energyPoints);
        }
        void adjustEnergy() { energyPoints += 10; }
    };

    class Manager: public Human {
      public:
        Manager(string name, int energyPoints) : Human(name, energyPoints) {
          cout << "Creating M(" << name << ")" << endl;
        }
        ~Manager() { cout << "Freeing M(" << name << ")" << endl; }
        void adjustEnergy() { energyPoints *= 2; }
    }; 
	
  Write a ``main()`` method (and, if necessary, modify the above code) 
  that reads standard input of ``N`` humans or managers with their names
  and energy levels. 
  
    * Create an array of ``Human*`` pointers pointing to
      ``Human`` or ``Manager`` objects. 
    * Call ``adjustEnergy()`` on every pointer in this array. 
    * After that output the (updated) energy levels for each pointer
      (and free the ``Human`` object by calling ``delete`` on its pointer). 
  
  The number of humans ``N`` is provided on the first line of input:
  
  **Sample Input:** 
  
  .. code-block:: text
  
    2
    H Andrejs 100
    M Cintija 101


  **Sample Output:**  

  .. code-block:: text
  
    Creating H(Andrejs)
    Creating H(Cintija)
    Creating M(Cintija)
    H Andrejs 110
    Freeing H(Andrejs)
    M Cintija 202
    Freeing M(Cintija)
    Freeing H(Cintija)