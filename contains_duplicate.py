'''Given an integer array nums,
return true if any value appears more than once in the array,
otherwise return false.'''


nums=[1,2,3,4,1]

print(len(nums)!=len(set(nums)))
