# Problem Description: https://practice.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/

from collections import defaultdict


class Graph():
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):  # add directed edge from u to v.
        self.graph[u].append(v)


def isCyclicUtil(g, v, visited, parent):
    visited[v] = True

    for i in g[v]:
        if(visited[i] == False):
            if(isCyclicUtil(g, i, visited, v)):
                return True
        elif(parent != i):
            return True
    return False


def isCyclic(g, N):
    visited = [False] * N

    for i in range(N):
        if(visited[i] == False):
            if(isCyclicUtil(g, i, visited, -1)):
                return True
    return False


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        N, E = map(int, input().strip().split())
        g = Graph(N)
        edges = list(map(int, input().strip().split()))
        for i in range(0, len(edges), 2):
            u, v = edges[i], edges[i+1]
            g.addEdge(u, v)  # add an undirected edge from u to v
            g.addEdge(v, u)
        print(isCyclic(g.graph, N))
