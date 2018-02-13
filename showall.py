import Tkinter
from Tkinter import Tk, Frame, Button, NO, Toplevel, StringVar
import ttk
import mysql.connector

def setupGUI(a1):
    root = Tkinter.Tk()
    id = Tkinter.StringVar()
    id = a1[0]
    print id
    print("*********Before updating the database********")
    firstname=a1[1]
    print firstname
    lastname=a1[2]
    print lastname
    emailid=a1[3]
    print emailid
    dob=a1[4]
    print dob
    phone=a1[5]
    print phone
    gender=a1[6]
    print gender
    address=a1[7]
    print address
    country=a1[8]
    print country
    state=a1[9]
    print state
    city=a1[10]
    print city
    lb1 = Tkinter.Label(root, text="First Name", width=20, height=3, justify="left", anchor="w",
                        font=("arial", 10, "bold"))
    lb1.grid(row=0, column=0)

    E1 = Tkinter.Entry(root, textvariable="firstname", width=25)
    E1.setvar("firstname",firstname)
    E1.grid(row=0, column=1)

    lb2 = Tkinter.Label(root, text="Last Name", width=20, height=3, justify="left", anchor="w",
                        font=("arial", 10, "bold"))
    lb2.grid(row=1, column=0)

    E2 = Tkinter.Entry(root, textvariable="lastname", width=25)
    E2.setvar("lastname", lastname)
    E2.grid(row=1, column=1)
    lb3 = Tkinter.Label(root, text="Email ID", width=20, height=3, justify="left", anchor="w",
                        font=("arial", 10, "bold"))
    lb3.grid(row=2, column=0)
    E3 = Tkinter.Entry(root, textvariable="emailid", width=25)
    E3.setvar("emailid", emailid)
    E3.grid(row=2, column=1)
    lb4 = Tkinter.Label(root, text="Date of Birth", width=20, height=3, justify="left", anchor="w",
                        font=("arial", 10, "bold"))
    lb4.grid(row=3, column=0)
    E4 = Tkinter.Entry(root, textvariable="dob", width=25)
    E4.setvar("dob", dob)
    E4.grid(row=3, column=1)
    lb5 = Tkinter.Label(root, text="Phone", width=20, height=3, justify="left", anchor="w",
                        font=("arial", 10, "bold"))
    lb5.grid(row=4, column=0)
    E5 = Tkinter.Entry(root, textvariable="phone", width=25)
    E5.setvar("phone",phone)
    E5.grid(row=4, column=1)
    lb6 = Tkinter.Label(root, text="Gender", width=20, height=3, justify="left", anchor="w",
                        font=("arial", 10, "bold"))
    lb6.grid(row=5, column=0)
    E6 = Tkinter.Entry(root, textvariable="gender", width=25)
    E6.setvar("gender",gender)
    E6.grid(row=5, column=1)
    lb7 = Tkinter.Label(root, text="address", width=20, height=3, justify="left", anchor="w",
                        font=("arial", 10, "bold"))
    lb7.grid(row=6, column=0)
    E7 = Tkinter.Entry(root, textvariable="address", width=25)
    E7.setvar("address", address)
    E7.grid(row=6, column=1)
    lb8 = Tkinter.Label(root, text="country", width=20, height=3, justify="left", anchor="w",
                        font=("arial", 10, "bold"))
    lb8.grid(row=7, column=0)
    E8 = Tkinter.Entry(root, textvariable="country", width=25)
    E8.setvar("country",country)
    E8.grid(row=7, column=1)
    lb9 = Tkinter.Label(root, text="state", width=20, height=3, justify="left", anchor="w",
                        font=("arial", 10, "bold"))
    lb9.grid(row=8, column=0)
    E9 = Tkinter.Entry(root, textvariable="state", width=25)
    E9.setvar("state",state)
    E9.grid(row=8, column=1)
    lb10 = Tkinter.Label(root, text="city", width=20, height=3, justify="left", anchor="w",
                        font=("arial", 10, "bold"))
    lb10.grid(row=9, column=0)
    E10 = Tkinter.Entry(root, textvariable="city", width=25)
    E10.setvar("city",city)
    E10.grid(row=9, column=1)

    ref2 = Tkinter.Button(root, text="Save", width=10, height=0, font=("arial", 10, "bold"),
                         command=lambda :save())
    ref2.grid(row=10, column=1)
    def save():

        con = mysql.connector.connect(user='root', password='', host='localhost', database='python')
        if(con):
           cursor = con.cursor()
           fn = E1.get()
           ln=E2.get()
           em=E3.get()
           Db=E4.get()
           ph=E5.get()
           ge=E6.get()
           add=E7.get()
           ct=E8.get()
           st=E9.get()
           ct1=E10.get()
           cursor.execute(
                   "update registerform set firstname='%s',lastname='%s',email='%s',dob='%s',phone='%s',gender='%s',address='%s',country='%s',state='%s',city='%s' where ID='%s'"%(fn,ln,em,Db,ph,ge,add,ct,st,ct1,id))         # print l_name
           con.commit()
           print ("**************After updating the database*******")
           print(fn)
           print(ln)
           print(em)
           print (Db)
           print (ph)
           print (ge)
           print(add)
           print(ct)
           print (st)
           print (ct1)
        else:
           print("Failed To Connect to DataBase :")

