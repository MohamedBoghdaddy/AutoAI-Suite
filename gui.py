import tkinter as tk
from file_management import classify_files
from web_scraping import scrape_and_summarize
from email_automation import send_email
from tkinter import filedialog, messagebox

def start_gui():
    root = tk.Tk()
    root.title("AutoAI Suite")

    # Label for the GUI
    label = tk.Label(root, text="Welcome to AutoAI Suite", font=("Arial", 16))
    label.pack(pady=10)

    # Button to classify files
    def classify_files_action():
        file_paths = filedialog.askopenfilenames(title="Select Files")
        labels = classify_files(file_paths)
        messagebox.showinfo("Classification Result", f"Files classified into: {labels}")

    classify_button = tk.Button(root, text="Classify Files", command=classify_files_action)
    classify_button.pack(pady=10)

    # Button for web scraping and summarization
    def summarize_action():
        url = tk.simpledialog.askstring("Input", "Enter URL to scrape:")
        summary = scrape_and_summarize(url)
        messagebox.showinfo("Summary", summary)

    summarize_button = tk.Button(root, text="Scrape & Summarize", command=summarize_action)
    summarize_button.pack(pady=10)

    # Button for sending email
    def send_email_action():
        to_address = tk.simpledialog.askstring("Input", "Recipient Email:")
        subject = tk.simpledialog.askstring("Input", "Email Subject:")
        body = tk.simpledialog.askstring("Input", "Email Body:")
        send_email(to_address, subject, body)
        messagebox.showinfo("Success", "Email sent successfully!")

    email_button = tk.Button(root, text="Send Email", command=send_email_action)
    email_button.pack(pady=10)

    # Run the GUI main loop
    root.mainloop()
