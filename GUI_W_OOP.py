import tkinter as tk
from tkinter import messagebox , PhotoImage
from tkinter import *


#################### Login Page ####################
class LoginPage(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("640x446+200+100")
        self.title("Login!")
        self.iconbitmap(r"F:\courses\Ai Instant\Self\Tkinter\summary\Ancient_Legend.ico")

        # Variables
        self.var_username = tk.StringVar()
        self.var_password = tk.StringVar()
        self.database = {"ahmedessam": "essam", "ahmedtamer": "tamer", "youssef": "youssef", "a":"a"}

        # Background
        self.image_back = tk.PhotoImage(file=r"F:\courses\Ai Instant\Self\Tkinter\summary\rafael-m-CTNHIGI2WcU-unsplash.png")
        self.lbl_back = tk.Label(self, image=self.image_back)
        self.lbl_back.place(x=-2, y=-2)

        # Entry Box for Username
        self.ent_username = tk.Entry(self, highlightthickness=2.5, bg ="#e4d0b5",highlightbackground="#663300", highlightcolor="#864f00", relief="flat", font=("arial", 12), textvariable=self.var_username)
        self.ent_username.place(x=280, y=207, width=179.24, height=23.37)

        self.lbl_username_word = tk.Label(self, text="Username", bg="#e4d0b5", fg="#441f02",highlightthickness=2.5, highlightbackground="#663300", highlightcolor="#864f00", relief="flat",font=("arial", 8, "bold"))
        self.lbl_username_word.place(x=212,y=207, width=65,height=23.37)


        # Entry Box for Password
        self.ent_password = tk.Entry(self, highlightthickness=2.5, bg ="#e4d0b5", highlightbackground="#663300", highlightcolor="#864f00", relief="flat", font=("arial", 12), show="*", textvariable=self.var_password)
        self.ent_password.place(x=280, y=250, width=179.24, height=23.37)

        self.lbl_password_word = tk.Label(self, text="Password", bg="#e4d0b5", fg="#441f02",highlightthickness=2.5, highlightbackground="#663300", highlightcolor="#864f00", relief="flat",font=("arial", 8, "bold"))
        self.lbl_password_word.place(x=212,y=250, width=65,height=23.37)


        # Buttons for Login and Sign Up
        self.bt_login = tk.Button(self, text="Login", font=("arial", 10, "bold"), bg="#864f00", activebackground="#663300", relief="flat", command=self.login)
        self.bt_login.place(x=229, y=289, width=91, height=21)
        self.bt_login.bind("<Enter>", self.bt_login_enter)
        self.bt_login.bind("<Leave>", self.bt_login_leave)


        self.bt_signup = tk.Button(self, text="Sign Up", font=("arial", 10, "bold"), bg="#864f00", activebackground="#663300", relief="flat", command=self.sign_up)
        self.bt_signup.place(x=347, y=289, width=91, height=21)
        self.bt_signup.bind("<Enter>", self.bt_signup_enter)
        self.bt_signup.bind("<Leave>", self.bt_signup_leave)

    def login(self):
        username = self.var_username.get()
        password = self.var_password.get()
        if username in self.database.keys():
            if password == self.database[username]:
                messagebox.showinfo("Success", f"Welcome {username}!")
                self.withdraw()  # Hide the login window
                library_window = LibraryGUI(self)
                library_window.mainloop()
            else:
                messagebox.showerror("Error", "Wrong password!")
        else:
            messagebox.showerror("Error", "Wrong username!")

    def sign_up(self):
        signup_window = Toplevel()
        signup_window.title("Sign Up")
        signup_window.geometry("300x200")

        # Username label & entry
        Label(signup_window, text="Username:").pack(pady=5)
        username_entry = Entry(signup_window)
        username_entry.pack(pady=5)

        # Password label & entry
        Label(signup_window, text="Password:").pack(pady=5)
        password_entry = Entry(signup_window, show="*")
        password_entry.pack(pady=5)

        # Save user function
        def save_user():
            username = username_entry.get()
            password = password_entry.get()
            if username and password:
                self.database[username] = password
                messagebox.showinfo("welcome" ,f"User '{username}' signed up successfully!")
                signup_window.destroy()
            else:
                print("Both fields are required.")

        Button(signup_window, text="Sign Up", command=save_user).pack(pady=10)

    def bt_login_enter(self, e):
        self.bt_login.config(bg="#864f00")
    def bt_login_leave(self, e):
        self.bt_login.config(bg="#663300")
    def bt_signup_enter(self, e):
        self.bt_signup.config(bg="#864f00")
    def bt_signup_leave(self, e):
        self.bt_signup.config(bg="#663300")
            

        

#################### Library Management System ####################
class Book:
    def __init__(self, id, title, author, no_of_copies):
        self._id = id
        self._title = title
        self._author = author
        self._no_of_copies = no_of_copies

    def get_id(self):
        return self._id
    
    def get_title(self):
        return self._title
    
    def get_author(self):
        return self._author
    
    def get_no_of_copies(self):
        return self._no_of_copies

    def set_title(self, title):
        self._title = title
    
    def set_author(self, author):
        self._author = author

    def set_no_of_copies(self, no_of_copies):
        self._no_of_copies = no_of_copies

    def display_info(self):
        return f"ID: {self._id}\nTitle: {self._title}\nAuthor: {self._author}\nCopies: {self._no_of_copies}\n"


class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, id, title, author, no_of_copies):
        if id in self.books:
            return False  # Book with this ID already exists
        book = Book(id, title, author, no_of_copies)
        self.books[book.get_id()] = book
        return True
    
    def borrow(self, book_id):
        book = self.books.get(book_id)
        if book and book.get_no_of_copies() > 0:
            book.set_no_of_copies(book.get_no_of_copies() - 1)
            return book
        return None

    def remove_book(self, book_id):
        if book_id in self.books:
            del self.books[book_id]
            return True
        return False

    def search(self, name):
        results = []
        for book in self.books.values():
            if name.lower() in book.get_title().lower() or name.lower() in book.get_author().lower():
                results.append(book)
        return results 
    
    def get_all_books(self):
        return list(self.books.values())


