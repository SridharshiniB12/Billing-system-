from tkinter import *
from tkinter import messagebox
import random,os,tempfile,smtplib

def clear():
    CokeEntry.insert(0,0)
    MilkshakesEntry.insert(0,0)
    PepsiEntry.insert(0,0)
    FrootiEntry.insert(0,0)
    MirandaEntry.insert(0,0)
    LassiEntry.insert(0,0)

    riceEntry.insert(0,0)
    wheatEntry.insert(0,0)
    SugarEntry.insert(0,0)
    SaltEntry.insert(0,0)
    MasalaEntry.insert(0,0)
    OilEntry.insert(0,0)

    FacecreamEntry.insert(0,0)
    FacemaskEntry.insert(0,0)
    tonerprice.insert(0,0)
    MoisturiserEntry.insert(0,0)
    PerfumeEntry.insert(0,0)
    BodylotionEntry.insert(0,0)

    beautyaidstaxEntry.delete(0,END)
    grocerytaxEntry.delete(0,END)
    cooldrinkstaxEntry.delete(0,END)

    beautyaidspriceEntry.delete(0,END)
    grocerypriceEntry.delete(0,END)
    cooldrinkspriceEntry.delete(0,END)

    textarea.delete(1.0,END)

def send_email():
    def send_gmail():
        try:
            ob=smtplib.SMTP('smtp.gmail.com',587)
            ob.starttls()
            ob.login(senderEntry.get(),passwordEntry.get())

            message=email_textarea.get(1.0,END)
            receiver_address=receiverEntry.get()
            ob.sendmail(senderEntry.get(),receiverEntry.get(),message)
            ob.quit()
            messagebox.showinfo('Success','Bill is successfully sent',parent=root1)
            root1.destroy()
        except:
            messagebox.showerror('Error','Something went wrong,Please try again',parent=root1)
        
    if textarea.get(1.0,END)=='\n':
        messagebox.showerror('Error','Bill is empty')
    else:
        root1=Toplevel()
        root1.grab_set()
        root1.title('send Gmail')
        root1.config(bg='gray20')
        root1.resizable(0,0)

        senderFrame = LabelFrame(root1,text='Sender',font=('arial',16,'bold'),bd=6,bg='gray20',fg='white')
        senderFrame.grid(row=0,column=0,padx=40,pady=20)

        gmailLabel=Label(senderFrame,text="Sender's Email",font=('arial',14,'bold'),bg='gray20',fg='white')
        gmailLabel.grid(row=0,column=0,padx=10,pady=8)

        senderEntry=Entry(senderFrame,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE)
        senderEntry.grid(row=0,column=1,padx=10,pady=8)

        passwordLabel=Label(senderFrame,text='Password',font=('arial',14,'bold'),bg='gray20',fg='white')
        passwordLabel.grid(row=1,column=0,padx=10,pady=8)

        passwordEntry=Entry(senderFrame,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE,show='*')
        passwordEntry.grid(row=1,column=1,padx=10,pady=8)

        recipientFrame = LabelFrame(root1,text='Recipient',font=('arial',16,'bold'),bd=6,bg='gray20',fg='white')
        recipientFrame.grid(row=1,column=0,padx=40,pady=20)

        receiverLabel=Label(recipientFrame,text='Email address',font=('arial',14,'bold'),bg='gray20',fg='white')
        receiverLabel.grid(row=0,column=0,padx=10,pady=8)

        receiverEntry=Entry(recipientFrame,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE)
        receiverEntry.grid(row=0,column=1,padx=10,pady=8)

        messageLabel=Label(recipientFrame,text='Message',font=('arial',14,'bold'),bg='gray20',fg='white')
        messageLabel.grid(row=1,column=0,padx=10,pady=8)

        email_textarea=Text(recipientFrame,font=('arial',14,'bold'),bd=2,relief=SUNKEN,width=42,height=11)
        email_textarea.grid(row=2,column=0,columnspan=2)
        email_textarea.delete(1.0,END)
        email_textarea.insert(END,textarea.get(1.0,END).replace('=','').replace('-','').replace('\t\t\t','\t\t'))


        sendButton=Button(root1,text='Send',font=('arial',14,'bold'),width=15,command=send_gmail)
        sendButton.grid(row=2,column=0,pady=20)

      
      

