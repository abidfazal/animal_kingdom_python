import tkinter as tk
from tkinter import messagebox
import pygame
from PIL import Image, ImageTk
import re

class AnimalApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Animal Kingdom")
        self.geometry("400x300")
        self.current_frame = None
        self.switch_frame(LoginFrame)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self.current_frame is not None:
            self.current_frame.destroy()
        self.current_frame = new_frame
        self.current_frame.pack()


class LoginFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.configure(bg="#f0f0f0")

        self.username_label = tk.Label(self, text="Username:", bg="#f0f0f0", font=("Helvetica", 12))
        self.username_label.grid(row=0, column=0, pady=(20, 5), padx=10, sticky="w")
        self.username_entry = tk.Entry(self, font=("Helvetica", 12))
        self.username_entry.grid(row=0, column=1, pady=(20, 5), padx=10, sticky="ew")

        self.password_label = tk.Label(self, text="Password:", bg="#f0f0f0", font=("Helvetica", 12))
        self.password_label.grid(row=1, column=0, pady=5, padx=10, sticky="w")
        self.password_entry = tk.Entry(self, show="*", font=("Helvetica", 12))
        self.password_entry.grid(row=1, column=1, pady=5, padx=10, sticky="ew")

        login_button = tk.Button(self, text="Login", command=self.validate_login, bg="#4CAF50", fg="white", font=("Helvetica", 12))
        login_button.grid(row=2, column=0, columnspan=2, pady=10, padx=10, sticky="ew")

        signup_button = tk.Button(self, text="Sign Up", command=self.open_signup_screen, bg="#008CBA", fg="white", font=("Helvetica", 12))
        signup_button.grid(row=3, column=0, columnspan=2, pady=5, padx=10, sticky="ew")

    def validate_login(self):
        # Placeholder logic for validation
        messagebox.showinfo("Login Successful", "You have been successfully logged in!")
        self.master.switch_frame(MainMenuFrame)

    def open_signup_screen(self):
        self.master.switch_frame(SignupFrame)


class SignupFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.configure(bg="#f0f0f0")

        self.username_label = tk.Label(self, text="Username:", bg="#f0f0f0", font=("Helvetica", 12))
        self.username_label.grid(row=0, column=0, pady=(20, 5), padx=10, sticky="w")
        self.username_entry_signup = tk.Entry(self, font=("Helvetica", 12))
        self.username_entry_signup.grid(row=0, column=1, pady=(20, 5), padx=10, sticky="ew")

        self.password_label = tk.Label(self, text="Password:", bg="#f0f0f0", font=("Helvetica", 12))
        self.password_label.grid(row=1, column=0, pady=5, padx=10, sticky="w")
        self.password_entry_signup = tk.Entry(self, show="*", font=("Helvetica", 12))
        self.password_entry_signup.grid(row=1, column=1, pady=5, padx=10, sticky="ew")

        self.email_label = tk.Label(self, text="Email:", bg="#f0f0f0", font=("Helvetica", 12))
        self.email_label.grid(row=2, column=0, pady=5, padx=10, sticky="w")
        self.email_entry_signup = tk.Entry(self, font=("Helvetica", 12))
        self.email_entry_signup.grid(row=2, column=1, pady=5, padx=10, sticky="ew")

        signup_button = tk.Button(self, text="Sign Up", command=self.register_user, bg="#4CAF50", fg="white", font=("Helvetica", 12))
        signup_button.grid(row=3, column=0, columnspan=2, pady=10, padx=10, sticky="ew")

    def register_user(self):
        username = self.username_entry_signup.get()
        password = self.password_entry_signup.get()
        email = self.email_entry_signup.get()

        # Placeholder logic for registration validation
        if not username or not password or not email:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            messagebox.showerror("Error", "Invalid email address.")
            return

        messagebox.showinfo("Registration Successful", "You have been successfully registered!")
        self.master.switch_frame(WelcomeFrame)


class WelcomeFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        label = tk.Label(self, text="Welcome to Animal Kingdom!", font=("Helvetica", 14, "bold"), bg="#f0f0f0")
        label.pack()

        continue_button = tk.Button(self, text="Continue", command=lambda: self.master.switch_frame(MainMenuFrame), bg="#008CBA", fg="white", font=("Helvetica", 12))
        continue_button.pack()


class MainMenuFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        label = tk.Label(self, text="Main Menu", font=("Helvetica", 14, "bold"), bg="#f0f0f0")
        label.pack()

        mammal_button = tk.Button(self, text="Mammals", command=lambda: self.master.switch_frame(MammalFrame), bg="#4CAF50", fg="white", font=("Helvetica", 12))
        mammal_button.pack()

        aves_button = tk.Button(self, text="Aves", command=lambda: self.master.switch_frame(AvesFrame), bg="#4CAF50", fg="white", font=("Helvetica", 12))
        aves_button.pack()

        amphibian_button = tk.Button(self, text="Amphibians", command=lambda: self.master.switch_frame(AmphibianFrame), bg="#4CAF50", fg="white", font=("Helvetica", 12))
        amphibian_button.pack()

        reptile_button = tk.Button(self, text="Reptiles", command=lambda: self.master.switch_frame(ReptileFrame), bg="#4CAF50", fg="white", font=("Helvetica", 12))
        reptile_button.pack()

        insect_button = tk.Button(self, text="Insects", command=lambda: self.master.switch_frame(InsectFrame), bg="#4CAF50", fg="white", font=("Helvetica", 12))
        insect_button.pack()


class AnimalFrame(tk.Frame):
    def __init__(self, master, animal_name, color, sensory_organs, reproduction_method, image_path, sound_path):
        super().__init__(master)
        self.master = master
        self.animal_name = animal_name
        self.color = color
        self.sensory_organs = sensory_organs
        self.reproduction_method = reproduction_method

        self.image_path = image_path
        self.sound_path = sound_path

        label = tk.Label(self, text=f"{self.animal_name} Information", font=("Helvetica", 14, "bold"), bg="#f0f0f0")
        label.pack()

        color_label = tk.Label(self, text=f"Color: {self.color}", bg="#f0f0f0", font=("Helvetica", 12))
        color_label.pack()

        sensory_label = tk.Label(self, text=f"Sensory Organs: {self.sensory_organs}", bg="#f0f0f0", font=("Helvetica", 12))
        sensory_label.pack()

        reproduction_label = tk.Label(self, text=f"Reproduction Method: {self.reproduction_method}", bg="#f0f0f0", font=("Helvetica", 12))
        reproduction_label.pack()

        image_button = tk.Button(self, text="View Image", command=self.show_image, bg="#4CAF50", fg="white", font=("Helvetica", 12))
        image_button.pack()

        sound_button = tk.Button(self, text="Play Sound", command=self.play_sound, bg="#4CAF50", fg="white", font=("Helvetica", 12))
        sound_button.pack()

        back_button = tk.Button(self, text="Back to Menu", command=self.back_to_menu, bg="#008CBA", fg="white", font=("Helvetica", 12))
        back_button.pack()

    def show_image(self):
        img = Image.open(self.image_path)
        img.show()

    def play_sound(self):
        pygame.mixer.init()
        pygame.mixer.music.load(self.sound_path)
        pygame.mixer.music.play()

    def back_to_menu(self):
        self.master.switch_frame(MainMenuFrame)


class MammalFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        label = tk.Label(self, text="Mammals", font=("Helvetica", 14, "bold"), bg="#f0f0f0")
        label.pack()

        cat_button = tk.Button(self, text="Cat", command=lambda: self.master.switch_frame(CatFrame), bg="#4CAF50", fg="white", font=("Helvetica", 12))
        cat_button.pack()

        dog_button = tk.Button(self, text="Dog", command=lambda: self.master.switch_frame(DogFrame), bg="#4CAF50", fg="white", font=("Helvetica", 12))
        dog_button.pack()

        monkey_button = tk.Button(self, text="Monkey", command=lambda: self.master.switch_frame(MonkeyFrame), bg="#4CAF50", fg="white", font=("Helvetica", 12))
        monkey_button.pack()


class CatFrame(AnimalFrame):
    def __init__(self, master):
        super().__init__(master, "Cat", "Varies", "Eyes", "Varies", "kingdomnew/pic/cat.jpg", "kingdomnew/audio/Cat_voice(256k).mp3")


