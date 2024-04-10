import sys
import pprint
from collections import defaultdict


def Dijkstra(graph, source):
    inf = sys.maxsize
    node_data = {
        "A": {"cost": inf, "pred": []},
        "B": {"cost": inf, "pred": []},
        "C": {"cost": inf, "pred": []},
        "D": {"cost": inf, "pred": []},
        "E": {"cost": inf, "pred": []},
        "F": {"cost": inf, "pred": []},
        "G": {"cost": inf, "pred": []},
        "H": {"cost": inf, "pred": []},
        "I": {"cost": inf, "pred": []},
    }
    visited = []
    least_cost = []
    least_cost_node = []
    temp = source
    node_data[source]["cost"] = 0
    for i in range(len(graph) - 1):
        if temp not in visited:
            visited.append(temp)
            for j in graph[temp]:
                if j not in visited:
                    cost = node_data[temp]["cost"] + graph[temp][j]
                    if cost < node_data[j]["cost"]:
                        least_cost.append(cost)
                        least_cost_node.append(j)
                        node_data[j]["cost"] = cost
                        node_data[j]["pred"] = node_data[temp]["pred"] + [temp]
        x = min(least_cost)
        index = least_cost.index(x)
        temp = least_cost_node[index]
        least_cost_node.pop(index)
        least_cost.pop(index)
    pp = pprint.PrettyPrinter(depth=4)
    pp.pprint(node_data)
    print("\n")


if __name__ == "__main__":
    graph = {
        "A": {"B": 4, "C": 8},
        "B": {"A": 4, "C": 11, "D": 8},
        "C": {"A": 8, "B": 11, "E": 7, "F": 1},
        "D": {"B": 8, "E": 2, "G": 7, "H": 4},
        "E": {"D": 2, "F": 6, "C": 7},
        "F": {"H": 2, "E": 6, "C": 1},
        "G": {"D": 7, "H": 14, "I": 9},
        "H": {"F": 2, "G": 14, "I": 10},
        "I": {"G": 9, "H": 10},
    }

    source = "A"
    Dijkstra(graph, source)
