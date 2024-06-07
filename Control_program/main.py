import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import cv2
import serial
import time
from ultralytics import YOLO
import re
import threading


# Функции для отправки команд микроконтроллеру манипулятора для перемещению объектов по первому алгоритму
# Перемещение из красного сегмента в зону выгрузки
def move_from_red_segment():
    command = [b'open_claw\n', b'position_top_left\n', b'close_claw\n', b'up\n', b'home_position\n', b'position_end\n',
               b'open_claw\n', b'up\n', b'home_position\n']
    sleep = [2, 4, 2, 1, 3, 4, 2, 1, 3]

    for i in range(len(command)):
        ser.write(command[i])
        time.sleep(sleep[i])


# Перемещение из зеленого сегмента в зону выгрузки
def move_from_green_segment():
    command = [b'open_claw\n', b'position_down_right\n', b'close_claw\n', b'up\n', b'home_position\n', b'position_end\n',
               b'open_claw\n', b'up\n', b'home_position\n']
    sleep = [2, 4, 2, 1, 3, 4, 2, 1, 3]

    for i in range(len(command)):
        ser.write(command[i])
        time.sleep(sleep[i])


# Перемещение из синего сегмента в зону выгрузки
def move_from_blue_segment():
    command = [b'open_claw\n', b'position_top_right\n', b'close_claw\n', b'up\n', b'home_position\n', b'position_end\n',
               b'open_claw\n', b'up\n', b'home_position\n']
    sleep = [2, 4, 2, 1, 3, 4, 2, 1, 3]

    for i in range(len(command)):
        ser.write(command[i])
        time.sleep(sleep[i])


# Перемещение из желтого сегмента в зону выгрузки
def move_from_yellow_segment():
    command = [b'open_claw\n', b'position_down_left\n', b'close_claw\n', b'up\n', b'home_position\n', b'position_end\n',
               b'open_claw\n', b'up\n', b'home_position\n']
    sleep = [2, 4, 2, 1, 3, 4, 2, 1, 3]

    for i in range(len(command)):
        ser.write(command[i])
        time.sleep(sleep[i])


# Функция для отправки команд микроконтроллеру манипулятора для перемещения объектов по второму алгоритму
def algorithm_2():
    command = [b'open_claw\n', b'position_down_left\n', b'close_claw\n', b'up\n', b'position_end1\n', b'open_claw\n',
               b'up\n', b'home_position\n',

               b'position_top_left\n', b'close_claw\n', b'up\n', b'position_end2\n',
               b'open_claw\n', b'up\n', b'home_position\n',

               b'position_top_right\n', b'close_claw\n', b'up\n',
               b'position_end_3_top\n', b'position_end3\n', b'open_claw\n', b'up\n', b'home_position\n']

    sleep = [2, 4, 2, 2, 4, 2, 2, 3,
             4, 2, 2, 4, 2, 2, 3,
             4, 2, 2, 3, 2, 2, 2, 3]

    for i in range(len(command)):
        ser.write(command[i])
        time.sleep(sleep[i])


# Функция для отправки команд микроконтроллеру манипулятора для перемещения объектов по третьему алгоритму
def algorithm_3():
    command = [b'open_claw\n', b'position_top_left\n', b'close_claw\n', b'up\n', b'position_end\n', b'open_claw\n',
               b'up\n', b'home_position\n',

               b'position_down_right\n', b'close_claw\n', b'up\n', b'position_end_2_mid\n',
               b'open_claw\n', b'up\n', b'home_position\n',

               b'position_top_right\n', b'close_claw\n', b'up\n',
               b'position_end_3_top\n', b'open_claw\n', b'up\n', b'home_position\n']

    sleep = [2, 4, 2, 2, 4, 2, 2, 3,
             4, 2, 2, 4, 2, 2, 3,
             4, 2, 2, 4, 2, 2, 3]

    for i in range(len(command)):
        ser.write(command[i])
        time.sleep(sleep[i])


# Функция для отображения окна с описанием ошибки, при ее возникновении
def show_error(message):
    messagebox.showerror("Произошла ошибка!", message)


