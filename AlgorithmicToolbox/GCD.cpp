// Problem Description: Compute the greatest common divisor of two positive
// integers.

#include <iostream>
using namespace std;

long long GCD(long long a, long long b)
{
    for (long long i = a + b + 1; i > 1; i--)
    {
        if (b % i == 0 && a % i == 0)
        {
            return i;
        }
    }
    return 1;
}

long long GCDfast(long long a, long long b)
{
    if (b == 0)
    {
        return a;
    }
    return GCDfast(b, a % b);
}

int main()
{
    long long a, b;
    cin >> a >> b;
    cout << GCDfast(a, b);
    return 0;
}