import string
from random import randint, choice
from tkinter import *

def generate_password():
    password_min = 6
    password_max = 20
    all_chars = string.ascii_letters + string.punctuation + string.digits

    password ="".join(choice(all_chars) for x in range(randint(password_min, password_max)))
    password_entry.delete(0, END)
    password_entry.insert(0, password)


#creation de la fenetre
window = Tk()
window.title("Générateur de mot de passe")
window.geometry("1080x720")
window.iconbitmap("logo.ico")
window.config(background='#215bb2')

#créee une boite
frame = Frame(window, bg='#215bb2')

#creation d'image
width = 500
height = 500
image = PhotoImage(file="password.png")
canvas = Canvas(frame, width=width, height=height, bg='#215bb2', bd=0, highlightthickness=0)
canvas.create_image(width/2, height/2, image=image)
canvas.grid(row=0, column=0, sticky=W)

#créer sous boite
right_frame= Frame(frame, bg='#215bb2')

#créer un titre
label_title = Label(right_frame, text= "Mot de passe", font=("Courrier", 20), bg='#215bb2', fg='white')
label_title.pack()

#créer un champ
password_entry = Entry(right_frame, text= "Mot de passe", font=("Courrier", 20), bg='#215bb2', fg='white')
password_entry.pack()

#créer un bouton
generate_password_button = Button(right_frame, text= "Générer", font=("Courrier", 20), bg='#215bb2', fg='white', command=generate_password)
generate_password_button.pack(fill=X)

#sous boite  droite de la frame pricipal
right_frame.grid(row=0, column=1, sticky=W)

#afficher frame
frame.pack(expand=YES)

#creation d'une barre de menu
menu_bar = Menu(window)

#créer un premier menu
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Nouveau", command=generate_password)
file_menu.add_command(label="Quitter", command=window.quit)
menu_bar.add_cascade(label="Fichier", menu=file_menu)

#configurer la fenetre pour le menu bar
window.config(menu=menu_bar)

#afficher la fenetre
window.mainloop()