# Класс окна со стартовыми настройками
class StartSettings:
    def __init__(self, window, title, size):
        super().__init__()

        # Установка параметров окна
        self.window = window
        self.window.title(title)
        self.window.geometry(f'{size[0]}x{size[1]}')
        self.window.minsize(size[0], size[1])
        self.window.maxsize(size[0], size[1])

        # Переменные для обновленных значений
        self.com_port_new = ""
        self.baud_rate_new = ""
        self.video_source_new = ""

        # Списки с возможными вариантами параметров для каждой из настроек
        self.com_port_list = ["COM1", "COM2", "COM3", "COM4", "COM5", "COM6", "COM7", "COM8", "COM9"]
        self.baud_rate_list = ["2400", "9600", "19200", "38400",
                               "57600", "115200", "250000", "500000", "1000000"]
        self.video_source_list = ["0", "1", "2", "3", "4"]

        # Переменные, содержащие дефолтные значения параметров настроек
        self.com_port_list_var = StringVar(value=self.com_port_list[2])
        self.baud_rate_list_var = StringVar(value=self.baud_rate_list[1])
        self.video_source_list_var = StringVar(value=self.video_source_list[0])

        # Label и сombobox для выбора СОМ порта
        self.select_com_port_label = ttk.Label(self.window, text="Выберите COM порт: ")
        self.select_com_port_label.place(x=10, y=10)
        self.combobox_com_port = ttk.Combobox(textvariable=self.com_port_list_var, values=self.com_port_list,
                                              state="readonly")
        self.combobox_com_port.place(x=135, y=10)

        # Label и сombobox для выбора скорости передачи данных (Baud rate) микроконтроллеру манипулятора
        self.select_baud_rate_label = ttk.Label(self.window, text="Выберите Baud rate: ")
        self.select_baud_rate_label.place(x=10, y=50)
        self.combobox_baud_rate = ttk.Combobox(textvariable=self.baud_rate_list_var, values=self.baud_rate_list,
                                               state="readonly")
        self.combobox_baud_rate.place(x=135, y=50)

        # Label и сombobox для выбора id камеры
        self.select_video_source_label = ttk.Label(self.window, text="Выберите камеру: ")
        self.select_video_source_label.place(x=10, y=90)
        self.combobox_video_source = ttk.Combobox(textvariable=self.video_source_list_var,
                                                  values=self.video_source_list, state="readonly")
        self.combobox_video_source.place(x=135, y=90)

        # Кнопка сохранения настроек
        self.button = ttk.Button(window, text="Сохранить выбранные значения", command=self.get_selected_values, padding=3)
        self.button.place(x=70, y=130)
        self.text = ttk.Label(self.window, text="После нажатия кнопки сохранения данное окно закроется.")
        self.text.place(x=10, y=165)

        self.window.mainloop()

    # Функция для считывания выбранных настроек и установки новых значений в переменные
    def get_selected_values(self):
        global com_port
        global baud_rate
        global video_source

        self.com_port_new = str(self.com_port_list_var.get())
        self.baud_rate_new = str(self.baud_rate_list_var.get())
        self.video_source_new = int(self.video_source_list_var.get())

        com_port = self.com_port_new
        baud_rate = self.baud_rate_new
        video_source = self.video_source_new

        self.window.destroy()


