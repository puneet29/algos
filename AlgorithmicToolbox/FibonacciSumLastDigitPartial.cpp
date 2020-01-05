// Problem Description: Compute the last digit of
// Fm + Fm+1 + ··· + Fn.

#include <iostream>
#include <vector>
#include <numeric>
using namespace std;

vector<int> f = {0, 1};

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
    int curr;
    for (int i = 2; i < 101; i++)
    {
        curr = (f[i - 1] + f[i - 2]) % 10;
        if (curr == 0 && f[i - 1] == 1)
        {
            break;
        }
        f.push_back(curr);
    }
    cin >> m >> n;
    cout << fibsumpartial(m, n) << endl;
    return 0;
}
