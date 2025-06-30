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

hint = ttk.Label(top_frame,text="Select Images")
hint.pack()


label_file_explorer  = ttk.Label(top_frame,text='')
label_file_explorer.pack()




bot_frame = Frame(root)
bot_frame.grid(row=1,column=1)

saved_label = ttk.Label(bot_frame,text='')
saved_label.pack()

def browse_files():
    global selected_files,files_list
    files_list = [] 
    selected_files = filedialog.askopenfilenames(title="Select images", filetypes=[("image files","*.jpeg *.png *.jpg")])
    
    for path in selected_files:
        filename = os.path.basename(path)
        files_list.append(filename)
        files_list_text = "\n".join(files_list)

    label_file_explorer.configure(text=f"{files_list_text}")
    hint.configure(text='Selected Images: \n')


def convert_to_single_pdf():
    global selected_files,files_list
    if len(files_list) < 1:
        label_file_explorer.configure(text="Please select at least 1 image!")
        return
    
    save_path = filedialog.asksaveasfilename(defaultextension='.pdf',
                                             filetypes=[("PDF files","*.pdf")],
                                             title="Save as PDF")
    
    if not save_path:
        return
    try:
        a4input = (img2pdf.mm_to_pt(210),img2pdf.mm_to_pt(297))
        layout_fun = img2pdf.get_layout_fun(a4input,fit = img2pdf.FitMode.shrink)

        with open(save_path,"wb") as f:
            f.write(img2pdf.convert(selected_files,layout_fun=layout_fun))
            saved_label.configure(text=f"Saved to {save_path}")
    except Exception as e:
        saved_label.configure(text=f"Error: {e}")

def convert_to_seperate_pdfs():
    global selected_files,files_list
    if len(files_list) < 1:
        label_file_explorer.configure(text="Please select at least 1 image!")
        return
    
    save_dir = filedialog.askdirectory(title="Select folder to save PDFs")

    if not save_dir:
        return
    

    try:
        # Used for resizing the images to fit A4 format
        # a4input = (img2pdf.mm_to_pt(210),img2pdf.mm_to_pt(297))
        # layout_fun = img2pdf.get_layout_fun(a4input,fit = img2pdf.FitMode.shrink)

        for img_path in selected_files:
            img_name = os.path.splitext(os.path.basename(img_path))[0]
            output_path = os.path.join(save_dir,f"{img_name}.pdf")

            with open(output_path,"wb") as f:
                f.write(img2pdf.convert([img_path])) # add "layout_fun=layout_fun" for a4 resizing
        
        saved_label.configure(text=f"Saved {len(selected_files)} files to :\n {save_dir}")

    except Exception as e:
        saved_label.configure(text=f"Error: {e}")
        print(e)

files_btn = ttk.Button(bot_frame, text="Choose images",command=browse_files)
files_btn.pack()

single_pdf_btn = ttk.Button(bot_frame,text="Convert images to single PDF",command=convert_to_single_pdf)
single_pdf_btn.pack()
multiple_pdf_btn = ttk.Button(bot_frame,text="Convert images to seperate PDFs",command=convert_to_seperate_pdfs)
multiple_pdf_btn.pack()

root.mainloop()

