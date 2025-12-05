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

class DeleteBlogGUI:
    def __init__(self, controller):
        # delete a blog
        self.controller = controller

        self.delete_blog_layout = QGridLayout()

        self.id_delete_blog_label = QLabel("Enter the ID of the Blog")
        self.id_delete_blog_text = QLineEdit()
        self.delete_blog_btn = QPushButton("Delete")
        self.go_back_btn6 = QPushButton("Go Back to Main Menu")

        self.delete_blog_layout.addWidget(self.id_delete_blog_label, 0,0)
        self.delete_blog_layout.addWidget(self.id_delete_blog_text, 0,1)
        self.delete_blog_layout.addWidget(self.delete_blog_btn,0,2)
        self.delete_blog_layout.addWidget(self.go_back_btn6, 1,1)

        self.delete_blog_widget = QWidget()
        self.delete_blog_widget.setLayout(self.delete_blog_layout)

    def delete_blog_btn_clicked(self):
        blog_to_delete = self.id_delete_blog_text.text()

        try:
            if self.controller.delete_blog(blog_to_delete):
                QMessageBox.information(None, "Success", "Blog Deleted Successfully!")
                self.id_delete_blog_text.setText("")
                return 7

        except IllegalOperationException:
            QMessageBox.warning(None, "Error", "Could Not Delete Blog.")
            self.id_delete_blog_text.setText("")

        except IllegalAccessException:
            QMessageBox.warning(None, "Error", "You Must Login First")
            self.id_delete_blog_text.setText("")
            return 0
        