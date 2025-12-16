from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QGridLayout, QPushButton, QWidget, QLabel, QMessageBox, QPlainTextEdit
from blogging.controller import Controller 

from blogging.exception.illegal_access_exception import IllegalAccessException
from blogging.exception.no_current_blog_exception import NoCurrentBlogException

class ListPostGUI:
    def __init__(self, controller):
        self.controller = controller
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
        self.list_posts_widget = QWidget()
        self.list_posts_widget.setLayout(self.list_posts_layout)

    #display blogs
    def list_posts_btn_clicked(self): 
        self.list_posts.clear()
  
        try: 
            posts = self.controller.list_posts()
            for post in posts: 
                self.list_posts.appendPlainText(f"Code: {post.code} {post}")

        except NoCurrentBlogException:
            QMessageBox.warning(None, "List Posts Error", "Cannot List Posts Without Blog Selected") 
                
        except IllegalAccessException:
            QMessageBox.warning(None, "Error", "You Must Login First")
