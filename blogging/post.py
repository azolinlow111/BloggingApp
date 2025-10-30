from datetime import datetime

class Post:

    def __init__(self, code, title, text, creation, update):
        self.code = code
        self.title = title
        self.text = text
        self.creation = datetime.now()
        self.update = datetime.now()

    def __str__(self):
        # returns printable string representation of a post
        return f"Last Edited: {self.update}. Title: {self.title}. Post Content: {self.text}"

    def __repr__(self):
        # returns string representation of a post
        return f"Integer Code: {self.code}. Created: {self.creation}. Updated: {self.update}. Title: {self.title}. Post Content: {self.text}"

    def __eq__(self, other):
        # compares post based on code, title, text
        return (self.code == other.code) and (self.title == other.title) and (self.text == other.text)