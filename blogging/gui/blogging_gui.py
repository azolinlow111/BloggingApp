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

from blogging.gui.retrieve_blog_gui import RetrieveBlogsGUI
from blogging.gui.list_all_blogs_gui import ListBlogsGUI
from blogging.gui.login_gui import LoginGUI
from blogging.gui.delete_blog_gui import DeleteBlogGUI
from blogging.gui.create_blog_gui import CreateBlogGUI
from blogging.gui.search_blog_gui import SearchBlogGUI
from blogging.gui.update_blog_gui import UpdateBlogGUI

class BloggingGUI(QMainWindow):

    def __init__(self):
        super().__init__()
        # set autosave to True to ensure persistence is working
        self.configuration = Configuration()
        self.configuration.__class__.autosave = True
        self.controller = Controller()
        
        self.retrieve_blogs_gui = RetrieveBlogsGUI(self.controller)
        self.list_blogs_gui = ListBlogsGUI(self.controller)
        self.login_gui = LoginGUI(self.controller)
        self.delete_blog_gui = DeleteBlogGUI(self.controller)
        self.create_blog_gui = CreateBlogGUI(self.controller)
        self.search_blog_gui = SearchBlogGUI(self.controller)
        self.update_blog_gui = UpdateBlogGUI(self.controller)
        self.add_post_gui = AddPostGUI(self.controller)
        self.delete_post_gui = DeletePostGUI(self.controller)
        self.retrieve_post_gui = RetrievePostGUI(self.controller)
        self.update_post_gui = UpdatePostGUI(self.controller)
        self.list_posts_gui = ListPostGUI(self.controller)
        
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

        self.edit_blog_widget1 = QWidget()
        self.edit_blog_widget1.setLayout(self.edit_blog_layout1)

        self.post_menu_widget = QWidget()
        self.post_menu_widget.setLayout(self.post_menu_layout)
   
        self.stack = QStackedWidget()
        self.stack.addWidget(self.login_gui.login_widget) # 0
        self.stack.addWidget(self.main_widget) # 1

        self.stack.addWidget(self.list_blogs_gui.list_blogs_widget) # 2
        self.stack.addWidget(self.create_blog_gui.create_blog_widget) # 3
        self.stack.addWidget(self.search_blog_gui.search_blog_widget) # 4

        self.stack.addWidget(self.retrieve_blogs_gui.retrieve_blogs_widget) # 5
        self.stack.addWidget(self.update_blog_gui.update_blog_widget) # 6
        self.stack.addWidget(self.delete_blog_gui.delete_blog_widget) # 7
        self.stack.addWidget(self.edit_blog_widget1) # 8
        self.stack.addWidget(self.post_menu_widget) # 9
        self.stack.addWidget(self.add_post_gui.add_post_widget) #10
        self.stack.addWidget(self.retrieve_post_gui.retrieve_post_widget) #11
        self.stack.addWidget(self.update_post_gui.update_post_widget) #12
        self.stack.addWidget(self.delete_post_gui.delete_post_widget) #13
        self.stack.addWidget(self.list_posts_gui.list_posts_widget) #14

        self.setCentralWidget(self.stack)

        self.login_gui.quit_btn.clicked.connect(self.quit_btn_clicked)
        self.login_gui.login_btn.clicked.connect(self.login_btn_clicked)
        self.logout_btn_main.clicked.connect(self.logout_btn_clicked)
        self.list_all_blogs_btn_main.clicked.connect(self.list_all_blogs_btn_clicked)
        self.create_blog_btn_main.clicked.connect(self.create_blog_btn_clicked_main)
        self.search_blog_btn_main.clicked.connect(self.search_blog_btn_clicked_main)
        self.retrieve_blog_btn_main.clicked.connect(self.retrieve_blog_btn_clicked_main)
        self.retrieve_blogs_gui.retrieve_blogs_btn.clicked.connect(self.retrieve_blogs_gui.load_table)
        
        self.update_blog_btn_main.clicked.connect(self.update_blog_btn_clicked_main)
        self.delete_blog_btn_main.clicked.connect(self.delete_blog_btn_clicked_main)
        self.edit_blog_btn_main.clicked.connect(self.edit_blog_btn_clicked_main)
        
        self.add_post_btn_main.clicked.connect(lambda: self.post_menu_btn_clicked(10))
        self.add_post_gui.add_post_btn.clicked.connect(self.add_post_gui.add_post_btn_clicked)
        self.retrieve_post_btn_main.clicked.connect(lambda: self.post_menu_btn_clicked(11))
        self.retrieve_post_gui.retrieve_post_btn.clicked.connect(self.retrieve_post_gui.retrieve_post_btn_clicked)
        self.update_post_btn_main.clicked.connect(lambda: self.post_menu_btn_clicked(12))
        self.update_post_gui.update_post_btn.clicked.connect(self.update_post_gui.update_post_btn_clicked)
        self.delete_post_btn_main.clicked.connect(lambda: self.post_menu_btn_clicked(13))
        self.delete_post_gui.delete_post_btn.clicked.connect(self.delete_post_gui.delete_post_btn_clicked)
        self.list_all_posts_btn_main.clicked.connect(self.list_posts_btn_clicked)

        # go back buttons

        self.create_blog_gui.go_back_btn1.clicked.connect(self.go_back_btn_clicked)
        self.list_blogs_gui.go_back_btn2.clicked.connect(self.go_back_btn_clicked)
        self.list_blogs_gui.go_back_btn2.clicked.connect(self.go_back_btn_clicked)
        self.search_blog_gui.go_back_btn3.clicked.connect(self.go_back_btn_clicked)

        self.retrieve_blogs_gui.go_back_btn4.clicked.connect(self.go_back_btn_clicked)
        self.update_blog_gui.go_back_btn5.clicked.connect(self.go_back_btn_clicked)
        self.delete_blog_gui.go_back_btn6.clicked.connect(self.go_back_btn_clicked)
        self.go_back_btn7.clicked.connect(self.go_back_btn_clicked)
        self.finish_editing_btn_main.clicked.connect(self.go_back_btn_clicked)
        
        self.add_post_gui.go_back_btn_posts1.clicked.connect(self.go_back_btn_posts_clicked)
        self.retrieve_post_gui.go_back_btn_posts2.clicked.connect(self.go_back_btn_posts_clicked)
        self.update_post_gui.go_back_btn_posts3.clicked.connect(self.go_back_btn_posts_clicked)
        self.delete_post_gui.go_back_btn_posts4.clicked.connect(self.go_back_btn_posts_clicked)
        self.list_posts_gui.go_back_btn_posts5.clicked.connect(self.go_back_btn_posts_clicked)
        
        self.stack.setCurrentIndex(0)

