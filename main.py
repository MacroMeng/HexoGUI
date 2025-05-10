import os
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
from tkinter.filedialog import *
import subprocess
import threading as thr

import sv_ttk
import darkdetect as darkd


def no_hexo_proj_tip():
    console_error("当前目录下似乎没有Hexo项目。请在切换到一个可用的Hexo项目目录。")
    showerror("没有Hexo项目",
              "当前目录下似乎没有Hexo项目。请在打开时选择可用的Hexo项目目录。",
              parent=root,
              detail="你可以在Hexo官方网站(Hexo.io)找到关于“创建Hexo项目”的教程。")


def ask_work_dir():
    try:
        fn = askdirectory(title="选择Hexo项目目录", initialdir=".")
        if not fn:
            console_error("没有选择目录。将以HexoGUI所在目录作为Hexo项目目录。")
            showerror("没有选择目录", "您没有选择任何目录。将以HexoGUI所在目录作为Hexo项目目录。")
            fn = "."
        os.chdir(fn)
    except OSError as exc:
        console_error(f"无法打开目录: {exc}")
        showerror("无效文件夹", "您没有提供一个有效的文件夹。将以HexoGUI所在目录作为Hexo项目目录。")
    finally:
        console_info(f"已切换到Hexo项目目录: {os.getcwd()}")


def console_info(text):
    console["state"] = "normal"
    console.insert(END, text + "\n")
    console.see(END)
    console["state"] = "disabled"


def console_error(text):
    console["state"] = "normal"
    console.insert(END, text + "\n", "strong")
    console.see(END)
    console["state"] = "disabled"


def hexo_g():
    runner = subprocess.run(["cmd", "/r", "hexo", "g"], capture_output=True, text=True)
    output = runner.stdout
    if output.startswith("Usage:"):
        no_hexo_proj_tip()
        return
    elif runner.returncode == 0:
        console_info("[生成成功]" + output)
    else:
        console_error("[生成失败]" + output)
        return


def hexo_d():
    runner = subprocess.run(["cmd", "/r", "hexo", "d"], capture_output=True, text=True)
    output = runner.stdout
    if output.startswith("Usage:"):
        no_hexo_proj_tip()
        return
    else:
        console_info("[部署操作完成]" + output)


def hexo_g_d():
    hexo_g()
    hexo_d()


def hexo_s():
    thr.Thread(target=lambda: showinfo("本地服务器正在启动",
                                       "Hexo本地服务器正在启动，"
                                       "待命令行窗口打开后你就可以在浏览器中访问http://localhost:4000预览你的网站。",
                                       detail="你可以通过在打开的命令行窗口中按下Ctrl+C来停止本地服务器。\n"
                                              "如果无法打开该网址，或是命令行窗口一闪而过或根本不显示，请检查你的网络设置。",
                                       parent=root)).start()
    thr.Thread(target=lambda: os.system("start hexo s")).start()


def hexo_clean():
    runner = subprocess.run(["cmd", "/r", "hexo", "clean"], capture_output=True, text=True)
    output = runner.stdout
    if output.startswith("Usage:"):
        no_hexo_proj_tip()
        return
    elif runner.returncode == 0:
        console_info("[缓存清除成功]" + output)
    else:
        console_error("[缓存清除失败]" + output)


# Tk配置与常量
root = Tk()
VERSION = "v1.0.5"
root.title(f"HexoGUI by MacrosMeng {VERSION}")
root.geometry("400x500")
root.resizable(False, False)

# 控件配置
title = Label     (root, text="HexoGUI", font=("Verdana", 30, "bold"))
subtitle = Label  (root,
                   text=f"来自MacrosMeng的适用于Hexo的GUI管理工具。版本: {VERSION}",
                   font=("Microsoft YaHei UI", 10, "normal"))
controls = Frame  (root)
console = Text    (root, width=50, height=20, font=("Courier New", 10))
console.tag_config("strong", background="#ffcccc", foreground="#ff1111", font=("Courier New", 10, "bold"))
console["state"] = "disabled"
title.pack   (padx=5, pady=(5, 0))
subtitle.pack(padx=5, pady=0)
controls.pack(padx=5, pady=0, expand=True, fill="both")
console.pack (padx=5, pady=5, expand=True, fill="both")
generate = Button   (controls, text="💥生成💥",           width=20, command=hexo_g)
deploy = Button     (controls, text="🖥部署🖥",            width=20, command=hexo_d)
preview = Button    (controls, text="📰本地服务器预览📰‍", width=20, command=hexo_s)
clean = Button      (controls, text="🧹清除缓存🧹",       width=20, command=hexo_clean)
gen_deploy = Button (controls, text="✅生成并部署✅",     width=40, command=hexo_g_d)
change_dir = Button (controls, text="📁切换目录📁",       width=20, command=ask_work_dir)
exit_button = Button(controls, text="❌退出❌",           width=20, command=root.quit)
generate.grid   (row=0, column=0, columnspan=1, sticky=N + W + E, ipadx=5, ipady=5)
deploy.grid     (row=0, column=1, columnspan=1, sticky=N + W + E, ipadx=5, ipady=5)
preview.grid    (row=1, column=0, columnspan=1, sticky=N + W + E, ipadx=5, ipady=5)
clean.grid      (row=1, column=1, columnspan=1, sticky=N + W + E, ipadx=5, ipady=5)
gen_deploy.grid (row=2, column=0, columnspan=2, sticky=N + W + E, ipadx=5, ipady=5)
change_dir.grid (row=3, column=0, columnspan=1, sticky=N + W + E, ipadx=5, ipady=5)
exit_button.grid(row=3, column=1, columnspan=1, sticky=N + W + E, ipadx=5, ipady=5)

# 启动时的欢迎信息
sv_ttk.set_theme(darkd.theme())
console_info("HexoGUI已启动，这里将会显示Hexo的命令行输出与HexoGUI的日志信息。\n")
showinfo("欢迎使用HexoGUI",
         "HexoGUI是一个适用于Hexo的GUI管理工具。你可以在这里完成Hexo的一些常用操作。\n"
         "接下来，请在文件夹选择窗口中选中你的Hexo项目目录。",
         parent=root)
ask_work_dir()


root.mainloop()
