#include <iostream>

using namespace std;

void multiply(int *fact, int &n, int no)
{
    int carry = 0;
    for (int i = 0; i < n; i++)
    {
        int product = fact[i] * no + carry;
        fact[i] = product % 10;
        carry = product / 10;
    }
    while (carry)
    {
        fact[n] = carry % 10;
        carry = carry / 10;
        n++;
    }
}

void bigFactorial(int num)
{
    // Considering that the factorial doesn't exceed more than 1000 digits
    int *fact = new int[1000];

    // Factorial of 0 is 1, Base case
    fact[0] = 1;

    int n = 1; // n is the length of factorial

    for (int i = 2; i < num; i++)
    {
        multiply(fact, n, i);
    }
    for (int i = n - 1; i >= 0; i--)
    {
        cout << fact[i];
    }
    cout << endl;
}

int main()
{
    bigFactorial(100);
    return 0;
}