from tkinter import *

root = Tk()
root.title('Transparent')
#root.iconbitmap('dinasour.ico')
root.geometry("500x500")

#root.wm_attributes('-alpha', 0.5)
root.wm_attributes('-transparentcolor','red')

my_frame = Frame(root, width=200, height=200,bg="red")
my_frame.pack(pady=20)

root.mainloop()