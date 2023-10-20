from tkinter import *
from PIL import ImageTk,Image
root = Tk()
root.title("Image Viewer")

#must have mentioned images in the same directory in your local system.
root.iconbitmap("C:/Wallpaper/VScode.ico")
myimg1 = ImageTk.PhotoImage(Image.open("C:/Wallpaper/srk1.jpeg"))
myimg2 = ImageTk.PhotoImage(Image.open("C:/Wallpaper/srk2.jpeg"))
myimg3 = ImageTk.PhotoImage(Image.open("C:/Wallpaper/srk3.jpeg"))
myimg4 = ImageTk.PhotoImage(Image.open("C:/Wallpaper/srk4.jpeg"))
myimg5 = ImageTk.PhotoImage(Image.open("C:/Wallpaper/srk5.jpeg"))
imagelist = [myimg1,myimg2,myimg3,myimg4,myimg5]
numofimages = len(imagelist)
mylabel = Label(image=myimg1)
mylabel.grid(row=0,column=0,columnspan=3)
def forward(imagenumber):
    global mylabel
    global forwardbutton 
    global backwardbutton
    
    if imagenumber >= (numofimages+1):
        forwardbutton = Button(root,text='Next',state=DISABLED,width=10,command=lambda:forward(imagenumber+1))
        
    else:
        mylabel.grid_forget()
        mylabel = Label(image=imagelist[imagenumber-1])
        mylabel.grid(row=0,column=0,columnspan=3)
        forwardbutton = Button(root,text='Next',width=10,command=lambda:forward(imagenumber+1))
        forwardbutton.grid(row=1,column=2)
        backwardbutton = Button(root,text='Previous',width=10,command=lambda:backward(imagenumber-1))
        backwardbutton.grid(row=1,column=0)
        status = Label(root,text=f'Image {imagenumber} of {numofimages}',bd=0,border=0,relief=SUNKEN,pady=10)
        status.grid(row=2,column=1)

def backward(imagenumber):
    global mylabel
    global forwardbutton
    global backwardbuttons
    if imagenumber < 1:
        backwardbutton = Button(root,text='Previous',state=DISABLED,width=10,command=lambda:backward(imagenumber-1))
        
    else:
        mylabel.grid_forget()
        mylabel = Label(image=imagelist[imagenumber-1])
        forwardbutton = Button(root,text='Next',width=10,command=lambda:forward(imagenumber+1))
        forwardbutton.grid(row=1,column=2)
        backwardbutton = Button(root,text='Previous',width=10,command=lambda:backward(imagenumber-1))
        backwardbutton.grid(row=1,column=0)
        mylabel.grid(row=0,column=0,columnspan=3)
        status = Label(root,text=f'Image {imagenumber} of {numofimages}',bd=0,border=0,relief=SUNKEN,pady=10)
        status.grid(row=2,column=1)

    

    
exitprogram = Button(root,text='Exit',command=root.quit,width=10)
forwardbutton = Button(root,text='Next',width=10,command=lambda:forward(2))
backwardbutton = Button(root,text='Previous',width=10,command=lambda:backward(1))
status = Label(root,text=f'Image 1 of {numofimages}',border=0,relief=SUNKEN,pady=10,bd=0)
status.grid(row=2,column=1)
forwardbutton.grid(row=1,column=2)
backwardbutton.grid(row=1,column=0)
exitprogram.grid(row=1,column=1)









root.mainloop()
