n = int(input())
c = list(map(int, input().split()))

last = [-1 for _ in range(n + 1)]

class FenwickTree:
    def __init__(self, size):
        """Initialize a 0-indexed Fenwick Tree with a given size."""
        self.size = size
        self.tree = [0] * (size + 1)  # We still allocate size + 1 elements

    def update(self, index, delta):
        """Update Fenwick Tree by adding delta at index (0-based)."""
        index += 1  # Shift to 1-based index
        while index <= self.size:
            self.tree[index] += delta
            index += index & -index  # Move to next index

    def prefix_sum(self, index):
        """Compute prefix sum from 0 to index (inclusive)."""
        index += 1  # Shift to 1-based index
        result = 0
        while index > 0:
            result += self.tree[index]
            index -= index & -index  # Move to parent index
        return result

    def range_sum(self, left, right):
        """Compute range sum from left to right (both inclusive)."""
        return self.prefix_sum(right) - self.prefix_sum(left - 1)

fw = FenwickTree(n)
output = 0
for i in range(n):
    output += fw.range_sum(last[c[i]] + 1, i)
    if last[c[i]] != -1:
        fw.update(last[c[i]], -1)
    fw.update(i, 1)
    last[c[i]] = i

print(output)