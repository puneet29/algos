# Problem Description: https://practice.geeksforgeeks.org/problems/bfs-traversal-of-graph/

from collections import defaultdict
import queue


class Graph():
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):  # add directed edge from u to v.
        self.graph[u].append(v)


def bfs(g, N):
    '''
    :param g: given adjacency list of graph
    :param N: number of nodes in N.
    :return: print the bfs of the graph from node 0, newline is given by driver code
    '''

    q = queue.Queue(maxsize=N)
    visited = [False] * N
    q.put(0)
    visited[0] = True

    while(not q.empty()):
        node = q.get()
        print(node, end=" ")
        for i in g[node]:
            if(not visited[i]):
                q.put(i)
                visited[i] = True


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        N, E = map(int, input().strip().split())
        g = Graph(N)
        edges = list(map(int, input().strip().split()))
        for i in range(0, len(edges), 2):
            u, v = edges[i], edges[i+1]
            g.addEdge(u, v)  # add a directed edge from u to v
        bfs(g.graph, N)  # print bfs of graph
        print()
