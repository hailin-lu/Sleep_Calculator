from tkinter import *
import tkinter.ttk
from tkinter import messagebox as mb

root= Tk()
root.title('Sleep Cycle Calculator')

Label(root,text='This sleep calculator helps you to figure out when you should go to bed.\nYou will be given several results based on your desired time to wake up.\nThe suggested sleep cycles are refered from National Sleep Foundation.').grid(row=0,column=0, columnspan=3)
hour= Entry(root,width=5,borderwidth=2)
hour.grid(row=1,column=0,columnspan=1,padx=5,pady=5,sticky=E)

hourLabel = Label(root,text=':').grid(row=1,column=1)

minute = Entry(root,width=5,borderwidth=2)
minute.grid(row=1,column=2,columnspan=1,padx=5,pady=5,sticky=W)

def button_calculate():

    hour_get = hour.get()
    minute_get = minute.get()
    if (hour_get=='' or minute_get==''):
        mb.showerror('Error','You have not entered the time.')
    else:
        try:
            if (int(hour_get)>24 or int(minute_get)>60 or int(hour_get)<0 or int(minute_get)<0):
                mb.showerror('Error','You have not entered the time properly.')
            if (int(hour_get)<=24 and int(minute_get)<=60 and int(hour_get)>=0 and int(minute_get)>=0):
                total_minutes= int(hour.get())*60+int(minute.get())
                off_set_1 = total_minutes- 7.5*60
            # 5 sleep cycles
                hour_one= int(24+ off_set_1//60)
                if (hour_one>24):
                    hour_one%=24

                if (off_set_1%60 <0):
                    minute_1= int(0 - off_set_1%60)
                else:
                    minute_1=int(0 + off_set_1%60)

                if (minute_1 != 0 and minute_1//10==0):
                    minute_1= '0'+ str(minute_1)
                if (minute_1 ==0):
                    minute_1= str(minute_1)+'0'

                option_1_hour= Label(root,text='In order to get 5 sleep cycles, you need to go to sleep at '+ str(hour_one)+':'+str(minute_1)).grid(row=3,column=0,columnspan=3)

            # 6 sleep cycles
                off_set_2= total_minutes-9.0*60
                hour_two= int(24+ off_set_2//60)
                if (hour_two>24):
                    hour_two%=24

                if (off_set_2%60 <0):
                    minute_2= int(0 - off_set_2%60)
                else:
                    minute_2=int( 0 + off_set_2%60)

                if (minute_2 != 0 and minute_2//10==0):
                    minute_2= '0'+ str(minute_2)
                if (minute_2 ==0):
                    minute_2= str(minute_2)+'0'

                option_2_hour= Label(root,text='In order to get 6 sleep cycles, you need to go to sleep at '+ str(hour_two)+':'+str(minute_2)).grid(row=4,column=0,columnspan=3)
        except ValueError:
            mb.showerror('Error','Only numbers are allowed in the boxes.')


button= Button(root,text='Enter The Time You Want To Get Up',command= button_calculate)
button.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

tkinter.ttk.Separator(root, orient=VERTICAL).grid(column=3, row=0, rowspan=8, sticky='ns')

Guidline_title = Label(root, text='Sleep cycle guidelines').grid(column=4,row=0,columnspan=2)
six_thirteen = Label(root, text='6 to 13 years: 6~7 sleep cycles').grid(column=4,row=1,columnspan=2)
fourteen_seventeen = Label(root, text='14 to 17 years: 5 ~6 sleep cycles').grid(column=4,row=2,columnspan=2)
eighteen_64 = Label(root, text='18 to 64 years:5 ~6 sleep cycles').grid(column=4,row=3,columnspan=2)
sixtyfive_above= Label(root, text='65 years and older: 5 sleep cycles').grid(column=4,row=4,columnspan=2)


button_quit = Button(root, text='Quit the Calculator',command= root.quit)
button_quit.grid(row=5,column =0, columnspan=3, padx=5, pady=5)

root.mainloop()
