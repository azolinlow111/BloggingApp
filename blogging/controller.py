from blogging.blog import Blog
from blogging.post import Post

class controller:
    def __init__(self):
        self.blogs = []
        self.current_blog = None

def create_blog(self, id, name, url, email):
    if not search_blog(self, id):
    
        b = Blog(id, name, url, email)

        self.blogs.append(b)
    
    else:
        print("Blog already exists")


def search_blog(self, id):

    for b in self.blogs:
        if id == b.id:
            return True

    return False