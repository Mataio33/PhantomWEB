import http.server
import socketserver
import os
import tkinter as tk
from tkinter import filedialog
import webbrowser
import socket
import threading

def select_directory():
    root = tk.Tk()
    root.withdraw()
    directory = filedialog.askdirectory(title='Sélectionnez le répertoire à servir', initialdir='/chemin/vers/le/répertoire/initial', mustexist=True)
    return directory

def start_server():
    global httpd, httpd_thread
    PORT = int(port_entry.get())
    os.chdir(select_directory())
    Handler = http.server.SimpleHTTPRequestHandler
    
    httpd = socketserver.TCPServer(("", PORT), Handler)
    print("serving at http://" + socket.gethostbyname(socket.gethostname()) + ":" + str(PORT))
    print("open the following link in your web browser: http://" + socket.gethostbyname(socket.gethostname()) + ":" + str(PORT))
    webbrowser.open("http://" + socket.gethostbyname(socket.gethostname()) + ":" + str(PORT))
    
    httpd_thread = threading.Thread(target=httpd.serve_forever)
    httpd_thread.start()

def stop_server():
    global httpd
    httpd.shutdown()
    print("Server stopped")

root = tk.Tk()
root.title("PhantomWEB")
root.geometry("300x600")

app_name = tk.Label(root, text="PhantomWEB", font=("Arial", 18, "bold"), foreground="orange")
app_name.pack()

author_message = tk.Label(root, text="Made by Mathieu RODRICK", font=("Arial", 6, "italic"))
author_message.pack()

# Ajout de l'image
server_image = tk.PhotoImage(file="logo.png")
image_label = tk.Label(root, image=server_image)
image_label.pack()

# Saut de 1 lignes
tk.Label(root, text="").pack()

welcome_message = tk.Label(root, text="Bienvenue sur votre serveur web temporaire", font=("Arial", 10, "bold"), justify="center", wraplength=300)
welcome_message.pack()

# Saut de 1 lignes
tk.Label(root, text="").pack()

description_message = tk.Label(root, text="Cette application lance un serveur web qui sert les fichiers d'un répertoire choisi.", wraplength=300)
description_message.pack()

# Ajout du bouton pour le choix du répertoire
choose_dir_button = tk.Button(root, text="Choix du répertoire", command=select_directory, width=20)
choose_dir_button.pack()

# Saut de 1 lignes
tk.Label(root, text="").pack()

label = tk.Label(root, text="Port du serveur:")
label.pack()

port_entry = tk.Entry(root)
port_entry.pack()

start_button = tk.Button(root, text="GO", command=start_server, width=20)
start_button.pack()

stop_button = tk.Button(root, text="STOP", command=stop_server, width=20)
stop_button.pack()

root.mainloop()