class DogFrame(AnimalFrame):
    def __init__(self, master):
        super().__init__(master, "Dog", "Varies", "Eyes", "Varies", "kingdomnew/pic/dog.jpeg", "kingdomnew/audio/Dog_sound.mp3")


class MonkeyFrame(AnimalFrame):
    def __init__(self, master):
        super().__init__(master, "Monkey", "Varies", "Eyes", "Varies", "kingdomnew/pic/moneky.jpeg", "kingdomnew/audio/Monkey_sound.mp3")


class AvesFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        label = tk.Label(self, text="Aves", font=("Helvetica", 14, "bold"), bg="#f0f0f0")
        label.pack()

        parrot_button = tk.Button(self, text="Parrot", command=lambda: self.master.switch_frame(ParrotFrame), bg="#4CAF50", fg="white", font=("Helvetica", 12))
        parrot_button.pack()

        owl_button = tk.Button(self, text="Owl", command=lambda: self.master.switch_frame(OwlFrame), bg="#4CAF50", fg="white", font=("Helvetica", 12))
        owl_button.pack()


class ParrotFrame(AnimalFrame):
    def __init__(self, master):
        super().__init__(master, "Parrot", "Varies", "Eyes", "Varies", "kingdomnew/pic/piroat.jpeg", "kingdomnew/audio/Parrot_sound.mp3")


class OwlFrame(AnimalFrame):
    def __init__(self, master):
        super().__init__(master, "Owl", "Varies", "Eyes", "Varies", "kingdomnew/pic/owl.jpg", "kingdomnew/audio/Owl_sound.mp3")


class AmphibianFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        label = tk.Label(self, text="Amphibians", font=("Helvetica", 14, "bold"), bg="#f0f0f0")
        label.pack()

        frog_button = tk.Button(self, text="Frog", command=lambda: self.master.switch_frame(FrogFrame), bg="#4CAF50", fg="white", font=("Helvetica", 12))
        frog_button.pack()


class FrogFrame(AnimalFrame):
    def __init__(self, master):
        super().__init__(master, "Frog", "Varies", "Eyes", "Varies", "kingdomnew/pic/frog.jpg", "kingdomnew/audio/Frog_sound.mp3")


class ReptileFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        label = tk.Label(self, text="Reptiles", font=("Helvetica", 14, "bold"), bg="#f0f0f0")
        label.pack()

        lizard_button = tk.Button(self, text="Lizard", command=lambda: self.master.switch_frame(LizardFrame), bg="#4CAF50", fg="white", font=("Helvetica", 12))
        lizard_button.pack()

        snake_button = tk.Button(self, text="Python Snake", command=lambda: self.master.switch_frame(SnakeFrame), bg="#4CAF50", fg="white", font=("Helvetica", 12))
        snake_button.pack()


class LizardFrame(AnimalFrame):
    def __init__(self, master):
        super().__init__(master, "Lizard", "Varies", "Eyes", "Varies", "kingdomnew/pic/lizzard.jpg", "kingdomnew/audio/Lizard_sound.mp3")


class SnakeFrame(AnimalFrame):
    def __init__(self, master):
        super().__init__(master, "Python Snake", "Varies", "Eyes", "Varies", "kingdomnew/pic/snak.jpeg", "kingdomnew/audio/Snake_sound.mp3")


class InsectFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        label = tk.Label(self, text="Insects", font=("Helvetica", 14, "bold"), bg="#f0f0f0")
        label.pack()

        bee_button = tk.Button(self, text="Bees", command=lambda: self.master.switch_frame(BeeFrame), bg="#4CAF50", fg="white", font=("Helvetica", 12))
        bee_button.pack()


class BeeFrame(AnimalFrame):
    def __init__(self, master):
        super().__init__(master, "Bees", "Varies", "Eyes", "Varies", "kingdomnew/pic/bees.jpeg", "kingdomnew/audio/Bee_Buzzing_-_Nature_Sound_Effects_HD(256k).mp3")


if __name__ == "__main__":
    app = AnimalApp()
    app.mainloop()
