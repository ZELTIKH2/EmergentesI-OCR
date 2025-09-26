import os
import re
import csv
from google.cloud import vision

def limpiar_numeros(texto):
   
    numeros = re.findall(r"\d{1,3}(?:\s\d{3})*(?:[.,]\d+)?", texto)
    
    return [float(n.replace(" ", "").replace(",", ".")) for n in numeros]

def validar_factura(image_path, client):
    with open(image_path, "rb") as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations

    if not texts:
        return (image_path, None, None, None, "❌ Sin texto")

   
    texto = texts[0].description
    numeros = limpiar_numeros(texto)

    if len(numeros) < 3:
        return (image_path, None, None, None, "❌ Datos incompletos")

    
    net, vat, total = numeros[-3:]
    estado = "✅ Correcto" if abs((net + vat) - total) < 0.01 else "❌ Error"
    return (image_path, net, vat, total, estado)

def procesar_lote(carpeta, salida_csv="resultados.csv", guardar_csv=False):
    client = vision.ImageAnnotatorClient()
    resultados = []

    for archivo in os.listdir(carpeta):
        if archivo.lower().endswith((".jpg", ".png", ".jpeg")):
            ruta = os.path.join(carpeta, archivo)
            print(f"\nProcesando {ruta}...")
            resultado = validar_factura(ruta, client)
            resultados.append(resultado)

    
    print("\n=== RESULTADOS DEL LOTE ===")
    for factura, net, vat, total, estado in resultados:
        print(f"📄 {factura} → Net={net}, VAT={vat}, Total={total} → {estado}")

    
    if guardar_csv:
        with open(salida_csv, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Factura", "Net worth", "VAT", "Total", "Estado"])
            writer.writerows(resultados)
        print(f"\n📂 Resultados guardados en {salida_csv}")



procesar_lote("Images/batch1_1")
