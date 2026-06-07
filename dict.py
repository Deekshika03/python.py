#Create Dictionary
d = {
    "name": "John",
    "age": 21
}

print(d)

#Access Values
print(d["name"])

#Using get():
print(d.get("age"))

#Add / Update
d["city"] = "Delhi"   
d["age"] = 22        

#Count Frequency 
s = "banana"
freq = {}
for ch in s:
    freq[ch] = freq.get(ch,0)+1
print(freq)

***********************************************************************
#majority element  
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
            if count[num] > len(nums) // 2:
                return num
