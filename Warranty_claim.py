import ttkbootstrap as ttk
from tkinter.filedialog import askopenfilename
from tkinter.scrolledtext import ScrolledText


class App(ttk.Window):
    def __init__(self):
        super().__init__(
            title="إشعار ضمان",
            themename="flatly",
            size=(700, 700),
            resizable=(False, False),
        )
        # title   bootstyle="inverse" 
        frame = ttk.Frame(self ,bootstyle="dark" )
        frame.pack(fill="both" , anchor="e")
        ttk.Label(frame , text="إشعار ضمان" , font="arial 32 bold" ,  bootstyle="inverse" ).pack()
        ttk.Separator(self,bootstyle="dark").pack(fill="both" , pady=4)
        



if __name__ == '__main__':
    app = App()
    app.mainloop()
