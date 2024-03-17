from ultralytics import YOLO
import torch
import torchvision


# pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
# yolo predict model=runs/detect/train/weights/best.pt source='D:\Programs\object_detection.v2i.yolov8\test\images\IMG_20240304_140604_jpg.rf.129ed14a8c99b3029701670e82cba98c.jpg' imgsz=640

# Create a new YOLO model from scratch
model = YOLO('yolov8n.yaml')

# Load a pretrained YOLO model (recommended for training)
model = YOLO('yolov8n.pt')

# Train the model
results = model.train(data='D:\Programs\YoloV8\data.yaml', epochs=50, imgsz=640)

# Evaluate the model's performance on the validation set
results = model.val()

# Perform object detection on an image using the model
results = model('D:\Programs\object_detection.v2i.yolov8\IMG_20240304_135054_jpg.rf.7beaf759b321d66b69feb353a6d644f1.jpg')

# Export the model to ONNX format
success = model.export(format='onnx')