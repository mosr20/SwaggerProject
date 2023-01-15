
class create_object:

    def __init__(self,id,category ,name,photoUrls ,tags,status):
        self.id  = id
        self.category  =category
        self.name = name
        self.photoUrls = photoUrls
        self.tags = tags
        self.status = status




    def build_message(self):
        return {self.id : 100,self.category :{"id": 0,"name": "string" },self.name :"moshe",
                self.photoUrls :["string"],self.tags :[{"id": 0, "name": "string" }]
            ,self.status :"available"}



