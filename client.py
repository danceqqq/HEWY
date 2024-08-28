# client.py
import tkinter as tk
from tkinter import messagebox
import requests

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.blur_background()

    def create_widgets(self):
        self.login_frame = tk.Frame(self)
        self.login_frame.pack()

        self.username_label = tk.Label(self.login_frame, text="Логин:")
        self.username_label.pack(side="top")

        self.username_entry = tk.Entry(self.login_frame)
        self.username_entry.pack(side="top")

        self.password_label = tk.Label(self.login_frame, text="Пароль:")
        self.password_label.pack(side="top")

        self.password_entry = tk.Entry(self.login_frame, show="*")
        self.password_entry.pack(side="top")

        self.login_button = tk.Button(self.login_frame, text="Войти", command=self.login)
        self.login_button.pack(side="top")

        self.register_button = tk.Button(self.login_frame, text="Регистрация", command=self.register)
        self.register_button.pack(side="top")

    def blur_background(self):
        self.master.attributes("-alpha", 0.5)

    def unblur_background(self):
        self.master.attributes("-alpha", 1.0)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        response = requests.post('http://localhost:5000/login', json={'username': username, 'password': password})
        if response.json()['success']:
            self.unblur_background()
            self.login_frame.pack_forget()
            self.create_main_frame()
        else:
            messagebox.showerror("Ошибка", "Неправильный логин или пароль")

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        response = requests.post('http://localhost:5000/register', json={'username': username, 'password': password})
        if response.json()['success']:
            messagebox.showinfo("Успешно", "Регистрация прошла успешно")
        else:
            messagebox.showerror("Ошибка", "Пользователь с таким логином уже существует")

    def create_main_frame(self):
        self.main_frame = tk.Frame(self)
        self.main_frame.pack()

        self.get_data_button = tk.Button(self.main_frame, text="Получить данные", command=self.get_data)
        self.get_data_button.pack(side="top")

    def get_data(self):
        response = requests.get('http://localhost:5000/get_data')
        messagebox.showinfo("Данные", response.json()['data'])

root = tk.Tk()
app = Application(master=root)
app.mainloop()
