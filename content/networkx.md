Title: Generating Running Routes with NetworkX
Date: 2020-03-28 22:47
Modified: 2020-03-29 16:24
Category: Computer Science
Tags: graph theory, networkx
Slug: networkx
Status: draft

https://networkx.github.io/


```python
import networkx as nx
import matplotlib.pyplot as plt
```


```python
G = nx.petersen_graph()
plt.subplot(121)

nx.draw(G, with_labels=True, font_weight='bold')
plt.subplot(122)

nx.draw_shell(G, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')
```


![png](output_3_0.png)



```python
# As an example here is code to use Dijkstra’s algorithm to find the shortest weighted path
G = nx.Graph()
e = [('a', 'b', 0.3), ('b', 'c', 0.9), ('a', 'c', 0.5), ('c', 'd', 1.2)]
G.add_weighted_edges_from(e)
print(nx.dijkstra_path(G, 'a', 'd'))
```

    ['a', 'c', 'd']


![small neighbourhood map]({static}/images/test-nodes.png)


```python
G = nx.Graph()
e = [(1,2), (1,3), (3,4), (3,8), (4,5), (4,7), (5,6), (5,7), (7,11),
     (8,9), (9,10), (9,15), (10,11), (10,17), (11,12), (11,16),
     (12,13), (12,14), (13,13), (15,16), (15,19), (16,17), (17,18),
     (19,20)]
G.add_edges_from(e)
```


```python
nx.draw(G, with_labels=True, font_weight='bold')
```


![png](output_7_0.png)



```python
G = nx.MultiGraph()
e = [(1,2, 0.08), (1,3, 0.08), (3,4, 0.17), (3,8, 0.15), (4,5, 0.17),
     (4,7, 0.27), (5,6, 0.07), (5,7, 0.09), (7,11, 0.01), (8,9, 0.14),
     (9,10, 0.11), (9,15, 0.19), (10,11, 0.15), (10,17, 0.09),
     (11,12, 0.07), (11,16, 0.37), (12,13, 0.09), (12,14, 0.26),
     (13,13, 0.06), (15,16, 0.11), (15,19, 0.06), (16,17, 0.10),
     (17,18, 0.04), (19,20, 0.11)]
G.add_weighted_edges_from(e)
```


```python
nx.draw(G, with_labels=True, font_weight='bold')
```


![png](output_9_0.png)



```python
print(nx.dijkstra_path(G, 2, 20))
```

    [2, 1, 3, 8, 9, 15, 19, 20]



```python
print(nx.dijkstra_path(G, 1, 13))
```

    [1, 3, 4, 5, 7, 11, 12, 13]



```python

```
