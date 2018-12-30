from time import sleep
import cv2

def cv_fourcc(c1, c2, c3, c4):
        return (ord(c1) & 255) + ((ord(c2) & 255) << 8) + \
            ((ord(c3) & 255) << 16) + ((ord(c4) & 255) << 24)

def main():
    OUT_FILE_NAME = "kenbikyo_video.mp4"
    FRAME_RATE=30
    w=200
    h=150
    out = cv2.VideoWriter(OUT_FILE_NAME, \
              cv_fourcc('M', 'P', '4', 'V'), \
              FRAME_RATE, \
              (w, h), \
              True)
    cap = cv2.VideoCapture(1)
    is_video = 'False'
    s=0.1
    while True:
        timer = cv2.getTickCount()
        ret, frame = cap.read()
        sleep(s)
        fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);
        # Display FPS on frame
        cv2.putText(frame, "FPS : " + str(int(1000*fps)), (100,50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2);
        cv2.imshow('test',frame)
        
        key = cv2.waitKey(1)&0xff
        
        if is_video=="True":
            img_dst = cv2.resize(frame, (int(200), 150))
            out.write(img_dst)
            print(is_video)
            
        if key == ord('q'):   #113
            #cv2.destroyAllWindows()
            break
        elif key == ord('p'):
            s=1
            is_video = "True"
        elif key == ord('s'):
            s=0.1
            is_video = "False"    

if __name__ == '__main__':
    main()
