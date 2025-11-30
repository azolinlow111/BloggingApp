import sys
from blogging.configuration import Configuration
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QGridLayout, QPushButton, QWidget, QLabel, QLineEdit, QMessageBox, QStackedWidget, QPlainTextEdit
from blogging.controller import Controller 

from blogging.exception.invalid_login_exception import InvalidLoginException
from blogging.exception.duplicate_login_exception import DuplicateLoginException

class BloggingGUI(QMainWindow):

    def __init__(self):
        super().__init__()
        # set autosave to True to ensure persistence is working
        self.configuration = Configuration()
        self.configuration.__class__.autosave = True
        self.controller = Controller()
        
        self.setWindowTitle("Blogging System")
        
        login_layout = QGridLayout()
        
        #setting variables for login
        self.username_label = QLabel("Username")
        self.quit_btn = QPushButton("Quit")
        self.login_btn = QPushButton("Log in")
        self.password_label = QLabel("Password")
        self.username_text = QLineEdit()
        self.password_text = QLineEdit()
        
        #add to login_layout
        login_layout.addWidget(self.username_label, 0,0)
        login_layout.addWidget(self.username_text, 0,1)
        login_layout.addWidget(self.password_label , 1, 0)
        login_layout.addWidget(self.password_text, 1,1)
        login_layout.addWidget(self.login_btn, 2,1)
        login_layout.addWidget(self.quit_btn, 2, 0)

        # add main menu layout
        self.main_menu_layout = QGridLayout()

        self.main_menu_label = QLabel("Please Select an Option")
        self.create_blog_btn = QPushButton("Create New Blog")
        self.search_blog_btn = QPushButton("Search for a Blog by ID")
        self.retrieve_blog_btn = QPushButton("Retrieve a Blog by Name")
        self.update_blog_btn = QPushButton("Update a Blog")
        self.delete_blog_btn = QPushButton("Delete a Blog")
        self.list_all_blogs_btn = QPushButton("List All Blogs")
        self.edit_blog_btn = QPushButton("Edit the Posts In a Blog")
        self.logout_btn = QPushButton("Logout")

        self.main_menu_layout.addWidget(self.main_menu_label, 0,0)
        self.main_menu_layout.addWidget(self.create_blog_btn, 1,0)
        self.main_menu_layout.addWidget(self.search_blog_btn, 2,0)
        self.main_menu_layout.addWidget(self.retrieve_blog_btn, 3,0)
        self.main_menu_layout.addWidget(self.update_blog_btn, 4,0)
        self.main_menu_layout.addWidget(self.delete_blog_btn, 5,0)
        self.main_menu_layout.addWidget(self.list_all_blogs_btn, 6,0)
        self.main_menu_layout.addWidget(self.edit_blog_btn, 7,0)
        self.main_menu_layout.addWidget(self.logout_btn, 8,0)

        #listing blogs
        self.list_blogs_layout = QGridLayout()
        self.list_blog_text_box = QPlainTextEdit()
        self.list_blogs_label = QLabel("List of All Blogs")
        self.list_blogs_layout.addWidget(self.list_blogs_label, 0,0)
        self.list_blogs_layout.addWidget(self.list_blog_text_box, 1,0)
        self.list_blog_text_box.setEnabled(False)

        # creating blogs
        self.create_blog_layout = QGridLayout()
        
        #setting variables for login
        self.id_label = QLabel("ID")
        self.name_label = QLabel("Name")
        self.url_label = QLabel("ID")
        self.email_label = QLabel("Name")
        self.username_text = QLineEdit()
        self.password_text = QLineEdit()
        
        #add to login_layout
        login_layout.addWidget(self.username_label, 0,0)
        login_layout.addWidget(self.username_text, 0,1)
        login_layout.addWidget(self.password_label , 1, 0)
        login_layout.addWidget(self.password_text, 1,1)
        login_layout.addWidget(self.login_btn, 2,1)
        login_layout.addWidget(self.quit_btn, 2, 0)

        # set widgets
        self.login_widget = QWidget()
        self.login_widget.setLayout(login_layout)

        self.main_widget = QWidget()
        self.main_widget.setLayout(self.main_menu_layout)

        self.list_blogs_widget = QWidget()
        self.list_blogs_widget.setLayout(self.list_blogs_layout)

        self.stack = QStackedWidget()
        self.stack.addWidget(self.login_widget) # 0
        self.stack.addWidget(self.main_widget) # 1
        self.stack.addWidget(self.list_blogs_widget) # 2
        self.setCentralWidget(self.stack)

        self.quit_btn.clicked.connect(self.quit_btn_clicked)
        self.login_btn.clicked.connect(self.login_btn_clicked)
        self.logout_btn.clicked.connect(self.logout_btn_clicked)
        self.list_all_blogs_btn.clicked.connect(self.list_all_blogs_btn_clicked)
        
        #self.setCentralWidget(self.login_widget)
        self.stack.setCurrentIndex(0)
    
    def quit_btn_clicked(self): 
        self.close()

    def clear_login(self):
        self.username_text.setText("")
        self.password_text.setText("")
    
    def login_btn_clicked(self): 
        username = self.username_text.text()
        password = self.password_text.text()
        
        try: 
            success = self.controller.login(username, password)
            if success: 
                #QMessageBox.information(self, "Logged In", "Logged in correctly")
                self.stack.setCurrentIndex(1)
        except (InvalidLoginException, DuplicateLoginException): 
            QMessageBox.warning(self, "Login Error", "Not logged in correctly")
            self.clear_login()

    def logout_btn_clicked(self):
        self.controller.logout()

        self.stack.setCurrentIndex(0)
        self.clear_login()

    def list_all_blogs_btn_clicked(self):
        self.stack.setCurrentIndex(2)

        blogs = self.controller.list_blogs()

        for b in blogs:
            self.list_blog_text_box.appendPlainText(str(b))

def main():
    app = QApplication(sys.argv)
    window = BloggingGUI()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()
