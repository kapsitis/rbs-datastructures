It is known that we can check if an undirected graph is 2-colorable with a DFS algorithm that visits all edges and checks that it does not have odd cycles. 

Can you can list algorithmic tasks (YES/NO problems) solvable using DFS traversal of a directed graph?


1. Detecting the presence of a cycle in the directed graph (YES if a cycle exists, NO otherwise).

2. Checking if a directed graph is strongly connected (YES if strongly connected, NO otherwise).

3. Determining if there is a path between two given vertices (YES if a path exists, NO otherwise).

4. Identifying if the directed graph is a DAG (Directed Acyclic Graph) (YES if it is a DAG, NO otherwise).

5. Checking if the directed graph is semi-connected (YES if semi-connected, NO otherwise).

6. Verifying if the directed graph has a cycle of a specific length (YES if such a cycle exists, NO otherwise).

7. Determining if the directed graph is Eulerian (YES if Eulerian, NO otherwise).

8. Checking if the directed graph is k-partite for a given k (YES if k-partite, NO otherwise).

9. Detecting the presence of a strongly connected component with more than one vertex (YES if such a component exists, NO otherwise).

10. Verifying if the directed graph has a Hamiltonian path or cycle (YES if a Hamiltonian path or cycle exists, NO otherwise). Note that this problem is NP-complete, so the DFS solution may not be efficient for large graphs.