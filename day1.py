from mcpi.minecraft import Minecraft
mc=Minecraft.create()
t=0
while True:
    x,y,z=mc.player.getTilePos()
    mc.postToChat('X:'+str(x)+'Y:'+str(y)+'Z:'+str(z))
     


x,y,z=mc.player.getTilePos()
C
mc.setBlock(x,y+2,z,46)
mc.setBlock(x,y+3,z,46)
mc.setBlock(x,y+4,z,46)
mc.setBlock(x,y+5,z,46)
mc.setBlock(x,y+6,z,46)
mc.setBlock(x,y+7,z,46)
mc.setBlock(x,y+8,z,46)
mc.setBlock(x,y+9,z,46)
mc.setBlock(x,y+10,z,46)


x,y,z=mc.player.getTilePos()
mc.setBlock(x+1,y,z,57)
mc.setBlock(x-1,y,z,57)
mc.setBlock(x,y,z+1,57)
mc.setBlock(x,y,z-1,57)
mc.setBlock(x+1,y,z+1,57)
mc.setBlock(x-1,y,z+1,57)
mc.setBlock(x-1,y,z-1,57)
mc.setBlock(x+1,y,z-1,57)

mc.setBlock(x+1,y+2,z,57)
mc.setBlock(x-1,y+2,z,57)
mc.setBlock(x,y+2,z+1,57)
mc.setBlock(x,y+2,z-1,57)
mc.setBlock(x+1,y+2,z+1,57)
mc.setBlock(x-1,y+2,z+1,57)
mc.setBlock(x-1,y+2,z-1,57)
mc.setBlock(x+1,y+2,z-1,57)



x,y,z=mc.player.getTilePos()
mc.setBlocks(x+10,y,z+10,x-10,y,z-10,57)


import random
import time
x,y,z=mc.player.getTilePos()

while True:
    r=random.randrange(0,16)
    mc.setBlocks(x+5,y,z+5,x-5,y,z-5,35,r)
    time.sleep(0.5)                              
        
        








