from Tkinter import *
import mysql.connector
import tkFont
#Define a function to handle a button click
def button_click():
 root.destroy()
# Create the root. This will be the
# "window" for all of our activity.
root = Tk()
#root.geometry("600x500")
root.title("Chocoholics Membership List")
# Create a frame to hold the controls with a fixed height & width
myContainer = Frame(root)
myContainer.pack(side=TOP, expand=YES, fill=BOTH)
# Let's open a connection to a MySQL database
db=mysql.connector.connect(user='root', password='', host='localhost', database='python')
s="select ID, firstname,lastname,email,Dob,phone,gender,Address from registerform"
cursor = db.cursor()
cursor.execute(s)
rows = cursor.fetchall()
# Let's find out how many rows are in our result set
numrows = cursor.rowcount
# Put the Header Information on the Page
BigFont=tkFont.Font(family="Arial", size=14, weight="bold") # Font for Big Labels
HeaderFont = tkFont.Font(family="Arial", size=12, weight="bold") #Font for header
HLabel1 = Label(myContainer, text = "ID", fg = "blue", font=HeaderFont)
HLabel2 = Label(myContainer, text = "firstname", fg = "blue", font=HeaderFont)
HLabel3 = Label(myContainer, text = "lastname", fg = "blue", font=HeaderFont)
HLabel4 = Label(myContainer, text = "email", fg = "blue", font=HeaderFont)
HLabel5 = Label(myContainer, text = "dob", fg = "blue", font=HeaderFont)
HLabel6 = Label(myContainer, text = "phone", fg = "blue", font=HeaderFont)
HLabel7 = Label(myContainer, text = "gender", fg = "blue", font=HeaderFont)
HLabel8 = Label(myContainer, text = "address", fg = "blue", font=HeaderFont)
HLabelTop = Label(myContainer, text= "New Member Entry", font=BigFont, fg="red")
HLabelTop.grid(row = 0, column = 0, columnspan = 9)
HLabel1.grid(row = 1, column = 0)
HLabel2.grid(row = 1, column = 1)
HLabel3.grid(row = 1, column = 2)
HLabel4.grid(row = 1, column = 3)
HLabel5.grid(row = 1, column = 4)
HLabel6.grid(row = 1, column = 5)
HLabel7.grid(row = 1, column = 6)
HLabel8.grid(row = 1, column = 7)

# Add new labels dynamically to the root to display our data.
# Use a set of lists to hold each field of data
ID=[]
firstname = []
lastname=[]
email=[]
dob=[]
phone=[]
gender=[]
address=[]
for a in range(numrows):
 # data = rows[a][1] + " " + rows[a][3] + ". " + rows[a][2]
  myLabel = Label(myContainer,text=rows[a][0])
  ID.append(myLabel)
  myLabel1 = Label(myContainer,text=rows[a][1])
  firstname.append(myLabel1)
  myLabel2 = Label(myContainer, text = rows[a][2])
  lastname.append(myLabel2)
  myLabel3 = Label(myContainer, text = rows[a][3])
  email.append(myLabel3)
  myLabel4 = Label(myContainer, text = rows[a][4])
  dob.append(myLabel4)
  myLabel5 = Label(myContainer, text = rows[a][5])
  phone.append(myLabel5)
  myLabel6 = Label(myContainer, text = rows[a][6])
  gender.append(myLabel6)
  myLabel7 = Label(myContainer, text=rows[a][7])
  address.append(myLabel7)
btn = Button(myContainer, text = "Quit", command=button_click, height=1, width=6)
# Force the system to put all of the controls on the window.
for a in range(numrows):
 ID[a].grid(row=a+2,column=0,sticky=W)
 firstname[a].grid(row=a+2, column=1, sticky=W)
 lastname[a].grid(row=a+2, column=2, sticky=W)
 email[a].grid(row=a+2, column=3, sticky=W)
 dob[a].grid(row=a+2, column=4, sticky=W)
 phone[a].grid(row=+2, column=5, sticky=W)
 gender[a].grid(row=+2, column=6, sticky=W)
 address[a].grid(row=+2, column=7, sticky=W)

btn.grid(row=a+3,column=0,columnspan=5)
# Start things running. Note that you can
# stop this program by clicking the "close" or "Quit"
# buttons
root.mainloop()
db.close()