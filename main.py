import os
import tkinter as tk
from tkinter import simpledialog, messagebox, Listbox, Scrollbar, END

HOSTS_PATH = r"C:\Windows\System32\drivers\etc\hosts"
REDIRECT_IP = "127.0.0.1"


def read_blocked_sites():
    if not os.path.exists(HOSTS_PATH):
        return []
    with open(HOSTS_PATH, 'r') as file:
        lines = file.readlines()
    blocked = []
    for line in lines:
        if line.startswith(REDIRECT_IP):
            parts = line.split()
            if len(parts) > 1:
                blocked.append(parts[1])
    return blocked


def block_website(domain):
    if not domain:
        return
    domain = domain.strip().replace("https://", "").replace("http://", "").split('/')[0]
    blocked = read_blocked_sites()
    if domain in blocked:
        messagebox.showinfo("Already Blocked", f"{domain} is already blocked.")
        return

    try:
        with open(HOSTS_PATH, "a") as file:
            file.write(f"\n{REDIRECT_IP} {domain}")
        messagebox.showinfo("Success", f"{domain} blocked successfully!")
        refresh_list()
    except PermissionError:
        messagebox.showerror("Permission Denied", "Please run this program as Administrator.")


def unblock_website(domain):
    if not domain:
        return
    try:
        with open(HOSTS_PATH, 'r') as file:
            lines = file.readlines()
        with open(HOSTS_PATH, 'w') as file:
            for line in lines:
                if domain not in line.strip():
                    file.write(line)
        messagebox.showinfo("Success", f"{domain} unblocked successfully!")
        refresh_list()
    except PermissionError:
        messagebox.showerror("Permission Denied", "Please run this program as Administrator.")


def refresh_list():
    listbox.delete(0, END)
    blocked = read_blocked_sites()
    for site in blocked:
        listbox.insert(END, site)


def block_input():
    domain = simpledialog.askstring("Block Website", "Enter website URL or domain:")
    if domain:
        block_website(domain)


def unblock_selected():
    selected = listbox.curselection()
    if selected:
        site = listbox.get(selected)
        unblock_website(site)


# GUI setup
root = tk.Tk()
root.title("Block Websites - Hosts File Manager")
root.geometry("400x300")

frame = tk.Frame(root)
frame.pack(pady=10)

btn_block = tk.Button(frame, text="Block New Website", command=block_input)
btn_block.pack(pady=5)

btn_unblock = tk.Button(frame, text="Unblock Selected Website", command=unblock_selected)
btn_unblock.pack(pady=5)

btn_refresh = tk.Button(frame, text="Refresh List", command=refresh_list)
btn_refresh.pack(pady=5)

scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")

listbox = Listbox(root, width=50, height=10, yscrollcommand=scrollbar.set)
listbox.pack(pady=10)
scrollbar.config(command=listbox.yview)

refresh_list()

root.mainloop()