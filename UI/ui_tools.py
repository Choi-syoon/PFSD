import cv2
import customtkinter as ctk
from PIL import Image, ImageTk

class cbx(*args):

    def window_eventor(*args, main):
        global n_window, n_canvas
        n_cbx_state = ctk.IntVar()

        if n_cbx_state.get():
            n_window = ctk.CTkToplevel(main)
            n_window.title("Canny")
            n_canvas = ctk.CTkCanvas(n_window, width=512, height=384)
            n_canvas.pack()
        else:
            if isinstance(n_window, ctk.CTkToplevel):
                n_window.destroy()
                n_canvas = None
    n_canvas = None


    def update_window(main_window_panel, target_window, video):
        _, frame = video.read()

        if _:
            frame = cv2.resize(frame, (512, 384))
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            image = Image.fromarray(frame)
            image_tk = ImageTk.PhotoImage(image=image)

            main_window_panel.create_image(0, 0, anchor='nw', image=image_tk)
            main_window_panel.image_tk = image_tk

            if isinstance(cbx. ,ctk.CTkCanvas):
                cbx..create_image(0, 0, anchor='nw', image=image_tk)
                cbx..image_tk = image_tk

        target_window.after(25 ,update_window)



    