#include <iostream>
#include <list>
using namespace std;
bool R(int a, int b) { return (a <= b); }
int main()
{
    list<int> listA({2, 8, 7, 5, 3, 1, 4});
    list<int> listB({11, 7, 6, 3, 2, 10, 14});
    list<int> listC;
    for (int a : listA)
    {
        bool valid = true;
        for (int b : listB)
        {
            valid = valid && R(a, b);
        }
        if (valid)
        {
            listC.push_back(a);
        }
    }
    for (int c : listC)
    {
        cout << c << " ";
    }
    cout << endl;
}