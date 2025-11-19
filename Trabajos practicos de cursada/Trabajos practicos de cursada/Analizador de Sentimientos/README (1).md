---
title: SENTIMENT ANALYZER
emoji: 📉
colorFrom: indigo
colorTo: purple
sdk: gradio
sdk_version: 5.49.1
app_file: app.py
pinned: false
license: apache-2.0
short_description: COMPARADOR DE MODELOS
---


# 😊 Análisis de Sentimiento en Español

MVP para análisis de sentimiento en español utilizando modelos transformers pre-entrenados de HuggingFace.

## 🚀 Características

- **Comparación side-by-side** de dos modelos especializados en español
- **BETO**: Modelo formal entrenado en Wikipedia española
- **RoBERTuito**: Modelo especializado en redes sociales y jerga coloquial
- **Interfaz web** intuitiva con Gradio
- **Análisis en tiempo real** con indicadores de confianza

## 🏗️ Arquitectura

```
LAB-Desarrollo/
├── sentiment_analyzer.py  # Core engine con modelos transformers
├── utils.py              # Utilidades de procesamiento de texto
├── app.py                # Interfaz Gradio
├── requirements.txt      # Dependencias
└── README.md            # Esta documentación
```

## 🛠️ Instalación y Uso Local

### 1. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 2. Ejecutar la aplicación
```bash
python app.py
```

La aplicación estará disponible en `http://localhost:7860`

## 📦 Deploy en Hugging Face Spaces

### 1. Crear un nuevo Space
- Ve a [Hugging Face Spaces](https://huggingface.co/spaces)
- Crea un nuevo Space con Gradio como SDK
- Clona el repositorio localmente

### 2. Subir archivos
Copia estos archivos al Space:
- `app.py` (como archivo principal)
- `sentiment_analyzer.py`
- `utils.py`
- `requirements.txt`

### 3. Configurar el Space
- **SDK**: Gradio
- **App file**: `app.py`
- **Requirements**: `requirements.txt`

## 🎯 Uso de la Aplicación

### Modos de análisis:
1. **BETO**: Análisis formal, mejor para textos escritos
2. **RoBERTuito**: Especializado en jerga y redes sociales
3. **Comparar**: Muestra resultados de ambos modelos side-by-side

### Ejemplos de uso:
- ✅ "La comida estaba deliciosa" → POS
- ❌ "El servicio fue pésimo" → NEG
- 😐 "Está bien, nada especial" → NEU

## 🤖 Modelos Utilizados

### BETO (`finiteautomata/beto-sentiment-analysis`)
- Basado en BERT entrenado en Wikipedia española
- 110M parámetros
- Mejor para textos formales
- 3 clases: POS, NEU, NEG

### RoBERTuito (`pysentimiento/robertuito-sentiment-analysis`)
- RoBERTa entrenado en tweets españoles
- Maneja jerga, emojis y expresiones coloquiales
- Ideal para redes sociales
- 3 clases: POS, NEU, NEG

## 🔧 Tecnologías

- **Transformers**: HuggingFace transformers library
- **Gradio**: Interfaz web para ML
- **PyTorch**: Backend de deep learning
- **Python 3.8+**: Lenguaje de programación

## 📊 Limitaciones

- Máximo 512 tokens por texto (limitación de BERT)
- Modelos out-of-the-box (sin fine-tuning específico)
- No maneja contexto conversacional avanzado
- Puede tener dificultades con ironía/sarcasmo

## 🚀 Próximas Mejoras

- [ ] Fine-tuning con datos específicos del dominio
- [ ] Soporte para análisis de emociones (más de 3 clases)
- [ ] Procesamiento batch para múltiples textos
- [ ] API REST para integración
- [ ] Visualizaciones avanzadas de atención

## 📝 Licencia

Este proyecto es parte del curso de Procesamiento de Lenguaje Natural - Tecnicatura en Ciencia de Datos (IFTS).

## 🤝 Contribuciones

Para mejoras o reportes de bugs, por favor crear un issue en el repositorio del curso.

---


Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference
