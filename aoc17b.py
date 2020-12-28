
import numpy as np

if 0:
  init_state = np.array([
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 1]])
else:
  init_state = np.array([
    [1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [1, 1, 1, 1, 1, 0, 1, 1],
    [1, 0, 0, 0, 0, 1, 1, 1],
    [1, 1, 0, 0, 1, 1, 0, 0],
    [1, 0, 0, 1, 1, 1, 1, 0],
    [1, 0, 0, 0, 1, 0, 1, 0]])

ncycles = 6

shape = (init_state.shape[0] + 2*ncycles, init_state.shape[1] + 2*ncycles, 1 + 2*ncycles, 1 + 2*ncycles)

active_mask = np.zeros(shape, dtype=int)
active_mask[ncycles:ncycles+init_state.shape[0], ncycles:ncycles+init_state.shape[1], ncycles, ncycles] = init_state

buffer = np.empty_like(active_mask)

ls = slice(1, None)
cs = slice(0, None)
rs = slice(0, -1)
slices = [ls, cs, rs]

for cyc in range(ncycles):
  buffer = -active_mask

  for l in [0, 1, 2]:
    sl1 = slices[l]
    sl2 = slices[2-l]
    for k in [0, 1, 2]:
      sk1 = slices[k]
      sk2 = slices[2-k]
      for j in [0, 1, 2]:
        sj1 = slices[j]
        sj2 = slices[2-j]
        for i in [0, 1, 2]:
          si1 = slices[i]
          si2 = slices[2-i]
          buffer[si1, sj1, sk1, sl1] += active_mask[si2, sj2, sk2, sl2]

  mask1 = np.logical_and(active_mask, np.logical_or(buffer == 2, buffer == 3))
  mask2 = np.logical_and(active_mask == 0, buffer == 3)
  active_mask.fill(0)
  active_mask[np.logical_or(mask1, mask2)] = 1

print(active_mask.sum())
