
if 0:
  card_pub_key = 5764801
  door_pub_key = 17807724
else:
  card_pub_key = 13135480
  door_pub_key = 8821721

def find_loop_size(pub_key):
  subj = 7
  value = 1
  loop_size = 0
  while value != pub_key:
    value = (subj*value) % 20201227
    loop_size += 1

  return loop_size

card_loop_size = find_loop_size(card_pub_key)
print(card_loop_size)

door_loop_size = find_loop_size(door_pub_key)
print(door_loop_size)

def encrypt_key(key, loop_size):
  value = 1
  for k in range(loop_size):
    value = (key*value) % 20201227

  return value

print(encrypt_key(door_pub_key, card_loop_size))
print(encrypt_key(card_pub_key, door_loop_size))
