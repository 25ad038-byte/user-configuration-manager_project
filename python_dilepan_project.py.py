
import tkinter as tk
from tkinter import ttk, messagebox

# ==========================================
# USER CONFIGURATION MANAGEMENT SYSTEM
# ==========================================

# Initial settings dictionary
test_settings = {
    'theme': 'dark',
    'notifications': 'enabled',
    'volume': 'high'
}


# ==========================================
# 1. ADD SETTING
# ==========================================

def add_setting(test_dict, test_tuple):
    key, value = test_tuple
    key_low = key.lower()
    value_low = value.lower()

    if key_low in test_dict:
        return f"Setting '{key_low}' already exists!"

    test_dict[key_low] = value_low

    return f"Setting '{key_low}' added successfully!"


# ==========================================
# 2. UPDATE SETTING
# ==========================================

def update_setting(test_dict, test_tuple):
    key, value = test_tuple
    key_low = key.lower()
    value_low = value.lower()

    if key_low in test_dict:
        test_dict[key_low] = value_low
        return f"Setting '{key_low}' updated successfully!"

    return f"Setting '{key_low}' does not exist!"


# ==========================================
# 3. DELETE SETTING
# ==========================================

def delete_setting(test_dict, key):
    key_low = key.lower()

    if key_low in test_dict:
        test_dict.pop(key_low)
        return f"Setting '{key_low}' deleted successfully!"

    return "Setting not found!"


# ==========================================
# 4. VIEW SETTINGS
# ==========================================

def view_settings(test_dict):
    if len(test_dict) == 0:
        return "No settings available."

    string = ""

    for key, value in test_dict.items():
        string += f"{key.capitalize()}: {value}\n"

    return string


# ==========================================
# GUI FUNCTIONS
# ==========================================

def refresh_table():
    for item in table.get_children():
        table.delete(item)

    for key, value in test_settings.items():
        table.insert(
            "",
            "end",
            values=(key.capitalize(), value)
        )

    total_label.config(text=str(len(test_settings)))


def clear_fields():
    name_entry.delete(0, tk.END)
    value_entry.delete(0, tk.END)


def select_setting(event):
    selected = table.selection()

    if selected:
        values = table.item(selected[0], "values")

        clear_fields()

        name_entry.insert(0, values[0])
        value_entry.insert(0, values[1])


def add_button():
    key = name_entry.get().strip()
    value = value_entry.get().strip()

    if not key or not value:
        messagebox.showwarning(
            "Warning",
            "Please enter setting name and value!"
        )
        return

    result = add_setting(test_settings, (key, value))

    if result.endswith("successfully!"):
        messagebox.showinfo("Success", result)
        refresh_table()
        clear_fields()
    else:
        messagebox.showerror("Error", result)


def update_button():
    key = name_entry.get().strip()
    value = value_entry.get().strip()

    if not key or not value:
        messagebox.showwarning(
            "Warning",
            "Please enter setting name and value!"
        )
        return

    result = update_setting(test_settings, (key, value))

    if result.endswith("successfully!"):
        messagebox.showinfo("Success", result)
        refresh_table()
        clear_fields()
    else:
        messagebox.showerror("Error", result)


def delete_button():
    key = name_entry.get().strip()

    if not key:
        messagebox.showwarning(
            "Warning",
            "Please enter or select a setting!"
        )
        return

    if key.lower() not in test_settings:
        messagebox.showerror("Error", "Setting not found!")
        return

    confirm = messagebox.askyesno(
        "Confirm Delete",
        f"Delete setting '{key}'?"
    )

    if confirm:
        result = delete_setting(test_settings, key)

        messagebox.showinfo("Success", result)

        refresh_table()
        clear_fields()


def view_button():
    result = view_settings(test_settings)

    messagebox.showinfo(
        "Current User Settings",
        result
    )


# ==========================================
# MAIN WINDOW
# ==========================================

root = tk.Tk()

root.title("User Configuration Management System")
root.geometry("950x650")
root.configure(bg="#F1F5F9")
root.resizable(False, False)


# ==========================================
# HEADER
# ==========================================

header = tk.Frame(
    root,
    bg="#172554",
    height=110
)

header.pack(fill="x")
header.pack_propagate(False)

tk.Label(
    header,
    text="USER CONFIGURATION MANAGER",
    font=("Arial", 23, "bold"),
    bg="#172554",
    fg="white"
).pack(pady=(22, 5))

tk.Label(
    header,
    text="Manage your personal settings easily",
    font=("Arial", 11),
    bg="#172554",
    fg="#BFDBFE"
).pack()


# ==========================================
# DASHBOARD SUMMARY
# ==========================================

summary = tk.Frame(
    root,
    bg="white",
    highlightbackground="#CBD5E1",
    highlightthickness=1
)

summary.pack(fill="x", padx=35, pady=20)

