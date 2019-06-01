// Problem url: https://hack.codingblocks.com/contests/c/101/90

#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

bool compare(pair<string, int> e1, pair<string, int> e2)
{
    if (e1.second == e2.second)
    {
        return (e1.first < e2.first);
    }
    return (e1.second > e2.second);
}

int main()
{
    int x, n, salary;
    string name;
    pair<string, int> employee[100001];
    cin >> x >> n;

    for (int i = 0; i < n; i++)
    {
        cin >> name >> salary;
        employee[i].first = name;
        employee[i].second = salary;
    }
    sort(employee, employee + n, compare);
    for (int i = 0; i < n; i++)
    {
        if (employee[i].second >= x)
        {
            cout << employee[i].first << " " << employee[i].second << endl;
        }
    }

    return 0;
}