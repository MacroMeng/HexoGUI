from tkinter import *
from tkinter.ttk import *
import subprocess


def insert_to_console(text):
    console.insert(END, text)
    console.see(END)


def hexo_g():
    runner = subprocess.run(["hexo", "generate"], capture_output=True, text=True)
    output = runner.stdout
    if runner.returncode == 0:
        insert_to_console("[成功生成]")
        insert_to_console(output)
    else:
        pass


root = Tk()
VERSION = "v1.0.2"
root.title(f"HexoGUI by MacrosMeng {VERSION}")
root.geometry("400x350")
root.resizable(False, False)

title = Label(root, text="HexoGUI", font=("Verdana", 30, "bold"))
title.pack(padx=5, pady=(5, 0))
subtitle = Label(root, text=f"适用于Hexo的GUI管理工具。版本: {VERSION}", font=("Microsoft YaHei UI", 10, "normal"))
subtitle.pack(padx=5, pady=0)
controls = Frame(root)
controls.pack(padx=5, expand=True, fill="both")
generate = Button(controls, text="生成", width=25, command=hexo_g)
generate.grid(row=0, column=0, sticky=N+W+E, ipadx=5, ipady=5)
deploy = Button(controls, text="部署", width=25)
deploy.grid(row=0, column=1, sticky=N+W+E, ipadx=5, ipady=5)
gen_deploy = Button(controls, text="生成并部署", width=50)
gen_deploy.grid(row=1, column=0, columnspan=2, sticky=N+W+E, ipadx=5, ipady=5)
preview = Button(controls, text="本地预览", width=50)
preview.grid(row=2, column=0, columnspan=2, sticky=N+W+E, ipadx=5, ipady=5)
clean = Button(controls, text="清除缓存", width=50)
clean.grid(row=3, column=0, columnspan=2, sticky=N+W+E, ipadx=5, ipady=5)
console = Text(root, width=50, height=20, font=("Courier New", 12))
console.pack(padx=5, pady=5, expand=True, fill="both")
insert_to_console("HexoGUI已启动，这里将会显示Hexo的命令行输出。")


root.mainloop()
