# import sys
# sys.path is a list of absolute path strings
#sys.path.append('C:/Users/lavigne.axel/Desktop/opencv/build/python/cv2')

from math import fabs
from matplotlib.colors import rgb_to_hsv
import numpy as np
from random import randint, random
from PIL import Image
import cv2
import colorsys

# im1_name = "test2.png"
# im2_name = "pattern.png"


# ore_pattern32_img = np.array(Image.open('pattern32.png'))
# ore_patterns32 = []

# ore_pattern_img = np.array(Image.open('pattern.png'))
# ore_patterns = []

# ptrn32 = {

#     "nb":4,
#     "size":8

# }
# ptrn = {

#     "nb":4,
#     "size":4

# }


# for i in range(ptrn32["nb"]-1):
    # for j in range(ptrn32["nb"]-1):
        # x = i * ptrn32["size"]
        # y = j * ptrn32["size"]
        # ore_patterns32.append(ore_pattern32_img[x:x+ptrn32["size"],y:y+ptrn32["size"]])
# 
# for i in range(ptrn["nb"]-1):
    # for j in range(ptrn["nb"]-1):
        # x = i * ptrn["size"]
        # y = j * ptrn["size"]
        # ore_patterns.append(ore_pattern_img[x:x+ptrn["size"],y:y+ptrn["size"]])






# im1 = np.array(Image.open(im1_name))
# im2 = np.array(Image.open(im2_name))



# im2 = im2[0:4,0:4]



# im1 = Image.fromarray(im1)
# im2 = Image.fromarray(im2)


# # for i in range(5):
# #     imgg = Image.fromarray(ore_patterns[randint(0,len(ore_patterns)-1)])
# #     padding = 2
# #     im1.paste(imgg,(randint(padding,16-(ptrn["size"]-2)-padding),randint(padding,16-(ptrn["size"]-2)-padding)),imgg)

# imgg = Image.fromarray(ore_patterns[randint(0,len(ore_patterns)-1)])
# imgg32 = Image.fromarray(ore_patterns32[randint(0,len(ore_patterns32)-1)])
# imm = (imgg if bool(randint(0,1)) else imgg32)
# im1.paste(imm,(2,2),imm)

# imgg = Image.fromarray(ore_patterns[randint(0,len(ore_patterns)-1)])
# imgg32 = Image.fromarray(ore_patterns32[randint(0,len(ore_patterns32)-1)])
# imm = (imgg if randint(0,1) == 1 else imgg32)
# im1.paste(imm,(8,2),imm)

# imgg = Image.fromarray(ore_patterns[randint(0,len(ore_patterns)-1)])
# imgg32 = Image.fromarray(ore_patterns32[randint(0,len(ore_patterns32)-1)])
# imm = (imgg if randint(0,1) == 1 else imgg32)
# im1.paste(imm,(2,6),imm)

# imgg = Image.fromarray(ore_patterns[randint(0,len(ore_patterns)-1)])
# imgg32 = Image.fromarray(ore_patterns32[randint(0,len(ore_patterns32)-1)])
# imm = (imgg if randint(0,1) == 1 else imgg32)
# im1.paste(imm,(8,6),imm)

# imgg = Image.fromarray(ore_patterns[randint(0,len(ore_patterns)-1)])
# imgg32 = Image.fromarray(ore_patterns32[randint(0,len(ore_patterns32)-1)])
# imm = (imgg if randint(0,1) == 1 else imgg32)
# im1.paste(imm,(2,10),imm)

# imgg = Image.fromarray(ore_patterns[randint(0,len(ore_patterns)-1)])
# imgg32 = Image.fromarray(ore_patterns32[randint(0,len(ore_patterns32)-1)])
# imm = (imgg if randint(0,1) == 1 else imgg32)
# im1.paste(imm,(8,10),imm)



# im3 = im1

# im3.save("result.png", "PNG")





