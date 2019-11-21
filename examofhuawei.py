import sys

de = dict()

inx = sys.stdin.readline().strip()
ds = inx.split("],")

rel = dict()
ks = []
for v in ds:
    vx = v.split(":")
    vl = vx[1]
    if vl[-1] == "]":
        vl = vl[1:-1].split(",")
    else:
        vl = vl[1:].split(",")

    k = vx[0]
    ks.append(k)
    rel[k] = vl

# print(rel)

des = []
for k in ks:
    for l in rel[k]:
        des.append([k, l])

# print(des)


class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

    def set_ch(self, c):
        self.children.append(c)

    def print_n(self):
        print(self.name)


def get_path(root: Node, n: list):
    if len(root.children) < 1 and root.name not in n:
        return []
    if root.name in n:
        return [[root.name]]
    a = []
    for x in root.children:
        tp = n[:]
        tp.append(root.name)

        a += get_path(x, tp)
    return [[root.name] + i for i in a]


al = dict()
for k in ks:
    if k not in al.keys():
        node = Node(k)
        al[k] = node

    for v in rel[k]:
        if v not in al.keys():
            node = Node(v)
            al[v] = node
        al[k].set_ch(al[v])

# for l in al[ks[0]].children:
    # print(l.name)
temp = []
z = (get_path(al[ks[0]], temp))
for x in z:
    s = set(x)
    if len(x) > len(s):
        print("".join(sorted(s)))
# 1:[2,3],2:[4],3:[4],4:[1]
