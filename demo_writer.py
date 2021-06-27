#haven't actually used this yet. too hard to figure out how to 
#program the RAM with a file in Digital...
addresses = [0b0000, 0b0001, 0b0010, 0b1000]

instructions = [ 0b00011000, # LDA from 0b1000
0b00110000, # OUT register A
0b11110000, # HLT
0b01010101 # data
]

from intelhex import IntelHex

hexout_upper = IntelHex()
hexout_lower = IntelHex()

for step in range(len(addresses)):
    hexout_upper[addresses[step]] = instructions[step] >> 4
    hexout_lower[addresses[step]] = instructions[step] & 0b1111
  
hexout_lower.tofile('demo_lower.hex', format='hex')
hexout_upper.tofile('demo_upper.hex', format='hex')