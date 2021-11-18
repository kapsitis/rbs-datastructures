#include <iostream>

using namespace std;
long long string_hash(char *a)
{
    int len;
    unsigned char *p;
    long long x;
    len = strlen(a);
    // p = (unsigned char *) a->ob_sval;
    p = new unsigned char[len + 1];
    for (int i = 0; i <= len; i++)
    {
        p[i] = a[i];
    }
    x = *p << 7;
    while (--len >= 0)
        x = (1000003 * x) ^ *p++;
    x ^= strlen(a);
    if (x == -1)
        x = -2;
    return x;
}

int main()
{
    char *a1 = "Latvia";
    char *a2 = "Luxembourg";
    char *a3 = "Malta";

    cout << "hash(" << a1 << ") = " << (string_hash(a1) % 11) << endl;
    cout << "hash(" << a2 << ") = " << (string_hash(a2) % 11) << endl;
    cout << "hash(" << a3 << ") = " << (string_hash(a3) % 11) << endl;
}