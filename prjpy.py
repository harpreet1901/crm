from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

class CRM:
    def __init__(self, root):
        self.root = root
        self.root.title("Customer Relationship Management System")
        self.root.geometry("1080x900")

        # Load and set background image for main window
        self.bg_image = Image.open("img1.jpg")
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        self.bg_label = Label(self.root, image=self.bg_photo)
        self.bg_label.place(relwidth=1, relheight=1)

        # Title Labels
        lbltitle = Label(
            self.root, bd=20, relief=RIDGE,
            text="CUSTOMER RELATIONSHIP MANAGEMENT SYSTEM",
            fg="blue", bg="white", font=("Times New Roman", 30, "bold")
        )
        lbltitle.pack(side=TOP)

        lbltitle2 = Label(
            self.root, bd=20, relief=RIDGE,
            text="-------BY SP OFFICIALS", fg="blue", bg="white",
            font=("Times New Roman", 22, "bold")
        )
        lbltitle2.pack(side=TOP, fill=X)

        # Welcome Message
        welcome_label = Label(
            self.root, text="Welcome! Please click below to proceed.",
            font=("Times New Roman", 14, "bold"), bg="white"
        )
        welcome_label.pack(pady=20)

        # Main frame
        self.main_frame = Frame(self.root, bg="white")
        self.main_frame.pack(fill=BOTH, expand=True)

        # Button to open the dashboard
        self.open_dashboard_button = Button(
            self.main_frame, text="Proceed to CRM System",
            font=("Times New Roman", 15, "bold"), fg="#2d3e50", bg="white", bd=5,
            command=self.open_dashboard
        )
        self.open_dashboard_button.pack(pady=20)

        # Storage for customer details
        self.customers = {}

    def open_dashboard(self):
        # Create a new window for the dashboard
        dashboard_window = Toplevel(self.root)
        dashboard_window.title("CRM Dashboard")
        dashboard_window.geometry("800x600")

        # Load and set background image for the dashboard window
        dashboard_bg_image = Image.open("img1.jpg")
        dashboard_bg_image.putalpha(110)
        dashboard_bg_photo = ImageTk.PhotoImage(dashboard_bg_image)
        dashboard_bg_label = Label(dashboard_window, image=dashboard_bg_photo)
        dashboard_bg_label.image = dashboard_bg_photo
        dashboard_bg_label.place(relwidth=1, relheight=1)

        # Dashboard Label
        dashboard_label = Label(
            dashboard_window, text="Welcome to the CRM Dashboard!",
            font=("Times New Roman", 25, "bold"), fg="green", bg="white"
        )
        dashboard_label.pack(pady=40)

        # Buttons for different actions
        Button(dashboard_window, text="Insert Customer", font=("Times New Roman", 15, "bold"),
               command=self.open_insert_form).pack(pady=20)
        Button(dashboard_window, text="Update Customer", font=("Times New Roman", 15, "bold"),
               command=self.open_update_form).pack(pady=20)
        Button(dashboard_window, text="Delete Customer", font=("Times New Roman", 15, "bold"),
               command=self.open_delete_form).pack(pady=20)
        Button(dashboard_window, text="View Customer Details", font=("Times New Roman", 15, "bold"),
               command=self.open_view_form).pack(pady=20)
        Button(dashboard_window, text="Close Dashboard",
               command=dashboard_window.destroy, font=("Times New Roman", 15, "bold")).pack(pady=20)

    def open_insert_form(self):
        insert_window = Toplevel(self.root)
        insert_window.title("Insert Customer")
        insert_window.geometry("600x500")

        # Scrollable Frame
        scroll_frame = Frame(insert_window)
        scroll_frame.pack(fill=BOTH, expand=True)

        # Create a canvas for scrolling
        canvas = Canvas(scroll_frame)
        scrollable_frame = Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

        # Create a scrollbar
        scrollbar = Scrollbar(scroll_frame, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)

        # Form title
        Label(scrollable_frame, text="Insert Customer Details", font=("Times New Roman", 18, "bold"), fg="blue").pack(pady=20)

        # Customer details entries
        self.enrolment_id_entry = self.create_entry(scrollable_frame, "Enrolment ID")
        self.name_entry = self.create_entry(scrollable_frame, "Name")
        self.contact_entry = self.create_entry(scrollable_frame, "Contact")
        self.age_entry = self.create_entry(scrollable_frame, "Age")

        # Gender dropdown
        self.gender_combobox = self.create_combobox(scrollable_frame, "Gender", ["Male", "Female", "Other"])
        self.address_entry = self.create_entry(scrollable_frame, "Address")

        # Visa Type radio buttons
        self.visa_type = StringVar(value="Tourist")
        self.create_radio_buttons(scrollable_frame, "Visa Type", ["Tourist", "Study"], self.visa_type)

        # Visa Country dropdown
        self.visa_country_combobox = self.create_combobox(scrollable_frame, "Visa Country",
                                                           ["Canada", "USA", "Australia", "South Korea", "UK", "Dubai", "Singapore"])

        # Submit button
        Button(scrollable_frame, text="Submit", font=("Times New Roman", 14, "bold"),
               command=self.submit_customer_details).pack(pady=20)

    def create_entry(self, parent, label_text):
        label = Label(parent, text=label_text, font=("Times New Roman", 14))
        label.pack(anchor=W, padx=20, pady=5)
        entry = Entry(parent, font=("Times New Roman", 14))
        entry.pack(fill=X, padx=20, pady=5)
        return entry

    def create_combobox(self, parent, label_text, values):
        label = Label(parent, text=label_text, font=("Times New Roman", 14))
        label.pack(anchor=W, padx=20, pady=5)
        combobox = ttk.Combobox(parent, font=("Times New Roman", 14), state="readonly")
        combobox['values'] = values
        combobox.pack(fill=X, padx=20, pady=5)
        return combobox

    def create_radio_buttons(self, parent, label_text, options, variable):
        label = Label(parent, text=label_text, font=("Times New Roman", 14))
        label.pack(anchor=W, padx=20, pady=5)
        for option in options:
            radio = Radiobutton(parent, text=option, variable=variable, value=option, font=("Times New Roman", 12))
            radio.pack(anchor=W, padx=20)

    def submit_customer_details(self):
        enrolment_id = self.enrolment_id_entry.get()
        name = self.name_entry.get()
        contact = self.contact_entry.get()
        age = self.age_entry.get()
        gender = self.gender_combobox.get()
        address = self.address_entry.get()
        visa_type = self.visa_type.get()
        visa_country = self.visa_country_combobox.get()

        # Store customer details
        if enrolment_id not in self.customers:
            self.customers[enrolment_id] = {
                'name': name,
                'contact': contact,
                'age': age,
                'gender': gender,
                'address': address,
                'visa_type': visa_type,
                'visa_country': visa_country
            }

            details = (
                f"Enrolment ID: {enrolment_id}\n"
                f"Name: {name}\n"
                f"Contact: {contact}\n"
                f"Age: {age}\n"
                f"Gender: {gender}\n"
                f"Address: {address}\n"
                f"Visa Type: {visa_type}\n"
                f"Visa Country: {visa_country}"
            )

            messagebox.showinfo("Customer Details Submitted", details)
            self.clear_insert_form()
        else:
            messagebox.showwarning("Customer Exists", "Customer with this Enrolment ID already exists.")

    def clear_insert_form(self):
        self.enrolment_id_entry.delete(0, END)
        self.name_entry.delete(0, END)
        self.contact_entry.delete(0, END)
        self.age_entry.delete(0, END)
        self.gender_combobox.set('')
        self.address_entry.delete(0, END)
        self.visa_type.set("Tourist")
        self.visa_country_combobox.set('')

    def open_update_form(self):
        update_window = Toplevel(self.root)
        update_window.title("Update Customer")
        update_window.geometry("700x500")

        # Scrollable Frame
        scroll_frame = Frame(update_window)
        scroll_frame.pack(fill=BOTH, expand=True)

        # Create a canvas for scrolling
        canvas = Canvas(scroll_frame)
        scrollable_frame = Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

        # Create a scrollbar
        scrollbar = Scrollbar(scroll_frame, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)

        # Form title
        Label(scrollable_frame, text="Update Customer Details", font=("Times New Roman", 18, "bold"), fg="blue").pack(pady=20)

        self.update_enrolment_id_entry = self.create_entry(scrollable_frame, "Enrolment ID")

        Button(scrollable_frame, text="Load Customer Details", font=("Times New Roman", 14, "bold"),
               command=self.load_customer_details).pack(pady=20)

        self.update_name_entry = self.create_entry(scrollable_frame, "Name")
        self.update_contact_entry = self.create_entry(scrollable_frame, "Contact")
        self.update_age_entry = self.create_entry(scrollable_frame, "Age")
        self.update_gender_combobox = self.create_combobox(scrollable_frame, "Gender", ["Male", "Female", "Other"])
        self.update_address_entry = self.create_entry(scrollable_frame, "Address")
        self.update_visa_type = StringVar(value="Tourist")
        self.create_radio_buttons(scrollable_frame, "Visa Type", ["Tourist", "Study"], self.update_visa_type)
        self.update_visa_country_combobox = self.create_combobox(scrollable_frame, "Visa Country",
                                                                   ["Canada", "USA", "Australia", "South Korea", "UK", "Dubai", "Singapore"])

        Button(scrollable_frame, text="Update", font=("Times New Roman", 14, "bold"),
               command=self.update_customer_details).pack(pady=20)

    def load_customer_details(self):
        enrolment_id = self.update_enrolment_id_entry.get()
        if enrolment_id in self.customers:
            customer = self.customers[enrolment_id]
            self.update_name_entry.delete(0, END)
            self.update_name_entry.insert(0, customer['name'])
            self.update_contact_entry.delete(0, END)
            self.update_contact_entry.insert(0, customer['contact'])
            self.update_age_entry.delete(0, END)
            self.update_age_entry.insert(0, customer['age'])
            self.update_gender_combobox.set(customer['gender'])
            self.update_address_entry.delete(0, END)
            self.update_address_entry.insert(0, customer['address'])
            self.update_visa_type.set(customer['visa_type'])
            self.update_visa_country_combobox.set(customer['visa_country'])
        else:
            messagebox.showwarning("Customer Not Found", "No customer found with this Enrolment ID.")

    def update_customer_details(self):
        enrolment_id = self.update_enrolment_id_entry.get()
        if enrolment_id in self.customers:
            self.customers[enrolment_id]['name'] = self.update_name_entry.get()
            self.customers[enrolment_id]['contact'] = self.update_contact_entry.get()
            self.customers[enrolment_id]['age'] = self.update_age_entry.get()
            self.customers[enrolment_id]['gender'] = self.update_gender_combobox.get()
            self.customers[enrolment_id]['address'] = self.update_address_entry.get()
            self.customers[enrolment_id]['visa_type'] = self.update_visa_type.get()
            self.customers[enrolment_id]['visa_country'] = self.update_visa_country_combobox.get()

            messagebox.showinfo("Update Successful", "Customer details updated successfully.")
        else:
            messagebox.showwarning("Customer Not Found", "No customer found with this Enrolment ID.")

    def open_delete_form(self):
        delete_window = Toplevel(self.root)
        delete_window.title("Delete Customer")
        delete_window.geometry("600x400")

        Label(delete_window, text="Delete Customer", font=("Times New Roman", 18, "bold"), fg="red").pack(pady=20)

        self.delete_enrolment_id_entry = self.create_entry(delete_window, "Enrolment ID")

        Button(delete_window, text="Delete Customer", font=("Times New Roman", 14, "bold"),
               command=self.delete_customer).pack(pady=20)

    def delete_customer(self):
        enrolment_id = self.delete_enrolment_id_entry.get()
        if enrolment_id in self.customers:
            del self.customers[enrolment_id]
            messagebox.showinfo("Delete Successful", "Customer deleted successfully.")
        else:
            messagebox.showwarning("Customer Not Found", "No customer found with this Enrolment ID.")

    def open_view_form(self):
        view_window = Toplevel(self.root)
        view_window.title("View Customer Details")
        view_window.geometry("600x400")

        # Scrollable Frame
        scroll_frame = Frame(view_window)
        scroll_frame.pack(fill=BOTH, expand=True)

        # Create a canvas for scrolling
        canvas = Canvas(scroll_frame)
        scrollable_frame = Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

        # Create a scrollbar
        scrollbar = Scrollbar(scroll_frame, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)

        # Form title
        Label(scrollable_frame, text="View Customer Details", font=("Times New Roman", 18, "bold"), fg="blue").pack(pady=20)

        self.view_enrolment_id_entry = self.create_entry(scrollable_frame, "Enrolment ID")

        Button(scrollable_frame, text="View Details", font=("Times New Roman", 14, "bold"),
               command=self.view_customer_details).pack(pady=20)

    def view_customer_details(self):
        enrolment_id = self.view_enrolment_id_entry.get()
        if enrolment_id in self.customers:
            customer = self.customers[enrolment_id]
            details = (
                f"Enrolment ID: {enrolment_id}\n"
                f"Name: {customer['name']}\n"
                f"Contact: {customer['contact']}\n"
                f"Age: {customer['age']}\n"
                f"Gender: {customer['gender']}\n"
                f"Address: {customer['address']}\n"
                f"Visa Type: {customer['visa_type']}\n"
                f"Visa Country: {customer['visa_country']}"
            )
            messagebox.showinfo("Customer Details", details)
        else:
            messagebox.showwarning("Customer Not Found", "No customer found with this Enrolment ID.")

if __name__ == "__main__":
    root = Tk()
    crm_app = CRM(root)
    root.mainloop()
