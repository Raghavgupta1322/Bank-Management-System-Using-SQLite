from tkinter import *
import dataBase
from tkinter import messagebox
from tkinter import ttk
from PIL import Image,ImageTk

root =Tk()
root.configure(background="skyblue")
root.geometry("900x450")
root.title("Bank Management System")
# img = Image.open("img/back.jpg")
# background_image = ImageTk.PhotoImage(img)
# background_label = Label(root, image=background_image)
# # background_label.place(relwidth=1, relheight=1)
# background_label.pack()
# ------------------------
font1 =('Arial', 12, 'bold')
bcolor='#000'
btnclr='#ff6690'

#Functions
def front():
    import cv2
    img = cv2.imread("img/front.png")
    cv2.imshow("FrontPage",img)
    cv2.waitKey(1500)
    cv2.destroyAllWindows()

def insrec():
    id = identry.get()
    name = nameentry.get()
    fname = fnameentry.get()
    phone = phoneentry.get()
    balance = balentry.get()
    if not(id and name and fname and phone and balance):
        messagebox.showerror("Error","Please Fill All Fields")
    elif dataBase.id_exits(id):
        messagebox.showerror("Error","Id Has already exits")
    else:
        val = dataBase.openaccount(id,name,fname,phone,balance)
        messagebox.showinfo("Sucess","Account Open Sucess....")
    identry.delete(0,END)
    nameentry.delete(0,END)
    fnameentry.delete(0,END)
    phoneentry.delete(0,END)
    balentry.delete(0,END)
    for i in val:
        tree.insert("",END,values=i)


def ondeposite():
    rot =Tk()
    rot.configure(background="pink")
    rot.geometry("500x300")
    lableid = Label(rot, text="ID", fg='white', bg=bcolor, font=font1)
    lableid.place(x=30, y=30)
    identry = Entry(rot, width=20, font=font1)
    identry.place(x=30, y=70)
    labledep = Label(rot,text="Enter the Money You want to deposite.",fg="white",bg=bcolor,font=font1)
    labledep.place(x=30,y=100)
    entrydep = Entry(rot,width=20,font=font1)
    entrydep.place(x=30,y=130)
    def deposite():
        id = int(identry.get())
        money = int(entrydep.get())
        res = dataBase.depositemoney(id,money)
        if not (str(id) and str(money)):
            messagebox.showerror("Error","Please fill all fields.")
        elif res==0:
            messagebox.showerror("Error","Record not found.")
            identry.delete(0,END)
        else:
            messagebox.showinfo("Sucess","Money Deposite sucess....")
            update()
        rot.destroy()
    btn = Button(rot,text="Deposite",fg="white",bg=btnclr,font=font1,command=deposite)
    btn.place(x=30,y=170)
    # deposite()
    rot.mainloop()

def onwithdraw():
    win = Tk()
    win.configure(background="orange")
    win.geometry("500x300")
    lableid = Label(win, text="ID", fg='white', bg=bcolor, font=font1)
    lableid.place(x=30, y=30)
    identry = Entry(win, width=20, font=font1)
    identry.place(x=30, y=70)
    lablewith = Label(win, text="Enter the Money You want to Withdraw.", fg="white", bg=bcolor, font=font1)
    lablewith.place(x=30, y=100)
    entrywith = Entry(win, width=20, font=font1)
    entrywith.place(x=30, y=130)
    def withdraw():
        id = identry.get()
        money = int(entrywith.get())
        if not (id and money):
            messagebox.showerror("Error","Please fill all fields.")
        res= dataBase.wihdrawmoney(id, money)
        if res==0:
            messagebox.showerror("Error","Record not found.")
            identry.delete(0, END)
        else:
            messagebox.showinfo("Sucess","Money has Withdrawd.")
            update()
        win.destroy()
    btn = Button(win,text="Withdraw",fg="white",bg=btnclr,font=font1,command=withdraw)
    btn.place(x=30,y=170)
    win.mainloop()

def viewbalance():
    id = identry.get()
    if not (id):
        messagebox.showerror("Error","Please enter the ID")
    balance = dataBase.viewbalance(id)
    if balance ==0:
        messagebox.showerror("Error","Record not found.")
        identry.delete(0,END)
    else:
        balentry.delete(0,END)
        balentry.insert(0,balance)
    nameentry.delete(0,END)
    fnameentry.delete(0,END)
    phoneentry.delete(0,END)

def viwecustomer():
    id = identry.get()
    if not(id):
        messagebox.showerror("Error","please enter the ID")
    row = dataBase.customer(id)
    if row ==0:
        messagebox.showerror("Error","Record not found.")
    else:
        identry.delete(0,END)
        identry.insert(0,row[0][0])

        nameentry.delete(0,END)
        nameentry.insert(0,row[0][1])

        fnameentry.delete(0,END)
        fnameentry.insert(0,row[0][2])

        phoneentry.delete(0,END)
        phoneentry.insert(0,row[0][3])

        balentry.delete(0,END)
        balentry.insert(0,row[0][4])

