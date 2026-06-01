#A HashMap stores data as:key → value
d = {
    "apple": 5,
    "banana": 3
}
#Access → O(1) average time.

#Two Sum 
def two_sum(nums, target):
    mp = {}
    for i,num in enumerate(nums):
        diff = target-num
        if diff in mp:
            return [mp[diff], i]
        mp[num]=i

#Frequency Count 
Count occurrences of elements.
arr = [1,2,2,3,1]
freq = {}
for x in arr:
    freq[x] = freq.get(x,0)+1
print(freq)
#output:{1: 2, 2: 2, 3: 1}