class LibraryGUI(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Library Management System")
        self.geometry("1200x744+200+10")
        self.iconbitmap(r"F:\courses\Ai Instant\Self\Tkinter\summary\George-Ui-Ancient-Legend-Books-Library.ico")

        #Background
        self.image_back = PhotoImage(file = r"F:\courses\Ai Instant\Self\Tkinter\summary\library_mangament (2).png")
        self.lbl_back = tk.Label(self, image= self.image_back, )
        self.lbl_back.place(x=-2, y=-2)

        self.library = Library()
        self.create_widgets()

    def create_widgets(self):
        self.id_label = tk.Label(self, text="Book ID", bg="#fbe8c7", fg="#86432d")
        self.id_label.place(x=80,y=195)
        self.id_entry = tk.Entry(self, bg="#e4d0b5",highlightthickness=2.5 ,highlightbackground="#684d32", highlightcolor="#56402b", relief="flat")
        self.id_entry.place(x=204, y=195,width=200,height=25)

        self.title_label = tk.Label(self, text="Book Title", bg="#fbe8c7", fg="#86432d")
        self.title_label.place(x=80, y=266)
        self.title_entry = tk.Entry(self,bg="#e4d0b5",highlightthickness=2.5 ,highlightbackground="#684d32", highlightcolor="#56402b", relief="flat")
        self.title_entry.place(x=204, y=266,width=200,height=25)

        self.author_label = tk.Label(self, text="Book Author", bg="#fbe8c7", fg="#86432d")
        self.author_label.place(x=80, y=329)
        self.author_entry = tk.Entry(self, bg="#e4d0b5",highlightthickness=2.5 ,highlightbackground="#684d32", highlightcolor="#56402b", relief="flat")
        self.author_entry.place(x=204, y=329,width=200,height=25)

        self.copies_label = tk.Label(self, text="Number of Copies", bg="#fbe8c7", fg="#86432d")
        self.copies_label.place(x=80, y=386)
        self.copies_entry = tk.Entry(self, bg="#e4d0b5",highlightthickness=2.5 ,highlightbackground="#684d32", highlightcolor="#56402b", relief="flat")
        self.copies_entry.place(x=204, y=386,width=200,height=25)

        self.add_button = tk.Button(self, text="Add Book", command=self.add_book, bg="#8C5C2D", fg="#000000", relief="flat")
        self.add_button.place(x=430 , y=410, width=126, height=43)

        self.search_label = tk.Label(self, text="Search Book by Title/Author", bg="#fbf2e1", fg="#86432d")
        self.search_label.place(x=120, y=500)
        self.search_entry = tk.Entry(self, bg="#e4d0b5",highlightthickness=2.5 ,highlightbackground="#684d32", highlightcolor="#56402b", relief="flat")
        self.search_entry.place(x=357, y=500,width=200,height=25)

        self.search_button = tk.Button(self, text="Search", command=self.search_book, bg="#8C5C2D", fg="#000000", relief="flat")
        self.search_button.place(x=600, y=490,width=111.14, height=37.56)

        self.borrow_label = tk.Label(self, text="Enter Book ID to Borrow", bg="#fbe8c7", fg="#9e553d")
        self.borrow_label.place(x=105, y=570, width=196 , height=14)
        self.borrow_entry = tk.Entry(self, bg="#e4d0b5",highlightthickness=2.5 ,highlightbackground="#684d32", highlightcolor="#56402b", relief="flat")
        self.borrow_entry.place(x=357, y=570,width=200,height=25)

        self.borrow_button = tk.Button(self, text="Borrow Book", command=self.borrow_book, bg="#8C5C2D", fg="#000000", relief="flat")
        self.borrow_button.place(x=600, y=560, width=111.14, height=37.56)

        self.display_button = tk.Button(self, text="Display All Books", command=self.display_books, bg="#8C5C2D", fg="#000000", relief="flat")
        self.display_button.place(x=391, y=630, width=365, height=43)

        self.output_text = tk.Text(self, height=10, width=60,bg="#e4d0b5",highlightthickness=2.5 ,highlightbackground="#684d32", highlightcolor="#56402b", relief="flat")
        self.output_text.place(x=677,y=132,width=505,height=271 )

    def add_book(self):
        book_id = self.id_entry.get()
        title = self.title_entry.get()
        author = self.author_entry.get()
        no_of_copies = self.copies_entry.get()

        if not book_id or not title or not author or not no_of_copies.isdigit():
            messagebox.showerror("Input Error", "Please fill all fields correctly!")
            return
        
        if not self.library.add_book(book_id, title, author, int(no_of_copies)):
            messagebox.showerror("Duplicate Error", f"Book with ID '{book_id}' already exists!")
            return
        
        messagebox.showinfo("Success", "Book added successfully!")
        self.clear_entries()

    def borrow_book(self):
        book_id = self.borrow_entry.get()
        
        if not book_id:
            messagebox.showerror("Input Error", "Please enter a book ID to borrow!")
            return
        
        book = self.library.borrow(book_id)
        
        if not book:
            messagebox.showerror("Not Found", "No book found with this ID or the book is unavailable!")
        else:
            remaining_copies = book.get_no_of_copies()
            if remaining_copies == 0:
                messagebox.showinfo("Out of Stock", f"You're the last one to borrow this book: {book.get_title()} by {book.get_author()}. No more copies left.")
            else:
                messagebox.showinfo("Success", f"You borrowed: {book.get_title()} by {book.get_author()}. Remaining copies: {remaining_copies}")

        self.clear_entries()

    def search_book(self):
        search_term = self.search_entry.get()
        
        if not search_term:
            messagebox.showerror("Input Error", "Please enter a search term!")
            return

        results = self.library.search(search_term)
        
        if not results:
            messagebox.showinfo("No Results", "No books found!")
        else:
            self.display_books_list(results)

    def display_books(self):
        all_books = self.library.get_all_books()
        self.display_books_list(all_books)

    def display_books_list(self, books):
        self.output_text.delete(1.0, tk.END)
        for book in books:
            self.output_text.insert(tk.END, book.display_info() + "\n")

    def clear_entries(self):
        self.id_entry.delete(0, tk.END)
        self.title_entry.delete(0, tk.END)
        self.author_entry.delete(0, tk.END)
        self.copies_entry.delete(0, tk.END)
        self.search_entry.delete(0, tk.END)
        self.borrow_entry.delete(0, tk.END)


if __name__ == "__main__":
    app = LoginPage()
    app.mainloop()
