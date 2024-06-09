from pkg_resources import parse_requirements
from .ModInfo import *
import io
import os
import re

def vim(path:str) -> io.FileIO:
        """
        create the file at a certain location in the src directory
        will overide any existing file with the same path
        """
        path = MI.Dir_Gen + '/' + path
        os.makedirs(os.path.dirname(path), mode = 0o777, exist_ok = True)
        file = io.open(path,mode="w", encoding="utf-8")
        return file

def dirM(path:str) -> str:
    path = MI.Dir_Gen + '/' + path
    os.makedirs(os.path.dirname(path), mode = 0o777, exist_ok = True)
    return path

# format with a entire dict
def strDF(txt:str,dico:dict) -> str:
    patterns = re.findall(r"¤[^¤]+¤",txt)

    for p in set(patterns):
        p:str
        _p = p.replace('¤','')
        _p = _p.replace('>','')

        if _p in dico:
            _v = dico[_p]
            if not '>' in p:
                txt = txt.replace(p,_v)
            else:
                txt = txt.replace(p,_v+p)
    
    return txt

# format with simple pattern/replacer
def strF(txt:str,pattern:str,replacer:str):

    
    # patterns = re.findall(r"¤[^¤]+¤",txt)

    # rp = '¤'+pattern+'¤'   # raw pattern
    # rap = '¤>'+pattern+'¤'  # raw append pattern

    # if rp in patterns:
    #     txt = txt.replace(rp, replacer)
    # if rap in patterns:
    #     txt = txt.replace(rap, replacer + rap)

    txt_result = "null amogusent"

    txt_result = txt.replace('¤'+pattern+'¤',replacer)
    txt_result = txt_result.replace('¤>'+pattern+'¤',replacer + '¤>'+pattern+'¤')

    return txt_result



class MF:
    """
    this is a dynamic minecraft file
    """

    path:str = "src"
    data:str = "Hello World !"

    def __init__(self,path = "src") -> None:
        self.path = path
        pass

    def Build(self):
        f = vim(self.path)

        # clean the data from the ¤info¤
        cleanData = self.data

        # remove all patern exept '¤[<]+¤' which is made to remove one char behind
        patterns = re.findall(r"¤[^¤]+¤",cleanData)
        for i in patterns:
            i:str
            if not i[1:-1].count('<') == len(i[1:-1]):
                cleanData = cleanData.replace(i,"")

        # remove char before [^¤]¤[<]+¤ patterns
        patterns = re.findall(r"[^¤]¤[<]+¤",cleanData)
        for i in patterns:
            cleanData = cleanData.replace(i,"")

        f.write(cleanData)
        f.close()
        pass

    # set data from template file
    def __or__(self,template):
        with io.open(MI.Dir_Template + '/' + template + ".template",mode="r", encoding="utf-8") as f:
            self.data = f.read()
        return self
    
    # format with str
    def FormatStr(self,pattern:str,replacer:str):
        self.data = strF(self.data,pattern,replacer)
    
    # format with dict
    def FormatDict(self,dico : dict):
        self.data = strDF(self.data,dico)

    # format with MF
    def FormatFM(self,id,catMF):
        self.FormatStr(id,catMF.data)
    



MF_Registry = {}
MF_Action = {}


def GMF(id:str) -> MF:
    if not id in MF_Registry:
        MF_Registry[id] = MF(id)
    return MF_Registry[id]


    
    


# found = re.findall(r"¤[^¤]+¤",self.data)

# bigDico = dico | MODINFO.dico

# if len(found)>0:
#     for i in set(found):
#         i : str
#         ni = i.replace("¤","")

#         keep : bool = False
        
#         if ni.count('>') > 0: 
#             keep : bool = True
#             ni = ni.replace('>',"")

#         if(ni in bigDico):
#             self.data = self.data.replace(i,bigDico[ni] + i if keep else "")
        
#         print(ni.replace('.','/'))

#         if(ni.count('.')>0):
#             self.data = self.data.replace(i,FM.TemplateToStr(ni.replace('.','/')) + i if keep else "")