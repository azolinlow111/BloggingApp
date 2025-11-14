from blogging.post import Post
import datetime

class Blog:

    def __init__(self, id, name, url, email, posts =None, post_counter =0):
        self.id = id
        self.name = name
        self.url = url
        self.email = email
        self.post_counter = post_counter
        
        if posts is not None: 
            self.posts = posts
        else: 
            self.posts = []
        
    def __eq__(self, other) -> bool:
        return ((self.id == other.id) and (self.name == other.name) and (self.url == other.url) and (self.email == other.email))
    
    def __str__(self) -> str:
        return f"ID Number: {self.id}. Name: {self.name}. URL: {self.url}. Email: {self.email}."
    
    def __repr__(self) -> str:
        return f"ID Number: {self.id}. Name: {self.name}. URL: {self.url}. Email: {self.email}."
    
    def create_post(self, title, text) -> Post:
        self.post_counter +=1        
        new_post = Post(self.post_counter, title, text, datetime.datetime.now())
        self.posts.append(new_post)
        
        return new_post
        
    def search_post(self, code):
        for p in self.posts: #locate post in list 

            if p.code == code:
                post = p #get post to be returned 

                return post
            
        return None
    
    def retrieve_posts(self, keyword):
        posts_retrieved = [] 

        for p in self.posts:                       #loop over posts in blog

            if ((keyword in p.title) or (keyword in p.text)):   #check keyword in text or title 

                posts_retrieved.append(p)                       #append post to list 

        return posts_retrieved
    
    def update_posts(self, code, title, text):
        post = self.search_post(code)
                
        if post is not None:

            post.title = title 
            post.text = text
            post.update = datetime.datetime.now()
                    
            return post
    
    def delete_post(self, code):
        deleted_post = self.search_post(code)
            
        if deleted_post is not None: 

            self.posts.remove(deleted_post)
        
            return True
        
    def list_posts(self):
             
        posts_li = list(reversed(self.posts))
                
        return posts_li
            