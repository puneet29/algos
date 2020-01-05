// Stress test generator for Last Digit of the Partial Sum of
// Fibonacci Numbers problem.

#include <iostream>
#include <vector>
#include <numeric>
#include <random>
using namespace std;

vector<int> f = {0, 1};

int fibsum(long long n)
{
    return (
               // (n / f.size()) * accumulate(f.begin(), f.end(), 0) +
               // As sum(f) % 10 == 0, remove above line
               accumulate(f.begin(), f.begin() + (n % f.size() + 1), 0)) %
           10;
}

int checkfibsumpartial(long long m, long long n)
{
    if (m > n)
    {
        return -1;
    }
    int ans = (fibsum(n) - fibsum(m) + f[m % f.size()]) % 10;
    return ans < 0 ? 10 + ans : ans;
}

int fibsumpartial(long long m, long long n)
{
    if (m > n)
    {
        return -1;
    }
    if (f.size() > n)
    {
        return accumulate(f.begin() + m, f.begin() + n + 1, 0) % 10;
    }
    return (accumulate(f.begin() + m % f.size(), f.end(), 0) +
            // accumulate(f.begin(), f.end(), 0) * (n / f.size() - 1) +
            // As sum(f)%10==0, remove the above line.
            accumulate(f.begin(), f.begin() + (n % f.size() + 1), 0)) %
           10;
}

int main()
{
    long long m, n;
    int curr, act, out;
    random_device rd;
    default_random_engine generator(rd());
    uniform_int_distribution<long long> distribution1(0, LONG_LONG_MAX);
    for (int i = 2; i < 101; i++)
    {
        curr = (f[i - 1] + f[i - 2]) % 10;
        if (curr == 0 && f[i - 1] == 1)
        {
            break;
        }
        f.push_back(curr);
    }
    while (true)
    {
        n = distribution1(generator);
        uniform_int_distribution<long long> distribution2(0, n);
        m = distribution2(generator);
        cout << m << " " << n << endl;
        act = checkfibsumpartial(m, n);
        out = fibsumpartial(m, n);
        if (out == act)
        {
            cout << "OK" << endl;
        }
        else
        {
            cout << "Wrong Answer.\tActual Answer: " << act << "\tOutput: " << out << endl;
            break;
        }
    }
    return 0;
}
