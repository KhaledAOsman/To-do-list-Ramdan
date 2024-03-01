#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
import pandas as pd
from datetime import datetime
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# In[2]:


def update_time():
    current_time = datetime.now().strftime('%Y-%m-%d')
    time_label.config(text=current_time)
    app.after(1000, update_time)  


# In[3]:


excel_file = "رمضان-1445.xlsx"
try:
    df = pd.read_excel(excel_file, index_col='التاريخ')
except FileNotFoundError:

    df = pd.DataFrame(columns=['الدعاء', 'الصلاة', 'قراءة القرآن', 'الزكاة', 'صلة الأرحام', 'الصدقة', 'الاعتكاف'])


# In[4]:


def exit():
     app.destroy()


# In[5]:


def on_button_click():
    global df 
    selected_values = [var.get() for var in vars]
    date = datetime.now().strftime('%Y-%m-%d')
    
    new_data = {
                'الدعاء': selected_values[0],
                'الصلاة': selected_values[1],
                'قراءة القرآن': selected_values[2],
                'الزكاة': selected_values[3],
                'صلة الأرحام': selected_values[4],
                'الصدقة': selected_values[5],
                'الاعتكاف': selected_values[6]}
    
    df.loc[date] = new_data

    df.to_excel(excel_file, index_label='التاريخ')

    messagebox.showinfo("رمضان 1445-1446","تم الحفظ")
    app.destroy()


# In[6]:


def update_radio_buttons(vars):

    if not df.empty:
        last_row = df.iloc[-1]
        for i, label in enumerate(labels):
            vars[i].set(last_row[label])


# In[7]:


def create_dashboard():
    global df
    if df.empty:
        print("DataFrame is empty. Cannot create dashboard.")
        return


    app.withdraw()
    dashboard_window = tk.Toplevel()
    dashboard_window.title("Dashboard")

    screen_width = dashboard_window.winfo_screenwidth()
    screen_height = dashboard_window.winfo_screenheight()
    window_width = dashboard_window.winfo_reqwidth()
    window_height = dashboard_window.winfo_reqheight()
    x_coordinate = (screen_width - window_width) // 2
    y_coordinate = (screen_height - window_height) // 2

    dashboard_window.geometry("+{}+{}".format(x_coordinate, y_coordinate))

    column_sums = df.sum()

    plt.figure(figsize=(6, 4))
    column_sums.plot(kind='bar')
    plt.xlabel('Column Name')
    plt.ylabel('Sum of Data')
    plt.title('Sum of Data for Each Column')

    dashboard_canvas = FigureCanvasTkAgg(plt.gcf(), master=dashboard_window)
    dashboard_canvas.draw()
    dashboard_canvas.get_tk_widget().pack()


    def close_dashboard():
        dashboard_window.destroy()
        app.deiconify()
        
        
    dashboard_window.protocol("WM_DELETE_WINDOW", close_dashboard)


# In[9]:


import tkinter as tk

# Create the main application window
app = tk.Tk()
app.title("رمضان 1445-1446")


time_label = tk.Label(app, font=('Cario', 18))
time_label.pack()
update_time()


labels = ['الدعاء', 'الصلاة', 'قراءة القرآن', 'الزكاة', 'صلة الأرحام', 'الصدقة', 'الاعتكاف']
vars = [tk.IntVar() for _ in range(len(labels))]
radio_buttons=[]


for i, label in enumerate(labels):
    label_widget = tk.Label(app, text=label)
    label_widget.pack()
    radio_yes = tk.Radiobutton(app, text="Yes", variable=vars[i], value=1)
    radio_no = tk.Radiobutton(app, text="No", variable=vars[i], value=0)
    
    radio_yes.pack()
    radio_no.pack()
    radio_buttons.append((label_widget, radio_yes, radio_no))
    

update_radio_buttons(vars)    
    
    
button = tk.Button(app, text="حفظ", command=on_button_click)
button.pack()

dashboard_button = tk.Button(app, text="Sample Dashboard", command=create_dashboard)
dashboard_button.pack()


dashboard_button = tk.Button(app, text="خروج", command=exit)
dashboard_button.pack()


app.update_idletasks()
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
window_width = app.winfo_reqwidth()
window_height = app.winfo_reqheight()
x_coordinate = (screen_width - window_width) // 2
y_coordinate = (screen_height - window_height) // 2
app.geometry("+{}+{}".format(x_coordinate, y_coordinate))



# Run the application
app.mainloop()




# In[ ]:





# In[ ]:




