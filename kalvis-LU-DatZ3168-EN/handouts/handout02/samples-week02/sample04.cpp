#include <iostream>
using namespace std;

bool allEqualOnRow(int* row, int nCols) {
	for (int j = 0; j < nCols; j++) {
		if (row[j] != row[0]) return false;
	}
	return true;
}

void printEqual(int** arr, int nRows, int nCols) {
	for (int i = 0; i < nRows; i++) {
		if (allEqualOnRow(arr[i], nCols)) cout << i << endl;
	}
}



int main() {
	int** m = new int*[3];
	int r1[] = {4,5,6,4}; m[0] = r1;
	int r2[] = {8,5,6,5}; m[1] = r2;
	int r3[] = {5,5,5,5}; m[2] = r3;
    printEqual(m,4,3);
}
