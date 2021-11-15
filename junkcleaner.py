# import modules
import os  
import glob  
import shutil  
from tkinter import * 
import base64
import getpass 

#window creation
window = Tk()
window.geometry('400x300')
window.resizable(0, 0)

#Title
window.title('Junk cleaner')

#function for deleting temp files
def clean():
    #path as string
    path = 'C:/Users/' + getpass.getuser() + '/AppData/Local/Temp'


    folders = path + '/*'
    folders = glob.glob(folders)
    for file in os.listdir(path):
        files = os.path.join(path, file)     #joining path
        try:
            os.unlink(files)     #removing files
            print('Deleted')
        except:
            print('File cannot be deleted') 


    for folder in folders:
        try:
            shutil.rmtree(folder)  #Removes a folder
            print('Directory deleted')
        except:
            print('Directory cannot be deleted')
    Label(window, text='Done', font='arial 10 bold', bg="white", fg="black", cursor="heart").place(x=168, y=200) #done message
    Label(window, text='Tip:Empty your recycle bin', font='arial 10 bold', bg="white", fg="black",
          cursor="heart").place(x=100, y=240) #tip message


Button(window, font='arial 10 bold', text='clean', padx=2, bg='LightGray', command=clean).place(x=165, y=130) #clean button gui
window.mainloop() #stop window
