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
        self.create_blog_btn_main = QPushButton("Create New Blog")
        self.search_blog_btn_main = QPushButton("Search for a Blog by ID")
        self.retrieve_blog_btn_main = QPushButton("Retrieve Blogs by Name")
        self.update_blog_btn_main = QPushButton("Update a Blog")
        self.delete_blog_btn_main = QPushButton("Delete a Blog")
        self.list_all_blogs_btn_main = QPushButton("List All Blogs")
        self.edit_blog_btn_main = QPushButton("Edit the Posts In a Blog")
        self.logout_btn_main = QPushButton("Logout")

        self.main_menu_layout.addWidget(self.main_menu_label, 0,0)
        self.main_menu_layout.addWidget(self.create_blog_btn_main, 1,0)
        self.main_menu_layout.addWidget(self.search_blog_btn_main, 2,0)
        self.main_menu_layout.addWidget(self.retrieve_blog_btn_main, 3,0)
        self.main_menu_layout.addWidget(self.update_blog_btn_main, 4,0)
        self.main_menu_layout.addWidget(self.delete_blog_btn_main, 5,0)
        self.main_menu_layout.addWidget(self.list_all_blogs_btn_main, 6,0)
        self.main_menu_layout.addWidget(self.edit_blog_btn_main, 7,0)
        self.main_menu_layout.addWidget(self.logout_btn_main, 8,0)

        #listing blogs
        self.list_blogs_layout = QGridLayout()
        self.list_blog_text_box = QPlainTextEdit()
        self.list_blogs_label = QLabel("List of All Blogs")
        self.go_back_btn2 = QPushButton("Go Back to Main Menu")

        self.list_blogs_layout.addWidget(self.list_blogs_label, 0,0)
        self.list_blogs_layout.addWidget(self.list_blog_text_box, 1,0)
        self.list_blogs_layout.addWidget(self.go_back_btn2, 2, 0)
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
        self.go_back_btn1 = QPushButton("Go Back to Main Menu")
        
        self.create_blog_layout.addWidget(self.id_label, 0,0)
        self.create_blog_layout.addWidget(self.id_text, 0,1)
        self.create_blog_layout.addWidget(self.name_label, 1,0)
        self.create_blog_layout.addWidget(self.name_text, 1,1)
        self.create_blog_layout.addWidget(self.url_label, 2,0)
        self.create_blog_layout.addWidget(self.url_text, 2,1)
        self.create_blog_layout.addWidget(self.email_label, 3,0)
        self.create_blog_layout.addWidget(self.email_text, 3,1)
        self.create_blog_layout.addWidget(self.go_back_btn1, 4,0)
        self.create_blog_layout.addWidget(self.create_new_blog_btn, 4, 1)

        #updating a blog
        self.update_blog_layout = QGridLayout()
        
        self.old_id_label = QLabel("Current ID")
        self.new_id_label = QLabel("New ID")
        self.new_name_label = QLabel("New Name")
        self.new_url_label = QLabel("New URL")
        self.new_email_label = QLabel("New Email")
        self.old_id_text = QLineEdit()
        self.new_id_text = QLineEdit()
        self.new_name_text = QLineEdit()
        self.new_url_text = QLineEdit()
        self.new_email_text = QLineEdit()
        self.update_blog_btn = QPushButton("Update")
        self.go_back_btn5 = QPushButton("Go Back to Main Menu")
        
        self.update_blog_layout.addWidget(self.old_id_label, 0,0)
        self.update_blog_layout.addWidget(self.old_id_text, 0,1)
        self.update_blog_layout.addWidget(self.new_id_label, 1,0)
        self.update_blog_layout.addWidget(self.new_id_text, 1,1)
        self.update_blog_layout.addWidget(self.new_name_label, 2,0)
        self.update_blog_layout.addWidget(self.new_name_text, 2,1)
        self.update_blog_layout.addWidget(self.new_url_label, 3,0)
        self.update_blog_layout.addWidget(self.new_url_text, 3,1)
        self.update_blog_layout.addWidget(self.new_email_label, 4,0)
        self.update_blog_layout.addWidget(self.new_email_text, 4,1)
        self.update_blog_layout.addWidget(self.go_back_btn5, 5,0)
        self.update_blog_layout.addWidget(self.update_blog_btn, 5, 1)

        # search blog
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

        # retrieve blogs by name
        self.retrieve_blogs_layout = QGridLayout()

        self.retrieve_blogs_label = QLabel("Search by Name")
        self.retrieve_blogs_text = QLineEdit()
        self.retrieve_blogs_btn = QPushButton("Retrieve")
        self.retrieved_blogs = QPlainTextEdit()
        self.go_back_btn4 = QPushButton("Go Back to Main Menu")

        self.retrieve_blogs_layout.addWidget(self.retrieve_blogs_label, 0,0)
        self.retrieve_blogs_layout.addWidget(self.retrieve_blogs_text, 0,1)
        self.retrieve_blogs_layout.addWidget(self.retrieve_blogs_btn, 0,2)
        self.retrieve_blogs_layout.addWidget(self.retrieved_blogs, 1,0)
        self.retrieve_blogs_layout.addWidget(self.go_back_btn4, 2,0)

        self.retrieved_blogs.setEnabled(False)

        # delete a blog
        self.delete_blog_layout = QGridLayout()

        self.id_delete_blog_label = QLabel("Enter the ID of the Blog")
        self.id_delete_blog_text = QLineEdit()
        self.delete_blog_btn = QPushButton("Delete")
        self.go_back_btn6 = QPushButton("Go Back to Main Menu")

        self.delete_blog_layout.addWidget(self.id_delete_blog_label, 0,0)
        self.delete_blog_layout.addWidget(self.id_delete_blog_text, 0,1)
        self.delete_blog_layout.addWidget(self.delete_blog_btn,0,2)
        self.delete_blog_layout.addWidget(self.go_back_btn6, 1,1)

        # start editing a blog, ID screen
        self.edit_blog_layout1 = QGridLayout()

        self.edit_id_label = QLabel("Enter the ID of the Blog for Editing")
        self.edit_id_text = QLineEdit()
        self.edit_blog_btn = QPushButton("Edit")
        self.go_back_btn7 = QPushButton("Go Back to Main Menu")
        
        self.edit_blog_layout1.addWidget(self.edit_id_label, 0,0)
        self.edit_blog_layout1.addWidget(self.edit_id_text, 0,1)
        self.edit_blog_layout1.addWidget(self.edit_blog_btn, 0, 2)
        self.edit_blog_layout1.addWidget(self.go_back_btn7, 1,1)

        # post menu layout

        self.post_menu_layout = QGridLayout()

        self.post_menu_label = QLabel("Please Select an Option")
        self.add_post_btn_main = QPushButton("Create New Post")
        self.retrieve_post_btn_main = QPushButton("Retrieve Posts by Name")
        self.update_post_btn_main = QPushButton("Update a Post")
        self.delete_post_btn_main = QPushButton("Delete a Post")
        self.list_all_posts_btn_main = QPushButton("List All Posts")
        self.finish_editing_btn_main = QPushButton("Finish Editing Blog's Posts")

        self.post_menu_layout.addWidget(self.post_menu_label, 0,0)
        self.post_menu_layout.addWidget(self.add_post_btn_main, 1,0)
        self.post_menu_layout.addWidget(self.retrieve_post_btn_main, 2,0)
        self.post_menu_layout.addWidget(self.update_post_btn_main, 3,0)
        self.post_menu_layout.addWidget(self.delete_post_btn_main, 4,0)
        self.post_menu_layout.addWidget(self.list_all_posts_btn_main, 5,0)
        self.post_menu_layout.addWidget(self.finish_editing_btn_main, 6,0)
        
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

        self.retrieve_blogs_widget = QWidget()
        self.retrieve_blogs_widget.setLayout(self.retrieve_blogs_layout)

        self.update_blog_widget = QWidget()
        self.update_blog_widget.setLayout(self.update_blog_layout)

        self.delete_blog_widget = QWidget()
        self.delete_blog_widget.setLayout(self.delete_blog_layout)

        self.edit_blog_widget1 = QWidget()
        self.edit_blog_widget1.setLayout(self.edit_blog_layout1)

        self.post_menu_widget = QWidget()
        self.post_menu_widget.setLayout(self.post_menu_layout)

        self.stack = QStackedWidget()
        self.stack.addWidget(self.login_widget) # 0
        self.stack.addWidget(self.main_widget) # 1
        self.stack.addWidget(self.list_blogs_widget) # 2
        self.stack.addWidget(self.create_blog_widget) # 3
        self.stack.addWidget(self.search_blog_widget) # 4
        self.stack.addWidget(self.retrieve_blogs_widget) # 5
        self.stack.addWidget(self.update_blog_widget) # 6
        self.stack.addWidget(self.delete_blog_widget) # 7
        self.stack.addWidget(self.edit_blog_widget1) # 8
        self.stack.addWidget(self.post_menu_widget) # 9

        self.setCentralWidget(self.stack)

        self.quit_btn.clicked.connect(self.quit_btn_clicked)
        self.login_btn.clicked.connect(self.login_btn_clicked)
        self.logout_btn_main.clicked.connect(self.logout_btn_clicked)
        self.list_all_blogs_btn_main.clicked.connect(self.list_all_blogs_btn_clicked)
        self.create_blog_btn_main.clicked.connect(self.create_blog_btn_clicked_main)
        self.search_blog_btn_main.clicked.connect(self.search_blog_btn_clicked_main)
        self.retrieve_blog_btn_main.clicked.connect(self.retrieve_blog_btn_clicked_main)
        self.update_blog_btn_main.clicked.connect(self.update_blog_btn_clicked_main)
        self.delete_blog_btn_main.clicked.connect(self.delete_blog_btn_clicked_main)
        self.edit_blog_btn_main.clicked.connect(self.edit_blog_btn_clicked_main)

        # go back buttons
        self.go_back_btn1.clicked.connect(self.go_back_btn_clicked)
        self.go_back_btn2.clicked.connect(self.go_back_btn_clicked)
        self.go_back_btn3.clicked.connect(self.go_back_btn_clicked)
        self.go_back_btn4.clicked.connect(self.go_back_btn_clicked)
        self.go_back_btn5.clicked.connect(self.go_back_btn_clicked)
        self.go_back_btn6.clicked.connect(self.go_back_btn_clicked)
        self.go_back_btn7.clicked.connect(self.go_back_btn_clicked)
        self.finish_editing_btn_main.clicked.connect(self.go_back_btn_clicked)

        self.stack.setCurrentIndex(0)

    def edit_blog_btn_clicked_main(self):
        self.stack.setCurrentIndex(8)
        self.edit_blog_btn.clicked.connect(self.edit_blog_btn_clicked)

    def edit_blog_btn_clicked(self):
        id = self.edit_id_text.text()

        try:
            if self.controller.set_current_blog(id) is not None:
                self.stack.setCurrentIndex(9)

        except IllegalOperationException:
            QMessageBox.warning(self, "Error", "Could Not Find Blog.")
            self.edit_id_text.setText("")

        except IllegalAccessException:
            QMessageBox.warning(self, "Error", "You Must Login First")
            self.edit_id_text.setText("")
            self.stack.setCurrentIndex(0)

    def delete_blog_btn_clicked_main(self):
        self.stack.setCurrentIndex(7)
        self.delete_blog_btn.clicked.connect(self.delete_blog_btn_clicked)

    def delete_blog_btn_clicked(self):
        blog_to_delete = self.id_delete_blog_text.text()

        try:
            if self.controller.delete_blog(blog_to_delete):
                QMessageBox.information(self, "Success", "Blog Deleted Successfully!")
                self.id_delete_blog_text.setText("")

        except IllegalOperationException:
            QMessageBox.warning(self, "Error", "Could Not Delete Blog.")
            self.id_delete_blog_text.setText("")

        except IllegalAccessException:
            QMessageBox.warning(self, "Error", "You Must Login First")
            self.id_delete_blog_text.setText("")
            self.stack.setCurrentIndex(0)

    def update_blog_btn_clicked_main(self):
        self.stack.setCurrentIndex(6)
        self.update_blog_btn.clicked.connect(self.update_blog_btn_clicked)

    def update_blog_btn_clicked(self):
        old_id = self.old_id_text.text()
        id = self.new_id_text.text()
        name = self.new_name_text.text()
        url = self.new_url_text.text()
        email = self.new_email_text.text()

        try: 
            if self.controller.update_blog(old_id, id, name, url, email): 
                QMessageBox.information(self, "Success", "Blog Updated Successfully!")
                self.clear_update()

        except IllegalOperationException: 
            QMessageBox.warning(self, "Error", "Could Not Update Blog.")
            self.clear_update()
        except IllegalAccessException:
            QMessageBox.warning(self, "Error", "You Must Login First")
            self.clear_update()
            self.stack.setCurrentIndex(0)

    def search_blog_btn_clicked_main(self): 
        self.stack.setCurrentIndex(4)
        self.search_results.clear()
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

    def retrieve_blog_btn_clicked_main(self):
        self.stack.setCurrentIndex(5)
        self.retrieved_blogs.clear()
        self.retrieve_blogs_btn.clicked.connect(self.retrieve_blog_btn_clicked)

    def retrieve_blog_btn_clicked(self):
        self.retrieved_blogs.clear()

        keyword = self.retrieve_blogs_text.text()

        blogs = self.controller.retrieve_blogs(keyword)
        try:
            if len(blogs) > 0:
                for b in blogs:
                    self.retrieved_blogs.appendPlainText(str(b))

                self.retrieve_blogs_text.setText("")
            else:
                QMessageBox.warning(None, "Error", "No matching Blogs")
                self.retrieve_blogs_text.setText("")
        except IllegalAccessException:
            QMessageBox.warning(self, "Error", "You Must Login First")
            self.stack.setCurrentIndex(0)
   
    def go_back_btn_clicked(self):
        self.stack.setCurrentIndex(1)
    
    def quit_btn_clicked(self): 
        self.close()

    def clear_update(self):
        self.old_id_text.setText("")
        self.new_id_text.setText("")
        self.new_name_text.setText("")
        self.new_url_text.setText("")
        self.new_email_text.setText("")

    def clear_login(self):
        self.username_text.setText("")
        self.password_text.setText("")

    def clear_create_blog(self):
        self.id_text.setText("")
        self.name_text.setText("")
        self.url_text.setText("")
        self.email_text.setText("")

    def create_blog_btn_clicked_main(self):
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
                self.clear_create_blog()

        except IllegalOperationException: 
            QMessageBox.warning(self, "Error", "Blog Cannot Have the Same ID as Another Blog.")
            self.clear_create_blog()

        except IllegalAccessException:
            QMessageBox.warning(self, "Error", "You Must Login First")
            self.clear_create_blog()
            self.stack.setCurrentIndex(0)

    def login_btn_clicked(self): 
        username = self.username_text.text()
        password = self.password_text.text()
        
        try: 
            success = self.controller.login(username, password)
            if success: 
                #QMessageBox.information(self, "Logged In", "Logged in correctly")
                self.stack.setCurrentIndex(1)
        except InvalidLoginException: 
            QMessageBox.warning(self, "Login Error", "Not logged in correctly")
            self.clear_login()

        except DuplicateLoginException:
            QMessageBox.warning(self, "Login Error", "Cannot Login While Logged In")
            self.clear_login()

    def logout_btn_clicked(self):
        self.controller.logout()

        self.stack.setCurrentIndex(0)
        self.clear_login()

    def list_all_blogs_btn_clicked(self):
        self.stack.setCurrentIndex(2)
        self.list_blog_text_box.clear()

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
