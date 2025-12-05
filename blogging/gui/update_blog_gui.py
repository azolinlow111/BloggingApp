import sys
from blogging.configuration import Configuration
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QGridLayout, QPushButton, QWidget, QLabel, QLineEdit, QMessageBox, QStackedWidget, QPlainTextEdit
from blogging.controller import Controller 


from blogging.exception.invalid_login_exception import InvalidLoginException
from blogging.exception.duplicate_login_exception import DuplicateLoginException
from blogging.exception.invalid_logout_exception import InvalidLogoutException
from blogging.exception.illegal_access_exception import IllegalAccessException
from blogging.exception.illegal_operation_exception import IllegalOperationException
from blogging.exception.no_current_blog_exception import NoCurrentBlogException

class UpdateBlogGUI:
    def __init__(self, controller):
        self.controller = controller

        #updating a blog
        self.update_blog_layout = QGridLayout()
        
        self.old_id_label = QLabel("Current ID")
        self.new_id_label = QLabel("New ID")
        self.new_name_label = QLabel("New Name")
        self.new_url_label = QLabel("New URL")
        self.new_email_label = QLabel("New Email")
        self.old_id_text = QLineEdit()
        self.new_id_text = QLineEdit()
        self.new_name_text = QLineEdit()
        self.new_url_text = QLineEdit()
        self.new_email_text = QLineEdit()
        self.update_blog_btn = QPushButton("Update")
        self.go_back_btn5 = QPushButton("Go Back to Main Menu")
        
        self.update_blog_layout.addWidget(self.old_id_label, 0,0)
        self.update_blog_layout.addWidget(self.old_id_text, 0,1)
        self.update_blog_layout.addWidget(self.new_id_label, 1,0)
        self.update_blog_layout.addWidget(self.new_id_text, 1,1)
        self.update_blog_layout.addWidget(self.new_name_label, 2,0)
        self.update_blog_layout.addWidget(self.new_name_text, 2,1)
        self.update_blog_layout.addWidget(self.new_url_label, 3,0)
        self.update_blog_layout.addWidget(self.new_url_text, 3,1)
        self.update_blog_layout.addWidget(self.new_email_label, 4,0)
        self.update_blog_layout.addWidget(self.new_email_text, 4,1)
        self.update_blog_layout.addWidget(self.go_back_btn5, 5,0)
        self.update_blog_layout.addWidget(self.update_blog_btn, 5, 1)

        self.update_blog_widget = QWidget()
        self.update_blog_widget.setLayout(self.update_blog_layout)

    def update_blog_btn_clicked(self):
        old_id = self.old_id_text.text()
        id = self.new_id_text.text()
        name = self.new_name_text.text()
        url = self.new_url_text.text()
        email = self.new_email_text.text()

        try: 
            if self.controller.update_blog(old_id, id, name, url, email): 
                QMessageBox.information(None, "Success", "Blog Updated Successfully!")
                self.clear_update()
                return 6

        except IllegalOperationException: 
            QMessageBox.warning(None, "Error", "Could Not Update Blog.")
            self.clear_update()
            return 6
        except IllegalAccessException:
            QMessageBox.warning(None, "Error", "You Must Login First")
            self.clear_update()
            return 0
        
    def clear_update(self):
        self.old_id_text.setText("")
        self.new_id_text.setText("")
        self.new_name_text.setText("")
        self.new_url_text.setText("")
        self.new_email_text.setText("")
