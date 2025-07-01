'''
    QQ消息轰炸程序。（错误）
    需要下载库 pywin32
'''
import win32gui
import win32con

for i in range(15):
    yo_1 = win32gui.FindWindow(None, "纳西妲")
    win32gui.SendMessage(yo_1, win32con.WM_PASTE)
    win32gui.SendMessage(yo_1, win32con.WM_KEYDOWN,
                         win32con.VK_RETURN)
