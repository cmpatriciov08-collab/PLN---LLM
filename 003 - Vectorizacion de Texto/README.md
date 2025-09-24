# Text Mining y Vectorización

## 🎯 Objetivos del Módulo

- Dominar técnicas de vectorización de texto (Bag of Words, TF-IDF)
- Implementar análisis de text mining en corpus reales
- Comprender n-gramas y términos compuestos
- Analizar el corpus de cuentos de Hernán Casciari

## 🔢 Técnicas de Vectorización

### Bag of Words (BoW)
- Representación de frecuencias de palabras
- Matriz documento-término
- Ventajas y limitaciones

### TF-IDF (Term Frequency - Inverse Document Frequency)
- Ponderación por importancia relativa
- Reducción del peso de palabras comunes
- Identificación de términos discriminativos

### N-gramas
- **Unigramas**: Palabras individuales
- **Bigramas**: Pares de palabras ("Buenos Aires")
- **Trigramas**: Tríos de palabras ("Mar del Plata")

## 📖 Corpus de Cuentos de Casciari

### Características del Dataset
- **Período**: 2004-2015 (12 años de producción)
- **Género**: Cuentos en español rioplatense
- **Temática**: Vida cotidiana, humor, crítica social
- **Formato**: Textos limpios y datos procesados

### Análisis Realizados
1. **Evolución temporal** del vocabulario
2. **Temas recurrentes** por año
3. **Análisis de sentimientos** implícito
4. **Patrones lingüísticos** del autor

## 🔧 Herramientas Utilizadas

```python
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
```

## 💡 Conceptos Clave

### Preprocesamiento Avanzado
- Manejo de stopwords en español
- Normalización de caracteres especiales
- Tratamiento de términos compuestos

### Análisis Estadístico
- Distribución de frecuencias
- Palabras más discriminativas
- Correlaciones entre documentos

## 🚀 Ejercicios Prácticos

1. **Análisis Temporal**: Evolución del vocabulario de Casciari
2. **Comparación de Métodos**: BoW vs TF-IDF
3. **N-gramas Especializados**: Detección de expresiones argentinas
4. **Visualización**: Nubes de palabras y gráficos de frecuencia

## 📊 Resultados Esperados

- Comprensión profunda de vectorización de texto
- Habilidad para analizar corpus literarios
- Identificación de patrones lingüísticos
- Preparación para técnicas más avanzadas

## 🎓 Competencias Desarrolladas

- ✅ Vectorización de texto con scikit-learn
- ✅ Análisis de corpus literarios
- ✅ Manejo de datos temporales en NLP
- ✅ Visualización de resultados de text mining

## 🎯 Metodología de Micro-laboratorios

- **Brainstorming**: "¿Cómo podemos representar el texto de manera que se preserve la información relevante y se minimice el ruido?"
- **Análisis Colaborativo**: Interpretación de resultados en equipo
- **Aplicación Cultural**: Análisis de literatura argentina contemporánea

## 🌟 Casos de Uso Especiales

- Análisis de evolución estilística de un autor
- Detección de temas recurrentes en literatura
- Comparación de corpus por períodos temporales
- Identificación de regionalismos y argentinismos
