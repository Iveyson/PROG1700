ch = "g"
base =ord('a')
step=3
offset=ord(ch)-base
new_offset=(offset + step) % 26
print(base)
print(offset)
print(new_offset)