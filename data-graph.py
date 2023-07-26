# Small data graph
graph = {
    'A':{'B':35},
    'B':{'A':35,'F':430},
    'E':{'F':870},
    'F':{'B':430,'E':870},
}

# Small data graph
graph = {
    'A':{'B':35},
    'B':{'A':35,'C':220,'F':430},
    'C':{'B':220,'D':575},
    'D':{'C':575,'E':867},
    'E':{'D':867,'F':870,'H':1160},
    'F':{'B':430,'E':870,'G':670},
    'G':{'F':670,'H':40},
    'H':{'G':40,'E':1160},
}

# Large data graph
graph = {
    'A':{'B':35},
    'B':{'A':35,'C':220,'F':430},
    'C':{'B':220,'D':575},
    'D':{'C':575,'E':867},
    'E':{'D':867,'F':870,'H':1160},
    'F':{'B':430,'E':870,'G':670},
    'G':{'F':670,'H':40,'I':800},
    'H':{'G':40,'N':200'E':1160},
    'I':{'G':800,'J':1200},
    'J':{'I':1200,'K':1500},
    'K':{'J':1500,'L':800},
    'L':{'K':800,'M':740},
    'M':{'L':740,'N':500},
    'N':{'M':500,'H':200},
}

# floyd-warshall matrix for small data
[
    [0, 35, INF, INF, INF, INF, INF, INF],
    [35, 0, 220, INF, INF, 430, INF, INF],
    [INF, 220, 0, 575, INF, INF, INF, INF],
    [INF, INF, 575, 0, 867, INF, INF, INF],
    [INF, INF, INF, 867, 0, 870, INF, 1160],
    [INF, 430, INF, INF, 870, 0, 670, INF],
    [INF, INF, INF, INF, INF, 670, 0, 40],
    [INF, INF, INF, INF, 1160, INF, 40, 0],
]

# floyd-warshall matrix for large data
[   
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