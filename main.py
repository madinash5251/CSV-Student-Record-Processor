import tkinter as tk
from tkinter import filedialog, messagebox
from app.functions import load_csv

def main():
    # Create the main window
    root = tk.Tk()
    root.title("Student Grade Analyzer")  # Set window title
    root.geometry("600x600")  # Set window size

    # Function to browse and load CSV file
    def browse_file():
        # Open a file dialog to select a CSV file
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if file_path:
            # Load the CSV file using the load_csv function from the functions module
            sorted_data, error = load_csv(file_path)
            if error:
                # Show an error message if loading the CSV file fails
                messagebox.showerror("Error", error)
            else:
                # Display student data in the GUI
                display_data(sorted_data)

    # Function to display student data in the GUI
    def display_data(dataframe):
        try:
            # Extract 'Name' and 'Average' columns, convert to list of tuples, and sort by 'Average' in descending order
            sorted_students = dataframe[['Name', 'Average']].values.tolist()
            sorted_students = sorted(sorted_students, key=lambda x: x[1], reverse=True)
            for student in sorted_students:
                # Create labels with student names and their average scores formatted to two decimal places
                label = tk.Label(root, text=f"{student[0]}, {student[1]:.2f}")
                label.pack()  # Place labels in the window vertically
        except Exception as e:
            # Show an error message if displaying the data fails
            messagebox.showerror("Error", f"Error displaying data: {e}")

    # Create a button to load CSV file when clicked
    load_button = tk.Button(root, text="Load CSV", command=browse_file)
    load_button.pack()  # Place the button in the window

    # Run the main GUI event loop
    root.mainloop()

# Execute the main function if this script is run directly
if __name__ == "__main__":
    main()
