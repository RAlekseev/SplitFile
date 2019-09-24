import sys
import re
from time import time


def make_breaking_up(line : str, temp_f):

	if type_check(line):
		br_up_item = line.split()[2][1:-1] if first == '--module' else line.split()[0] 
		if br_up_item in opened_f.keys():
			temp_f = opened_f[br_up_item]
			temp_f.write(line)
		else:
			temp_f = open( 'trace_' + br_up_item + '.log', 'w')
			opened_f[br_up_item] = temp_f
			temp_f.write(line)
	else:
		temp_f.write(line)
	return temp_f


def clear_opened_f(opened_f):
	for item in opened_f.keys():
		opened_f[item].close()

def type_check(line : str) -> bool:
	return line[0].isdigit() \
	and line[1].isdigit() \
	and line[2] == '.' \
	and line[3].isdigit() \
	and line[4].isdigit() \
	and line[5] == '.' \
	and line[6].isdigit() \
	and line[7].isdigit() \
	and line[8].isdigit() \
	and line[9].isdigit()
		

time0 = time()

if __name__ == "__main__":
	first = sys.argv[1] if len(sys.argv) > 1 else exit('bad args')
	second = sys.argv[2] if len(sys.argv) > 2 else 'trace.log'
	try:
		f = open(second, encoding = 'utf-8')
	except:
		pass
	
	temp_f = open('_Unknown_.log', 'w')
	opened_f = {'Unknown': temp_f}

	for line in f:
		temp_f =  make_breaking_up(line, temp_f)

	clear_opened_f(opened_f)
	f.close()
	
print(time() - time0)
