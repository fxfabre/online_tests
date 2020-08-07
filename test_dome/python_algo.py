import numpy as np



def count_numbers(sorted_list, less_than):
    n = len(sorted_list)
    
    def find_smaller(l, r):
        if l >= r-1:
            return l
        middle = (l + r) // 2

        if sorted_list[middle] <= less_than:
            return find_smaller(middle, r)
        return find_smaller(l+1, middle)
        
    idx = find_smaller(0, n - 1)
    
    if sorted_list[idx] > less_than:
        while (idx >= 0) and (sorted_list[idx] > less_than):
            print('-')
            idx -= 1
        return idx + 1
    
    while (idx < n) and (sorted_list[idx] < less_than):
        print("+")
        idx += 1
    return idx


sorted_list = [1, 3,3,3,3, 5, 7]
sorted_list = list(range(1000))
sorted_list = [-5, 4, 12]
print(count_numbers(sorted_list, 4)) # should print 2










SIZE = 10000

class TrainComposition:
    """
    Create a structure to store int
    Can add / remove values from the left and right.
    A simple implementation is to use a list : .insert(0, val), .pop(0), .append(val), .pop()
    
    This one tries to be optimized : avoid multiple malloc / memcpy
    Uses a numpy array, to store values.
    create a new array if space is missing, no réalloc (possible in python ?)
    """
    
    def __init__(self):
        self.reset()
    
    def reset(self):
        self.arrays = [np.zeros(10000, dtype=np.int)]
        self.idx_l = 10000 // 2
        self.idx_r = self.idx_l -1
    
    def attach_wagon_from_left(self, wagonId):
        if self.idx_l > 0:
            self.idx_l -= 1
        else:
            self.arrays = [np.zeros(10000, dtype=np.int)] + self.arrays
            self.idx_l = 9999
   
        self.arrays[0][self.idx_l] = wagonId
    
    def attach_wagon_from_right(self, wagonId):
        self.idx_r += 1
        
        if self.idx_r >= 10000:
            self.arrays.append(np.zeros(10000, dtype=np.int))
            self.idx_r = 0
        self.arrays[-1][self.idx_r] = wagonId

    def detach_wagon_from_left(self):
        wid = self.arrays[0][self.idx_l]
        self.idx_l += 1
        if self.idx_l >= 10000:
            self.arrays = self.arrays[1:]
            self.idx_l = 0
        if (len(self.arrays) == 1) and (self.idx_l > self.idx_r):
            self.reset()
        return wid
    
    def detach_wagon_from_right(self):
        wid = self.arrays[-1][self.idx_r]
        self.idx_r -= 1
        
        if self.idx_r < 0:
            self.arrays = self.arrays[:-1]
            self.idx_r = 9999
        
        if (len(self.arrays) == 1) and (self.idx_l > self.idx_r):
            self.reset()
        return wid

    
if __name__ == "__main__":
    train = TrainComposition()
    train.attach_wagon_from_left(7)
    train.attach_wagon_from_left(13)
    print(train.detach_wagon_from_right()) # should print 7
    print(train.detach_wagon_from_left()) # should print 13



