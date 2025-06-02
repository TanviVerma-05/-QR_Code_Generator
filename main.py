import tkinter as tk
from tkinter import messagebox, filedialog
import qrcode
from PIL import Image, ImageTk

# Theme state
is_dark_mode = False

def generate_qr():
    data = entry.get()
    if not data:
        messagebox.showwarning("Input Error", "Please enter text or a URL!")
        return

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("temp_qr.png")

    # Display QR code
    qr_img = Image.open("temp_qr.png")
    qr_img = qr_img.resize((200, 200))
    qr_photo = ImageTk.PhotoImage(qr_img)
    qr_label.config(image=qr_photo)
    qr_label.image = qr_photo

def save_qr():
    file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=[("PNG files", "*.png")])
    if file_path:
        img = Image.open("temp_qr.png")
        img.save(file_path)
        messagebox.showinfo("Success", f"QR Code saved as:\n{file_path}")

def toggle_theme():
    global is_dark_mode
    is_dark_mode = not is_dark_mode

    if is_dark_mode:
        bg_color = "#2e2e2e"
        fg_color = "white"
        entry_bg = "#444"
    else:
        bg_color = "white"
        fg_color = "black"
        entry_bg = "white"

    root.config(bg=bg_color)
    for widget in root.winfo_children():
        widget.config(bg=bg_color, fg=fg_color)

    entry.config(bg=entry_bg, fg=fg_color, insertbackground=fg_color)
    qr_label.config(bg=bg_color)

# --- GUI Setup ---
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("400x550")
root.resizable(False, False)
root.config(bg="white")  # Default light mode

label = tk.Label(root, text="Enter text or URL:", font=("Arial", 12), bg="white", fg="black")
label.pack(pady=10)

entry = tk.Entry(root, width=40, font=("Arial", 12), bg="white", fg="black", insertbackground="black")
entry.pack(pady=5)

generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr, bg="white", fg="black")
generate_button.pack(pady=10)

qr_label = tk.Label(root, bg="white")
qr_label.pack(pady=20)

save_button = tk.Button(root, text="Save QR Code", command=save_qr, bg="white", fg="black")
save_button.pack(pady=10)

theme_button = tk.Button(root, text="Toggle Theme", command=toggle_theme, bg="white", fg="black")
theme_button.pack(pady=10)

root.mainloop()
