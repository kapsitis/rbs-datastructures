#include <iostream>
using namespace std;

int main ()
{
    int a = -3;
int x = 0x00005430;
int b = a^x;
cout << hex << b;
// This prints the "hex" representation of "b"
// It outputs "0xffffabcd"    
//             0xfffffffd
}
