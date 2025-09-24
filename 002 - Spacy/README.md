# Módulo 2: SpaCy y Preprocesamiento

## 🎯 Objetivos
- Dominar la biblioteca SpaCy para procesamiento de lenguaje natural
- Implementar técnicas de preprocesamiento de texto
- Comprender tokenización, lematización y análisis morfológico
- Crear pipelines de procesamiento eficientes

## 🔧 Técnicas de Preprocesamiento Cubiertas

### **Tokenización**
- Separación de texto en tokens
- Manejo de puntuación y espacios
- Tokenización de oraciones vs palabras

### **Análisis Morfológico**
- Lematización: Reducir palabras a su forma base
- Stemming: Eliminación de sufijos
- POS Tagging: Etiquetado de partes del discurso

### **Limpieza de Texto**
- Eliminación de stopwords
- Normalización de caracteres especiales
- Manejo de mayúsculas y minúsculas

## 🚀 Características de SpaCy Implementadas
- Modelos preentrenados para español
- Pipelines eficientes de procesamiento
- Análisis sintáctico y dependencias
- Reconocimiento de entidades nombradas
- Vectorización de palabras

## 💡 Aplicaciones Prácticas
1. **Limpieza de Corpus**: Preparar textos para análisis
2. **Extracción de Información**: Identificar entidades y relaciones
3. **Normalización**: Estandarizar formatos de texto
4. **Análisis Sintáctico**: Comprender estructura gramatical

## 🔧 Stack Tecnológico
```python
import spacy
import pandas as pd
import matplotlib.pyplot as plt

# Cargar modelo en español
nlp = spacy.load("es_core_news_sm")
```

## 📊 Ejercicios Principales
- **Análisis de Texto**: Procesar artículos de noticias
- **Comparación de Técnicas**: Stemming vs Lematización
- **Pipeline Personalizado**: Crear procesador específico
- **Evaluación de Rendimiento**: Medir eficiencia de procesamiento

## 🎓 Competencias Desarrolladas
- ✅ Uso avanzado de SpaCy
- ✅ Técnicas de preprocesamiento
- ✅ Análisis morfológico y sintáctico
- ✅ Optimización de pipelines de NLP

## 🎯 Metodología
- **Brainstorming**: Reflexión sobre preprocesamiento sin sesgos
- **Experimentación**: Comparar diferentes enfoques
- **Aplicación Real**: Textos en español rioplatense

## 🌟 Casos de Uso Especiales
- Procesamiento de textos informales (redes sociales)
- Manejo de jerga argentina
- Análisis de textos académicos
- Procesamiento de documentos legales
