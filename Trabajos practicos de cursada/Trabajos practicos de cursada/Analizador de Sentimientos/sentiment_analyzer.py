"""
Análisis de Sentimiento en Español - Core Engine
MVP para comparar BETO y RoBERTuito
"""

from transformers import pipeline
import logging
from typing import Dict, List, Tuple, Optional
import warnings

# Suprimir warnings de transformers
warnings.filterwarnings('ignore')
logging.getLogger("transformers").setLevel(logging.ERROR)

class SentimentAnalyzer:
    """
    Clase principal para análisis de sentimiento con modelos transformers
    """

    def __init__(self):
        """Inicializa los modelos BETO y RoBERTuito"""
        self.models = {}
        self._load_models()

    def _load_models(self):
        """Carga los modelos pre-entrenados"""
        try:
            print("Cargando modelos...")

            # BETO - Modelo formal
            self.models['beto'] = pipeline(
                "sentiment-analysis",
                model="finiteautomata/beto-sentiment-analysis"
            )

            # RoBERTuito - Modelo para redes sociales
            self.models['robertuito'] = pipeline(
                "sentiment-analysis",
                model="pysentimiento/robertuito-sentiment-analysis"
            )

            print("Modelos cargados correctamente.")

        except Exception as e:
            raise Exception(f"Error cargando modelos: {str(e)}")

    def analyze_text(self, text: str, model_name: str = 'beto') -> Dict:
        """
        Analiza el sentimiento de un texto con un modelo específico

        Args:
            text: Texto a analizar
            model_name: 'beto' o 'robertuito'

        Returns:
            Dict con label, score y modelo usado
        """
        if not text.strip():
            return {"error": "Texto vacío"}

        if model_name not in self.models:
            return {"error": f"Modelo {model_name} no disponible"}

        try:
            result = self.models[model_name](text)[0]
            return {
                "label": result['label'],
                "score": round(result['score'], 3),
                "model": model_name,
                "text_length": len(text)
            }
        except Exception as e:
            return {"error": f"Error en análisis: {str(e)}"}

    def compare_models(self, text: str) -> Dict:
        """
        Compara ambos modelos en el mismo texto

        Args:
            text: Texto a analizar

        Returns:
            Dict con resultados de ambos modelos
        """
        if not text.strip():
            return {"error": "Texto vacío"}

        try:
            beto_result = self.models['beto'](text)[0]
            robertuito_result = self.models['robertuito'](text)[0]

            return {
                "beto": {
                    "label": beto_result['label'],
                    "score": round(beto_result['score'], 3)
                },
                "robertuito": {
                    "label": robertuito_result['label'],
                    "score": round(robertuito_result['score'], 3)
                },
                "agreement": beto_result['label'] == robertuito_result['label'],
                "text_length": len(text)
            }
        except Exception as e:
            return {"error": f"Error en comparación: {str(e)}"}

    def get_model_info(self) -> Dict:
        """Retorna información sobre los modelos disponibles"""
        return {
            "beto": {
                "name": "BETO (Spanish BERT)",
                "description": "Modelo formal entrenado en Wikipedia",
                "classes": ["POS", "NEU", "NEG"]
            },
            "robertuito": {
                "name": "RoBERTuito",
                "description": "Modelo especializado en redes sociales y jerga",
                "classes": ["POS", "NEU", "NEG"]
            }
        }

# Instancia global para reutilización
analyzer = SentimentAnalyzer()