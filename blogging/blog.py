class Blog:

    def __init__(self, id, name, url, email, posts = [], post_counter = 0):
        self.id = id
        self.name = name
        self.url = url
        self.email = email
        self.posts = posts
        self.post_counter = post_counter

    def __eq__(self, other):
        return ((self.id == other.id) and (self.name == other.name) and (self.url == other.url) and (self.email == other.email))
    
    def __str__(self):
        return f"ID Number: {self.id}. Name: {self.name}. URL: {self.url}. Email: {self.email}."