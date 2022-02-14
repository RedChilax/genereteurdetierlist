import random
from turtle import width
from PIL import Image , ImageDraw , ImageFont
tier_number = random.randint(2,6)
colorlist = [(255,127,127) , (255,191,127), (255,223,127) , (255,255,127) , (191,255,127) , (127,255,237)]
tier_name = []

def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)
xx= 0
while xx < tier_number:
    tier_name.append(random_line('liste_francais.txt'))
    xx += 1

im = Image.open("templat.png")
fnt = ImageFont.truetype('fonts/arial.ttf', 30)
d = ImageDraw.Draw(im)

users_tier = {}
i = 1
while i <= 53:
    users_tier[i] = random.randint(1 , tier_number)
    i+=1

tier_counter = {}
h = 1
while h <= tier_number:
    count = 0
    for key in users_tier:
        if(users_tier[key] == h):
            count+=1
    tier_counter[h] = count
    h+=1
print(tier_counter)
x = 0 
xpos1 = 0
ypos1 = 0
xpos2 = 225
ypos2 = 185
while(x < tier_number):
    size = int(tier_counter[x+1]/11)
    print(size)
    t = 0
    while t < size:
        ypos2 += 185
        t += 1
    d.rectangle((xpos1 , ypos1 , xpos2 , ypos2), fill=colorlist[x], outline='black' , width=2)
    d.text((20,ypos1+50), tier_name[x], font=fnt ,fill=(0,0,0))
    t = 0
    while t < size:
        ypos1 += 185
        t += 1
    ypos1 += 185
    ypos2 += 185
    x+=1

g = 1
newposy=20
while g <= tier_number:
    newposx=235
    compteur = 0
    for key in users_tier:
        if users_tier[key] == g:
            compteur +=1
            if(compteur % 11 == 0):
                newposy += 185
                newposx =235

            img2 = Image.open("users/"+str(key)+".png")
            img2 = img2.resize((150,150), Image.ANTIALIAS)
            im.paste(img2 , (newposx,newposy))
            
            
            newposx+=160
    newposy += 185
    g+=1

img3 = Image.open("tiermaker-logo.png")
img3.putalpha(200)
img3 = img3.resize((400,73), Image.ANTIALIAS)
im.paste(img3 , (2000-400,0))

im.save("tierlist_generated.png")

