from abc import ABC, abstractmethod
from blogging.exception.invalid_login_exception import InvalidLoginException
from blogging.exception.duplicate_login_exception import DuplicateLoginException
from blogging.exception.invalid_logout_exception import InvalidLogoutException
from blogging.exception.illegal_access_exception import IllegalAccessException
from blogging.exception.illegal_operation_exception import IllegalOperationException
from blogging.exception.no_current_blog_exception import NoCurrentBlogException

class BlogDAOJSON(ABC):
    # searches for a blog by id, if found, returns the blog, if not returns None
    @abstractmethod
    def search_blog(self, key):
        
        if self.login_status:
            for b in self.blogs:
                if id == b.id:
                    return b

            return None
        else:
            raise IllegalAccessException()
        
    @abstractmethod
    def create_blog(self, blog):
        pass
    @abstractmethod
    def retrieve_blogs(self, search_string):
        pass
    @abstractmethod
    def update_blog(self, key, blog):
        pass
    @abstractmethod
    def delete_blog(self, key):
        pass
    @abstractmethod
    def list_blogs(self):
        pass