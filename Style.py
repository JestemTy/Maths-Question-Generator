import tkinter as tk

class ModernNeutralColors:
    def __init__(self, root):
        self.root = root
        self.root.configure(bg='#F7F7F7')

        # Create a frame for the main content
        self.main_frame = tk.Frame(self.root, bg='#F7F7F7')
        self.main_frame.pack(padx=20, pady=20)

        # Create a label for the title
        self.title_label = tk.Label(self.main_frame, text="Modern Neutral Colors", font=('Arial', 18), fg='#3498db')
        self.title_label.pack(pady=10)

        # Create a label for the description
        self.description_label = tk.Label(self.main_frame, text="Lorem ipsum dolor sit amet, consectetur adipiscing elit.", font=('Arial', 14), fg='#777777')
        self.description_label.pack(pady=10)

        # Create a button for the call-to-action
        self.button = tk.Button(self.main_frame, text="Call to Action", font=('Arial', 14), fg='#3498db', bg='#F0F0F0', activebackground='#E0E0E0')
        self.button.pack(pady=10)

# Create the main window
root = tk.Tk()
root.title("Modern Neutral Colors")

# Create an instance of the ModernNeutralColors class
modern_neutral_colors = ModernNeutralColors(root)

# Run the application
root.mainloop()