import tkinter as tk
from Simulator import Type
import customtkinter
from tkinter import filedialog
import tkinter

customtkinter.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"

class App(customtkinter.CTk):

    WIDTH = 780
    HEIGHT = 520

    def __init__(self):
        super().__init__()
        self.resizable(0, 0)
        self.title("Autotype(Fixed By Richard)")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        # 设置窗口始终在最前面
        self.attributes("-topmost", True)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        # ============ created two frames ============

        # configured grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(
            master=self, width=180, corner_radius=0
        )
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # ============ frame_left ============

        # configure grid layout (1x11)
        self.frame_left.grid_rowconfigure(
            0, minsize=10
        )  # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(2, minsize=10)  # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(
            5, weight=1
        )  # empty row as spacing
        self.frame_left.grid_rowconfigure(
            8, minsize=20
        )  # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(
            11, minsize=10
        )  # empty row with minsize as spacing

        self.delay = customtkinter.CTkEntry(
            master=self.frame_left, width=140, placeholder_text="等多久开始输入（3秒）"
        )
        self.delay.grid(row=1, column=0, pady=10, padx=20)

        self.key_delay = customtkinter.CTkEntry(
            master=self.frame_left, width=140, placeholder_text="输入间隔（0.3秒）"
        )
        self.key_delay.grid(row=3, column=0, pady=10, padx=20)

        self.line_delay = customtkinter.CTkEntry(
            master=self.frame_left, width=140, placeholder_text="换行间隔（0.5秒）"
        )
        self.line_delay.grid(row=5, column=0, pady=10, padx=20)

        # Clear Input Button
        self.button_clear = customtkinter.CTkButton(
            master=self.frame_left,
            text="清除输入框",
            fg_color=("gray75", "gray30"),  # <- custom tuple-color
            command=self.clear_input,
            hover=True,
        )
        self.button_clear.grid(row=6, column=0, pady=10, padx=20)

        # Start Button
        self.button_2 = customtkinter.CTkButton(
            master=self.frame_left,
            text="开始",
            fg_color=("gray75", "gray30"),  # <- custom tuple-color
            command=self.start_typing,
            hover=True,
        )
        self.button_2.grid(row=7, column=0, pady=10, padx=20)

        self.label = customtkinter.CTkLabel(master=self.frame_left, text="")
        self.label.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

        self.switch_1 = customtkinter.CTkSwitch(
            master=self.frame_left, text="深色模式", command=self.change_mode
        )
        self.switch_1.grid(row=10, column=0, pady=10, padx=20, sticky="w")

        # ============ frame_right ============

        self.code = customtkinter.CTkTextbox(
            master=self.frame_right, width=520, height=400
        )
        self.code.grid(row=8, column=0, columnspan=2, pady=20, padx=20, sticky="we")

        # Bind right-click event to the custom paste function
        self.code.bind("<Button-3>", self.right_click_paste)

        self.label_2 = customtkinter.CTkLabel(
            master=self.frame_right,
            text="上方输入英文文本；右键粘贴。\n上方为空点击开始时可以选择txt文件进行输入；左侧留空为默认值。",
            font=("Roboto Medium", -16),
            anchor="center"
        )  # font name and size in px
        self.label_2.place(relx=0.5, rely=1.0, anchor="s")

    def open_file(self):
        filePath = filedialog.askopenfile()
        return filePath.name

    def start_typing(self):
        # Get the delay time, key delay time, line delay time, and code from the GUI inputs
        delay = self.delay.get()
        key_delay = self.key_delay.get()
        line_delay = self.line_delay.get()
        # code = self.code.textbox.get("1.0", tk.END)
        code = self.code.get("1.0", tk.END)

        # Check if key_delay and line_delay are provided
        if not key_delay:
            key_delay = 0.1  # Set a default value (e.g., 0.1 seconds) if not provided
        else:
            key_delay = float(key_delay)

        if not line_delay:
            line_delay = 0.1  # Set a default value (e.g., 0.1 seconds) if not provided
        else:
            line_delay = float(line_delay)

        # Continue with the logic based on code and delay as before
        if not code.strip() and delay:
            Type(path=self.open_file(), delay=int(delay), code=None, key_delay=key_delay, line_delay=line_delay)
            self.label.configure(text="完成")
        elif not code.strip() and not delay:
            Type(path=self.open_file(), delay=3, code=None, key_delay=key_delay, line_delay=line_delay)
            self.label.configure(text="完成")
        elif code.strip() and delay:
            Type(path=None, delay=int(delay), code=code, key_delay=key_delay, line_delay=line_delay)
            self.label.configure(text="完成")
        else:
            Type(path=None, delay=3, code=code, key_delay=key_delay, line_delay=line_delay)
            self.label.configure(text="完成")

    def clear_input(self):
        # Clear the text in the CTkTextbox
        self.code.delete("1.0", tk.END)

    def change_mode(self):
        if self.switch_1.get() == 1:
            customtkinter.set_appearance_mode("dark")
        else:
            customtkinter.set_appearance_mode("light")

    def on_closing(self, event=0):
        self.destroy()

    def start(self):
        self.mainloop()

    def right_click_paste(self, event):
        # Simulate a paste operation
        event.widget.event_generate("<<Paste>>")

if __name__ == "__main__":
    app = App()
    app.start()
