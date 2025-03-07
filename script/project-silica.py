# Pretty crappy code but it will do

# For the one other contributor: Fix my Python because I haven't learned it yet

from customtkinter import *
import pymem
from pynput.mouse import Button, Controller
from ReadWriteMemory import ReadWriteMemory

# MENU
menu = CTk()
menu.geometry("300x200")
set_appearance_mode("dark")
menu.resizable(False, False)
menu.title("project silica")

# MODULES
mouse = Controller()

# Initialize variables in-function !
# (except if it is common across two functions)

rwm = ReadWriteMemory()
process = rwm.get_process_by_name('Minecraft.Windows.exe')

# Globals:
velx = process.get_pointer(0x0, offsets=[0x0])
vely = process.get_pointer(0x0, offsets=[0x0])
velz = process.get_pointer(0x0, offsets=[0x0])

def reach() : 
    reach_ptr = process.get_pointer(0x0, offsets=[0x0]) # Ill add offsets later once I get to reversing

# def clicker() : 

# def velocity() : 

def speed() :
    speed_ptr = process.get_pointer(0x0, offsets=[0x0])

# def vanillaFly() :             # For these two I should make faster

# def motionFly() : 

# def bhop() :

def hitbox() : 
    x_hitboxPtr = process.get_pointer(0x0, offsets=[0x0])
    y_hitboxPtr = process.get_pointer(0x0, offsets=[0x0])

# BUTTONS

combat = CTkButton(master=menu, text="combat") 
combat.place(relx=0.01,rely=0.01)

movement = CTkButton(master=menu, text="movement")
movement.place(relx=0.01,rely=0.20)

settingsmisc = CTkButton(master=menu, text="settings/misc")
settingsmisc.place(relx=0.01,rely=0.40)

# Gui Settings(for modes)

def flyHandler() : {
    
}

# LOOP
menu.mainloop()
