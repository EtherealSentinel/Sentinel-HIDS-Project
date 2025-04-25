from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import logging

# Bu kısımda logging kullanılarak hedef dizinde oluşan dedğişikler kayıt altına alınıyor /  The directory I want to watch is written in the path section here.

class IDSHandler(FileSystemEventHandler):
    def on_created(self, event):
        logging.info(f"[+] File created: {event.src_path}")

    def on_deleted(self, event):
        logging.warning(f"[-] File deleted: {event.src_path}")

    def on_modified(self, event):
        logging.warning(f"[!] File modified: {event.src_path}")

if __name__ == "__main__":
    logging.basicConfig(
        filename='alerts.log',
        level=logging.INFO,
        format='%(asctime)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

# İzlemek istediğim dizin burada bulunan path kısmına yazılıyor /  The directory I want to watch is written in the path section here.

    path = "./test_directory"
    event_handler = IDSHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

