#include <iostream>

int* g(int *arg, int size) {
    int a = arg[3];
    return &a;
}

using namespace std;
int main() {    
    int primes[8] = {2, 3, 5, 7, 11, 13, 17, 19};
    int* primePtr = g(primes,8);
    cout << *(primes + 3) << endl;
    cout << *primePtr << endl;
}


char* f(char* s) {    
    char* s1 = new char[strlen(s)];
    strcpy(s1,s);
    cout << "s1 = " << s1 << endl;
    return s1;
}

