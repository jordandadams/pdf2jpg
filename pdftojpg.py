import tkinter as tk
from tkinter import filedialog
from pdf2image import convert_from_path
from tkinter import messagebox
        
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('PDF to JPG Converter')
        self.file_var = tk.StringVar()
        self.poppler_var = tk.StringVar()
        txt_box = tk.Entry(self,
                        textvariable = self.file_var)
        txt_box.grid(column = 2, row = 2, padx = 10, pady = 10)
        btn = tk.Button(self,
                        text = 'Browse',
                        command=self.getFilePath)
        btn.grid(column = 1, row = 2, padx = 10, pady = 10)
        btn2 = tk.Button(self,
                        text = 'Convert',
                        command=self.pdf2img)
        btn2.grid(column = 3, row = 2, padx = 10, pady = 10)

        #poppler path
        poppler_txt_box = tk.Entry(self,
                        textvariable = self.poppler_var)
        poppler_txt_box.grid(column = 2, row = 1, padx = 10, pady = 10)
        btn3 = tk.Button(self,
                        text = 'Path',
                        command=self.getPopplerPath)
        btn3.grid(column = 1, row = 1, padx = 10, pady = 10)

    def getFilePath(self):
        self.file_path = filedialog.askopenfilename(initialdir = "/",
                                           title = "Select a file")
        if not (".pdf") in self.file_path:
             Result = "Sorry, must be a .jpg file!"
             messagebox.showinfo("Result", Result)
             self.file_path = ''
        self.file_var.set(self.file_path)

    def getPopplerPath(self):
        self.poppler_path = filedialog.askdirectory(initialdir = "/",
                                           title = "Select path")
        if not ("bin") in self.poppler_path:
             Result = "Sorry, must be the bin path directory!"
             messagebox.showinfo("Result", Result)
             self.poppler_path = ''
        self.poppler_var.set(self.poppler_path)

    def pdf2img(self):
        try:
            images = convert_from_path(str(self.file_path), poppler_path=str(self.poppler_path))
            for img in images:
                img.save(str(self.file_path).lower().replace(".pdf",".jpg"),'JPEG')
    
        except:
            Result = "Sorry, no pdf found!"
            messagebox.showinfo("Result", Result)
    
        else:
            Result = "Success!"
            messagebox.showinfo("Result", Result)


if __name__ == "__main__":
    app = App()
    app.mainloop()