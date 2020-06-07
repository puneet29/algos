# Algorithms and Data Structures

## Algorithms

Implementation of algorithms and data structures from various programming portals are given in respective directories:

- [GeeksForGeeks](GeeksForGeeks/)
- [spoj](spoj/)
- [LeetCode](LeetCode/)
- [CodeChef](CodeChef/)
- [Algorithmic Toolbox](AlgorithmicToolbox/)
- [Miscellaneous](misc/)

## Data Structures

- ### TRIE

1. It is an information retrieval data structure.
2. It is also called radix/prefix tree.
3. It is used for efficient searching of keys in a container. If the keys are strings, the particular string can be searched in O(n), where n denotes the length of the string to be searched.
4. Each node of the trie has multiple branches, a node where a word ends is marked with terminal = true.

Implementation : [trie](DataStructures/trie.cpp)

![Trie example](Images/trie.jpeg)

## Series

### Catalan Series

#### Formula

![Formula for catalan series](https://latex.codecogs.com/gif.latex?C_{0}%20=%201%20\%20and%20\%20C_{n+1}%20=%20\sum_{i=0}^{n}C_{i}C_{n-i}%20\%20for%20\%20n\geq%200)

1. Number of possible binary search trees with n keys.
2. Number of expressions containing n pairs of parantheses which are correctly matched. For n = 3, possible expressions are ((())), ()()(), (())(), ()(()), (()())
3. Number of ways n + 1 factors can be completely paranthesized, for eg. N = 3 and 3 + 1 factors: (a, b, c, d), we have: (ab)(cd), a(b(cd)), ((ab)c)d, (a(bc))d, a((bc)d).
4. Number of ways a convex polygon of n + 2 sides can split into triangles by connecting vertices.
5. Number of different unlabelled binary trees can be there with n nodes.
6. The number of paths with 2n steps on a rectangular grid from botton left, i.e., (n-1, 0) to top right (0, n-1) that do not cross above the main diagonal.
7. Number of ways to form a "mountain range"  with n upstrokes and n downstrokes.
