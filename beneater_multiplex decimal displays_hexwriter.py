int_digits = [ 0x7e, 0x30, 0x6d, 0x79, 0x33, 0x5b, 0x5f, 0x70, 0x7f, 0x7b ]
digits = bytearray(int_digits)
hexout = bytearray()

for value in range(256):
    hexout = hexout + digits[int(value % 10)].to_bytes(1, byteorder='little', signed=False) #not sure if this should be true.

for value in range(256):
    hexout = hexout + digits[int((value / 10) % 10)].to_bytes(1, byteorder='little', signed=False)

for value in range(256):
    hexout = hexout + digits[int((value / 100) % 10)].to_bytes(1, byteorder='little', signed=False)

for value in range(256):
    hexout = hexout + b'\x00'


for value in range(-128, 128):
    hexout = hexout + digits[int(abs(value) % 10)].to_bytes(1, byteorder='little', signed=False)

for value in range(-128, 128):
    hexout = hexout + digits[int(abs(value / 10) % 10)].to_bytes(1, byteorder='little', signed=False)

for value in range(-128, 128):
    hexout = hexout + digits[int(abs(value / 100) % 10)].to_bytes(1, byteorder='little', signed=False)

for value in range(-128, 128):
    if value < 0:
        hexout = hexout + b'\x01'
    else:
        hexout = hexout + b'\x00'

with open('display_rom_hexout.hex', 'wb') as f:
    f.write(hexout)
    
