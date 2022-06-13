from cgitb import text
import os
import time
import tkinter as tk
from tkinter.messagebox import NO
from tkinter.ttk import Style, Widget
from turtle import bgcolor, width
import webbrowser
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *

chrome_path = "C:/Users/daved/Documents/repos/Deployment_Helper/Project/pics/chrome.jpg"


# OPEN PPG
def openPPG():
    ppg_window = tk.Toplevel()
    ppg_window.geometry("500x500")
    ppg_lbl = tk.Label(ppg_window, text="PPG")
    ppg_lbl.pack()

    #Input field
    ppg_input = ttk.Entry(ppg_window, width=50)
    ppg_input.pack()

    URLS = (
        "/borrow/mortgages/",
        "/plan/pensions/",
        "/borrow/mortgages/calculators/mortgage-calculator/",
        "/investments-calculator-form/",
        "/investments-goal-saver-calculator/",
        "/investments-regular-saver-calculator/",
        "/children-education-calculator/?accommodationType=rent&childrenAges=6,,,,,,,,,#gf_442",
        "/bank/international-payments/daily-foreign-exchange-rates/?latest=version"
    )
    
    def openFirefox():
        firefox_path = "C://Program Files//Mozilla Firefox//firefox.exe %s"
        firefox = webbrowser.get(firefox_path)
        text = ppg_input.get()

        #Open the PPG homepage
        firefox.open(f"{text}", new=1)
        time.sleep(3)

        status = True
        for url in URLS:
            firefox.open_new_tab(f"{text}{url}")
            time.sleep(3)


    def openChrome():    
        chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s --incognito --start-maximized"
        chrome = webbrowser.get(chrome_path)
        text = ppg_input.get()    

        #Open PPG homepage
        chrome.open(f"{text}", new=1)
        time.sleep(3)

        status = False
        for url in URLS:
            chrome.open_new_tab(f"{text}{url}")
            time.sleep(3) 


    def openEdge():
        edge_path = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge_proxy.exe %s -inprivate --start-maximized"
        edge = webbrowser.get(edge_path)
        text = ppg_input.get()    

        #Open PPG homepage
        edge.open(f"{text}", new=1)
        time.sleep(3)

        status = False
        for url in URLS:
                edge.open(f"{text}{url}", new=2)
                time.sleep(3)

    btn_firefox = ttk.Button(ppg_window, text="Firefox", command=openFirefox).place(x=50, y=75)
    btn_chrome= ttk.Button(ppg_window, text="Chrome", command=openChrome).place(x=200, y=75)
    btn_edge= ttk.Button(ppg_window, text="Edge", command=openEdge).place(x=350, y=75)
    

def openBB():
    bb_window = tk.Toplevel()
    bb_window.geometry("500x500")
    bb_lbl = tk.Label(bb_window, text="BB")
    bb_lbl.pack()

    #Input field
    bb_input = ttk.Entry(bb_window, width=50)
    bb_input.pack()

    URLS = (
        "/business-supports/sectors/",
        "/credit/business-loans/business-loan/features-and-benefits/",
        "/financial-wellbeing/",
        "/support-centre/business-banking/"
    )
    
    def openFirefox():
        firefox_path = "C://Program Files//Mozilla Firefox//firefox.exe %s"
        firefox = webbrowser.get(firefox_path)
        text = bb_input.get()

        firefox.open(f"{text}", new=1)
        time.sleep(3)

        status = True
        for url in URLS:
            firefox.open_new_tab(f"{text}{url}")
            time.sleep(3)


    def openChrome():    
        chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s --incognito --start-maximized"
        chrome = webbrowser.get(chrome_path)
        text = bb_input.get()    

        chrome.open(f"{text}", new=1)
        time.sleep(3)

        status = False
        for url in URLS:
            chrome.open_new_tab(f"{text}{url}")
            time.sleep(3) 


    def openEdge():
        edge_path = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge_proxy.exe %s -inprivate --start-maximized"
        edge = webbrowser.get(edge_path)
        text = bb_input.get()    

        edge.open(f"{text}", new=1)
        time.sleep(3)

        status = False
        for url in URLS:
                edge.open_new_tab(f"{text}{url}")
                time.sleep(3)

    btn_firefox = ttk.Button(bb_window, text="Firefox", command=openFirefox).place(x=50, y=75)
    btn_chrome= ttk.Button(bb_window, text="Chrome", command=openChrome).place(x=200, y=75)
    btn_edge= ttk.Button(bb_window, text="Edge", command=openEdge).place(x=350, y=75)

