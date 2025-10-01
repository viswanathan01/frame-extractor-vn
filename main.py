import cv2
import os

def extract_frames(video_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    cap = cv2.VideoCapture(video_path)

    frame_count = 0
    while True:
        ret, frame = cap.read()

        if not ret: 
            break

        frame_filename = os.path.join(output_folder, f"frame_{frame_count:04d}.jpg")
        cv2.imwrite(frame_filename, frame)

        print(f"Saved {frame_filename}")
        frame_count += 1

    cap.release()
    print("✅ Frame extraction complete!")


video_file = "video source path"   
output_dir = "output folder where frames to be added."         
extract_frames(video_file, output_dir)
