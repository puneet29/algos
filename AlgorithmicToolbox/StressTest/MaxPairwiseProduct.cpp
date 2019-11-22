// Stress test generator for MaxPairwiseProduct problem.

#include <iostream>
using namespace std;

int MaxPairwiseProductBrute(int arr[], int n)
{
    int res = 0;
    for (int i = 0; i < n; i++)
    {
        for (int j = i + 1; j < n; j++)
        {
            if (arr[i] * arr[j] > res)
            {
                res = arr[i] * arr[j];
            }
        }
    }
    return (res);
}

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
    while (true)
    {
        int n = rand() % 10000 + 2;
        cout << n << endl;
        int arr[n];
        for (int i = 0; i < n; i++)
        {
            arr[i] = rand() % 100000;
            cout << arr[i] << " ";
        }
        cout << endl;

        int actual = MaxPairwiseProductBrute(arr, n);
        int out = MaxPairwiseProduct(arr, n);
        if (out != actual)
        {
            cout << "Wrong Answer\nOutput: " << out << "\t"
                 << "Actual answer: " << actual << endl;
            break;
        }
        else
        {
            cout << "OK" << endl;
        }
    }
    return 0;
}