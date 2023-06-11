import ttkbootstrap as ttk
from tkinter.filedialog import askopenfilename
from tkinter.scrolledtext import ScrolledText


class App(ttk.Window):
    def __init__(self):
        super().__init__(
            title="إشعار ضمان",
            themename="flatly",
            size=(700, 700),
            # resizable=(False, False),
        )
        # title
        frame = ttk.Frame(self ,bootstyle="dark" )
        frame.pack(fill="both" , anchor="e")
        ttk.Label(frame , text="إشعار ضمان" , font="arial 32 bold" ,  bootstyle="inverse" ,).pack()
        ttk.Separator(self,bootstyle="dark").pack(fill="both" , pady=4)
        # Basic information
        entries = (
            ("Warranty Claim:"      , "warranty_claim"      , "menu"    ,0,0 , ("Accepted - مقبول", "Rejected - مرفوض")),
            ("Distributer:"         , "distribute"          , "entry"   ,1,0 , None),
            ("Location:"            , "location"            , "entry"   ,2,0 , None),
            ("Inspection Center:"   , "inspection_center"   , "entry"   ,3,0 , None),
            ("Technical Inspector:" , "technical_inspector" , "entry"   ,1,1 , None),
            ("Inspection Date:"     , "Inspection_date"     , "entry"   ,2,1 , None),
            ("Received On:"         , "received_on"         , "entry"   ,3,1 , None),
        )
        self.basic_info = EntriesFrame(self,"Basic Information (المعلومات الاساسية)",entries)
        
        
class EntriesFrame(ttk.Labelframe):
    def __init__(self,master,title,entry_ls=()):
        self.entry_dict = {}
        super().__init__(master,text= title,  height=100)
        self.pack(fill="both" , pady =10, padx=2)
        self.entries_frame = ttk.Frame(self); self.entries_frame.pack(fill="both",expand=True,padx=4,pady=4)
        for entry in entry_ls:
            self.add_entry(entry)
        ttk.Button(self,command=self.get_data).pack()
    def add_entry(self,entry_info):
        label, entry_name , entry_type , row , col , options=entry_info
        self.entries_frame.grid_columnconfigure(col,weight=1)
        frame = ttk.Frame(self.entries_frame)
        frame.grid(sticky="we",row=row,column=col,padx=10)
        ttk.Label(frame , text=f"{label:<20}" , font="arial 10 bold",width=20).pack(side="left" ,anchor="w")
        if entry_type == "entry":
            self.entry_dict[entry_name] = ttk.Entry(frame )
            self.entry_dict[entry_name].pack(side="left", fill="both" , expand=True)
        elif entry_type == "menu":
            self.entry_dict[entry_name] = ttk.StringVar()
            option_menu = ttk.OptionMenu(frame ,self.entry_dict[entry_name] ,"Choose Option", *options)
            option_menu.pack(side="left", fill="both" , expand=True)
            option_menu.config(width=19)
            
    def get_data(self):
        data = {}
        for entry_name in self.entry_dict:
            data[entry_name] = self.entry_dict[entry_name].get()
        print(data)
        return data

if __name__ == '__main__':
    app = App()
    app.mainloop()
