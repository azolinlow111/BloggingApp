from blogging.blog import Blog
from blogging.post import Post
from datetime import datetime
import os
from blogging.configuration import Configuration
from blogging.exception.invalid_login_exception import InvalidLoginException
from blogging.exception.duplicate_login_exception import DuplicateLoginException
from blogging.exception.invalid_logout_exception import InvalidLogoutException
from blogging.exception.illegal_access_exception import IllegalAccessException
from blogging.exception.illegal_operation_exception import IllegalOperationException
from blogging.exception.no_current_blog_exception import NoCurrentBlogException

class Controller:
    def __init__(self):
        self.blogs = []
        self.current_blog = None
        self.login_status = False
        self.users_passwords = {"user":"8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92", "ali":"6394ffec21517605c1b426d43e6fa7eb0cff606ded9c2956821c2c36bfee2810", "kala":"e5268ad137eec951a48a5e5da52558c7727aaa537c8b308b5e403e6b434e036e", "user":"123456", "ali":"@G00dPassw0rd"}

    # Checks if user is logged in and if not logs them in if they use the correct username and password
    def login(self, username, password) -> bool:
        if self.login_status:
            raise DuplicateLoginException()
        
        else:
            if username in self.users_passwords:
                
                if password == self.users_passwords.get(username):
                    self.login_status = True
                    return True

                else:
                    raise InvalidLoginException()

            else:
                raise InvalidLoginException()
    
    # Logout the user if they are logged in
    def logout(self) -> bool:
        if self.login_status:
            self.login_status = False
            return True
        
        else:
            raise InvalidLogoutException()

    # ------BLOG METHODS--------

    # searches for a blog by id, if found, returns the blog, if not returns None
    def search_blog(self, id) -> Blog:
        if self.login_status:
            for b in self.blogs:
                if id == b.id:
                    return b

            return None
        else:
            raise IllegalAccessException()
    
    # Creates a new blog if it does not already exist
    def create_blog(self, id, name, url, email) -> Blog:
        if self.login_status:
            # check if blog exists
            if not self.search_blog(id):
            
                b = Blog(id, name, url, email)

                self.blogs.append(b)
                return b
            
            else:
                raise IllegalOperationException()
        else:
            raise IllegalAccessException()
        
    # Retrieves all blogs containing keyword
    def retrieve_blogs(self, keyword):
        if self.login_status:

            retrieved_blogs = []

            for b in self.blogs:
                if keyword in b.name:
                    retrieved_blogs.append(b)

            return retrieved_blogs
        
        else:
            raise IllegalAccessException()

    # Update information about a blog, can change id if its not already in use
    def update_blog(self, id, new_id, new_name, new_url, new_email) -> bool:

        if self.login_status:  #check is logged in
            
            blog_for_update = self.search_blog(id)
            # check that the blog is not current blog
            if self.current_blog is None or self.current_blog != blog_for_update: 
                
                # check that blog exists
                if blog_for_update is not None: 
                    
                    if new_id == id: #check if ids remain unchangend 
                        blog_for_update.name = new_name
                        blog_for_update.url = new_url
                        blog_for_update.email = new_email
                        
                        return True
                
                    if self.search_blog(new_id) is None: #check if new_id is not in list 
                        
                        blog_for_update.id = new_id
                        blog_for_update.name = new_name
                        blog_for_update.url = new_url
                        blog_for_update.email = new_email
                        
                        return True

                    else:
                        raise IllegalOperationException()
            
                else: 
                    raise IllegalOperationException()
                
            else:
                raise IllegalOperationException()
        
        else:
            raise IllegalAccessException()
                    
    # Removes a blog if it exists
    def delete_blog(self, id):
        # check if user is logged in and if there are blogs
        if self.login_status:
        
            if len(self.blogs) > 0:

                # check if blog exists
                if self.search_blog(id) is not None:
                
                    if self.current_blog is not None:

                        # check the blog is not the current blog
                        if self.current_blog.id != id:
                            self.blogs.remove(self.search_blog(id))

                            return True
                        
                        else:
                            raise IllegalOperationException()
                    
                    else:

                        self.blogs.remove(self.search_blog(id))

                        return True

                else:
                    raise IllegalOperationException()
                
            else:
                raise IllegalOperationException()
        
        else:
            raise IllegalAccessException()

    # lists the current blogs
    def list_blogs(self):
        if self.login_status:

            return self.blogs
        
        else:

            raise IllegalAccessException()
    
    # sets the current blog based on id
    def set_current_blog(self, id):
        if self.login_status and len(self.blogs) > 0:

            if self.search_blog(id) is not None:
                self.current_blog = self.search_blog(id)

                return self.current_blog

            else:
                raise IllegalOperationException()

        else:
            raise IllegalAccessException()
        
    # Returns the current blog
    def get_current_blog(self):
        if self.login_status:
            return self.current_blog
        
        else:
            raise IllegalAccessException()
        
    # Sets current blog to None
    def unset_current_blog(self):
        if self.login_status:
            self.current_blog = None

            return self.current_blog
        
        else:
            raise IllegalAccessException()
            
    # ------POST METHODS--------
        
    # Searches post in a blog by code and returns if found
    def search_post(self, code) -> Post:
        post = None
        
        if self.login_status: #check user is logged in 

            if self.current_blog is not None: 

                for p in self.current_blog.posts: #locate post in list 

                    if p.code == code:
                        post = p #get post to be returned 

                return post
            
            else:
                raise NoCurrentBlogException()
            
        else:
            raise IllegalAccessException()
        
    # Creates a new post if it doesn't already exist
    def create_post(self, title, text) -> Post:
        post_created = None
        
        if self.login_status:                #check if user is logged in 

            if self.current_blog is not None:     #make sure current_blog is valid

                post_created = self.current_blog.add_post(title, text)
        
                return post_created 
            
            else:
                raise NoCurrentBlogException()
            
        else:
            raise IllegalAccessException()
        
    # Returns a list of posts that contain keyword
    def retrieve_posts(self, keyword): 
        if self.login_status:                                           #check user is logged in

            posts_retrieved = [] 
            
            if self.current_blog is not None:                           #check current blog

                for p in self.current_blog.posts:                       #loop over posts in blog

                    if ((keyword in p.title) or (keyword in p.text)):   #check keyword in text or title 

                        posts_retrieved.append(p)                       #append post to list 

                return posts_retrieved
            
            else: 
                raise NoCurrentBlogException()

        else: 
            raise IllegalAccessException()
    
    # Updates a post if it exists
    def update_post(self, code, title, text) -> Post: 
        post = None

        if self.login_status:  

            if self.current_blog is not None:
            
                post = self.search_post(code)
                
                if post is not None:

                    post.title = title 
                    post.text = text
                    post.update = datetime.now()
                    
                    return post
                
            else:
                raise NoCurrentBlogException()
                
        else:
            raise IllegalAccessException()

    # Removes a post if it exists
    def delete_post(self, code) -> bool: 
        deleted = False
        
        if self.login_status: 

            if self.current_blog is not None:
                
                deleted_post = self.search_post(code)
            
                if deleted_post is not None: 

                    self.current_blog.posts.remove(deleted_post)
                    deleted = True
        
                    return deleted
                
            else:
                raise NoCurrentBlogException()
            
        else:
            raise IllegalAccessException()
        
    # returns a list of all posts within a blog
    def list_posts(self): 
        posts_li = None

        if self.login_status:

            if self.current_blog is not None: 
                
                posts_li = list(reversed(self.current_blog.posts))
                
                return posts_li
            
            else:
                raise NoCurrentBlogException()
            
        else:
            raise IllegalAccessException()
