// Question taken from Redhat test.

#include <stdio.h>
#include <stdlib.h>
#include <iostream>
using namespace std;

// Dir: 0->right, 1->down, 2->left, 3->up
void solution(int R, int C, int **M)
{
    int row = 0, col = 0, dir = 0;
    int Rmax = R - 1, Cmax = C - 1, Cmin = 0, Rmin = 0;
    for (int i = 0; i < R * C; i++)
    {
        cout << M[row][col];
        if (dir == 0 && col == Cmax)
        {
            dir = 1;
        }
        else if (dir == 1 && row == Rmax)
        {
            dir = 2;
            Rmin++;
            Cmax--;
        }
        else if (dir == 2 && col == Cmin)
        {
            dir = 3;
        }
        else if (dir == 3 && row == Rmin)
        {
            dir = 0;
            Rmax--;
            Cmin++;
        }
        if (dir == 0)
        {
            col++;
        }
        else if (dir == 1)
        {
            row++;
        }
        else if (dir == 2)
        {
            col--;
        }
        else
        {
            row--;
        }
    }
}

// Following is the part of the program and is provided as an assistance to read the input.
int main()
{
    int R, C, i, j;
    scanf("%d %d", &R, &C);
    int **M = (int **)malloc(R * sizeof(int *));
    for (i = 0; i < R; i++)
        M[i] = (int *)malloc(C * sizeof(int));
    for (i = 0; i < R; i++)
        for (j = 0; j < C; j++)
            scanf("%d", &M[i][j]);
    solution(R, C, M);
    return 0;
}