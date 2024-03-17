import torch
import torchvision
import torchaudio
import os
import pandas as pd
os.environ["GIT_PYTHON_REFRESH"] = "quiet"
import git
import subprocess
from roboflow import Roboflow


rf = Roboflow(api_key="NnGA9CdLaYmdJPxH6MtB")
project = rf.workspace("vstu-peu9x").project("object_detection-kdaj6")
version = project.version(2)
dataset = version.download("yolov5")

# pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

# подгрузка yoloV5 и всех ее зависимостей
# cd yolov5
# pip3 install -qr requirements.txt # install dependencies
# pip3 install -q roboflow

# img: размер изображения, квадратный.
# batch: размер партии
# epochs: количество эпох
# data: файл данных YAML, содержащий информацию о наборе данных (путь к изображениям, меткам) (его загрузить в yolo/data)
# workers: количество процессорных рабочих
# cfg: Файл конфигурации модели архитектуры, Есть 4 варианта доступны: yolo5s.yaml, yolov5m.yaml, yolov5l.yaml, yolov5x.yaml.
# weights: Предварительно натренированные веса

file_path = "D:\\University\\3_Дипломная работа\\programs\\YoloV5_train\\yolov5\\train.py"
args = ["--img", "640", "--cfg", "yolov5m.yaml", "--batch", "1", "--epoch", "140", "--data", "data.yaml", "--weights", "yolov5m.pt", "--name", "result", "--device", "0"]
subprocess.call(["python", file_path] + args)

file_path = "D:\\University\\3_Дипломная работа\\programs\\YoloV5_train\\yolov5\\detect.py"
args = ["--weights", "D:\\University\\3_Дипломная работа\\programs\\YoloV5_train\\yolov5\\runs\\train\\result\\weights\\best.pt", "--conf", " 0.5", "--source",
        "D:\\object_detection.v2i.yolov5pytorch\\test\\images\\IMG_20240304_135054_jpg.rf.7beaf759b321d66b69feb353a6d644f1.jpg"]
subprocess.call(["python", file_path] + args)
