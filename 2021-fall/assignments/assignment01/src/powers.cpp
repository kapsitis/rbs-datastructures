#include <iostream>

using namespace std;
int main() {
int pow = 1;
        for (int i = 0; i < 25; i++) { pow *= 3; }
        int val = 0x46562aa3;  // Write a 4-byte hex value to get "Success"
        if (pow == val) { cout << "Success\n"; }
				
        if (pow < 0) { cout << "3^25 is negative" << endl; }
        if (pow > 0) { cout << "3^25 is positive" << endl; }
        if (pow == 0) { cout << "3^25 is zero" << endl; }

		// Optionally, you can also print "pow"  
		// as hexadecimal and as decimal to inspect.
		cout << "pow(as hex) = " << std::hex << pow << endl;
		cout << "pow(as dec) = " << std::dec << pow << endl;


	pow = 1;
	for (int i = 0; i < 30; i++) { 
		cout << std::dec << "3^" << i << "=" << pow << "    " << std::hex << pow << endl;
		pow *= 3; 		
	}


}
