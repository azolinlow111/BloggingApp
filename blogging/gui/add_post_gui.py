from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QGridLayout, QPushButton, QWidget, QLabel, QLineEdit, QMessageBox, QStackedWidget, QPlainTextEdit
from blogging.controller import Controller 

from blogging.exception.invalid_login_exception import InvalidLoginException
from blogging.exception.duplicate_login_exception import DuplicateLoginException
from blogging.exception.invalid_logout_exception import InvalidLogoutException
from blogging.exception.illegal_access_exception import IllegalAccessException
from blogging.exception.illegal_operation_exception import IllegalOperationException
from blogging.exception.no_current_blog_exception import NoCurrentBlogException

class AddPostGUI:
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

        self.add_post_widget = QWidget()
        self.add_post_widget.setLayout(self.add_post_layout)

    # takes user input and creates a post  
    def add_post_btn_clicked(self): 
        title = self.post_title.text()
        text = self.post_text.text()

        try: 
           self.controller.create_post(title, text)
           QMessageBox.information(None, "Success", "Post Created Successfully!")
           self.post_text.setText("")
           self.post_title.setText("")

        except (NoCurrentBlogException, IllegalAccessException): 
           QMessageBox.warning(None, "Create Post Error", "Cannot Create Post Properly")
           self.post_text.setText("")
           self.post_title.setText("")