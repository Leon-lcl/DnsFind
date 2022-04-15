from tkinter import *
import webbrowser
import os
from os import *

# creer une premiere fenetre
window = Tk()

# personnaliser la fenetre
window.title("DnsFind")
window.geometry("1450x640")
window.minsize(580, 360)
window.iconbitmap("icone.ico")
window.config(background="#41b77F")

# créer la frame
frame = Frame(window, bg="#41b77F")

# ajouter un premier texte
label_title = Label(frame, text="Bienvenue sur DnsFind", font=("Courrier", 40), bg="#41b77F", fg="white")
label_title.pack(expand=YES, pady=25)

# ajouter un second texte
label_subtitle = Label(frame, text="L'appplication de recherche", font=("Courrier", 25), bg="#41b77F", fg="white")
label_subtitle.pack(expand=YES)

input_entry = Entry(frame, font=("Helvetica", 20), bg="#4065A4", fg="white")
input_entry.pack(pady=25)


def result():
    global label_result
    rslt = os.system('ipconfig /displaydns | findstr ' + input_entry.get())

    if rslt == 1:
        label_result.configure(text="Le mot " + input_entry.get() + " n'a pas été recherché", fg="red", )

    else:
        label_result.configure(text="Le mot " + input_entry.get() + " a bien été recherché", fg="#6266FB")


# ajouter un premier bouton
search_button = Button(frame, text="Rechercher", font=("Courrier", 25), bg="white", fg="#41b77F", bd=NO, command=result)
search_button.pack()

# le resultat
label_result = Label(frame, text="", font=("Courrier", 25), bg="#41b77F", fg="white")
label_result.pack(expand=YES)

# ajouter
frame.pack(expand=YES)

# afficher
window.mainloop()
