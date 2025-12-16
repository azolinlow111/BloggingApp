from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QGridLayout, QPushButton, QWidget, QLabel, QLineEdit, QMessageBox, QPlainTextEdit
from blogging.controller import Controller 

from blogging.exception.illegal_access_exception import IllegalAccessException
from blogging.exception.no_current_blog_exception import NoCurrentBlogException

class RetrievePostGUI:
    def __init__(self, controller):
        self.controller = controller

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

        self.retrieve_post_widget = QWidget()
        self.retrieve_post_widget.setLayout(self.retrieve_post_layout)
    
    #retrieves post containing keyword in text 
    def retrieve_post_btn_clicked(self): 
        self.post_retrieved.clear()
        keyword = self.post_keyword.text()

        try:
            if all([keyword]):
                post_li = self.controller.retrieve_posts(keyword)

                if len(post_li) > 0: 
                    for post in post_li: 
                        self.post_retrieved.appendPlainText(f"Code: {post.code} {post}")
                else: 
                    QMessageBox.warning(None, "Error", "No matching Posts")
            
            else:
                QMessageBox.warning(None, "Error", "Please Enter A Keyword")

        except NoCurrentBlogException:
            QMessageBox.warning(None, "Error", "Cannot Delete Post Without Current Blog Selected")
            
        except IllegalAccessException:
            QMessageBox.warning(None, "Error", "You Must Login First")
        
        self.post_keyword.clear()