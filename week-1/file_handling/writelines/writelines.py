

f = open('week-1/file_handling/writelines/writelines.txt', 'w')
lines = ['1\n', 'two\n', '3\n', 'four\n', '5\n']
f.writelines(lines)
f.close()