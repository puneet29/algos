// Problem description: Find the maximum product of two distinct numbers in a
// sequence of non-negative integers.

#include <iostream>
#include <vector>
using namespace std;

int MaxPairwiseProduct(vector<int> arr, long long n)
{
    int a = 0, b = 0;
    for (long long i = 0; i < n; i++)
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
    long long n;
    cin >> n;
    vector<int> arr;
    for (long long i = 0; i < n; i++)
    {
        int temp;
        cin >> temp;
        arr.push_back(temp);
    }
    cout << MaxPairwiseProduct(arr, n);
    return 0;
}