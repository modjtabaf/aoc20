
if 0:
  data = [3, 8, 9, 1, 2, 5, 4, 6, 7]
else:
  data = [2, 5, 3, 1, 4, 9, 8, 6, 7]

curr = data[0]
picked = [0]*3

for i in range(100):
  curr_ind = data.index(curr)

  for j in range(3):
    picked[j] = data[curr_ind+j+1 if curr_ind+j < 8 else curr_ind+j-8]

  for k in picked:
    data.remove(k)
  
  dest = curr - 1
  while dest in picked or dest == 0:
    if dest == 0:
      dest = 9
    else:
      dest -= 1

  dest_ind = data.index(dest)
  
  data = data[:dest_ind+1] + picked + data[dest_ind+1:]

  curr = data[0] if curr == data[-1] else data[data.index(curr) + 1]

print(data)
