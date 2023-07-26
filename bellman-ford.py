import sys
import time

def bellmanford(graph,src,dest):
    start_time = time.time()
    inf = sys.maxsize
    node_data = {
        'A':{'cost':inf,'pred':[]},
        'B':{'cost':inf,'pred':[]},
        'C':{'cost':inf,'pred':[]},
        'D':{'cost':inf,'pred':[]},
        'E':{'cost':inf,'pred':[]},
        'F':{'cost':inf,'pred':[]},
        'G':{'cost':inf,'pred':[]},
        'H':{'cost':inf,'pred':[]},
        'I':{'cost':inf,'pred':[]},
        'J':{'cost':inf,'pred':[]},
        'K':{'cost':inf,'pred':[]},
        'L':{'cost':inf,'pred':[]},
        'M':{'cost':inf,'pred':[]},
        'N':{'cost':inf,'pred':[]},
    }
    node_data[src]['cost'] = 0
    for i in range(13):
        print('Iteration '+str(i))
        for itr in graph:
            for neighbor in graph[itr]:
                cost = node_data[itr]['cost'] + graph[itr][neighbor]
                if cost < node_data[neighbor]['cost']:
                    node_data[neighbor]['cost'] = cost
                    if node_data[neighbor]['cost'] == inf:
                        node_data[neighbor]['pred'] = node_data[itr]['pred'] + list(itr)
                    else:
                        node_data[neighbor]['pred'].clear()
                        node_data[neighbor]['pred'] = node_data[itr]['pred'] + list(itr)

        print(node_data)


    print("Shortest Distance: " + str(node_data[dest]['cost']))
    print("Shortest Path: " + str(node_data[dest]['pred']))
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    graph = {
        'A':{'B':35},
        'B':{'A':35,'C':220,'F':430},
        'C':{'B':220,'D':575},
        'D':{'C':575,'E':867},
        'E':{'D':867,'F':870,'H':1160},
        'F':{'B':430,'E':870,'G':670},
        'G':{'F':670,'H':40,'I':800},
        'H':{'G':40,'N':200,'E':1160},
        'I':{'G':800,'J':1200},
        'J':{'I':1200,'K':1500},
        'K':{'J':1500,'L':800},
        'L':{'K':800,'M':740},
        'M':{'L':740,'N':500},
        'N':{'M':500,'H':200},
    }

    source = 'A'
    destination = 'E'
bellmanford(graph,source,destination)