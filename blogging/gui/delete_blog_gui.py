import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QGridLayout, QPushButton, QWidget, QLabel, QLineEdit, QMessageBox
from blogging.controller import Controller 

from blogging.exception.illegal_access_exception import IllegalAccessException
from blogging.exception.illegal_operation_exception import IllegalOperationException

class DeleteBlogGUI:
    def __init__(self, controller):
        # delete a blog layout
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

    #delete blog when btn is clicked
    def delete_blog_btn_clicked(self):
        blog_to_delete = self.id_delete_blog_text.text()

        try:
            if all([blog_to_delete]):
                if self.controller.delete_blog(blog_to_delete):
                    QMessageBox.information(None, "Success", "Blog Deleted Successfully!")
                    self.id_delete_blog_text.setText("")
                    return 7
                
            else:
                QMessageBox.warning(None, "Error", "Please Enter An ID")
                return 7

        except IllegalOperationException:
            QMessageBox.warning(None, "Error", "Could Not Delete Blog.")
            self.id_delete_blog_text.setText("")

        except IllegalAccessException:
            QMessageBox.warning(None, "Error", "You Must Login First")
            self.id_delete_blog_text.setText("")
            return 0
        