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
        self.window = window
        self.window.title(title)
        self.window.geometry(f'{size[0]}x{size[1]}')
        self.window.minsize(size[0], size[1])
        self.window.maxsize(size[0], size[1])

        # Создание рамок для групп кнопок
        frame_movement1 = ttk.Frame(window, borderwidth=1, relief=SOLID, padding=[8, 8])
        frame_movement2 = ttk.Frame(window, borderwidth=1, relief=SOLID, padding=[33, 8])

        #
        movement_label1 = ttk.Label(frame_movement1, text="Перемещение и поворот")
        forward_btn = ttk.Button(frame_movement1, text="Вперед")
        back_btn = ttk.Button(frame_movement1, text="Назад")
        clockwise_btn = ttk.Button(frame_movement1, text="По часовой")
        counterclockwise_btn = ttk.Button(frame_movement1, text="Против часовой")

        #
        movement_label2 = ttk.Label(frame_movement2, text="Подъем и захват")
        up_btn = ttk.Button(frame_movement2, text="Вверх")
        down_btn = ttk.Button(frame_movement2, text="Вниз")
        open_btn = ttk.Button(frame_movement2, text="Открыть")
        close_btn = ttk.Button(frame_movement2, text="Закрыть")

        # Установка положения объектов
        movement_label1.pack(anchor="n")
        forward_btn.pack(side=TOP, padx=3, pady=3, expand=True, ipadx=2, ipady=2)
        back_btn.pack(side=BOTTOM, padx=3, pady=3, expand=True, ipadx=2, ipady=2)
        clockwise_btn.pack(side=RIGHT, padx=3, pady=3, expand=True, ipadx=15, ipady=2)
        counterclockwise_btn.pack(side=LEFT, padx=3, pady=3, expand=True, ipadx=2, ipady=2)
        frame_movement1.pack(anchor="ne", padx=5, pady=5)

        movement_label2.pack(anchor="n")
        up_btn.pack(side=TOP, padx=3, pady=3, expand=True, ipadx=2, ipady=2)
        down_btn.pack(side=BOTTOM, padx=3, pady=3, expand=True, ipadx=2, ipady=2)
        open_btn.pack(side=RIGHT, padx=3, pady=3, expand=True, ipadx=2, ipady=2)
        close_btn.pack(side=LEFT, padx=3, pady=3, expand=True, ipadx=2, ipady=2)
        frame_movement2.pack(anchor="ne", padx=5, pady=0)

        # Установка параметров для захвата видео с веб-камеры
        self.video_source = 0
        self.vid = cv2.VideoCapture(self.video_source)
        self.vid.set(cv2.CAP_PROP_FPS, 30)  # Частота кадров

        self.canvas = tk.Canvas(window, width=self.vid.get(cv2.CAP_PROP_FRAME_WIDTH) - 40,
                                height=self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.canvas.place(x=5, y=5)

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
App(root, 'Robot control application', (1280, 720))
