from tkinter import *
from tkinter import messagebox
import tkinter as tk

#Functionality Part

def bill_area():
    if nameEntry.get()=='' and phoneEntry.get()=='':
        messagebox.showerror('Error','Customer Details are Required')
    elif cosmeticpriceEntry.get()=='' and grocerypriceEntry.get()=='' and drinkspriceEntry.get()=='':
        messagebox.showerror('Error', 'No Products are Selected')
    elif cosmeticpriceEntry.get()=='0 TK.' and grocerypriceEntry.get()=='0 TK.' and drinkspriceEntry.get()=='0 TK.':
        messagebox.showerror('Error', 'No Products are Selected')
    else:
        textarea.insert(END,"* Welcome Customer *")

def total():
    #Cosmetics Price
    soapprice= int(bathsoapEntry.get())*20
    facecreamprice= int(facecreamEntry.get())*50
    facewashprice= int(facewashEntry.get())*50
    hairsprayprice= int(hairsprayEntry.get())*50
    hairgelprice = int(hairgelEntry.get())*50
    bodylotionprice = int(bodylotionEntry.get())*50

    totalcosmeticprice=soapprice + facecreamprice + facewashprice + hairsprayprice + hairgelprice + bodylotionprice
    cosmeticpriceEntry.delete(0,END)
    cosmeticpriceEntry.insert(0,f"{totalcosmeticprice} TK.")
    cosmetictax=totalcosmeticprice*0.5
    cosmetictaxEntry.delete(0,END)
    cosmetictaxEntry.insert(0,f"{cosmetictax} TK.")


    #grocery price calculation
    riceprice = int(riceEntry.get())*50
    oilprice = int(oilEntry.get())*50
    daalprice = int(DaalEntry.get())*50
    sugerprice = int(sugerEntry.get())*50
    wheatprice = int(WheatEntry.get())*50
    teaprice = int(TeaEntry.get())*50

    totalgrocery = riceprice + oilprice + daalprice + sugerprice + wheatprice+ teaprice
    grocerypriceEntry.delete(0, END)
    grocerypriceEntry.insert(0, f"{totalgrocery} TK.")
    grocerytax = totalgrocery * 0.5
    grocerytaxEntry.delete(0, END)
    grocerytaxEntry.insert(0, f"{grocerytax} TK.")


    #Cold Drink Price Calculation
    cocacolaprice = int(cocacolaEntry.get())*50
    pepsiprice = int(pepsiEntry.get())*50
    funtaprice = int(funtaEntry.get())*50
    frutiprice = int(frutiEntry.get())*50
    sevenupprice = int(sevenupEntry.get())*50
    spriteprice = int(spriteEntry.get())*50

    totaldrinks = cocacolaprice + pepsiprice + funtaprice + frutiprice + sevenupprice + spriteprice
    drinkspriceEntry.delete(0, END)
    drinkspriceEntry.insert(0, f"{totaldrinks} TK.")
    drinkstax = totaldrinks * 0.5
    drinkstaxEntry.delete(0, END)
    drinkstaxEntry.insert(0, f"{drinkstax} TK.")


def bill_area():
    if(nameEntry.get()=="" or phoneEntry.get()==""):
        messagebox.showerror("Error", "Please enter Customer Details")
    elif(cosmeticpriceEntry.get()=="" and grocerypriceEntry.get()=="" and drinkspriceEntry.get()==""):
        messagebox.showerror("Error", "No Products are selected")
    elif(cosmeticpriceEntry.get() == "0 TK." and grocerypriceEntry.get() == "0 TK." and drinkspriceEntry.get() == "0 TK."):
        messagebox.showerror("Error", "No Products are selected")


#GUI Part
root=Tk()
root.title("Retail Billing System")
root.geometry("1270x685")
root.iconbitmap("icon.ico")
headingLabel=Label(root,text="Retail Billing System",font=("times new roman",30,"bold"),fg="yellow",bg="dark green",bd=10,relief=GROOVE)
headingLabel.pack(fill=X)

customer_details_frame=LabelFrame(root,text="Customer Details",font=("times new roman",15,"bold"),bg="red4",fg="yellow",bd=8,relief=GROOVE)
customer_details_frame.pack(fill=X)

nameLabel=Label(customer_details_frame,text="Name",font=("times new roman",15,"bold"),bg="red4",fg="white")

nameLabel.grid(row=0,column=0,padx=20)

nameEntry=Entry(customer_details_frame,font=("arial",15),bd=7,width=18)
nameEntry.grid(row=0,column=1,padx=8)

phoneLabel=Label(customer_details_frame,text="Phone Number",font=("times new roman",15,"bold"),bg="red4",fg="white")

