# -*- coding: utf-8 -*-

"""
Script para procesar archivos de subtítulos (.srt) en una carpeta.

Este script solicita al usuario que seleccione una carpeta, busca todos los
archivos .srt, extrae y limpia el texto de diálogo de cada uno, y consolida
los resultados en un único archivo de texto llamado 'todos.txt' en la misma
carpeta.
"""

import os
import re
import tkinter as tk
from tkinter import filedialog

def extraer_texto_limpio_de_srt(ruta_archivo: str) -> str:
    """
    Lee un archivo .srt, limpia su contenido y extrae solo las líneas de diálogo.

    Args:
        ruta_archivo: La ruta completa al archivo .srt.

    Returns:
        Una única cadena de texto con todo el diálogo consolidado y limpio,
        o una cadena vacía si ocurre un error o no hay diálogo.
    """
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as f:
            contenido = f.read()
    except Exception as e:
        print(f"Error al leer el archivo {ruta_archivo}: {e}")
        return ""

    # 1. Eliminar contenido entre corchetes, como [Música] o [Aplausos]
    # Usamos re.DOTALL para que '.' también coincida con saltos de línea,
    # aunque para '[.*?]' no es estrictamente necesario, es una buena práctica.
    contenido_sin_corchetes = re.sub(r'\[.*?\]', '', contenido, flags=re.DOTALL)

    lineas_de_dialogo = []
    lineas = contenido_sin_corchetes.splitlines()

    for linea in lineas:
        linea_limpia = linea.strip()

        # 2. Ignorar líneas no deseadas:
        # - Números de secuencia (líneas que son solo dígitos)
        # - Marcas de tiempo (contienen '-->')
        # - Líneas en blanco
        if (linea_limpia.isdigit() or 
            '-->' in linea_limpia or 
            not linea_limpia):
            continue
        
        # Si la línea sobrevive a los filtros, es diálogo
        lineas_de_dialogo.append(linea_limpia)

    # 3. Consolidar todas las líneas de diálogo en un solo párrafo
    return ' '.join(lineas_de_dialogo)


def procesar_carpeta_srt():
    """
    Función principal que orquesta el proceso de selección, procesamiento y guardado.
    """
    # --- 1. Interacción con el Usuario (Selección de Carpeta) ---
    # Ocultar la ventana raíz de tkinter que no aporta valor
    root = tk.Tk()
    root.withdraw()

    print("Por favor, selecciona la carpeta que contiene los archivos .srt...")
    # Abrir el cuadro de diálogo para seleccionar una carpeta
    folder_path = filedialog.askdirectory(title="Selecciona la carpeta con archivos .srt")

    if not folder_path:
        print("Selección cancelada.")
        return # Finaliza el script de forma limpia

    print(f"Carpeta seleccionada: {folder_path}")

    # --- 4. Generación del Archivo de Salida ---
    output_filepath = os.path.join(folder_path, "todos.txt")

    try:
        # Abrir el archivo de salida en modo escritura con codificación UTF-8
        # El modo 'w' sobrescribirá el archivo si ya existe.
        with open(output_filepath, 'w', encoding='utf-8') as f_out:
            
            # --- 2. Búsqueda y Procesamiento de Archivos ---
            # Iterar sobre todos los archivos en el directorio seleccionado
            archivos_en_carpeta = sorted(os.listdir(folder_path)) # sorted para un orden predecible
            
            for filename in archivos_en_carpeta:
                # Procesar solo archivos que terminen en .srt (insensible a mayúsculas)
                if filename.lower().endswith('.srt'):
                    print(f"Procesando: {filename}...")
                    
                    full_file_path = os.path.join(folder_path, filename)

                    # --- 5. Formato del Contenido de Salida ---
                    # a. TÍTULO: Nombre del archivo sin extensión, en mayúsculas
                    titulo = os.path.splitext(filename)[0].upper()

                    # b. TEXTO: Llamada a la función de extracción y limpieza
                    texto_limpio = extraer_texto_limpio_de_srt(full_file_path)

                    # Solo escribir si se extrajo algún texto
                    if texto_limpio:
                        # Escribir en el archivo de salida con el formato especificado
                        f_out.write(f"{titulo}\n")
                        f_out.write(f"{texto_limpio}\n\n")

        # --- 6. Feedback al Usuario ---
        print("\n" + "="*50)
        print("¡Proceso completado exitosamente!")
        print(f"Archivo consolidado guardado en: {output_filepath}")
        print("="*50)

    except IOError as e:
        print(f"\nError de E/S al escribir en el archivo de salida: {e}")
    except Exception as e:
        print(f"\nOcurrió un error inesperado durante el procesamiento: {e}")


# --- Punto de Entrada del Script ---
if __name__ == "__main__":
    procesar_carpeta_srt()