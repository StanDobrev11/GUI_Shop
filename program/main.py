from canvas import root
from authentication import render_entry

if __name__ == "__main__":  # to be able to execute only the code below this statement to avoid circular import
    render_entry()
    root.mainloop()

