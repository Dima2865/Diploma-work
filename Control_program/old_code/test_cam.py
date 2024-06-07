import cv2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, 30)  # Частота кадров
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 600)  # Ширина кадров в видеопотоке.
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)  # Высота кадров в видеопотоке.

while True:
    ret, img = cap.read()
    cv2.imshow("camera", img)
    if cv2.waitKey(10) == 27:  # Клавиша Esc
        break

cap.release()
cv2.destroyAllWindows()


# функция делающая фото и запускающая обрабтку его нейросетью
def take_photo(self):
    # захватываем кадр с веб камеры
    ret, frame = self.vid.read()

    if ret:
        self.photo = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))

        cv2.imwrite('photo.jpg', frame)
        print('Фото сохранено как photo.jpg')
    else:
        print('Не удалось захватить фото')

    self.vid.release()

    # обработка фото нейросетью
    command = "yolo predict model=runs/detect/train2/weights/best.pt source='obj_detect.v1i.yolov8/test/images/IMG_20240327_145633_jpg.rf.0891fc27d71bedc8953af7c2e19603af.jpg' imgsz=640"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    # print("Output: ", result.stdout)