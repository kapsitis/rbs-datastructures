#include <iostream>

using namespace std;
int main() {
    int intArray[] = {1, 2, 3};
	int* p = intArray;
	*p++; 
	(*p++)++;
	(*p)++;
    cout << intArray[0] << " " << intArray[1] << " " << intArray[2] << endl;
}
