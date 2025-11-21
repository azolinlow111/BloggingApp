from json import JSONDecoder

# converts json object into a Blog object
class BlogDecoder(JSONDecoder): 
    def __init__(self, *args, **kwargs): 
        super().__init__(object_hook=self.object_hook, *args, **kwargs)
    
    def object_hook(self, dct): 
        from blogging.blog import Blog
        if '__type__' in dct and dct['__type__'] == 'Blog': 
            return Blog(dct['id'],  dct['name'], dct['url'], dct['email'])
        return dct