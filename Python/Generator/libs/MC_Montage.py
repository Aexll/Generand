from libs.Randomizer import *
from libs.MC_Objects import *

"""


* a "Montage" is a "rule" to create a set of "Objects"
*
* example: an ore with his drop and his recipe to smelt it and the tool he can make
*
*
*



"""

class Montage:

    spawned_objs:list = None

    def __init__(self,**kwargs):
        self.spawned_objs = list()
        pass

    def __call__(self, *args, **kwds):
        pass


class M_Ore(Montage):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __call__(self, *args, **kwds):
        super().__call__(*args, **kwds)

        # info only in montage
        unshard_info = {

            "name": RD_Name(),
            "rarity": RD_Exponent(0.5,10,0.5,clamp=True) # 1:common 4:rare
        }

        # common info to share with all objects
        info_new = {

            "color": RD_Color(),
            "intensity": random()*0.8+0.2,
            "dropAmount":str(int(RD_Exponent(1,4,0.2,clamp=False))),

            # tools infos 
            "tool_uses" :   str(int(    RD_Gausse(10,1000,0.2) * unshard_info["rarity"]/4)),
            "tool_level":   str(int(    RD_Exponent(1,unshard_info["rarity"],0.5,clamp=True))),
            "tool_speed":   str(int(    RD_Gausse(2,6+unshard_info["rarity"]*2))),
            "tool_damages": str(int(    RD_Exponent(1,unshard_info["rarity"],0.5,clamp=False) )),
            "tool_enchant": str(int(    RD_Exponent(1,unshard_info["rarity"],0.5,clamp=True) ))
        }

        name_raw    = "Raw "+unshard_info["name"]
        name_ore    = unshard_info["name"].capitalize()+" ore"
        name_ingot  = unshard_info["name"].capitalize()+" ingot"
        
        #tools
        name_t_pickaxe  = unshard_info["name"].capitalize() + " pickaxe"
        name_t_axe      = unshard_info["name"].capitalize() + " axe"
        name_t_shovel   = unshard_info["name"].capitalize() + " shovel"
        name_t_sword    = unshard_info["name"].capitalize() + " sword"
        name_t_hoe      = unshard_info["name"].capitalize() + " hoe"





        # objects

        i_raw = MCOBJ_ITEM( name = name_raw,img_pattern = "raw", **info_new   )
        i_block = MCOBJ_BLOCK(name = name_ore, dropID = name_raw.upper().replace(' ','_'), **info_new )
        i_ingot = MCOBJ_ITEM( name = name_ingot,img_pattern = "ingot", **info_new   )
        
        i_pickaxe   = MCOBJ_TOOL( name = name_t_pickaxe,repair_ingredient   = i_ingot.dico["ID"],img_pattern = "pickaxe",   **info_new   )
        i_axe       = MCOBJ_TOOL( name = name_t_axe,    repair_ingredient   = i_ingot.dico["ID"],img_pattern = "axe",       **info_new   )
        i_shovel    = MCOBJ_TOOL( name = name_t_shovel, repair_ingredient   = i_ingot.dico["ID"],img_pattern = "shovel",    **info_new   )
        i_sword     = MCOBJ_TOOL( name = name_t_sword,  repair_ingredient   = i_ingot.dico["ID"],img_pattern = "sword",     **info_new   )
        i_hoe       = MCOBJ_TOOL( name = name_t_hoe,    repair_ingredient   = i_ingot.dico["ID"],img_pattern = "hoe",       **info_new   )

        self.spawned_objs.append(i_raw)
        self.spawned_objs.append(i_block)
        self.spawned_objs.append(i_ingot)
        self.spawned_objs.append(i_pickaxe )
        self.spawned_objs.append(i_axe     )
        self.spawned_objs.append(i_shovel  )
        self.spawned_objs.append(i_sword   )
        self.spawned_objs.append(i_hoe     )

        
        

        # recipes

        # raw -> ingot
        DF("resources/data/generand/recipes/smelting_"+i_raw.dico["id"]+".json") | "recipes/raw_to_ore" <= {
            "ingredient":i_raw.dico["mc:id"],
            "result":i_ingot.dico["mc:id"],
            "smelt_xp":str(randint(0,10)),
            "smelt_time":str(RD_Gausse(1,200))
            }
        

        # ingot -> pickaxe
        DF("resources/data/generand/recipes/crafting_"+unshard_info["name"]+"_pickaxe.json") | "recipes/craft_pickaxe" <= {
            "ingredient":i_ingot.dico["mc:id"],
            "result":i_pickaxe.dico["mc:id"],
            "count":"1"
            }
        # ingot -> axe
        DF("resources/data/generand/recipes/crafting_"+unshard_info["name"]+"_axe.json") | "recipes/craft_axe" <= {
            "ingredient":i_ingot.dico["mc:id"],
            "result":i_axe.dico["mc:id"],
            "count":"1"
            }
        # ingot -> hoe
        DF("resources/data/generand/recipes/crafting_"+unshard_info["name"]+"_hoe.json") | "recipes/craft_hoe" <= {
            "ingredient":i_ingot.dico["mc:id"],
            "result":i_hoe.dico["mc:id"],
            "count":"1"
            }
        # ingot -> shovel
        DF("resources/data/generand/recipes/crafting_"+unshard_info["name"]+"_shovel.json") | "recipes/craft_shovel" <= {
            "ingredient":i_ingot.dico["mc:id"],
            "result":i_shovel.dico["mc:id"],
            "count":"1"
            }
        # ingot -> sword
        DF("resources/data/generand/recipes/crafting_"+unshard_info["name"]+"_sword.json") | "recipes/craft_sword" <= {
            "ingredient":i_ingot.dico["mc:id"],
            "result":i_sword.dico["mc:id"],
            "count":"1"
            }
    




        return self

class M_Biome(Montage):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __call__(self, *args, **kwds):
        super().__call__(*args, **kwds)

        return self