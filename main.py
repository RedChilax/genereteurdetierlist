import random
from PIL import Image , ImageDraw , ImageFont
import os

NB_USER = 53
OFFSET = 1

tierNb = random.randint(2,6)
colorlist = [(255,127,127) , (255,191,127), (255,223,127) , (255,255,127) , (191,255,127) , (127,255,237)]
tiersName = []

def random_line(fname, nbLines):
    lines = open(fname).read().splitlines()
    return random.sample(lines, nbLines)

dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

tiersName = random_line('liste_francais.txt', tierNb)

im = Image.new(mode = "RGB", size = (2000, 2000), color = (26, 26, 23))
fnt = ImageFont.truetype('fonts/arial.ttf', 30)
d = ImageDraw.Draw(im)

tiers = [[] for i in range(tierNb)]
for i in range(NB_USER):
    tierValue = random.randint(0 , tierNb-1)
    tiers[tierValue].append(i)

#print(tiers)

xpos1 = 0
ypos1 = 0
xpos2 = 225
ypos2 = 150


for tierIndex in range(tierNb):
    size = int(len(tiers[tierIndex])/12)
    #print(size)

    ypos2 += size * 150 

    d.rectangle((xpos1 , ypos1 , xpos2 , ypos2), fill=colorlist[tierIndex], outline='black' , width=2)
    d.text((20,ypos1+50), tiersName[tierIndex], font=fnt ,fill=(0,0,0))

    cpt = 0
    usrPosx=226
    usrPosy=ypos1
    for user in tiers[tierIndex]:

        usrImg = Image.open("users/"+str(user+1)+".png")
        usrImg = usrImg.resize((150,150), Image.ANTIALIAS)
        im.paste(usrImg , (usrPosx,usrPosy + OFFSET))        
        usrPosx+=150
        
        cpt += 1
        if(cpt % 11 == 0):
            usrPosy += 150
            usrPosx = 235
    
    
    ypos1 = ypos2
    ypos2 += 150
    

logoImg = Image.open("tiermaker-logo.png")
logoImg.putalpha(200)
logoImg = logoImg.resize((400,73), Image.ANTIALIAS)
im.paste(logoImg , (2000-400,0))

im.save("tierlist_generated.png")
im.show()