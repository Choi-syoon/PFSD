import serial
import serial.tools.list_ports as sp
import threading
import tkinter as tk
import customtkinter as ctk


#-----Main-----
main = ctk.CTk() 
main.title("PFSD Desktop GUI")
main.geometry("960x640")
main.resizable(False, False)
main._set_appearance_mode('dark')


# -----Functions-----


# -----Sub-section-----
sub_panel = ctk.CTkFrame(main)
sub_panel.pack(side='bottom', padx=100)

# request communicate section


# -----Serial Communicate section-----
# def Find_Serial_ports():
#     serial_list = sp.comports()
#     available_port = []
#     for p in serial_list:
#         available_port.append(p.device)
#     return available_port

# def on_combobox_select(event):
#     selected_value = Serial_Cbx.get()
#     print("Selected value:", selected_value)

# Serial_Cbx = ctk.CTkComboBox(main, values=Find_Serial_ports())
# Serial_Cbx.pack()
# Serial_Cbx.bind("<<ComboboxSelected>>", on_combobox_select)

main.mainloop()