from classes.user import User
from classes.post import Post

usera = User("soonu@gmail.com","saurabh","jabwemet","sde")
usera.user_info()
usera.change_job_title("data analyst")
usera.user_info()

first_post = Post("on a secret mission today",usera.name)
first_post.get_post_info()