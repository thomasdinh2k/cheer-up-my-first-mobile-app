import glob
import random

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import json, glob
from datetime import datetime
from pathlib import Path

Builder.load_file('design.kv')  # Load the kv file


class LoginScreen(Screen):
    def sign_up(self):
        self.manager.current = 'sign_up_screen'

    def log_in(self, usr, pwd):
        with open("users.json", "r") as file:
            usr_dict = json.load(file)
        for u in usr_dict:
            if usr in usr_dict[u]["username"]:
                if pwd == usr_dict[u]["password"]:  # Correct User-name
                    print(f"User {u} Login Successful")
                    self.manager.transition.direction = 'up'
                    self.manager.current = 'after_login'
                else:
                    self.ids.login_wrong.text = 'Password Incorrect'
                    print(f"Username {usr} correct, password incorrect")
                    continue
            else:
                print("Username incorrect")
                self.ids.login_wrong.text = 'Username Incorrect'


class SignUpScreen(Screen):
    def add_user(self, full_name, usr, pwd):
        with open("users.json") as file:
            users_dict = json.load(file)
            numbers_of_users = len(users_dict)
        users_dict[f"user{numbers_of_users}"] = {'fullname': full_name, 'username': usr, 'password': pwd,
                                                 'created': datetime.now().strftime("%Y-%m-%d | %H:%M:%S")}
        print(users_dict)
        with open("users.json", "w") as file:
            json.dump(users_dict, file)
        self.manager.current = 'sign_up_successful'


class SignUpSuccessful(Screen):
    def LoginScreen(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'login_screen'


class AfterLogin(Screen):
    def get_quote(self, feel):
        feel = feel.lower()
        available_feelings = glob.glob("quotes/*txt")
        available_feelings = [Path(filename).stem for filename in available_feelings]
        print(available_feelings)

        if feel in available_feelings:
            with open(f"quotes/{feel}.txt", "r") as file:
                quotes = file.readlines()
            self.ids.quotes.text = random.choice(quotes)
        else:
            self.ids.quotes.text = f'We only support {", ".join(map(str, available_feelings))}, sorry :)'

    def log_out(self):
        self.manager.transition.direction = 'up'
        self.manager.current = 'login_screen'


class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


if __name__ == "__main__":
    MainApp().run()
