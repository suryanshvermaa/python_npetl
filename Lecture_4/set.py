# set in python
# collection of unordered items
# Each element in set must be unique & immutable
nums={1,2,4,5,6,7,77,8,8,8,8,8,8}
print(nums)

# set methods
nums.add(4) # adds element 4
nums.remove(7) # remove the element 7
print(nums)
nums.pop() # removes random value
print(nums)
# nums.clear() # empty the set
# print(nums)
nums2={4,5,2,0,55}
print(nums.union(nums2)) # combines both set values and returns new
print(nums.intersection(nums2)) # combines common values and returns new
