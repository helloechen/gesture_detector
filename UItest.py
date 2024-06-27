import tkinter as tk
from tkinter import ttk
from auto_control_copy import *


def print_one():
    print(1)
    label2['text'] = "使用ing(ﾉ´ヮ`)ﾉ*:"
    label2['foreground'] = 'green'
    start_button['state'] = 'disabled'
    main()

def print_five():
    print(f"退出按钮的状态为：{start_button['state']}")
    if start_button['state'] == 'normal':
        print("退出系统")
        root.destroy()
    else:
        label2['text'] = "再见喽(^o^)"       # 这个地方用不着放global权限符
        label2['foreground'] = 'red'
        start_button['state'] = 'normal'
        out()
        
        

root = tk.Tk()
root.title("手势识别优化：提升短视频浏览体验的智能交互技术")
img_pic = tk.PhotoImage(file = 'pic3.png')


root.configure(bg='#D3D3D3')


root.geometry("800x400")  # 设置窗口宽度为800像素，高度为400像素

frame = ttk.Frame(root, padding="20")
frame.pack(fill=tk.BOTH, expand=True)

label_text1 = '''                 手势识别优化：
提升短视频浏览体验的智能交互系统'''
label_text2 = "欢迎(≧▽≦)/！"
label1 = ttk.Label(frame, text=label_text1, font=("Times New Roman", 20, "bold"), background='#D3D3D3', foreground='#333333')
label1.place(x = 150,y = 25)  
label2 = ttk.Label(frame, text=label_text2,font=("Times New Roman", 15, "bold"), background='#D3D3D3', foreground='#333333',image = img_pic)
label2.place(x = 200,y = 120)

button_font = ("Helvetica", 18, "bold")

# 自定义样式
root.style = ttk.Style(root)
root.style.theme_use('classic')  
root.style.configure('Green.TButton', font=button_font, background='#4CAF50', foreground='white', padding=20, borderwidth=0)
root.style.configure('Red.TButton', font=button_font, background='#F44336', foreground='white', padding=20, borderwidth=0)

start_button = ttk.Button(frame, text="开始体验", command=print_one, style='Green.TButton',state = 'normal')
#print(start_button['state'])
end_button = ttk.Button(frame, text="结束体验", command=print_five, style='Red.TButton',state = 'normal')
#print(end_button['state'])

start_button.place(x = 150,y = 250)
end_button.place(x = 450,y =250 )

root.mainloop()
