import cv2
import time

# Подключение к IP-камере (замените URL на свой!)
# Обычно ссылка выглядит так: "rtsp://login:password@ip_address:port/path"
camera_url = "rtsp://admin:Charlie8969@192.168.46.173:554/Streaming/Channels/101"
cap = cv2.VideoCapture(camera_url)

previous_frame = None  # Здесь будем хранить предыдущий кадр

while True:
    # Читаем кадр с камеры
    ret, frame = cap.read()
    if not ret:
        print("Ошибка подключения к камере!")
        break

    # 1. Конвертируем в черно-белый (упростит обработку)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 2. Размытие чтобы убрать шумы
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    # Если это первый кадр - просто сохраняем
    if previous_frame is None:
        previous_frame = gray
        continue  # Переходим к следующему кадру

    # 3. Сравниваем текущий и предыдущий кадр
    delta = cv2.absdiff(previous_frame, gray)
    # 4. Делаем "черно-белую маску" где различия (25 - порог чувствительности)
    thresh = cv2.threshold(delta, 25, 255, cv2.THRESH_BINARY)[1]

    # 5. Считаем белые пиксели в маске
    white_pixels = thresh.sum()  # Чем больше число - тем больше движения

    # 6. Проверяем, превышает ли движение порог (настройте под свою камеру)
    if white_pixels > 100000:
        print("Движение обнаружено! Пикселей:", white_pixels)
        # Тут позже добавим отправку в Telegram

    # Обновляем предыдущий кадр
    previous_frame = gray
    # Пауза чтобы не нагружать процессор
    time.sleep(1)  # Проверяем каждый 1 секунду

# Когда цикл прерван, освобождаем камеру
cap.release()
print("Программа завершена")


