import tkinter
# from tkinter import *
#
# window= Tk()
# window.minsize(width=900, height=550)
# window.config(padx=5, pady=5)
# window.title("American Chase")
# canvas= Canvas(width=900, height=550,  background="#A0E9FF")
#
# title= Label(text="Health Card",fg="black", bg="#A0E9FF", font=("Arial",28,"bold"))
# title.place(x=370,y=10)
#
#
# client_name= Label(text="Client Name= ",fg="black", bg="#A0E9FF", font=("Arial",15))
# client_name.place(x=10, y=50)
# value_1= Entry(width=15, bg="#A0E9FF").place(x=110,y=50)
#
# analyst_name= Label(text="Support Analyst= ",fg="black", bg="#A0E9FF", font=("Arial",15))
# analyst_name.place(x=300,y=50)
# value_2= Entry
# canvas.pack()
# window.mainloop()
from tkinter import *
import csv
# from pandas import *

#Function to handle button click event
# def submit():
#     client_name = client_name_entry.get()
#     support_name = support_name_entry.get()
#     analyst_name= analyst_name_entry.get()
#     result_label.config(text=f"Client Name: {client_name}\nSupport Name: {support_name}\nAnalyst Name: {analyst_name}")
def save_csv():
    data=[client_name_entry.get(),support_name_entry.get(),analyst_name_entry.get(),projectD_entry.get(),projects_entry.get(),
          support_entry.get(),client_entry.get(),project_entry.get()]

    with open('healthcard.csv','a',newline='') as file:
        writer=csv.writer(file)
        writer.writerow(data)

    client_name_entry.delete(0,tkinter.END)
    support_name_entry.delete(0,tkinter.END)
    analyst_name_entry.delete(0,tkinter.END)
    projectD_entry.delete(0,tkinter.END)
    projects_entry.delete(0,tkinter.END)



# Create main window
root= Tk()
root.minsize(width=700, height=500)
root.resizable(0,0)
root.config(bg="#D2E0FB")
root.title("Health Card (V 1.0)")

# Create and place labels and entry widgets for client name
client_name_label = Label (root, text="Client Name:", foreground="black", bg="#D2E0FB",font=("Arial",14,"bold"))
client_name_label.place(x=10, y=50)
client_name_entry = Entry(root, bg="white", foreground="black")
client_name_entry.place(x=130, y=50)

# Create and place labels and entry widgets for support name
support_name_label = Label(root, text="Support Name:", bg="#D2E0FB", foreground="black", font=("Arial",14,"bold"))
support_name_label.place(x=10, y=200)
support_name_entry = Entry(root, bg="white", foreground="black")
support_name_entry.place(x=130, y=200)

# Create and place labels and entry widgets for Analyst name
system_analyst_label = Label(root, text="System Analyst:", bg="#D2E0FB", foreground="black", font=("Arial",14,"bold"))
system_analyst_label.place(x=10, y=350)
analyst_name_entry = Entry(root, bg="white", foreground="black")
analyst_name_entry.place(x=130,y=350)

support_1_label= Label(root, text="Support Aval:", bg="#D2E0FB", foreground="black",font=("Arial",14,"bold"))
support_1_label.place(x=400, y=50)
support_entry= Spinbox(from_=0, to=10, width=5 , bg="white", foreground="black")
support_entry.place(x=620, y=50)
#
client_comms= Label(root, text="Comms Client:", bg="#D2E0FB", foreground="black",font=("Arial",14,"bold"))
client_comms.place(x=400, y=130)
client_entry= Spinbox(from_=0, to=10, width=5, bg="white", foreground="black" )
client_entry.place(x=620, y=130)
#
projectU= Label(root, text="Project Understanding:", bg="#D2E0FB", foreground="black",font=("Arial",14,"bold"))
projectU.place(x=400,y=210)
project_entry= Spinbox(from_=0, to=10, width=5, bg="white", foreground="black" )
project_entry.place(x=620, y=210)
#
projectD= Label(root, text="Deliverabilty:", bg="#D2E0FB", foreground="black",font=("Arial",14,"bold"))
projectD.place(x=400, y=290)
projectD_entry= Entry(root, bg="white", foreground="black")
projectD_entry.place(x=500, y=290)
#
project_s= Label(root, text="Project scope:",  bg="#D2E0FB", foreground="black",font=("Arial",14,"bold"))
project_s.place(x=400, y=370)
projects_entry= Entry(root, bg="white", foreground="black")
projects_entry.place(x=500, y=370)





# Create and place submit button
submit_button = Button(root, text="Submit", bg="white",command=save_csv)
submit_button.place(x=300, y=450)




# Create label to display the result
# result_label = Label(root, text="")
# result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)


# Start the main loop
root.mainloop()
