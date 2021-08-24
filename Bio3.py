from suffix_trees import STree

string = "GCGAGC"
suffixTree = STree.STree(string)
nodes = [string[i:] for i in range(len(string))]
out = [suffixTree.find(key) for key in sorted(nodes)]
print(out)


