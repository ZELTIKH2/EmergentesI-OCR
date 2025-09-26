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

