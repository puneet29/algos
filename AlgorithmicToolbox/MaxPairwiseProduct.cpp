// Problem description: Find the maximum product of two distinct numbers in a
// sequence of non-negative integers.

#include <iostream>
using namespace std;

int MaxPairwiseProduct(int arr[], int n)
{
    int a = 0, b = 0;
    for (int i = 0; i < n; i++)
    {
        if (arr[i] > a)
        {
            b = a;
            a = arr[i];
            continue;
        }
        if (arr[i] > b)
        {
            b = arr[i];
        }
    }
    return (a * b);
}

int main()
{
    int n;
    cin >> n;
    int arr[n];
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }
    cout << MaxPairwiseProduct(arr, n);
    return 0;
}