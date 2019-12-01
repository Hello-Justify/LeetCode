'''
46.全排列
@author   : hca
@date     : 2019-11-25 21:55
# 回溯算法
'''

def permute(nums):
    def update_output(seg):
        segments = []
        for i in seg:
            segments.append(i)
        output.append(segments)

    def backtrack(n = 1):
        for num in nums:
            if num not in segment:
                segment.append(num)
                if n == len(nums):
                    update_output(segment)
                else:
                    backtrack(n+1)
                segment.pop()

    segment, output = [], []
    backtrack()
    return output

if __name__ == "__main__":
    nums = [1, 2, 3]
    print(permute(nums))
