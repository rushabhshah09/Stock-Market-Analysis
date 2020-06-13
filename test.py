import tkinter as tk
from functools import partial
from tkinter import ttk
from tkcalendar import *
from tkinter import *
import json
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.figure import Figure
from matplotlib import style
style.use("ggplot")
from tkinter import messagebox
from pandas import Series, DataFrame
import pandas as pd
import datetime
import pandas_datareader.data as web
from alpha_vantage.timeseries import TimeSeries
import matplotlib.dates
import matplotlib.pyplot as plt
from matplotlib import style
from nsetools import Nse
nse = Nse()

LARGE_FONT= ("Verdana",15)
class stockanalysis(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        container=tk.Frame(self)
        container.pack(side="top",fill="both",expand=True)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)
        self.frames= {}
        for F in(HomePage,StartPage,GraphPage):
            frame= F(container,self)
            self.frames[F]=frame
            frame.grid(row=0,column=0,sticky="nsew")
        self.show_frame(StartPage)
    def show_frame(self,cont):
        frame=self.frames[cont]
        frame.tkraise()

def exitt():
    exit()



class GraphPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        label=tk.Label(self,text="Graphs",fg="blue",bg="yellow",relief="solid",font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        label1 = tk.Label(self, text=" Select Company Name : ", fg="red",bg="lightgreen",relief="solid",font=("arial",10,"bold"))
        label1.place(x=100, y=75)
        cname=StringVar()



        list = ['BAJAJ FINANCE', 'RELIANCE', 'TATAMOTORS']
        droplist = OptionMenu(self, cname, *list)
        cname.set("COMPANY ")
        droplist.config(font=("Arial", 9, "bold"), fg="red", bg="white")
        droplist.place(x=270, y=68)

        def compare():
            def calval():
                messagebox.showinfo("You selected ", cal.get_date())
                start1 = cal.get_date()
                star = datetime.datetime.strptime(start1, '%m/%d/%y')
                mm = star.strftime('%m')
                dd = star.strftime('%d')
                yy = star.strftime('%Y')
                start = datetime.datetime(int(yy), int(mm), int(dd))
                end = datetime.datetime(2019, 10, 22)
                stock = \
                web.DataReader(['RELIANCE.NS', 'TATAMOTORS.NS', 'BAJFINANCE.NS'], 'yahoo', start=start, end=end)[
                    'Adj Close']
                stock.plot(grid=True)

            sen = "SELECT START DATE FIRST "
            messagebox.showinfo("Select date", sen)
            cal = Calendar(self, selectmode="day", year=2019, month=5, day=17)
            cal.place(x=370, y=10)

            btn5 = Button(self, text="Select date", command=calval)
            btn5.place(x=550, y=195)

        def EMA(*args):
            txtname1=cname.get()
            def first(*args):
                start = datetime.datetime(2017, 5, 1)
                end = datetime.datetime(2019, 10, 22)
                if txtname1=="RELIANCE":
                    df = web.DataReader("RELIANCE.NS", 'yahoo', start, end)
                if txtname1 == "TATAMOTORS":
                    df = web.DataReader("TATAMOTORS.NS", 'yahoo', start, end)
                if txtname1 == "BAJAJ FINANCE":
                    df = web.DataReader("BAJFINANCE.NS", 'yahoo', start, end)


                AC = df['Adj Close']
                return AC

            AC = first()
            ema20 = AC.ewm(span=20, adjust=False).mean()
            ema50 = AC.ewm(span=50, adjust=False).mean()
            pd.DataFrame({
                txtname1: AC,
                'EMA20': ema20,
                'EMA50': ema50
            }).plot(
                title='Close Price / EMA Crossover'
            );

        def SMA(*args):
            txtname1=cname.get()
            def calval():
                messagebox.showinfo("You selected ", cal.get_date())
                start1 = cal.get_date()
                star = datetime.datetime.strptime(start1, '%m/%d/%y')
                mm = star.strftime('%m')
                dd = star.strftime('%d')
                yy = star.strftime('%Y')
                txtname1 = cname.get()

                if txtname1 == "RELIANCE":
                    start = datetime.datetime(int(yy), int(mm), int(dd))
                    end = datetime.datetime(2019, 10, 22)
                    df = web.DataReader("RELIANCE.NS", 'yahoo', start, end)
                    AC = df['Adj Close']
                    sma20 = AC.rolling(20).mean()
                    sma50 = AC.rolling(50).mean()
                    style.use('ggplot')
                    AC.plot(label='Reliance')
                    pd.DataFrame({
                        txtname1: AC,
                        'SMA20': sma20,
                        'SMA50': sma50
                    }).plot(
                        title='Close Price / SMA Crossover'
                    );
                    sma20.plot(label='Reliance')
                    sma50.plot(label='Reliance')

                if txtname1 == "TATAMOTORS":
                    start = datetime.datetime(int(yy), int(mm), int(dd))
                    end = datetime.datetime(2019, 10, 22)
                    df = web.DataReader("TATAMOTORS.NS", 'yahoo', start, end)
                    AC = df['Adj Close']
                    sma20 = AC.rolling(20).mean()
                    sma50 = AC.rolling(50).mean()
                    style.use('ggplot')
                    AC.plot(label='TataMotors')
                    pd.DataFrame({
                        txtname1: AC,
                        'SMA20': sma20,
                        'SMA50': sma50
                    }).plot(
                        title='Close Price / SMA Crossover'
                    );
                    sma20.plot(label='TataMotors')
                    sma50.plot(label='TataMotors')

                if txtname1 == "BAJAJ FINANCE":
                    start = datetime.datetime(int(yy), int(mm), int(dd))
                    end = datetime.datetime(2019, 10, 22)
                    df = web.DataReader("BAJFINANCE.NS", 'yahoo', start, end)
                    AC = df['Adj Close']
                    style.use('ggplot')
                    sma20 = AC.rolling(20).mean()
                    sma50 = AC.rolling(50).mean()
                    AC.plot(label='Bajaj Finance')
                    pd.DataFrame({
                        txtname1: AC,
                        'SMA20': sma20,
                        'SMA50': sma50
                    }).plot(
                        title='Close Price / SMA Crossover'
                    );
                    sma20.plot(label='Bajaj Finance')
                    sma50.plot(label='Bajaj Finance')

            sen = "SELECT START DATE FIRST "
            messagebox.showinfo("Select date", sen)
            cal = Calendar(self, selectmode="day", year=2019, month=10, day=22)
            cal.place(x=370, y=10)

            btn5 = Button(self, text="Select date", command=calval)
            btn5.place(x=550, y=195)

        def first(*args):
            def calval():
                messagebox.showinfo("You selected", cal.get_date())
                start1 = cal.get_date()
                star = datetime.datetime.strptime(start1, '%m/%d/%y')
                mm = star.strftime('%m')
                dd = star.strftime('%d')
                yy = star.strftime('%Y')
                txtname1 = cname.get()

                if txtname1 == "RELIANCE":
                    start = datetime.datetime(int(yy), int(mm), int(dd))
                    end = datetime.datetime(2019, 10, 22)
                    df = web.DataReader("RELIANCE.NS", 'yahoo', start, end)
                    AC = df['Adj Close']
                    return AC
                if txtname1 == "TATAMOTORS":
                    start = datetime.datetime(int(yy), int(mm), int(dd))
                    end = datetime.datetime(2019, 10, 22)
                    df = web.DataReader("TATAMOTORS.NS", 'yahoo', start, end)
                    AC = df['Adj Close']
                    return AC
                if txtname1 == "BAJAJ FINANCE":
                    start = datetime.datetime(int(yy), int(mm), int(dd))
                    end = datetime.datetime(2019, 10, 22)
                    df = web.DataReader("BAJFINANCE.NS", 'yahoo', start, end)
                    AC = df['Adj Close']
                    return AC
            sen = "SELECT START DATE FIRST "
            messagebox.showinfo("Select date", sen)
            cal = Calendar(self, selectmode="day", year=2019, month=5, day=17)
            cal.place(x=370, y=10)

            btn5 = Button(self, text="Select date", command=calval)
            btn5.place(x=550, y=195)


        def Historic(*args):

                def calval():
                    messagebox.showinfo("You selected ", cal.get_date())
                    start1 = cal.get_date()
                    star = datetime.datetime.strptime(start1, '%m/%d/%y')
                    mm = star.strftime('%m')
                    dd = star.strftime('%d')
                    yy = star.strftime('%Y')
                    txtname1 = cname.get()

                    if txtname1 == "RELIANCE":
                        start = datetime.datetime(int(yy), int(mm), int(dd))
                        end = datetime.datetime(2019, 10, 22)
                        df = web.DataReader("RELIANCE.NS", 'yahoo', start, end)
                        AC = df['Adj Close']
                        style.use('ggplot')
                        AC.plot(label='Reliance')
                        plt.show()
                    if txtname1 == "TATAMOTORS":
                        start = datetime.datetime(int(yy), int(mm), int(dd))
                        end = datetime.datetime(2019, 10, 22)
                        df = web.DataReader("TATAMOTORS.NS", 'yahoo', start, end)
                        AC = df['Adj Close']
                        style.use('ggplot')
                        AC.plot(label='TATAMOTORS')
                        plt.show()
                    if txtname1 == "BAJAJ FINANCE":
                        start = datetime.datetime(int(yy), int(mm), int(dd))
                        end = datetime.datetime(2019, 10, 22)
                        df = web.DataReader("BAJFINANCE.NS", 'yahoo', start, end)
                        AC = df['Adj Close']
                        style.use('ggplot')
                        AC.plot(label='BAJFINANCE')
                        plt.show()
                sen="SELECT START DATE FIRST "
                messagebox.showinfo("Select date",sen)
                cal = Calendar(self, selectmode="day", year=2019, month=5, day=17)
                cal.place(x=370, y=10)

                btn5 = Button(self, text="Select date", command=calval)
                btn5.place(x=550, y=195)





        def volu(*args):
            txtname2=cname.get()
            if txtname2=="RELIANCE":
                start = datetime.datetime(2017, 5, 1)
                end = datetime.datetime(2019, 10, 22)
                df = web.DataReader("RELIANCE.NS", 'yahoo', start, end)
                vol = df['Volume']
                style.use('ggplot')
                vol.plot(label='Volume')
                plt.legend()
            if txtname2=="TATAMOTORS":
                start = datetime.datetime(2017, 5, 1)
                end = datetime.datetime(2019, 10, 22)
                df = web.DataReader("TATAMOTORS.NS", 'yahoo', start, end)
                vol = df['Volume']
                style.use('ggplot')
                vol.plot(label='Volume')
                plt.legend()
            if txtname2=="BAJAJ FINANCE":
                start = datetime.datetime(2017, 5, 1)
                end = datetime.datetime(2019, 10, 22)
                df = web.DataReader("BAJFINANCE.NS", 'yahoo', start, end)
                vol = df['Volume']
                style.use('ggplot')
                vol.plot(label='Volume')
                plt.legend()

        def Intraday(*args):
            from pandas import Series, DataFrame
            txtname2=cname.get()
            if txtname2=="RELIANCE":
                ALPHA_VANTAGE_API_KEY = '841Y2OP5B619FK1X'
                ts = TimeSeries(key=ALPHA_VANTAGE_API_KEY, output_format='pandas')
                intraday_data, data_info = ts.get_intraday(
                    'RELIANCE.NS', outputsize='full', interval='1min')
                intraday_data.head()
                intraday_data['4. close'].plot(figsize=(11, 7))
               # plt.title("Intraday Price", fontsize=16)
                plt.ylabel('Price', fontsize=14)
                plt.xlabel('Time', fontsize=14)

                plt.grid(which="major", color='k', linestyle='-.', linewidth=0.5)
                plt.show()
            if txtname2=="TATAMOTORS":
                ALPHA_VANTAGE_API_KEY = '841Y2OP5B619FK1X'
                ts = TimeSeries(key=ALPHA_VANTAGE_API_KEY, output_format='pandas')
                intraday_data, data_info = ts.get_intraday(
                    'TATAMOTORS.NS', outputsize='full', interval='1min')
                intraday_data.head()
                intraday_data['4. close'].plot(figsize=(11, 7))
                #plt.title("Intraday Price", fontsize=16)
                plt.ylabel('Price', fontsize=14)
                plt.xlabel('Time', fontsize=14)

                plt.grid(which="major", color='k', linestyle='-.', linewidth=0.5)
                plt.show()
            if txtname2=="BAJAJ FINANCE":
                ALPHA_VANTAGE_API_KEY = '841Y2OP5B619FK1X'
                ts = TimeSeries(key=ALPHA_VANTAGE_API_KEY, output_format='pandas')
                intraday_data, data_info = ts.get_intraday(
                    'BAJFINANCE.NS', outputsize='full', interval='1min')
                intraday_data.head()
                intraday_data['4. close'].plot(figsize=(11, 7))
               # plt.title("Intraday Price", fontsize=16)
                plt.ylabel('Price', fontsize=14)
                plt.xlabel('Time', fontsize=14)

                plt.grid(which="major", color='k', linestyle='-.', linewidth=0.5)
                plt.show()

        button1 = tk.Button(self, text="Historic Data", command=partial(Historic,cname),relief="raised",fg="white",bg="blue")
        button1.place(x=160,y=205)
        button2 = tk.Button(self, text="Weekly", command=partial(Intraday,cname),relief="raised",fg="white",bg="blue")
        button2.place(x=290,y=205)
        button4 = tk.Button(self, text="Simple Moving Average", command=partial(SMA,cname),relief="raised",fg="white",bg="blue")
        button4.place(x=100,y=275)
        button5 = tk.Button(self, text="Exponential Moving Average", command=partial(EMA,cname),relief="raised",fg="white",bg="blue")
        button5.place(x=375,y=275)
        button8 = tk.Button(self, text="Volume Change", command=partial(volu,cname), relief="raised", fg="white",bg="blue")
        button8.place(x=120, y=330)
        button9 = tk.Button(self, text="Compare ", command=compare, relief="raised", fg="white", bg="blue")
        button9.place(x=430, y=330)
        button6= tk.Button(self, text="Exit", command=exitt,relief="raised",fg="white",bg="blue",font=("arial",12,"bold"))
        button6.place(x=550,y=400)
        button7= tk.Button(self, text="Back", command=lambda: controller.show_frame(HomePage),relief="raised",fg="white",bg="blue",font=("arial",12,"bold"))
        button7.place(x=50,y=400)
class HomePage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label=tk.Label(self,text="Stock Analysis Application",fg="blue",bg="yellow",relief="solid",font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        label1 = tk.Label(self, text=" Select Company Name : ", fg="red",bg="lightgreen",relief="solid",font=("arial",10,"bold"))
        label1.place(x=100, y=75)
        def change(*args):
            sbr = Scrollbar(self)
            sbr.place(x=480,y=250)
            txtname=cname.get()
            if txtname=="RELIANCE":

                q = nse.get_quote('RELIANCE')
                from pprint import pprint  # just for neatness of display
                listbox = Listbox(self, width=50, font=("arial", 10, "bold"), fg="red", bg="Black")

                sbr.config(command=listbox.yview)
                listbox.config(yscrollcommand=sbr.set)
                for key, value in q.items():
                    listbox.insert(10, "    " + key + "  :  " + str(value))

                listbox.place(x=125, y=160)
            if txtname=="TATAMOTORS":
                q = nse.get_quote('TATAMOTORS')
                from pprint import pprint  # just for neatness of display
                listbox = Listbox(self, width=50, font=("arial", 10, "bold"), fg="red", bg="Black")
                sbr.config(command=listbox.yview)
                listbox.config(yscrollcommand=sbr.set)
                for key, value in q.items():
                    listbox.insert(10, "    " + key + "  :  " + str(value))

                listbox.place(x=125, y=160)
            if txtname=="BAJAJ FINANCE":
                q = nse.get_quote('BAJFINANCE')
                from pprint import pprint  # just for neatness of display
                listbox = Listbox(self, width=50, font=("arial", 10, "bold"), fg="red", bg="Black")
                sbr.config(command=listbox.yview)
                listbox.config(yscrollcommand=sbr.set)
                for key, value in q.items():
                    listbox.insert(10, "    " + key + "  :  " + str(value))

                listbox.place(x=125, y=160)

        cname = StringVar()
        list=['BAJAJ FINANCE','RELIANCE','TATAMOTORS']
        droplist=OptionMenu(self,cname,*list)
        cname.set("COMPANY ")
        droplist.config(font=("Arial",9,"bold"),fg="red",bg="white")
        droplist.place(x=270,y=70)
        button1 = tk.Button(self, text="Graphs",  command=lambda: controller.show_frame(GraphPage),font=("arial",12,"bold"),relief="raised",fg="white",bg="blue")
        button1.place(x=50,y=400)
        button2 = tk.Button(self, text="Get InFo", command=partial(change,cname),relief="raised",fg="white",bg="blue")
        button2.place(x=430,y=75)
        button6 = tk.Button(self, text="Exit", command=exitt, relief="raised", fg="white", bg="blue",font=("arial", 12, "bold"))
        button6.place(x=550, y=400)



class StartPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="""        Stock Analysis Application 
        Try at your own risk""", font=LARGE_FONT)

        label.pack(pady=10, padx=10)

        button2 = tk.Button(self, text="Agree", command=lambda: controller.show_frame(HomePage),relief="raised",fg="white",bg="red")
        button2.place(x=255,y=75)
        button3 = tk.Button(self, text="Disagree", command=exitt,relief="raised",fg="white",bg="red")
        button3.place(x=350,y=75)




app=stockanalysis()
app.geometry('620x480')
app.title("Stock Analysis application")

app.mainloop()

