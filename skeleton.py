#import the Minecraft libraries

from mcpi import block

#Connector
= Minecraft.create()

#Find current position.
x,y,z = 


# Declaring and intitalizing the variables for the size of the structure
width =  #z
length = #x
height = #y

# Create the ceiling and the walls.


# Create the floor.





# Add a Door.


# Add Windows.


# Add a Roof.
for i in range(int(length/2) + 1):
    mc.setBlocks(x+i, y+height+i, z+3, x+i, y+height+i, z+3+width, block.STAIRS_WOOD.id, 0)
    mc.setBlocks(x+length-i, y+height+i, z+3, x+length-i, y+height+i, z+3+width, block.STAIRS_WOOD.id, 1)
    
    if (int(length/2) - i > 0):
        mc.setBlocks(x+1+i, y+height+i, z+3, x+length-i-1, y+height+i, z+3, block.BRICK_BLOCK.id, 0)
        mc.setBlocks(x+1+i, y+height+i, z+3+width, x+length-i-1, y+height+i, z+3+width, block.BRICK_BLOCK.id, 1)