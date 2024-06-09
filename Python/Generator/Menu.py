from re import T
from subprocess import call
from random import randint
from libs.Randomizer import RD_Gausse
from libs.Randomizer import RD_Exponent
import dearpygui.dearpygui as dpg

dpg.create_context()

"""


7: B
8: A
9: C
10: C
11: A
12: B
13: C
14: A
15: B
16: A
17: A
18: B
19: C
20: A
21: C
22: B
23: A
24: C
25: C
26: B
27: A
28: A
29: C or B
30: B
31: C


TODO: lol


65-67

C
A
C

















"""

# callback runs when user attempts to connect attributes
def link_callback(sender, app_data):
    # app_data -> (link_id1, link_id2)
    print(sender)
    dpg.add_node_link(app_data[0], app_data[1], parent=sender)

# callback runs when user attempts to disconnect attributes
def delink_callback(sender, app_data):
    # app_data -> link_id
    dpg.delete_item(app_data)

def hello_callback(sender):
    print("Hello World")

def add_node_callback(sender, app_data, user_data):

    print(user_data)
    
    random_id = randint(0, 50000)
    while dpg.does_item_exist(str(random_id) + "!Node_Addition"):
        random_id = randint(0, 50000)

    with dpg.node(tag=str(random_id) + "_Node_InputFloat", parent="NodeEditor", label="New", pos=(100,100)):
        with dpg.node_attribute(tag=str(random_id) + "_Node_InputFloat_Output", attribute_type=dpg.mvNode_Attr_Output):
            dpg.add_text("Generate a set", bullet=False)
        with dpg.node_attribute(tag=str(random_id) + "_Node_InputFloat_Static_1", attribute_type=dpg.mvNode_Attr_Static):
            dpg.add_combo(label="Type", width=200, items=["Ore","Biome","Dimention"], default_value="Ore", no_arrow_button = True, )
        with dpg.node_attribute(tag=str(random_id) + "_Node_InputFloat_Static_2", attribute_type=dpg.mvNode_Attr_Static):
            dpg.add_input_int(label="nb", width=200)
        with dpg.node_attribute(tag=str(random_id) + "_Node_InputFloat_Input", attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
            dpg.add_input_text(label="Data", width=200, hint="data")

def add_node_range(sender, app_data, user_data):

    print(user_data)
    
    random_id = randint(0, 50000)
    while dpg.does_item_exist(str(random_id) + "!Node_Addition"):
        random_id = randint(0, 50000)

    with dpg.node(tag=str(random_id) + "_Node_InputFloat", parent="NodeEditor", label="New", pos=(100,100)):
        with dpg.node_attribute(tag=str(random_id) + "_Node_InputFloat_Output", attribute_type=dpg.mvNode_Attr_Output):
            dpg.add_text("Random", bullet=False)
            # dpg.add_clipper()
        with dpg.node_attribute(tag=str(random_id) + "_Node_InputFloat_Static_2", attribute_type=dpg.mvNode_Attr_Static):
            v = [ RD_Exponent(0,1) for i in range(1000) ]
            v.sort()
            dpg.add_simple_plot(width=100,height=100, default_value = v )
            dpg.add_input_int(label="nb", width=200)
        with dpg.node_attribute(tag=str(random_id) + "_Node_InputFloat_Input", attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
            dpg.add_input_text(label="Data", width=200, hint="data")




# add a font registry

with dpg.font_registry():
    # first argument ids the path to the .ttf or .otf file
    default_font = dpg.add_font("libs/font.ttf", 20)
    second_font = dpg.add_font("libs/font.ttf", 10)


def Quit(sender):
    dpg.destroy_context()

with dpg.viewport_menu_bar():
    with dpg.menu(label="Quit"):
        dpg.add_menu_item(label="Quit",callback=Quit)





with dpg.window(label="Generand", height=800, width=1600, pos=(50,50)):
    
   # set font of specific widget
    dpg.bind_font(default_font)


    with dpg.node_editor(tag="NodeEditor",callback=link_callback, delink_callback=delink_callback, menubar=True) as win__:


        with dpg.menu_bar():
            with dpg.menu(label="Add"):
                dpg.add_menu_item(label="New set",callback=add_node_callback, user_data="new_node")
                dpg.add_menu_item(label="New data",callback=add_node_callback, user_data="new_node")
                dpg.add_menu_item(label="New range",callback=add_node_range, user_data="new_node")

        # with dpg.node(label="Generate",pos=(10,10)):
        #     with dpg.node_attribute(label="Node A1",attribute_type=dpg.mvNode_Attr_Output, shape = dpg.mvNode_PinShape_TriangleFilled, ) as run:
        #         dpg.add_button(label="Run",width=150)
        

        with dpg.node(label="Generate",pos=(1000,10)):
            with dpg.node_attribute(label="Node A3",attribute_type=dpg.mvNode_Attr_Input, shape = dpg.mvNode_PinShape_TriangleFilled) as out:
                dpg.add_combo(label="Folder", width=200, items=["main","test","secondary"], default_value="main", no_arrow_button = True, )
            with dpg.node_attribute(label="Node A3",attribute_type=dpg.mvNode_Attr_Static, shape = dpg.mvNode_PinShape_TriangleFilled) as out:
                dpg.add_button(label="Generate",width=150)

        
        
        # link_callback(win__, [run,out])
        


        with dpg.node(label="Menu",pos=(10,200)):
            with dpg.node_attribute(label="Node A1",attribute_type=dpg.mvNode_Attr_Static, shape = dpg.mvNode_PinShape_TriangleFilled, ):
                dpg.add_combo(label="Folder", width=200)
                dpg.add_button(label="Play",width=150)

        # with dpg.node(label="Ore",pos=(500,10)):
        #     with dpg.node_attribute(label="in",attribute_type=dpg.mvNode_Attr_Output, shape = dpg.mvNode_PinShape_TriangleFilled):
        #         dpg.add_combo(label=">", width=200)
        #     with dpg.node_attribute(label="out",attribute_type=dpg.mvNode_Attr_Input, shape = dpg.mvNode_PinShape_TriangleFilled):
        #         dpg.add_combo(label="<", width=200)

            # with dpg.node_attribute(label="Node A2",attribute_type=dpg.mvNode_Attr_Input, shape = dpg.mvNode_PinShape_CircleFilled):
            #     dpg.mvNodeCol_TitleBar = (255,2,2)
            #     dpg.mvNodeCol_Pin = (12,22,333)
            #     dpg.add_input_int(label="Seed", width=200)
            
            # with dpg.node_attribute(label="Node A2"):
            #     dpg.add_input_float(label="F2", width=150)




# dpg.show_font_manager()

dpg.create_viewport(title='Custom Title', width=800, height=600 )
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.toggle_viewport_fullscreen()
dpg.start_dearpygui()
dpg.destroy_context()
