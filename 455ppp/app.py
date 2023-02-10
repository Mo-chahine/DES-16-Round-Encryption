from tkinter import *
from customtkinter import *
from GUI import *
from tkinter.scrolledtext import ScrolledText
from tkinter.font import *


# GUI
root = Tk()
img = PhotoImage(file='g/dep.png')
limg= Label(root, image=img)
limg.place(x=0,y=0)
root.geometry("600x400")
root.title("DES Encryption by Bassel Isber, Khaled Hatoum & Mohammad Chahine")
root.iconphoto(False, PhotoImage(file='g/icon.png'))



key=StringVar()
plaintext=StringVar()

def submit():
 hel.clear()
 her.clear()
 zed.clear()
 mk=key.get()
 pt=plaintext.get()
 DESencrypt(pt,mk)
 cipherText.config(state='normal')
 cipherText.delete(1.0,END)
 cipherText1.config(state='normal')
 cipherText1.delete(1.0,END)                      
 for i in range(16):
  cipherText.insert(END, "Round ")
  cipherText.insert(END, i+1)
  cipherText.insert(END, " : ")
  cipherText.insert(END, eachROUND(i))
  cipherText.insert(END,"\n")
  cipherText1.insert(END, "Round ")
  cipherText1.insert(END, i+1)
  cipherText1.insert(END," : ")
  cipherText1.insert(END, Kis(i))
  cipherText1.insert(END,"\n")
 cipherText.insert(END, "Encrypted text is: ", DESencrypt(pt,mk))
 cipherText.insert(END, DESencrypt(pt,mk))
 cipherText.config(state="disabled")
 cipherText1.config(state='disabled')
 name_entry.delete(0,END)
 name_entry1.delete(0,END)


Desired_font =Font( family = "Helvetica", size = 10, weight = "bold")
Desired_font1 =Font( family = "Comic Sans MS", size = 15, weight = "bold")

##Result Cipher Text area
#Label3 = Label(root, fg="lightblue", text="The Cipher Text:", font=Desired_font1, bg='black').place(x=100, y=160)
cipherText = ScrolledText(root, height=5, width=35,bg="lightblue")
cipherText.grid(row=1, column=1)
cipherText.place(x=40, y=205)
cipherText.configure( font = Desired_font )
cipherText.insert(END,"Cipher Text Will Appear here!")
cipherText.tag_configure("centered", justify="center")
cipherText.config(state='disabled')
cipherText1 = ScrolledText(root, height=5, width=60,bg="lightblue")
cipherText1.grid(row=1, column=1)
cipherText1.place(x=40, y=300)
cipherText1.configure( font = Desired_font )
cipherText1.insert(END,"Key Expansion of Each Round Will Appear here!")
cipherText1.tag_configure("centered", justify="center")
cipherText1.config(state='disabled')






##Key Input Area
Key = Label(root,font=Desired_font,fg="lightblue", bg="black",text = "Key:").place(x = 40,y = 60)
entry_name=PhotoImage(file='g/Rectangle 1.png')
entry_image=Label(root,image=entry_name,border=0,bg='black')
entry_image.place(x=110,y=60)
name_entry=Entry(root,width=27,border=0,font=Desired_font,textvariable=key)
name_entry.place(x=117,y=64)




#key_entry = Entry(root,bg="lightblue", textvariable=key, width = 30).place(x = 110,y = 60) 

#plaintext_entry_area = Entry(root,image=entry_name,border=0, textvariable=plaintext, width = 27).place(x = 110,y = 100)

##Plain Text Input Area
Plaintext = Label(root,font=Desired_font,fg="lightblue",bg="black",text = "Plaintext:").place(x = 40,y = 100)
entry_image1=Label(root,image=entry_name,border=0,bg='black')
entry_image1.place(x=110,y=100)
name_entry1=Entry(root,width=27,border=0,font=Desired_font,textvariable=plaintext)
name_entry1.place(x=117,y=104)

#submit_button = Button(root,font="Calibiri",text = "Submit", bg="lightblue",command=submit).place(x = 300,y = 130)
submit_button = CTkButton(master=root,text="ENCRYPT",font=('Calibri',20), height=50,width=150,border_width=2,corner_radius=8,border_color="black",bg_color="black",hover=True,hover_color="lightblue",command=submit).place(x=350,y=140)



root.mainloop()
