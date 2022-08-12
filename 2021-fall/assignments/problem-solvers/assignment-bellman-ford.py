
def verbose_bellman_ford(V, E):
    # Compute "infinity" in Bellman-Ford algorithm (larger than any possible path)
    totalAbsWeight = 1
    for edge in E:
        totalAbsWeight += edge[2]

    distance = dict()
    parent = dict()
    for vertex in V:
        distance[vertex] = totalAbsWeight
        parent[vertex] = 'Null'
    distance['v0'] = 0

    for i in range(1, len(V)):
        print('**Phase {}:**'.format(i))
        print()
        print('================')
        for edge in E:
            u = edge[0]
            v = edge[1]
            w = edge[2]
            if distance[v] > distance[u] + w:
                print('Relax :math:`({},{})`'.format(u,v),  end =' ')
                distance[v] = distance[u] + w
                parent[v] = u
                print('{}    {}    {}    {}    {}    {}'.format(distance['v0'], distance['v1'],
                                                                distance['v2'], distance['v3'],
                                                                distance['v4'], distance['v5']))
        print('===============')
        print()


def main():
    V = ['v0', 'v1', 'v2', 'v3', 'v4', 'v5']
    E = [['v0', 'v1', 0], ['v0', 'v2', 0], ['v0', 'v3', 0], ['v0', 'v4', 0], ['v0', 'v5', 0],
         ['v1', 'v4', 3], ['v2', 'v1', 4], ['v2', 'v3', 1], ['v3', 'v4', 5], ['v3', 'v5', -4],
         ['v4', 'v2', -5], ['v4', 'v5', -8], ['v5', 'v1', 5], ['v5', 'v4', 10]]
    verbose_bellman_ford(V,E)


if __name__ == '__main__':
    main()