#----- LOGIN/LOGOUT ----
    def login_btn_clicked(self): 
        i = self.login_gui.login_btn_clicked()

        self.stack.setCurrentIndex(i)

    def logout_btn_clicked(self):
        self.controller.logout()
        self.login_gui.clear_login()
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

    def update_blog_btn_clicked_main(self):
        self.stack.setCurrentIndex(6)
        self.update_blog_gui.update_blog_btn.clicked.connect(self.update_blog_gui.update_blog_btn_clicked)

    def update_blog_btn_clicked(self):
        i = self.update_blog_gui.update_blog_btn_clicked()

        self.stack.setCurrentIndex(i)

    def search_blog_btn_clicked_main(self): 
        self.stack.setCurrentIndex(4)
        self.search_blog_gui.search_results.clear()
        self.search_blog_gui.search_b_btn.clicked.connect(self.search_blog_gui.search_b_btn_clicked)

    def retrieve_blog_btn_clicked_main(self):
        self.stack.setCurrentIndex(5)
        self.retrieve_blogs_gui.retrieved_blogs.setModel(None)
        self.retrieve_blogs_gui.retrieve_blogs_text.clear()
        
   
    def go_back_btn_clicked(self):
        self.stack.setCurrentIndex(1)
    
    def delete_blog_btn_clicked_main(self):
        self.stack.setCurrentIndex(7)
        self.delete_blog_gui.delete_blog_btn.clicked.connect(self.delete_blog_gui.delete_blog_btn_clicked)

    def delete_blog_btn_clicked(self):
        i = self.delete_blog_gui.delete_blog_btn_clicked()

        self.stack.setCurrentIndex(i)

    def create_blog_btn_clicked_main(self):
        self.stack.setCurrentIndex(3)
        self.create_blog_gui.create_new_blog_btn.clicked.connect(self.create_new_blog_btn_clicked)
    
    def create_new_blog_btn_clicked(self):
        i = self.create_blog_gui.create_new_blog_btn_clicked()
        self.stack.setCurrentIndex(i)

    def list_all_blogs_btn_clicked(self):
        self.stack.setCurrentIndex(2)
        self.list_blogs_gui.load_table()
  
  # ----- POST FUNCTIONS -----
  
    #changes layout to index
    def post_menu_btn_clicked(self, index): 
        self.stack.setCurrentIndex(index)

    #go back to post editing options
    def go_back_btn_posts_clicked(self): 
        self.stack.setCurrentIndex(9)
        
    #list posts 
    def list_posts_btn_clicked(self): 
        
        self.stack.setCurrentIndex(14)

def main():
    app = QApplication(sys.argv)
    window = BloggingGUI()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()
