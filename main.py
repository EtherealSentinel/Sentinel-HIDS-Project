from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from rich.console import Console
import time
import logging
import json
import time
import hashlib
import requests

observers = []

#işletim sissteminden kaynaklanan çok kısa süre içerisinden birden çok modified logunun kayıt altına alınmasını engellemek için eklendi.

last_modified_times = {}

# console object create

console = Console()

#hash file

file_hashes = {} 

# İzlemek istenilen dizin burada bulunan path kısmına yazılıyor /  The directory you want to watch is written in the path section here.

with open('config.json') as config_file:
    config = json.load(config_file)
    monitor_paths = config.get("monitor_paths", ["./test_directory"])

#webhook burada

def send_webhook_alert(message):
    try:
        with open('config.json', 'r') as f:
            config = json.load(f)
        webhook_url = config.get("webhook_url")
        if not webhook_url:
            return
        
        data = {
            "content": message
        }
        requests.post(webhook_url, json=data)
    except Exception as e:
        print(f"Failed to send webhook alert: {e}")


# Alert Logger

alert_logger = logging.getLogger('alertLogger')
alert_handler = logging.FileHandler('critical_alerts.log')
alert_formatter = logging.Formatter('%(asctime)s - %(message)s')
alert_handler.setFormatter(alert_formatter)
alert_logger.addHandler(alert_handler)
alert_logger.setLevel(logging.WARNING)

#Hash değerini hesaplayan fonksiyon / calculate hash 

def calculate_hash(file_path):
    try:
        sha256_hash = hashlib.sha256()
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except Exception as e:
        return None  # Dosya silinmiş olabilir vs.


# Bu kısımda logging kullanılarak hedef dizinde oluşan dedğişikler kayıt altına alınıyor /  The directory I want to watch is written in the path section here.

class IDSHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            file_hash = calculate_hash(event.src_path)
            file_hashes[event.src_path] = file_hash
            console.print(f"[green][+] File created:[/] {event.src_path}")
            logging.info(f"[CREATED] {event.src_path} | Hash: {file_hash}")

    def on_deleted(self, event):
        if not event.is_directory:
            console.print(f"[red][-] File deleted:[/] {event.src_path}")
            logging.warning(f"[-] File deleted: {event.src_path}")
            alert_logger.warning(f"[ALERT] File deleted: {event.src_path}")

    def on_modified(self, event):
        if not event.is_directory:
            now = time.time()
            last_time = last_modified_times.get(event.src_path, 0)
            if now - last_time > 2:
                new_hash = calculate_hash(event.src_path)
                old_hash = file_hashes.get(event.src_path)
                if old_hash != new_hash:
                    file_hashes[event.src_path] = new_hash
                    console.print(f"[yellow][!] File modified (hash changed):[/] {event.src_path}")
                    logging.warning(f"[MODIFIED] {event.src_path} | New Hash: {new_hash}")
                    alert_logger.warning(f"[ALERT] Hash changed for: {event.src_path}")
                else:
                    console.print(f"[yellow][!] File modified (no content change):[/] {event.src_path}")
                last_modified_times[event.src_path] = now

if __name__ == "__main__":
    logging.basicConfig(
        filename='alerts.log',
        level=logging.INFO,
        format='%(asctime)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

#event handler

for path in monitor_paths:
    event_handler = IDSHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    observers.append(observer)

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    for observer in observers:
        observer.stop()
    for observer in observers:
        observer.join()