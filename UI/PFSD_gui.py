import serial
import numpy as np
import serial.tools.list_ports as sp
import threading
import cv2
import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import filedialog


# Main
main = ctk.CTk() 
main.title("PFSD Desktop GUI")
main.geometry("500x420")
main.resizable(False, False)
ctk.set_appearance_mode('dark')

# Functions
def roi(target):
    pts = np.array([[35, 400], [235, 250], [370, 250], [480, 400]], np.int32)
    mask = np.zeros_like(target)
    cv2.fillConvexPoly(mask, pts, (255, 255, 255))
    masked = cv2.bitwise_and(target, mask)
    return masked


# Event Functions
def canny_event(*args):
    global canny_window, canny_canvas
    
    if canny_cbx_state.get():
        canny_window = ctk.CTkToplevel(main)
        canny_window.title("Canny")
        canny_canvas = ctk.CTkCanvas(canny_window, width=512, height=384)
        canny_canvas.pack()
    else:
        if isinstance(canny_window, ctk.CTkToplevel):
            canny_window.destroy()
            canny_canvas = None
canny_canvas = None

def roi_canny_event(*args):
    global roi_canny_window, roi_canny_canvas
    
    if roi_canny_cbx_state.get():
        roi_canny_window = ctk.CTkToplevel(main)
        roi_canny_window.title("roi_canny")
        roi_canny_canvas = ctk.CTkCanvas(roi_canny_window, width=512, height=384)
        roi_canny_canvas.pack()
    else:
        if isinstance(roi_canny_window, ctk.CTkToplevel):
            roi_canny_window.destroy()
            roi_canny_canvas = None
roi_canny_canvas = None

# Sub_section
video_panel = ctk.CTkCanvas(main, width=512, height=384)
video_panel.pack()

option_panel = ctk.CTkFrame(main, corner_radius=10, height=100)
option_panel.pack(padx=50)

btn_panel = ctk.CTkFrame(option_panel, height=70)
btn_panel.grid(row=0, column=0)

communication_panel = ctk.CTkFrame(option_panel, height=70)
communication_panel.grid(row=0, column=1)

# Options 
canny_cbx_state = ctk.IntVar()
bird_eye_cbx_state = ctk.IntVar()
roi_canny_cbx_state = ctk.IntVar()
lanes_cbx_state = ctk.IntVar()

canny_cbx_state.trace_add('write', canny_event) # options window 생성 및 command 실행
roi_canny_cbx_state.trace_add('write', roi_canny_event)

# CheckBox 선언
canny_cbx = ctk.CTkCheckBox(btn_panel, text='Canny', variable=canny_cbx_state)
canny_cbx.grid(row=0, column=0, ipady=10)

bird_eye_cbx = ctk.CTkCheckBox(btn_panel, text='Bird_eye', variable=bird_eye_cbx_state)
bird_eye_cbx.grid(row=1, column=0, ipady=10)

roi_canny_cbx = ctk.CTkCheckBox(btn_panel, text="ROI Canny", variable=roi_canny_cbx_state)
roi_canny_cbx.grid(row=0, column=1)

lanes_cbx = ctk.CTkCheckBox(btn_panel, text="Lanes")
lanes_cbx.grid(row=1, column=1)

# Communication 영역 지정
communication_label = ctk.CTkLabel(communication_panel, text="Communication IP")
communication_label.grid(row=0, column=0)
communication_tbx = ctk.CTkTextbox(communication_panel, height=50)
communication_tbx.grid(row=1, column=0)

# Canvas Video stream
source_path = filedialog.askopenfilename()
print("video_path :", source_path)

video = cv2.VideoCapture(source_path)

def update_canny():
    _, frame = video.read()

    if _:
        frame = cv2.resize(frame, (512, 384))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blurred_frame = cv2.GaussianBlur(gray_frame, (5, 5), 0)
        canny_frame = cv2.Canny(blurred_frame, 100,100)
        roi_canny_frame = roi(canny_frame)
        
        image = Image.fromarray(frame)
        image_tk = ImageTk.PhotoImage(image=image)
        canny_image = Image.fromarray(canny_frame)
        canny_image_tk = ImageTk.PhotoImage(image=canny_image)
        roi_canny_image = Image.fromarray(roi_canny_frame)
        roI_canny_tk = ImageTk.PhotoImage(image=roi_canny_image)

        video_panel.create_image(0, 0, anchor='nw', image=image_tk)
        video_panel.image_tk = image_tk
        
        if isinstance(canny_canvas,ctk.CTkCanvas):
            canny_canvas.create_image(0, 0, anchor='nw', image=canny_image_tk)
            canny_canvas.image_tk = canny_image_tk

        if isinstance(roi_canny_canvas ,ctk.CTkCanvas):
            roi_canny_canvas.create_image(0, 0, anchor='nw', image=roI_canny_tk)
            roi_canny_canvas.image_tk = roI_canny_tk

    main.after(25 ,update_canny)
    
update_canny()
main.mainloop()