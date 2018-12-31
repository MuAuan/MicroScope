from time import sleep
import cv2

def cv_fourcc(c1, c2, c3, c4):
        return (ord(c1) & 255) + ((ord(c2) & 255) << 8) + \
            ((ord(c3) & 255) << 16) + ((ord(c4) & 255) << 24)

def main():
    OUT_FILE_NAME = "kenbikyo_video.mp4"
    FRAME_RATE=30
    w=640 #1280
    h=480 #960
    out = cv2.VideoWriter(OUT_FILE_NAME, \
              cv_fourcc('M', 'P', '4', 'V'), \
              FRAME_RATE, \
              (w, h), \
              True)
    cap = cv2.VideoCapture(1)
    is_video = 'False'
    s=0.1
    j=0
    timer = cv2.getTickCount()
    while True:
        ret, frame = cap.read()
        #sleep(s)
        fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);
        timer = cv2.getTickCount()
        # Display FPS on frame
        cv2.putText(frame, "FPS : " + str(int(1000*fps)), (100,50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2);
        cv2.putText(frame, "time : " + str(int((j-1)*s)) + " s", (400,50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2);
        #print(int(j*s),is_video)
        #j += 1
        cv2.imshow('test',frame)
        
        key = cv2.waitKey(int(s*1000))&0xff
        if key == ord('q'):   #113
            #cv2.destroyAllWindows()
            break
        elif key == ord('p'):
            s=60
            is_video = "True"
        elif key == ord('s'):
            s=0.1
            is_video = "False"    
        
        if is_video=="True":
            img_dst = cv2.resize(frame, (int(w), h))   #1280x960
            out.write(img_dst)
            print(int(j*s),is_video)
            j += 1

if __name__ == '__main__':
    main()
