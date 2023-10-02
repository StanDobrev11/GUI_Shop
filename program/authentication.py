import customtkinter as ctk
from canvas import root, frame


def render_entry():
    register_button = ctk.CTkButton(
        frame,
        text="Register",
        bg_color='green',
        fg_color='white',
        width=40,
        height=20,
    )
    register_button.place(x=200, y=200)

