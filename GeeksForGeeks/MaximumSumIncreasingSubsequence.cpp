// Problem Description: https://practice.geeksforgeeks.org/problems/maximum-sum-increasing-subsequence/0

#include <iostream>
using namespace std;

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n, ans = 0;
        cin >> n;
        int a[n], dp[n];

        for (int i = 0; i < n; i++)
        {
            cin >> a[i];
            dp[i] = a[i];
        }

        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < i; j++)
            {
                if (a[i] > a[j] && dp[i] < dp[j] + a[i])
                {
                    dp[i] = dp[j] + a[i];
                }
            }
            if (ans < dp[i])
            {
                ans = dp[i];
            }
        }
        cout << ans << endl;
    }
    return 0;
}