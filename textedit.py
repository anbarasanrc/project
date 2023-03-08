import tkinter as tk
from tkinter import filedialog

class TextEditor:
    def __init__(self, master):
        self.master = master
        self.master.title("Text Editor")

        # Create a text widget for editing the text
        self.text = tk.Text(self.master)
        self.text.pack(fill=tk.BOTH, expand=True)

        # Create a menu bar with a File menu
        self.menubar = tk.Menu(self.master)
        self.master.config(menu=self.menubar)
        self.filemenu = tk.Menu(self.menubar)
        self.menubar.add_cascade(label="File", menu=self.filemenu)

        # Add commands to the File menu
        self.filemenu.add_command(label="New", command=self.new_file)
        self.filemenu.add_command(label="Open", command=self.open_file)
        self.filemenu.add_command(label="Save", command=self.save_file)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.master.quit)

    def new_file(self):
        # Clear the text widget
        self.text.delete("1.0", tk.END)

    def open_file(self):
        # Prompt the user to select a file
        filename = filedialog.askopenfilename()
        if filename:
            # Open the file and insert its contents into the text widget
            with open(filename, "r") as file:
                text = file.read()
            self.text.delete("1.0", tk.END)
            self.text.insert(tk.END, text)

    def save_file(self):
        # Prompt the user to select a file or confirm overwriting an existing file
        filename = filedialog.asksaveasfilename()
        if filename:
            # Write the contents of the text widget to the file
            with open(filename, "w") as file:
                text = self.text.get("1.0", tk.END)
                file.write(text)

# Create the application window and start the event loop
root = tk.Tk()
app = TextEditor(root)
root.mainloop()
