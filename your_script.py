import cv2
import os
from datetime import datetime
import win32evtlog
import time

def capture_photo(image_dir="security_logs"):
    """Capture a photo using the webcam."""
    os.makedirs(image_dir, exist_ok=True)
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    image_path = os.path.join(image_dir, f"capture_{timestamp}.png")
    
    cam = cv2.VideoCapture(0)
    ret, frame = cam.read()
    if ret:
        cv2.imwrite(image_path, frame)
        print(f"Photo saved at {image_path}")
    cam.release()
    cv2.destroyAllWindows()
    return image_path

def monitor_failed_logins(log_file="security_logs/failed_logins.log"):
    """Monitor Windows Event Logs dynamically for failed login attempts."""
    try:
        server = None
        log_type = "Security"
        event_id_to_watch = 4625
        image_dir = "security_logs"
        
        handle = win32evtlog.OpenEventLog(server, log_type)
        print("Monitoring failed login attempts (Event ID 4625)... Press Ctrl+C to exit.")
        
        while True:
            events = win32evtlog.ReadEventLog(
                handle,
                win32evtlog.EVENTLOG_SEQUENTIAL_READ | win32evtlog.EVENTLOG_BACKWARDS_READ,
                0,
            )
            for event in events:
                if event.EventID == event_id_to_watch:
                    timestamp = event.TimeGenerated.Format()
                    username = event.StringInserts[5] if len(event.StringInserts) > 5 else "Unknown"
                    print(f"Failed Login Attempt: {username} at {timestamp}")

                    photo_path = capture_photo(image_dir)
                    if photo_path:
                        with open(log_file, "a") as log:
                            log.write(f"Failed Login | Time: {timestamp} | User: {username} | Photo: {photo_path}\n")
                            print(f"Logged failed login: {username} at {timestamp}")
            time.sleep(1)

    except Exception as e:
        print(f"Error monitoring failed logins: {e}")
        with open("C:\\path\\to\\your_log\\error_log.txt", "a") as error_log:
            error_log.write(f"Error in monitor_failed_logins: {str(e)}\n")

    except KeyboardInterrupt:
        print("Monitoring stopped.")
    finally:
        win32evtlog.CloseEventLog(handle)

if __name__ == "__main__":
    monitor_failed_logins()
