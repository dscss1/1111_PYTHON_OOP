import flet as ft
import sqlite3


class UserManager:
    def __init__(self, db_name="users.db"):
        self.db_name = db_name
        self.init_db()

    def init_db(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users
                          (username TEXT PRIMARY KEY, password TEXT)''')
        conn.commit()
        conn.close()

    def register(self, username, password):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        if cursor.fetchone():
            conn.close()
            return "User with this username already exists."

        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        conn.close()
        return "Registration successful"

    def login(self, username, password):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        if cursor.fetchone():
            conn.close()
            return "Login successful"
        conn.close()
        return "Invalid username or password."


class App:
    def __init__(self):
        self.user_manager = UserManager()
        self.page = None
        self.username_input = None
        self.password_input = None
        self.status_text = None
        self.logged_in_username = None

    def handle_register(self, e):
        username = self.username_input.value
        password = self.password_input.value
        result = self.user_manager.register(username, password)
        self.show_toast(result)
        self.page.update()

    def handle_login(self, e):
        username = self.username_input.value
        password = self.password_input.value
        result = self.user_manager.login(username, password)
        if result == "Login successful":
            self.logged_in_username = username
            self.show_main_page()
        else:
            self.show_toast(result)
            self.page.update()

    def show_register_page(self):
        self.page.clean()
        self.page.add(
            ft.Text("Register", size=40, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE),
            self.username_input,
            self.password_input,
            ft.ElevatedButton("Register", on_click=self.handle_register),
            self.status_text,
            ft.ElevatedButton("Back to main", on_click=self.show_main_page)
        )
        self.page.update()

    def show_login_page(self):
        self.page.clean()
        self.page.add(
            ft.Text("Login", size=40, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE),
            self.username_input,
            self.password_input,
            ft.ElevatedButton("Login", on_click=self.handle_login),
            self.status_text,
            ft.ElevatedButton("Back to main", on_click=self.show_main_page)
        )
        self.page.update()

    def logout(self, e):
        self.logged_in_username = None
        self.show_main_page()

    def show_main_page(self, e=None):
        self.page.clean()
        if self.logged_in_username:
            self.page.add(
                ft.Text(f"Welcome, {self.logged_in_username}!", size=40, weight=ft.FontWeight.BOLD,
                        color=ft.Colors.PURPLE),
                ft.ElevatedButton("Logout", on_click=self.logout),
            )
        else:
            self.page.add(
                ft.Text("Welcome!", size=40, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE),
                ft.ElevatedButton("Register", on_click=lambda e: self.show_register_page()),
                ft.ElevatedButton("Login", on_click=lambda e: self.show_login_page())
            )
        self.page.update()

    def show_toast(self, message):
        self.page.snack_bar = ft.SnackBar(
            ft.Text(message, size=20),
            duration=3000
        )
        self.page.open(self.page.snack_bar)
        self.page.update()

    def main(self, page):
        self.page = page
        page.title = "Welcome"
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        self.username_input = ft.TextField(label="Username", autofocus=True)
        self.password_input = ft.TextField(label="Password", password=True)
        self.status_text = ft.Text()

        self.show_main_page()


def run_app():
    app = App()
    ft.app(target=app.main)


run_app()
