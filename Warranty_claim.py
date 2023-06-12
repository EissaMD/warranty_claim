import ttkbootstrap as ttk

class App(ttk.Window):
    def __init__(self):
        super().__init__(
            title="إشعار ضمان",
            themename="flatly",
            size=(700, 800),
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
            ("Inspection Date:"     , "Inspection_date"     , "date"    ,2,1 , None),
            ("Received On:"         , "received_on"         , "entry"   ,3,1 , None),
        )
        self.basic_info = EntriesFrame(self,"Basic Info (المعلومات الاساسية)",entries)
        # Customer and Vehicle information
        entries = (
            ("Customer Name:"   , "customer_name"   , "entry"   ,0,0 , None),
            ("Customer Address:", "customer_address", "entry"   ,1,0 , None),
            ("Contact Phone:"   , "contact_phone"   , "entry"   ,2,0 , None),
            ("Car:"             , "car"             , "entry"   ,0,1 , None),
            ("Door No:"         , "door_no"         , "entry"   ,1,1 , None),
            ("Contact Email:"   , "contact_email"   , "entry"   ,2,1 , None),
        )
        self.customer_info = EntriesFrame(self,"Customer and Vehicle Info (معلومات العميل و المركبة)",entries)
        # Tire information
        entries = (
            ("Tire:"                , "tire"            , "entry"   ,0,0 , None),
            ("Tire category:"       , "tire_category"   , "entry"   ,1,0 , None),
            ("Load Index [70-170]:" , "load_index"      , "spinbox" ,2,0 , (70,170)),
            ("Origin:"              , "origin"          , "entry"   ,3,0 , None),
            ("Tire Position:"       , "tire_position"   , "menu"    ,1,1 , ("FL","FR","BL","BR")),
            ("Speed Rating:"        , "speed_rating"    , "entry"   ,2,1 , None),
            ("DOT:"                 , "dot"             , "entry"   ,3,1 , None),
        )
        self.tire_info = EntriesFrame(self,"Tire Info (معلومات الإطار)",entries)
        # Damage information
        entries = (
            ("Section:"         , "section"         , "entry"   ,0,0 , None),
            ("Type:"            , "type"            , "entry"   ,1,0 , None),
            ("Detailed Damage:" , "detailed_damage" , "entry"   ,2,0 , None),
            ("PSI:"             , "psi"             , "entry"   ,0,1 , None),
            ("BAR:"             , "bar"             , "entry"   ,1,1 , None),
            ("KPA:"             , "kpa"             , "entry"   ,2,1 , None),
        )
        self.damage_info = EntriesFrame(self,"Damage Info (معلومات الضرر)",entries)
        
        
class EntriesFrame(ttk.Labelframe):
    def __init__(self,master,title,entry_ls=()):
        self.entry_dict = {}
        super().__init__(master,text= title,  height=100)
        self.pack(fill="both" , pady =10, padx=2)
        self.entries_frame = ttk.Frame(self); self.entries_frame.pack(fill="both",expand=True,padx=4,pady=4)
        for entry in entry_ls:
            self.add_entry(entry)
        # ttk.Button(self,command=self.get_data).pack()
    def add_entry(self,entry_info):
        label, entry_name , entry_type , row , col , options=entry_info
        self.entries_frame.grid_columnconfigure(col,weight=1)
        frame = ttk.Frame(self.entries_frame)
        frame.grid(sticky="we",row=row,column=col,padx=10)
        ttk.Label(frame , text=f"{label:<20}" , font="arial 10 bold",width=20).pack(side="left" ,anchor="w")
        # entry type
        if entry_type == "entry":
            self.entry_dict[entry_name] = ttk.Entry(frame )
            self.entry_dict[entry_name].pack(side="left", fill="both" , expand=True)
        elif entry_type == "menu":
            self.entry_dict[entry_name] = ttk.StringVar()
            option_menu = ttk.OptionMenu(frame ,self.entry_dict[entry_name] ,options[0], *options , bootstyle="outline")
            option_menu.pack(side="left", fill="both" , expand=True)
            option_menu.config(width=19)
        elif entry_type == "spinbox":
            self.entry_dict[entry_name] = ttk.Spinbox(frame , from_=options[0] , to=options[1])
            self.entry_dict[entry_name].pack(side="left", fill="both" , expand=True)
        elif entry_type == "date":
            self.entry_dict[entry_name] = ttk.DateEntry(master=frame)
            self.entry_dict[entry_name].pack(side="left", fill="both" , expand=True)
            
    def get_data(self):
        data = {}
        for entry_name in self.entry_dict:
            data[entry_name] = self.entry_dict[entry_name].get()
        print(data)
        return data

if __name__ == '__main__':
    app = App()
    app.mainloop()