phoneLabel.grid(row=0,column=2,padx=20,pady=2)

phoneEntry=Entry(customer_details_frame,font=("arial",15),bd=7,width=18)
phoneEntry.grid(row=0,column=3,padx=8)

billnumberLabel=Label(customer_details_frame,text="Bill Number",font=("times new roman",15,"bold"),bg="red4",fg="white")

billnumberLabel.grid(row=0,column=4,padx=20,pady=2)

phoneEntry=Entry(customer_details_frame,font=("arial",15),bd=7,width=18)
phoneEntry.grid(row=0,column=5,padx=8)

searchButton=Button(customer_details_frame,text="Search",font=("arial",12,"bold"),bd=7,width=10)
searchButton.grid(row=0,column=6,padx=20, pady=8)


productFrame=Frame(root)
productFrame.pack()

cosmeticsFrame=LabelFrame(productFrame,text="Cosmetics",font=("times new roman",15,"bold"),bg="red4",fg="yellow",bd=8,relief=GROOVE)
cosmeticsFrame.grid(row=0,column=0)

bathsoapLabel=Label(cosmeticsFrame,text="Bath Soap",font=("times new roman",15,"bold"),bg="red4",fg="white")
bathsoapLabel.grid(row=0,column=0,pady=9,padx=10,sticky="w")

bathsoapEntry=Entry(cosmeticsFrame,font=("times new roman",15,"bold"),width=10,bd=5)
bathsoapEntry.grid(row=0,column=1,pady=9,padx=1)
bathsoapEntry.insert(0,0)

facecreamLabel=Label(cosmeticsFrame,text="Face Cream",font=("times new roman",15,"bold"),bg="red4",fg="white")
facecreamLabel.grid(row=1,column=0,pady=9,padx=10,sticky="w")

facecreamEntry=Entry(cosmeticsFrame,font=("times new roman",15,"bold"),width=10,bd=5)
facecreamEntry.grid(row=1,column=1,pady=9,padx=10)
facecreamEntry.insert(0,0)

facewashLabel=Label(cosmeticsFrame,text="Face Cream",font=("times new roman",15,"bold"),bg="red4",fg="white")
facewashLabel.grid(row=2,column=0,pady=9,padx=10,sticky="w")

facewashEntry=Entry(cosmeticsFrame,font=("times new roman",15,"bold"),width=10,bd=5)
facewashEntry.grid(row=2,column=1,pady=9,padx=10)
facewashEntry.insert(0,0)

hairsprayLabel=Label(cosmeticsFrame,text="Hair Spray",font=("times new roman",15,"bold"),bg="red4",fg="white")
hairsprayLabel.grid(row=3,column=0,pady=9,padx=10,sticky="w")

hairsprayEntry=Entry(cosmeticsFrame,font=("times new roman",15,"bold"),width=10,bd=5)
hairsprayEntry.grid(row=3,column=1,pady=9,padx=10)
hairsprayEntry.insert(0,0)

hairgelLabel=Label(cosmeticsFrame,text="Hair Gel",font=("times new roman",15,"bold"),bg="red4",fg="white")
hairgelLabel.grid(row=4,column=0,pady=9,padx=10,sticky="w")

hairgelEntry=Entry(cosmeticsFrame,font=("times new roman",15,"bold"),width=10,bd=5)
hairgelEntry.grid(row=4,column=1,pady=9,padx=10)
hairgelEntry.insert(0,0)

bodylotionLabel=Label(cosmeticsFrame,text="Body Lotion",font=("times new roman",15,"bold"),bg="red4",fg="white")
bodylotionLabel.grid(row=5,column=0,pady=9,padx=10,sticky="w")

bodylotionEntry=Entry(cosmeticsFrame,font=("times new roman",15,"bold"),width=10,bd=5)
bodylotionEntry.grid(row=5,column=1,pady=9,padx=10)
bodylotionEntry.insert(0,0)



groceryFrame=LabelFrame(productFrame,text="Grocery",font=("times new roman",15,"bold"),bg="red4",fg="yellow",bd=8,relief=GROOVE)
groceryFrame.grid(row=0,column=1)


riceLabel=Label(groceryFrame,text="Rice",font=("times new roman",15,"bold"),bg="red4",fg="white")
riceLabel.grid(row=0,column=0,pady=9,padx=10,sticky="w")

riceEntry=Entry(groceryFrame,font=("times new roman",15,"bold"),width=10,bd=5)
riceEntry.grid(row=0,column=1,pady=9,padx=10)
riceEntry.insert(0,0)

oilLabel=Label(groceryFrame,text="Oil",font=("times new roman",15,"bold"),bg="red4",fg="white")
oilLabel.grid(row=1,column=0,pady=9,padx=10,sticky="w")

