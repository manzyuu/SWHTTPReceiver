import json


class JsonControl:

    
    def __init__(self,path:str):
        self.path=path
        self.data={}
        
        self.sample={"Websoket":{"URL":"",},
        "data":"",
        "path":"",}

    def check(self):
        try:
            file=open(self.path,'r',encoding='UTF-8')
            file.close()
            return ""

        except:
            self.data=self.sample
            self.write()
            return None
            
        


    def load(self):#,category: str,type: str,*array: str):

        try:
            file=open(self.path,'r',encoding='UTF-8')
            self.data=json.load(file)
            file.close()
            return self.data
        except Exception as e:
            print("loadErroer:",e)
        
        
        

        
        
        
        
    def write(self):#  value,category:str,type:str,*array:int):
        file=open(self.path,'w',encoding='UTF-8')
        #self.data=json.load(file)
        """try:
            self.data[category][type][array[0]][array[1]]=value
            json.dump(self.data,file,indent=4)
            file.close()
            print('writed data:',category,type,array[0],array[1],'data:', self.data[category][type][array[0]][array[1]])

        except: """
        
        #self.data[category][type]=value
        json.dump(self.data,file,indent=4)
        file.close()
        print('writed data')#,self.data[category][type])
    
    

