// Problem Description: Compute the n-th Fibonacci number.

#include <iostream>
using namespace std;

long long fibonacci(long long n)
{
    if (n <= 1)
    {
        return n;
    }
    long long temp, a = 0, b = 1;
    for (long long i = 2; i < n + 1; i++)
    {
        temp = a + b;
        a = b;
        b = temp;
    }
    return b;
}

int main()
{
    long long n;
    cin >> n;
    cout << fibonacci(n) << endl;
    return 0;
}
