# =============================================================================
# PREORDER TRAVERSAL — TWO STYLES
# =============================================================================
# Preorder = visit current node, then left subtree, then right subtree.
# Both versions produce the same output. The difference is HOW the result
# list is built and passed around in memory.
# =============================================================================


# -----------------------------------------------------------------------------
# VERSION 1: MUTATING STYLE (shared list in memory)
# -----------------------------------------------------------------------------
# One list object is created by the original caller.
# Every recursive call receives a REFERENCE to that same list and appends
# directly to it. No merging, no copying. The `return visited` at the end
# is only useful for the very first caller — recursive calls ignore it.
#
# Pros: faster, less memory, fewer moving parts.
# Cons: relies on "spooky action at a distance" — mutation through shared state.
# -----------------------------------------------------------------------------
class BSTNode:
    def preorder(self, visited):
        if self.val is not None:
            visited.append(self.val)  # mutates the ONE shared list
        if self.left is not None:
            self.left.preorder(visited)  # same list reference goes deeper
        if self.right is not None:
            self.right.preorder(visited)  # same list reference again
        return visited  # convenience for the top-level caller


# -----------------------------------------------------------------------------
# VERSION 2: FUNCTIONAL STYLE (new list per call, merged on the way up)
# -----------------------------------------------------------------------------
# Each recursive call creates its OWN fresh list with preorder([]).
# That subtree's result is then merged into the parent's list via extend().
# More list objects exist in memory at once, but each call only touches
# the list it owns — no shared state.
#
# Pros: easier to reason about, no hidden mutation across calls.
# Cons: more allocations, more work, slightly slower.
# -----------------------------------------------------------------------------
class BSTNode:
    def preorder(self, visited):
        if self.val is not None:
            visited.append(self.val)  # append to MY list
        if self.left is not None:
            visited.extend(self.left.preorder([]))  # merge child's NEW list
        if self.right is not None:
            visited.extend(self.right.preorder([]))  # merge child's NEW list
        return visited  # every caller uses this


# =============================================================================
# MEMORY MODEL — THE KEY INSIGHT
# =============================================================================
# Python passes objects by REFERENCE, not by copy.
#
#   shared = []
#   def add(lst): lst.append(1)
#   add(shared)
#   print(shared)  # [1]   <-- the original was mutated
#
# Version 1 leans on this: one list, many references, everyone writes to it.
# Version 2 sidesteps it: each call owns its own list, results flow upward
# via return values.
#
# This same mutate-vs-return-new distinction shows up everywhere:
#   list.sort()       mutates, returns None
#   sorted(list)      returns a new list, original untouched
#   list.reverse()    mutates
#   reversed(list)    returns a new iterator
#
# Rule of thumb: if a function returns None but "did something," it mutated.
# =============================================================================