class Application(ttk.Frame):
    def __init__(self,master):
        """ Initialize the Frame"""
        ttk.Frame.__init__(self,master)

        self.grid()
        self.create_widgets()

    def create_widgets(self):


        self.btnDisconnect = ttk.Button(self, text="Edit data", command=self.add_data).grid(row=0, column=1)
        self.btnCancelMktData = ttk.Button(self, text='Delete', command=self.remove_all).grid(row=0, column=2)

        self.tv = ttk.Treeview(root)

        # create Treeview
        self.tv = ttk.Treeview(self, height=8)
        self.tv['columns'] = ('id','firstname','lastname','email','dob','phone','gender','address','country','state','city')
        self.tv.heading('id', text='ID')
        self.tv.column('id', anchor='center', width=70)
        self.tv.heading('firstname', text='firstname')
        self.tv.column('firstname', anchor='center', width=100)
        self.tv.heading('lastname', text='lastname')
        self.tv.column('lastname', anchor='center', width=100)
        self.tv.heading('email', text='email')
        self.tv.column('email', anchor='center', width=150)
        self.tv.heading('dob', text='dob')
        self.tv.column('dob', anchor='center', width=130)
        self.tv.heading('phone', text='phone')
        self.tv.column('phone', anchor='center', width=100)
        self.tv.heading('gender', text='gender')
        self.tv.column('gender', anchor='center', width=70)
        self.tv.heading('address', text='address')
        self.tv.column('address', anchor='center', width=130)
        self.tv.heading('country', text='country')
        self.tv.column('country', anchor='center', width=70)
        self.tv.heading('state', text='state')
        self.tv.column('state', anchor='center', width=100)
        self.tv.heading('city', text='city')
        self.tv.column('city', anchor='center', width=70)


        self.tv.bind('<ButtonRelease-1>', self.select_item)
        self.tv.grid(row=1, column=0, columnspan=6, padx=5, pady=5)

        self.treeview = self.tv


        ttk.Style().configure("Treeview", font=('', 11), background="#383838",
                              foreground="white", fieldbackground="yellow")

        self.con = mysql.connector.connect(user='root', password='', host='localhost', database='python')
        cursor = self.con.cursor()
        cursor.execute("select * from registerform")
        rows = cursor.fetchall()
        for row in rows:

            self.tv.insert('', index="end",
                        value=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]))
            print row

    def remove_all(self):
        selected_item = self.tv.selection()[0]  ## get selected item
        self.tv.delete(selected_item)



    def select_item(self,event):
        row = self.tv.selection()[0]

    def add_data(self):
        a1=[]
        test_str_library = self.tv.item(self.tv.selection())
        item = self.tv.selection()[0]  #
        t = (self.tv.item(item)['values'][0])
        self.con = mysql.connector.connect(user='root', password='', host='localhost', database='python')
        cursor = self.con.cursor()
        cursor.execute("""select * from registerform where ID = '%d'"""%(t))
        rows=cursor.fetchall()

        for row in rows:
            a1 = row
            setupGUI(a1)


root=Tk()
app=Application(root)
root.mainloop()