tk.Label(
    summary,
    text="TOTAL CONFIGURATIONS",
    font=("Arial", 11, "bold"),
    bg="white",
    fg="#64748B"
).pack(pady=(10, 2))

total_label = tk.Label(
    summary,
    text="3",
    font=("Arial", 25, "bold"),
    bg="white",
    fg="#2563EB"
)

total_label.pack(pady=(0, 10))


# ==========================================
# MAIN CONTENT AREA
# ==========================================

content = tk.Frame(
    root,
    bg="#F1F5F9"
)

content.pack(
    fill="both",
    expand=True,
    padx=35
)


# ==========================================
# LEFT SIDE - INPUT FORM
# ==========================================

left = tk.Frame(
    content,
    bg="white",
    width=320
)

left.pack(
    side="left",
    fill="y",
    padx=(0, 20)
)

left.pack_propagate(False)

tk.Label(
    left,
    text="Manage Configuration",
    font=("Arial", 15, "bold"),
    bg="white",
    fg="#172554"
).pack(anchor="w", padx=20, pady=20)


tk.Label(
    left,
    text="Setting Name",
    font=("Arial", 10, "bold"),
    bg="white"
).pack(anchor="w", padx=20)

name_entry = tk.Entry(
    left,
    font=("Arial", 12),
    bd=1,
    relief="solid"
)

name_entry.pack(
    fill="x",
    padx=20,
    pady=(7, 18),
    ipady=8
)


tk.Label(
    left,
    text="Setting Value",
    font=("Arial", 10, "bold"),
    bg="white"
).pack(anchor="w", padx=20)

value_entry = tk.Entry(
    left,
    font=("Arial", 12),
    bd=1,
    relief="solid"
)

value_entry.pack(
    fill="x",
    padx=20,
    pady=(7, 20),
    ipady=8
)


# ==========================================
# ACTION BUTTONS
# ==========================================

tk.Button(
    left,
    text="ADD SETTING",
    command=add_button,
    bg="#2563EB",
    fg="white",
    font=("Arial", 10, "bold"),
    relief="flat",
    cursor="hand2"
).pack(fill="x", padx=20, pady=5, ipady=9)


tk.Button(
    left,
    text="UPDATE SETTING",
    command=update_button,
    bg="#0F766E",
    fg="white",
    font=("Arial", 10, "bold"),
    relief="flat",
    cursor="hand2"
).pack(fill="x", padx=20, pady=5, ipady=9)


tk.Button(
    left,
    text="DELETE SETTING",
    command=delete_button,
    bg="#DC2626",
    fg="white",
    font=("Arial", 10, "bold"),
    relief="flat",
    cursor="hand2"
).pack(fill="x", padx=20, pady=5, ipady=9)


tk.Button(
    left,
    text="VIEW SETTINGS",
    command=view_button,
    bg="#475569",
    fg="white",
    font=("Arial", 10, "bold"),
    relief="flat",
    cursor="hand2"
).pack(fill="x", padx=20, pady=5, ipady=9)


tk.Button(
    left,
    text="CLEAR FIELDS",
    command=clear_fields,
    bg="#E2E8F0",
    fg="#172554",
    font=("Arial", 10, "bold"),
    relief="flat",
    cursor="hand2"
).pack(fill="x", padx=20, pady=5, ipady=9)


# ==========================================
# RIGHT SIDE - SETTINGS TABLE
# ==========================================

right = tk.Frame(
    content,
    bg="white"
)

right.pack(
    side="right",
    fill="both",
    expand=True
)

tk.Label(
    right,
    text="Current Configurations",
    font=("Arial", 16, "bold"),
    bg="white",
    fg="#172554"
).pack(anchor="w", padx=20, pady=20)


# TABLE DESIGN

style = ttk.Style()

style.theme_use("clam")

style.configure(
    "Treeview",
    rowheight=40,
    font=("Arial", 11),
    background="white",
    fieldbackground="white"
)

style.configure(
    "Treeview.Heading",
    font=("Arial", 10, "bold"),
    background="#DBEAFE",
    foreground="#172554"
)

table = ttk.Treeview(
    right,
    columns=("name", "value"),
    show="headings"
)

table.heading(
    "name",
    text="SETTING NAME"
)

table.heading(
    "value",
    text="SETTING VALUE"
)

table.column(
    "name",
    width=160
)

table.column(
    "value",
    width=160
)

table.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=(0, 20)
)

table.bind(
    "<<TreeviewSelect>>",
    select_setting
)


# ==========================================
# FOOTER
# ==========================================

footer = tk.Label(
    root,
    text="Python Mini Project | User Configuration Management System",
    font=("Arial", 9),
    bg="#172554",
    fg="white",
    pady=10
)

footer.pack(fill="x")


# ==========================================
# START APPLICATION
# ==========================================

refresh_table()

root.mainloop()
