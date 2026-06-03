from typing import Any
class HashMap:
    def insert(self, key: str, value: Any) -> None:
        original_index = index = self.key_to_index(key)
        first_iteration = True
        while self.hashmap[index] is not None and self.hashmap[index][0] != key:
            if first_iteration == False and index == original_index:
                raise Exception("hashmap is full")
            index = (index + 1) % len(self.hashmap)
            first_iteration = False
        self.hashmap[index] = key, value


    def get(self, key: str) -> Any:
        original_index = index = self.key_to_index(key)
        first_iteration = True
        while self.hashmap[index] is not None:
            k, v = self.hashmap[index]
            if k == key:
                return v
            if first_iteration is False and index == original_index:
                raise Exception("sorry, key not found")
            index = (index + 1) % len(self.hashmap)
            first_iteration = False



    # don't touch below this line

    def __init__(self, size: int) -> None:
        self.hashmap = [None for i in range(size)]

    def key_to_index(self, key: str) -> int:
        total = 0
        for c in key:
            total += ord(c)
        return total % len(self.hashmap)

    def __repr__(self) -> str:
        final = ""
        for i, v in enumerate(self.hashmap):
            if v != None:
                final += f" - {str(v)}\n"
        return final
