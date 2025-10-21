"""
Main application for Smart Parking System
"""

import cv2
import time
import threading
from car_detector import CarDetector
from parking_manager import ParkingManager
from web_dashboard import update_web_data
import config

def main():
    print("🚗 Starting Smart Parking System...")
    
    # Инициализация компонентов
    car_detector = CarDetector(confidence_threshold=config.DETECTION_CONFIDENCE)
    parking_manager = ParkingManager(config.PARKING_SPOTS)
    
    # Запуск веб-сервера в отдельном потоке
    from web_dashboard import app
    web_thread = threading.Thread(target=lambda: app.run(
        host=config.WEB_HOST, 
        port=config.WEB_PORT, 
        debug=config.DEBUG_MODE, 
        use_reloader=False
    ))
    web_thread.daemon = True
    web_thread.start()
    print("🌐 Web dashboard started on http://{}:{}".format(config.WEB_HOST, config.WEB_PORT))
    
    # Инициализация видео потока
    if config.USE_WEBCAM:
        cap = cv2.VideoCapture(0)  # Веб-камера
    else:
        cap = cv2.VideoCapture(config.VIDEO_SOURCE)
    
    if not cap.isOpened():
        print("❌ Error: Could not open video source")
        return
    
    print("✅ System initialized successfully")
    print("Press 'q' to quit")
    
    try:
        while True:
            # Чтение кадра
            ret, frame = cap.read()
            if not ret:
                print("❌ Error: Could not read frame")
                break
            
            # Детекция автомобилей
            cars = car_detector.detect_cars(frame)
            
            # Определение статуса парковочных мест
            parking_status = parking_manager.get_parking_status(cars)
            statistics = parking_manager.get_statistics()
            
            # Обновление веб-интерфейса
            update_web_data(parking_status, statistics)
            
            # Визуализация (для отладки)
            frame_with_detections = car_detector.draw_detections(frame.copy(), cars)
            
            # Отображение
            cv2.imshow('Smart Parking System', frame_with_detections)
            
            # Выход по нажатию 'q'
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
                
            time.sleep(config.UPDATE_INTERVAL)
            
    except KeyboardInterrupt:
        print("\n🛑 Shutting down...")
    
    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
