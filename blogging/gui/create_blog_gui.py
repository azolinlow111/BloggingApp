import sys
import re
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QGridLayout, QPushButton, QWidget, QLabel, QLineEdit, QMessageBox
from blogging.controller import Controller 

from blogging.exception.illegal_access_exception import IllegalAccessException
from blogging.exception.illegal_operation_exception import IllegalOperationException

class CreateBlogGUI:
    def __init__(self, controller):
        self.controller = controller

        # layout
        self.create_blog_layout = QGridLayout()
        
        self.id_label = QLabel("ID")
        self.name_label = QLabel("Name")
        self.url_label = QLabel("URL")
        self.email_label = QLabel("Email")
        self.id_text = QLineEdit()
        self.name_text = QLineEdit()
        self.url_text = QLineEdit()
        self.email_text = QLineEdit()
        self.create_new_blog_btn = QPushButton("Create")
        self.go_back_btn1 = QPushButton("Go Back to Main Menu")
        
        self.create_blog_layout.addWidget(self.id_label, 0,0)
        self.create_blog_layout.addWidget(self.id_text, 0,1)
        self.create_blog_layout.addWidget(self.name_label, 1,0)
        self.create_blog_layout.addWidget(self.name_text, 1,1)
        self.create_blog_layout.addWidget(self.url_label, 2,0)
        self.create_blog_layout.addWidget(self.url_text, 2,1)
        self.create_blog_layout.addWidget(self.email_label, 3,0)
        self.create_blog_layout.addWidget(self.email_text, 3,1)
        self.create_blog_layout.addWidget(self.go_back_btn1, 4,0)
        self.create_blog_layout.addWidget(self.create_new_blog_btn, 4, 1)

        self.create_blog_widget = QWidget()
        self.create_blog_widget.setLayout(self.create_blog_layout)
    
    #creates a new blog when button is clicked
    def create_new_blog_btn_clicked(self):
        id = self.id_text.text()
        name = self.name_text.text()
        url = self.url_text.text()
        email = self.email_text.text()

        try: 
            if all([id, name, url, email]):

                try:
                    converted_id = int(id)

                    if converted_id <= 0:
                        raise ValueError
                    
                    else:
                        if self.is_url(url):

                            if self.is_email(email):

                                if self.controller.create_blog(converted_id, name, url, email):

                                    QMessageBox.information(None, "Success", "Blog Created Successfully!")
                                    self.clear_create_blog()
                                    return 3
                                
                            else:
                                QMessageBox.warning(None, "Error", "You Must Use A Valid Email")
                                return 3
                                
                        else:    
                            QMessageBox.warning(None, "Error", "You Must Use A Valid URL")
                            return 3
                
                except ValueError:
                    QMessageBox.warning(None, "Error", "ID Must Be An Integer > 0")
                    return 3

            else:
                QMessageBox.warning(None, "Error", "You Must Fill All Fields")
                return 3
            
        except IllegalOperationException: 
            QMessageBox.warning(None, "Error", "Blog Cannot Have the Same ID as Another Blog.")
            self.clear_create_blog()
            return 3

        except IllegalAccessException:
            QMessageBox.warning(None, "Error", "You Must Login First")
            self.clear_create_blog()
            return 0
    
    #clear input boxes information
    def clear_create_blog(self):
        self.id_text.setText("")
        self.name_text.setText("")
        self.url_text.setText("")
        self.email_text.setText("")

    def is_email(self, email):
        valid_email = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(valid_email, email) is not None

    def is_url(self, url):
        valid_url = r'^(https?://)?(www\.)?[\w\-]+\.[a-z]{2,}(/[\w\./?%&=-]*)?$'
        return re.match(valid_url, url) is not None
    