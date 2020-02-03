'''
26.从排序数组中删除重复项
@author   : hca
@date     : 2019-11-17 9:05
@parameter: 
    {
    nums:待删除重复项的已排序数组
    }
'''

def removeDuplicates(nums) -> int:
    n = 0
    for num in nums:
    	if num != nums[n]:
    		n += 1
    		nums[n] = num
    return n+1

def test(arr):
    print("原数组为：", arr)
    l = removeDuplicates(arr)
    print("新数组为：", arr[:l])
    print("新数组长度为%d"%l)

if __name__ == "__main__":
    arr1 = [1,1,2]
    arr2 = [0,0,1,1,1,2,2,3,3,4]
    arr3 = [2,2,2,3,4,4]
    test(arr1)
    test(arr2)
    test(arr3)