def print_bill():
    if textarea.get(1.0,END)=='\n':
        messagebox.showerror('Error','Bill is empty')
    else:
        file=tempfile.mktemp('.txt')
        open(file,'w').write(textarea.get(1.0,END))
        os.startfile(file,'print')



def search_bill():
    for i in os.listdir('bills/'):
        if i.split('.')[0] == billnumberEntry.get():
            f=open('bills/{i}','r')
            textarea.delete(1.0,END)
            for data in f:
                textarea.insergt(END,data)
            f.close()
            break
    else:
        messagebox.showerroe('Error','Invalid Bill Number')

             

#if not os.path.exist('bills'):
    #os.mkdir('bills')


def save_bill():
    global billnumber
    result=messagebox.askyesno('Confirm','Do you want to save the bill?')
    if result:
        bill_content=textarea.get(1.0,END)
        file=open(f'bills/{billnumber}.txt','w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo('Success',f'bill number{billnumber} is saved successfully')
        billnumber=random.randint(500,1000)


billnumber=random.randint(500,1000)
#funtionality part

def bill_area():
    if nameEntry.get()=='' or phoneEntry.get()=='':
        messagebox.showerror('Error','Customer Details are required')
    elif beautyaidspriceEntry.get()==''and grocerypriceEntry.get=='' and cooldrinkspriceEntry.get()=='':
       messagebox.showerror('Error','No products are selected')
    elif beautyaidspriceEntry.get()=='0 Rs'and grocerypriceEntry.get=='0 Rs' and cooldrinkspriceEntry.get()=='0 Rs':
        messagebox.showerror('Error','No products are selected')  
    else:  
        textarea.delete(1.0,END)


        textarea.insert(END,'\t\t**WELCOME CUSTOMER**\n')  
        textarea.insert(END,f'\nBill Number:{billnumber}\n')
        textarea.insert(END,f'\nCustomer Name:{nameEntry.get()}\n')
        textarea.insert(END,f'\nCustomer PhoneNumber:{phoneEntry.get()}\n')
        textarea.insert(END,f'================================================')
        textarea.insert(END,'Products\t\tQuantity\t\t\tPrice\n')
        textarea.insert(END,f'================================================')
        if FacecreamEntry.get()!='0':
            textarea.insert(END,f'\nface cream \t\t\t{FacecreamEntry.get()}\t\t{creamprice} Rs')
        if FacemaskEntry.get()!='0':
            textarea.insert(END,f'\nFace mask \t\t\t{FacemaskEntry.get()}\t\t{maskprice} Rs')
        if TonerEntry.get()!='0':
            textarea.insert(END,f'\nToner \t\t\t{TonerEntry.get()}\t\t{tonerprice} Rs')
        if MoisturiserEntry.get()!='0':
            textarea.insert(END,f'\nMoisturiser \t\t\t{MoisturiserEntry.get()}\t\t{moisturiserprice} Rs')
        if PerfumeEntry.get()!='0':
            textarea.insert(END,f'\nPerfume \t\t\t{PerfumeEntry.get()}\t\t{perfumeprice} Rs')
        if riceEntry.get()!='0':
            textarea.insert(END,f'\nRice \t\t\t{riceEntry.get()}\t\t{riceprice} Rs')
        if wheatEntry.get()!='0':
            textarea.insert(END,f'\nWheat \t\t\t{wheatEntry.get()}\t\t{wheatprice} Rs')
        if SugarEntry.get()!='0':
            textarea.insert(END,f'\nSugar\t\t\t{SugarEntry.get()}\t\t{sugarprice} Rs')
        if SaltEntry.get()!='0':
            textarea.insert(END,f'\nSalt\t\t\t{SaltEntry.get()}\t\t{saltprice} Rs')
        if MasalaEntry.get()!='0':
            textarea.insert(END,f'\nMasala \t\t\t{MasalaEntry.get()}\t\t{masalaprice} Rs')
        if OilEntry.get()!='0':
            textarea.insert(END,f'\nOil \t\t\t{OilEntry.get()}\t\t{oilprice} Rs')
        if CokeEntry.get()!='0':
            textarea.insert(END,f'\nCoke \t\t\t{CokeEntry.get()}\t\t{cokeprice}Rs')
        if MirandaEntry.get()!='0':
            textarea.insert(END,f'\nMiranda \t\t\t{MirandaEntry.get()}\t\t{mirandaprice} Rs')
        if FrootiEntry.get()!='0':
            textarea.insert(END,f'\nFrooti \t\t\t{FrootiEntry.get()}\t\t{frootiprice} Rs')
        if PepsiEntry.get()!='0':
            textarea.insert(END,f'\nPepsi \t\t\t{PepsiEntry.get()}\t\t{pepsiprice} Rs')
        if MilkshakesEntry.get()!='0':
            textarea.insert(END,f'\nMilkshakes \t\t\t{MilkshakesEntry.get()}\t\t{milkshakesprice} Rs')
        if LassiEntry.get()!='0':
            textarea.insert(END,f'\nLassi \t\t\t{LassiEntry.get()}\t\t{lassiprice} Rs')

        textarea.insert(END,f'\n------------------------------------------------')
        
        if beautyaidstaxEntry.get()!='0.0 Rs':
            textarea.insert(END,f'\n Beauty Aids tax\t\t{beautyaidstaxEntry.get()}')
        if grocerytaxEntry.get()!='0.0 Rs':
            textarea.insert(END,f'\n Groceries tax\t\t{grocerytaxEntry.get()}')
        if cooldrinkstaxEntry.get()!='0.0 Rs':
            textarea.insert(END,f'\n Cooldrinks tax\t\t{cooldrinkstaxEntry.get()}')

        textarea.insert(END,f'\n Total Bill \t\t{totalbill}')  
        textarea.insert(END,f'\n------------------------------------------------') 
        save_bill()


def  total():
    global creamprice,maskprice,tonerprice,moisturiserprice,bodylotionprice,perfumeprice
    global riceprice,wheatprice,sugarprice,saltprice,masalaprice,oilprice
    global cokeprice,milkshakesprice,pepsiprice,frootiprice,mirandaprice,lassiprice
    global totalbill
    
    creamprice=int(FacecreamEntry.get())*50
    maskprice=int(FacemaskEntry.get())*50
    tonerprice=int(TonerEntry.get())*40
    moisturiserprice=int(MoisturiserEntry.get())*100
    perfumeprice=int(PerfumeEntry.get())*150
    bodylotionprice=int(BodylotionEntry.get())*150

    totalbeautyaidsprice=creamprice+maskprice+tonerprice+moisturiserprice+bodylotionprice+perfumeprice
    beautyaidspriceEntry.delete(0,END)
    beautyaidspriceEntry.insert(0,str(totalbeautyaidsprice) +'Rs')
    beautyaidstax=totalbeautyaidsprice*0.18
    beautyaidstaxEntry.delete(0,END)
    beautyaidstaxEntry.insert(0,str(beautyaidstax)+'Rs')


     
    riceprice=int(riceEntry.get())*70
    wheatprice=int(wheatEntry.get())*60
    sugarprice=int(SugarEntry.get())*40
    saltprice=int(SaltEntry.get())*10
    masalaprice=int(MasalaEntry.get())*15
    oilprice=int(OilEntry.get())*180

    totalgroceryprice=riceprice+wheatprice+sugarprice+saltprice+masalaprice+oilprice
    grocerypriceEntry.delete(0,END)
    grocerypriceEntry.insert(0,str(totalgroceryprice)+'Rs')
    grocerytax=totalgroceryprice*0.18
    grocerytaxEntry.delete(0,END)
    grocerytaxEntry.insert(0,str(grocerytax)+'Rs')

    cokeprice=int(CokeEntry.get())*40
    milkshakesprice=int(MilkshakesEntry.get())*60
    pepsiprice=int(PepsiEntry.get())*40
    frootiprice=int(FrootiEntry.get())*10
    mirandaprice=int(MirandaEntry.get())*30
    lassiprice=int(LassiEntry.get())*20

    totalcooldrinksprice=cokeprice+milkshakesprice+pepsiprice+mirandaprice+lassiprice+frootiprice
    cooldrinkspriceEntry.delete(0,END)
    cooldrinkspriceEntry.insert(0,str(totalcooldrinksprice)+'Rs')
    cooldrinkstax=totalcooldrinksprice*0.18
    cooldrinkstaxEntry.delete(0,END)
    cooldrinkstaxEntry.insert(0,str(cooldrinkstax)+'Rs')

    totalbill= totalbeautyaidsprice+totalgroceryprice+totalcooldrinksprice+beautyaidstax+grocerytax+cooldrinkstax

root=Tk()
root.title('Billing System')
root.geometry('1270x685')
root.iconbitmap('bill.ICO.ico')
headingLabel=Label(root,text='Billing System',font=('Algerian',32,'italic'),bg='DeepSkyBlue4',fg='grey1',bd=12,relief=RIDGE)
headingLabel.pack(fill=X)

customer_details_frame=LabelFrame(root,text='Customer Details',font=('times new roman',13,'bold','italic'),bg= 'DeepSkyBlue3',fg='grey1',bd=8,relief=RIDGE)
customer_details_frame.pack(fill=X)

nameLabel=Label(customer_details_frame,text='NAME',font=('times new roman',13,'bold','italic'),bg= 'DeepSkyBlue3',fg='white')
nameLabel.grid(row=0,column=0,padx=20,pady=2)


nameEntry=Entry(customer_details_frame,font=('arial',15),bd=6,width=18)
nameEntry.grid(row=0,column=1,padx=8)

phoneLabel=Label(customer_details_frame,text='PHONE No',font=('times new roman',13,'bold','italic'),bg= 'DeepSkyBlue3',fg='white')
phoneLabel.grid(row=0,column=2,padx=20,pady=2)

phoneEntry=Entry(customer_details_frame,font=('arial',15),bd=6,width=18)
phoneEntry.grid(row=0,column=3,padx=8)

billnumberLabel=Label(customer_details_frame,text='Bill number',font=('times new roman',13,'bold','italic'),bg= 'DeepSkyBlue3',fg='white')
billnumberLabel.grid(row=0,column=4,padx=20,pady=2)

billnumberEntry=Entry(customer_details_frame,font=('arial',15),bd=6,width=18)
billnumberEntry.grid(row=0,column=5,padx=8)

searchButton=Button(customer_details_frame,text='SEARCH',
                    font=('arial',13,'bold'),bd=7,width=10,command = search_bill)
searchButton.grid(row=0,column=6,padx=20,pady=8)

productsFrame=Frame(root)
productsFrame.pack(fill=X)

Beauty_aidsFrame=LabelFrame(productsFrame,text='Beauty Aids',font=('times new roman',13,'bold','italic'),bg= 'DeepSkyBlue3',fg='grey1',bd=8,relief=RIDGE)
Beauty_aidsFrame.grid(row=0,column=0)

FacecreamLabel=Label(Beauty_aidsFrame,text='Face Cream',font=('times new roman',13,'bold','italic'),bg= 'DeepSkyBlue3',fg='white')
FacecreamLabel.grid(row=0,column=0,pady=8,padx=10,sticky='w')
FacecreamEntry=Entry(Beauty_aidsFrame,font=('arial',15),bd=5,width=10)
FacecreamEntry.grid(row=0,column=1,pady=8,padx=20)
FacecreamEntry.insert(0,0)

FacemaskLabel=Label(Beauty_aidsFrame,text='Face mask',font=('times new roman',13,'bold','italic'),bg= 'DeepSkyBlue3',fg='white')
FacemaskLabel.grid(row=1,column=0,pady=8,padx=10,sticky='w')
FacemaskEntry=Entry(Beauty_aidsFrame,font=('arial',15),bd=5,width=10)
FacemaskEntry.grid(row=1,column=1,pady=8,padx=20)
FacemaskEntry.insert(0,0)

TonerLabel=Label(Beauty_aidsFrame,text='Toner',font=('times new roman',13,'bold','italic'),bg= 'DeepSkyBlue3',fg='white')
TonerLabel.grid(row=2,column=0,pady=8,padx=10,sticky='w')
TonerEntry=Entry(Beauty_aidsFrame,font=('arial',15),bd=5,width=10)
TonerEntry.grid(row=2,column=1,pady=8,padx=20)
TonerEntry.insert(0,0)

MoisturiserLabel=Label(Beauty_aidsFrame,text='Moisturiser',font=('times new roman',13,'bold','italic'),bg= 'DeepSkyBlue3',fg='white')
MoisturiserLabel.grid(row=3,column=0,pady=8,padx=10,sticky='w')
MoisturiserEntry=Entry(Beauty_aidsFrame,font=('arial',15),bd=5,width=10)
MoisturiserEntry.grid(row=3,column=1,pady=8,padx=20)
MoisturiserEntry.insert(0,0)

PerfumeLabel=Label(Beauty_aidsFrame,text='Perfume',font=('times new roman',13,'bold','italic'),bg= 'DeepSkyBlue3',fg='white')
PerfumeLabel.grid(row=4,column=0,pady=8,padx=10,sticky='w')
PerfumeEntry=Entry(Beauty_aidsFrame,font=('arial',15),bd=5,width=10)
PerfumeEntry.grid(row=4,column=1,pady=8,padx=20)
PerfumeEntry.insert(0,0)

BodylotionLabel=Label(Beauty_aidsFrame,text='Body lotion',font=('times new roman',13,'bold','italic'),bg= 'DeepSkyBlue3',fg='white')
BodylotionLabel.grid(row=5,column=0,pady=8,padx=10,sticky='w')
BodylotionEntry=Entry(Beauty_aidsFrame,font=('arial',15),bd=5,width=10)
BodylotionEntry.grid(row=5,column=1,pady=8,padx=20)
BodylotionEntry.insert(0,0)


GroceryFrame=LabelFrame(productsFrame,text='Grocery',font=('times new roman',13,'bold','italic'),bg= 'DeepSkyBlue3',fg='grey1',bd=8,relief=RIDGE)
GroceryFrame.grid(row=0,column=1)

riceLabel=Label(GroceryFrame,text='Rice',font=('times new roman',13,'bold','italic'),bg= 'DeepSkyBlue3',fg='white')
riceLabel.grid(row=0,column=1,pady=8,padx=10,sticky='w')
riceEntry=Entry(GroceryFrame,font=('arial',15),bd=5,width=10)
riceEntry.grid(row=0,column=2,pady=8,padx=20)
riceEntry.insert(0,0)

wheatLabel=Label(GroceryFrame,text='Wheat',font=('times new roman',13,'bold','italic'),bg= 'DeepSkyBlue3',fg='white')
wheatLabel.grid(row=1,column=1,pady=8,padx=10,sticky='w')
wheatEntry=Entry(GroceryFrame,font=('arial',15),bd=5,width=10)
wheatEntry.grid(row=1,column=2,pady=8,padx=20)
wheatEntry.insert(0,0)

SugarLabel=Label(GroceryFrame,text='Sugar',font=('times new roman',13,'bold','italic'),bg= 'DeepSkyBlue3',fg='white')
SugarLabel.grid(row=2,column=1,pady=8,padx=10,sticky='w')
SugarEntry=Entry(GroceryFrame,font=('arial',15),bd=5,width=10)
SugarEntry.grid(row=2,column=2,pady=8,padx=20)
SugarEntry.insert(0,0)

SaltLabel=Label(GroceryFrame,text='Salt',font=('times new roman',13,'bold','italic'),bg= 'DeepSkyBlue3',fg='white')
SaltLabel.grid(row=3,column=1,pady=8,padx=10,sticky='w')
SaltEntry=Entry(GroceryFrame,font=('arial',15),bd=5,width=10)
SaltEntry.grid(row=3,column=2,pady=8,padx=20)
SaltEntry.insert(0,0)

MasalaLabel=Label(GroceryFrame,text='Masala',font=('times new roman',13,'bold','italic'),bg= 'DeepSkyBlue3',fg='white')
MasalaLabel.grid(row=4,column=1,pady=8,padx=10,sticky='w')
MasalaEntry=Entry(GroceryFrame,font=('arial',15),bd=5,width=10)
MasalaEntry.grid(row=4,column=2,pady=8,padx=20)
MasalaEntry.insert(0,0)

OilLabel=Label(GroceryFrame,text='Oil',font=('times new roman',13,'bold','italic'),bg= 'DeepSkyBlue3',fg='white')
OilLabel.grid(row=5,column=1,pady=8,padx=10,sticky='w')
OilEntry=Entry(GroceryFrame,font=('arial',15),bd=5,width=10)
OilEntry.grid(row=5,column=2,pady=8,padx=20)
OilEntry.insert(0,0)


CooldrinksFrame=LabelFrame(productsFrame,text='Cool drinks',font=('times new roman',13,'bold','italic'),bg= 'DeepSkyBlue3',fg='grey1',bd=8,relief=RIDGE)
CooldrinksFrame.grid(row=0,column=2)

CokeLabel=Label(CooldrinksFrame,text='Coke',font=('times new roman',13,'bold','italic'),bg= 'DeepSkyBlue3',fg='white')
CokeLabel.grid(row=0,column=2,pady=8,padx=10,sticky='w')
CokeEntry=Entry(CooldrinksFrame,font=('arial',15),bd=5,width=10)
CokeEntry.grid(row=0,column=3,pady=8,padx=15)
CokeEntry.insert(0,0)

MilkshakesLabel=Label(CooldrinksFrame,text='Milkshakes',font=('times new roman',13,'bold','italic'),bg= 'DeepSkyBlue3',fg='white')
MilkshakesLabel.grid(row=1,column=2,pady=8,padx=10,sticky='w')
MilkshakesEntry=Entry(CooldrinksFrame,font=('arial',15),bd=5,width=10)
MilkshakesEntry.grid(row=1,column=3,pady=8,padx=15)
MilkshakesEntry.insert(0,0)

PepsiLabel=Label(CooldrinksFrame,text='Pepsi',font=('times new roman',13,'bold','italic'),bg= 'DeepSkyBlue3',fg='white')
PepsiLabel.grid(row=2,column=2,pady=8,padx=10,sticky='w')
PepsiEntry=Entry(CooldrinksFrame,font=('arial',15),bd=5,width=10)
PepsiEntry.grid(row=2,column=3,pady=8,padx=15)
PepsiEntry.insert(0,0)

FrootiLabel=Label(CooldrinksFrame,text='Frooti',font=('times new roman',13,'bold','italic'),bg= 'DeepSkyBlue3',fg='white')
FrootiLabel.grid(row=3,column=2,pady=8,padx=10,sticky='w')
FrootiEntry=Entry(CooldrinksFrame,font=('arial',15),bd=5,width=10)
FrootiEntry.grid(row=3,column=3,pady=8,padx=15)
FrootiEntry.insert(0,0)

MirandaLabel=Label(CooldrinksFrame,text='Miranda',font=('times new roman',13,'bold','italic'),bg= 'DeepSkyBlue3',fg='white')
MirandaLabel.grid(row=4,column=2,pady=8,padx=10,sticky='w')
MirandaEntry=Entry(CooldrinksFrame,font=('arial',15),bd=5,width=10)
MirandaEntry.grid(row=4,column=3,pady=8,padx=15)
MirandaEntry.insert(0,0)

LassiLabel=Label(CooldrinksFrame,text='Lassi',font=('times new roman',13,'bold','italic'),bg= 'DeepSkyBlue3',fg='white')
LassiLabel.grid(row=5,column=2,pady=8,padx=10,sticky='w')
LassiEntry=Entry(CooldrinksFrame,font=('arial',15),bd=5,width=10)
LassiEntry.grid(row=5,column=3,pady=8,padx=15)
LassiEntry.insert(0,0)


billFrame=Frame(productsFrame,bd=8,relief=RIDGE,padx=100)
billFrame.grid(row=0,column=3,padx=10)

billareaLabel=Label(billFrame,text='Label Area',font=('arial',15,'bold'),bd=6,relief=RIDGE)
billareaLabel.pack(fill=X)

scrollbar=Scrollbar(billFrame,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)
textarea=Text(billFrame,height=18,width=48,yscrollcommand= scrollbar.set)
textarea.pack()

scrollbar.config(command=textarea.yview)
billmenuFrame=LabelFrame(root,text='Bill menu',font=('times new roman',13,'bold','italic'),bg= 'DeepSkyBlue3',fg='gray1',bd=8,relief=RIDGE)
billmenuFrame.pack()

beautyaidspriceLabel=Label(billmenuFrame,text='Beauty Aids Price',font=('times new roman',13,'bold','italic'),bg= 'DeepSkyBlue3',fg='white')
beautyaidspriceLabel.grid(row=0,column=0,pady=8,padx=10,sticky='w')
beautyaidspriceEntry=Entry(billmenuFrame,font=('arial',15),bd=5,width=10)
beautyaidspriceEntry.grid(row=0,column=1,pady=8,padx=10)

grocerypriceLabel=Label(billmenuFrame,text='Groceries Price',font=('times new roman',13,'bold','italic'),bg= 'DeepSkyBlue3',fg='white')
grocerypriceLabel.grid(row=1,column=0,pady=8,padx=10,sticky='w')
grocerypriceEntry=Entry(billmenuFrame,font=('arial',15),bd=5,width=10)
grocerypriceEntry.grid(row=1,column=1,pady=8,padx=10) 

cooldrinkspriceLabel=Label(billmenuFrame,text='Cool drinks Price',font=('times new roman',13,'bold','italic'),bg= 'DeepSkyBlue3',fg='white')
cooldrinkspriceLabel.grid(row=2,column=0,pady=8,padx=10,sticky='w')
cooldrinkspriceEntry=Entry(billmenuFrame,font=('arial',15),bd=5,width=10)
cooldrinkspriceEntry.grid(row=2,column=1,pady=8,padx=10)

beautyaidstaxLabel=Label(billmenuFrame,text='Beauty Aids tax',font=('times new roman',13,'bold','italic'),bg= 'DeepSkyBlue3',fg='white')
beautyaidstaxLabel.grid(row=0,column=2,pady=8,padx=10,sticky='w')
beautyaidstaxEntry=Entry(billmenuFrame,font=('arial',15),bd=5,width=10)
beautyaidstaxEntry.grid(row=0,column=3,pady=8,padx=10)

grocerytaxLabel=Label(billmenuFrame,text='Groceries tax',font=('times new roman',13,'bold','italic'),bg= 'DeepSkyBlue3',fg='white')
grocerytaxLabel.grid(row=1,column=2,pady=8,padx=10,sticky='w')
grocerytaxEntry=Entry(billmenuFrame,font=('arial',15),bd=5,width=10)
grocerytaxEntry.grid(row=1,column=3,pady=8,padx=10) 

cooldrinkstaxLabel=Label(billmenuFrame,text='Cool drinks tax',font=('times new roman',13,'bold','italic'),bg= 'DeepSkyBlue3',fg='white')
cooldrinkstaxLabel.grid(row=2,column=2,pady=8,padx=10,sticky='w')
cooldrinkstaxEntry=Entry(billmenuFrame,font=('arial',15),bd=5,width=10)
cooldrinkstaxEntry.grid(row=2,column=3,pady=8,padx=10)

buttonFrame=Frame(billmenuFrame,bd=8,relief=RIDGE,padx=140,pady=80)
buttonFrame.grid(row=0,column=4,rowspan=3)


totalButton=Button(buttonFrame,text='Total',font=('arial',16,'bold'),bg='gray1',fg='white',bd=5,width=8,command=total)
totalButton.grid(row=0,column=0,pady=20,padx=5)

billButton=Button(buttonFrame,text='Bill',font=('arial',16,'bold'),bg='gray1',fg='white',bd=5,width=8,command=bill_area)
billButton.grid(row=0,column=1,pady=20,padx=5)

emailButton=Button(buttonFrame,text='Email',font=('arial',16,'bold'),bg='gray1',fg='white',bd=5,width=8,command=send_email)
emailButton.grid(row=0,column=2,pady=20,padx=5)

printButton=Button(buttonFrame,text='Print',font=('arial',16,'bold'),bg='gray1',fg='white',bd=5,width=8,command =print_bill)
printButton.grid(row=0,column=3,pady=20,padx=5)

clearButton=Button(buttonFrame,text='Clear',font=('arial',16,'bold'),bg='gray1',fg='white',bd=5,width=8,command=clear)
clearButton.grid(row=0,column=4,pady=20,padx=5)

root.mainloop()