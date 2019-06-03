#include <iostream>
using namespace std;

int findMax(int *memo, int i, int j, int w)
{
    int maxValue = 0;
    int start = j - 1, end = j + 1;
    if (j == 0)
    {
        start = 0;
        end = 1;
    }
    else if (j == w - 1)
    {
        start = w - 2;
        end = w - 1;
    }
    while (start <= end)
    {
        if (*((memo + (i + 1) * w) + start) > maxValue)
        {
            maxValue = *((memo + (i + 1) * w) + start);
        }
        start++;
    }
    return maxValue;
}

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int h, w;
        cin >> h >> w;
        int stones[h][w], memo[h][w];
        for (int i = 0; i < h; i++)
        {
            for (int j = 0; j < w; j++)
            {
                cin >> stones[i][j];
                if (i == h - 1)
                    memo[i][j] = stones[i][j];
                else
                    memo[i][j] = 0;
            }
        }
        for (int row = h - 2; row >= 0; row--)
        {
            for (int col = 0; col < w; col++)
            {
                memo[row][col] = stones[row][col] + findMax((int *)memo, row, col, w);
            }
        }
        int ans = 0;
        for (int i = 0; i < w; i++)
        {
            if (ans < memo[0][i])
                ans = memo[0][i];
        }
        cout << ans << endl;
    }
    return 0;
}