def openWWW():
    www_window = tk.Toplevel()
    www_window.geometry("500x500")
    www_lbl = tk.Label(www_window, text="WWW")
    www_lbl.pack()

    #Input field
    www_input = ttk.Entry(www_window, width=50)
    www_input.pack()

    URLS = (
        "/branch-locator/",
        "/help-centre/",
        "/kiosk-application-centre/"
    )
    
    def openFirefox():
        firefox_path = "C:/Program Files/Mozilla Firefox/firefox.exe %s"
        firefox = webbrowser.get(firefox_path)
        text = www_input.get()

        firefox.open(f"{text}", new=1)
        time.sleep(3)

        status = True
        for url in URLS:
            firefox.open(f"{text}{url}", new=2)
            time.sleep(3)


    def openChrome():    
        chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s --incognito --start-maximized"
        chrome = webbrowser.get(chrome_path)
        text = www_input.get()    

        chrome.open(f"{text}", new=1)
        time.sleep(3)

        status = False
        for url in URLS:
            chrome.open_new_tab(f"{text}{url}")
            time.sleep(3) 


    def openEdge():
        edge_path = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge_proxy.exe %s -inprivate --start-maximized"
        edge = webbrowser.get(edge_path)
        text = www_input.get()    

        edge.open(f"{text}", new=1)
        time.sleep(3)

        status = False
        for url in URLS:
                edge.open_new_tab(f"{text}{url}")
                time.sleep(3)

    btn_firefox = ttk.Button(www_window, text="Firefox", command=openFirefox).place(x=50, y=75)
    btn_chrome= ttk.Button(www_window, text="Chrome", command=openChrome).place(x=200, y=75)
    btn_edge= ttk.Button(www_window, text="Edge", command=openEdge).place(x=350, y=75)

def openBOIUK():
    boiuk_window = tk.Toplevel()
    boiuk_window.geometry("500x500")
    boiuk_lbl = tk.Label(boiuk_window, text="BOI_UK")
    boiuk_lbl.pack()

    #Input field
    boiuk_input = ttk.Entry(boiuk_window, width=50)
    boiuk_input.pack()

    URLS = (
        "/personal/",
        "/business/",
        "/mortgages/existing-customer/",
        "/daily-foreign-exchange-rates/",
        "/mortgages/existing-customer/calculators/",
        "/mortgages/existing-customer/calculators/overpayment/",
        "/personal/financial-wellbeing/",
        "/personal/what-is-youth-financial-wellbeing/",
        "/help-and-support/"
    )
    
    def openFirefox():
        firefox_path = "C:/Program Files/Mozilla Firefox/firefox.exe %s"
        firefox = webbrowser.get(firefox_path)      
        text = boiuk_input.get()

        firefox.open(f"{text}", new=1)
        time.sleep(3)

        status = True
        for url in URLS:
            firefox.open_new_tab(f"{text}{url}")
            time.sleep(3)


    def openChrome():
        chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s --incognito --start-maximized"
        chrome = webbrowser.get(chrome_path)
        text = boiuk_input.get()    

        chrome.open(f"{text}", new=1, )
        time.sleep(3)

        status = False
        for url in URLS:
            chrome.open_new_tab(f"{text}{url}")
            time.sleep(3) 


    def openEdge():
        edge_path = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge_proxy.exe %s -inprivate --start-maximized"
        edge = webbrowser.get(edge_path)
        text = boiuk_input.get()    

        edge.open(f"{text}", new=1)
        time.sleep(3)

        status = False
        for url in URLS:
                edge.open_new_tab(f"{text}{url}")
                time.sleep(3)

    btn_firefox = ttk.Button(boiuk_window, text="Firefox", command=openFirefox).place(x=50, y=75)
    btn_chrome= ttk.Button(boiuk_window, text="Chrome", command=openChrome).place(x=200, y=75)
    btn_edge= ttk.Button(boiuk_window, text="Edge", command=openEdge).place(x=350, y=75)


root = tk.Tk()
root.geometry("500x500")
root.title("Deployment helper")

root.tk.call("source", "azure.tcl")
root.tk.call("set_theme", "dark")

btn_ppg = ttk.Button(root, text="PPG", command=openPPG).place(x=25, y=25)
btn_bb = ttk.Button(root, text="BB", command=openBB).place(x=25, y=100)
btn_www = ttk.Button(root, text="WWW", command=openWWW).place(x=25, y=175)
btn_boiuk = ttk.Button(root, text="BOI_UK", command=openBOIUK).place(x=25, y=250)


root.mainloop()
# k = input()