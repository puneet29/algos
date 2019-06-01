// Problem url: https://www.spoj.com/problems/ARRAYSUB/

#include <iostream>
#include <deque>

using namespace std;

int main()
{
    int i, n, k, ele[1000001];

    cin >> n;

    for (int i = 0; i < n; i++)
    {
        cin >> ele[i];
    }

    cin >> k;
    deque<int> q(k);

    for (i = 0; i < k; i++)
    {
        while (!q.empty() && ele[i] >= ele[q.back()])
            q.pop_back();
        q.push_back(i);
    }

    for (; i < n; i++)
    {
        cout << ele[q.front()] << " ";
        while (!q.empty() && (q.front() <= i - k))
            q.pop_front();
        while (!q.empty() && ele[i] >= ele[q.back()])
            q.pop_back();
        q.push_back(i);
    }
    cout << ele[q.front()];
    return 0;
}