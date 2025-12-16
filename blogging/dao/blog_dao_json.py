import json
from blogging.dao.blog_dao import BlogDAO
from blogging.exception.illegal_operation_exception import IllegalOperationException
from blogging.configuration import Configuration
from blogging.dao.blog_encoder import BlogEncoder
from blogging.dao.blog_decoder import BlogDecoder

class BlogDAOJSON(BlogDAO):
    # initialize BlogDAOJSON class
    def __init__(self):
        self.blogs = []
        self.autosave = Configuration.autosave

        # if using persistence create blog.json file
        if self.autosave:
            self.blog_file = Configuration.blogs_file
            try:
                with open(self.blog_file, 'r') as file:
                   self.blogs = json.load(file, cls=BlogDecoder)

            except (FileNotFoundError, json.JSONDecodeError):
                with open(self.blog_file, 'w') as file:
                    json.dump([], file)
 
    # searches for a blog by id, if found, returns the blog, if not returns None
    def search_blog(self, id):
        for b in self.blogs:
            if id == b.id:
                return b

        return None     

    # create a new blog, if using persistence save it to blog.json
    def create_blog(self, blog):
        self.blogs.append(blog)
        
        if self.autosave:
            with open(self.blog_file, 'w') as file:
                json.dump(self.blogs, file, cls=BlogEncoder)
        
        return blog

    # retrieve blogs by keyword, return list of blogs
    def retrieve_blogs(self, keyword):
        retrieved_blogs = []
        
        for b in self.blogs:
            if keyword.lower() in b.name.lower():
                retrieved_blogs.append(b)

        return retrieved_blogs

    # update a blog in the blogs list, if using persistence update the blog.json file too
    def update_blog(self, id, blog):
        blog_for_update = self.search_blog(id)

        #check that blog is in the list 
        if blog_for_update is not None: 
            
            if blog.id == id: #check if ids remain unchangend 
                blog_for_update.name = blog.name
                blog_for_update.url = blog.url
                blog_for_update.email = blog.email
                
                #update json file 
                if self.autosave:
                    with open(self.blog_file, 'w') as file:
                        json.dump(self.blogs, file, cls=BlogEncoder)

                return True
                
            if self.search_blog(blog.id) is None: #check if new_id is not in list 
                
                blog_for_update.id = blog.id
                blog_for_update.name = blog.name
                blog_for_update.url = blog.url
                blog_for_update.email = blog.email
                
                #update json file 
                if self.autosave:
                    with open(self.blog_file, 'w') as file:
                        json.dump(self.blogs, file, cls=BlogEncoder)
               
                return True 
            
            else: 
                raise IllegalOperationException()
        
        else: 
            raise IllegalOperationException()
        
    # delete a blog based on id, if using persistence remove from blog.json file too
    def delete_blog(self, id):
        self.blogs.remove(self.search_blog(id))
        
        #update json file 
        if self.autosave:
            with open(self.blog_file, 'w') as file:
                json.dump(self.blogs, file, cls=BlogEncoder)
               
    # returns a list of all blogs
    def list_blogs(self):
        return self.blogs