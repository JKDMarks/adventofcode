import re
from operator import mul
from functools import reduce

from pdb import set_trace as db


def make_dict(f):
    return dict([make_tuple(t) for t in f.read().split("\n\n")])


def make_tuple(tile_str):
    tile_id, tile = tile_str.split(":\n")
    tile_id = int(tile_id[5:])
    tile = [list(t) for t in tile.split("\n")]
    return (tile_id, tile)


with open("test-input.txt") as f:
    test_tiles = make_dict(f)

with open("input.txt") as f:
    tiles = make_dict(f)


def make_edges(tiles):
    edge_dict = {}

    for id, tile in tiles.items():
        edges = []
        edge_dict[id] = edges
        edges += tile[0], tile[9]  # , tile[0][::-1], tile[9][::-1]

        verts = [[], []]
        for t in tile:
            verts[0] += t[0]
            verts[1] += t[9]

        edges += verts[0], verts[1]  # , verts[0][::-1], verts[1][::-1]

    return edge_dict


def make_adj(tiles, is_p1=False):
    edges = make_edges(tiles)
    adj = {k: [] for k in tiles}

    for id1, edges1 in edges.items():
        for id2, edges2 in {k: v for (k, v) in edges.items() if k != id1}.items():
            # if id1 == 3079 and id2 == 2473:
            #     db
            for (i1, e1) in enumerate(edges1):
                for (i2, e2) in enumerate(edges2):
                    if e1 == e2:
                        adj[id1] += [{"id": id2, "fwd": True, "e1": i1, "e2": i2}]
                    elif e1[::-1] == e2:
                        adj[id1] += [{"id": id2, "fwd": False, "e1": i1, "e2": i2}]

    if is_p1:
        corners = [k for (k, v) in adj.items() if len(v) == 2]
        print(reduce(mul, corners, 1))  # part 1

    return adj


print(make_adj(test_tiles, True))  # 20899048083289
print(make_adj(tiles, True))  # 83775126454273
