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


from blogging.gui.post_gui import PostGUI
from blogging.gui.login_gui import LoginGUI
from blogging.gui.delete_blog_gui import DeleteBlogGUI

class BloggingGUI(QMainWindow):

    def __init__(self):
        super().__init__()
        # set autosave to True to ensure persistence is working
        self.configuration = Configuration()
        self.configuration.__class__.autosave = True
        self.controller = Controller()
        
        self.login_gui = LoginGUI(self.controller)
        self.post_gui = PostGUI(self.controller)
        self.delete_blog_gui = DeleteBlogGUI(self.controller)
        
        self.setWindowTitle("Blogging System")

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

        self.edit_blog_widget1 = QWidget()
        self.edit_blog_widget1.setLayout(self.edit_blog_layout1)

        self.post_menu_widget = QWidget()
        self.post_menu_widget.setLayout(self.post_menu_layout)
    
   
        self.stack = QStackedWidget()
        self.stack.addWidget(self.login_gui.login_widget) # 0
        self.stack.addWidget(self.main_widget) # 1
        self.stack.addWidget(self.list_blogs_widget) # 2
        self.stack.addWidget(self.create_blog_widget) # 3
        self.stack.addWidget(self.search_blog_widget) # 4
        self.stack.addWidget(self.retrieve_blogs_widget) # 5
        self.stack.addWidget(self.update_blog_widget) # 6
        self.stack.addWidget(self.delete_blog_gui.delete_blog_widget) # 7
        self.stack.addWidget(self.edit_blog_widget1) # 8
        self.stack.addWidget(self.post_menu_widget) # 9
        self.stack.addWidget(self.post_gui.add_post_widget) #10
        self.stack.addWidget(self.post_gui.retrieve_post_widget) #11
        self.stack.addWidget(self.post_gui.update_post_widget) #12
        self.stack.addWidget(self.post_gui.delete_post_widget) #13
        self.stack.addWidget(self.post_gui.list_posts_widget) #14

        self.setCentralWidget(self.stack)

        self.login_gui.quit_btn.clicked.connect(self.quit_btn_clicked)
        self.login_gui.login_btn.clicked.connect(self.login_btn_clicked)
        self.logout_btn_main.clicked.connect(self.logout_btn_clicked)
        self.list_all_blogs_btn_main.clicked.connect(self.list_all_blogs_btn_clicked)
        self.create_blog_btn_main.clicked.connect(self.create_blog_btn_clicked_main)
        self.search_blog_btn_main.clicked.connect(self.search_blog_btn_clicked_main)
        self.retrieve_blog_btn_main.clicked.connect(self.retrieve_blog_btn_clicked_main)
        self.update_blog_btn_main.clicked.connect(self.update_blog_btn_clicked_main)
        self.delete_blog_btn_main.clicked.connect(self.delete_blog_btn_clicked_main)
        self.edit_blog_btn_main.clicked.connect(self.edit_blog_btn_clicked_main)
        
        self.add_post_btn_main.clicked.connect(lambda: self.post_menu_btn_clicked(10))
        self.post_gui.add_post_btn.clicked.connect(self.post_gui.add_post_btn_clicked)
        self.retrieve_post_btn_main.clicked.connect(lambda: self.post_menu_btn_clicked(11))
        self.post_gui.retrieve_post_btn.clicked.connect(self.post_gui.retrieve_post_btn_clicked)
        self.update_post_btn_main.clicked.connect(lambda: self.post_menu_btn_clicked(12))
        self.post_gui.update_post_btn.clicked.connect(self.post_gui.update_post_btn_clicked)
        self.delete_post_btn_main.clicked.connect(lambda: self.post_menu_btn_clicked(13))
        self.post_gui.delete_post_btn.clicked.connect(self.post_gui.delete_post_btn_clicked)
        self.list_all_posts_btn_main.clicked.connect(self.list_posts_btn_clicked)

        # go back buttons
        self.go_back_btn1.clicked.connect(self.go_back_btn_clicked)
        self.go_back_btn2.clicked.connect(self.go_back_btn_clicked)
        self.go_back_btn3.clicked.connect(self.go_back_btn_clicked)
        self.go_back_btn4.clicked.connect(self.go_back_btn_clicked)
        self.go_back_btn5.clicked.connect(self.go_back_btn_clicked)
        self.delete_blog_gui.go_back_btn6.clicked.connect(self.go_back_btn_clicked)
        self.go_back_btn7.clicked.connect(self.go_back_btn_clicked)
        self.finish_editing_btn_main.clicked.connect(self.go_back_btn_clicked)
        
        self.post_gui.go_back_btn_posts1.clicked.connect(self.go_back_btn_posts_clicked)
        self.post_gui.go_back_btn_posts2.clicked.connect(self.go_back_btn_posts_clicked)
        self.post_gui.go_back_btn_posts3.clicked.connect(self.go_back_btn_posts_clicked)
        self.post_gui.go_back_btn_posts4.clicked.connect(self.go_back_btn_posts_clicked)
        self.post_gui.go_back_btn_posts5.clicked.connect(self.go_back_btn_posts_clicked)
        
        self.stack.setCurrentIndex(0)

#----- LOGIN/LOGOUT ----
    def login_btn_clicked(self): 
        i = self.login_gui.login_btn_clicked()

        self.stack.setCurrentIndex(i)

    def logout_btn_clicked(self):
        self.controller.logout()

        self.clear_login()
        self.stack.setCurrentIndex(0)

    def quit_btn_clicked(self): 
        self.close()

#---- BLOG FUNCTIONS ------ 

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
        
        self.edit_id_text.clear()

    def delete_blog_btn_clicked_main(self):
        self.stack.setCurrentIndex(7)
        self.delete_blog_gui.delete_blog_btn.clicked.connect(self.delete_blog_gui.delete_blog_btn_clicked)

    def delete_blog_btn_clicked(self):
        i = self.delete_blog_gui.delete_blog_btn_clicked()

        self.stack.setCurrentIndex(i)

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
    
    

    def clear_update(self):
        self.old_id_text.setText("")
        self.new_id_text.setText("")
        self.new_name_text.setText("")
        self.new_url_text.setText("")
        self.new_email_text.setText("")

    

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

    def list_all_blogs_btn_clicked(self):
        self.stack.setCurrentIndex(2)
        self.list_blog_text_box.clear()

        blogs = self.controller.list_blogs()

        for b in blogs:
            self.list_blog_text_box.appendPlainText(str(b))
  
  # ----- POST FUNCTIONS -----
  
    #changes layout to index
    def post_menu_btn_clicked(self, index): 
        self.stack.setCurrentIndex(index)

    #go back to post editing options
    def go_back_btn_posts_clicked(self): 
        self.stack.setCurrentIndex(9)
        
        #list posts 
    def list_posts_btn_clicked(self): 
  
        self.post_gui.list_posts.clear()
        self.stack.setCurrentIndex(14)
        try: 
            posts = self.controller.list_posts()
            for post in posts: 
                self.post_gui.list_posts.appendPlainText(str(post))
        except (NoCurrentBlogException, IllegalAccessException):
            pass
            
        

def main():
    app = QApplication(sys.argv)
    window = BloggingGUI()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()
