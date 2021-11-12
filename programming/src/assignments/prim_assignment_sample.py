import numpy as np

def main():
    vv = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    ee = []
    NN = 16

    Matrix = [[0 for i in range(NN)] for j in range(NN)]

    for i in range(len(vv)):
        for j in range(i+1, len(vv)):
#            ee.append((vv[i], vv[j]))
            ee.append(vv[i]+vv[j])

    edgeNums = np.random.choice(range(len(ee)), size=NN, replace=False)
    ww = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13]
    foundWeights = False
    while not foundWeights:
        weights = list(np.random.choice(ww, size=NN, replace=True))
        x = weights.count(11)
        y = weights.count(12)
        z = weights.count(13)
        if x == 1 and y == 1 and z == 1:
            foundWeights = True


    selectedEdges = list(map(lambda x: ee[x], edgeNums))
    selectedEdges.sort()

    print('selectedEdges = {}'.format(selectedEdges))
    print('weights = {}'.format(weights))

    weightedEdges = list(map(lambda x: (selectedEdges[x], weights[x]), range(NN)))
    print('weightedEdges = {}'.format(weightedEdges))

    print()
    count = 0
    for i in range(len(vv)):
        for j in range(len(vv)):
            edge = vv[i] + vv[j]
            edge2 = vv[j] + vv[i]
            if selectedEdges.count(edge) > 0:
                Matrix[i][j] = weights[count]
                Matrix[j][i] = weights[count]
                if j < len(vv)-1:
                    print('{} & '.format(weights[count]), end='')
                else:
                    print('{} '.format(weights[count]), end='')
                count += 1
            elif j > i and Matrix[i][j] > 0:
                if j < len(vv)-1:
                    print('{} & '.format(Matrix[i][j]), end='')
                else:
                    print('{} '.format(Matrix[i][j]), end='')
            else:
                print('0 & ', end='')
        print('\\\\')



if __name__ == '__main__':
    main()