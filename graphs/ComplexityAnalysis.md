# Complexity Analysis of Graph Algorithms

## Representation

### Adjacency Matrix
Add, Remove vertex: O(V^2)
Add, Remove edge: O(1)

### Adjacency List
Add vertex: O(1)  
Remove vertex: O(V + E)  
Add edge: O(1)
Remove edge: O(E)

## Cycle detection
O(V)

## Dijkstra Shortest Path
O(VlogV)
Each vertex is added to the priority queue at most once. And  
pq operations are O(logN).

## Bellman-Ford Single Source Shortest Path
O(VE)
Relax each edge V times.

## Depth First Search
O(V)

## Breadth First Search
O(V)

## Topological Sort
O(V + E)
We find the indegrees of each vertex in O(E), and
place all those vertices with indegree 0 into a
queue. We pop from the queue V times, each time
decrementing the indegrees of its neighbors. If
the neighbor reaches an indegree of 0, we add it
to the queue.

