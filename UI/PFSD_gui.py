import serial
import serial.tools.list_ports as sp
import threading
import tkinter as tk
import customtkinter as ctk


#-----Main-----
main = ctk.CTk() 
main.title("PFSD Desktop GUI")
main.geometry("500x480")
main.resizable(False, False)
ctk.set_appearance_mode('dark')


# -----Functions-----


# -----Sub-section-----
video_panel = ctk.CTkCanvas(main, width=512, height=384)
video_panel.grid(padx=30, pady=20)
option_panel = ctk.CTkFrame(main, corner_radius=10, height=100)
option_panel.grid()
btn_panel = ctk.CTkFrame(option_panel, height=70)
btn_panel.grid(row=0, column=0)
communication_panel = ctk.CTkFrame(option_panel, height=70)
communication_panel.grid(row=0, column=1)

canny_cbx = ctk.CTkCheckBox(btn_panel, text='Canny')
canny_cbx.grid(row=0, column=0, ipady=10)
roi_cbx = ctk.CTkCheckBox(btn_panel, text='ROI')
roi_cbx.grid(row=1, column=0, ipady=10)
roi_canny_cbx = ctk.CTkCheckBox(btn_panel, text="ROI Canny")
roi_canny_cbx.grid(row=0, column=1)
lanes_cbx = ctk.CTkCheckBox(btn_panel, text="Lanes")
lanes_cbx.grid(row=1, column=1)

communication_label = ctk.CTkLabel(communication_panel, text="Communication IP")
communication_label.grid(row=0, column=0)
communication_tbx = ctk.CTkTextbox(communication_panel, height=50)
communication_tbx.grid(row=1, column=0)

# ----- Option Button actions -----
canny_action = ''

# target_ip_label = ctk.CTkLabel(sub_panel, text="Please Entered WebServer IP")
# target_ip_label.grid(row=0, column=0)

# connect_ip_tbx = ctk.CTkTextbox(sub_panel)
# connect_ip_tbx.grid(row=1, column=0)

# request communicate section


main.mainloop()