f = open('in.txt', 'r').readlines()

f = [list(x[:-1]) for x in f]

mas = 0

for x in range(1, len(f)-1):
  for y in range(1, len(f[0])-1):
    if f[x][y] == 'A':
      
      if f[x-1][y-1] + f[x+1][y+1] + f[x-1][y+1] + f[x+1][y-1] in ['MSMS', 'SMSM', 'MSSM', 'SMMS']:
        mas += 1

print(mas)