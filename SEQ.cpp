// Problem Description: https://www.spoj.com/problems/SEQ/

#include <iostream>
#include <vector>
#define MOD 1000000000

using namespace std;

vector<vector<unsigned long>> multiply(vector<vector<unsigned long>> a, vector<vector<unsigned long>> b)
{
    unsigned long k = a.size();
    vector<vector<unsigned long>> result(k, vector<unsigned long>(k));
    for (int i = 0; i < k; i++)
    {
        for (int j = 0; j < k; j++)
        {
            for (int l = 0; l < k; l++)
            {
                result[i][j] = (result[i][j] + (a[i][l] * b[l][j]) % MOD) % MOD;
            }
        }
    }
    return result;
}

vector<vector<unsigned long>> pow(vector<vector<unsigned long>> a, unsigned long power)
{
    if (power == 1 || power == 0)
    {
        return a;
    }
    // If power is odd
    if (power & 1)
    {
        return multiply(a, pow(a, power - 1));
    }
    else
    {
        vector<vector<unsigned long>> X = pow(a, power / 2);
        return multiply(X, X);
    }
}

int main()
{
    int t;

    cin >> t;
    while (t--)
    {
        // Variables
        int k;
        unsigned long n, temp;
        vector<unsigned long> a, b, c;
        vector<vector<unsigned long>> tf;

        // Input
        cin >> k;
        for (int i = 0; i < k; i++)
        {
            cin >> temp;
            b.push_back(temp);
        }
        for (int i = 0; i < k; i++)
        {
            cin >> temp;
            c.push_back(temp);
        }
        cin >> n;

        // F1 and tf initialization
        unsigned long f[k];
        for (int i = 0; i < k; i++)
        {
            f[i] = b[i];
            vector<unsigned long> tempVec;
            for (int j = 0; j < k; j++)
            {
                tempVec.push_back(0);
            }
            tf.push_back(tempVec);
        }

        // Transformation matrix values
        for (int r = 0; r < k - 1; r++)
        {
            for (int c = 0; c < k; c++)
            {
                if (c - r == 1)
                {
                    tf[r][c] = 1;
                }
                else
                {
                    tf[r][c] = 0;
                }
            }
        }
        for (int i = 0; i < k; i++)
        {
            tf[k - 1][i] = c[k - i - 1];
        }

        // Multiply transformation matrix with itself(n-1)
        tf = pow(tf, n - 1);

        // Print results
        unsigned long res = 0;
        for (int i = 0; i < k; i++)
        {
            res = (res + (tf[0][i] * f[i]) % MOD) % MOD;
        }

        cout << res << endl;
    }

    return 0;
}