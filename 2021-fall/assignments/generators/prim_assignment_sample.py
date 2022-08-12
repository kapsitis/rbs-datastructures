import numpy as np

def main():
    vv = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    ee = []
    # The number of edges
    numE = 11
    # The number of vertices
    numV = len(vv)

    Matrix = [['0' for i in range(numV)] for j in range(numV)]

    # Create all edges
    for i in range(numV):
        for j in range(i+1, numV):
            ee.append(vv[i]+vv[j])

    selectedEdges = np.random.choice(ee, size=numE, replace=False)
    ww = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13]
    foundWeights = False
    while not foundWeights:
        weights = list(np.random.choice(ww, size=numE, replace=True))
        x = weights.count(11)
        y = weights.count(12)
        z = weights.count(13)
        if x == 1 and y == 1 and z == 1:
            foundWeights = True

    count = 0
    for i in range(numV):
        for j in range(i+1, numV):
            edge = vv[i]+vv[j]
            if edge in selectedEdges:
                ss = str(weights[count])
                if weights[count] == 11:
                    ss = 'x'
                if weights[count] == 12:
                    ss = 'y'
                if weights[count] == 13:
                    ss = 'z'
                Matrix[i][j] = str(ss)
                Matrix[j][i] = str(ss)
                count += 1

    #print('selectedEdges = {}'.format(selectedEdges))
    #print('weights = {}'.format(weights))
    # Just to print weighted edges
    weightedEdges = list(map(lambda x: (selectedEdges[x], weights[x]), range(numE)))
    print('weightedEdges = {}'.format(weightedEdges))

    # Output LaTeX
    print()
    count = 0
    for i in range(len(vv)):
        for j in range(len(vv)):
            print('{} '.format(Matrix[i][j]), end='')
            if j < len(vv) - 1:
                print('& ', end='')
        print('\\\\')



if __name__ == '__main__':
    main()