from collections import defaultdict
from typing import List

class Node:
    __slots__ = ("name","children","sig","deleted")
    def __init__(self, name: str):
        self.name     = name
        self.children = {}      # name -> Node
        self.sig      = ""      # subtree signature
        self.deleted  = False   # mark if to be pruned

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        # 1) Build the trie of folders
        root = Node("")
        for path in paths:
            cur = root
            for folder in path:
                cur = cur.children.setdefault(folder, Node(folder))

        # 2) Post-order: compute subtree-signature for every node,
        #    but count only those with children (non-leaves).
        count = defaultdict(int)
        def dfs_sig(node: Node) -> str:
            # compute child signatures
            subs = []
            for child in node.children.values():
                child_sig = dfs_sig(child)
                subs.append((child.name, child_sig))
            subs.sort(key=lambda x: x[0])  # canonical order
            # build this node's signature (ignores its own name)
            sig = "(" + "".join(name + sig for name, sig in subs) + ")"
            node.sig = sig
            # count only if this node has at least one child
            if subs:
                count[sig] += 1
            return sig

        for child in root.children.values():
            dfs_sig(child)

        # 3) Mark for deletion: any non-leaf whose signature repeats
        def dfs_mark(node: Node):
            if node.children and count[node.sig] > 1:
                node.deleted = True
                return
            for child in node.children.values():
                dfs_mark(child)

        for child in root.children.values():
            dfs_mark(child)

        # 4) Collect remaining paths as List[List[str]]
        result, stack = [], []
        def dfs_collect(node: Node):
            for child in node.children.values():
                if child.deleted:
                    continue
                stack.append(child.name)
                result.append(stack.copy())
                dfs_collect(child)
                stack.pop()

        dfs_collect(root)
        return result
