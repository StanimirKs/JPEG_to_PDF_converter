from tkinter import *
from tkinter import ttk,filedialog
from tkinter.ttk import *

root = Tk()
root.title('JPEG to PDF Converter')
root.geometry('600x600')

top_frame = Frame(root)
top_frame.pack()

def browse_files():
    filename = filedialog.askopenfilename(title="Select image",
                                          filetypes=[("image files","*.jpeg *.png *.jpg")])
    label_file_explorer.configure( text="Chosen image: \n" + filename)

files_btn = ttk.Button(top_frame, text="Choose image",command=browse_files)
files_btn.pack(anchor="center")

# files_box = Text(top_frame,height=20,width=80,bg='light yellow')
# files_box.pack(anchor='center')

bot_frame = Frame(root)
bot_frame.pack(side="bottom")




label_file_explorer  = ttk.Label(top_frame,text='')
label_file_explorer.pack()


root.mainloop()

