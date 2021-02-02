from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()

a=0
while a<5:
    mc.setBlocks(x+10,y-1,z,x-5,y-5,z,19)
    z=z+5
    a=a+1

x,y,z=mc.player.getTilePos()
a=int(input('想放甚麼方塊'))
mc.setBlock(x,y,z,a)


name=input('enter your name:')
message=input('enter your message:')
mc.postToChat('<'+ name +'>' + message)


x,y,z=mc.player.getTilePos()
mc.setSign(x,y,z,63,0,'hello','','','world')


while True:
    x,y,z=mc.player.getTilePos()
    
    a=mc.getBlockWithData(x,y-1,z)
    if a.data == 15:
        mc.postToChat('死路')
       
    if a.data == 11:
        mc.postToChat('右轉')
     
    if a.data == 14:
        mc.postToChat('小心')

while True:
    hits = mc.events.pollBlockHits()
     
    if len(hits) > 0:
        hit = hits[0]
        x,y,z = hit.pos.x,hit.pos.y,hit.pos.z
        block = mc.getBlock(x,y,z)
        mc.postToChat("Block ID:" + str(block))
        
        
        
while True:
    hits = mc.events.pollBlockHits()
     
    if len(hits) > 0:
        hit = hits[0]
        x,y,z = hit.pos.x,hit.pos.y,hit.pos.z
        block = mc.getBlock(x,y,z)
         
        if block == 1:
              mc.setBlock(x,y,z,41)    
        
x,y,z=mc.player.getTilePos()
mc.spawnEntity(x,y,z,93)       
    
        
        
        