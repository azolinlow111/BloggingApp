from blogging.dao.post_dao import PostDAO
from blogging.post import Post
import datetime
from blogging.dao.blog_dao_json import BlogDAOJSON
from blogging.exception.invalid_login_exception import InvalidLoginException
from blogging.exception.duplicate_login_exception import DuplicateLoginException
from blogging.exception.invalid_logout_exception import InvalidLogoutException
from blogging.exception.illegal_access_exception import IllegalAccessException
from blogging.exception.illegal_operation_exception import IllegalOperationException
from blogging.exception.no_current_blog_exception import NoCurrentBlogException

class PostDAOPickle(PostDAO):
    def __init__(self, blog):
        self.blog = blog
        self.posts = []
  
    def search_post(self, key):
        for p in self.posts: #locate post in list 

            if p.code == key:
                return p
            
        return None
    
    
    def create_post(self, post):
        self.posts.append(post)
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
                    
            return post
    
    def delete_post(self, key):
        deleted_post = self.search_post(key)
            
        if deleted_post is not None: 

            self.posts.remove(deleted_post)
            
            return True
    
    def list_posts(self):
        return list(reversed(self.posts))
