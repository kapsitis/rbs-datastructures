#include <iostream>
using namespace std;
int main() {
    // No intitialization; filled with garbage
    double arr[1000];
    // An array filled with 0.0
    float zeros[1000] = {0.0};
    // Specific values; implied size
    int days[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    // Array size is 6  (including terminating '\0')
    char greeting[] = "Hello";
    // Same thing
    char* greeting2 = "Hello";
    // Just first chars initialized
    char name[100] = "Hello";
}