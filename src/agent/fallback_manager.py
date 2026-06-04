import csv
import os
from datetime import datetime

CSV_LOG_FILE = "telemetry_fallback.csv"

def log_fallback_event(event_type, status):
    file_exists = os.path.isfile(CSV_LOG_FILE)
    try:
        with open(CSV_LOG_FILE, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(["Timestamp", "Equipo", "Tipo_Evento", "Estado"])
            
            pc_name = os.environ.get('COMPUTERNAME', 'PC_Desconocido')
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            writer.writerow([timestamp, pc_name, event_type, status])
            print(f"[FALLBACK] Evento guardado localmente: {event_type} - {status}")
            
    except Exception as e:
        print(f"[ERROR CRÍTICO] Fallo al escribir en CSV local: {e}")