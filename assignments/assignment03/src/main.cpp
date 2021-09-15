#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

// https://stackoverflow.com/questions/1380463/sorting-a-vector-of-custom-objects
using namespace std;
struct Pair {
    int i{};
    int j{};
};
void Pair_print(Pair const &arg) {
    cout << "(" << arg.i << "," << arg.j << ")";
}
bool Pair_cmp(Pair const &left, Pair const &right) {
    Pair_print(left); cout << " vs. "; Pair_print(right); cout << endl;
    return (left.i < right.i || (left.i == right.i && left.j < right.j));
}


struct StrInt { string s; int a; };

static int numOfCompareCalls = 0;

// This function should return 0, if both arguments are equal
// It should return negative number, if "left" is less than "right"
// It should return positive number, if "left" is more than "right"
int compare(StrInt left, StrInt right) {
    numOfCompareCalls++; // increment the counter of calls
    int strCompare = left.s.compare(right.s);
    if (strCompare != 0) {
        return strCompare;
    }
    else {
        return (left.a - right.a);
    }
}


int main() {
    vector<Pair> vv{
        {7, 2}, {7, 7}, {5, 5}, {3, 4}, {5, 1}, {7, 3}, {3, 6}};
    std::sort(vv.begin(), vv.end(), Pair_cmp);
    for (vector<Pair>::iterator it = vv.begin(); it != vv.end(); ++it) {
        Pair_print(*it);
        cout << " ";
    }
    /*
    cout << endl;

    StrInt arr[3] = {{"ZZ", 13}, {"BB", 5}, {"CC", 6}};
    cout << compare(arr[0], arr[1]) << endl;
    cout << compare(arr[0], arr[2]) << endl;
    cout << compare(arr[1], arr[2]) << endl;
    cout << "numCompares = " << numOfCompareCalls << endl;
*/
}

