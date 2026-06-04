import os
import mysql.connector
from datetime import datetime

DB_HOST = "tu-host-mysql.nube.com"
DB_USER = "tu_usuario"
DB_PASS = "tu_contraseña"
DB_NAME = "smart_campus_db"

def sync_to_cloud_database(event_type, status):
    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASS,
            database=DB_NAME,
            connect_timeout=5
        )
        
        cursor = connection.cursor()
        
        pc_name = os.environ.get('COMPUTERNAME', 'PC_Desconocido')
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        query = """INSERT INTO telemetry_logs (timestamp, workstation_id, event_type, status) 
                   VALUES (%s, %s, %s, %s)"""
        values = (timestamp, pc_name, event_type, status)
        
        cursor.execute(query, values)
        connection.commit()
        
        print(f"[NUBE] Sincronización exitosa: {event_type}")
        return True
        
    except mysql.connector.Error as err:
        print(f"[ERROR RED] Fallo conexión a MySQL: {err}")
        raise Exception("Fallo de conexión a base de datos externa")
        
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()