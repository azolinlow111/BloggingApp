from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QGridLayout, QPushButton, QWidget, QLabel, QLineEdit, QMessageBox, QTableView
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from blogging.controller import Controller 

from blogging.exception.illegal_access_exception import IllegalAccessException

class RetrieveBlogsGUI: 
    
    def __init__(self, controller): 
        
        self.controller = controller 
        
        # retrieve blogs by name layout 
        self.retrieve_blogs_layout = QGridLayout()

        self.retrieve_blogs_label = QLabel("Search by Name")
        self.retrieve_blogs_text = QLineEdit()
        self.retrieve_blogs_btn = QPushButton("Retrieve")
        self.retrieved_blogs = QTableView()
        self.go_back_btn4 = QPushButton("Go Back to Main Menu")

        self.retrieve_blogs_layout.addWidget(self.retrieve_blogs_label, 0,0)
        self.retrieve_blogs_layout.addWidget(self.retrieve_blogs_text, 0,1)
        self.retrieve_blogs_layout.addWidget(self.retrieve_blogs_btn, 0,2)
        self.retrieve_blogs_layout.addWidget(self.retrieved_blogs, 1,0)
        self.retrieve_blogs_layout.addWidget(self.go_back_btn4, 2,0)
        

        self.retrieve_blogs_widget = QWidget()
        self.retrieve_blogs_widget.setLayout(self.retrieve_blogs_layout)
    
    #create table and display it 
    def load_table(self): 
        
        self.retrieved_blogs.setModel(None)

        keyword = self.retrieve_blogs_text.text()

        blogs = self.controller.retrieve_blogs(keyword)
        try:
            if len(blogs) > 0:
                table = QStandardItemModel(len(blogs), 4)
                
                table.setHorizontalHeaderLabels(["ID", "Name", "URL", "Email"])
                
                for row, blog, in enumerate(blogs): 
                    table.setItem(row, 0, QStandardItem(str(blog.id)))
                    table.setItem(row, 1, QStandardItem(blog.name))
                    table.setItem(row, 2, QStandardItem(blog.url))
                    table.setItem(row, 3, QStandardItem(blog.email))
                
                self.retrieved_blogs.setModel(table) 
                self.retrieved_blogs.resizeColumnsToContents()

            else:
                QMessageBox.warning(None, "Error", "No matching Blogs")
                self.retrieve_blogs_text.setText("")
                
        except IllegalAccessException:
            QMessageBox.warning(self, "Error", "You Must Login First")
            self.stack.setCurrentIndex(0)