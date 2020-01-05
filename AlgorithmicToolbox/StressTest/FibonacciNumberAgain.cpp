// Stress test generator for Fibonacci Number Again problem.

#include <iostream>
#include <vector>
#include <chrono>
#include <random>
using namespace std;
using namespace std::chrono;

long long naivefibonaccimodulo(long long n, long long m)
{
    if (n <= 1)
    {
        return n;
    }
    long long temp, a = 0, b = 1;
    for (long long i = 2; i < n + 1; i++)
    {
        temp = (a + b) % m;
        a = b;
        b = temp;
    }
    return b;
}

long long fibonaccimodulo(long long n, long long m)
{
    long long curr;
    long reps;
    vector<long long> f = {0, 1};
    for (int i = 2; i < m * m && i <= n; i++)
    {
        curr = (f[i - 1] + f[i - 2]) % m;
        if (i == n)
        {
            return curr;
        }
        if (curr == 0 && f[i - 1] == 1)
        {
            reps = f.size();
            break;
        }
        f.push_back(curr);
    }
    return (f[n % reps]);
}

int main()
{
    long long n, m, act, out;
    /* Seed */
    random_device rd;
    /* Random number generator */
    default_random_engine generator(rd());
    /* Distribution on which to apply the generator */
    uniform_int_distribution<long long> distribution(0, LONG_LONG_MAX);
    while (true)
    {
        n = distribution(generator) % 10000000;
        m = distribution(generator) % 100000 + 2;
        cout << n << " " << m << endl;
        auto start = high_resolution_clock::now();
        out = fibonaccimodulo(n, m);
        auto stop = high_resolution_clock::now();
        auto fastduration = duration_cast<microseconds>(stop - start);
        start = high_resolution_clock::now();
        act = naivefibonaccimodulo(n, m);
        stop = high_resolution_clock::now();
        auto naiveduration = duration_cast<microseconds>(stop - start);
        if (act == out)
        {
            cout << "OK\tNaive: " << naiveduration.count() << " microseconds\tFast: " << fastduration.count() << " microseconds" << endl;
        }
        else
        {
            cout << "Wrong Answer\tActual answer: " << act << "\tOutput: " << out << endl;
            break;
        }
    }
    return 0;
}
