f = open('in.txt', 'r').readlines()

f = [list(x[:-1]) for x in f]

match = 0

for x in range(len(f)):
  for y in range(len(f[0])):
    if f[x][y] == 'X':
        
      if x < len(f) - 3 and y < len(f[0]) - 3 and (f[x+1][y+1] == 'M' and f[x+2][y+2] == 'A' and f[x+3][y+3] == 'S' ) :
        match += 1
      if 2 < x and 2 < y and (f[x-1][y-1] == 'M' and f[x-2][y-2] == 'A' and f[x-3][y-3] == 'S' ):
        match += 1  
      if x < len(f) - 3 and 2 < y and (f[x+1][y-1] == 'M' and f[x+2][y-2] == 'A' and f[x+3][y-3] == 'S' ) :
        match += 1
      if 2 < x and y < len(f[0]) - 3 and (f[x-1][y+1] == 'M' and f[x-2][y+2] == 'A' and f[x-3][y+3] == 'S' ):
        match += 1
      if y < len(f[0]) - 3 and (f[x][y+1] == 'M' and f[x][y+2] == 'A' and f[x][y+3] == 'S' ) :
        match += 1
      if 2 < x and (f[x-1][y] == 'M' and f[x-2][y] == 'A' and f[x-3][y] == 'S' )  :
        match += 1
      if x < len(f) - 3 and (f[x+1][y] == 'M' and f[x+2][y] == 'A' and f[x+3][y] == 'S' ):
        match += 1
      if 2 < y and (f[x][y-1] == 'M' and f[x][y-2] == 'A' and f[x][y-3] == 'S' ) :
        match += 1
print(match)
