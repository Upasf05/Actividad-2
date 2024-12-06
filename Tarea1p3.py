import tkinter as tk
from tkinter import messagebox, simpledialog
import random

class AdivinarNumeroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego adivinador de números")
        self.root.geometry("400x300")
        root.configure(bg='yellow')

        self.nmin = 1
        self.nmax = 10
        self.nadv = random.randint(self.nmin, self.nmax)
        self.intentos = 0
        self.intentos_max = 15
        self.modo = None

        self.create_widgets()  
    
    def create_widgets(self):
        tk.Label(self.root, text="¡Bienvenido al Adivinador de números!", bg= 'yellow').pack(pady=10)

        tk.Label(self.root, text="Elige un modo:", bg= 'yellow').pack()
        tk.Button(self.root, text="Fácil", bg= 'green', command=lambda: self.iniciar_juego(1)).pack(pady=5)
        tk.Button(self.root, text="Intermedio", bg= 'blue', command=lambda: self.iniciar_juego(2)).pack(pady=5)
        tk.Button(self.root, text="Díficil", bg= 'red', command=lambda: self.iniciar_juego(3)).pack(pady=5)
        tk.Button(self.root, text="Clásico", bg= 'green', command=lambda: self.iniciar_juego(4)).pack(pady=5)
        tk.Button(self.root, text="Desafío", bg= 'red', command=lambda: self.iniciar_juego(5)).pack(pady=5)
        tk.Button(self.root, text="Sorpresa", bg= 'blue', command=lambda: self.iniciar_juego(6)).pack(pady=5)

    def iniciar_juego(self, modo):
        self.modo = modo
        self.intentos = 0

        if modo == 1:
            self.nmax = 10
            self.intentos_max = 15
        elif modo == 2:
            self.nmax = 15
            self.intentos_max = 10
        elif modo == 3:
            self.nmax = 30
            self.intentos_max = 10
        elif modo == 4:
            self.nmax = int(self.ask_integer("Introduce el número hasta el que quieres adivinar"))
            self.intentos_max = None
        elif modo == 5:
            self.nmax = int(self.ask_integer("Introduce el número hasta el que quieres adivinar"))
            self.intentos_max = int(self.ask_integer("Introduce el número de intentos que deseas"))
        elif modo == 6:
            self.nmax = int(self.ask_integer("Introduce el número hasta el que quieres adivinar"))
            self.intentos_max = None

        self.nadv = random.randint(self.nmin, self.nmax)
        self.show_riddle_camp()

    def ask_integer(self, mensaje):
        return tk.simpledialog.askinteger("Entrada", mensaje)

    def show_riddle_camp(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text=f"Adivina un número entre {self.nmin} y {self.nmax}.", bg= 'yellow').pack(pady=10)

        self.intentos_label = tk.Label(self.root, text=f"Intentos: {self.intentos}", bg= 'yellow')
        self.intentos_label.pack(pady=5)
        
        self.input_var = tk.StringVar()
        tk.Entry(self.root, textvariable=self.input_var).pack(pady=5)

        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=5)
        
        tk.Button(self.root, text="Adivinar", bg= 'green', command=self.check_number).pack(pady=5)
        tk.Button(button_frame, text="Reiniciar", bg= 'blue', command=self.restart_game).pack(side=tk.RIGHT, padx=5)
        tk.Button(button_frame, text="Menú", bg= 'red', command=self.return_to_menu).pack(side=tk.RIGHT, padx=5)
        
    def restart_game(self):
        self.nadv = random.randint(self.nmin, self.nmax)
        self.intentos = None
        self.show_riddle_camp()

    def return_to_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.create_widgets()    
        
    def check_number(self):
        try:
            njgd = int(self.input_var.get())
            self.intentos +=1

            self.intentos_label.config(text=f"Intentos: {self.intentos if self.intentos_max is None else self.intentos_max - self.intentos}")

            if njgd < self.nadv:
                messagebox.showinfo("Adivinador de números", "Demasiado bajo, intenta con un número más alto.")
            elif njgd > self.nadv:
                messagebox.showinfo("Adivinador de números", "Demasiado alto, intenta con un número más alto.")
            else:
                messagebox.showinfo("Adivinador de números", f"¡Correcto! Has adivinado el número en {self.intentos}")
                self.return_to_menu()

            if self.intentos_max is not None and self.intentos >= self.intentos_max:
                messagebox.showinfo("Adivinador de números", f"Has perdido, el número era {self.nadv}")
                self.return_to_menu()
            
            if self.modo == 6 and self.intentos % 5 == 0:
                self.nadv = random.randint(self.nmin, self.nmax)
                messagebox.showinfo("¡El número ha cambiado!")

        except ValueError:
            messagebox.showerror("Adivinador de números", "Por favor, introduce un número válido")

if __name__ == "__main__":
    root = tk.Tk()
    app = AdivinarNumeroApp(root)
    root.mainloop()                  
