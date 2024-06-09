import sys
from .Randomizer import *
from libs.DF import *
from libs.MC_Files import *
from libs.Patterns import patterns
from libs.Procedures import *
import libs.TextureGenerator.GenTexture as GT



def idFromName(name:str) -> dict:
    nd = dict()
    idn = name.lower().replace(' ','_')
    nd["id"] = idn
    nd["Id"] = ''.join([i.capitalize() for i in idn.split('_')])
    nd["ID"] = idn.upper()
    nd["mc:id"] = "generand:"+nd["id"]
    return nd




main_dico_default = {
    
    "type" : "null",
    "name" : RD_Name(),
    "color" : (255,0,0),
    "tab":"GenerandModTabs.TAB_GENERAND"
}

class MCOBJ:

    dico:dict = None

    def __init__(self,**dico) -> None:

        self.dico = dict()
        
        # set defaults value if not given
        for key in main_dico_default:
            if not key in dico : dico[key] = main_dico_default[key]
        
        # fixs
        dico["Type"] = dico["type"].capitalize()

        # Python 3.9 or higer required
        # assert sys.version_info[1]<9
        # self.dico |= dico
        # self.dico |= idFromName(self.dico["name"])

        self.dico = {**self.dico, **dico}
        self.dico = {**self.dico, **idFromName(self.dico["name"])}

        pass

    def __call__(self, *args,**kwds):
        # no rule to make empty object

        pass
    pass




class MCOBJ_ITEM(MCOBJ):

    def __init__(self, **dico) -> None:

        #class dependanties
        dico_default = {

            "type":"item",
            "stack":"64",
            "use_speed":str(int(RD_Gausse(0,60,sigma=1.5))),

            "img_pattern":"raw",
            "extend":"Item",
            "item_type":"item", # item, tool > this is template forlder name !
            "repair_ingredient": ""
            
        }
        # set defaults value if not given
        for key in dico_default:
            if not key in dico : dico[key] = dico_default[key]

        # init main class
        super().__init__(**dico)
    
    def __call__(self, *args, **kwds):
        super().__call__(*args, **kwds)

        
        DF("java/generand/init/GenerandModItems.java") @ "import" << T("import/import_class",self.dico) 
        DF("java/generand/init/GenerandModItems.java") @ "java_init_new_item" << T("java/init/new_item",self.dico)

        # add personal class file
        DF("java/generand/item/"+self.dico["Id"]+"Item.java") | "java/item/"
        DF("java/generand/item/"+self.dico["Id"]+"Item.java") @ "super" << T("java/item/super/"+self.dico["item_type"])
        DF("java/generand/item/"+self.dico["Id"]+"Item.java") @ "properties" << "new Item.Properties().tab(¤tab¤).stacksTo(¤stack¤).rarity(Rarity.COMMON)\n\t\t¤food¤"

        if self.dico["repair_ingredient"]=="":
            DF("java/generand/item/"+self.dico["Id"]+"Item.java") @ "repair_ingredient" << "Ingredient.EMPTY;"
        else:
            DF("java/generand/item/"+self.dico["Id"]+"Item.java") @ "repair_ingredient" << "Ingredient.of(¤>new_ingredient¤,¤<¤);"
            DF("java/generand/item/"+self.dico["Id"]+"Item.java") @ "new_ingredient" << "new ItemStack(GenerandModItems."+self.dico["repair_ingredient"]+".get())"
        
        DF("java/generand/item/"+self.dico["Id"]+"Item.java") <= self.dico

        # import PickaxeItem for example, but not Item cause its already imported
        if self.dico["extend"] != "Item" : 
            DF("java/generand/item/"+self.dico["Id"]+"Item.java") @ "import" << "import net.minecraft.world.item."+self.dico["extend"]+";\n"

        # food
        if(RD_Exponent(1,2)>3):
            final_food:str = T("java/item/food")
            final_food = strF(final_food,"args",".alwaysEat()")
            final_food = strF(final_food,"args",".meat()")
            final_food = strF(final_food,"args",".build()")
            DF("java/generand/item/"+self.dico["Id"]+"Item.java") @ "food" << final_food
            DF("java/generand/item/"+self.dico["Id"]+"Item.java") @ "import" << "import net.minecraft.world.food.FoodProperties;\n"

        
        # Create the event
        event_nb = randint(0,4)
        events_descr = [
            "droped",
            "hit enemy",
            "swing",
            "when in inventory",
            "crafted"
        ]
        event_template_name = "event/"+str(event_nb)
        final_event = T(event_template_name)
        DF("java/generand/item/"+self.dico["Id"]+"Item.java") @ "description" << T("java/item/description",{"text":"when " + events_descr[event_nb]})

        # Add procedure to call
        toadd_procedure = PROCEDURE.Random().name
        DF("java/generand/item/"+self.dico["Id"]+"Item.java") @ "description" <<  T("java/item/description",{"text":toadd_procedure})
        final_event = strF(final_event,"procedure",T("event/new_proc",{"procedure_class":toadd_procedure}))
        DF("java/generand/item/"+self.dico["Id"]+"Item.java") @ "import" << "import generand.procedures."+toadd_procedure+";\n"

        # toadd_procedure = "Proc2"
        # final_event = strF(final_event,"procedure",T("event/new_proc",{"procedure_class":toadd_procedure}))
        # DF("java/generand/item/"+self.dico["Id"]+"Item.java") @ "import" << "import generand.procedures."+toadd_procedure+";\n"

        # Add the final event to the item
        DF("java/generand/item/"+self.dico["Id"]+"Item.java") @ "procedures" << final_event        
        
        
        # add name to en_us
        DF("resources/assets/generand/lang/en_us.json") @ "newname" << T("lang/new_lang",self.dico)

        # add model file
        DF("resources/assets/generand/models/item/"+self.dico["id"]+".json") | "model/item" <= self.dico

        

        

        # create the texture
        GT.GenTextureFromPattern(patterns[self.dico["img_pattern"]],color=self.dico["color"]).save("main/resources/assets/generand/textures/items/"+self.dico["id"]+".png", "PNG")
        # GT.GenRawTexture()

        return


