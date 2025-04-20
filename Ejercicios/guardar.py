import os

def guardar_sin_sobrescribir(profile, nombre, carpeta="Reportes"):
    os.makedirs(carpeta, exist_ok=True)
    base_path = os.path.join(carpeta, f"{nombre}.html")
    
    path = base_path
    count = 1
    while os.path.exists(path):
        path = os.path.join(carpeta, f"{nombre}_{count}.html")
        count += 1
    
    profile.to_file(path)
    print(f"Reporte guardado en: {path}")