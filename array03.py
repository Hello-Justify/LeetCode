'''
217.存在重复元素
@author   : hca
@date     : 2019-11-17 21:59
@parameter: 
    {
    nums:待检查数组
    }
'''

def containsDuplicate(nums) -> bool:
    d = {}
    for num in nums:
        if num not in d:
            d[num] = 1
        else:
            return True
    return False


arr = [1,2,3,1]

print(containsDuplicate(arr))
