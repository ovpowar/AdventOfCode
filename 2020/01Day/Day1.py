import fileinput
import time
start_time = time.time()

input_data = list(fileinput.input())

def part1():
	for line in input_data:
		rest = 2020 - int(line)
		if rest in map(int,input_data):
			return(int(rest)*int(line))

def part2():
	minimum_val = min(input_data)
	for line in input_data:
		leftover = 2020 - int(line)
		if leftover < int(minimum_val):
			break
		else:
			for i in input_data:
				leftover_sides = leftover - int(i)
				if leftover_sides > 0:
					if leftover_sides in map(int, input_data):
						_mulitple = int(i)*int(line)
						return(_mulitple*leftover_sides)
				else:
					break

print(part1())
print(part2())

print("--- %s seconds ---" % (time.time() - start_time))
