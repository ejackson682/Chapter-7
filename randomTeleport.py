import random
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
count = 1
while count <= 1:
    x = random.randint(-127, 127)
    y = random.randint(0, 64)
    z = random.randint(-127, 127)
mc.player.setTilePos(x + 1, y +1, z + 1)
