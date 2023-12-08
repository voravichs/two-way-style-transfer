import cv2
import os
import numpy as np

def stitch_video_from_image_frames(img_folder, video_name, frame_size=None, fps=30, img_ext='.jpg'):
    video_path = os.path.join(image_folder, video_name)

    images = [img for img in os.listdir(img_folder) if img.endswith(img_ext)]
    images.sort()

    if frame_size is None:
        # Get frame size from the first image (assume all have same resolution)
        img = cv2.imread(os.path.join(img_folder, images[0]))
        H, W, _ = img.shape
        frame_size = (H, W)

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video = cv2.VideoWriter(video_path, fourcc, fps, frame_size)

    for img in images:
        img_path = os.path.join(img_folder, img)
        frame = cv2.imread(img_path)
        frame = cv2.resize(frame, frame_size)
        video.write(frame)

    video.release()
    return video_path

# Set the path to the directory containing your images
image_folder = 'videos\complex_square_frames'
video_name = 'output_video.mp4'

stitch_video_from_image_frames(image_folder, video_name, fps=60)