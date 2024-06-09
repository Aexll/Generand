from libs.DF import *
from random import randint

class PROCEDURE:
    Procedures_Registry = {}

    name:str = ""
    template:str = ""
    rarity:int = 1 # 1:rare -> 10:common 0:unregistered

    def __new__(cls:type,name:str,template:str="",**kwarg):

        # simple singelton optimisation system
        if not name in cls.Procedures_Registry:
            cls.Procedures_Registry[name] = super().__new__(cls) 
            DF("java/generand/procedures/"+name+".java") | template
            DF("java/generand/procedures/"+name+".java") @ "classname" << name
            DF("java/generand/procedures/"+name+".java") <= kwarg

        return cls.Procedures_Registry[name]

    def __init__(self,name:str,template:str,**kwargs) -> None:
        self.name = name
        self.template = template
        if "rarity" in kwargs: self.rarity = kwargs["rarity"]
        pass

    @classmethod
    def Random(self):
        _P_IP = {}
        _I = 0
        for i in PROCEDURE.Procedures_Registry.values():
            for j in range(i.rarity):
                _P_IP[_I] = i
                _I+=1
        return _P_IP[randint(0,len(_P_IP)-1)]