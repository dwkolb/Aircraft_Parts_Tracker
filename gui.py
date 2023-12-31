# gui.py
import tkinter as tk
from tkinter import simpledialog
from tracker import AircraftPartsTracker

class AircraftPartsGUI:
    def __init__(self, master, tracker):
        self.master = master
        self.master.title("Aircraft Parts Tracker")
        self.master.geometry("800x600")

        self.tracker = tracker

        # Frame for labels and entry boxes
        entry_frame = tk.Frame(master)
        entry_frame.grid(row=0, column=0, columnspan=2)

        labels = ["Part Number", "Serial Number", "Description", "Condition", "Quantity"]
        for row, label_text in enumerate(labels):
            label = tk.Label(entry_frame, text=label_text)
            label.grid(row=row, column=0, padx=10, pady=5, sticky="e")

            entry = tk.Entry(entry_frame)
            entry.grid(row=row, column=1, padx=10, pady=5, sticky="w")

        # Listbox for displaying inventory
        self.inventory_listbox = tk.Listbox(master, selectmode=tk.SINGLE, height=10)
        self.inventory_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        # Scrollbar for the listbox
        scrollbar = tk.Scrollbar(master, command=self.inventory_listbox.yview)
        scrollbar.grid(row=1, column=2, sticky="nsew")
        self.inventory_listbox.config(yscrollcommand=scrollbar.set)

        # Update inventory display initially
        self.tracker.update_inventory_display()

        # Center the GUI
        master.grid_rowconfigure(1, weight=1)  # Adjusted row configuration for the listbox
        master.grid_columnconfigure(0, weight=1)
        master.grid_columnconfigure(1, weight=1)

    def receive_part(self):
        part_info = [entry.get() for entry in self.master.winfo_children() if isinstance(entry, tk.Entry)]
        self.tracker.receive_part(part_info)
        self.tracker.update_inventory_display()

    def checkout_part(self):
        part_number = simpledialog.askstring("Checkout Part", "Enter Part Number:")
        if part_number:
            quantity = simpledialog.askinteger("Checkout Part", "Enter Quantity:")
            if quantity:
                self.tracker.checkout_part(part_number, quantity)
                self.tracker.update_inventory_display()

if __name__ == "__main__":
    root = tk.Tk()
    tracker = AircraftPartsTracker()
    gui = AircraftPartsGUI(root, tracker)
    root.mainloop()
