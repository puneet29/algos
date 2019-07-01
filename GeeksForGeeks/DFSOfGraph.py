# Problem Description: https://practice.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph

from collections import defaultdict


class Graph():
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):  # add directed edge from u to v.
        self.graph[u].append(v)


def dfsUtil(v, visited, g):
    visited[v] = True
    print(v, end=" ")

    for i in g[v]:
        if(not visited[i]):
            dfsUtil(i, visited, g)


def dfs(g, N):
    '''
    :param g: given adjacency list of graph
    :param N: number of nodes in N.
    :return: print the dfs of the graph from node 0, newline is given by driver code
    '''
    visited = [False] * N
    dfsUtil(0, visited, g)


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        N, E = map(int, input().strip().split())
        g = Graph(N)
        edges = list(map(int, input().strip().split()))
        for i in range(0, len(edges), 2):
            u, v = edges[i], edges[i+1]
            g.addEdge(u, v)
            g.addEdge(v, u)
        dfs(g.graph, N)
        print()
