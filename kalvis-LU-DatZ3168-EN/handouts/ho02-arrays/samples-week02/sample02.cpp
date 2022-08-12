#include <iostream>
using namespace std;
int countELL(char arg[]) {
    int count = 0; 
    int size = sizeof(arg)/sizeof(arg[0]);
    for (int i = 0; i < size; i++) {
        if (arg[i] == 'l' || arg[i] == 'L' ) { count++; }
    }
    return count;
}

int main() {
    char greeting[] = "HELLO";
    char* greeting2 = "HELLO";
    cout << "The count of L's in HELLO: " << countELL(greeting) << endl;
    cout << "The count of L's in HELLO: " << countELL(greeting2) << endl;
}