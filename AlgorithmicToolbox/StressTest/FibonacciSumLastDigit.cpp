// Problem Description: Compute the last digit of F0 +F1 +···+Fn.

#include <iostream>
#include <vector>
#include <numeric>
#include <chrono>
#include <random>
using namespace std;
using namespace std::chrono;

vector<int> f = {0, 1};

int naivefibsum(long long n)
{
    if (n <= 1)
    {
        return n;
    }
    int temp, a = 0, b = 1, sumTotal = 1;
    for (int i = 2; i < n + 1; i++)
    {
        temp = (a + b) % 10;
        a = b;
        b = temp;
        sumTotal = (sumTotal + b) % 10;
    }
    return sumTotal;
}

int fibsum(long long n)
{
    return (
               // (n / f.size()) * accumulate(f.begin(), f.end(), 0) +
               // As sum(f) % 10 == 0, remove above line
               accumulate(f.begin(), f.begin() + (n % f.size() + 1), 0)) %
           10;
}

int main()
{
    int curr, act, out;
    long long n;
    for (int i = 2; i <= 100; i++)
    {
        curr = (f[i - 1] + f[i - 2]) % 10;
        if (curr == 0 && f[i - 1] == 1)
        {
            break;
        }
        f.push_back(curr);
    }
    random_device rd;
    default_random_engine generator(rd());
    uniform_int_distribution<long long> distribution(0, LONG_LONG_MAX);
    while (true)
    {
        n = distribution(generator) % 100000000;
        cout << n << endl;
        auto start = high_resolution_clock::now();
        act = naivefibsum(n);
        auto stop = high_resolution_clock::now();
        auto naiveduration = duration_cast<microseconds>(stop - start);
        start = high_resolution_clock::now();
        out = fibsum(n);
        stop = high_resolution_clock::now();
        auto fastduration = duration_cast<microseconds>(stop - start);
        if (act == out)
        {
            cout << out << endl
                 << "OK\tNaive: " << naiveduration.count() << " microseconds\tFast: " << fastduration.count() << " microseconds" << endl
                 << endl;
        }
        else
        {
            cout << "Wrong answer\t Actual answer: " << act << "\tOutput: " << out << endl;
            break;
        }
    }
    return 0;
}