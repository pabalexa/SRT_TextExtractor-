# SRT Text Extractor

[![Python Version](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> Script Python para limpiar y consolidar texto de archivos .srt. Extrae diálogos, elimina timestamps/corchetes, y une todo el contenido en un único todos.txt por carpeta. Ideal para análisis textual o creación de corpora de texto a partir de subtítulos

## 🌟 Características Principales

- **Interfaz Gráfica Sencilla**: Utiliza `tkinter` para mostrar un diálogo nativo de selección de carpeta, mejorando la experiencia de usuario.
- **Procesamiento por Lotes**: Explora automáticamente una carpeta y procesa todos los archivos de subtítulos (`.srt`, `.SRT`, etc.).
- **Limpieza Avanzada de Texto**:
  - Elimina los números de secuencia de los subtítulos.
  - Descarta las marcas de tiempo (ej: `00:02:16,612 --> 00:02:19,380`).
  - Elimina anotaciones no verbales encerradas en corchetes (ej: `[Música]` o `[Aplausos]`).
- **Consolidación Inteligente**: Une todas las líneas de diálogo de un archivo en un único párrafo continuo.
- **Salida Organizada**: Genera un único archivo `todos.txt` en la misma carpeta, con el contenido de cada archivo `.srt` formateado con un título en mayúsculas y su texto limpio correspondiente.

## 🚀 ¿Por qué usar este script?

Este script es la herramienta perfecta si necesitas:

- Crear un **corpus de texto** a partir de una colección de películas o series para análisis de NLP (Procesamiento del Lenguaje Natural).
- Obtener una **transcripción limpia** de varios videos para su estudio o lectura.
- Preparar datos para **entrenar modelos de lenguaje**.
- Simplemente **unificar el diálogo** de múltiples subtítulos en un solo lugar de forma rápida y eficiente.

## 📋 Requisitos

- **Python 3.6** o superior.
- La biblioteca `tkinter` debe estar instalada. Generalmente viene incluida con Python en Windows y macOS. En algunas distribuciones de Linux, podría necesitar ser instalada por separado:
  ```bash
  # Para sistemas basados en Debian/Ubuntu
  sudo apt-get install python3-tk
  ```

## ⚙️ Cómo Usar

1.  **Clona o descarga el repositorio:**

    ```bash
    git clone https://github.com/tu-usuario/SRT_TextExtractor.git
    ```

    O simplemente descarga el archivo `srt_extractor.py` (o el nombre que le hayas dado).

2.  **Navega al directorio del proyecto:**

    ```bash
    cd SRT_TextExtractor
    ```

3.  **Ejecuta el script desde tu terminal:**

    ```bash
    python srt_extractor.py
    ```

4.  **Selecciona la carpeta**: Se abrirá una ventana. Navega y selecciona la carpeta que contiene tus archivos `.srt`.

5.  **¡Listo!**: El script procesará los archivos y creará un `todos.txt` en esa misma carpeta. Un mensaje de confirmación aparecerá en la terminal cuando el proceso haya finalizado.

## 📝 Ejemplo de Funcionamiento

#### Estructura de archivos de entrada:

```
mi_carpeta_de_videos/
├── pelicula_uno.srt
├── serie_ep_01.srt
└── archivo_extra.txt
```

#### Contenido de `pelicula_uno.srt`:

```
1
00:00:05,000 --> 00:00:08,000
Hola, este es el primer diálogo.
[Sonido de puerta]

2
00:00:09,123 --> 00:00:11,456
Y este es el segundo,
después de una acción.
```

#### Archivo de salida `todos.txt` generado:

```
PELICULA_UNO
Hola, este es el primer diálogo. Y este es el segundo, después de una acción.

SERIE_EP_01
Todo el texto limpio del episodio uno consolidado aquí en un solo párrafo...


```

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Si tienes ideas para mejorar el script o encuentras algún error, por favor, abre un "Issue" o envía un "Pull Request".

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
