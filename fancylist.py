import tkinter as tk
from tkinter import ttk
import pyperclip  # You'll need to install pyperclip with `pip install pyperclip`


class FancyTreeview(ttk.Treeview):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.popup_menu = tk.Menu(self, tearoff=0)
        self.popup_menu.add_command(label="Delete", command=self.delete_selected)
        self.popup_menu.add_command(label="Select All", command=self.select_all)
        self.popup_menu.add_command(label="Copy", command=self.copy_selected)
        self.bind("<Button-3>", self.popup)  # Right-click event

    def popup(self, event):
        try:
            self.popup_menu.tk_popup(event.x_root, event.y_root, 0)
        finally:
            self.popup_menu.grab_release()

    def delete_selected(self):
        for item in self.selection():
            self.delete(item)

    def select_all(self):
        for item in self.get_children():
            self.selection_add(item)

    def copy_selected(self):
        selected_items = self.selection()
        copied_text = ""
        for item in selected_items:
            values = self.item(item, 'values')
            copied_text += ", ".join(values) + "\n"
        pyperclip.copy(copied_text.strip())


# Create the main window
root = tk.Tk()
root.geometry('600x400')
root.title('Treeview with Context Menu')

# Create the FancyTreeview
columns = ('index', 'value')
tree = FancyTreeview(root, columns=columns, show='headings', selectmode='extended')
tree.heading('index', text='Index')
tree.heading('value', text='Value')
tree.pack(fill='both', expand=True)

# Insert some data
for i in range(10):
    tree.insert('', 'end', values=(i, f"Value {i}"))

# Run the application
root.mainloop()
