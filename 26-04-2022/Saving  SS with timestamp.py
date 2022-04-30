#!/usr/bin/env python
# coding: utf-8

# In[4]:


#to save a image anywhere in the system 
from tkinter import Tk, filedialog #tinker can be used for opening the search browser to select a folder
import os
import pyautogui #pyautogui is used to take screenshot using python
import time
n=5
k=n-1
#making the star pyramid
for i in range (0,n):
    for j in range(0,k):
        print(end=" ")
    k=k-1
    for j in range(0,i+1):
        print("*",end=" ")
    print("\r")
time.sleep(5)
#taking screenshot
screen=pyautogui.screenshot()
#using tkinter to open the browsing window to select the path
open_file = filedialog.askdirectory()
file=os.path.join(open_file,"hello"+new_time+".jpg") #adding time stamp so that the name is always different new_time is defined below
screen.save(file)


# Using timestamp with name to save the file so that the name never repeats

# In[6]:


#formatting date and time
from datetime import datetime
current_time=datetime.now().replace(microsecond=0)#removing microseconds from time
forma ="%y_%b_%d_%H_%M_%S"#we can use %B for full month name
new_time=datetime.strftime(current_time,forma)#formatting the current_time and converting it to string so that we can concat it later
new_time


# In[3]:


print(current_time)#date format before formatting
type(current_time) #date type before formatting


# In[5]:


type(new_time) #date type after formatting

