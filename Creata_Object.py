
class create_object:

    def __init__(self,id,category ,name,photoUrls ,tags,status):
        self.id  = id
        self.category  =category
        self.name = name
        self.photoUrls = photoUrls
        self.tags = tags
        self.status = status


    def create_dict(self):
        return {"id" : self.id,self.category :{"id": 0,"name": "string" },self.name :"moshe",
                self.photoUrls :["string"],self.tags :[{"id": 0, "name": "string" }]
            ,self.status :"available"}



bbb = create_object("100","category","name","photoUrls","tags","status")
aaa = bbb.create_dict()
print(aaa)