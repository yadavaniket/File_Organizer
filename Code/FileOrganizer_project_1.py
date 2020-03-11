import tkinter as tk
from tkinter import ttk,filedialog
import os,shutil
from PIL import Image,ImageTk

win=tk.Tk()
win.title("One Click File Organizer")

# labels
folder=ttk.Label(win,text="Enter Your Folder Path :")
folder.grid(row=0,column=0)

# entry box
folder_path_var=tk.StringVar()
folder_path=ttk.Entry(win,width=30,textvariable=folder_path_var)
folder_path.grid(row=0,column=1)

# **************************************logic**************************************
extension_dict={
   "HTML": (".html5", ".html", ".htm", ".xhtml"),
    "IMAGES": (".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg",
               ".heif", ".psd",".PNG"),
    "VIDEOS": (".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",
               ".qt", ".mpg", ".mpeg", ".3gp", ".mkv"),
    "DOCUMENTS": (".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods",
                  ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                  ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",
                  "pptx"),
    "ARCHIVES": (".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
                 ".dmg", ".rar", ".xar", ".zip"),
    "AUDIO": (".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
              ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"),
    "PLAINTEXT": (".txt", ".in", ".out"),
    "PDF": (".pdf"),
    "PYTHON": (".py"),
    "XML": (".xml"),
    "EXE": (".exe")}

def action():
    entry_box_value=folder_path_var.get()
    if len(entry_box_value)>0:
        selected_folder=entry_box_value
    else:
        selected_folder=folder_selector()
        

    def file_finder(selected_folder_name,desired_extension):
            files=[]
            for file in os.listdir(selected_folder_name):
                for extension in desired_extension:
                    if file.endswith(extension):
                        files.append(file)
            if len(files)>0:
                return(files)
            else:
                pass



    for file_type,extension_tuple in extension_dict.items():
    # print(file_type)
        folder_name=file_type.split("_")[0]+" Files"
        folder_path=os.path.join(selected_folder,folder_name)
        # print(folder_path)
        checker=file_finder(selected_folder,extension_tuple)
        if checker is None:
            pass
        else:
            os.makedirs(folder_path, exist_ok=True)
            # presence=os.path.isdir(folder_name)
            # if presence is False:
            #     os.mkdir(folder_path)                
            # else:
            #     pass
        
        temp=file_finder(selected_folder,extension_tuple)
        if temp is None:
            pass
        else:
            for item in temp:
                item_path=os.path.join(selected_folder,item)
                item_new_path=os.path.join(folder_path,item)
                shutil.move(item_path,item_new_path)

def folder_selector():
    path_selected=filedialog.askdirectory()
    folder_path_var.set(path_selected)
    return(path_selected)
# /home/aniket/Desktop/Test

    
# ************************************logic end************************************

submit_button=ttk.Button(win,text="Begin Organizing....",command=action)
submit_button.grid(row=3,columnspan=4)

# picture=PhotoImage(file='')
img=Image.open('D:\Desktop\File Organizer - Aniket Yadav/icon.png')
image1=ImageTk.PhotoImage(img)

# image1=tk.PhotoImage(file='/home/aniket/Desktop/Python Projects/icon.png')
select_folder_button=ttk.Button(win,image=image1,command=folder_selector)
select_folder_button.grid(row=0,column=3)
win.mainloop()
