// Problem Description: https://practice.geeksforgeeks.org/problems/get-minimum-element-from-stack/1/

#include <bits/stdc++.h>
using namespace std;
class _stack
{
    stack<int> s;
    int minEle;

public:
    int getMin();
    int pop();
    void push(int);
};
int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int q;
        cin >> q;
        _stack *a = new _stack();
        while (q--)
        {
            int qt;
            cin >> qt;
            if (qt == 1)
            {
                //push
                int att;
                cin >> att;
                a->push(att);
            }
            else if (qt == 2)
            {
                //pop
                cout << a->pop() << " ";
            }
            else if (qt == 3)
            {
                //getMin
                cout << a->getMin() << " ";
            }
        }
        cout << endl;
    }
}

int _stack ::getMin()
{
    if (s.empty())
    {
        return -1;
    }
    else if (minEle == -1)
    {
        stack<int> temp;
        while (!s.empty())
        {
            temp.push(s.top());
            s.pop();
        }
        while (!temp.empty())
        {
            push(temp.top());
            temp.pop();
        }
    }
    return minEle;
}
/*returns poped element from stack*/
int _stack ::pop()
{
    if (s.empty())
    {
        return -1;
    }
    int x = s.top();
    s.pop();

    if (x == minEle)
    {
        minEle = -1;
    }

    return x;
}
/*push element x into the stack*/
void _stack::push(int x)
{
    if (s.empty())
    {
        minEle = x;
    }
    else if (x < minEle)
    {
        minEle = x;
    }
    s.push(x);
}
