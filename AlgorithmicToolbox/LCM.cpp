// Problem Description: Compute the least common multiple of two positive
// integers.

#include <iostream>
using namespace std;

long long GCD(long long a, long long b)
{
    if (b == 0)
    {
        return a;
    }
    return GCD(b, a % b);
}

long long LCM(long long a, long long b)
{
    long long h = GCD(a, b);
    if (h == 1 || a == 1 || b == 1)
    {
        return (a * b);
    }
    return (h * LCM(a / h, b / h));
}

int main()
{
    long long a, b;
    cin >> a >> b;
    cout << LCM(a, b) << endl;
    return 0;
}