# Класс с основным интерфейсом программы управления манипулятором
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

        # Подгрузка обученной модели YOLOv8s
        self.model = YOLO('best_s.pt')

        # Переменная для хранения найденной подстроки в выводе данных от нейросети
        self.found_substring = ""

        # self.objects_classes = ['obj_1_blue', 'obj_1_green', 'obj_1_red', 'obj_1_yellow', 'obj_2_blue', 'obj_2_green',
        #                         'obj_2_red', 'obj_2_yellow', 'obj_3_blue', 'obj_3_green', 'obj_3_red', 'obj_3_yellow']

        # Переменная для хранения номера алгоритма
        self.algorithm_number = 0

        # Выделение потока
        self.thread = threading.Thread()
        self.thread_was_started = 0

        # Создание рамки для панели с выбором алгоритма
        self.frame_select_alg = ttk.Frame(window, borderwidth=1, relief=SOLID, padding=[20, 8])
        self.frame_select_alg.pack(anchor="w", padx=5, pady=5)

        self.select_alg_label = ttk.Label(self.frame_select_alg, text="Выберите алгоритм действий:")
        self.select_alg_label.pack(anchor="n", padx=3, pady=3, expand=True, ipadx=2, ipady=2)

        # Кнопки выбора алгоритмов
        self.alg_1_btn = ttk.Button(self.frame_select_alg, text="Алгоритм 1", command=self.alg_1_btn_click)
        self.alg_2_btn = ttk.Button(self.frame_select_alg, text="Алгоритм 2", command=self.alg_2_btn_click)
        self.alg_3_btn = ttk.Button(self.frame_select_alg, text="Алгоритм 3", command=self.alg_3_btn_click)
        self.clear_alg = ttk.Button(self.frame_select_alg, text="Сбросить выбор алгоритма", command=self.clear_alg)
        self.alg_1_btn.pack(anchor="n", padx=3, pady=3, expand=True, ipadx=2, ipady=2)
        self.alg_2_btn.pack(anchor="n", padx=3, pady=3, expand=True, ipadx=2, ipady=2)
        self.alg_3_btn.pack(anchor="n", padx=3, pady=3, expand=True, ipadx=2, ipady=2)
        self.clear_alg.pack(anchor="n", padx=3, pady=3, expand=True, ipadx=2, ipady=2)

        # Схематичное изображение алгоритмов действий
        self.alg_1_img = ImageTk.PhotoImage(Image.open("alg_img/alg_1.png"))
        self.alg_1_label = Label()
        self.alg_1_label.place(x=3, y=200)
        self.alg_2_img = ImageTk.PhotoImage(Image.open("alg_img/alg_2.png"))
        self.alg_2_label = Label()
        self.alg_2_label.place(x=3, y=200)
        self.alg_3_img = ImageTk.PhotoImage(Image.open("alg_img/alg_3.png"))
        self.alg_3_label = Label()
        self.alg_3_label.place(x=3, y=200)

        # Рамка для отображения текстового описания алгоритмов
        self.frame_alg_description = ttk.Frame(window, borderwidth=1, relief=SOLID, padding=[30, 8], width=500, height=500)
        self.frame_alg_description.pack_propagate(False)
        self.frame_alg_description.configure(width=275, height=187)
        self.frame_alg_description.place(x=235, y=5)

        self.alg_description_label = ttk.Label(self.frame_alg_description, text="Описание выбранного алгоритма: ")
        self.alg_description_label.pack(anchor="n", padx=3, pady=3)

        self.alg_description_text = ttk.Label(self.frame_alg_description, text="Пустовато...\nВыберите алгоритм.")
        self.alg_description_text.pack(anchor="n", pady=10)

        # Установка параметров для захвата видео с веб-камеры
        self.delay = 20                                                 # задержка
        self.video_source = int(video_source)                           # id камеры
        self.vid = cv2.VideoCapture(self.video_source)                  # захват видео с камеры
        self.vid.set(cv2.CAP_PROP_FPS, 24)                        # частота кадров

        # Canvas для отображениея видео с камеры
        self.canvas = tk.Canvas(window, width=self.vid.get(cv2.CAP_PROP_FRAME_WIDTH) - 1,
                                height=self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.canvas.place(x=520, y=5)

        # Запуск функции для трансляции видео с камеры и обработки кадров с помощью YoloV8
        try:
            self.update_video()
        except CameraException as cam_ex:
            show_error(cam_ex)

        self.window.mainloop()

    # Функция для трансляции видео с камеры и обработки кадров с помощью YoloV8
    def update_video(self):
        # Захват кадра с камеры
        ret, frame = self.vid.read()
        # Если кадр успешно захвачен
        if ret:
            # Обработка кадра с помощью YoloV8 (минимальная точность 70%)
            results = self.model(frame, conf=0.7)

            # Поиск нужной подстроки с информацией об типо объекта и его положении на рабочей зоне
            for r in results:
                pattern = r"tensor\(\[[\d., ]+\], device='cuda:\d+'\)"
                objects_info = re.search(pattern, str(r.boxes))

                if objects_info:
                    self.found_substring = objects_info.group()
                    print("Найденная подстрока:", self.found_substring)
                else:
                    print("Подстрока не найдена в выводе")

            # Проверки на то, что поток, в котором работает одна из функций по перемещения, отработал
            # и можно заново запускать проверки на положение объектов
            if not self.algorithm_number == -1:
                if not self.thread.is_alive() and self.thread_was_started == 1:
                    self.algorithm_number = 1
                    self.thread_was_started = 0
                    self.found_substring = "---"

                if not self.thread.is_alive() and self.thread_was_started == 2:
                    self.algorithm_number = 2
                    self.thread_was_started = 0
                    self.found_substring = "---"

                if not self.thread.is_alive() and self.thread_was_started == 3:
                    self.algorithm_number = 3
                    self.thread_was_started = 0
                    self.found_substring = "---"

            # Проверки для алгоритма 1 на положение объектов
            if self.algorithm_number == 1:
                # Находится ли объект в синем сегменте?
                if ("tensor([0.], device='cuda:0')" == self.found_substring
                        or "tensor([4.], device='cuda:0')" == self.found_substring
                        or "tensor([8.], device='cuda:0')" == self.found_substring):

                    # Проверка на то, что старый поток не запущен
                    if not self.thread.is_alive() and self.thread_was_started == 0:
                        # Сброс номера алгоритма
                        self.algorithm_number = 0
                        # Запуск функции перемещения из синего сегмента в новом потоке
                        self.thread = threading.Thread(target=move_from_blue_segment)
                        self.thread.start()
                        if self.thread.is_alive():
                            self.thread_was_started = 1

                # Находится ли объект в зеленом сегменте?
                if ("tensor([1.], device='cuda:0')" == self.found_substring
                        or "tensor([5.], device='cuda:0')" == self.found_substring
                        or "tensor([9.], device='cuda:0')" == self.found_substring):

                    # Проверка на то, что старый поток не запущен
                    if not self.thread.is_alive() and self.thread_was_started == 0:
                        # Сброс номера алгоритма
                        self.algorithm_number = 0
                        # Запуск функции перемещения из зеленого сегмента в новом потоке
                        self.thread = threading.Thread(target=move_from_green_segment)
                        self.thread.start()
                        if self.thread.is_alive():
                            self.thread_was_started = 1

                # Находится ли объект в красном сегменте?
                if ("tensor([2.], device='cuda:0')" == self.found_substring
                        or "tensor([6.], device='cuda:0')" == self.found_substring
                        or "tensor([10.], device='cuda:0')" == self.found_substring):

                    # Проверка на то, что старый поток не запущен
                    if not self.thread.is_alive() and self.thread_was_started == 0:
                        # Сброс номера алгоритма
                        self.algorithm_number = 0
                        # Запуск функции перемещения из красного сегмента в новом потоке
                        self.thread = threading.Thread(target=move_from_red_segment)
                        self.thread.start()
                        if self.thread.is_alive():
                            self.thread_was_started = 1

                # Находится ли объект в желтом сегменте?
                if ("tensor([3.], device='cuda:0')" == self.found_substring
                        or "tensor([7.], device='cuda:0')" == self.found_substring
                        or "tensor([11.], device='cuda:0')" == self.found_substring):

                    # Проверка на то, что старый поток не запущен
                    if not self.thread.is_alive() and self.thread_was_started == 0:
                        # Сброс номера алгоритма
                        self.algorithm_number = 0
                        self.found_substring = "---"
                        # Запуск функции перемещения из желтого сегмента в новом потоке
                        self.thread = threading.Thread(target=move_from_yellow_segment)
                        self.thread.start()
                        if self.thread.is_alive():
                            self.thread_was_started = 1

            # Проверки для алгоритма 2 на положение объектов
            if self.algorithm_number == 2:
                # 1 в желтом (3), 2 в красном (6), 3 в синем (8)
                if ("tensor([8., 6., 3.], device='cuda:0')" == self.found_substring
                        or "tensor([6., 8., 3.], device='cuda:0')" == self.found_substring
                        or "tensor([3., 6., 8.], device='cuda:0')" == self.found_substring
                        or "tensor([6., 3., 8.], device='cuda:0')" == self.found_substring
                        or "tensor([3., 8., 6.], device='cuda:0')" == self.found_substring
                        or "tensor([8., 3., 6.], device='cuda:0')" == self.found_substring):

                    # Проверка на то, что старый поток не запущен
                    if not self.thread.is_alive() and self.thread_was_started == 0:
                        # Сброс номера алгоритма
                        self.algorithm_number = 0
                        self.found_substring = "---"
                        # Запуск функции перемещения объектов по второму алгоритму в новом потоке
                        self.thread = threading.Thread(target=algorithm_2)
                        self.thread.start()
                        if self.thread.is_alive():
                            self.thread_was_started = 2

            # проверки для алгоритма 3 на положение объектов
            if self.algorithm_number == 3:
                # 1 в красном (2), 2 в зеленом (5), 3 в синем (8)
                if ("tensor([8., 5., 2.], device='cuda:0')" == self.found_substring
                        or "tensor([8., 2., 5.], device='cuda:0')" == self.found_substring
                        or "tensor([5., 8., 2.], device='cuda:0')" == self.found_substring
                        or "tensor([5., 2., 8.], device='cuda:0')" == self.found_substring
                        or "tensor([2., 8., 5.], device='cuda:0')" == self.found_substring
                        or "tensor([2., 5., 8.], device='cuda:0')" == self.found_substring):

                    # Проверка на то, что старый поток не запущен
                    if not self.thread.is_alive() and self.thread_was_started == 0:
                        # Сброс номера алгоритма
                        self.algorithm_number = 0
                        self.found_substring = "---"
                        # Запуск функции перемещения объектов по третьему алгоритму в новом потоке
                        self.thread = threading.Thread(target=algorithm_3)
                        self.thread.start()
                        if self.thread.is_alive():
                            self.thread_was_started = 3

            # Отображение обработанного кадра
            annotated_frame = results[0].plot()
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
        else:
            raise CameraException("Ошибка! Камера не найдена.\nПодключите камеру и перезапустите программу.")

        self.window.after(self.delay, self.update_video)

    # Выбор алгоритма действий, отображение его схематичного изображения и текстового описания
    # Алгоритм 1
    def alg_1_btn_click(self):
        self.alg_1_label.config(image=self.alg_1_img)
        self.alg_2_label.config(image="")
        self.alg_3_label.config(image="")
        self.alg_description_text.config(text="При появлении объекта в любой\nзоне – взять его и переместить "
                                              "в\nнеобходимое место.")
        self.algorithm_number = 1

    # Алгоритм 2
    def alg_2_btn_click(self):
        self.alg_1_label.config(image="")
        self.alg_2_label.config(image=self.alg_2_img)
        self.alg_3_label.config(image="")
        self.alg_description_text.config(text="Из заданного расположения\nобъектов по зонам произвести "
                                              "их\nперемещение в необходимое\nместо с расстановкой в\nопределенном "
                                              "порядке.")
        self.algorithm_number = 2

    # Алгоритм 3
    def alg_3_btn_click(self):
        self.alg_1_label.config(image="")
        self.alg_2_label.config(image="")
        self.alg_3_label.config(image=self.alg_3_img)
        self.alg_description_text.config(text="Из заданного расположения\nобъектов по зонам произвести "
                                              "их\nперемещение в свободную зону\nи расставить друг на друга "
                                              "в\nопределенном порядке.")
        self.algorithm_number = 3

    # Сброс выбора алгоритма
    def clear_alg(self):
        self.alg_1_label.config(image="")
        self.alg_2_label.config(image="")
        self.alg_3_label.config(image="")
        self.alg_description_text.config(text="Пустовато...\nВыберите алгоритм.")
        self.algorithm_number = -1

    # Освобождение захвата кадров с камеры при закрытии окна
    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()


# Пользовательский класс исключения при возникновении ошибки с камерой
class CameraException(Exception):
    def __init__(self, message="-пусто-"):
        self.message = message
        super().__init__(self.message)


# Стандартные значения номера порта, скорости передачи данных и id камеры
com_port = "COM3"
baud_rate = "9600"
video_source = "0"

if __name__ == "__main__":
    # Запуск стартового окна с настройками
    start_window = tk.Tk()
    StartSettings(start_window, 'Start settings', (350, 200))

    # Переменная, говорящая о наличии\отсутствии ошибки при подключении к микроконтроллеру манипулятора
    errors = False

    # Подключение к микроконтроллеру манипулятора
    try:
        ser = serial.Serial(com_port, int(baud_rate), timeout=1)
        ser.write(b'none\n')
    except serial.SerialException as ser_ex:
        show_error(ser_ex)
        errors = True

    # Запуск основной программы при успешном подключении микроконтроллера
    if not errors:
        root = tk.Tk()
        App(root, 'Robot control application', (1170, 540))

# pyinstaller --noconsole -n "Robot control app" main.py
