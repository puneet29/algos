# Problem Description: https://practice.geeksforgeeks.org/problems/snake-and-ladder-problem/

from collections import defaultdict
import queue


class Graph:
    def __init__(self, V):
        self.graph = defaultdict(list)
        self.V = V

    def addEdge(self, u, v, bidir=False):
        self.graph[u].append(v)
        if(bidir):
            self.graph[v].append(u)

    def bfsDistance(self, u, v):
        visited = [False] * self.V
        q = queue.Queue(self.V)
        dist = [0] * self.V

        q.put(u)
        visited[u] = True

        while(not q.empty()):
            node = q.get()
            for neighbor in self.graph[node]:
                if(not visited[neighbor]):
                    q.put(neighbor)
                    visited[neighbor] = True
                    dist[neighbor] = dist[node] + 1
                    if(neighbor == v):
                        return dist[v]
        return dist[v]


t = int(input())

for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    board = [0] * 36
    g = Graph(36)

    for i in range(0, 2*n, 2):
        board[a[i]] = a[i+1] - a[i]

    for u in range(30):
        for dice in range(1, 7):
            v = u + dice + board[u+dice]
            g.addEdge(u, v)

    print(g.bfsDistance(1, 30))
