#!/usr/bin/env python3

INPUTFILE = "input"
START = "start"
END = "end"

def _find_paths_(path, connections):
    results = []
    for connection in connections[path[-1]]:
        if connection.islower() and connection in path:
            continue
        path_temp = path.copy()
        path_temp.append(connection)
        if connection == END:
            results.append(path_temp)
        else:
            for path_ in _find_paths_(path_temp, connections):
                results.append(path_)
    return results

def _find_paths(visited, connections):
    result = []
    for path in visited:
        result = _find_paths_(path, connections)
    return result # list of list of strings

def _find_paths_2(path, connections):
    results = []
    for connection in connections[path[-1]]:
        if connection.islower() and connection in path:
            if connection == END:
                continue
            if connection == START:
                continue
            test = False
            for cave in path:
                if cave.islower() and path.count(cave) > 1:
                    test = True
                    break
            if test:
                continue
        path_temp = path.copy()
        path_temp.append(connection)
        if connection == END:
            results.append(path_temp)
        else:
            for path_ in _find_paths_2(path_temp, connections):
                results.append(path_)
    return results

def _find_paths2(visited, connections):
    result = []
    for path in visited:
        result = _find_paths_2(path, connections)
    return result # list of list of strings

def main():
    f = open(INPUTFILE, 'r')
    result = []
    connections = {} # dict of caves
    line = f.readline().rstrip()
    while line:
        path = line.split("-")
        for i in [0, 1]:
            if not path[i] in connections:
                connections[path[i]] = [path[1-i]]
            else:
                if path[1-i] not in connections[path[i]]:
                    connections[path[i]].append(path[1-i])
        line = f.readline().rstrip()
    f.close()
    for cave in connections.keys():
        connections[cave].sort()
    paths = _find_paths([[START]], connections)
    print("Part 1: Number of paths:", len(paths))
    paths = _find_paths2([[START]], connections)
    print("Part 2: Number of paths:", len(paths))

if __name__ == "__main__":
    main()