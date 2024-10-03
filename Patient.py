import sqlite3
import tkinter as tk
from tkinter import messagebox
conn = sqlite3.connect('hospital_management.db')
cursor = conn.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS Patient (
    patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    dob DATE NOT NULL,
    gender TEXT NOT NULL,
    contact_number TEXT,
    address TEXT,
    medical_history TEXT
);
''')
conn.commit()
def insert_patient():
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    dob = entry_dob.get()
    gender = entry_gender.get()
    contact_number = entry_contact_number.get()
    address = entry_address.get()
    medical_history = entry_medical_history.get()
    
    if first_name and last_name and dob and gender:
        cursor.execute('''
        INSERT INTO Patient (first_name, last_name, dob, gender, contact_number, address, medical_history)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (first_name, last_name, dob, gender, contact_number, address, medical_history))
        conn.commit()
        messagebox.showinfo("Success", "Patient added successfully!")
        clear_fields()
    else:
        messagebox.showwarning("Input Error", "Please fill all required fields.")
def clear_fields():
    entry_first_name.delete(0, tk.END)
    entry_last_name.delete(0, tk.END)
    entry_dob.delete(0, tk.END)
    entry_gender.delete(0, tk.END)
    entry_contact_number.delete(0, tk.END)
    entry_address.delete(0, tk.END)
    entry_medical_history.delete(0, tk.END)


def display_patients():
    cursor.execute('SELECT * FROM Patient')
    patients = cursor.fetchall()

    display_window = tk.Toplevel(root)
    display_window.title("All Patients")
    
    text = tk.Text(display_window, width=100, height=20)
    text.pack()

    text.insert(tk.END, "Patient ID | First Name | Last Name | DOB | Gender | Contact Number | Address | Medical History\n")
    text.insert(tk.END, "-"*100 + "\n")
    
    for patient in patients:
        text.insert(tk.END, f"{patient[0]} | {patient[1]} | {patient[2]} | {patient[3]} | {patient[4]} | {patient[5]} | {patient[6]} | {patient[7]}\n")


root = tk.Tk()
root.title("Patient Information")


tk.Label(root, text="First Name").grid(row=0, column=0, padx=10, pady=5)
entry_first_name = tk.Entry(root)
entry_first_name.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Last Name").grid(row=1, column=0, padx=10, pady=5)
entry_last_name = tk.Entry(root)
entry_last_name.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Date of Birth (YYYY-MM-DD)").grid(row=2, column=0, padx=10, pady=5)
entry_dob = tk.Entry(root)
entry_dob.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Gender").grid(row=3, column=0, padx=10, pady=5)
entry_gender = tk.Entry(root)
entry_gender.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Contact Number").grid(row=4, column=0, padx=10, pady=5)
entry_contact_number = tk.Entry(root)
entry_contact_number.grid(row=4, column=1, padx=10, pady=5)

tk.Label(root, text="Address").grid(row=5, column=0, padx=10, pady=5)
entry_address = tk.Entry(root)
entry_address.grid(row=5, column=1, padx=10, pady=5)

tk.Label(root, text="Medical History").grid(row=6, column=0, padx=10, pady=5)
entry_medical_history = tk.Entry(root)
entry_medical_history.grid(row=6, column=1, padx=10, pady=5)

add_button = tk.Button(root, text="Add Patient", command=insert_patient)
add_button.grid(row=7, column=0, columnspan=2, pady=10)

display_button = tk.Button(root, text="Display All Patients", command=display_patients)
display_button.grid(row=8, column=0, columnspan=2, pady=10)


root.mainloop()
conn.close()


