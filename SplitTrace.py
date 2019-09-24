import sys
import re
from time import time
time0 = time()
def make_breaking_up(line : str, temp_f):
	reg = r'^\d{2}\.\d{2}\.\d{4}\ \d{2}\:\d{2}\:\d{2}'
	result = re.match(reg, line)
	if result is not  None:
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