// Problem url: https://en.wikipedia.org/wiki/Birthday_problem

#include <iostream>

using namespace std;

int main()
{
    // p is the probability of two persons not having same birthday
    float p = 1;

    // Considering the probability for no person being in the room
    int num = 365;
    float denom = 365;
    float people = 0;

    while (p > 0.5)
    {
        p *= (num / denom);
        num--;
        people++;
    }

    cout << "Minimum number of people required to get " << (1-p)*100 <<" probability is " << people << endl;

    return 0;
}