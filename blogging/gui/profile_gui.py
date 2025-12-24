from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QGridLayout, QPushButton, QWidget, QLabel, QLineEdit, QMessageBox, QPlainTextEdit
from blogging.controller import Controller 

class ProfileGUI:
    def __init__(self, controller):
        self.controller = controller

        self.profile_layout = QGridLayout()

        self.username_label = QLabel(self.controller.current_user)
        self.reset_password_btn = QPushButton("Reset Password")
        self.delete_acc_btn = QPushButton("Delete Account")
        self.go_back_btn9 = QPushButton("Go Back To Main Menu")

        self.profile_layout.addWidget(self.username_label, 0, 0)
        self.profile_layout.addWidget(self.reset_password_btn, 1, 0)
        self.profile_layout.addWidget(self.delete_acc_btn, 2, 0)
        self.profile_layout.addWidget(self.go_back_btn9, 3, 0)

        self.profile_widget = QWidget()
        self.profile_widget.setLayout(self.profile_layout)

    