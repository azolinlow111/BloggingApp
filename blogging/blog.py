from blogging.post import Post
from blogging.dao.post_dao_pickle import PostDAOPickle
import datetime

class Blog:

    def __init__(self, id, name, url, email):
        self.id = id
        self.name = name
        self.url = url
        self.email = email
        
        self.post_counter = 0; 
        
        self.post_dao = PostDAOPickle(self) #initiate a postDAOPickle variable
        
    def __eq__(self, other) -> bool:
        return ((self.id == other.id) and (self.name == other.name) and (self.url == other.url) and (self.email == other.email))
    
    def __str__(self) -> str:
        return f"ID Number: {self.id}. Name: {self.name}. URL: {self.url}. Email: {self.email}."
    
    def __repr__(self) -> str:
        return f"ID Number: {self.id}. Name: {self.name}. URL: {self.url}. Email: {self.email}."
    
    def create_post(self, title, text) -> Post:  
        self.post_counter +=1          
        new_post = Post(self.post_counter, title, text, datetime.datetime.now())
        return self.post_dao.create_post(new_post)
        
    def search_post(self, code):     
        return self.post_dao.search_post(code)
    
    def retrieve_posts(self, keyword):
        return self.post_dao.retrieve_posts(keyword)
    
    def update_post(self, code, title, text):
        return self.post_dao.update_post(code, title, text)
    
    def delete_post(self, code):
        return self.post_dao.delete_post(code)
        
    def list_posts(self):
        return self.post_dao.list_posts()