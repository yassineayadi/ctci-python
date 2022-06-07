"""
Sort Big File: Imagine you have a 20 GB file with one string per line. Explain how you would sort the file.

"""

# how to:
# * divide file into k -1 chunks each read  and sorted individually
# * read in AVAILABLE_MEMORY / k chunks
# * k-1 buffers for chunks , 1 buffer for sorted output
# * priority queue (minheap) based on first element of chunk:
# -> decides which next word to read (and add to output buffer)
# -> as soon as buffer is empty read from file
# -> heapify up
# -> Q: need to resort everytime? A: yes as we always need to evaluate what is the next item in the list

FILE_ON_DISK_SIZE_MB = 20_000

CHUNK_SIZE_MB = 100
MEMORY_SIZE_MB = 500
CHUNKS = 4


class Reader:
    def __init__(self, file: str):
        self.file = file
        self.io = open(file)
        self.is_empty = False

    def read_chunk(self):
        data = self.io.read(CHUNK_SIZE_MB)
        if data == "":
            self.is_empty = True
        return data


class MinHeap:
    def __init__(self, size: int):
        self._heap = [None for _ in range(size)]  # noqa
        self.last = -1
        self.size = size

    def left_key(self, key):
        left_key = (key * 2) + 1
        if left_key < self.size:
            return left_key

    def right_key(self, key):
        right_key = (key * 2) + 2
        if right_key < self.size:
            return right_key

    def parent_key(self, key):
        parent_key = (key - 1) // 2
        if parent_key >= 0:
            return parent_key

    def insert(self, key):
        self._heap[self.last + 1] = key
        self.last += 1

    def get(self, key):
        return self._heap[key]

    def swap(self, k1, k2):
        self._heap[k1], self._heap[k2] = self._heap[k2], self._heap[k1]

    def min_heapify(self, key):
        parent_key = self.parent_key(key)
        if self.get(parent_key) > self.get(key):
            self.swap(parent_key, key)
            self.min_heapify(parent_key)

    @property
    def first(self):
        return 0

    def pop(self):
        stream = self._heap[0]
        data = stream.get_next()
        self.min_heapify(stream)
        return data

    def min_heapify_down(self, key):
        left_key, right_key = self.left_key(key), self.right_key(key)
        if left_key and right_key:
            min_key = (
                left_key
                if self.get(left_key) < self.get(right_key)
                else self.get(right_key)
            )
            if self.get(key) > self.get(min_key):
                self.swap(key, min_key)
                self.min_heapify(min_key)
        elif left_key and key > left_key:
            self.swap(key, left_key)
            self.min_heapify(left_key)
        elif right_key and key > right_key:
            self.swap(key, right_key)
            self.min_heapify(right_key)

    def __iter__(self):
        while any(stream.is_file_empty is False for stream in self._heap):
            yield self.pop()


from dataclasses import dataclass, field


@dataclass
class Streams:
    reader: Reader
    data: list[str] = field(init=False)

    def __post_init__(self):
        self.data = []
        self.get_next()

    def __eq__(self, other: "Streams"):
        if self.data and other.data:
            return self.data[0] == other.data[0]

    def __lt__(self, other):
        if self.data and other.data:
            return self.data[0] < other.data[0]

    def __le__(self, other):
        if self.data and other.data:
            return self.data[0] <= other.data[0]

    @property
    def is_buffer_empty(self):
        return bool(self.data)

    @property
    def is_file_empty(self):
        return self.reader.is_empty

    def get_next(self):
        if self.is_buffer_empty:
            self.data.append(self.reader.read_chunk())
        return self.data.pop(0)


def main():
    files = ["file0.txt", "file1.txt", "file2.txt", "file3.txt"]
    output = "sorted_output.txt"
    readers = [Reader(file) for file in files]
    queue = MinHeap(4)
    streams = [Streams(reader) for reader in readers]
    for stream in streams:
        queue.insert(stream)

    with open(output, "w") as f:
        for item in queue:
            f.write(item)
