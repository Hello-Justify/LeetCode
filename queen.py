'''
51.N皇后
@author   : hca
@date     : 2019-11-25 21:55
# 回溯算法
'''
def NQueen(n):
	def valid(curr_row, curr_col):
		for row, col in enumerate(cols):
			if col == curr_col or row + col == curr_row + curr_col or row - col == curr_row - curr_col:
				return False
		return True

	def update_output():
		segment = []
		for col in cols:
			s = ''
			for i in range(n):
				if i == col:
					s += 'Q'
				else:
					s += '.'
			segment.append(s)
		output.append(segment)

	def backtrack(curr_row = 0):
		for curr_col in range(n): 
			if valid(curr_row, curr_col):
				cols.append(curr_col)
				if curr_row == n - 1:
					update_output()
				else:
					backtrack(curr_row + 1)
				cols.pop()

	cols, output = [], []
	backtrack()
	return output

if __name__ == "__main__":
	n = 8
	print(len(NQueen(n)))
