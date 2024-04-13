import numpy as np
import cv2 as cv
from datetime import timedelta
from moviepy.editor import VideoFileClip
import os

SAVING_FRAMES_PER_SECOND = 10


def format_timedelta(td):
    result = str(td)
    try:
        result, ns = result.split(".")
    except ValueError:
        return result + ".00".replace(":", "-")

    ns = round(int(ns) / 10000)
    return f"{result}.{ns:02}".replace(":", "-")


def main(video_file):
    video_clip = VideoFileClip(video_file)
    filename, _ = os.path.splitext(video_file)

    if not os.path.isdir(filename):
        os.mkdir(filename)

    saving_frames_per_second = min(video_clip.fps, SAVING_FRAMES_PER_SECOND)
    step = 1 / video_clip.fps if saving_frames_per_second == 0 else 1 / saving_frames_per_second

    for current_duration in np.arange(0, video_clip.duration, step):
        frame_duration_formatted = format_timedelta(timedelta(seconds=current_duration)).replace(":", "-")
        frame_filename = os.path.join(filename, f"frame{frame_duration_formatted}.jpg")

        video_clip.save_frame(frame_filename, current_duration)


cap = cv.VideoCapture(0)
cap1 = cv.VideoCapture(1)
frameNr = 0
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('left_video.avi', fourcc, 20.0, (640, 480))
fourcc1 = cv.VideoWriter_fourcc(*'XVID')
out1 = cv.VideoWriter('right_video.avi', fourcc1, 20.0, (640, 480))

while cap.isOpened() and cap1.isOpened():
    ret, frame = cap.read()
    ret1, frame1 = cap1.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    out.write(frame)
    out1.write(frame1)
    cv.imshow('left', frame1)
    cv.imshow('right', frame)  
    if ret and ret1:
        cv.imwrite(f'C:/python/frame/frame_left_{frameNr}.jpg', frame)
        cv.imwrite(f'C:/python/frame/frame_right_{frameNr}.jpg', frame1)
    frameNr = frameNr+1
    if cv.waitKey(1) == ord('q'):
        break


# Release everything if job is finished
cap.release()
cap1.release()
out.release()
out1.release()
cv.destroyAllWindows()

left_video = 'left_video.avi'
right_video = 'right_video.avi'
main(left_video)
main(right_video)
