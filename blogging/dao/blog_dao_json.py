from abc import ABC, abstractmethod
from blogging.dao.blog_dao import BlogDAO
from blogging.exception.invalid_login_exception import InvalidLoginException
from blogging.exception.duplicate_login_exception import DuplicateLoginException
from blogging.exception.invalid_logout_exception import InvalidLogoutException
from blogging.exception.illegal_access_exception import IllegalAccessException
from blogging.exception.illegal_operation_exception import IllegalOperationException
from blogging.exception.no_current_blog_exception import NoCurrentBlogException

class BlogDAOJSON(BlogDAO):
    def __init__(self):
        self.blogs = []
        self.current_blog = None
    # searches for a blog by id, if found, returns the blog, if not returns None
    def search_blog(self, id):
        for b in self.blogs:
                if id == b.id:
                    return b

        return None     

    def create_blog(self, blog):

        self.blogs.append(blog)
        return blog

    def retrieve_blogs(self, keyword):
        retrieved_blogs = []

        for b in self.blogs:
            if keyword in b.name:
                retrieved_blogs.append(b)

        return retrieved_blogs

    def update_blog(self, id, blog):
        if self.current_blog is None or self.current_blog != blog_for_update: 
                
                blog_for_update = self.search_blog(id)

                # check that blog exists
                if blog_for_update is not None: 
                     
                    

                    if blog.id == id: #check if ids remain unchangend 
                        blog_for_update.name = blog.name
                        blog_for_update.url = blog.url
                        blog_for_update.email = blog.email
                        
                        return True
                    
                    if self.search_blog(blog.id) is None: #check if new_id is not in list 
                        
                        blog_for_update.id = blog.id
                        blog_for_update.name = blog.name
                        blog_for_update.url = blog.url
                        blog_for_update.email = blog.email
                        
                        return True
                    else:
                        raise IllegalOperationException()
                
                else: 
                    raise IllegalOperationException()
                
        else:
            raise IllegalOperationException()

        

    def delete_blog(self, id):
        if len(self.blogs) > 0:

            if self.current_blog is not None:

                # check the blog is not the current blog
                if self.current_blog.id != id:
                    self.blogs.remove(self.search_blog(id))
                            
                else:
                    raise IllegalOperationException()
                        
            else:

                self.blogs.remove(self.search_blog(id))

                return True

            return True
        else:
            raise IllegalOperationException()

    def list_blogs(self):
        return self.blogs