#include <iostream>
#include <string>

using namespace std;

int main()
{
    double age;
    string name;
    cin >> age;
    cin.ignore(256, '\n'); 
    getline (cin, name);
}


Input is: 
20
Joe

After this program we get age=20; name="Joe". 
What happens, if we remove cin.ignore? 

(A) age=2; name="0"
(B) age=20; name=""
(C) age=20; name="Joe"
(D) Runtime error





What is printed by this: 

for (i = 0; i < 3; i++)
    cout << "Hello";
	cout << "*";
	
(A) HelloHelloHello*
(B) Hello*Hello*Hello*
(C) HelloHelloHelloHello*
(D) Hello*Hello*Hello*Hello





(First)
i = 11;
while (i <= 10) { cout << "*"; i++; }
cout << endl;

(Second)
i = 11;
do { cout << "*"; i++ } while (i <= 10); 
cout << endl;

(A) Both produce output of the same length; 
(B) (First) produces longer output
(C) (Second) produces longer output
(D) Neither fragment produces output.




What happens if you need to break out from the 
outer loop?

