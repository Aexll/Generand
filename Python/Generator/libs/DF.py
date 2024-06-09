from typing import Type
from .Main import *
from .MC_Files import *

"""
Dependency File

manage the dependency of files

*  '+=' add action
*  '*=' add dependancy
*  '|=' set default template copy-from


*  Transfer             : data ------> reciver
*  Formating            : data -> F -> Fdata
*  Formated Transfer    : data -> F -> Reciver


*  Formatings:

*  Str  Formating       : str input , str pattern , str replacer
*  Dict Formating       : str input , dict dico (replace key as patter with value as replacer for each dico element)




"""

BuildIgnore = set()

Dependencies = {}

class DF:

    id = ""
    actions = None
    builded:bool = False
    pattern:str = None

    _DF_refs = dict()

    def __new__(cls:type,id:str):

        # if a DF with a id already instanciated,
        # find the already created DF and return him
        # this doesnt create useless object
        # Its a kind of singletone.
        if not id in cls._DF_refs:
            _newObj = super().__new__(cls)

            cls._DF_refs[id] = _newObj
            _newObj.actions = list()

        return cls._DF_refs[id]

    def __init__(self,id:str) -> None:
        # object independant init
        # will be redo every DF() init
        self.id = id
    
    # build into MF file
    def __call__(self):
        self.builded = True
        for i in self.actions:
            i()
    
    # add action
    def __iadd__(self,action):
        self.actions += [action]
        return self
    
    # add dependency
    def __mul__(self,id:str):
        if not self.id in Dependencies:
            Dependencies[self.id] = []
        Dependencies[self.id] += [id]
        return self

    # set data from template
    def __or__(self,template:str):
        GMF(self.id) | template
        return self
    
    # at pattern
    def __matmul__(self,pattern:str):
        self.pattern = pattern
        return self

    #* +action : replace self.pattern by text:str
    def __lshift__(self,text:str):
        
        if(not self.pattern is None):
            pat = str(self.pattern) 
            self+=lambda: GMF(self.id).FormatStr(pat,text)
            self.pattern = None
        return self
    
    #* +action : format self with dictionary
    def __le__(self,dico:dict):
        new_dico = dict(dico) # avoid copying the ref !
        self += lambda: GMF(self.id).FormatDict(new_dico)
        return self



    # make a "with as" statement possible
    def __enter__(self):
        return self
        pass

    def __exit__(self,*args):
        pass
    




    #   Self Str Format With Recieved Dict-Formated Data (SF_DFD)
    #*  input -> Dict-Format -> Formated input
    #*  Self -> Str-Format ( Str Pattern by Formated input )
    #   this has the advantage to not create useless temporary files
    def SF_DFD(self,sender:str,pattern:str,dico:dict):
        textf = strDF(GMF(sender).data,dico)
        self+=lambda:GMF(self.id).FormatStr(pattern,textf)
        self*=sender






# easy get DF function /!\ will crash if id dont existe yet ! , use GDFS instead !
def GDF(id:str) -> DF:
    return DF._DF_refs[id]

# GDF Secured
def GDFS(id:str) -> DF:
    if not id in DF._DF_refs:
        DF(id)
    return GDF(id)

#build every DF in the right oreder of dependancies
def BuildWithDependancies():
    for i in DF._DF_refs.values():
        i:DF
        if not i.builded:
            BuildRec(i.id)

#build dependancies recusively then build the id DF
def BuildRec(id:str):
    if id in Dependencies.keys():
        for i in Dependencies[id]:
            if not GDF(i).builded:
                BuildRec(i)
    GDF(id)()
    pass

# return formated text from template name
def T(template:str,dico:dict = None) -> str: 
    txt:str = ""
    with io.open(MI.Dir_Template + '/' + template + ".template",mode="r", encoding="utf-8") as f:
        txt = f.read()
    if not dico is None:
        return strDF(txt,dico)
    else:
        return txt