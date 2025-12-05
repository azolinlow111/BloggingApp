from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QGridLayout, QPushButton, QWidget, QLabel, QTableView
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from blogging.controller import Controller 

from blogging.exception.illegal_access_exception import IllegalAccessException
from blogging.exception.no_current_blog_exception import NoCurrentBlogException

class ListBlogsGUI: 
    
    def __init__(self, controller):
    
        self.controller = controller 
        
        #listing blogs layout 
        self.list_blogs_layout = QGridLayout()
        self.blogs_table = QTableView()
        self.list_blogs_label = QLabel("Blogs")
        self.go_back_btn2 = QPushButton("Go Back to Main Menu")

        self.list_blogs_layout.addWidget(self.list_blogs_label, 0,0)
        self.list_blogs_layout.addWidget(self.blogs_table, 1,0)
        self.list_blogs_layout.addWidget(self.go_back_btn2, 2, 0)
        
        #Adding widget 
        self.list_blogs_widget = QWidget()
        self.list_blogs_widget.setLayout(self.list_blogs_layout)
    
    #create table and display 
    def load_table(self): 
        
        try:
            blogs = self.controller.list_blogs()
            
            table = QStandardItemModel(len(blogs), 4)
            table.setHorizontalHeaderLabels(["ID", "Name", "URL", "Email"])
            
            for row, blog, in enumerate(blogs): 
                table.setItem(row, 0, QStandardItem(str(blog.id)))
                table.setItem(row, 1, QStandardItem(blog.name))
                table.setItem(row, 2, QStandardItem(blog.url))
                table.setItem(row, 3, QStandardItem(blog.email))
            
            self.blogs_table.setModel(table) 
            self.blogs_table.resizeColumnsToContents()
            
        except (NoCurrentBlogException, IllegalAccessException):
                pass 
            
    
    