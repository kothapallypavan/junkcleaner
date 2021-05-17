# import modules
import os  # for os operations
import glob  # for paths
import shutil  #for removing folders
from tkinter import * #for GUI
import base64
import getpass #to get username

#creating and resizeing window
window = Tk()
window.geometry('400x300')
window.resizable(0, 0)

#added title
window.title('Junk cleaner')

#function to delete temp files
def clean():
    #path as string
    path = 'C:/Users/' + getpass.getuser() + '/AppData/Local/Temp'


    folders = path + '/*'
    folders = glob.glob(folders)

    #loop for every file in temp folder
    for file in os.listdir(path):
        files = os.path.join(path, file)     #joining path
        try:
            os.unlink(files)     #removing files
            print('Deleted')
        except:
            print('File cannot be deleted') #if any occurs such as try againa it will not delete file

    #loop for every folder in temp
    for folder in folders:
        try:
            shutil.rmtree(folder)  #it will remove folders
            print('Directory deleted')
        except:
            print('Directory cannot be deleted')
    Label(window, text='Done', font='arial 10 bold', bg="white", fg="black", cursor="heart").place(x=168, y=200) #done message
    Label(window, text='Tip:Empty your recycle bin', font='arial 10 bold', bg="white", fg="black",
          cursor="heart").place(x=100, y=240) #tip message


Button(window, font='arial 10 bold', text='clean', padx=2, bg='LightGray', command=clean).place(x=165, y=130) #clean button gui
window.mainloop() #stop window
