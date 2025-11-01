from blogging.post import Post

class Blog:

    def __init__(self, id, name, url, email, posts =None, post_counter =0):
        self.id = id
        self.name = name
        self.url = url
        self.email = email
        
        if posts is not None: 
            self.posts = posts
        else: 
            self.posts = []
        
        self.post_counter = post_counter

    def __eq__(self, other):
        return ((self.id == other.id) and (self.name == other.name) and (self.url == other.url) and (self.email == other.email))
    
    def __str__(self):
        return f"ID Number: {self.id}. Name: {self.name}. URL: {self.url}. Email: {self.email}."
    
    def add_post(self, title, text):
        self.post_counter +=1        
        new_post = Post(self.post_counter, title, text)
        self.posts.append(new_post)
        
        return new_post
        
    