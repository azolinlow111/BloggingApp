from blogging.blog import Blog
from blogging.post import Post
import hashlib
from blogging.configuration import Configuration
from blogging.exception.invalid_login_exception import InvalidLoginException
from blogging.exception.duplicate_login_exception import DuplicateLoginException
from blogging.exception.invalid_logout_exception import InvalidLogoutException
from blogging.exception.illegal_access_exception import IllegalAccessException
from blogging.exception.illegal_operation_exception import IllegalOperationException
from blogging.exception.no_current_blog_exception import NoCurrentBlogException
from blogging.dao.blog_dao_json import BlogDAOJSON

class Controller:
    # initialize controller class
    def __init__(self):
        self.blog_dao= BlogDAOJSON()
        self.current_blog = None 
        self.login_status = False
        self.users_passwords = {}
        self.autosave = Configuration.autosave
        self.users_file = Configuration.users_file
        
        # get usernames and passwords from file
        with open(self.users_file, 'r') as file: 
            for line in file: 
                line = line.strip()
                username, password = line.split(',')
                    
                self.users_passwords[username] = password
        
    
    def get_password_hash(self, password):
        encoded_password = password.encode('utf-8')     # Convert the password to bytes
        hash_object = hashlib.sha256(encoded_password)      # Choose a hashing algorithm (e.g., SHA-256)
        hex_dig = hash_object.hexdigest()       # Get the hexadecimal digest of the hashed password
        return hex_dig
    
    # Checks if user is logged in and if not logs them in if they use the correct username and password
    def login(self, username, password):
        if self.login_status:
            raise DuplicateLoginException()
        
        else:
            if username in self.users_passwords:
                
                if self.get_password_hash(password) == self.users_passwords.get(username):
                    self.login_status = True
                    return True

                else:
                    raise InvalidLoginException()

            else:
                raise InvalidLoginException()
    
    # Logout the user if they are logged in
    def logout(self):
        if self.login_status:
            self.login_status = False
            return True
        
        else:
            raise InvalidLogoutException()

    # ------BLOG METHODS--------

    # search for a specific blog by id
    def search_blog(self, id):
        if self.login_status:
            return self.blog_dao.search_blog(id)
            
        else:
            raise IllegalAccessException()
    
    # Creates a new blog if it does not already exist
    def create_blog(self, id, name, url, email) -> Blog:
        if self.login_status:
            # check if blog exists
            if not self.search_blog(id):
            
                return self.blog_dao.create_blog(Blog(id, name, url, email))
            
            else:
                raise IllegalOperationException()
        else:
            raise IllegalAccessException()
        
    # Retrieves all blogs containing keyword
    def retrieve_blogs(self, keyword):
        if self.login_status:

            return self.blog_dao.retrieve_blogs(keyword)
        
        else:
            raise IllegalAccessException()

    # Update information about a blog, can change id if its not already in use
    def update_blog(self, id, new_id, new_name, new_url, new_email) -> bool:

        if self.login_status:  #check is logged in
            
            # check that the blog is not current blog
            if self.current_blog is None or self.current_blog.id != id:
                
                updated_blog = Blog(new_id, new_name, new_url, new_email)
                return self.blog_dao.update_blog(id, updated_blog)
                
            else: 
                raise IllegalOperationException()
                
        else:
            raise IllegalAccessException()
                    
    # Removes a blog if it exists
    def delete_blog(self, id):
        # check if user is logged in
        if self.login_status:
            
            #check blog to be erased is in the list 
            if self.search_blog(id) is not None:
                
                #check if blog to be erased is the current_blog
                if self.current_blog is not None: 
                    
                    if self.current_blog.id != id:
                        self.blog_dao.delete_blog(id)
                        return True
                            
                    else:
                        raise IllegalOperationException
                else: 
                    self.blog_dao.delete_blog(id)
                    return True
            else:
                raise IllegalOperationException()
        else:
            raise IllegalAccessException()

    # lists the current blogs
    def list_blogs(self):
        if self.login_status:

            return self.blog_dao.list_blogs()
        
        else:

            raise IllegalAccessException()
    
    # sets the current blog based on id
    def set_current_blog(self, id):
        if self.login_status:

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
        
        if self.login_status: #check user is logged in 

            if self.current_blog is not None: 

                return self.current_blog.search_post(code)

            else:
                raise NoCurrentBlogException()
            
        else:
            raise IllegalAccessException()
        
    # Creates a new post if it doesn't already exist
    def create_post(self, title, text):

        if self.login_status:                #check if user is logged in 

            if self.current_blog is not None:     #make sure current_blog is valid

                return self.current_blog.create_post(title, text)
            
            else:
                raise NoCurrentBlogException()
            
        else:
            raise IllegalAccessException()
        
    # Returns a list of posts that contain keyword
    def retrieve_posts(self, keyword): 
        if self.login_status:                                           #check user is logged in
            
            if self.current_blog is not None:                           #check current blog
                return self.current_blog.retrieve_posts(keyword)
                
            else: 
                raise NoCurrentBlogException()

        else: 
            raise IllegalAccessException()
    
    # Updates a post if it exists
    def update_post(self, code, title, text): 

        if self.login_status:  

            if self.current_blog is not None:
            
                return self.current_blog.update_post(code, title, text)
                
            else:
                raise NoCurrentBlogException()
                
        else:
            raise IllegalAccessException()

    # Removes a post if it exists
    def delete_post(self, code): 
        
        if self.login_status: 

            if self.current_blog is not None:
                
                return self.current_blog.delete_post(code)
                
            else:
                raise NoCurrentBlogException()
            
        else:
            raise IllegalAccessException()
        
    # returns a list of all posts within a blog
    def list_posts(self): 

        if self.login_status:

            if self.current_blog is not None: 
                return self.current_blog.list_posts()
           
            else:
                raise NoCurrentBlogException()
            
        else:
            raise IllegalAccessException()
