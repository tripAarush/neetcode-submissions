class TimeMap:
    from collections import defaultdict
    def __init__(self):
        # hashmap with key pointing to list of times, each time points to value
        # key will point to list with 2 lists in it, one for times (ordered) one for val corresponding idxs
        self.hashmap = defaultdict(list)
    
    def binary_search(self, times: list, target):
        left, right = 0, len(times)-1
        if target < times[left]:
            return -1
        while right>left:
            mid = -1*(-1*(right+left)//2)
            if times[mid] > target:
                right = mid-1
            else:
                left = mid
        return right


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hashmap:
            self.hashmap[key][0].append(timestamp)
            self.hashmap[key][1].append(value)
        else:
            self.hashmap[key] = [[timestamp], [value]]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ""
        idx = self.binary_search(self.hashmap[key][0], timestamp)
        return "" if idx == -1 else self.hashmap[key][1][idx]
    