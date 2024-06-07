import cv2
from ultralytics import YOLO
import re


# Load the YOLOv8 model
model = YOLO('D://University//3_Дипломная работа//programs//control_program_py//best_s.pt')

cap = cv2.VideoCapture(0)

found_substring = ""
objects_classes = ['obj_1_blue', 'obj_1_green', 'obj_1_red', 'obj_1_yellow', 'obj_2_blue', 'obj_2_green', 'obj_2_red', 'obj_2_yellow', 'obj_3_blue', 'obj_3_green', 'obj_3_red', 'obj_3_yellow']

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        # Run YOLOv8 inference on the frame
        results = model(frame)

        print(results)

        for r in results:
            pattern = r"tensor\(\[[\d., ]+\], device='cuda:\d+'\)"
            objects_info = re.search(pattern, str(r.boxes))

            if objects_info:
                found_substring = objects_info.group()
                print("Найденная подстрока:", found_substring)
            else:
                print("Подстрока не найдена в выводе")

        if "0." in found_substring or "4." in found_substring or "8." in found_substring:
            print("blue")

        if "1." in found_substring or "5." in found_substring or "9." in found_substring:
            print("green")

        if "2." in found_substring or "6." in found_substring or "10." in found_substring:
            print("red")

        if "3." in found_substring or "7." in found_substring or "11." in found_substring:
            print("yellow")

        # Visualize the results on the frame
        annotated_frame = results[0].plot()

        # Display the annotated frame
        cv2.imshow("YOLOv8 Inference", annotated_frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()


