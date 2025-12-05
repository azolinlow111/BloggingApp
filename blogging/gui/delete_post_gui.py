from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QGridLayout, QPushButton, QWidget, QLabel, QLineEdit, QMessageBox
from blogging.controller import Controller 

from blogging.exception.illegal_access_exception import IllegalAccessException
from blogging.exception.no_current_blog_exception import NoCurrentBlogException

class DeletePostGUI:
    def __init__(self, controller):
        self.controller = controller

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

        self.delete_post_widget = QWidget()
        self.delete_post_widget.setLayout(self.delete_post_layout)

    #delete post 
    def delete_post_btn_clicked(self): 
        code = self.delete_post_code.text()
        try:
            if all([code]):

                if self.controller.delete_post(int(code)): 
                    QMessageBox.information(None, "Success", "Post Deleted Successfully!")
                else: 
                    QMessageBox.warning(None, "Failure", "Post Was Not Deleted Successfully")
                
            else:
                QMessageBox.warning(None, "Error", "Please Enter A Code")

        except NoCurrentBlogException:
            QMessageBox.warning(None, "Error", "Cannot Delete Post Without Current Blog Selected")
                
        except IllegalAccessException:
            QMessageBox.warning(None, "Error", "You Must Login First")
        
        self.delete_post_code.clear()