from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QGridLayout, QPushButton, QWidget, QLabel, QLineEdit, QMessageBox, QStackedWidget, QPlainTextEdit
from blogging.controller import Controller 

from blogging.exception.invalid_login_exception import InvalidLoginException
from blogging.exception.duplicate_login_exception import DuplicateLoginException
from blogging.exception.invalid_logout_exception import InvalidLogoutException
from blogging.exception.illegal_access_exception import IllegalAccessException
from blogging.exception.illegal_operation_exception import IllegalOperationException
from blogging.exception.no_current_blog_exception import NoCurrentBlogException

class PostGUI: 
    def __init__(self, controller):
        self.controller = controller  
        
        #add post layout 
        self.add_post_layout = QGridLayout()
        
        self.post_title_label = QLabel("Add Post Title")
        self.post_title = QLineEdit()
        self.post_text_label = QLabel("Add Post Text")
        self.post_text = QLineEdit()
        self.add_post_btn = QPushButton("Create New Post")
        self.go_back_btn_posts1 = QPushButton("Go Back To Post Menu")
        
        self.add_post_layout.addWidget(self.post_title_label, 0,0)
        self.add_post_layout.addWidget(self.post_title, 0,1)
        self.add_post_layout.addWidget(self.post_text_label, 1,0)
        self.add_post_layout.addWidget(self.post_text, 1,1)
        self.add_post_layout.addWidget(self.add_post_btn, 2,1)
        self.add_post_layout.addWidget(self.go_back_btn_posts1,2,0)
        
        #retrieve post layout 
        self.retrieve_post_layout = QGridLayout() 
        
        self.post_keyword_label = QLabel("Search Post By Text")
        self.post_keyword = QLineEdit()
        self.retrieve_post_btn = QPushButton("Search") 
        self.post_retrieved = QPlainTextEdit()
        self.post_retrieved.setEnabled(False) 
        self.go_back_btn_posts2 = QPushButton("Go Back To Post Menu")
        
        self.retrieve_post_layout.addWidget(self.post_keyword_label, 0,0)
        self.retrieve_post_layout.addWidget(self.post_keyword, 0,1)        
        self.retrieve_post_layout.addWidget(self.retrieve_post_btn, 0,2)
        self.retrieve_post_layout.addWidget(self.post_retrieved, 1,0) 
        self.retrieve_post_layout.addWidget(self.go_back_btn_posts2,2,0)
        
        #update post layout 
        self.update_post_layout = QGridLayout()
        
        self.post_code_label = QLabel("Enter Code")
        self.post_code = QLineEdit()
        self.post_new_title_label = QLabel("New Title")
        self.post_new_title = QLineEdit()
        self.post_new_text_label = QLabel("New Text")
        self.post_new_text = QLineEdit()
        self.update_post_btn = QPushButton("Update")
        self.go_back_btn_posts3 = QPushButton("Go Back To Post Menu")
        
        self.update_post_layout.addWidget(self.post_code_label, 0,0)
        self.update_post_layout.addWidget(self.post_code, 0,1)
        self.update_post_layout.addWidget(self.post_new_title_label, 1,0)
        self.update_post_layout.addWidget(self.post_new_title, 1,1)
        self.update_post_layout.addWidget(self.post_new_text_label, 2,0)
        self.update_post_layout.addWidget(self.post_new_text, 2,1)
        self.update_post_layout.addWidget(self.go_back_btn_posts3,3,0)
        self.update_post_layout.addWidget(self.update_post_btn,3,1)
        
        #delete post layout 
        self.delete_post_layout = QGridLayout() 
        
        self.delete_post_code_label = QLabel("Enter Code")
        self.delete_post_code = QLineEdit()
        self.delete_post_btn = QPushButton("Delete")
        self.go_back_btn_posts4 = QPushButton("Go Back To Post Menu")
        
        self.delete_post_layout.addWidget(self.delete_post_code_label, 0,0)
        self.delete_post_layout.addWidget(self.delete_post_code, 0,1)
        self.delete_post_layout.addWidget(self.delete_post_btn, 1,1)
        self.delete_post_layout.addWidget(self.go_back_btn_posts4,1,0)
        
        #list posts layout 
        self.list_posts_layout = QGridLayout() 
        
        self.list_posts_label = QLabel("Posts")
        self.list_posts = QPlainTextEdit()
        self.list_posts.setEnabled(False) 
        self.go_back_btn_posts5 = QPushButton("Go Back To Post Menu")
        
        self.list_posts_layout.addWidget(self.list_posts_label, 0,0)
        self.list_posts_layout.addWidget(self.list_posts, 1,0)
        self.list_posts_layout.addWidget(self.go_back_btn_posts5, 2,0)
        
        # set layouts  
        
        self.add_post_widget = QWidget()
        self.add_post_widget.setLayout(self.add_post_layout)
        
        self.retrieve_post_widget = QWidget()
        self.retrieve_post_widget.setLayout(self.retrieve_post_layout)
        
        self.update_post_widget = QWidget()
        self.update_post_widget.setLayout(self.update_post_layout)
        
        self.delete_post_widget = QWidget()
        self.delete_post_widget.setLayout(self.delete_post_layout)
        
        self.list_posts_widget = QWidget()
        self.list_posts_widget.setLayout(self.list_posts_layout)
        
    
    #takes user input and creates a post  
    def add_post_btn_clicked(self): 
        title = self.post_title.text()
        text = self.post_text.text()
        try: 
           self.controller.create_post(title, text)
           QMessageBox.information(None, "success", "Post Created Successfully!")
           self.post_text.setText("")
           self.post_title.setText("")
        except (NoCurrentBlogException, IllegalAccessException): 
           QMessageBox.warning(None, "Create Post Error", "Cannot Create Post Properly")
           self.post_text.setText("")
           self.post_title.setText("")
    
    #retrieves post containing keyword in text 
    def retrieve_post_btn_clicked(self): 
        self.post_retrieved.clear()
        keyword = self.post_keyword.text()

        try: 
            post_li = self.controller.retrieve_posts(keyword)

            if len(post_li) > 0: 
                for post in post_li: 
                    self.post_retrieved.appendPlainText(str(post))
            else: 
                QMessageBox.warning(None, "Error", "No matching Posts")

        except (NoCurrentBlogException, IllegalAccessException):
            pass
        
        self.post_keyword.clear()
    
    #updates a post 
    def update_post_btn_clicked(self): 
        code = self.post_code.text() 
        title = self.post_new_title.text()
        text = self.post_new_text.text()
        
        try: 
            self.controller.update_post(int(code), title, text)
        
        except (NoCurrentBlogException, IllegalAccessException): 
            pass
        
        self.post_code.clear()
        self.post_new_title.clear()
        self.post_new_text.clear()

    #delete post 
    def delete_post_btn_clicked(self): 
        code = self.delete_post_code.text()
        try: 
            if self.controller.delete_post(int(code)): 
                QMessageBox.information(None, "success", "Post Deleted Successfully!")
            else: 
                QMessageBox.warning(None, "failure", "Post Was Not Deleted Successfully")
                
        except (NoCurrentBlogException, IllegalAccessException):
                pass 
        
        self.delete_post_code.clear()
    

        