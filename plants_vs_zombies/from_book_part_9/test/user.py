class User:
    def __init__(self,first_name,last_name,email,password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.login_attempts = 0
#形参中的参数(first_name,last_name,email,password)是用于从外部传递用户的具体信息来初始化实例的
#login_attempts是记录用户登录尝试次数的属性，是在方法内部直接设置的默认值.它不需要从外部传递,也因此没有出现在形参列表中.

    def describe_user(self):
        print(f"Name: {self.first_name.title()} {self.last_name.title()}")
        print(f"Email: {self.email}")
        print(f"Password: {self.password}")

    def greet_user(self):
        print(f"Welcome {self.first_name.title()} {self.last_name.title()}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

# We added a title() method to the first_name and last_name attributes to capitalize the first letter of each name.

#_init_()方法是一个特殊的方法，用于初始化对象的属性。它在创建对象时自动调用。我们在这里定义了四个属性：first_name、last_name、email和password。我们还定义了两个方法：describe_user()和greet_user()，用于描述用户和问候用户。最后，我们还定义了两个方法：increment_login_attempts()和reset_login_attempts()，用于增加和重置登录尝试次数。
# 我们还可以定义其他方法，如check_password()方法，用于验证用户的密码。
# 最后，我们可以创建User类的实例，并调用其方法。例如：

user1 = User("John", "Doe", "johndoe@gmail.com", "password123")
user1.describe_user()
user1.greet_user()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(user1.login_attempts)
user1.reset_login_attempts()
print(user1.login_attempts)
