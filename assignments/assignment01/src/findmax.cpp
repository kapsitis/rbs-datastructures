#include <iostream>

// your implementation of findMax(...)

using namespace std;
int findMax(int a[][5], int &rowNum, int &colNum)
{
    rowNum = 0;
    colNum = 0;
    int max = a[rowNum][colNum];
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 5; j++)
        {
            if (a[i][j] >= max)
            {
                max = a[i][j];
                rowNum = i;
                colNum = j;
            }
        }
    }
    return max;
}

int main()
{
    int arr[3][5];
    // input the 3x5 array

    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 5; j++)
        {
            cin >> arr[i][j];
        }
    }

    int i, j;
    int maxValue = findMax(arr, i, j);
    cout << "MaxValue = " << maxValue
         << " found at arr[" << i << "," << j << "]" << endl;
}