data = [0b0100000000000100, 0b0001010000001000, 0, 0, 0, 0, 0, 0, # NOP - 0000
0b0100000000000100, 0b0001010000001000, 0b0100100000000000, 0b0001001000000000, 0, 0, 0, 0, # LDA - 0001
0b0100000000000100, 0b0001010000001000, 0b0100100000000000, 0b0001000000100000, 0b0000001010000000, 0, 0, 0, # ADD - 0010
0b0100000000000100, 0b0001010000001000, 0b0000000100010000, 0, 0, 0, 0, 0, # OUT - 0011
0,0,0,0,0,0,0,0, # - 0100
0,0,0,0,0,0,0,0, # - 0101
0,0,0,0,0,0,0,0, # - 0110
0,0,0,0,0,0,0,0, # - 0111
0,0,0,0,0,0,0,0, # - 1000
0,0,0,0,0,0,0,0, # - 1001
0,0,0,0,0,0,0,0, # - 1010
0,0,0,0,0,0,0,0, # - 1011
0,0,0,0,0,0,0,0, # - 1100
0,0,0,0,0,0,0,0, # - 1101
0,0,0,0,0,0,0,0, # - 1110
0b0100000000000100, 0b0001010000001000, 0b1000000000000000, 0, 0, 0, 0, 0] # HLT - 1111

from intelhex import IntelHex

hexout_upper = IntelHex()
hexout_lower = IntelHex()

for step in range(len(data)):
    hexout_upper[step] = (data[step] >> 8)
    hexout_lower[step] = (data[step] & 0xFF)

for step in range(1920):
    hexout_upper[len(data) + step] = 0x00
    hexout_lower[len(data) + step] = 0x00
    
hexout_lower.tofile('ucode_lower.hex', format='hex')
hexout_upper.tofile('ucode_upper.hex', format='hex')