from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from rich.console import Console
import time
import logging
import json
import time


#işletim sissteminden kaynaklanan çok kısa süre içerisinden birden çok modified logunun kayıt altına alınmasını engellemek için eklendi

last_modified_times = {}

# console object create

console = Console()

# Bu kısımda logging kullanılarak hedef dizinde oluşan dedğişikler kayıt altına alınıyor /  The directory I want to watch is written in the path section here.

class IDSHandler(FileSystemEventHandler):
    def on_created(self, event):
        console.print(f"[green][+] File created:[/] {event.src_path}")
        logging.info(f"[CREATED] {event.src_path}")

    def on_deleted(self, event):
        console.print(f"[red][-] File deleted:[/] {event.src_path}")
        logging.warning(f"[DELETED] {event.src_path}")

    def on_modified(self, event):
        now = time.time()
        last_time = last_modified_times.get(event.src_path, 0)
        if now - last_time > 2:  # 2 saniyeden eskiyse logla
            console.print(f"[yellow][!] File modified:[/] {event.src_path}")
            logging.warning(f"[MODIFIED] {event.src_path}")
            last_modified_times[event.src_path] = now

if __name__ == "__main__":
    logging.basicConfig(
        filename='alerts.log',
        level=logging.INFO,
        format='%(asctime)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

# İzlemek istenilen dizin burada bulunan path kısmına yazılıyor /  The directory you want to watch is written in the path section here.

with open('config.json') as config_file:
    config = json.load(config_file)
    path = config.get("monitor_path", "./test_directory")

#event handler

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


