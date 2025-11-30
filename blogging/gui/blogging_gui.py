import sys
from blogging.configuration import Configuration
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QGridLayout, QPushButton, QWidget, QLabel, QLineEdit, QMessageBox, QStackedWidget, QPlainTextEdit
from blogging.controller import Controller 

from blogging.exception.invalid_login_exception import InvalidLoginException
from blogging.exception.duplicate_login_exception import DuplicateLoginException
from blogging.exception.illegal_operation_exception import IllegalOperationException
from blogging.exception.illegal_access_exception import IllegalAccessException

class BloggingGUI(QMainWindow):

    def __init__(self):
        super().__init__()
        # set autosave to True to ensure persistence is working
        self.configuration = Configuration()
        self.configuration.__class__.autosave = True
        self.controller = Controller()

        self.setWindowTitle("Blogging System")

        self.go_back_btn = QPushButton("Go Back to Main Menu")
        
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
        
        self.id_label = QLabel("ID")
        self.name_label = QLabel("Name")
        self.url_label = QLabel("URL")
        self.email_label = QLabel("Email")
        self.id_text = QLineEdit()
        self.name_text = QLineEdit()
        self.url_text = QLineEdit()
        self.email_text = QLineEdit()
        self.create_new_blog_btn = QPushButton("Create")
        
        self.create_blog_layout.addWidget(self.id_label, 0,0)
        self.create_blog_layout.addWidget(self.id_text, 0,1)
        self.create_blog_layout.addWidget(self.name_label, 1,0)
        self.create_blog_layout.addWidget(self.name_text, 1,1)
        self.create_blog_layout.addWidget(self.url_label, 2,0)
        self.create_blog_layout.addWidget(self.url_text, 2,1)
        self.create_blog_layout.addWidget(self.email_label, 3,0)
        self.create_blog_layout.addWidget(self.email_text, 3,1)
        self.create_blog_layout.addWidget(self.go_back_btn, 4,0)
        self.create_blog_layout.addWidget(self.create_new_blog_btn, 4, 1)

        # search blog
        self.search_blog_layout = QGridLayout()

        self.search_label = QLabel("Enter A ID")
        self.search_text = QLineEdit()
        self.search_b_btn = QPushButton("Search")
        self.search_results = QPlainTextEdit()

        self.search_blog_layout.addWidget(self.search_label, 0,0)
        self.search_blog_layout.addWidget(self.search_text, 0,1)
        self.search_blog_layout.addWidget(self.search_b_btn, 0,2)
        self.search_blog_layout.addWidget(self.search_results, 1,0)

        self.search_results.setEnabled(False)

        # set widgets
        self.login_widget = QWidget()
        self.login_widget.setLayout(login_layout)

        self.main_widget = QWidget()
        self.main_widget.setLayout(self.main_menu_layout)

        self.list_blogs_widget = QWidget()
        self.list_blogs_widget.setLayout(self.list_blogs_layout)

        self.create_blog_widget = QWidget()
        self.create_blog_widget.setLayout(self.create_blog_layout)

        self.search_blog_widget = QWidget()
        self.search_blog_widget.setLayout(self.search_blog_layout)

        self.stack = QStackedWidget()
        self.stack.addWidget(self.login_widget) # 0
        self.stack.addWidget(self.main_widget) # 1
        self.stack.addWidget(self.list_blogs_widget) # 2
        self.stack.addWidget(self.create_blog_widget) # 3
        self.stack.addWidget(self.search_blog_widget) #4

        self.setCentralWidget(self.stack)

        self.quit_btn.clicked.connect(self.quit_btn_clicked)
        self.login_btn.clicked.connect(self.login_btn_clicked)
        self.logout_btn.clicked.connect(self.logout_btn_clicked)
        self.list_all_blogs_btn.clicked.connect(self.list_all_blogs_btn_clicked)
        self.go_back_btn.clicked.connect(self.go_back_btn_clicked)
        self.create_blog_btn.clicked.connect(self.create_blog_btn_clicked)
        self.search_blog_btn.clicked.connect(self.search_blog_btn_clicked)

        #self.setCentralWidget(self.login_widget)
        self.stack.setCurrentIndex(0)

    def search_blog_btn_clicked(self): 
        self.stack.setCurrentIndex(4)
        self.search_b_btn.clicked.connect(self.search_b_btn_clicked)

    def search_b_btn_clicked(self):
        self.search_results.clear()

        id = self.search_text.text()
        blog = self.controller.search_blog(id)

        if blog is not None: 
            self.search_results.appendPlainText(str(blog))
            self.search_text.setText("")
        else: 
            QMessageBox.warning(self, "Search Error", "Blog Does Not Exist")
            self.search_text.setText("")

    def go_back_btn_clicked(self):
        self.stack.setCurrentIndex(1)
    
    def quit_btn_clicked(self): 
        self.close()

    def clear_login(self):
        self.username_text.setText("")
        self.password_text.setText("")

    def create_blog_btn_clicked(self):
        self.stack.setCurrentIndex(3)
        self.create_new_blog_btn.clicked.connect(self.create_new_blog_btn_clicked)
    
    def create_new_blog_btn_clicked(self):
        id = self.id_text.text()
        name = self.name_text.text()
        url = self.url_text.text()
        email = self.email_text.text()

        try: 
            if self.controller.create_blog(id, name, url, email): 
                QMessageBox.information(self, "Success", "Blog Created Successfully!")
                self.id_text.setText("")
                self.name_text.setText("")
                self.url_text.setText("")
                self.email_text.setText("")

        except (IllegalAccessException, IllegalOperationException): 
            QMessageBox.warning(self, "Error", "Blog Cannot Have the Same ID as Another Blog.")
            self.id_text.setText("")
            self.name_text.setText("")
            self.url_text.setText("")
            self.email_text.setText("")

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