oilEntry=Entry(groceryFrame,font=("times new roman",15,"bold"),width=10,bd=5)
oilEntry.grid(row=1,column=1,pady=9,padx=10)
oilEntry.insert(0,0)

DaalLabel=Label(groceryFrame,text="Daal",font=("times new roman",15,"bold"),bg="red4",fg="white")
DaalLabel.grid(row=2,column=0,pady=9,padx=10,sticky="w")

DaalEntry=Entry(groceryFrame,font=("times new roman",15,"bold"),width=10,bd=5)
DaalEntry.grid(row=2,column=1,pady=9,padx=10)
DaalEntry.insert(0,0)

sugerLabel=Label(groceryFrame,text="Suger",font=("times new roman",15,"bold"),bg="red4",fg="white")
sugerLabel.grid(row=3,column=0,pady=9,padx=10,sticky="w")

sugerEntry=Entry(groceryFrame,font=("times new roman",15,"bold"),width=10,bd=5)
sugerEntry.grid(row=3,column=1,pady=9,padx=10)
sugerEntry.insert(0,0)

WheatLabel=Label(groceryFrame,text="Wheat",font=("times new roman",15,"bold"),bg="red4",fg="white")
WheatLabel.grid(row=4,column=0,pady=9,padx=10,sticky="w")

WheatEntry=Entry(groceryFrame,font=("times new roman",15,"bold"),width=10,bd=5)
WheatEntry.grid(row=4,column=1,pady=9,padx=10)
WheatEntry.insert(0,0)

TeaLabel=Label(groceryFrame,text="Tea",font=("times new roman",15,"bold"),bg="red4",fg="white")
TeaLabel.grid(row=5,column=0,pady=9,padx=10,sticky="w")

TeaEntry=Entry(groceryFrame,font=("times new roman",15,"bold"),width=10,bd=5)
TeaEntry.grid(row=5,column=1,pady=9,padx=10)
TeaEntry.insert(0,0)




drinksFrame=LabelFrame(productFrame,text="Soft Drinks",font=("times new roman",15,"bold"),bg="red4",fg="yellow",bd=8,relief=GROOVE)
drinksFrame.grid(row=0,column=2)

cocacolaLabel=Label(drinksFrame,text="CocaCola",font=("times new roman",15,"bold"),bg="red4",fg="white")
cocacolaLabel.grid(row=0,column=0,pady=9,padx=10,sticky="w")

cocacolaEntry=Entry(drinksFrame,font=("times new roman",15,"bold"),width=10,bd=5)
cocacolaEntry.grid(row=0,column=1,pady=9,padx=10)
cocacolaEntry.insert(0,0)

pepsiLabel=Label(drinksFrame,text="Pepsi",font=("times new roman",15,"bold"),bg="red4",fg="white")
pepsiLabel.grid(row=1,column=0,pady=9,padx=10,sticky="w")

pepsiEntry=Entry(drinksFrame,font=("times new roman",15,"bold"),width=10,bd=5)
pepsiEntry.grid(row=1,column=1,pady=9,padx=10)
pepsiEntry.insert(0,0)

funtaLabel=Label(drinksFrame,text="Funta",font=("times new roman",15,"bold"),bg="red4",fg="white")
funtaLabel.grid(row=2,column=0,pady=9,padx=10,sticky="w")

funtaEntry=Entry(drinksFrame,font=("times new roman",15,"bold"),width=10,bd=5)
funtaEntry.grid(row=2,column=1,pady=9,padx=10)
funtaEntry.insert(0,0)

frutiLabel=Label(drinksFrame,text="Fruti",font=("times new roman",15,"bold"),bg="red4",fg="white")
frutiLabel.grid(row=3,column=0,pady=9,padx=10,sticky="w")

frutiEntry=Entry(drinksFrame,font=("times new roman",15,"bold"),width=10,bd=5)
frutiEntry.grid(row=3,column=1,pady=9,padx=10)
frutiEntry.insert(0,0)

sevenupLabel=Label(drinksFrame,text="7up",font=("times new roman",15,"bold"),bg="red4",fg="white")
sevenupLabel.grid(row=4,column=0,pady=9,padx=10,sticky="w")

sevenupEntry=Entry(drinksFrame,font=("times new roman",15,"bold"),width=10,bd=5)
sevenupEntry.grid(row=4,column=1,pady=9,padx=10)
sevenupEntry.insert(0,0)

spriteLabel=Label(drinksFrame,text="Sprite",font=("times new roman",15,"bold"),bg="red4",fg="white")
spriteLabel.grid(row=5,column=0,pady=9,padx=10,sticky="w")

