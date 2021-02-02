from mcpi.minecraft import Minecraft
mc=Minecraft.create()


x,y,z=mc.player.getTilePos()
mc.setBlocks(x,y,z,x+19,y+19,z+19,101)
mc.setBlocks(x+1,y+1,z+1,x+18,y+18,z+18,0)


import time
while True:
    x,y,z=mc.player.getTilePos)()
    mc.setBlocks)(x,y,z,38)
    time.sleep(0.5)