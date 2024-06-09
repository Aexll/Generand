from time import sleep
from libs.Main import *
from libs.ModInfo import *
from libs.Randomizer import *
from libs.Patterns import patterns 
from libs.TextureGenerator.GenTexture import *
import shutil
import sys

if __name__ == "__main__":

    # remove old main
    try:
        shutil.rmtree(MI.Dir_Gen)
    except:
        pass
    
    
    result = main(item_nb = 200,biome_nb = 1)

    if result == 0:
        print("Generation Completed Successfully !")
    else:
        if result == 1:
            print("Generation Failed Successfuly !!")
        if result == 2:
            print("Build Failed Successfuly !!")
    

    # print("rd : ",RD_Exponent(5,10,simga=0.5,clamp=True))
    # GenTextureFromPattern(patterns["ingot"]).save("result.png", "PNG")

    sleep(.1)
