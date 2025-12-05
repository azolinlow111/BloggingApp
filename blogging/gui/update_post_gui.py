from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QGridLayout, QPushButton, QWidget, QLabel, QLineEdit, QMessageBox, QStackedWidget, QPlainTextEdit
from blogging.controller import Controller 

from blogging.exception.invalid_login_exception import InvalidLoginException
from blogging.exception.duplicate_login_exception import DuplicateLoginException
from blogging.exception.invalid_logout_exception import InvalidLogoutException
from blogging.exception.illegal_access_exception import IllegalAccessException
from blogging.exception.illegal_operation_exception import IllegalOperationException
from blogging.exception.no_current_blog_exception import NoCurrentBlogException

class UpdatePostGUI:
    def __init__(self, controller):
        self.controller = controller

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

        self.update_post_widget = QWidget()
        self.update_post_widget.setLayout(self.update_post_layout)

    #updates a post 
    def update_post_btn_clicked(self): 
        code = self.post_code.text() 
        title = self.post_new_title.text()
        text = self.post_new_text.text()
        
        try:
            if self.controller.search_post(int(code)) is not None:
                self.controller.update_post(int(code), title, text)
                QMessageBox.information(None, "Success", "Post Updated Successfully!")
                self.clear_update()
            else:
                QMessageBox.warning(None, "Update Post Error", "Cannot Update a Post that Doesn't Exist")
        
        except NoCurrentBlogException:
            QMessageBox.warning(None, "Update Post Error", "Cannot Update Post Without Blog Selected") 
            self.clear_update()
        except IllegalAccessException: 
            QMessageBox.warning(None, "Error", "You Must Login First")
            self.clear_update()
        
    def clear_update(self):
        self.post_code.clear()
        self.post_new_title.clear()
        self.post_new_text.clear()