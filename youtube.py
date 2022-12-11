import tkinter as tk
from tkinter import*
from pytube import Youtube
from tkinter import messagebox, filedialog

def Widgets():

    head_label = Label(root, text="Youtube Video Downloader using Tkinter",padx=15,pady=15,font="segoeUI 14",bg="palgreen1",fg="red")
    head_label.grid(row=1,column=1,pady=10,padx=5,columnspan=3)

    link_label = Label(root,text="Youtube Link : ",bg="salmon",pady=5,padx=5)
    link_label.grid(row=2,column=0,pady=5,padx=5)

    root.linkText = Entry(root, width=35,textvariable=video_Link,font="Arial 14")
    root.linkText.grid(row=2,column=1,pady=5,padx=5,columnspan=2)

    destination_label=Label(root,text="Destination: ",bg="salmon",pady=5,padx=9)
    destination_label.grid(row=3,column=0,pady=5,padx=5)

    root.destinationText = Entry(root,width=27,textvariable=download_Path,font="Arial 14")
    root.destinationText.grid(row=3,column=1,pady=5,padx=5)

    browse_B = Button(root, text="Browse",command=Browse,width=10,bg="bisque",relief=GROOVE)
    browse_B.grid(row=3,column=2,pady=1,padx=1)

    Download_B = Button(root,text="Download Video",command=Download,width=20,bg="thistle1",pady=10,padx=15,relief=GROOVE,font="Georgia, 13")
    Download_B.grid(row=4,column=1,pady=20,padx=20)


    def Browse():
        download_Directory =filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH",title="Save Video")
        doenload_path.set(download_Directory)
    def Download():
        Youtube_link = video_Link.get()
        download_Folder = download_path.get()
        getVideo = Youtube(Youtube_link)
        videoStream = getVieo.streams.first()
        videoStream.download(download_Folder)
        messagebox.showinfo("SUCCESSFULLY","DOWNLOAD AND SAVED IN\n",download_Folder)

root=tk.TK()
root.geometry("520*280")
root.resizable(False,False)
root.title("Youtube Video Downloader")
Root.config(background="PaleGreen1")

video_Link = StringVar()
download_Path = StringVar()

Widgets()
root.mainloop()