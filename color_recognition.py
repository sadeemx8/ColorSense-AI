import cv2
import numpy as np

def detect_color(frame, hsv, lower, upper, color_name, box_color):
    mask = cv2.inRange(hsv, lower, upper)

    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    contours, _ = cv2.findContours(
        mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    for contour in contours:
        area = cv2.contourArea(contour)

        if area > 800:
            x, y, w, h = cv2.boundingRect(contour)

            cv2.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                box_color,
                3
            )

            cv2.putText(
                frame,
                color_name,
                (x, max(y - 10, 25)),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                box_color,
                2
            )

    return mask


camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Error: Camera could not be opened.")
    raise SystemExit

while True:
    success, frame = camera.read()

    if not success:
        print("Error: Frame could not be read.")
        break

    frame = cv2.flip(frame, 1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    blue_mask = detect_color(
        frame,
        hsv,
        np.array([100, 120, 50]),
        np.array([140, 255, 255]),
        "Blue",
        (255, 0, 0)
    )

    green_mask = detect_color(
        frame,
        hsv,
        np.array([35, 70, 50]),
        np.array([85, 255, 255]),
        "Green",
        (0, 255, 0)
    )

    yellow_mask = detect_color(
        frame,
        hsv,
        np.array([20, 100, 100]),
        np.array([35, 255, 255]),
        "Yellow",
        (0, 255, 255)
    )

    red_mask_1 = cv2.inRange(
        hsv,
        np.array([0, 120, 70]),
        np.array([10, 255, 255])
    )

    red_mask_2 = cv2.inRange(
        hsv,
        np.array([170, 120, 70]),
        np.array([179, 255, 255])
    )

    red_mask = red_mask_1 | red_mask_2

    kernel = np.ones((5, 5), np.uint8)
    red_mask = cv2.morphologyEx(red_mask, cv2.MORPH_OPEN, kernel)
    red_mask = cv2.morphologyEx(red_mask, cv2.MORPH_CLOSE, kernel)

    red_contours, _ = cv2.findContours(
        red_mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    for contour in red_contours:
        area = cv2.contourArea(contour)

        if area > 800:
            x, y, w, h = cv2.boundingRect(contour)

            cv2.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                (0, 0, 255),
                3
            )

            cv2.putText(
                frame,
                "Red",
                (x, max(y - 10, 25)),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 0, 255),
                2
            )

    combined_mask = blue_mask | green_mask | yellow_mask | red_mask

    cv2.putText(
        frame,
        "Press Q to Exit",
        (15, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2
    )

    cv2.imshow("OpenCV Color Recognition", frame)
    cv2.imshow("Detected Colors Mask", combined_mask)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()