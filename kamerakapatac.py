import cv2

kameratur= input("Bilgisayarınızın türü leptop ise 0(sıfır)'ı tuşlayınız. Harici kameranız var ise 1(bir)'i tuşlayınız. 1 olmaz ise 2,3,4.. diğer sayıları deneyebilirsiniz...\n program ve kamera 'q' tuşuna basınca kapanacaktır. \n ==> ")
sayi= int(kameratur)
cam = cv2.VideoCapture(sayi)


if not cam.isOpened():
    print("kamera tanınmadı")
    exit()
    
while True:
    ret, frame = cam.read()

    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)


    if not ret:
        print("kameradan görüntü okunamıyor")
        break

    cv2.imshow("kamera",frame)
    
    if cv2.waitKey(1) == ord("q"):
        print("görüntü sonlandırıldı")
        break
cam.release()
cv2.destroyAllWindows()
