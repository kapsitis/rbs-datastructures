#include <iostream>
using namespace std;

int main() {
    int pow = 1; 
    for (int i = 0; i<13; i++) {
        cout << "10**" << i << " = " << pow << endl;
        pow *= 10;
    }
}
