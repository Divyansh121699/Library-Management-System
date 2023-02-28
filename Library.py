from tkinter import*
from tkinter import ttk
import mysql.connector
import tkinter
from tkinter import messagebox


class LibraryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("2000x1120+0+0")

        #----------------------------Variable-----------------------------------

        self.member_var=StringVar()
        self.reg_no_var=StringVar()
        self.id_var=StringVar()
        self.fn_var=StringVar()
        self.ln_var=StringVar()
        self.add1_var=StringVar()
        self.add2_var=StringVar()
        self.pin_var=StringVar()
        self.mobile_var=StringVar()
        self.book_id_var=StringVar()
        self.book_t_var=StringVar()
        self.author_var=StringVar()
        self.date_of_borrow_var=StringVar()
        self.due_date_var=StringVar()
        self.no_of_days_var=StringVar()
        self.late_fee_var=StringVar()
        self.over_due_date_var=StringVar()
        self.book_price_var=StringVar()

        lbltitle=Label(self.root,text="LIBRARAY MANAGEMENT SYSTEM",bg="light blue",fg="dark blue",bd=20,relief=RIDGE,font=("times new roman",50,"bold"),padx=4,pady=6)
        lbltitle.pack(side=TOP,fill=X) 

        frame=Frame(self.root,bd=11,relief=RIDGE,padx=20,bg="light blue")
        frame.place(x=0,y=130,width=1910,height=550)
        
        #-----------------------------Data Frame Left-------------------------------

        DataFrameLeft=LabelFrame(frame,text="LIBRARAY MEMBERSHIP INFORMATION",bg="light blue",fg="BLACK",bd=20,relief=RIDGE,font=("times new roman",22 ,"bold"))
        DataFrameLeft.place(x=0,y=5,width=950,height=505)

        lblMember=Label(DataFrameLeft,text="Member Type: ",bg="light blue",fg="BLACK",bd=11,font=("times new roman",18 ,"bold"),width=12)
        lblMember.grid(row=0,column=0,sticky=W)

        comMember=ttk.Combobox(DataFrameLeft,font=("times new roman",15 ,"bold"),width=18,textvariable=self.member_var,state="readonly")
        comMember["value"]=("Admin Staff","Student","Lecturer")
        comMember.grid(row=0,column=1)

        lblReg_No=Label(DataFrameLeft,text="Registration No: ",bg="light blue",fg="BLACK",bd=11,font=("times new roman",18 ,"bold"),width=13)
        lblReg_No.grid(row=1,column=0,sticky=W)
        txtReg_No=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.reg_no_var)
        txtReg_No.grid(row=1,column=1)

        lblId_No=Label(DataFrameLeft,text="ID No: ",bg="light blue",fg="BLACK",bd=11,font=("times new roman",18 ,"bold"),width=6)
        lblId_No.grid(row=2,column=0,sticky=W)
        txtId_No=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.id_var)
        txtId_No.grid(row=2,column=1)

        lblFN=Label(DataFrameLeft,text="First Name: ",bg="light blue",fg="BLACK",bd=11,font=("times new roman",18 ,"bold"),width=10)
        lblFN.grid(row=3,column=0,sticky=W)
        txtFN=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.fn_var)
        txtFN.grid(row=3,column=1)

        lblLN=Label(DataFrameLeft,text="Last Name: ",bg="light blue",fg="BLACK",bd=11,font=("times new roman",18 ,"bold"),width=10)
        lblLN.grid(row=4,column=0,sticky=W)
        txtLN=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.ln_var)
        txtLN.grid(row=4,column=1)

        lblAdd1=Label(DataFrameLeft,text="Address Line 1: ",bg="light blue",fg="BLACK",bd=11,font=("times new roman",18 ,"bold"),width=12)
        lblAdd1.grid(row=5,column=0,sticky=W)
        txtAdd1=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.add1_var)
        txtAdd1.grid(row=5,column=1)

        lblAdd2=Label(DataFrameLeft,text="Address Line 2: ",bg="light blue",fg="BLACK",bd=11,font=("times new roman",18 ,"bold"),width=12)
        lblAdd2.grid(row=6,column=0,sticky=W)
        txtAdd2=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.add2_var)
        txtAdd2.grid(row=6,column=1)

        lblPin=Label(DataFrameLeft,text="Pincode: ",bg="light blue",fg="BLACK",bd=11,font=("times new roman",18 ,"bold"),width=8)
        lblPin.grid(row=7,column=0,sticky=W)
        txtPin=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.pin_var)
        txtPin.grid(row=7,column=1)

        lblMobile=Label(DataFrameLeft,text="Mobile No: ",bg="light blue",fg="BLACK",bd=11,font=("times new roman",18 ,"bold"),width=10)
        lblMobile.grid(row=8,column=0,sticky=W)
        txtMobile=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.mobile_var)
        txtMobile.grid(row=8,column=1)

        lblBook_Id=Label(DataFrameLeft,text="Book Id: ",bg="light blue",fg="BLACK",bd=11,font=("times new roman",18 ,"bold"),width=6)
        lblBook_Id.grid(row=0,column=3,sticky=W)
        txtBook_Id=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.book_id_var)
        txtBook_Id.grid(row=0,column=4)

        lblBook_T=Label(DataFrameLeft,text="Book Title: ",bg="light blue",fg="BLACK",bd=11,font=("times new roman",18 ,"bold"),width=8)
        lblBook_T.grid(row=1,column=3,sticky=W)
        txtBook_T=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.book_t_var)
        txtBook_T.grid(row=1,column=4)

        lblAuthor_N=Label(DataFrameLeft,text="Author Name: ",bg="light blue",fg="BLACK",bd=11,font=("times new roman",18 ,"bold"),width=10)
        lblAuthor_N.grid(row=2,column=3,sticky=W)
        txtAuthor_N=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.author_var)
        txtAuthor_N.grid(row=2,column=4)

        lblBorrow_D=Label(DataFrameLeft,text="Date of Borrow: ",bg="light blue",fg="BLACK",bd=11,font=("times new roman",18 ,"bold"),width=12)
        lblBorrow_D.grid(row=3,column=3,sticky=W)
        txtBorrow_D=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.date_of_borrow_var)
        txtBorrow_D.grid(row=3,column=4)

        lblDue_D=Label(DataFrameLeft,text="Due Date: ",bg="light blue",fg="BLACK",bd=11,font=("times new roman",18 ,"bold"),width=7)
        lblDue_D.grid(row=4,column=3,sticky=W)
        txtDue_D=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.due_date_var)
        txtDue_D.grid(row=4,column=4)

        lblDays_Valid=Label(DataFrameLeft,text="No. of Days Valid: ",bg="light blue",fg="BLACK",bd=11,font=("times new roman",18 ,"bold"),width=13)
        lblDays_Valid.grid(row=5,column=3,sticky=W)
        txtDays_Valid=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.no_of_days_var)
        txtDays_Valid.grid(row=5,column=4)

        lblLate=Label(DataFrameLeft,text="Late Return Fine: ",bg="light blue",fg="BLACK",bd=11,font=("times new roman",18 ,"bold"),width=13)
        lblLate.grid(row=6,column=3,sticky=W)
        txtLate=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.late_fee_var)
        txtLate.grid(row=6,column=4)

        lblLate_D=Label(DataFrameLeft,text="Over Due Date: ",bg="light blue",fg="BLACK",bd=11,font=("times new roman",18 ,"bold"),width=11)
        lblLate_D.grid(row=7,column=3,sticky=W)
        comMember=ttk.Combobox(DataFrameLeft,font=("times new roman",15 ,"bold"),width=18,textvariable=self.over_due_date_var,state="readonly")
        comMember["value"]=("Yes","No")
        comMember.grid(row=7,column=4)

        lblPrice=Label(DataFrameLeft,text="Book Price: ",bg="light blue",fg="BLACK",bd=11,font=("times new roman",18 ,"bold"),width=9)
        lblPrice.grid(row=8,column=3,sticky=W)
        txtPrice=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.book_price_var)
        txtPrice.grid(row=8,column=4)

        #-----------------------------Data Frame Right-----------------------------

        DataFrameLRight=LabelFrame(frame,text="BOOK DETAILS",bg="light blue",fg="BLACK",bd=20,relief=RIDGE,font=("times new roman",22,"bold"))
        DataFrameLRight.place(x=960,y=5,width=890,height=505) 

        self.txtBox=Text(DataFrameLRight, font=("times new roman",12,"bold"),width=53,height=22,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2,pady=6)

        listScroll=Scrollbar(DataFrameLRight)
        listScroll.grid(row=0,column=1,sticky="ns",padx=(0,30),pady=10)

        listbooks=['Clean Code','The Mythical Man-month','The Pragmatic Programmer: Your Journey to Mastery',
			'The Art of Computer Programming','Programming Pearls','The Code Book','Introduction to Algorithms','Refactoring:Improving the Design of Existing Code',
				'Structure and Interpretation of Computer Programs (SICP)',
                    'The Clean Coder: A Code of Conduct for Professional Programmers','Code Complete: A Practical Handbook of Software Construction',
                            'Head First Design Patterns: A Brain-Friendly Guide','Working Effectively with Legacy Code',
                            'Domain-Driven Design: Tackling Complexity in the Heart of Software','Design Patterns: Elements of Reusable Object-Oriented Software',
                            'Patterns of Enterprise Application Architecture','Enterprise Integration Patterns','Headfirst Design Patterns: A Brain-Friendly Guide','User Stories Applied: For Agile Software Development',
                            'The DevOps Handbook','Artificial Intelligence For Dummies','Artificial Intelligence: A Modern Approach','Eloquent JavaScript: A Modern Introduction to Programming',
                            ' Learning PHP, MySQL & JavaScript: With jQuery, CSS & HTML5','C++ Primer','C Programming Absolute Beginner’s Guide','R for Data Science: Import, Tidy, Transform, Visualize, and Model Data']

        def Selectbook(event=""):
            value=str(lb.get(lb.curselection()))
            x=value
            if (x=="Clean Code"):
                self.book_id_var.set("B_ID0001")
                self.book_t_var.set("Clean Code")
                self.author_var.set("Robert Cecil Martin")
                self.late_fee_var.set("Rs. 50")
                self.book_price_var.set("Rs. 1000")

            elif(x=="The Mythical Man-month"):
                self.book_id_var.set("B_ID0002")
                self.book_t_var.set("The Mythical Man-month")
                self.author_var.set("Fred Brooks")
                self.late_fee_var.set("Rs. 50")
                self.book_price_var.set("Rs. 750")

            elif(x=="The Pragmatic Programmer: Your Journey to Mastery"):
                self.book_id_var.set("B_ID0003")
                self.book_t_var.set("The Pragmatic Programmer: Your Journey to Mastery")
                self.author_var.set("Andy Hunt and Dave Thomas")
                self.late_fee_var.set("Rs. 50")
                self.book_price_var.set("Rs. 1500")
            
            elif(x=="The Art of Computer Programming"):
                self.book_id_var.set("B_ID0004")
                self.book_t_var.set("The Art of Computer Programming")
                self.author_var.set("Donald Knuth")
                self.late_fee_var.set("Rs. 50")
                self.book_price_var.set("Rs. 1000")

            elif(x=="Programming Pearls"):
                self.book_id_var.set("B_ID0005")
                self.book_t_var.set("Programming Pearls")
                self.author_var.set("Jon Bentley")
                self.late_fee_var.set("Rs. 50")
                self.book_price_var.set("Rs. 500")

            elif(x=="Programming Pearls"):
                self.book_id_var.set("B_ID0005")
                self.book_t_var.set("Programming Pearls")
                self.author_var.set("Jon Bentley")
                self.late_fee_var.set("Rs. 50")
                self.book_price_var.set("Rs. 500")

            elif(x=="The Code Book"):
                self.book_id_var.set("B_ID0006")
                self.book_t_var.set("The Code Book")
                self.author_var.set("Simon Singh")
                self.late_fee_var.set("Rs. 50")
                self.book_price_var.set("Rs. 744")

            elif(x=="Introduction to Algorithms"):
                self.book_id_var.set("B_ID0007")
                self.book_t_var.set("Introduction to Algorithms")
                self.author_var.set("Thomas H. Cormen")
                self.late_fee_var.set("Rs. 50")
                self.book_price_var.set("Rs. 560")

            elif(x=="Refactoring:Improving the Design of Existing Code"):
                self.book_id_var.set("B_ID0008")
                self.book_t_var.set("Refactoring:Improving the Design of Existing Code")
                self.author_var.set("Kent Beck and Martin Fowler")
                self.late_fee_var.set("Rs. 50")
                self.book_price_var.set("Rs. 4574")

            elif(x=="Structure and Interpretation of Computer Programs (SICP)"):
                self.book_id_var.set("B_ID0009")
                self.book_t_var.set("Structure and Interpretation of Computer Programs (SICP)")
                self.author_var.set("Gerald Jay Sussman")
                self.late_fee_var.set("Rs. 50")
                self.book_price_var.set("Rs. 4165")

            elif(x=="The Clean Coder: A Code of Conduct for Professional Programmers"):
                self.book_id_var.set("B_ID0010")
                self.book_t_var.set("The Clean Coder: A Code of Conduct for Professional Programmers")
                self.author_var.set("Robert Cecil Martin")
                self.late_fee_var.set("Rs. 50")
                self.book_price_var.set("Rs. 402")

            elif(x=="Code Complete: A Practical Handbook of Software Construction"):
                self.book_id_var.set("B_ID0011")
                self.book_t_var.set("Code Complete: A Practical Handbook of Software Construction")
                self.author_var.set("Steve McConnell")
                self.late_fee_var.set("Rs. 50")
                self.book_price_var.set("Rs. 3449")
            
            elif(x=="Head First Design Patterns: A Brain-Friendly Guide"):
                self.book_id_var.set("B_ID0012")
                self.book_t_var.set("Head First Design Patterns: A Brain-Friendly Guide")
                self.author_var.set("Eric Freeman")
                self.late_fee_var.set("Rs. 50")
                self.book_price_var.set("Rs. 8000")

            elif(x=="Working Effectively with Legacy Code"):
                self.book_id_var.set("B_ID0013")
                self.book_t_var.set("Working Effectively with Legacy Code")
                self.author_var.set("Michael Feathers")
                self.late_fee_var.set("Rs. 50")
                self.book_price_var.set("Rs. 4225")

            elif(x=="Domain-Driven Design: Tackling Complexity in the Heart of Software"):
                self.book_id_var.set("B_ID0014")
                self.book_t_var.set("Domain-Driven Design: Tackling Complexity in the Heart of Software")
                self.author_var.set("Eric Evans")
                self.late_fee_var.set("Rs. 50")
                self.book_price_var.set("Rs. 400")

            elif(x=="Design Patterns: Elements of Reusable Object-Oriented Software"):
                self.book_id_var.set("B_ID0015")
                self.book_t_var.set("Design Patterns: Elements of Reusable Object-Oriented Software")
                self.author_var.set("Erich Gamma")
                self.late_fee_var.set("Rs. 50")
                self.book_price_var.set("Rs. 400")

            elif(x=="Patterns of Enterprise Application Architecture"):
                self.book_id_var.set("B_ID0016")
                self.book_t_var.set("Patterns of Enterprise Application Architecture")
                self.author_var.set("Martin Fowler")
                self.late_fee_var.set("Rs. 50")
                self.book_price_var.set("Rs. 4167")

            elif(x=="Enterprise Integration Patterns"):
                self.book_id_var.set("B_ID0017")
                self.book_t_var.set("Enterprise Integration Patterns")
                self.author_var.set("Gregor Hohpe")
                self.late_fee_var.set("Rs. 50")
                self.book_price_var.set("Rs. 637")

            elif(x=="Headfirst Design Patterns: A Brain-Friendly Guide"):
                self.book_id_var.set("B_ID0018")
                self.book_t_var.set("Headfirst Design Patterns: A Brain-Friendly Guide")
                self.author_var.set("Eric Freeman")
                self.late_fee_var.set("Rs. 50")
                self.book_price_var.set("Rs. 8200")

            elif(x=="User Stories Applied: For Agile Software Development"):
                self.book_id_var.set("B_ID0019")
                self.book_t_var.set("User Stories Applied: For Agile Software Development")
                self.author_var.set("Mike Cohn")
                self.late_fee_var.set("Rs. 50")
                self.book_price_var.set("Rs. 3744")

            elif(x=="The DevOps Handbook"):
                self.book_id_var.set("B_ID0020")
                self.book_t_var.set("The DevOps Handbook")
                self.author_var.set("Gene Kim")
                self.late_fee_var.set("Rs. 50")
                self.book_price_var.set("Rs. 1020")

            elif(x=="Artificial Intelligence For Dummies"):
                self.book_id_var.set("B_ID0021")
                self.book_t_var.set("Artificial Intelligence For Dummies")
                self.author_var.set("John Mueller and Luca Massaron")
                self.late_fee_var.set("Rs. 50")
                self.book_price_var.set("Rs. 653")

            elif(x=="Artificial Intelligence: A Modern Approach"):
                self.book_id_var.set("B_ID0022")
                self.book_t_var.set("Artificial Intelligence: A Modern Approach")
                self.author_var.set("Peter Norvig and Stuart J. Russell")
                self.late_fee_var.set("Rs. 50")
                self.book_price_var.set("Rs. 1200")

            elif(x=="Eloquent JavaScript: A Modern Introduction to Programming"):
                self.book_id_var.set("B_ID0023")
                self.book_t_var.set("Eloquent JavaScript: A Modern Introduction to Programming")
                self.author_var.set("Marijn Haverbeke")
                self.late_fee_var.set("Rs. 50")
                self.book_price_var.set("Rs. 1600")

            elif(x=="Learning PHP, MySQL & JavaScript: With jQuery, CSS & HTML5"):
                self.book_id_var.set("B_ID0024")
                self.book_t_var.set("Learning PHP, MySQL & JavaScript: With jQuery, CSS & HTML5")
                self.author_var.set("Robin Nixon")
                self.late_fee_var.set("Rs. 50")
                self.book_price_var.set("Rs. 850")

            elif(x=="C++ Primer"):
                self.book_id_var.set("B_ID0025")
                self.book_t_var.set("C++ Primer")
                self.author_var.set("Barbara E. Moo")
                self.late_fee_var.set("Rs. 50")
                self.book_price_var.set("Rs. 4200")

            elif(x=="C Programming Absolute Beginner’s Guide"):
                self.book_id_var.set("B_ID0026")
                self.book_t_var.set("C Programming Absolute Beginner’s Guide")
                self.author_var.set("Dean Miller and Greg Perry")
                self.late_fee_var.set("Rs. 50")
                self.book_price_var.set("Rs. 2560")

            elif(x=="R for Data Science: Import, Tidy, Transform, Visualize, and Model Data"):
                self.book_id_var.set("B_ID0027")
                self.book_t_var.set("R for Data Science: Import, Tidy, Transform, Visualize, and Model Data")
                self.author_var.set("Garrett Grolemund and Hadley Wickham")
                self.late_fee_var.set("Rs. 50")
                self.book_price_var.set("Rs. 1450")

        lb=Listbox(DataFrameLRight,font=("times new roman",12,"bold"),width=40,height=21)
        lb.bind("<<ListboxSelect>>",Selectbook)
        lb.grid(row=0,column=0,padx=(30,0),pady=10) 
        listScroll.config(command=lb.yview)  

        for item in listbooks:
            lb.insert(END,item)

        #------------------------------Buttons Frame------------------------------

        framebutton=Frame(self.root,bd=11,relief=RIDGE,padx=20,bg="light blue")
        framebutton.place(x=0,y=680,width=1915,height=100)

        btnAdd=Button(framebutton,command=self.add_data,text='Add Data',font=("times new roman",12,"bold"),width=30,height=2,bg='blue',fg='white')
        btnAdd.grid(row=0,column=0,padx=(0,20),pady=13)

        btnShow=Button(framebutton,command=self.show_data,text='Show Data',font=("times new roman",12,"bold"),width=30,height=2,bg='blue',fg='white')
        btnShow.grid(row=0,column=1,padx=17,pady=13)

        btnUpdate=Button(framebutton,text='Update',command=self.update,font=("times new roman",12,"bold"),width=30,height=2,bg='blue',fg='white')
        btnUpdate.grid(row=0,column=2,padx=17,pady=13)

        btnDelete=Button(framebutton,text='Delete',command=self.delete,font=("times new roman",12,"bold"),width=30,height=2,bg='blue',fg='white')
        btnDelete.grid(row=0,column=3,padx=17,pady=13)

        btnReset=Button(framebutton,command=self.reset,text='Reset',font=("times new roman",12,"bold"),width=30,height=2,bg='blue',fg='white')
        btnReset.grid(row=0,column=4,padx=17,pady=13)

        btnExit=Button(framebutton,text='Exit',command=self.exit,font=("times new roman",12,"bold"),width=30,height=2,bg='blue',fg='white')
        btnExit.grid(row=0,column=5,padx=(17,0),pady=13)


        #------------------------------Information Frame--------------------------

        frameDetails=Frame(self.root,bd=11,relief=RIDGE,padx=20,bg="light blue")
        frameDetails.place(x=0,y=780,width=1915,height=350)

        Table_frame=Frame(frameDetails,bd=11,relief=RIDGE,padx=20,bg="light blue")
        Table_frame.place(x=0,y=14,width=1850,height=300)

        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        self.library_table=ttk.Treeview(Table_frame,column=('Member Type','Registration No.','ID No.','First Name','Last Name','Address Line 1','Address Line 2',
                                                                    'Pincode','Mobile No.','Book Id','Book Title','Author Name','Date of Borrow','Due Date',
                                                                     'No. of Days Valid','Late Return Fine','Days over Due Date','Book Price'),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)

        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        self.library_table.heading("Member Type",text="Member Type")
        self.library_table.heading("Registration No.",text="Registration No.")
        self.library_table.heading("ID No.",text="ID No.")
        self.library_table.heading("First Name",text="First Name")
        self.library_table.heading("Last Name",text="Last Name")
        self.library_table.heading("Address Line 1",text="Address Line 1")
        self.library_table.heading("Address Line 2",text="Address Line 2")
        self.library_table.heading("Pincode",text="Pincode")     
        self.library_table.heading("Mobile No.",text="Mobile No.")  
        self.library_table.heading("Book Id",text="Book Id")
        self.library_table.heading("Book Title",text="Book Title")
        self.library_table.heading("Author Name",text="Author Name") 
        self.library_table.heading("Registration No.",text="Registration No.")
        self.library_table.heading("Date of Borrow",text="Date of Borrow")
        self.library_table.heading("Due Date",text="Due Date")
        self.library_table.heading("No. of Days Valid",text="No. of Days Valid")
        self.library_table.heading("Late Return Fine",text="Late Return Fine")
        self.library_table.heading("Days over Due Date",text="Days over Due Date")
        self.library_table.heading("Book Price",text="Book Price")

        self.library_table["show"]='headings'
        self.library_table.pack(fill=BOTH,expand=1)

        self.library_table.column("Member Type",width=150)
        self.library_table.column("Registration No.",width=150)
        self.library_table.column("ID No.",width=150)
        self.library_table.column("First Name",width=150)
        self.library_table.column("Last Name",width=150)
        self.library_table.column("Address Line 1",width=200)
        self.library_table.column("Address Line 2",width=200)
        self.library_table.column("Pincode",width=150)
        self.library_table.column("Mobile No.",width=150)
        self.library_table.column("Book Id",width=150)
        self.library_table.column("Book Title",width=200)
        self.library_table.column("Author Name",width=150)
        self.library_table.column("Date of Borrow",width=150)
        self.library_table.column("Due Date",width=150)
        self.library_table.column("No. of Days Valid",width=150)
        self.library_table.column("Late Return Fine",width=150)
        self.library_table.column("Days over Due Date",width=150)
        self.library_table.column("Book Price",width=150)

        self.fetch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)

    def add_data(self):
        conn=mysql.connector.connect(host="127.0.0.1",port="3306",username="root",password="Divyans12@",database="MyDatabase")
        my_cursor=conn.cursor()
        my_cursor.execute("INSERT INTO library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                self.member_var.get(),
                                                                                                                self.reg_no_var.get(),
                                                                                                                self.id_var.get(),
                                                                                                                self.fn_var.get(),
                                                                                                                self.ln_var.get(),
                                                                                                                self.add1_var.get(),
                                                                                                                self.add2_var.get(),
                                                                                                                self.pin_var.get(),
                                                                                                                self.mobile_var.get(),
                                                                                                                self.book_id_var.get(),
                                                                                                                self.book_t_var.get(),
                                                                                                                self.author_var.get(),
                                                                                                                self.date_of_borrow_var.get(),
                                                                                                                self.due_date_var.get(),
                                                                                                                self.no_of_days_var.get(),
                                                                                                                self.late_fee_var.get(),
                                                                                                                self.over_due_date_var.get(),
                                                                                                                self.book_price_var.get()
                                                                                                                ))                                                                                                                                          
        conn.commit()
        self.fetch_data()
        conn.close()
        
        messagebox.showinfo("Success","Member has been added successfully")

    def update(self):
        conn=mysql.connector.connect(host="127.0.0.1",port="3306",username="root",password="Divyans12@",database="MyDatabase")
        my_cursor=conn.cursor()
        my_cursor.execute("UPDATE library SET Member_Type=%s,ID_No=%s,First_Name=%s,Last_Name=%s,Address_Line_1=%s,Address_Line_2=%s,Phone_No=%s,Mobile_No=%s,Book_Id=%s,Book_Title=%s,Author_Name=%s,Date_of_Borrow=%s,Due_date=%s,No_of_days=%s,Late_fee=%s,Over_due_Date=%s,book_price=%s WHERE Registration_No=%s",(
                                                                                                                self.member_var.get(),
                                                                                                                self.id_var.get(),
                                                                                                                self.fn_var.get(),
                                                                                                                self.ln_var.get(),
                                                                                                                self.add1_var.get(),
                                                                                                                self.add2_var.get(),
                                                                                                                self.pin_var.get(),
                                                                                                                self.mobile_var.get(),
                                                                                                                self.book_id_var.get(),
                                                                                                                self.book_t_var.get(),
                                                                                                                self.author_var.get(),
                                                                                                                self.date_of_borrow_var.get(),
                                                                                                                self.due_date_var.get(),
                                                                                                                self.no_of_days_var.get(),
                                                                                                                self.late_fee_var.get(),
                                                                                                                self.over_due_date_var.get(),
                                                                                                                self.book_price_var.get(),
                                                                                                                self.reg_no_var.get(),                                                                                                    
        ))
        conn.commit()
        self.fetch_data()
        self.reset()
        conn.close()

        messagebox.showinfo("Success","Member Information has been Updated")

    def fetch_data(self):
        conn=mysql.connector.connect(host="127.0.0.1",port="3306",username="root",password="Divyans12@",database="MyDatabase")
        my_cursor=conn.cursor()
        my_cursor.execute("SELECT * FROM library")
        rows=my_cursor.fetchall()

        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    
    def get_cursor(self,event=""):
        cursor_row=self.library_table.focus()
        content=self.library_table.item(cursor_row)
        row=content['values']

        self.member_var.set(row[0]),
        self.reg_no_var.set(row[1]),
        self.id_var.set(row[2]),
        self.fn_var.set(row[3]),
        self.ln_var.set(row[4]),
        self.add1_var.set(row[5]),
        self.add2_var.set(row[6]),
        self.pin_var.set(row[7]),
        self.mobile_var.set(row[8]),
        self.book_id_var.set(row[9]),
        self.book_t_var.set(row[10]),
        self.author_var.set(row[11]),
        self.date_of_borrow_var.set(row[12]),
        self.due_date_var.set(row[13]),
        self.no_of_days_var.set(row[14]),
        self.late_fee_var.set(row[15]),
        self.over_due_date_var.set(row[16]),
        self.book_price_var.set(row[17])  

    def show_data(self):
        self.txtBox.insert(END,"Member Type:\t\t\t\t"+self.member_var.get()+"\n")
        self.txtBox.insert(END,"Registration No:\t\t\t\t"+self.reg_no_var.get()+"\n")   
        self.txtBox.insert(END,"ID No:\t\t\t\t"+self.id_var.get()+"\n")
        self.txtBox.insert(END,"First Name:\t\t\t\t"+self.fn_var.get()+"\n")
        self.txtBox.insert(END,"Last Name:\t\t\t\t"+self.ln_var.get()+"\n")
        self.txtBox.insert(END,"Address Line 1:\t\t\t\t"+self.add1_var.get()+"\n")
        self.txtBox.insert(END,"Address Line 2\t\t\t\t"+self.add2_var.get()+"\n")
        self.txtBox.insert(END,"Pincode:\t\t\t\t"+self.pin_var.get()+"\n")
        self.txtBox.insert(END,"Mobile No:\t\t\t\t"+self.mobile_var.get()+"\n")
        self.txtBox.insert(END,"Book Id:\t\t\t\t"+self.book_id_var.get()+"\n")
        self.txtBox.insert(END,"Book Title\t\t\t\t"+self.book_t_var.get()+"\n")
        self.txtBox.insert(END,"Author Name:\t\t\t\t"+self.author_var.get()+"\n")
        self.txtBox.insert(END,"Date of Borrow:\t\t\t\t"+self.date_of_borrow_var.get()+"\n")
        self.txtBox.insert(END,"Due Date:\t\t\t\t"+self.due_date_var.get()+"\n")
        self.txtBox.insert(END,"No. of Days Valid:\t\t\t\t"+self.no_of_days_var.get()+"\n")                         
        self.txtBox.insert(END,"Late Return Fee:\t\t\t\t"+self.late_fee_var.get()+"\n")
        self.txtBox.insert(END,"Over Due Date:\t\t\t\t"+self.over_due_date_var.get()+"\n")
        self.txtBox.insert(END,"Book Price:\t\t\t\t"+self.book_price_var.get()+"\n")

    def reset(self):
        self.member_var.set(""),
        self.reg_no_var.set(""),
        self.id_var.set(""),
        self.fn_var.set(""),
        self.ln_var.set(""),
        self.add1_var.set(""),
        self.add2_var.set(""),
        self.pin_var.set(""),
        self.mobile_var.set(""),
        self.book_id_var.set(""),
        self.book_t_var.set(""),
        self.author_var.set(""),
        self.date_of_borrow_var.set(""),
        self.due_date_var.set(""),
        self.no_of_days_var.set(""),
        self.late_fee_var.set(""),
        self.over_due_date_var.set(""),
        self.book_price_var.set("")
        self.txtBox.delete("1.0",END)

    def exit(self):
        exit=tkinter.messagebox.askyesno("Library Management System","Do you want to exit")
        if exit>0:
            self.root.destroy()
            return
        
    def delete(self):
        if self.reg_no_var.get()=="" or self.id_var.get()=="":
            messagebox.showerror("Error","First select the member")
        else:
            conn=mysql.connector.connect(host="127.0.0.1",port="3306",username="root",password="Divyans12@",database="MyDatabase")
            my_cursor=conn.cursor()
            my_cursor.execute("DELETE FROM library WHERE Registration_No=%s",(
                self.reg_no_var.get(),
            ))

            conn.commit()
            self.fetch_data()
            self.reset()
            conn.close()

            messagebox.showinfo("Success","Member details has been deleted")

if __name__=="__main__":
    root=Tk()
    obj=LibraryManagementSystem(root)
    root.mainloop( )    