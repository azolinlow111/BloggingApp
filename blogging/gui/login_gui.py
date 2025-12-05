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


class LoginGUI:
    def __init__(self, controller):
        self.controller = controller

        self.login_layout = QGridLayout()
        
        #setting variables for login
        self.username_label = QLabel("Username")
        self.quit_btn = QPushButton("Quit")
        self.login_btn = QPushButton("Log in")
        self.password_label = QLabel("Password")
        self.username_text = QLineEdit()
        self.password_text = QLineEdit()
        
        #add to login_layout
        self.login_layout.addWidget(self.username_label, 0,0)
        self.login_layout.addWidget(self.username_text, 0,1)
        self.login_layout.addWidget(self.password_label , 1, 0)
        self.login_layout.addWidget(self.password_text, 1,1)
        self.login_layout.addWidget(self.login_btn, 2,1)
        self.login_layout.addWidget(self.quit_btn, 2, 0)

        self.login_widget = QWidget()
        self.login_widget.setLayout(self.login_layout)


    def login_btn_clicked(self): 
        username = self.username_text.text()
        password = self.password_text.text()
        
        try: 
            success = self.controller.login(username, password)
            if success: 
                return 1
        except InvalidLoginException: 
            QMessageBox.warning(None, "Login Error", "Not logged in correctly")
            self.clear_login()

        except DuplicateLoginException:
            QMessageBox.warning(None, "Login Error", "Cannot Login While Logged In")
            self.clear_login()

    def clear_login(self):
        self.username_text.setText("")
        self.password_text.setText("")

    

def main():
    app = QApplication(sys.argv)
    window = LoginGUI()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()