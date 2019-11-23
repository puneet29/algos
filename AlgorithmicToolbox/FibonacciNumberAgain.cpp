// Problem Description: Compute the n-th Fibonacci number modulo m.

#include <iostream>
#include <vector>
using namespace std;

long long fibonaccimodulo(long long n, long long m)
{
    long long curr;
    long reps = n + 1;
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
    long long n, m;
    cin >> n >> m;
    cout << fibonaccimodulo(n, m) << endl;
    return 0;
}
