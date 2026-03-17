import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import os

def convertir():
    archivo = filedialog.askopenfilename(
        title="Selecciona una imagen",
        filetypes=[("Imágenes", "*.jpg *.jpeg *.png *.bmp *.gif *.webp")]
    )
    if not archivo:
        return

    salida_formato = formato_var.get()
    carpeta_salida = filedialog.askdirectory(title="Selecciona carpeta de salida")
    if not carpeta_salida:
        return

    try:
        img = Image.open(archivo)
        
        if salida_formato == "ICO":
            img = img.resize((256, 256))

        nombre_base = os.path.splitext(os.path.basename(archivo))[0]
        salida_path = os.path.join(carpeta_salida, f"{nombre_base}.{salida_formato.lower()}")
        img.save(salida_path, salida_formato.upper())
        messagebox.showinfo("Éxito", f"Imagen convertida a {salida_formato} en:\n{salida_path}")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo convertir la imagen:\n{e}")

root = tk.Tk()
root.title("Conversor de Imágenes")

formato_var = tk.StringVar(value="PNG")
opciones = ["PNG", "JPG", "WEBP", "BMP", "ICO"]

tk.Label(root, text="Formato de salida:").pack(pady=5)
tk.OptionMenu(root, formato_var, *opciones).pack(pady=5)
tk.Button(root, text="Convertir Imagen", command=convertir).pack(pady=20)

root.mainloop()
