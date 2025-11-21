from json import JSONEncoder

# converts a blog object into a json object
class BlogEncoder(JSONEncoder): 
    def default(self, obj): 
        from blogging.blog import Blog
        if isinstance(obj, Blog): 
            return {"__type__": "Blog", "id": obj.id, "name": obj.name, \
            "url": obj.url, "email": obj.email}
        return super().default(obj)