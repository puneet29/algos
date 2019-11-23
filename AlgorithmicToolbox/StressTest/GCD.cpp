// Stress test generator for GCD problem.

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
    long long a, b, ans, ansfast;
    while (true)
    {
        a = rand() % 100000;
        b = rand() % 100000;
        if (rand() % 2 == 0)
        {
            a *= rand() % 1000;
        }
        if (rand() % 2 == 0)
        {
            b *= rand() % 1000;
        }
        cout << a << " " << b << endl;
        ans = GCD(a, b);
        ansfast = GCDfast(a, b);
        if (ans == ansfast)
        {
            cout << "OK" << endl;
        }
        else
        {
            cout << "Wrong Answer\nActual answer: " << ans << "\t"
                 << "Output: " << ansfast << endl;
            break;
        }
    }
    return 0;
}