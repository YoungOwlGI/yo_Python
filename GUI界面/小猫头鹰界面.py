import tkinter

window = tkinter.Tk()
window.title("小猫头鹰")
window.geometry("1600x900")
labell = tkinter.Label(window, text="小猫头鹰\nYoung Owl", bg="blue", fg="cyan", font=("千图小兔体", 200), width=1600,
                       height=900)
labell.pack()
window.mainloop()