block_dico_default = {

    "dropID" : "WAITING_FOR_CHANGE",
}


class MCOBJ_BLOCK(MCOBJ):

    def __init__(self, **dico) -> None:
        dico["type"] = "block"

        # set defaults value if not given
        for key in block_dico_default:
            if not key in dico : dico[key] = block_dico_default[key]
        

        super().__init__(**dico)
    
    def __call__(self, *args, **kwds):
        super().__call__(*args, **kwds)

        
        # do block stuff
        

        # set in init item file
        DF("java/generand/init/GenerandModItems.java") @ "java_init_new_item_from_block" << T("java/init/new_item_from_block",self.dico)
        
        # set in block init file
        DF("java/generand/init/GenerandModBlocks.java") @ "java_init_new_block" << T("java/init/new_block",self.dico)
        DF("java/generand/init/GenerandModBlocks.java") @ "import" << T("import/import_class",self.dico)

        # add class file
        DF("java/generand/block/"+self.dico["Id"]+"Block.java") | "java/block/class" <= self.dico

        # add name to en_us
        DF("resources/assets/generand/lang/en_us.json") @ "newname" << T("lang/new_lang",self.dico)

        # add blockstate file
        DF("resources/assets/generand/blockstates/"+self.dico["id"]+".json") | "Blockstate"          <= self.dico

        # add model file
        DF("resources/assets/generand/models/block/"+self.dico["id"]+".json") | "model/block"         <= self.dico
        
        DF("resources/assets/generand/models/item/"+self.dico["id"]+".json") | "model/block_to_item" <= self.dico

        # add to mineable with pickaxe directory
        DF("resources/data/minecraft/tags/blocks/mineable/pickaxe.json") @ "resources_new_mineable" << T("resources/new_mineable",self.dico)

        # add world feature file
        DF("java/generand/world/features/ores/"+self.dico["Id"]+"Feature.java") | "world/ore_feature" <= self.dico
        DF("java/generand/init/GenerandModFeatures.java") @ "new_feature" << T("java/init/new_feature",self.dico)
        DF("java/generand/init/GenerandModFeatures.java") @ "import" << "import generand.world.features.ores."+self.dico["Id"]+"Feature;\n"
        
        # create the texture
        GT.GenOreTexture(src="imgs",color=self.dico["color"]).save("main/resources/assets/generand/textures/blocks/"+self.dico["id"]+"block.png", "PNG")

        return 

class MCOBJ_TOOL(MCOBJ_ITEM):

    def __init__(self, **dico) -> None:

        if "tool_type" in dico:
            tool_type = dico["tool_type"]

        # default PARENT-OVERIDE values
        dico_default = {
            
            "img_pattern":"Tools/pickaxe",
            "extend":"PickaxeItem",
            "item_type":"tool" # item, tool > this is template forlder name !
        }
        for key in dico_default:
            if not key in dico : dico[key] = dico_default[key]
        
        super().__init__(**dico)

    
    def __call__(self, *args, **kwds):
        super().__call__(*args, **kwds)

        return 