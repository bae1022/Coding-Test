s = input()

s = s.replace('c=', '*')
s = s.replace('c-', '*')
s = s.replace('dz=', '*')
s = s.replace('d-', '*')
s = s.replace('lj', '*')
s = s.replace('nj', '*')
s = s.replace('s=', '*')
s = s.replace('z=', '*')

print(len(s))