spriteEntry=Entry(drinksFrame,font=("times new roman",15,"bold"),width=10,bd=5)
spriteEntry.grid(row=5,column=1,pady=9,padx=10)
spriteEntry.insert(0,0)




billframe=Frame(productFrame,bd=8,relief=GROOVE)
billframe.grid(row=0,column=3)

billarealebel=Label(billframe,text="Bill Area",font=("times new roman",15,"bold"),bd=7,relief=GROOVE)
billarealebel.pack(fill=X)

scrollbar=Scrollbar(billframe,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)
textarea=Text(billframe,height=18,width=55,yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)


billmenuFrame=LabelFrame(root,text="Bill Menu",font=("times new roman",15,"bold"),bg="dark green",fg="yellow",bd=8,relief=GROOVE)
billmenuFrame.pack()

cosmeticpriceLabel=Label(billmenuFrame,text="Cosmetic Price",font=("times new roman",14,"bold"),bg="dark green",fg="white")
cosmeticpriceLabel.grid(row=0,column=0,pady=6,padx=10,sticky="w")

cosmeticpriceEntry=Entry(billmenuFrame,font=("times new roman",14,"bold"),width=10,bd=5)
cosmeticpriceEntry.grid(row=0,column=1,pady=6,padx=10)

grocerypriceLabel=Label(billmenuFrame,text="Grocery Price",font=("times new roman",14,"bold"),bg="dark green",fg="white")
grocerypriceLabel.grid(row=1,column=0,pady=6,padx=10,sticky="w")

grocerypriceEntry=Entry(billmenuFrame,font=("times new roman",14,"bold"),width=10,bd=5)
grocerypriceEntry.grid(row=1,column=1,pady=6,padx=10)

drinkspriceLabel=Label(billmenuFrame,text="Soft Drinks Price",font=("times new roman",14,"bold"),bg="dark green",fg="white")
drinkspriceLabel.grid(row=2,column=0,pady=6,padx=10,sticky="w")

drinkspriceEntry=Entry(billmenuFrame,font=("times new roman",14,"bold"),width=10,bd=5)
drinkspriceEntry.grid(row=2,column=1,pady=6,padx=10)


cosmetictaxLabel=Label(billmenuFrame,text="Cosmetic Tax",font=("times new roman",14,"bold"),bg="dark green",fg="white")
cosmetictaxLabel.grid(row=0,column=2,pady=6,padx=10,sticky="w")

cosmetictaxEntry=Entry(billmenuFrame,font=("times new roman",14,"bold"),width=10,bd=5)
cosmetictaxEntry.grid(row=0,column=3,pady=6,padx=10)

grocerytaxLabel=Label(billmenuFrame,text="Grocery Tax",font=("times new roman",14,"bold"),bg="dark green",fg="white")
grocerytaxLabel.grid(row=1,column=2,pady=6,padx=10,sticky="w")

grocerytaxEntry=Entry(billmenuFrame,font=("times new roman",14,"bold"),width=10,bd=5)
grocerytaxEntry.grid(row=1,column=3,pady=6,padx=10)

drinkstaxLabel=Label(billmenuFrame,text="Soft Drinks Tax",font=("times new roman",14,"bold"),bg="dark green",fg="white")
drinkstaxLabel.grid(row=2,column=2,pady=6,padx=10,sticky="w")

drinkstaxEntry=Entry(billmenuFrame,font=("times new roman",14,"bold"),width=10,bd=5)
drinkstaxEntry.grid(row=2,column=3,pady=6,padx=10)


buttonFrame=Frame(billmenuFrame,bd=8,relief=GROOVE)
buttonFrame.grid(row=0,column=4,rowspan=3)

totalButton=Button(buttonFrame,text="Total",font=("arial",16,"bold"),bg="dark green",fg="white",bd=5,width=8,pady=10,command=total)
totalButton.grid(row=0,column=0,pady=20,padx=5)

billButton=Button(buttonFrame,text="Bill",font=("arial",16,"bold"),bg="dark green",fg="white",bd=5,width=8,pady=10,command=bill_area)
billButton.grid(row=0,column=1,pady=20,padx=5)

emailButton=Button(buttonFrame,text="Email",font=("arial",16,"bold"),bg="dark green",fg="white",bd=5,width=8,pady=10)
emailButton.grid(row=0,column=2,pady=20,padx=5)

printButton=Button(buttonFrame,text="Print",font=("arial",16,"bold"),bg="dark green",fg="white",bd=5,width=8,pady=10)
printButton.grid(row=0,column=3,pady=20,padx=5)

clearButton=Button(buttonFrame,text="Clear",font=("arial",16,"bold"),bg="dark green",fg="white",bd=5,width=8,pady=10)
clearButton.grid(row=0,column=4,pady=20,padx=5)


root.mainloop()
