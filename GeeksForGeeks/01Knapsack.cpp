// Problem Description: https://practice.geeksforgeeks.org/problems/0-1-knapsack-problem/0

#include <iostream>
#include <bits/stdc++.h>
using namespace std;

void getMaxValue(int val[], int wt[], int W, int n)
{
    int K[n + 1][W + 1];

    for (int i = 0; i <= n; i++)
    {
        for (int j = 0; j <= W; j++)
        {
            if (i == 0 || j == 0)
            {
                K[i][j] = 0;
            }
            else if (wt[i - 1] <= j)
            {
                K[i][j] = max(K[i - 1][j], val[i - 1] + K[i - 1][j - wt[i - 1]]);
            }
            else
            {
                K[i][j] = K[i - 1][j];
            }
        }
    }
    cout << K[n][W] << endl;
}

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n, W;
        cin >> n >> W;
        int val[n], wt[n];
        for (int i = 0; i < n; i++)
        {
            cin >> val[i];
        }
        for (int i = 0; i < n; i++)
        {
            cin >> wt[i];
        }
        getMaxValue(val, wt, W, n);
    }
    return 0;
}