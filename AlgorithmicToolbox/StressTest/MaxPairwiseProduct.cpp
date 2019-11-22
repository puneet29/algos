// Stress test generator for MaxPairwiseProduct problem.

#include <iostream>
#include <vector>
using namespace std;

int MaxPairwiseProductBrute(vector<int> arr, long long n)
{
    int res = 0;
    for (long long i = 0; i < n; i++)
    {
        for (long long j = i + 1; j < n; j++)
        {
            if (arr[i] * arr[j] > res)
            {
                res = arr[i] * arr[j];
            }
        }
    }
    return (res);
}

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
    while (true)
    {
        long long n = rand() % 100000 + 2;
        // n *= rand() % 10 + 1;
        cout << n << endl;
        vector<int> arr;
        for (long long i = 0; i < n; i++)
        {
            arr.push_back(rand() % 100000);
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