def MakePattern(imgsdir) -> Image.Image:


    ore_pattern32_img = np.array(Image.open(imgsdir+'/pattern32.png'))
    ore_patterns32 = []

    ore_pattern_img = np.array(Image.open(imgsdir+'/pattern.png'))
    ore_patterns = []

    ptrn32 = {

        "nb":4,
        "size":8

    }
    ptrn = {

        "nb":4,
        "size":4

    }

    for i in range(ptrn32["nb"]-1):
        for j in range(ptrn32["nb"]-1):
            x = i * ptrn32["size"]
            y = j * ptrn32["size"]
            ore_patterns32.append(ore_pattern32_img[x:x+ptrn32["size"],y:y+ptrn32["size"]])

    for i in range(ptrn["nb"]-1):
        for j in range(ptrn["nb"]-1):
            x = i * ptrn["size"]
            y = j * ptrn["size"]
            ore_patterns.append(ore_pattern_img[x:x+ptrn["size"],y:y+ptrn["size"]])


    im1 = Image.new('RGBA',(16,16),(0,0,0,0))

    imgg = Image.fromarray(ore_patterns[randint(0,len(ore_patterns)-1)])
    imgg32 = Image.fromarray(ore_patterns32[randint(0,len(ore_patterns32)-1)])
    imm = (imgg if bool(randint(0,1)) else imgg32)
    im1.paste(imm,(2,2),imm)

    imgg = Image.fromarray(ore_patterns[randint(0,len(ore_patterns)-1)])
    imgg32 = Image.fromarray(ore_patterns32[randint(0,len(ore_patterns32)-1)])
    imm = (imgg if randint(0,1) == 1 else imgg32)
    im1.paste(imm,(8,2),imm)

    imgg = Image.fromarray(ore_patterns[randint(0,len(ore_patterns)-1)])
    imgg32 = Image.fromarray(ore_patterns32[randint(0,len(ore_patterns32)-1)])
    imm = (imgg if randint(0,1) == 1 else imgg32)
    im1.paste(imm,(2,6),imm)

    imgg = Image.fromarray(ore_patterns[randint(0,len(ore_patterns)-1)])
    imgg32 = Image.fromarray(ore_patterns32[randint(0,len(ore_patterns32)-1)])
    imm = (imgg if randint(0,1) == 1 else imgg32)
    im1.paste(imm,(8,6),imm)

    imgg = Image.fromarray(ore_patterns[randint(0,len(ore_patterns)-1)])
    imgg32 = Image.fromarray(ore_patterns32[randint(0,len(ore_patterns32)-1)])
    imm = (imgg if randint(0,1) == 1 else imgg32)
    im1.paste(imm,(2,10),imm)

    imgg = Image.fromarray(ore_patterns[randint(0,len(ore_patterns)-1)])
    imgg32 = Image.fromarray(ore_patterns32[randint(0,len(ore_patterns32)-1)])
    imm = (imgg if randint(0,1) == 1 else imgg32)
    im1.paste(imm,(8,10),imm)

    return im1




def MakePattern(imgsdir:str,patternName:str,pattern_info:dict = dict()) -> Image.Image:


    pattern_img = np.array(Image.open(imgsdir+'/'+patternName+'.png'))
    pattern_cut = []

    if not "nb" in pattern_info:
        pattern_info = {

            "nb":4,
            "size":16,
            "rot": False,
            "range": (1,3)

        }

    for i in range(pattern_info["nb"]-1):
        for j in range(pattern_info["nb"]-1):
            x = i * pattern_info["size"]
            y = j * pattern_info["size"]
            pattern_cut.append(pattern_img[x:x+pattern_info["size"],y:y+pattern_info["size"]])

    
    result = Image.new('RGBA',(16,16),(0,0,0,0))

    poss = [(0,0),(1,1),(1,0),(0,1),(0.5,0.5),(0,1)]

    padding = 2
    for i in range(randint(pattern_info["range"][0],pattern_info["range"][1])):

        imgg = Image.fromarray(pattern_cut[randint(0,len(pattern_cut)-1)])

        
        if pattern_info["rot"]: imgg = imgg.rotate([0,90,180,270][randint(0,3)])
        padding = 0
        # box = (
        #     randint(padding,16-padding-pattern_info["size"]),
        #     randint(padding,16-padding-pattern_info["size"]),
        # )

        box = (
            int( pattern_info["size"]*poss[i][0] + randint(-1,1) ),
            int( pattern_info["size"]*poss[i][1] + randint(-1,1) )
        )

        result.paste(imgg,box,imgg)
        # randint(padding,16-(pattern_info["size"]-2)-padding),randint(padding,16-(pattern_info["size"]-2)-padding)


    return result







img_info = {
    
    "directory" : "imgs",
    "name"      : "ore_patterns",
    "tile_size" : 16,
    "tile_nb_h" : 4,
    "tile_nb_v" : 4
}


def Texture_TileBreaker(img_info:dict,*args) -> Image.Image:

    img_pattern = np.array(Image.open(img_info["directory"]+'/'+img_info["name"]+'.png'))

    tiles = []

    for i in range(img_info["tile_nb_h"]):
        for j in range(img_info["tile_nb_v"]):
            x = i * img_info["tile_size"]
            y = j * img_info["tile_size"]
            tiles.append(img_pattern[x:x+img_info["tile_size"],y:y+img_info["tile_size"]])
    
    img_return = Image.new('RGBA',(16,16),(0,0,0,0))

    tile_chosen = Image.fromarray(tiles[randint(0,len(tiles)-1)])

    img_return.paste(tile_chosen,(0,0),tile_chosen)

    return img_return




