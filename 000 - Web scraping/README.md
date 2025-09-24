# 🌐 Web Scraping: Introducción y Fundamentos

## 📖 ¿Qué es el Web Scraping?

El **web scraping** es una técnica automatizada para extraer información de sitios web. Consiste en recuperar datos de páginas web de manera programática, transformando contenido no estructurado (HTML) en datos estructurados para su análisis.

## 🎯 Objetivos de esta sección

- Comprender los fundamentos del web scraping
- Aprender a usar BeautifulSoup para extraer datos
- Identificar elementos HTML y patrones de contenido
- Manejar ética y legalmente el scraping de datos

## 🛠️ Herramientas principales

### BeautifulSoup
```python
from bs4 import BeautifulSoup
import requests

# Ejemplo básico
response = requests.get('https://ejemplo.com')
soup = BeautifulSoup(response.content, 'html.parser')
```

### Librerías complementarias
- `requests`: Para hacer peticiones HTTP
- `pandas`: Para manejo y almacenamiento de datos
- `re`: Para expresiones regulares

## 📋 Contenido del módulo

### 1. **Conceptos básicos**
- Anatomía de una página web
- Estructura HTML/DOM
- Selectores CSS y XPath

### 2. **Técnicas de extracción**
- Búsqueda por etiquetas
- Selectores por clase e ID
- Navegación por el árbol DOM
- Extracción de atributos y texto

### 3. **Ejemplos prácticos**
```python
# Extraer todos los enlaces
enlaces = soup.find_all('a')

# Extraer texto de elementos específicos
titulos = soup.find_all('h1', class_='titulo')

# Navegación entre elementos
contenedor = soup.find('div', id='contenido')
parrafos = contenedor.find_all('p')
```

### 4. **Manejo de datos extraídos**
- Limpieza y transformación
- Almacenamiento en CSV/JSON
- Estructuración en DataFrames

## ⚠️ Consideraciones importantes

### ✅ Ética y legalidad
- Respetar `robots.txt`
- No sobrecargar servidores
- Usar delays entre peticiones
- Verificar términos de servicio

### 🔧 Buenas prácticas
```python
import time
from random import uniform

# Delay entre peticiones
time.sleep(uniform(1, 3))

# Headers apropiados
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}
```

## 🚀 Proyectos incluidos

1. **Scraping de noticias**: Extraer titulares y fechas
2. **Datos de productos**: Precios y descripciones de e-commerce
3. **Contenido académico**: Artículos y publicaciones
4. **Datos sociales**: Comentarios y reseñas (con limitaciones)

## 📊 Resultados esperados

Al finalizar esta sección podrás:
- Extraer datos estructurados de cualquier sitio web
- Manejar paginación y navegación
- Limpiar y organizar datos extraídos
- Exportar resultados en formatos útiles para análisis


