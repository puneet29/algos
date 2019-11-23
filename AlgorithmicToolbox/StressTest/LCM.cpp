// Stress test generator for LCM problem. This test checks
// the time taken for calculating LCMs of two numbers.

#include <iostream>
#include <chrono>
#include <random>
using namespace std;
using namespace std::chrono;

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
    int it = 0;
    double total = 0.0;
    /* Seed */
    random_device rd;
    /* Random number generator */
    default_random_engine generator(rd());
    /* Distribution on which to apply the generator */
    uniform_int_distribution<long long> distribution(0, LONG_LONG_MAX);
    while (true)
    {
        it++;
        a = distribution(generator) % 1000000000;
        b = distribution(generator) % 1000000000;
        cout << a << " " << b << endl;
        auto start = high_resolution_clock::now();
        cout << LCM(a, b) << endl;
        auto stop = high_resolution_clock::now();
        auto duration = duration_cast<microseconds>(stop - start);
        total += duration.count();
        cout << "Iteration: " << it << "\tTime taken: " << duration.count() << " microseconds\tTotal time: " << total * 1e-6 << " seconds" << endl;
    }
    return 0;
}