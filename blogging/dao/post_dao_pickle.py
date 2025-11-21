from blogging.dao.post_dao import PostDAO
from blogging.post import Post
import datetime
from blogging.dao.blog_dao_json import BlogDAOJSON
from blogging.configuration import Configuration
from pickle import dump, load, UnpicklingError

class PostDAOPickle(PostDAO):
    def __init__(self, blog):
        self.blog = blog
        self.posts = []
        self.autosave = Configuration.autosave
        
        if self.autosave: 
            self.posts_file = Configuration.records_path + "/" + str(self.blog.id) + Configuration.records_extension
            
            try:
                with open(self.posts_file, 'rb') as file:
                    self.posts = load(file)  # load the entire list at once
                    self.blog.post_counter = len(self.posts)
                    
            except (FileNotFoundError, EOFError, UnpicklingError):
                with open(self.posts_file, 'wb') as file:
                    pass


  
    def search_post(self, key):
        for p in self.posts: #locate post in list 

            if p.code == key:
                return p
            
        return None
    
    
    def create_post(self, post):
        self.posts.append(post)
        
        if self.autosave: 
            with open(self.posts_file, 'wb') as file:
                dump(self.posts, file)
        return post
        
    def retrieve_posts(self, search_string):
        posts_retrieved = [] 

        for p in self.posts:                       #loop over posts in blog

            if ((search_string in p.title) or (search_string in p.text)):   #check keyword in text or title 

                posts_retrieved.append(p)                       #append post to list 

        return posts_retrieved
    
    def update_post(self, key, new_title, new_text):
        post = self.search_post(key)
    
        if post is not None:

            post.title = new_title 
            post.text = new_text
            post.update = datetime.datetime.now()
        
            if self.autosave:
                with open(self.posts_file, 'wb') as file: 
                    dump(self.posts, file)
            
            return post
    
    def delete_post(self, key):
        deleted_post = self.search_post(key)
            
        if deleted_post is not None: 

            self.posts.remove(deleted_post)
            
            if self.autosave:
                with open(self.posts_file, 'wb') as file: 
                    dump(self.posts, file)
                    
            return True
    
    def list_posts(self):
        return list(reversed(self.posts))
