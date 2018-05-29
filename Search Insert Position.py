#Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
def searchInsert(nums, target):
	left=0
	right=len(nums)-1
	while left <=right:
		mid=(right-left)/2+left
		if nums[mid]==target:
			return mid
		elif nums[mid]>target:
			right=mid-1
		else:
			left=mid+1
	return left
L=[1,3,5,6]
print(searchInsert(L,5))
print(searchInsert(L,2))
print(searchInsert(L,7))
print(searchInsert(L,0))