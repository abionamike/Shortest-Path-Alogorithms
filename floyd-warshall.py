import sys
import time

numberOfVertices = 14
INF = sys.maxsize

def floyd_warshall(G):
    start_time = time.time()
    distance = list(map(lambda i: list(map(lambda j: j, i)), G))

    # Adding vertices individually
    for k in range(numberOfVertices):
        for i in range(numberOfVertices):
            for j in range(numberOfVertices):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    print_solution(distance)
    print("--- %s seconds ---" % (time.time() - start_time))

def print_solution(distance):
    for i in range(numberOfVertices):
        for j in range(numberOfVertices):
            if(distance[i][j] == INF):
                print("INF", end=" ")
            else:
                print(distance[i][j], end="  ")
        print(" ")

G = [   
        [0, 35, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [35, 0, 220, INF, INF, 430, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, 220, 0, 575, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, 575, 0, 867, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, 867, 0, 870, INF, 1160, INF, INF, INF, INF, INF, INF],
        [INF, 430, INF, INF, 870, 0, 670, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, 670, 0, 40, 800, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, 1160, INF, 40, 0, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, 800, INF, 0, 1200, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, 1200, 0, 1500, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, 1500, INF, 800, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 800, 0, 740, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 740, 0, 500],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 500, INF],
    ]
    
floyd_warshall(G)