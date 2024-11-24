class UserList:
    def __init__(self, filename):
        self.filename = filename
        self.users = self.read_user_file()

    def read_user_file(self):
        users = []
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    username, password = line.strip().split(',')
                    users.append({'username': username, 'password': password})
        except FileNotFoundError:
            print("Password file not found. Starting with an empty user list.")
        return users

    def find_username(self, username):
        for index, user in enumerate(self.users):
            if user['username'] == username:
                return index
        return -1

    def strength(self, password):
        score = 0
        if len(password) >= 8:
            score += 1
        if any(c.isupper() for c in password):
            score += 1
        if any(c.islower() for c in password):
            score += 1
        if any(c.isdigit() for c in password):
            score += 1
        if any(c in "~!@#$%^&*()_+|-={}[]:;<>?/" for c in password):
            score += 1
        return score

    def add_user(self, username, password):
        if self.find_username(username) == -1:
            self.users.append({'username': username, 'password': password})

    def delete_user(self, username):
        index = self.find_username(username)
        if index != -1:
            del self.users[index]

    def change_password(self, username, password):
        index = self.find_username(username)
        if index != -1:
            self.users[index]['password'] = password

    def display_user_list(self):
        if not self.users:
            print("No users found.")
            return
        print(f"{'Username':<15}{'Password'}")
        print(f"{'-' * 15}{'-' * 8}")
        for user in self.users:
            print(f"{user['username']:<15}{user['password']}")

    def write_user_file(self):
        with open(self.filename, 'w') as file:
            for user in self.users:
                file.write(f"{user['username']},{user['password']}\n")

def main():
    user_list = UserList('finalprojectpassword.txt')

    while True:
        print("\nMenu:")
        print("1) Add a New User")
        print("2) Delete an Existing User")
        print("3) Change Password on an Existing User")
        print("4) Display All Users")
        print("5) Save Changes to File")
        print("6) Quit")

        selection = input("Enter Selection: ")
        
        if selection == '1':
            username = input("Enter a new user ID: ")
            if user_list.find_username(username) != -1:
                print("Username Already Exists")
                continue
            
            while True:
                password = input("Enter a password: ")
                score = user_list.strength(password)
                if score < 5:
                    print(f"This password is weak - {score}. Try again.")
                else:
                    user_list.add_user(username, password)
                    print("User Added")
                    break
        
        elif selection == '2':
            username = input("Enter user ID to delete: ")
            if user_list.find_username(username) == -1:
                print("Username Not Found")
            else:
                user_list.delete_user(username)
                print("User Deleted")
        
        elif selection == '3':
            username = input("Enter user ID to change password: ")
            if user_list.find_username(username) == -1:
                print("Username Not Found")
            else:
                while True:
                    password = input("Enter a new password: ")
                    score = user_list.strength(password)
                    if score < 5:
                        print(f"This password is weak - {score}. Try again.")
                    else:
                        user_list.change_password(username, password)
                        print("Password Changed")
                        break
        
        elif selection == '4':
            user_list.display_user_list()
        
        elif selection == '5':
            user_list.write_user_file()
            print("Changes Saved")
        
        elif selection == '6':
            print("Exiting program.")
            break
        
        else:
            print("Invalid Selection")

if __name__ == "__main__":
    main()