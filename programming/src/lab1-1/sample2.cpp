#include <iostream>

using namespace std;

int abs(int a, int b) {
    return (a - b)>0 ? (a - b) : (b - a);
}

void print_array(int* arr, int size) {
    for (int i = 0; i < size; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

int main() {
    int a[2000] = {0};
    // is this number already used
    bool taken[2000] = {false};
    int b[1000] = {0};
    int c[1000] = {0};

    int n = 0;
    for (int i=0; i < 2000; i++) {
        int var; 
        cin >> var;
        if (var == 0) { n = i/2;  break; }
        a[i] = var;
        taken[i] = false;
    }

    for (int i = 0; i < n; i++) {
        int first = 0; 
        int second = 0;
        int minabs = 1000000000;
        for (int ii = 0; ii < 2*n; ii++) {
            if (taken[ii]) { continue; }
            for (int jj = 0; jj < 2*n; jj++) {
                if (jj == ii || taken[jj]) { continue; }
                if (abs(a[ii] - a[jj]) < minabs) {
                    minabs = abs(a[ii] - a[jj]);
                    first = ii;
                    second = jj;
                }
            }
            taken[first] = true;
            taken[second] = true;
            if (a[first] <= a[second]) {
                b[i] = a[first];
                c[i] = a[second];
            } else {
                b[i] = a[second];
                c[i] = a[first];
            }
        }
    }

    print_array(b,n);
    print_array(c,n);

    return 0;
}
