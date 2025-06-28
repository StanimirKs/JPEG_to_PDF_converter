from tkinter import *
from tkinter import ttk,filedialog
from tkinter.ttk import *
import os
import img2pdf

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


label_file_explorer  = ttk.Label(top_frame,text='')
label_file_explorer.pack()




bot_frame = Frame(root)
bot_frame.grid(row=1,column=1)

saved_label = ttk.Label(bot_frame,text='')
saved_label.pack()

def browse_files():
    global full_path,filename
    full_path = filedialog.askopenfilename(title="Select image", filetypes=[("image files","*.jpeg *.png *.jpg")])
    filename = os.path.basename(full_path)
    label_file_explorer.configure(text=f"{filename}")
    hint.configure(text='Selected Image: \n')

def convert_image():
    global full_path,filename
    if not filename:
        label_file_explorer.configure(text="Please select an image")
        return
    
    save_path = filedialog.asksaveasfilename(defaultextension='.pdf',
                                             filetypes=[("PDF files","*.pdf")],
                                             initialfile=os.path.splitext(filename)[0] + '.pdf',
                                             title="Save as PDF")
    
    if not save_path:
        return
    try:
        with open(save_path,"wb") as f:
            f.write(img2pdf.convert(full_path))
            saved_label.configure(text=f"Saved to {save_path}")
    except Exception as e:
        saved_label.configure(text=f"Error: {e}")


files_btn = ttk.Button(bot_frame, text="Choose image",command=browse_files)
files_btn.pack()

convert_btn = ttk.Button(bot_frame,text="Convert Image to PDF",command=convert_image)
convert_btn.pack()

root.mainloop()