def deleteCustomer():
    id = identry.get()
    if not (id):
        messagebox.showerror("Error","Please enter the ID")
    res = dataBase.delete(id)
    if res==0:
        messagebox.showerror("Error","Record not found.")
    else:
        messagebox.showinfo("Suces","Customer has deleted.")
        update()
    identry.delete(0,END)
    # tree.delete(id)

def dep():
    id = identry.get()
    money= balentry.get()
    if not (id and money):
        messagebox.showerror("Error", "Please enter ID and Balance ")
    res = dataBase.depositemoney(int(id), int(money))
    if res == 0:
        messagebox.showerror("Error", "Record not found.")
        identry.delete(0, END)
        balentry.delete(0, END)
    else:
        messagebox.showinfo("Sucess", "Money Deposite sucess....")
    update()
    identry.delete(0,END)
    nameentry.delete(0, END)
    fnameentry.delete(0, END)
    phoneentry.delete(0, END)
    balentry.delete(0,END)

def withd():
    id = identry.get()
    money = balentry.get()
    bal = int(money)
    if not (id and money):
        messagebox.showerror("Error", "Please enter ID and Balance.")
    res = dataBase.wihdrawmoney(int(id), int(money))
    userbal = res[0][0]
    if res == 0:
        messagebox.showerror("Error", "Record not found.")
        identry.delete(0, END)
    elif bal>userbal:
        messagebox.showerror("Error","Insufficient balance.")
    else:
        messagebox.showinfo("Sucess", "Money has Withdrawd.")
    update()
    identry.delete(0, END)
    nameentry.delete(0, END)
    fnameentry.delete(0, END)
    phoneentry.delete(0, END)
    balentry.delete(0, END)


# Making interface
# ------------------------------------
idlable= Label(root,text="ID",fg='white',bg=bcolor,font=font1)
idlable.place(x=30,y=30)
identry= Entry(root,width=20,font=font1)
identry.place(x=130,y=30)
# --------------------------------------------
namelable= Label(root,text="Name",fg='white',bg=bcolor,font=font1)
namelable.place(x=30,y=70)
nameentry= Entry(root,width=20,font=font1)
nameentry.place(x=130,y=70)
# ----------------------------------------------------
fnamelable= Label(root,text="FName",fg='white',bg=bcolor,font=font1)
fnamelable.place(x=30,y=110)
fnameentry= Entry(root,width=20,font=font1)
fnameentry.place(x=130,y=110)
# ------------------------------------------------------
phonelable= Label(root,text="Phone",fg='white',bg=bcolor,font=font1)
phonelable.place(x=30,y=150)
phoneentry= Entry(root,width=20,font=font1)
phoneentry.place(x=130,y=150)
# -------------------------------------------------------
ballable= Label(root,text='Balance',fg='white',bg=bcolor,font=font1)
ballable.place(x=30,y=190)
balentry= Entry(root,width=20,font=font1)
balentry.place(x=130,y=190)
# -------------------------------------------------------
#Button
openbtn= Button(root,text="Open Account",fg='white',bg=btnclr,font=font1,command=insrec)
openbtn.place(x=40,y=250)
# ---------------------------------
depbtn= Button(root,text="Deposite Money",fg='white',bg=btnclr,font=font1,command=dep)
depbtn.place(x=195,y=250)
# -----------------------------
withbtn=Button(root,text="Withdraw Money",fg='white',bg=btnclr,font=font1,command=withd)
withbtn.place(x=360,y=250)
# ----------------------------------------
viewbtn= Button(root,text="View Balance",fg="white",bg=btnclr,font=font1,command=viewbalance)
viewbtn.place(x=110,y=300)
# --------------------------------------
cusbtn= Button(root,text="View Customer Details",fg='white',bg=btnclr,font=font1,command=viwecustomer)
cusbtn.place(x=265,y=300)
# --------------------------------------------
delcus= Button(root,text="Delete Customer",fg="White",bg=btnclr,font=font1,command=deleteCustomer)
delcus.place(x=200,y=350)
# -----------------------------------------------
# Exit Button
exitbtn=Button(root,text="Exit",fg="white",bg=btnclr,font=font1,command=root.destroy)
exitbtn.place(x=250,y=400)

# making deposite and onwithdraw interface and entry

# Table for data
tree = ttk.Treeview(root)

tree["columns"]=("Id","Name","Fname","Phone","Balance")

tree.column("#0",width=0,stretch=NO)
tree.column("Id",anchor=CENTER,width=80)
tree.column("Name",anchor=W,width=100)
tree.column("Fname",anchor=CENTER,width=100)
tree.column("Phone",anchor=CENTER,width=110)
tree.column("Balance",anchor=CENTER,width=120)

tree.heading("#0",text="",anchor=CENTER)
tree.heading("Id",text="ID",anchor=CENTER)
tree.heading("Name",text="Name",anchor=CENTER)
tree.heading("Fname",text="Fname",anchor=CENTER)
tree.heading("Phone",text="Phone",anchor=CENTER)
tree.heading("Balance",text="Balance",anchor=CENTER)

tree.place(x=350,y=10)
def update():
    res = dataBase.fetch()
    for item in tree.get_children():
        tree.delete(item)
    for i in res:
        tree.insert("",END,values=i)



front()
update()
root.mainloop()
