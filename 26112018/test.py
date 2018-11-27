# binary=[1,1,1,0,0,0,1,0]
# for n,item in enumerate(binary):
#     if n%2 !=0:
#         binary[n],binary[n-1]=binary[n-1],binary[n]
# print (binary)

# a = list(map(lambda n:binary[n]=binary[n-1],enumerate(binary)))
# print (a)
def swap_bits(x):

    return (x & 0b10101010) >> 1 | (x & 0b01010101) << 1

print (bin(swap_bits(101010)))
# print(format(swap_bits(101010), "b"))