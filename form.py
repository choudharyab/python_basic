import Tkinter
import mysql.connector
import re
import time
from PIL import Image

from PIL import ImageTk


class Test:
    def __init__(self):
        self.root = Tkinter.Tk()
        self.inputFrame = Tkinter.Frame(self.root)

        img = Tkinter.PhotoImage(file=r'tecture.gif')
        self.root.tk.call('wm', 'iconphoto', self.root._w, img)
        #self.root.geometry("1200*1024")
        #self.root.resizable(0,0)
        self.root.title("TECTURE PVT.LTD")
        #self.root.configure(background="#e9e9e9")


        self.firstname = Tkinter.StringVar()
        self.lastname=Tkinter.StringVar()
        self.emailid = Tkinter.StringVar()
        self.dob = Tkinter.StringVar()
        self.phone = Tkinter.StringVar()
        self.gender=Tkinter.StringVar()
        self.address=Tkinter.StringVar()
        self.country=Tkinter.StringVar()
        self.state = Tkinter.StringVar()
        self.city=Tkinter.StringVar()

        self.connection = mysql.connector.connect(user='root', password='', host='localhost', database='python')
        self.setupGUI()
        self.root.mainloop()

    def setupGUI(self):


        lb1=Tkinter.Label(self.root,text="First Name",width=20,height=3,justify="left",anchor="w",font=("arial",10,"bold"))
        lb1.grid(row=0,column=0)
        E1=Tkinter.Entry(self.root,textvariable=self.firstname,width=25)
        E1.grid(row=0,column=1)
        lb2 = Tkinter.Label(self.root, text="Last Name :", width=20, height=3, justify="left", anchor="w",
                            font=("arial", 10, "bold"))
        lb2.grid(row=1, column=0)
        E2 = Tkinter.Entry(self.root, textvariable=self.lastname, width=25)
        E2.grid(row=1, column=1)
        lb3 = Tkinter.Label(self.root, text="Email ID :", width=20, height=3, justify="left", anchor="w",
                            font=("arial", 10, "bold"))
        lb3.grid(row=2, column=0)
        E3 = Tkinter.Entry(self.root, textvariable=self.emailid, width=25)
        E3.grid(row=2, column=1)
        lb4 = Tkinter.Label(self.root, text="Date_of_Birth :", height=3, width=20, justify="left", anchor="w",
                            font=("arial", 10, "bold"))
        lb4.grid(row=3, column=0)
        E4 = Tkinter.Entry(self.root, textvariable=self.dob, width=25)
        E4.grid(row=3, column=1)
        lb5 = Tkinter.Label(self.root, text="Phone No :", width=20, height=3, justify="left", anchor="w",
                            font=("arial", 10, "bold"))
        lb5.grid(row=4, column=0)
        E5 = Tkinter.Entry(self.root, textvariable=self.phone, width=25)
        E5.grid(row=4, column=1)
        lb6 = Tkinter.Label(self.root, text="Gender :", width=20, height=3, justify="left", anchor="w",
                            font=("arial", 10, "bold"))
        lb6.grid(row=5, column=0)
        E6 = Tkinter.Entry(self.root, textvariable=self.gender, width=25)
        E6.grid(row=5, column=1)
        lb7 = Tkinter.Label(self.root, text="Address :", width=20, height=3, justify="left", anchor="w",
                            font=("arial", 10, "bold"))
        lb7.grid(row=6, column=0)
        E7 = Tkinter.Entry(self.root, textvariable=self.address, width=25)
        E7.grid(row=6, column=1)
        lb8 = Tkinter.Label(self.root, text="country :", width=20, height=3, justify="left", anchor="w",
                            font=("arial", 10, "bold"))
        lb8.grid(row=7, column=0)
        E8 = Tkinter.Entry(self.root, textvariable=self.country, width=25)
        E8.grid(row=7, column=1)
        lb9 = Tkinter.Label(self.root, text="state :", width=20, height=3, justify="left", anchor="w",
                            font=("arial", 10, "bold"))
        lb9.grid(row=8, column=0)
        E9 = Tkinter.Entry(self.root, textvariable=self.state, width=25)
        E9.grid(row=8, column=1)
        lb10 = Tkinter.Label(self.root, text="city :", width=20, height=3, justify="left", anchor="w",
                            font=("arial", 10, "bold"))
        lb10.grid(row=9, column=0)
        E10 = Tkinter.Entry(self.root, textvariable=self.city, width=25)
        E10.grid(row=9, column=1)



        ref2 = Tkinter.Button(self.root, text="Submit", width=10, height=0, font=("arial", 10, "bold"),
                              command=self.save)
        #ref2.grid(row=10,column=1)
        ref2.place(relx=0.5, rely=0.98, anchor="center")

    def save(self):
        self.firstname = self.firstname.get()
        print self.firstname
        self.lastname = self.lastname.get()
        print self.lastname
        self.emailid = self.emailid.get()
        print self.emailid
        self.dob = self.dob.get()
        print self.dob
        self.phone = self.phone.get()
        print self.phone
        self.gender=self.gender.get()
        print self.gender
        self.address = self.address.get()
        print self.address
        self.country = self.country.get()
        print self.country
        self.state=self.state.get()
        print self.state
        self.city=self.city.get()
        print self.city
        rule = re.compile(r'^(\d{3}\d{3}\d{4})')
        #rule = re.compile(r'^(?:\+?44)?[07]\d{9,13}$')
        if self.firstname != "" and self.lastname != "" and self.emailid != "" and self.dob != "" and self.phone !="" and self.gender!="" and self.address!="" and self.country!="" and self.state!=" " and self.city!="":
             if ("@" in self.emailid and self.emailid.find("@") < (len(self.emailid) - 3) and   rule.search(self.phone)) :
            # if  re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", self.emailid) != None:
               print("All there!")
               self.storeData()

             else:
                print("Invalid data")
        else:
            print("Information Is Missing, Please Check Your Inputs.")
    def storeData(self):

        if (self.connection):

            self.cursor = self.connection.cursor()

            self.cursor.execute("INSERT INTO registerform(firstname,lastname,email,Dob,phone,gender,address,country,state,city) VALUES  ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (self.firstname,self.lastname,self.emailid,self.dob,self.phone,self.gender,self.address,self.country,self.state,self.city))
            self.connection.commit()
        else:
            print("Failed To Connect to DataBase :c")


if __name__ == "__main__":
    Test()
