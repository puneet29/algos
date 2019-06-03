#include <iostream>
#include <string>
using namespace std;

//returns minimum out of a and b
int findMin(int a, int b)
{
    if (a <= b)
    {
        return (a);
    }
    else
    {
        return (b);
    }
}

int palindrome(string A, int size)
{
    int MAT[size][size];

    // Initialize the Matrix with zeros
    for (int i = 0; i < size; i++)
    {
        for (int j = 0; j < size; j++)
        {
            MAT[i][j] = 0;
        }
    }

    // Main logic
    int i = 0, diff = 1, j = 0;
    while (diff <= size - 1)
    {
        j = i + diff;
        if (A[i] == A[j])
        {
            MAT[i][j] = MAT[i + 1][j - 1];
        }
        else
        {
            MAT[i][j] = findMin(MAT[i][j - 1], MAT[i + 1][j]) + 1;
        }

        if (j == size - 1)
        {
            i = 0;
            diff++;
        }
        else
        {
            i++;
        }
    }
    return (MAT[0][size - 1]);
}

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        string S;
        cin >> S;
        cout << palindrome(S, S.length())<<endl;
    }
    return 0;
}