import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QGridLayout, QPushButton, QWidget, QLabel, QLineEdit, QMessageBox, QPlainTextEdit
from blogging.controller import Controller 

class SearchBlogGUI:
    def __init__(self, controller):
        self.controller = controller

        # search blog layout
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

    #search blog 
    def search_b_btn_clicked(self):
        self.search_results.clear()

        id = self.search_text.text()
        blog = self.controller.search_blog(id)

        if all([id]):

            if blog is not None: 
                self.search_results.appendPlainText(str(blog))
                self.search_text.setText("")
            else: 
                QMessageBox.warning(None, "Search Error", "Blog Does Not Exist")
                self.search_text.setText("")
        else:
            QMessageBox.warning(None, "Error", "Please Enter A Blog ID")
        