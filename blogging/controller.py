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

    def search_blog(self, id):

        for b in self.blogs:
            if id == b.id:
                return b

        return None
    
    def create_blog(self, id, name, url, email):
        if self.login_status:
            if not self.search_blog(id):
            
                b = Blog(id, name, url, email)

                self.blogs.append(b)

                print(f"\n\nPRINTING B: {b}")

                return b
            
            else:
                print("Blog already exists")
        else:
            return None
        
    def retrieve_blogs(self, keyword):
        if self.login_status:

            retrieved_blogs = []

            for b in self.blogs:
                if keyword in b.name:
                    retrieved_blogs.append(b)

            return retrieved_blogs
        
        else:
            return None


    def update_blog(self, id, new_id, new_name, new_url, new_email):
        if self.login_status and len(self.blogs) > 0:

            if self.search_blog(new_id) is None:
            
                if self.current_blog is not None:

                    if self.current_blog.id != id:
                        blog_for_update = self.search_blog(id)

                        blog_for_update.id = new_id
                        blog_for_update.name = new_name
                        blog_for_update.url = new_url
                        blog_for_update.email = new_email

                        return True
                    
                    else:
                        return False
                
                else:

                    blog_for_update = self.search_blog(id)

                    blog_for_update.id = new_id
                    blog_for_update.name = new_name
                    blog_for_update.url = new_url
                    blog_for_update.email = new_email

                    return True

            else:
                if id == new_id:
                    if self.current_blog is not None:

                        if self.current_blog.id != id:
                            blog_for_update = self.search_blog(id)

                            blog_for_update.name = new_name
                            blog_for_update.url = new_url
                            blog_for_update.email = new_email

                            return True
                        
                        else:
                           return False
                    
                    else:
                        blog_for_update = self.search_blog(id)

                        blog_for_update.name = new_name
                        blog_for_update.url = new_url
                        blog_for_update.email = new_email

                        return True
                
                else:
                    return False
        
        else:
            return False
        
    def delete_blog(self, id):
        if self.login_status and len(self.blogs) > 0:

            if self.search_blog(id) is not None:
            
                if self.current_blog is not None:

                    if self.current_blog.id != id:
                        self.blogs.remove(self.search_blog(id))

                        return True
                    
                    else:
                        return False
                
                else:

                    for b in self.blogs:
                         if b.id == id:
                            self.blogs.remove(b)

                    return True

            else:
                return False
        
        else:
            return False

    def list_blogs(self):
        if self.login_status:

            return self.blogs
        
        else:

            return None
        
    def set_current_blog(self, id):
        if self.login_status and len(self.blogs) > 0:

            if self.search_blog(id) is not None:
                self.current_blog = self.search_blog(id)

                return self.current_blog

            else:
                return None


        else:
            return None
        
    def get_current_blog(self):
        if self.login_status:
            return self.current_blog
        
        else:
            return None
        
    def unset_current_blog(self):
        if self.login_status:
            self.current_blog = None

            return self.current_blog
        
        else:
            return False

