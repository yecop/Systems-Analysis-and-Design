import time
import psutil
import csv
import os
import requests
import ctypes
import tkinter as tk
from datetime import datetime


IDLE_THRESHOLD_MINUTES = 15
CPU_THRESHOLD_PERCENT = 20.0
NUDGE_TIMEOUT_SECONDS = 60
CSV_LOG_FILE = "telemetry_fallback.csv"
TELEGRAM_BOT_URL = "https://api.telegram.org/bot<TOKEN>/sendMessage"
CHAT_ID = "<CHAT_ID>"

class LASTINPUTINFO(ctypes.Structure):
    _fields_ = [
        ("cbSize", ctypes.c_uint),
        ("dwTime", ctypes.c_uint)
    ]

def get_idle_time_seconds():
    lii = LASTINPUTINFO()
    lii.cbSize = ctypes.sizeof(lii)
    if ctypes.windll.user32.GetLastInputInfo(ctypes.byref(lii)):
        millis = ctypes.windll.kernel32.GetTickCount() - lii.dwTime
        return millis / 1000.0
    return 0.0

def log_fallback_event(event_type, status):
    file_exists = os.path.isfile(CSV_LOG_FILE)
    try:
        with open(CSV_LOG_FILE, mode='a', newline='') as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(["Timestamp", "Equipo", "Tipo_Evento", "Estado"])
            pc_name = os.environ.get('COMPUTERNAME', 'PC_Desconocido')
            writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), pc_name, event_type, status])
    except Exception as e:
        print(f"Error escribiendo en CSV local: {e}")

def send_alert_telegram(message):
    try:
        data = {"chat_id": CHAT_ID, "text": message}
        response = requests.post(TELEGRAM_BOT_URL, json=data, timeout=5)
        response.raise_for_status()
    except requests.exceptions.RequestException:
        log_fallback_event("Intento_Alerta_Red", "Fallo_Conexion_Firewall")

def show_nudge_and_wait():
    root = tk.Tk()
    root.title("Aviso de Gestión de Energía")
    root.geometry("450x200")
    root.attributes("-topmost", True)

    user_canceled = [False]

    def cancel_action():
        user_canceled[0] = True
        root.destroy()

    lbl_title = tk.Label(root, text="Inactividad Detectada", font=("Segoe UI", 16, "bold"), fg="#d35400")
    lbl_title.pack(pady=10)

    lbl_timer = tk.Label(root, text=f"El equipo se suspenderá en {NUDGE_TIMEOUT_SECONDS} segundos...", font=("Segoe UI", 12))
    lbl_timer.pack(pady=10)

    btn_cancel = tk.Button(root, text="Estoy aquí (Cancelar)", font=("Segoe UI", 12, "bold"), 
                           bg="#2980b9", fg="white", command=cancel_action, padx=20, pady=5)
    btn_cancel.pack(pady=10)

    def countdown(time_left):
        if time_left > 0 and not user_canceled[0]:
            lbl_timer.config(text=f"El equipo se suspenderá en {time_left} segundos...")
            root.after(1000, countdown, time_left - 1)
        elif time_left <= 0:
            root.destroy()

    countdown(NUDGE_TIMEOUT_SECONDS)
    
    root.focus_force()
    root.mainloop()

    return user_canceled[0]

def suspend_os():
    pc_name = os.environ.get('COMPUTERNAME', 'PC_Desconocido')
    send_alert_telegram(f"Alerta: El equipo {pc_name} será suspendido por inactividad prolongada.")
    log_fallback_event("Suspension_OS", "Ejecutado")
    
    ctypes.windll.powrprof.SetSuspendState(False, True, False)

def autonomous_agent_loop():
    print(f"=== Agente Smart Campus Iniciado en {os.environ.get('COMPUTERNAME')} ===")
    log_fallback_event("Agente_Inicio", "OK")
    
    while True:
        try:
            idle_seconds = get_idle_time_seconds()
            
            if idle_seconds >= (IDLE_THRESHOLD_MINUTES * 60):
                cpu_usage = psutil.cpu_percent(interval=2)
                
                if cpu_usage < CPU_THRESHOLD_PERCENT:
                    canceled