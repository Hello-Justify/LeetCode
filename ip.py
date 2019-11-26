'''
93.复原IP地址
@author   : hca
@date     : 2019-11-25 21:55
# 回溯算法
'''
def restoreIpAdress(s):
	def valid(segment):
		return int(segment) < 256 if segment[0] != '0' else len(segment) == 1

	def update_output(curr_pos):
		segment = s[curr_pos + 1:]
		if valid(segment):
			segments.append(segment)
			output.append('.'.join(segments))
			segments.pop()

	def backtrack(prev_pos = -1, dots = 3):
		for curr_pos in range(prev_pos + 1, min(n - 1, prev_pos + 4)):
			segment = s[prev_pos + 1:curr_pos + 1]
			if valid(segment):
				segments.append(segment)
				if dots == 1:
					update_output(curr_pos)
				else:
					backtrack(curr_pos, dots - 1)
				segments.pop()

	n = len(s)
	segments, output = [], []
	backtrack()
	return output

if __name__ == "__main__":
	ip = "82937418"
	print(restoreIpAdress(ip))
