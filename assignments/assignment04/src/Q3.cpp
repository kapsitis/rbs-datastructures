#include <iostream>
#include <list>
#include <string>

using namespace std;
bool isOdd(int arg)
{
    return (arg % 2 != 0);
}

bool isOdd(string arg)
{ 
    return (arg.length() % 2 != 0);    
}

/* Generic function to filter only odd elements of any type */
template <class E>
list<E> filterOdd(list<E> arg)
{
    list<E> result;
    for (E item : arg)
    {
        if (isOdd(item))
        {
            result.push_back(item);
        }
    }
    return result;
}

int main()
{
    list<int> listA({2, 8, 7, 5, 3, 1, 4});
    list<string> listB({"A", "AA", "AAA", "AAAA"});

    // return list { 7,5,3,1}
    list<int> filteredA = filterOdd(listA);
    for (int a: filteredA) { cout << a << " "; } cout << endl;
    // return list ("A", "AAA")
    list<string> filteredB = filterOdd(listB);
    for (string b: filteredB) { cout << b << " "; } cout << endl;
}
