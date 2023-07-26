import sys
import time
from heapq import heapify, heappush, heappop

def dijsktra(graph,src,dest):
    start_time = time.time()
    inf = sys.maxsize
    node_data = {
        'A':{'cost':inf,'pred':[]},
        'B':{'cost':inf,'pred':[]},
        'E':{'cost':inf,'pred':[]},
        'F':{'cost':inf,'pred':[]},
    }
    node_data[src]['cost'] = 0
    visited = []
    temp = src
    for i in range(3):
        if temp not in visited: # TODO: Reassign source
            visited.append(temp)
            min_heap = []
            for j in graph[temp]:
                if j not in visited:
                    cost = node_data[temp]['cost'] + graph[temp][j]
                    if cost < node_data[j]['cost']:
                        node_data[j]['cost'] = cost
                        node_data[j]['pred'] = node_data[temp]['pred'] + [temp]
                    heappush(min_heap,(node_data[j]['cost'],j))
        heapify(min_heap)
        temp = min_heap[0][1]
    print("Shortest Distance: " + str(node_data[dest]['cost']))
    print("Shortest Path: " + str(node_data[dest]['pred'] + list(dest)))
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    graph = {
        'A':{'B':35},
        'B':{'A':35,'F':430},
        'E':{'F':870},
        'F':{'B':430,'E':870},
    }

    source = 'A'
    destination = 'E'
    dijsktra(graph,source,destination)