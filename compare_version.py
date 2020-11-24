def compare_version(version1, version2):
	if len(version1) == 0 and len(version2) > 0:
		return -1
	if len(version1) > 0 and len(version2) == 0:
		return 1

	part1 = version1.split('.')
	part2 = version2.split('.')

	#pad versions if necessary
	if len(part1) < len(part2):
		for i in range(0, len(part2) - len(part1)):
			part1.append("0")
	if len(part1) > len(part2):
		for i in range(0, len(part1) - len(part2)):
			part2.append("0")

	for i in range(len(part1)):
		if int(part1[i]) > int(part2[i]):
			return 1
		if int(part1[i]) < int(part2[i]):
			return -1

	return 0 


a = "1.2.0"
b = "1.2.1"

c = "99.99.99"
d = "99.99.99"

e = "6.4.5"
f = "6.4"

g = "001.01.1"
h = "01.01.01"

print(compare_version(a,b))
print(compare_version(c,d))
print(compare_version(e,f))
print(compare_version(g,h))