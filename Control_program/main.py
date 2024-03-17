import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
import cv2
import serial
import time


class App:
    def __init__(self, window, title, size):
        super().__init__()

        # Установка параметров окна
        self.photo = None
        self.window = window
        self.window.title(title)
        self.window.geometry(f'{size[0]}x{size[1]}')
        self.window.minsize(size[0], size[1])
        self.window.maxsize(size[0], size[1])

        # Создание рамки для панели с выбором алгоритма
        self.frame_select_alg = ttk.Frame(window, borderwidth=1, relief=SOLID, padding=[160, 8])
        self.select_alg_label = ttk.Label(self.frame_select_alg, text="Выберите алгоритм действий:")
        self.alg_1_btn = ttk.Button(self.frame_select_alg, text="Алгоритм 1", command=self.alg_1_btn_click)
        self.alg_2_btn = ttk.Button(self.frame_select_alg, text="Алгоритм 2", command=self.alg_2_btn_click)
        self.alg_3_btn = ttk.Button(self.frame_select_alg, text="Алгоритм 3", command=self.alg_3_btn_click)

        self.select_alg_label.pack(anchor="n", padx=3, pady=3, expand=True, ipadx=2, ipady=2)
        self.alg_1_btn.pack(anchor="n", padx=3, pady=3, expand=True, ipadx=2, ipady=2)
        self.alg_2_btn.pack(anchor="n", padx=3, pady=3, expand=True, ipadx=2, ipady=2)
        self.alg_3_btn.pack(anchor="n", padx=3, pady=3, expand=True, ipadx=2, ipady=2)
        self.frame_select_alg.pack(anchor="w", padx=5, pady=5)

        # Схематичное изображение алгоритмов действий
        self.alg_1_img = ImageTk.PhotoImage(Image.open("alg_img/alg_1.png"))
        self.alg_1_label = Label()
        self.alg_1_label.place(x=3, y=160)
        self.alg_2_img = ImageTk.PhotoImage(Image.open("alg_img/alg_2.png"))
        self.alg_2_label = Label()
        self.alg_2_label.place(x=3, y=160)
        self.alg_3_img = ImageTk.PhotoImage(Image.open("alg_img/alg_3.png"))
        self.alg_3_label = Label()
        self.alg_3_label.place(x=3, y=160)

        # Установка параметров для захвата видео с веб-камеры
        self.video_source = 0
        self.vid = cv2.VideoCapture(self.video_source)
        self.vid.set(cv2.CAP_PROP_FPS, 24)  # Частота кадров

        self.canvas = tk.Canvas(window, width=self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)-1,
                                height=self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.canvas.place(x=520, y=5)

        self.delay = 10
        self.update_video()

        self.window.mainloop()

    def update_video(self):
        ret, frame = self.vid.read()
        if ret:
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)

        self.window.after(self.delay, self.update_video)

    # функции для выбора алгоритма дейсвий и показа его схематичного изображения
    def alg_1_btn_click(self):
        self.alg_2_label.config(image="")
        self.alg_3_label.config(image="")
        self.alg_1_label.config(image=self.alg_1_img)

    def alg_2_btn_click(self):
        self.alg_1_label.config(image="")
        self.alg_3_label.config(image="")
        self.alg_2_label.config(image=self.alg_2_img)

    def alg_3_btn_click(self):
        self.alg_1_label.config(image="")
        self.alg_2_label.config(image="")
        self.alg_3_label.config(image=self.alg_3_img)

    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()


# ser = serial.Serial('COM3', 9600, timeout=1)
# print(ser.isOpen())

# time.sleep(8)
# ser.write(b'position_1\n')
# time.sleep(8)
# ser.write(b'position_2\n')

root = tk.Tk()
App(root, 'Robot control application', (1170, 500))

