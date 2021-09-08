#include <iostream>

using namespace std;
int main() {
    int intArray[] = {1, 2, 3};
	int* p = intArray;
	*p++; 
	(*p++)++;
	(*p)++;
    cout << intArray[0] << " " << intArray[1] << " " << intArray[2] << endl;

	const int c = 117;
	const int d = 118;
	int e = 119;

	int* const a = intArray; 	
	cout << "a[0] = " << (*a) << endl;

	const int* b; 
	b = &c;
	cout << "b as c = " << (*b) << endl;
	b = &d;
	cout << "b as d = " << (*b) << endl;
    b = &e;	
	b++;
	cout << "b as e = " << (*b) << endl;
}
