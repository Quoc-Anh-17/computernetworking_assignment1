header = bytearray(5)
# header[0] = (header[0] | 1 << 6) & 0xC0
# print(bin(int(str(header[0]), 10)))


# header[0] = (header[0] | 1 << 5)
# print(bin(int(str(header[0]), 10)))
a = 0b1001
print(a >> 1)