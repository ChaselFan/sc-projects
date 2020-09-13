"""
File: boggle.py
Name: Chasel Fan
----------------------------------------
TODO:
"""
# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
r = []
ans_lst=[]

def main():
	"""
	TODO:
	"""
	print('please wait for ten second...')
	read_dictionary()
	row1 = input('1 row of letter: ')
	row1=row1.split()
	for ch in row1:
		if len(ch) > 1 or len(row1) < 4:
			print('illegal input')
			break
	row2 = input('2 row of letter: ')
	row2=row2.split()
	for ch in row2:
		if len(ch) > 1 or len(row2) < 4:
			print('illegal input')
			break
	row3 = input('3 row of letter: ')
	row3=row3.split()
	for ch in row3:
		if len(ch) > 1 or len(row3) < 4:
			print('illegal input')
			break
	row4 = input('4 row of letter: ')
	row4=row4.split()
	for ch in row4:
		if len(ch) > 1 or len(row4) < 4:
			print('illegal input')
			break
	lst=[row1,row2,row3,row4]
	for x in range(len(lst)):
		for y in range(len(lst)):
			find_boggle(x, y, lst,'', [(x, y)])


def find_boggle(x, y, lst,ans, used_index):
	if len(ans) >= 4:
		if ans in r:
			if ans not in ans_lst:
				ans_lst.append(ans)
				print(f'Find {ans}')
				ans_lst.append(ans)

	if has_prefix(ans):
		for i in range(-1, 2):
			for j in range(-1, 2):
				if 3 >= x + i >= 0 and 3 >= y + j >= 0:
					if (x+i, y+j) not in used_index:
						ans += lst[x+i][y+j]
						used_index.append((x+i, y+j))
						find_boggle(x+i, y+j,lst, ans,used_index)
						ans = ans[:len(ans)-1]
						used_index.pop()


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	with open(FILE, 'r')as f:
		for line in f:
			line = line.strip()
			r.append(line)

def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	global r
	for word in r:
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
