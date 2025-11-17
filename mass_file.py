import os
import shutil
from tkinter import *
from tkinter import filedialog, messagebox

def copy_file_to_folders():
    source_file = source_entry.get()  
    target_folder = target_entry.get()  

    if not os.path.isfile(source_file):
        messagebox.showwarning("Предупреждение", "Исходный файл не найден!")
        return

    if not os.path.isdir(target_folder):
        messagebox.showwarning("Предупреждение", "Целевая папка не найдена!")
        return

    folders = [os.path.join(target_folder, folder) for folder in os.listdir(target_folder)]
    count = 0

    for folder in folders:
        destination = os.path.join(folder, os.path.basename(source_file))
        try:
            shutil.copy2(source_file, destination)
            count += 1
        except Exception as e:
            print(f"Ошибка при копировании в {folder}: {e}")

    messagebox.showinfo("Готово", f"Успешно скопировано в {count} папок.")

root = Tk()
root.title("Массовая рассылка файла")

Label(root, text="Источник (файл):").grid(row=0, column=0, sticky=E)
source_entry = Entry(root, width=50)
source_entry.grid(row=0, column=1, padx=10, pady=10)
Button(root, text="Выбрать файл",
       command=lambda: source_entry.insert(0, filedialog.askopenfilename())).grid(row=0, column=2)

Label(root, text="Цель (папка с подпапками):").grid(row=1, column=0, sticky=E)
target_entry = Entry(root, width=50)
target_entry.grid(row=1, column=1, padx=10, pady=10)
Button(root, text="Выбрать папку",
       command=lambda: target_entry.insert(0, filedialog.askdirectory())).grid(row=1, column=2)

start_button = Button(root, text="Отправить файл", command=copy_file_to_folders)
start_button.grid(row=2, columnspan=3, pady=20)

root.mainloop()