"""

kwargs:

* src : source folder where to find imgs
* color : color(s) to build with
* base : list of texture (str) needed to build on

"""
def GenOreTexture(**kwargs) -> Image.Image:

    if not "color" in kwargs : kwargs["color"] = hsv2rgb(random(),1,1)
    if not "intensity" in kwargs : kwargs["intensity"] = random()*10
    if not "shadowing" in kwargs : kwargs["shadowing"] = kwargs["intensity"]*(random()+1)


    img_fromTexture = Image.open("imgs/blocks/stone.png")

    img_info = {
    
        "directory" : "imgs",
        "name"      : "ore_patterns",
        "tile_size" : 16,
        "tile_nb_h" : 4,
        "tile_nb_v" : 4
    }
    img_patterned = Texture_TileBreaker(img_info)

    img_patterned = np.array(img_patterned)

    Colorize_Array(img_patterned,kwargs["color"],kwargs["intensity"],kwargs["shadowing"])
    
    img_patterned = Image.fromarray(img_patterned)

    img_fromTexture.paste(img_patterned,(0,0),img_patterned)

    return img_fromTexture










def GenRawTexture(**kwargs) -> Image.Image:

    if not "color" in kwargs : kwargs["color"] = hsv2rgb(random(),0.5,1)
    if not "intensity" in kwargs : kwargs["intensity"] = random()

    kwargs["color"] = hsv2rgb(rgb_to_hsv(kwargs["color"])[0],kwargs["intensity"],1)
    


    img_fromTexture = Image.new('RGBA',(16,16),(0,0,0,0))

    img_info = {
    
        "directory" : "imgs",
        "name"      : "raw_patterns",
        "tile_size" : 16,
        "tile_nb_h" : 3,
        "tile_nb_v" : 4
    }

    img_patterned = Texture_TileBreaker(img_info)

    img_patterned = np.array(img_patterned)

    Colorize_Array(img_patterned,kwargs["color"],1,1)
    
    img_patterned = Image.fromarray(img_patterned)

    img_fromTexture.paste(img_patterned,(0,0),img_patterned)

    return img_fromTexture

# if not "color" in kwargs : kwargs["color"] = hsv2rgb(random(),1,1)

# product = Image.new('RGBA',(16,16),(0,0,0,0))
# pat = MakePattern(kwargs["src"],"raw_pattern")
# # add the color
# pat = np.array(pat)
# Colorize_Array(pat,kwargs["color"],1,1)
# pat = Image.fromarray(pat)
# product.paste(pat,(0,0),pat)
# return product


def GenTextureFromPattern(pattern_info,**kwargs)-> Image.Image:

    if not "color" in kwargs : kwargs["color"] = hsv2rgb(random(),0.5,1)
    if not "intensity" in kwargs : kwargs["intensity"] = random()

    kwargs["color"] = hsv2rgb(rgb_to_hsv(kwargs["color"])[0],kwargs["intensity"],1)
    


    img_fromTexture = Image.new('RGBA',(16,16),(0,0,0,0))

    img_info = {
    
        "directory" : "imgs",
        "name"      : "raw_patterns",
        "tile_size" : 16,
        "tile_nb_h" : 1,
        "tile_nb_v" : 1
    }

    img_patterned = Texture_TileBreaker(pattern_info)

    img_patterned = np.array(img_patterned)

    Colorize_Array(img_patterned,kwargs["color"],1,1)
    
    img_patterned = Image.fromarray(img_patterned)

    img_fromTexture.paste(img_patterned,(0,0),img_patterned)

    return img_fromTexture











def sigmoid(x,l=5):
  
    z = np.exp(-1*(x-0.5)*l)
    sig = 1 / (1 + z)
    return sig


def hsv2rgb(h,s,v):
    return list(round(i * 255) for i in colorsys.hsv_to_rgb(h,s,v))


def Colorize_Array(array,color:tuple,alpha:float = 1,shadow:float = 1):

    color_array = np.array(color)

    for index_i,i in enumerate(array):
            for index_j,j in enumerate(i):
                r_scale = j[0]/255
                j_2 = np.append( r_scale*color_array, max(j[3]*shadow,1)/alpha)
                array[index_i][index_j] = j_2
    
    return array





















































# # read the target file
# image_ore = 'Ore.png'
# target_img = Image.open(image_ore) # cv2.imread(image_ore , cv2.IMREAD_UNCHANGED)

# target_img = np.array(target_img)

# print(target_img.shape)

# # create an image with a single color (here: red)
# red_img  = np.full((511,511,4), (0,0,255,0), np.uint8)

# # add the filter  with a weight factor of 20% to the target image
# fused_img  = cv2.addWeighted(target_img, 0.8, red_img, 0.2, 0)


# image_stone = 'Stone.jpg'
# img_stone = Image.open(image_stone)

# img_stone.paste(fused_img, (0, 0, 511, 511), fused_img)

# cv2.imwrite('blagaj_red_filter.png', img_stone)