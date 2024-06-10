from os import mkdir
from libs.MC_Files import *
from libs.DF import *
from libs.MC_Objects import *
from libs.MC_Montage import *
from libs.Procedures import *
from libs.Minecraft import *
import libs.TextureGenerator.GenTexture as GT


"""

how does it work ??


* the build is divided into 3 parts

* 1: objects
* 2: data
* 3: file

* 1:
* building the object of the mod creating DF files (dependancies files)

* 2:
* building MF files (minecraft files) from DF files

* 3:
* building the real files from the MF files



"""



"""

How ??

the point of this program is to automatise creation of a lot of files that have custom content that have some sort of cross referencing

before creating the file in the directory, we create a abstract class of file called MF (minecraft file)

MF has some content, and some operations to modify it, these operations are called actions
it also has a Build function to create the real file

Since there is a build order to be taken into account, instead of have some unclear dependencies between files, there is a class called:
DF (dependency files)

DF contains a MF and some other DF that are the dependencies, so at build time we can build everything in the right order


since creating some minecraft moded objects requires a lot of files to be created, to avoid having redundant codes there is a class called:

MCOBJ (minecraft object)
MCOBJ is the parent of all minecraft generated objects, such as some blocks or tools

since creating a block isnt the same as creating a tool, some childrens class of MCOBJ are created:
MCOBJ_ITEM
    MCOBJ_TOOL
MCOBJ_BLOCK


and since we often not only need one tool, but a set of all the tools that can be made with one kind of ore for example,
there is another class for that wich is called:
Montage

Montages contains a list of item
Some children classes of Montage are created, and contains the some logic to generate multiple Objects that shares similarities
it can also contains files for some recipes for example






Syntax

DF(PATH) # gets the reference of a file, by default no files exist, it will create a reference
# if the same file is get it will get the previous reference


"""








# generate all the DF files in the python program
def Gen(**kwargs): 






    # generate the folder where to place the textures
    dirM("resources/assets/generand/textures/items/hello_i_wont_be_created.world")
    dirM("resources/assets/generand/textures/blocks/hello_i_wont_be_created.world")







    ####################################################################|
    #                                                                   |
    #                                                                   |
    # misc file needed to run the mod ( totaly mandatory ! )            |
    DF("resources/pack.mcmeta")                                         | "misc/pack_meta"
    DF("resources/META-INF/mods.toml")                                  | "misc/mod_toml"
    # DF("resources/META-INF/accesstransformer.cfg")                      | "misc/accesstransformer"
    #                                                                   |
    # main mod file                                                     |
    DF("java/generand/GenerandMod.java")                                | "java/mod"
    #                                                                   |
    # init files                                                        |
    DF("java/generand/init/GenerandModBlocks.java")                     | "java/init/block"
    DF("java/generand/init/GenerandModItems.java")                      | "java/init/item"
    DF("java/generand/init/GenerandModFeatures.java")                   | "java/init/feature"
    # DF("java/generand/init/GenerandModBiomes.java")                     | "java/init/biomes"
    #                                                                   |
    # lang file                                                         |
    DF("resources/assets/generand/lang/en_us.json")                     | "lang/en_us"
    #                                                                   |
    DF("resources/data/minecraft/tags/blocks/mineable/pickaxe.json")    | "resources/pickaxe"
    #                                                                   |
    #                                                                   |
    #                                                                   |
    # add new of custom tab                                             |
    DF("java/generand/init/GenerandModTabs.java")                       | "java/init/tab"
    DF("resources/assets/generand/lang/en_us.json") @ "newname" << T("lang/new_lang",{"type":"itemGroup","id":"tabgenerand","name":"Generand"})


    # DF("java/generand/world/features/treedecorators/BiomftyfiujhvFruitDecorator.java") | "decorators/fruit"
    # DF("java/generand/world/features/treedecorators/BiomftyfiujhvLeaveDecorator.java") | "decorators/leave"
    # DF("java/generand/world/features/treedecorators/BiomftyfiujhvTrunkDecorator.java") | "decorators/trunk"
    # DF("java/generand/world/biome/BiomftyfiujhvBiome.java") | "world/biome"



    # reference the procedures
    PROCEDURE("P_Explosion","procedures/explosion",rarity = 2)
    PROCEDURE("P_LightningBolt","procedures/lightning_bolt",rarity = 5)
    PROCEDURE("P_play_sound","procedures/play_sound",rarity = 10)
    PROCEDURE("P_set_time","procedures/set_time",rarity = 4)
    PROCEDURE("P_bonemeal","procedures/bonemeal",rarity = 6)
    PROCEDURE("P_xp","procedures/xp",rarity = 5)

    for i in MINECRAFT.potions:
        PROCEDURE("P_Potion_"+i,"procedures/potion",rarity = 5,
        potion_effect=i,
        time=str(int(RD_Exponent(1,100,1))),
        level=str(int(RD_Exponent(1,3,1))))

    # k=[]
    # for i in range(100000): k+=[PROCEDURE.Random().name]
    # print(k.count("Proc")/k.count("Proc2"))



    # if not "item_nb" in kwargs: kwargs["item_nb"] = 10 # create 10 items if no default value was given
    default = {
        "item_nb":10
    }

    # set defaults value if not given
    for key in default:
        if not key in kwargs : kwargs[key] = default[key]


    objs = []
    out = {
        "ore":0,
        "biome":0
    }

    for i in range(kwargs["item_nb"]):

        objs += M_Ore()().spawned_objs
        out["ore"] += 1
    
    for i in range(kwargs["biome_nb"]):

        objs += M_Ore()().spawned_objs
        out["biome"] += 1

    


    """
    Generating every objects in the objs list
    """
    for i in objs:
        i()


    # contruct all the MF files from DF files
    BuildWithDependancies()

    print("Generated:")
    for i in out:
        print(i+":","\t\t",out[i])

    
    return 0













def Build() -> int: # build MF file into real files
    for key,value in enumerate(MF_Registry):
        if not value in BuildIgnore:
            MF_Registry[value].Build()
    return 0

def main(**kwargs) -> int:
    if Gen(**kwargs) != 0 : return 1 # return error if any error
    if Build() != 0 : return 2 # return error if any error
    return 0