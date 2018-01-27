
firePoints_names = ["infernal", "blaze", "flame", "ember", ""]
waterPoints_names = ["glacial", "blizzard", "ice", "hail", ""]
earthPoints_names = ["canyon", "chasm", "trench", "cracks", ""]
airPoints_names = ["mountain", "fortress", "wall", "mound", ""]
darkPoints_names = ["consuming", "draining", "leeching", "shrinking", ""]
lightPoints_names = ["exploding", "erupting", "blasting", "bursting", ""]
totalPoints = 60
usePoints = 60
name = input("Hello mage, what is your name?")
print ("Welcome to the spell generator", name, ", in this you are alloted a\nmaximum of 60 points to put into 6 base elements\nfire, water, earth, air, dark, light\nbut each element is only allowed a maximum of 16 points")

fire = input("How many points would you like to allot to the fire element?")

while (int(fire) < 0) or (int(fire) > 16):
    print ("Please reenter your points and remember that an input above 16 is not allowed")
    fire = input("How many points would you like to allot to the fire element?")
else:
    usePoints = usePoints - int(fire)
    while usePoints < 0:
        print ("Please reenter your points because you exceeded the total alottable points")
        usePoints = usePoints + int(fire)
        print (usePoints, "unallocated points")
        fire = input("How many points would you like to allot to the fire element?")
        usePoints = usePoints - int(fire)
        
print (usePoints, "unallocated points")

if (int(fire) == 9) or (int(fire) == 10):
    firePoints_names = firePoints_names[3]
elif (int(fire) == 11) or (int(fire) == 12):
    firePoints_names = firePoints_names[2]
elif (int(fire) == 13) or (int(fire) == 14):
    firePoints_names = firePoints_names[1]
elif (int(fire) == 15) or (int(fire) == 16):
    firePoints_names = firePoints_names[0]
elif int(fire) < 9:
    firePoints_names = firePoints_names[4]
    
water = input("How many points would you like to allot to the water element?")

while (int(water) < 0) or (int(water) > 16):
    print ("Please reenter your points and remember that an input above 16 is not allowed")
    water = input("How many points would you like to allot to the water element?")
else:
    usePoints = usePoints - int(water)
    while usePoints < 0:
        print ("Please reenter your points because you exceeded the total alottable points")
        usePoints = usePoints + int(water)
        print (usePoints, "unallocated points")
        water = input("How many points would you like to allot to the water element?")
        usePoints = usePoints - int(water)
        
print (usePoints, "unallocated points")

if (int(water) == 9) or (int(water) == 10):
    waterPoints_names = waterPoints_names[3]
elif (int(water) == 11) or (int(water) == 12):
    waterPoints_names = waterPoints_names[2]
elif (int(water) == 13) or (int(water) == 14):
    waterPoints_names = waterPoints_names[1]
elif (int(water) == 15) or (int(water) == 16):
    waterPoints_names = waterPoints_names[0]
elif int(water) < 9:
    waterPoints_names = waterPoints_names[4]
    
earth = input("How many points would you like to allot to the earth element?")

while (int(earth) < 0) or (int(earth) > 16):
    print ("Please reenter your points and remember that an input above 16 is not allowed")
    earth = input("How many points would you like to allot to the earth element?")
else:
    usePoints = usePoints - int(earth)
    while usePoints < 0:
        print ("Please reenter your points because you exceeded the total alottable points")
        usePoints = usePoints + int(earth)
        print (usePoints, "unallocated points")
        earth = input("How many points would you like to allot to the earth element?")
        usePoints = usePoints - int(earth)
        
print (usePoints, "unallocated points")

if (int(earth) == 9) or (int(earth) == 10):
    earthPoints_names = earthPoints_names[3]
elif (int(earth) == 11) or (int(earth) == 12):
    earthPoints_names = earthPoints_names[2]
elif (int(earth) == 13) or (int(earth) == 14):
    earthPoints_names = earthPoints_names[1]
elif (int(earth) == 15) or (int(earth) == 16):
    earthPoints_names = earthPoints_names[0]
elif int(earth) < 9:
    earthPoints_names = earthPoints_names[4]
    
air = input("How many points would you like to allot to the air element?")

while (int(air) < 0) or (int(air) > 16):
    print ("Please reenter your points and remember that an input above 16 is not allowed")
    air = input("How many points would you like to allot to the air element?")
else:
    usePoints = usePoints - int(air)
    while usePoints < 0:
        print ("Please reenter your points because you exceeded the total alottable points")
        usePoints = usePoints + int(air)
        print (usePoints, "unallocated points")
        air = input("How many points would you like to allot to the air element?")
        usePoints = usePoints - int(air)
        
print (usePoints, "unallocated points")

if (int(air) == 9) or (int(air) == 10):
    airPoints_names = airPoints_names[3]
