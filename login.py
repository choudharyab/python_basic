import Tkinter
import mysql.connector
class Test:
    def __init__(self):
        self.root=Tkinter.Tk()
        self.inputFrame = Tkinter.Frame(self.root)
        self.root.title("Login Form")

        self.username=Tkinter.StringVar()
        self.password=Tkinter.StringVar()
        self.connection = mysql.connector.connect(user='root', password='', host='localhost', database='python')
       # self.cursor=self.connection.cursor()
        self.setupGUI()

        self.root.mainloop()
    def setupGUI(self):
        label1 = Tkinter.Label(self.root, text='username',width=20,height=3,justify="left",anchor="w",font=("arial",10,"bold"))
        label1.grid(row=0,column=0)
        entry1 = Tkinter.Entry(self.root, textvariable=self.username)
        entry1.grid(row=0,column=1)
        label2 = Tkinter.Label(self.root, text='password',width=20,height=3,justify="left",anchor="w",font=("arial",10,"bold"))
        label2.grid(row=1,column=0)
        entry2 = Tkinter.Entry(self.root, textvariable=self.password)
        entry2.grid(row=1,column=1)
        b1= Tkinter.Button(self.root, text='Login', command=self.save,width=10,height=1,justify="left",anchor="w",font=("arial",10,"bold"))
       # b1.place(relx=0.5, rely=0.5,anchor="center")
        b1.grid(row=2,column=1)

    def save(self):
        self.username=self.username.get()
        print self.username
        self.password=self.password.get()
        print self.password

        if (self.connection):
            #self.db = mysql.connector.connect(user='root', password='', host='localhost', database='python')
            self.cursor = self.connection.cursor()


            self.cursor.execute("INSERT INTO login(username,password) VALUES  ('%s','%s')" % (self.username,self.password))
            self.connection.commit()
        else:
              print("Failed To Connect to DataBase :c")


if __name__ == "__main__":
    Test()
