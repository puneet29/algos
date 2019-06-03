#include <iostream>

using namespace std;

int main()
{
    int n;
    cin >> n;
    while (n)
    {
        int ans = 1;
        for (int i = 2; i <= n; i++)
        {
            ans += i * i;
        }
        cout << ans << endl;
        cin >> n;
    }
    return 0;
}