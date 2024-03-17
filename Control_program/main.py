import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
import cv2
import serial
import time


def alg_1_btn_click():
    pass


def alg_2_btn_click():
    pass


def alg_3_btn_click():
    pass


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
        frame_select_alg = ttk.Frame(window, borderwidth=1, relief=SOLID, padding=[160, 8])
        select_alg_label = ttk.Label(frame_select_alg, text="Выберите алгоритм действий:")
        alg_1_btn = ttk.Button(frame_select_alg, text="Алгоритм 1", command=alg_1_btn_click)
        alg_2_btn = ttk.Button(frame_select_alg, text="Алгоритм 2", command=alg_2_btn_click)
        alg_3_btn = ttk.Button(frame_select_alg, text="Алгоритм 3", command=alg_3_btn_click)

        select_alg_label.pack(anchor="n", padx=3, pady=3, expand=True, ipadx=2, ipady=2)
        alg_1_btn.pack(anchor="n", padx=3, pady=3, expand=True, ipadx=2, ipady=2)
        alg_2_btn.pack(anchor="n", padx=3, pady=3, expand=True, ipadx=2, ipady=2)
        alg_3_btn.pack(anchor="n", padx=3, pady=3, expand=True, ipadx=2, ipady=2)
        frame_select_alg.pack(anchor="w", padx=5, pady=5)

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
