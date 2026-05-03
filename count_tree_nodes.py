def count_nodes(node):
    if node is None:
        return 0
    # for k, v in node.items():
    #     print(f"k: {k}, v: {v}")
    result = 1
    for _node in node["children"]:
        result += count_nodes(_node)
    return result
    # if node is None:
    #     return 0
    # result = 1
    # for child in node.children:
    #     result += count_nodes(child)
    # return result
