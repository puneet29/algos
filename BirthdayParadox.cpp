// Problem url: 

#include <iostream>

using namespace std;

int main()
{
    // p is the probability of two persons not having same birthday
    float p = 1;

    // Considering the probability for no person being in the room
    int num = 365;
    int denom = 365;
    int people = 0;

    while (p > 0.5)
    {
        p *= (num / denom);
        num--;
        people++;
    }

    cout << "Probability of two person having same birthday is " << p << endl;

    return 0;
}