// Stress test generator for GCD problem.

#include <iostream>
#include <random>
#include <chrono>
using namespace std;
using namespace std::chrono;

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
    /* Seed */
    random_device rd;
    /* Random number generator */
    default_random_engine generator(rd());
    /* Distribution on which to apply the generator */
    uniform_int_distribution<long long> distribution(0, LONG_LONG_MAX);
    while (true)
    {
        a = distribution(generator) % 100000000;
        b = distribution(generator) % 100000000;
        cout << a << " " << b << endl;
        auto start = high_resolution_clock::now();
        ans = GCD(a, b);
        auto stop = high_resolution_clock::now();
        auto naiveduration = duration_cast<microseconds>(stop - start);
        start = high_resolution_clock::now();
        ansfast = GCDfast(a, b);
        stop = high_resolution_clock::now();
        auto fastduration = duration_cast<microseconds>(stop - start);
        if (ans == ansfast)
        {
            cout << "OK\tNaive: " << naiveduration.count() << " microseconds\tFast: " << fastduration.count() << " microseconds" << endl;
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