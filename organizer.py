import os
import shutil
import time
import threading
from tkinter import Tk, Label, Text, END, IntVar, PhotoImage, filedialog
from tkinter import ttk
from plyer import notification

def select_folder():
    global download_folder
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        download_folder = folder_selected
        folder_label.config(text=f"Cartella selezionata: {download_folder}")

def start_monitoring():
    global monitoring_active
    monitoring_active = True
    log_text.insert(END, "Monitoraggio avviato...\n")
    process_existing_files()  
    monitor_thread = threading.Thread(target=monitor_folder)
    monitor_thread.daemon = True
    monitor_thread.start()
    status_label.config(text="Stato: Attivo", foreground="green")

def stop_monitoring():
    global monitoring_active
    monitoring_active = False
    status_label.config(text="Stato: Inattivo", foreground="red")
    log_text.insert(END, "Monitoraggio interrotto.\n")

def send_grouped_notification(files_moved):
    if len(files_moved) == 1:
        file_name = files_moved[0][0]  
        folder_name = files_moved[0][1]  
        notification.notify(
            title="Organizer by HappyCoding",
            message=f"Il file {file_name} è stato spostato nella cartella {folder_name}.",
            timeout=5  
        )
    else:
        total_files = len(files_moved)
        folder_names = {f[1] for f in files_moved}  
        folders_str = ', '.join(folder_names)
        notification.notify(
            title="Organizer by HappyCoding",
            message=f"{total_files} file sono stati spostati nelle cartelle: {folders_str}.",
            timeout=5  
        )

def move_file(file_name, extension, files_moved):
    for folder, extensions in folders.items():
        if extension in extensions:
            dest_folder = os.path.join(download_folder, folder)

            if create_subfolders_var.get() == 1:
                dest_folder = os.path.join(dest_folder, extension)

            if not os.path.exists(dest_folder):
                os.makedirs(dest_folder)

            shutil.move(
                os.path.join(download_folder, file_name),
                os.path.join(dest_folder, file_name)
            )
            files_moved.append((file_name, folder))
            log_text.insert(END, f"Spostato {file_name} nella cartella {dest_folder}.\n")
            return

    
    others_folder = os.path.join(download_folder, "others")
    if not os.path.exists(others_folder):
        os.makedirs(others_folder)
    shutil.move(
        os.path.join(download_folder, file_name),
        os.path.join(others_folder, file_name)
    )
    files_moved.append((file_name, "others"))
    log_text.insert(END, f"Spostato {file_name} nella cartella 'others'.\n")


def is_file_complete(file_path):
    if any(file_path.endswith(ext) for ext in temp_extensions):
        return False
    try:
        initial_size = os.path.getsize(file_path)
        time.sleep(1)
        final_size = os.path.getsize(file_path)
        return initial_size == final_size
    except:
        return False


def process_existing_files():
    files_moved = []  
    files_in_folder = os.listdir(download_folder)
    for file_name in files_in_folder:
        file_path = os.path.join(download_folder, file_name)
        if os.path.isfile(file_path) and is_file_complete(file_path):
            file_extension = file_name.split(".")[-1].lower()
            move_file(file_name, file_extension, files_moved)
    
    send_grouped_notification(files_moved)  

   
    for folder_name in folders.keys():
        folder_path = os.path.join(download_folder, folder_name)
        if os.path.exists(folder_path) and os.path.isdir(folder_path):
            files_in_subfolder = os.listdir(folder_path)
            for file_name in files_in_subfolder:
                file_path = os.path.join(folder_path, file_name)
                if os.path.isfile(file_path) and is_file_complete(file_path):
                    file_extension = file_name.split(".")[-1].lower()

                    
                    if create_subfolders_var.get() == 1:
                        dest_subfolder = os.path.join(folder_path, file_extension)
                        if not os.path.exists(dest_subfolder):
                            os.makedirs(dest_subfolder)
                        shutil.move(file_path, os.path.join(dest_subfolder, file_name))
                        log_text.insert(END, f"Spostato {file_name} nella sottocartella {dest_subfolder}.\n")


def monitor_folder():
    already_seen = set(os.listdir(download_folder)) 
    while monitoring_active:
        files_moved = []  
        current_files = set(os.listdir(download_folder))
        new_files = current_files - already_seen
        for file_name in new_files:
            file_path = os.path.join(download_folder, file_name)
            if os.path.isfile(file_path) and is_file_complete(file_path):
                file_extension = file_name.split(".")[-1].lower()
                move_file(file_name, file_extension, files_moved)
        if files_moved:
            send_grouped_notification(files_moved)
        
        already_seen = current_files
        time.sleep(10)

download_folder = os.path.expanduser("~/Downloads")
monitoring_active = False
folders = {
    "images": ["png", "jpg", "jpeg", "gif", "bmp", "tiff"],
    "videos": ["mp4", "mov", "avi", "mkv", "flv"],
    "compressed": ["zip", "rar", "7z", "tar", "gz"],
    "documents": ["pdf", "doc", "docx", "xls", "xlsx", "txt"],
    "audio": ["mp3", "wav", "ogg", "m4a"],
    "others": []  
}
temp_extensions = ["crdownload", "part", "tmp"]


root = Tk()
root.title("Organizer by HappyCoding")
root.geometry("600x500")
root.resizable(False, False)  


logo_path = "happycoding_logo.png"
if os.path.exists(logo_path):
    logo_img = PhotoImage(file=logo_path)
    logo_label = Label(root, image=logo_img)
    logo_label.pack(pady=10)


icon_path = "happycoding_logo.ico"  
if os.path.exists(icon_path):
    root.iconbitmap(icon_path) 


folder_label = ttk.Label(root, text=f"Cartella selezionata: {download_folder}", wraplength=400)
folder_label.pack(pady=10)


select_button = ttk.Button(root, text="Seleziona Cartella", command=select_folder)
select_button.pack(pady=5)


status_label = ttk.Label(root, text="Stato: Inattivo", foreground="red")
status_label.pack(pady=5)

start_button = ttk.Button(root, text="Avvia Monitoraggio", command=start_monitoring)
start_button.pack(pady=5)

stop_button = ttk.Button(root, text="Ferma Monitoraggio", command=stop_monitoring)
stop_button.pack(pady=5)

create_subfolders_var = IntVar()  
create_subfolders_checkbox = ttk.Checkbutton(root, text="Crea sottocartelle per estensione", variable=create_subfolders_var)
create_subfolders_checkbox.pack(pady=5)

log_text = Text(root, height=10, width=60, bg="#f5f5f5", fg="black")
log_text.pack(pady=10)

root.mainloop()
