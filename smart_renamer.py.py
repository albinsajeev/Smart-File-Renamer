import os
import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox, ttk
import threading
import re

# --- THE CORE LOGIC ---
def process_renaming(user_selected_path, log_func, progress_func, status_func):
    # 1. Normalize Path for Windows
    raw_path = os.path.normpath(user_selected_path)
    long_path_prefix = "\\\\?\\"

    if os.name == 'nt' and not raw_path.startswith(long_path_prefix):
        folder_path = long_path_prefix + raw_path
    else:
        folder_path = raw_path

    count = 1
    
    log_func(f"--- TARGET: {raw_path} ---\n")
    status_func("Status: Scanning files...")

    try:
        # 2. Get Files in the folder
        try:
            files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        except OSError as e:
            status_func("Status: Error Accessing Folder")
            messagebox.showerror("Error", f"Could not access path:\n{e}")
            return

        # 3. Filter out non-media files (Optional: Keeps script safe from renaming itself or system files)
        ignore_files = ['smart_renamer.exe', 'smart_renamer.py', 'desktop.ini', 'thumbs.db']
        files = [f for f in files if f.lower() not in ignore_files]

        if not files:
            progress_func(100)
            status_func("Status: No files found")
            log_func("Folder is empty or contains no valid files.\n")
            return

        # 4. Sort Files (To keep them in their current order)
        # We try to sort by number if possible, otherwise alphabetical
        def smart_sort_key(name):
            # Extract the first number found in the string
            numbers = re.findall(r'\d+', name)
            if numbers:
                return int(numbers[0])
            return name
        
        files.sort(key=smart_sort_key)

        total_files = len(files)
        log_func(f"Found {total_files} files. Starting Renaming...\n")
        status_func("Status: Renaming...")

        # 5. RENAME LOOP
        for index, filename in enumerate(files):
            # Update Progress
            percentage = int(((index + 1) / total_files) * 100)
            progress_func(percentage)

            old_file_path = os.path.join(folder_path, filename)
            name_part, ext_part = os.path.splitext(filename)

            # --- CLEANING LOGIC ---
            # Regex: Remove digits, dots, underscores, spaces, hyphens from the START
            clean_name = re.sub(r'^[\d._\s-]+', '', name_part)
            
            # Safety: If the file was ONLY numbers (e.g. "001.mp4"), clean_name might be empty.
            # In that case, keep the original name part to avoid error.
            if not clean_name:
                clean_name = name_part

            # Create New Name: "001_CleanName.mp4"
            new_filename = f"{str(count).zfill(3)}_{clean_name}{ext_part}"
            new_file_path = os.path.join(folder_path, new_filename)

            # Skip if name is already correct
            if filename == new_filename:
                log_func(f"Skipped (Already correct): {filename}\n")
                count += 1
                continue

            try:
                # Check for collisions (if file exists, append _v2)
                if os.path.exists(new_file_path):
                    log_func(f"Conflict: {new_filename} exists. Skipping rename for safety.\n")
                else:
                    os.rename(old_file_path, new_file_path)
                    log_func(f"[{percentage}%] Renamed: {filename} -> {new_filename}\n")
                    count += 1
            except OSError as e:
                log_func(f"Error renaming {filename}: {e}\n")

        progress_func(100)
        status_func("Status: Completed")
        log_func("--- COMPLETED ---\n")
        messagebox.showinfo("Success", "Renaming Complete!")

    except Exception as e:
        status_func("Status: Critical Error")
        log_func(f"CRITICAL ERROR: {e}\n")
        messagebox.showerror("Critical Error", f"An unexpected error occurred:\n{e}")

# --- GUI HELPERS ---
def select_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        btn_select.config(state=tk.DISABLED, text="Running...")
        progress_bar['value'] = 0
        lbl_status.config(text="Status: Starting...", fg="blue")
        text_log.delete(1.0, tk.END)
        thread = threading.Thread(target=run_thread, args=(folder_selected,))
        thread.start()

def run_thread(folder):
    process_renaming(folder, update_log, update_progress, update_status)
    btn_select.config(state=tk.NORMAL, text="Select Folder to Rename")

def update_log(message):
    text_log.insert(tk.END, message)
    text_log.see(tk.END)

def update_progress(val):
    progress_bar['value'] = val
    root.update_idletasks()

def update_status(msg):
    lbl_status.config(text=msg)
    if "Error" in msg:
        lbl_status.config(fg="red")
    elif "Completed" in msg:
        lbl_status.config(fg="green")
    else:
        lbl_status.config(fg="blue")

# --- GUI LAYOUT ---
root = tk.Tk()
root.title("Smart Renamer (Files Only)")
root.geometry("600x500")

tk.Label(root, text="Smart File Renamer", font=("Arial", 16, "bold")).pack(pady=(15, 5))
tk.Label(root, text="Select a folder. This tool cleans filenames and re-numbers them (001, 002...)", font=("Arial", 10)).pack(pady=5)

btn_select = tk.Button(root, text="Select Folder to Rename", command=select_folder, height=2, width=25, bg="#E04F5F", fg="white", font=("Arial", 11, "bold"))
btn_select.pack(pady=15)

lbl_status = tk.Label(root, text="Status: Waiting for input...", font=("Arial", 11, "bold"), fg="gray")
lbl_status.pack(pady=5)

progress_bar = ttk.Progressbar(root, orient="horizontal", length=500, mode="determinate")
progress_bar.pack(pady=10)

text_log = scrolledtext.ScrolledText(root, height=12, width=70, font=("Consolas", 9))
text_log.pack(padx=10, pady=10)

root.mainloop()