elif (int(air) == 11) or (int(air) == 12):
    airPoints_names = airPoints_names[2]
elif (int(air) == 13) or (int(air) == 14):
    airPoints_names = airPoints_names[1]
elif (int(air) == 15) or (int(air) == 16):
    airPoints_names = airPoints_names[0]
elif int(air) < 9:
    airPoints_names = airPoints_names[4]
    
dark = input("How many points would you like to allot to the dark element?")

while (int(dark) < 0) or (int(dark) > 16):
    print ("Please reenter your points and remember that an input above 16 is not allowed")
    dark = input("How many points would you like to allot to the dark element?")
else:
    usePoints = usePoints - int(dark)
    while usePoints < 0:
        print ("Please reenter your points because you exceeded the total alottable points")
        usePoints = usePoints + int(dark)
        print (usePoints, "unallocated points")
        dark = input("How many points would you like to allot to the dark element?")
        usePoints = usePoints - int(dark)
        
print (usePoints, "unallocated points")

if (int(dark) == 9) or (int(dark) == 10):
    darkPoints_names = darkPoints_names[3]
elif (int(dark) == 11) or (int(dark) == 12):
    darkPoints_names = darkPoints_names[2]
elif (int(dark) == 13) or (int(dark) == 14):
    darkPoints_names = darkPoints_names[1]
elif (int(dark) == 15) or (int(dark) == 16):
    darkPoints_names = darkPoints_names[0]
elif int(dark) < 9:
    darkPoints_names = darkPoints_names[4]
    
light = input("How many points would you like to allot to the light element?")

while (int(light) < 0) or (int(light) > 16):
    print ("Please reenter your points and remember that an input above 16 is not allowed")
    light = input("How many points would you like to allot to the light element?")
else:
    usePoints = usePoints - int(light)
    while usePoints < 0:
        print ("Please reenter your points because you exceeded the total alottable points")
        usePoints = usePoints + int(light)
        print (usePoints, "unallocated points")
        light = input("How many points would you like to allot to the light element?")
        usePoints = usePoints - int(light)
        
print (usePoints, "unallocated points")

if (int(light) == 9) or (int(light) == 10):
    lightPoints_names = lightPoints_names[3]
elif (int(light) == 11) or (int(light) == 12):
    lightPoints_names = lightPoints_names[2]
elif (int(light) == 13) or (int(light) == 14):
    lightPoints_names = lightPoints_names[1]
elif (int(light) == 15) or (int(light) == 16):
    lightPoints_names = lightPoints_names[0]
else :
    lightPoints_names = lightPoints_names[4]
    
print (darkPoints_names, lightPoints_names, firePoints_names, waterPoints_names, earthPoints_names, airPoints_names)
magicElement = [fire, water, earth, air, light, dark]
if (int(water) == 16) and (int(air) == 16):
    print ("You have unlocked the magic element 'Ice'.\nIce can only be accessed when your water and air base elements are 16.")
if (int(water) == 16) and (int(earth) == 16):
    print ("You have unlocked the magic element 'Mud'.\nMud can only be accessed when your water and earth base elements are 16.")
if (int(water) == 16) and (int(light) == 16):
    print ("You have unlocked the magic element 'Crystal'.\nCrystal can only be accessed when your water and light base elements are 16.")
if (int(water) == 16) and (int(dark) == 16):
    print ("You have unlocked the magic element 'Poison'.\nPoison can only be accessed when your water and dark base elements are 16.")
if (int(fire) == 16) and (int(light) == 16):
    print ("You have unlocked the magic element 'Electricity'.\nElectricity can only be accessed when your fire and light base elements are 16.")
if (int(fire) == 16) and (int(earth) == 16):
    print ("You have unlocked the magic element 'Magma'.\nMagma can only be accessed when your fire and earth base elements are 16.")
if (int(fire) == 16) and (int(dark) == 16):
    print ("You have unlocked the magic element 'Fear'.\nFear can only be accessed when your fire and dark base elements are 16.")
if (int(fire) == 16) and (int(air) == 16):
    print ("You have unlocked the magic element 'Heat'.\nHeat can only be accessed when your fire and air base elements are 16.")

ready = input("Are you ready to start your adventure y/n?")
def adventure():
    print ("You walk out of the master mages house and are briefly blinded by the warm suns light.")
    direction = input("As your vision returns you see that you are standing\nat the edge a road running left to right which way would you like to go?")
    if (direction == "left") or (direction == "Left") or (direction == "L") or (direction == "l"):
        print ("As you continue down the road you eventually run across a pair of bandits \n do you wish to help the woman or look the other way")
    else :
        print ("As you continue down the road you eventually run across a camp of Orcs ")
if ready == "y":
    print ("Alright be on your way then.")
    adventure()
    
    
    
    



