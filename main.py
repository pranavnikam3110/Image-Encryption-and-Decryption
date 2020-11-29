from tkinter import *
from tkinter import filedialog

root = Tk()

root.geometry("200x160")
root.maxsize(200 ,160)
root.minsize(200,160)


root.title("Image Encryptor and Decryptor")
root.iconbitmap(r'picture.ico')


def encrypt_impage():
    file1=filedialog.askopenfile(mode='r',filetype=[('jpg file', '*.jpg'), ('png file', '*.png')])
    if file1 is not None:
        print(file1)
        file_name=file1.name
        print(file_name)
        key=entry1.get(1.0,END)
        print(file_name,key)
        fi=open(file_name,'rb')
        image=fi.read()
        fi.close()
        image=bytearray(image)
        for index,values in enumerate(image):
            image[index]=values^int(key)

        fi1=open(file_name,'wb')    
        fi1.write(image)
        fi1.close()


a=Label(text="Enter the Password\n for your Image :")
a.pack()

b1=Button(root,text="Encrypt",background='red', foreground='Black', command=encrypt_impage)
b1.place(x=70,y=70)


entry1=Text(root,height=1,width=10)
entry1.place(x=52,y=40)



root.mainloop()