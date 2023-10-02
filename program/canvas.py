import customtkinter as ctk


def create_root():
    root = ctk.CTk()

    root.title('MyGUIshop')
    root.geometry('500x500')
    root.resizable(False, False)  # wont be resizable

    return root


def create_frame():
    frame = ctk.CTkFrame(root, width=500, height=500)
    frame.grid(row=0, column=0)


    return frame


root = create_root()
frame = create_frame()

