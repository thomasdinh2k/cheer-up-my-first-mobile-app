# A Simple Login App using Kivy
## This is a simple login app built using Kivy, a Python framework for building user interfaces. 
The app has two screens, one for logging in and another for signing up.

The user is required to provide a username and password to log in. Upon successful login, the user is taken to a third screen that displays a quote based on the user's mood. The quote is fetched from a text file based on the mood selected by the user.
## Installation
To run this app, you need to have Python 3 installed on your machine. You also need to install Kivy. To install Kivy, run the following command:

```
pip install kivy
```

## Running the App
To run the app, navigate to the directory containing the main.py file and run the following command:

```
python main.py
```
# How the Code Works
The `main.py` file contains the main code for the app. It imports the necessary modules and defines four classes: `LoginScreen`, `SignUpScreen`, `SignUpSuccessful`, and `AfterLogin`.

The `LoginScreen` class handles the login process. It reads the user information from a JSON file named `users.json` and checks if the entered username and password match any of the existing user accounts. If the login is successful, the user is taken to the `AfterLogin` screen. If the login fails, an error message is displayed on the `LoginScreen`.

The `SignUpScreen` class handles the sign-up process. It allows the user to enter their full name, username, and password. The entered data is stored in the `users.json` file along with a timestamp indicating the time the account was created. Upon successful sign-up, the user is taken to the `SignUpSuccessful` screen.

The `SignUpSuccessful` class simply provides a button that allows the user to return to the `LoginScreen`.

The `AfterLogin` class displays a text box that shows a quote based on the user's selected mood. The user can select their mood from a dropdown menu. The available moods are determined by the text files stored in the `quotes/` directory. If the selected mood is not available, an error message is displayed. The user can also log out by clicking a button.

The `RootWidget` class is used to manage the different screens of the app. The `MainApp` class is the main application class that runs the app.

The `design.kv` file contains the Kivy language code that defines the layout and style of the app screen

# Conclusion
This simple app demonstrates how to build a login app using Kivy. It provides a basic foundation that can be built upon to create more complex login systems.