import sys
from blogging.configuration import Configuration
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QGridLayout, QPushButton, QWidget, QLabel, QLineEdit, QMessageBox
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
        # Continue here with your code!
        self.setWindowTitle("Blogging System")
        
        login_layout = QGridLayout()
        
        #setting variables
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
        

        widget =  QWidget()
        widget.setLayout(login_layout)
        
        self.quit_btn.clicked.connect(self.quit_btn_clicked)
        self.login_btn.clicked.connect(self.login_btn_clicked)
        
        self.setCentralWidget(widget)
    
    def quit_btn_clicked(self): 
        self.close()
    
    def login_btn_clicked(self): 
        username = self.username_text.text()
        password = self.password_text.text()
        
        try: 
            success = self.controller.login(username, password)
            if success: 
                QMessageBox.information(self, "login", "login correctly")
        except (InvalidLoginException, DuplicateLoginException): 
            QMessageBox.warning(self, "login error", "not login correctly")
def main():
    app = QApplication(sys.argv)
    window = BloggingGUI()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()
