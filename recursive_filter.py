def recursive_filter(predicate, items, acc=[]):
    if len(items) == 0:
        return acc

    # head = items[0]
    # tail = items[1:]

    # if predicate(head):
    #     acc.append(head)
    return [head for head in items[:1] if predicate(items[0])] + recursive_filter(
        predicate, items[1:], acc
    )
    # return [head] + recursive_filter(predicate, tail, acc)
    # return [head for head in recursive_filter(predicate, items[1:], acc) if predicate(items[0])]


def recursive_filter_v2(predicate, items):
    return (
        []
        if len(items) == 0
        else (
            ([items[0]] if predicate(items[0]) else [])
            + recursive_filter(predicate, items[1:])
        )
    )


def recursive_filter_v3(predicate, items):
    if len(items) == 0:
        return []

    head = items[0]
    tail = items[1:]

    if predicate(head):
        return [head] + recursive_filter(predicate, tail)
    return recursive_filter(predicate, tail)
