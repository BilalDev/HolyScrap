import sys
from PIL import Image

img = Image.open(sys.argv[1])
width, height = img.size

xblock = 5
yblock = 5

w_width = width / xblock
w_height = height / yblock

blockmap = [(xb*w_width, yb*w_height, (xb+1)*w_width, (yb+1)*w_height)
        for xb in xrange(xblock) for yb in xrange(yblock)]

newblockmap = list(blockmap)

newblockmap[0] = blockmap[14]
newblockmap[1] = blockmap[13]
newblockmap[2] = blockmap[12]
newblockmap[3] = blockmap[11]
newblockmap[4] = blockmap[10]
newblockmap[5] = blockmap[24]
newblockmap[6] = blockmap[23]
newblockmap[7] = blockmap[22]
newblockmap[8] = blockmap[21]
newblockmap[9] = blockmap[20]
newblockmap[10] = blockmap[4]
newblockmap[11] = blockmap[3]
newblockmap[12] = blockmap[2]
newblockmap[13] = blockmap[1]
newblockmap[14] = blockmap[0]
newblockmap[15] = blockmap[19]
newblockmap[16] = blockmap[18]
newblockmap[17] = blockmap[17]
newblockmap[18] = blockmap[16]
newblockmap[19] = blockmap[15]
newblockmap[20] = blockmap[9]
newblockmap[21] = blockmap[8]
newblockmap[22] = blockmap[7]
newblockmap[23] = blockmap[6]
newblockmap[24] = blockmap[5]

result = Image.new(img.mode, (width, height))
for box, sbox in zip(blockmap, newblockmap):
    c = img.crop(sbox)
    result.paste(c, box)
result.save(sys.argv[1])
