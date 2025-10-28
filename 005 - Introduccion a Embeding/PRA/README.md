# Modelos de Word Embeddings

## 🔤 Word2Vec
- **Arquitecturas**: CBOW (contexto → palabra) y Skip-gram (palabra → contexto)
- **Ventaja**: Captura relaciones semánticas eficientemente
- **Limitación**: No maneja palabras fuera de vocabulario (OOV)

## 🌐 GloVe (Global Vectors)
- **Enfoque**: Combina estadísticas globales con contexto local
- **Ventaja**: Excelente rendimiento en relaciones de palabras
- **Base**: Factorización de matriz de co-ocurrencias

## ⚡ FastText
- **Innovación**: Usa subword information (n-gramas de caracteres)
- **Ventaja**: Maneja palabras OOV y morfología compleja
- **Ideal**: Idiomas con flexión morfológica y textos con errores

## 📊 Uso Recomendado
- **Word2Vec**: Prototipado rápido y vocabularios establecidos
- **GloVe**: Tareas que requieren información corpus-global
- **FastText**: Aplicaciones con palabras raras, errores o múltiples idiomas
