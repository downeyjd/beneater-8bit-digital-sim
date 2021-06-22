digits = [ 0x7e, 0x30, 0x6d, 0x79, 0x33, 0x5b, 0x5f, 0x70, 0x7f, 0x7b ]

from intelhex import IntelHex

hexout = IntelHex()

for value in range(256):
    hexout[value] = digits[int(value % 10)].to_bytes(1, byteorder='little', signed=False) #not sure if this should be true.

for value in range(256):
    hexout[value + 256] = digits[int((value / 10) % 10)].to_bytes(1, byteorder='little', signed=False)

for value in range(256):
    hexout[value + 512] = digits[int((value / 100) % 10)].to_bytes(1, byteorder='little', signed=False)

for value in range(256):
    hexout[value + 768] = 0

for value in range(-128, 128):
    hexout[value + 1152] = digits[int(abs(value) % 10)].to_bytes(1, byteorder='little', signed=False)

for value in range(-128, 128):
    hexout[value + 1408] = digits[int(abs(value / 10) % 10)].to_bytes(1, byteorder='little', signed=False)

for value in range(-128, 128):
    hexout[value + 1664] = digits[int(abs(value / 100) % 10)].to_bytes(1, byteorder='little', signed=False)

for value in range(-128, 128):
    if value < 0:
        hexout[value + 1920] = 1
    else:
        hexout[value + 1920] = 0

hexout.tofile('display.hex', format='hex')
