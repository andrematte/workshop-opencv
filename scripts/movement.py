import cv2

# Open the default camera
cap = cv2.VideoCapture(1)

ret, frame1 = cap.read()
ret, frame2 = cap.read()

while cap.isOpened():
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (15, 15), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(
        thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
    )

    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)

        if cv2.contourArea(contour) < 7500:
            continue
        cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(
            frame1,
            "Movimento Detectado!!!!",
            (30, 80),
            cv2.FONT_HERSHEY_SIMPLEX,
            3,
            (0, 0, 255),
            4,
        )
    # cv2.drawContours(frame1, contours, -1, (0, 0, 255), 10)

    image = cv2.resize(frame1, (1280, 720))
    cv2.imshow("feed", frame1)
    frame1 = frame2
    ret, frame2 = cap.read()

    # Wait for the user to press 'q' key to exit
    if cv2.waitKey(40) == ord("q"):
        break

cv2.destroyAllWindows()
cap.release()
cap.release()
