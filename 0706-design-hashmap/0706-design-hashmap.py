class ListNode:
    __slots__ = ("key", "val", "next")
    def __init__(self, key: int, val: int, nxt=None):
        self.key = key
        self.val = val
        self.next = nxt

class MyHashMap:
    def __init__(self, capacity: int = 1009):
        """
        capacity: number of buckets. A prime like 1009 reduces clustering.
        """
        self.capacity = capacity
        self.buckets = [None] * self.capacity

    def _bucket_index(self, key: int) -> int:
        # simple hash: modulo capacity (handles negative keys too)
        return (key % self.capacity + self.capacity) % self.capacity

    def put(self, key: int, value: int) -> None:
        idx = self._bucket_index(key)
        node = self.buckets[idx]

        # if bucket empty, insert new node
        if node is None:
            self.buckets[idx] = ListNode(key, value)
            return

        # otherwise traverse to find if key exists; else append at head for simplicity
        prev = None
        cur = node
        while cur:
            if cur.key == key:
                cur.val = value  # update existing
                return
            prev = cur
            cur = cur.next

        # key not found, append new node at the end (or at head if preferred)
        prev.next = ListNode(key, value)

    def get(self, key: int) -> int:
        idx = self._bucket_index(key)
        cur = self.buckets[idx]
        while cur:
            if cur.key == key:
                return cur.val
            cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        idx = self._bucket_index(key)
        cur = self.buckets[idx]
        prev = None
        while cur:
            if cur.key == key:
                # remove node
                if prev is None:
                    # removing head
                    self.buckets[idx] = cur.next
                else:
                    prev.next = cur.next
                return
            prev = cur
            cur = cur.next
