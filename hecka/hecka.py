import tkinter as tk
from tkinter import messagebox
import datetime

# This will store the inventory in 'data.txt' file
FILE_NAME = "data.txt"

# Function to check for expiry alerts
def check_expiry():
    today = datetime.date.today()
    expiry_alert = []
    
    try:
        with open(FILE_NAME, 'r') as file:
            lines = file.readlines()
            for line in lines:
                item = line.strip().split(',')
                name, stock, purchase_date, expiry_date = item[0], item[1], item[2], item[3]
                
                # Convert expiry_date to datetime object
                expiry_date = datetime.datetime.strptime(expiry_date, "%Y-%m-%d").date()
                
                # If expiry is near (let's say within 7 days)
                if (expiry_date - today).days <= 7:
                    expiry_alert.append(f"{name} is expiring on {expiry_date}")
                    
    except FileNotFoundError:
        print("No inventory data found.")
        
    if expiry_alert:
        messagebox.showwarning("Expiry Alert", "\n".join(expiry_alert))

# Function to login
def login():
    username = entry_username.get()
    password = entry_password.get()

    if username == "thdcihet" and password == "shiro":
        login_window.destroy()
        open_inventory_window()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password!")

# Function to open inventory window
def open_inventory_window():
    inventory_window = tk.Tk()
    inventory_window.title("Inventory Management")

    # Function to add item to inventory
    def add_item():
        name = entry_item_name.get()
        stock = entry_stock.get()
        purchase_date = entry_purchase_date.get()
        expiry_date = entry_expiry_date.get()

        if name and stock and purchase_date and expiry_date:
            # Suggest item name (You can implement logic to suggest based on user input if required)
            with open(FILE_NAME, 'a') as file:
                file.write(f"{name},{stock},{purchase_date},{expiry_date}\n")
            messagebox.showinfo("Success", f"Item {name} added successfully!")
            entry_item_name.delete(0, 'end')
            entry_stock.delete(0, 'end')
            entry_purchase_date.delete(0, 'end')
            entry_expiry_date.delete(0, 'end')
        else:
            messagebox.showerror("Error", "All fields are required!")

    # UI elements for inventory management
    label_item_name = tk.Label(inventory_window, text="Item Name")
    label_item_name.grid(row=0, column=0)

    entry_item_name = tk.Entry(inventory_window)
    entry_item_name.grid(row=0, column=1)

    label_stock = tk.Label(inventory_window, text="Stock")
    label_stock.grid(row=1, column=0)

    entry_stock = tk.Entry(inventory_window)
    entry_stock.grid(row=1, column=1)

    label_purchase_date = tk.Label(inventory_window, text="Purchase Date (YYYY-MM-DD)")
    label_purchase_date.grid(row=2, column=0)

    entry_purchase_date = tk.Entry(inventory_window)
    entry_purchase_date.grid(row=2, column=1)

    label_expiry_date = tk.Label(inventory_window, text="Expiry Date (YYYY-MM-DD)")
    label_expiry_date.grid(row=3, column=0)

    entry_expiry_date = tk.Entry(inventory_window)
    entry_expiry_date.grid(row=3, column=1)

    button_add_item = tk.Button(inventory_window, text="Add Item", command=add_item)
    button_add_item.grid(row=4, columnspan=2)

    button_check_expiry = tk.Button(inventory_window, text="Check Expiry", command=check_expiry)
    button_check_expiry.grid(row=5, columnspan=2)

    inventory_window.mainloop()

# GUI for login page
login_window = tk.Tk()
login_window.title("Login Page")

label_username = tk.Label(login_window, text="Username")
label_username.grid(row=0, column=0)

entry_username = tk.Entry(login_window)
entry_username.grid(row=0, column=1)

label_password = tk.Label(login_window, text="Password")
label_password.grid(row=1, column=0)

entry_password = tk.Entry(login_window, show="*")
entry_password.grid(row=1, column=1)

button_login = tk.Button(login_window, text="Login", command=login)
button_login.grid(row=2, columnspan=2)

login_window.mainloop()

# make a data.txt file and attach it to this code for storing items