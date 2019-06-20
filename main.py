from camera import VideoCam

SKIPFRAME = 8
url = 0
v1 = VideoCam(url)
v1.check_camera(v1.cap)
ct = 0
while True:
    ct += 1
    try:
        ret = v1.cap.grab()
        if ct % SKIPFRAME == 0:  # skip some frames
            ret, frame = v1.get_frame()
            if not ret:
                v1.restart_capture(v1.cap)
                v1.check_camera(v1.cap)
                continue

            # frame HERE
            v1.show_frame(frame, 'frame')
    except KeyboardInterrupt:
        v1.close_cam()
        exit(0)