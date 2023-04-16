import sys

vertices = [1,2,3,4,5,6,7,8,9,10,11,12,13]
edges = [(1,7), (1,9),
         (2,5),(2,9),(2,8),(2,13), 
         (3,10),
         (4,6), (4,8), 
         (6,7), (6,10), (6,11), (6,13), 
         (7,12), 
         (8,10)]

Q = []

def visit(v):
    print(v, end=' ')
    Q.append(v)


def main(s):
    colors = dict()
    for v in vertices: 
        if v != s:
            colors[v] = 'white'
    colors[s] = 'gray'
    visit(s)
    while len(Q) > 0: 
        u = Q[0]
        adjU = []
        for (a,b) in edges: 
            if a == u: 
                adjU.append(b)
            elif b == u: 
                adjU.append(a)
        adjU.sort()
        for v in adjU: 
            if colors[v] == 'white': 
                colors[v] = 'gray'
                visit(v)
        Q.pop(0)
        colors[u] = 'black'
        



if __name__=='__main__':
    s = int(sys.argv[1])
    main(s)