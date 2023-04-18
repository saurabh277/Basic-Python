class User:
    # init constructor
    #sets initial value of class attribute whenever we create specific nobject

    def __init__(self, email, name, password, current_job_title):
         self.email = email
         self.name = name
         self.password = password
         self.current_job_title = current_job_title

    def change_password(self, new_password ):
        self.password = new_password

    def change_job_title(self, new_title):
        self.current_job_title = new_title

    def user_info(self):
        print(f"User {self.name} currently works as a {self.current_job_title} . You can contact them at {self.email}")

