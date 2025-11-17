from json import JSONDecoder
class blogging.blog import Blog

class BlogDecoder(JSONDecoder): 
    def __init__(self, *args, **kwargs): 
        super().__init__(object_hook=self.object_hook, *args, **kwargs)
    
    def object_hook(self, dct): 
        if '__type__' in dct and dct['__type__']