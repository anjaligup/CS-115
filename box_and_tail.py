Python 3.11.5 (v3.11.5:cce6ba91b3, Aug 24 2023, 10:50:31) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> L = ["eve", "alice", "bob"]
>>> M = L
>>> L[1] = "mary"
>>> print(M[1])
mary
>>> print(M[2])
bob
>>> L = ["eve", "alice", "bob"]
>>> M = list(L)
>>> L[1] = "mary"
>>> print(M[1])
alice
>>> L = [[1,2], [3,4]]
>>> M = list(L)
>>> L[0][1] = 5
>>> M[0] = [6,7]
>>> print(M)
[[6, 7], [3, 4]]
>>> print(L)
[[1, 5], [3, 4]]
>>> M = L
>>> print(M)
[[1, 5], [3, 4]]
>>> print(L)
[[1, 5], [3, 4]]
>>> L = [[1,1], [2,2]]
>>> M = list(L)
>>> M.append([5,5])
>>> print(L,M)
[[1, 1], [2, 2]] [[1, 1], [2, 2], [5, 5]]
>>> L = [[1,1], [2,2]]
>>> M = [L[1], list(L[0])]
>>> print(L,M)
[[1, 1], [2, 2]] [[2, 2], [1, 1]]
>>> L = [[1,1], [2,2]]
>>> M = [L[1], list(L[0])]
>>> M[0].append([5,5])
>>> print(L,M)
[[1, 1], [2, 2, [5, 5]]] [[2, 2, [5, 5]], [1, 1]]
