import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QGridLayout, QPushButton, QWidget, QLabel, QLineEdit, QMessageBox
from blogging.controller import Controller 

from blogging.exception.invalid_login_exception import InvalidLoginException
from blogging.exception.duplicate_login_exception import DuplicateLoginException
from blogging.exception.non_matching_password_exception import NonMatchingPasswords
from blogging.exception.username_in_use_exception import UsernameInUse

class LoginGUI:
    def __init__(self, controller):
        self.controller = controller

        self.login_layout = QGridLayout()
        
        #setting variables for login
        self.create_account_btn_main = QPushButton("Create an Account")
        self.username_label = QLabel("Username")
        self.quit_btn = QPushButton("Quit")
        self.login_btn = QPushButton("Log in")
        self.password_label = QLabel("Password")
        self.username_text = QLineEdit()
        self.password_text = QLineEdit()
        
        #add to login_layout
        self.login_layout.addWidget(self.create_account_btn_main, 0, 0)
        self.login_layout.addWidget(self.username_label, 1,0)
        self.login_layout.addWidget(self.username_text, 1,1)
        self.login_layout.addWidget(self.password_label , 2, 0)
        self.login_layout.addWidget(self.password_text, 2,1)
        self.login_layout.addWidget(self.login_btn, 3,1)
        self.login_layout.addWidget(self.quit_btn, 3, 0)
    
        self.login_widget = QWidget()
        self.login_widget.setLayout(self.login_layout)


        # create account layout
        self.create_acc_layout = QGridLayout()

        self.add_username_label = QLabel("Username")
        self.add_username_text = QLineEdit()
        self.add_pass_label = QLabel("Password")
        self.add_pass_text = QLineEdit()
        self.confirm_pass_label = QLabel("Confirm Password")
        self.confirm_pass_text = QLineEdit()
        self.create_account_btn = QPushButton("Create Account")
        self.go_back_btn8 = QPushButton("Go Back to Login")

        self.create_acc_layout.addWidget(self.add_username_label, 0, 0)
        self.create_acc_layout.addWidget(self.add_username_text, 0, 1)
        self.create_acc_layout.addWidget(self.add_pass_label, 1, 0)
        self.create_acc_layout.addWidget(self.add_pass_text, 1, 1)
        self.create_acc_layout.addWidget(self.confirm_pass_label, 2, 0)
        self.create_acc_layout.addWidget(self.confirm_pass_text, 2, 1)
        self.create_acc_layout.addWidget(self.create_account_btn, 3, 1)
        self.create_acc_layout.addWidget(self.go_back_btn8, 3, 0)

        self.create_acc_widget = QWidget()
        self.create_acc_widget.setLayout(self.create_acc_layout)

    #call login controller with input user and password 
    def login_btn_clicked(self): 
        username = self.username_text.text()
        password = self.password_text.text()
        
        try:
            if all([username, password]):
                if self.controller.login(username, password): 
                    return 1
            else:
                QMessageBox.warning(None, "Error", "You Must Fill All Fields")
                return 0

        except InvalidLoginException: 
            QMessageBox.warning(None, "Login Error", "Not logged in correctly")
            self.clear_login()
            return 0

        except DuplicateLoginException:
            QMessageBox.warning(None, "Login Error", "Cannot Login While Logged In")
            self.clear_login()
            
    def create_account_btn_clicked(self):
        username = self.add_username_text.text()
        pass1 = self.add_pass_text.text()
        pass2 = self.confirm_pass_text.text()

        if all([username, pass1,pass2]):
            try:
                if self.controller.create_account(username, pass1, pass2):
                    self.add_username_text.setText("")
                    self.add_pass_text.setText("")
                    self.confirm_pass_text.setText("")
                    return 0

            except NonMatchingPasswords:
                QMessageBox.warning(None, "Error", "Passwords Do Not Match")
                self.add_pass_text.setText("")
                self.confirm_pass_text.setText("")
                return 15

            except UsernameInUse:
                QMessageBox.warning(None, "Error", "Username In Use")
                return 15
            
        else:
            QMessageBox.warning(None, "Error", "You Must Fill All Fields")
            return 15
    
    #clear text boxes
    def clear_login(self):
        self.username_text.setText("")
        self.password_text.setText("")
        