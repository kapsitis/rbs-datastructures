#include <iostream>
using namespace std;
void swap(int& b, int c, int *d) {
    int temp = b;
    b = c;
    c = temp;
    temp = d[0];
    d[0] = d[1];
    d[1] = temp;
}

int main() {
    int arr[] = {7, 8};
    int b = 5;
    int c = 6;
    swap(b,c,arr);
    cout << b << " " << c << " " << arr[0] << " " << arr[1]; 
}
