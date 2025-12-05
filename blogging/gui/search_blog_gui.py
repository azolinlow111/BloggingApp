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

class SearchBlogGUI:
    def __init__(self, controller):
        self.controller = controller

        # search blog
        self.search_blog_layout = QGridLayout()

        self.search_label = QLabel("Enter A ID")
        self.search_text = QLineEdit()
        self.search_b_btn = QPushButton("Search")
        self.search_results = QPlainTextEdit()
        self.go_back_btn3 = QPushButton("Go Back to Main Menu")

        self.search_blog_layout.addWidget(self.search_label, 0,0)
        self.search_blog_layout.addWidget(self.search_text, 0,1)
        self.search_blog_layout.addWidget(self.search_b_btn, 0,2)
        self.search_blog_layout.addWidget(self.search_results, 1,0)
        self.search_blog_layout.addWidget(self.go_back_btn3, 2, 0)

        self.search_results.setEnabled(False)

        self.search_blog_widget = QWidget()
        self.search_blog_widget.setLayout(self.search_blog_layout)

    def search_b_btn_clicked(self):
        self.search_results.clear()

        id = self.search_text.text()
        blog = self.controller.search_blog(id)

        if blog is not None: 
            self.search_results.appendPlainText(str(blog))
            self.search_text.setText("")
        else: 
            QMessageBox.warning(None, "Search Error", "Blog Does Not Exist")
            self.search_text.setText("")

    