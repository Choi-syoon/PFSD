import customtkinter as ctk

main = ctk.CTk() 
main.title("PFSD Desktop GUI")
main.geometry("960x640")
main.resizable(False, False)
main._set_appearance_mode('dark')


# Functions


# Options
# btn_canny = ctk.CTkButton(main, text="PFSD GUI Program")
# btn_canny.grid(row=1, column=0)


# Sub-section
sub_panel = ctk.CTkFrame(main)
sub_panel.pack(side='bottom', padx=100)


main.mainloop()