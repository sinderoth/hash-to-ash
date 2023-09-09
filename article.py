from typing import List, Tuple
from helpers import *


class Article:
    MAX_LOAD_FACTOR: float = 0.65
    MARKED_INDEX: int = -99
    EMPTY_INDEX: int = -1
    EMPTY_KEY: str = ""

    def __init__(self, table_size: int, h1_param: int, h2_param: int) -> None:
        """
        Initialize an Article instance.

        Args:
            table_size (int): The size of the hash table.
            h1_param (int): The first hash function parameter.
            h2_param (int): The second hash function parameter.
        """
        self.table_size: int = table_size
        self.h1_param: int = h1_param
        self.h2_param: int = h2_param
        self.n: int = 0
        self.table: List[Tuple[str, int]] = [
            (self.EMPTY_KEY, self.EMPTY_INDEX)
        ] * table_size

    def get(self, key: str, nth: int, path: List[int]) -> int:
        probe, k = 0, 1

        for _ in range(self.table_size):
            hashed_index = self.hash_function(key, probe)
            word, occ = self.table[hashed_index]
            if probe > 0:
                path.append(hashed_index)

            if word == "" and occ != self.MARKED_INDEX:
                break

            if word == key and occ != self.MARKED_INDEX:
                if k == nth:
                    return occ
                k += 1
            probe += 1

        return -1

    def insert(self, key: str, original_index: int) -> int:
        """
        tries to keep word order in the text file
        lower original indexed word should be found earlier with this
        """
        if self.get_load_factor() > self.MAX_LOAD_FACTOR:
            self.expand_table()

        probes = 0
        for i in range(self.table_size):
            hashed_index = self.hash_function(key, i)
            if self.table[hashed_index][0] == key:
                if self.table[hashed_index][1] > original_index:
                    temp = self.table[hashed_index][1]
                    self.table[hashed_index] = (key, original_index)
                    original_index = temp

            if self.table[hashed_index][0] == self.EMPTY_KEY:
                self.table[hashed_index] = (key, original_index)
                self.n += 1
                return probes
            probes += 1
        return probes

    def expand_table(self) -> None:
        self.table_size = next_prime_after(2 * self.table_size)
        self.h2_param = first_prime_before(self.table_size)

        old_table = self.table
        self.table = [(self.EMPTY_KEY, self.EMPTY_INDEX)] * self.table_size
        self.n = 0

        for key, original_index in old_table:
            if key != self.EMPTY_KEY:
                self.insert(key, original_index)

    def remove(self, key: str, nth: int) -> int:
        k = 1
        probes = -1
        for i in range(self.table_size):
            probes += 1
            hashed_index = self.hash_function(key, i)

            if (
                self.table[hashed_index][0] == key
                and self.table[hashed_index][1] != self.MARKED_INDEX
            ):
                if k == nth:
                    self.table[hashed_index] = (self.EMPTY_KEY, self.MARKED_INDEX)
                    self.n -= 1
                    return probes
                k += 1

        return -1

    def get_load_factor(self) -> float:
        return self.n / self.table_size

    def hash_function(self, key: str, i: int) -> int:
        key = convert_str_to_int(key)
        return (self.h1(key) + i * self.h2(key)) % self.table_size

    def h1(self, key: int) -> int:
        count = 0
        for i in range(32):
            if key & (1 << i):
                count += 1
        return count * self.h1_param

    def h2(self, key: int) -> int:
        return self.h2_param - (key % self.h2_param)

    def get_all_words_from_file(self, filepath: str) -> None:
        with open(filepath, "r") as file:
            words = file.read().split()
            for index, word in enumerate(words, start=1):
                self.insert(word, index)

    def print_table(self) -> None:
        name_max_length = 0
        temp = 0
        max_index = 0
        max_index_length = 0
        blank_diff = 0
        index_length = 0

        for entry in self.table:
            name_max_length = max(name_max_length, len(entry[0]))
            max_index = max(max_index, entry[1])

        if max_index <= 0:
            name_max_length = 5
            max_index = 999

        temp = max_index
        while temp != 0:
            temp //= 10
            max_index_length += 1

        print("|" + "-" * (name_max_length + max_index_length + 5) + "|")

        print(
            f"| {' ' * ((name_max_length - 1) // 2)}K{' ' * ((name_max_length - 1) // 2)} | {' ' * ((max_index_length - 1) // 2)}I{' ' * ((max_index_length - 1) // 2)} |"
        )

        print("|" + "-" * (name_max_length + max_index_length + 5) + "|")

        for entry in self.table:
            index_length = 0
            blank_diff = name_max_length - len(entry[0])

            print(
                f"| {' ' * ((blank_diff // 2) + 1)}{entry[0]}{' ' * ((blank_diff // 2) + 1)} |",
                end="",
            )

            temp = entry[1]
            while temp != 0:
                temp = int(temp / 10)
                index_length += 1
            blank_diff = max_index_length - index_length

            print(f" {' ' * ((blank_diff // 2) + 1)}{entry[1]}", end="")

            if entry[1] > 0 or (entry[1] == -1 and max_index_length % 2 == 0):
                print(" ", end="")

            if entry[1] == -1 and max_index_length < 2:
                print(" ", end="")

            if (max_index_length - index_length) % 2 != 0 and entry[1] > 0:
                print(" ", end="")

            if entry[1] > 0 and max_index_length < 2:
                print(" ", end="")

            if entry[1] == -99 and max_index_length % 2 != 0 and max_index_length > 1:
                print(" ", end="")

            print(" |")

            print("|" + "-" * (name_max_length + max_index_length + 5) + "|")
