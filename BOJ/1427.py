lst = list(map(int, str(input())))
lst.sort(reverse=True)
print(''.join(map(str, lst)))