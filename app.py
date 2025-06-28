from tkinter import *
from tkinter import ttk,filedialog
from tkinter.ttk import *
import os

root = Tk()
root.title('JPEG to PDF Converter')
root.geometry('500x400')

root.grid_rowconfigure(0,weight=2)
root.grid_rowconfigure(1,weight=1)
root.grid_columnconfigure(1,weight=3)

top_frame = Frame(root)
top_frame.grid(row=0,column=1)

hint = ttk.Label(top_frame,text="Select Image")
hint.pack()

def browse_files():
    fulll_path = filedialog.askopenfilename(title="Select image", filetypes=[("image files","*.jpeg *.png *.jpg")])
    filename = os.path.basename(fulll_path)
    label_file_explorer.configure(text=f"{filename}")
    hint.configure(text='Selected Image: \n')



# files_box = Text(top_frame,height=20,width=80,bg='light yellow')
# files_box.pack(anchor='center')


label_file_explorer  = ttk.Label(top_frame,text='')
label_file_explorer.pack()




bot_frame = Frame(root)
bot_frame.grid(row=1,column=1)

files_btn = ttk.Button(bot_frame, text="Choose image",command=browse_files)
files_btn.pack()

convert_btn = ttk.Button(bot_frame,text="Convert Image to PDF")
convert_btn.pack()






root.mainloop()

