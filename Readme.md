# Proyecto OCR con Google Cloud Vision

## Requisitos
- Python 3.10+
- Entorno virtual (`venv`)
- Credenciales de Google Cloud Vision en formato `.json`

## Pasos para ejecutar
1. Clonar el repositorio.
2. Crear un entorno virtual:
   ```bash
   python -m venv venv
   
   venv\Scripts\activate 

   pip install google-cloud-vision
   
   pip install pillow

   set GOOGLE_APPLICATION_CREDENTIALS=Keys/tu-llave.json   

   python main.py


---

### 🔑 Nota importante
Por temas de seguridad, **la clave (archivo `.json`) de Google Cloud Vision no se incluye en este repositorio**.  
El docente deberá generar su propia clave desde la [Google Cloud Console](https://console.cloud.google.com/) y colocarla en una carpeta `Keys/` con el nombre que corresponda.  

### 📂 Carpeta Keys
Aquí es donde debe ir la clave `.json` generada en Google Cloud.

<img width="316" height="178" alt="Capeta Keys" src="https://github.com/user-attachments/assets/79c1caca-f70d-4d8f-8ea2-b7dcc8bab40b" />

### ⚙️ Proceso de ejecución
Ejemplo de cómo se ejecuta el script y procesa las facturas.

<img width="1078" height="793" alt="proceso" src="https://github.com/user-attachments/assets/a96d52a9-2114-4b19-8d4b-6e391ff660be" />

### ✅ Resultado final
Ejemplo de los resultados obtenidos después del OCR y validación.

<img width="683" height="476" alt="resultado" src="https://github.com/user-attachments/assets/171f3548-f5fd-40af-849a-33e90b52da59" />
