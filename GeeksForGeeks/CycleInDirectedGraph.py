# Problem Description: https://practice.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph

from collections import defaultdict


def creategraph(n, arr, graph):
    i = 0
    while i < 2 * e:
        graph[arr[i]].append(arr[i + 1])
        i += 2


def isCyclicUtil(graph, v, visited, stack):
    visited[v] = True
    stack[v] = True

    for i in graph[v]:
        if(not visited[i]):
            if(isCyclicUtil(graph, i, visited, stack)):
                return True
        elif(stack[i]):
            return True

    stack[v] = False
    return False


def isCyclic(n, graph):
    visited = [False] * n
    stack = [False] * n

    for i in range(n):
        if(not visited[i]):
            if(isCyclicUtil(graph, i, visited, stack)):
                return 1
    return 0


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, e = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        graph = defaultdict(list)
        creategraph(e, arr, graph)
        if isCyclic(n, graph):
            print(1)
        else:
            print(0)
