from Tkinter import *
import os
import speech_recognition as sr 

root = Tk(className = 'face_recognition_gui')
root.title('Face Recognizer');
svalue = StringVar() # defines the widget state as string


l = Label(root, text="Add new person")
l.config(font=("Courier", 30))
l.pack()

w = Entry(root,textvariable=svalue) # adds a textarea widget
w.pack()
r = sr.Recognizer()                                                                                   

    

    def train_lbph_btn_load():
       name = svalue.get()
       os.system('python train_lbph.py %s'%name)


    def recog_lbph_btn_load():
       os.system('python recog_lbph.py')

    def add_person():
       name = svalue.get()
       os.system('python add_person.py %s'%name)

    add_btn = Button(root,text="Add", command=add_person)
    add_btn.pack()

    f=Frame(root,height=1, width=400, bg="black")
    f.pack()

    l = Label(root, text="Train")
    l.config(font=("Courier", 30))
    l.pack()



    recogL_btn = Button(root,text="Train (LBPH)", command=train_lbph_btn_load)
    recogL_btn.pack()

    f=Frame(root,height=1, width=400, bg="black")
    f.pack()

    l = Label(root, text="Recognize")
    l.config(font=("Courier", 30))
    l.pack()



    recogL_btn = Button(root,text="Recognize (LBPH)", command=recog_lbph_btn_load)
    recogL_btn.pack()


    root.mainloop()
else:
    print("try again")
