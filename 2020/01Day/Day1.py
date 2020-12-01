import fileinput

lines = list(fileinput.input())

def part1():
	for line in lines:
		rest = 2020 - int(line)
		if rest in map(int,lines):
			return(int(rest)*int(line))

def part2():
	for line in lines:
		rest = 2020 - int(line)
		for i in lines:
			rest2 = rest - int(i)
			if rest2 in map(int, lines):
				_mulitple = int(i)*int(line)
				return(_mulitple*rest2)

print(part1())
print(part2())