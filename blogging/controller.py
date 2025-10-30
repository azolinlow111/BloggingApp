from blogging.blog import Blog
from blogging.post import Post

class Controller:
    def __init__(self):
        self.blogs = []
        self.current_blog = None
        self.login_status = False

    def login(self, username, password):
        if self.login_status:
            return False
        
        else:
            if username == "user":
                
                if password == "blogging2025":
                    self.login_status = True
                    return True

                else:
                    return False

            else:
                return False
        
    def logout(self):
        if self.login_status:
            self.login_status = False
            return True
        
        else:
            return False

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