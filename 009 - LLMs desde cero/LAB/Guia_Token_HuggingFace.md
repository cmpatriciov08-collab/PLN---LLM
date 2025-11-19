# Guía para Configurar tu Token de Acceso en Hugging Face

Esta guía te acompaña paso a paso en la configuración de tu token de acceso de Hugging Face, una herramienta fundamental para trabajar con modelos de lenguaje, datasets y aplicaciones en la plataforma.

---

## ¿Qué es un token de acceso y por qué lo necesitás?

Un **token de acceso** es una credencial digital personal que te permite:

- Descargar modelos y datasets de acceso restringido
- Interactuar con la API de Hugging Face desde tu código
- Subir tus propios modelos y datasets
- Acceder a Spaces privados o con autenticación

**Importante**: Tu token es como una contraseña. Guardalo de forma segura y nunca lo compartas públicamente.

---

## Paso 1: Crear tu token de acceso

### 1.1. Accedé a la configuración de tokens

Ingresá a tu cuenta de Hugging Face y navegá a:
https://huggingface.co/settings/tokens

### 1.2. Generá un nuevo token

1. Hacé clic en el botón **"Create new token"**
2. Asigná un nombre descriptivo (por ejemplo: "Token-Curso-NLP-2025")
3. Seleccioná el tipo de permisos:
   - **Read**: Solo lectura (descargar modelos y datasets públicos)
   - **Write**: Lectura y escritura (subir contenido)
   - **Fine-grained**: Permisos personalizados por repositorio

**Recomendación para estudiantes**: Seleccioná "Write" para tener acceso completo durante el curso.

### 1.3. Copiá tu token

Una vez creado, **copiá el valor del token inmediatamente**. Este valor solo se muestra una vez. Si lo perdés, tendrás que crear uno nuevo.

El token tiene este formato: `hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

---

## Paso 2: Usar tu token en Google Colab o Jupyter Notebook

Existen dos formas principales de autenticarte con tu token:

### Opción A: Login interactivo (recomendado para principiantes)

```python
from huggingface_hub import login

# Se abrirá un campo de texto para pegar tu token
login()
```

Al ejecutar esta celda, aparecerá un campo donde podés pegar tu token de forma segura.

### Opción B: Login directo con el token

```python
from huggingface_hub import login

# Reemplazá con tu token real
login("hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
```

**Advertencia**: No subas notebooks con tu token visible a repositorios públicos.

### Uso del token al cargar modelos

También podés pasar el token directamente al cargar un modelo:

```python
from transformers import pipeline

# Opción 1: Pasando el token explícitamente
model = pipeline(
    "text-generation",
    model="gpt2",
    token="hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
)

# Opción 2: Después de hacer login()
from huggingface_hub import login
login()  # Se autentica una vez
model = pipeline("text-generation", model="gpt2")
```

---

## Paso 3: Verificar que tu token funciona correctamente

Probá tu autenticación con este código simple:

```python
from huggingface_hub import whoami, login

# Primero autenticarse
login("hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

# Verificar identidad
usuario = whoami()
print(f"Conectado como: {usuario['name']}")
print(f"Email: {usuario.get('email', 'No disponible')}")
```

Si ves tu información de usuario, la configuración fue exitosa.

---

## Buenas prácticas de seguridad

### Mantené tu token seguro

- **No lo compartas** en chats, foros o grupos de estudio
- **No lo subas** a GitHub, GitLab u otros repositorios públicos
- **No lo incluyas** en capturas de pantalla que vayas a compartir

### Si tu token se filtró

1. Ingresá inmediatamente a https://huggingface.co/settings/tokens
2. Eliminá el token comprometido haciendo clic en "Delete"
3. Creá un nuevo token
4. Actualizá tu código con el nuevo valor

### Alternativa: Variables de entorno

Para proyectos más avanzados, podés usar variables de entorno:

```python
import os
from huggingface_hub import login

# Cargar token desde variable de entorno
token = os.environ.get("HUGGINGFACE_TOKEN")
login(token)
```

En Google Colab, podés usar Secrets para almacenar tu token de forma segura.

---

## Solución de problemas comunes

### Error: "Invalid token"
- Verificá que copiaste el token completo sin espacios
- Asegurate de que el token no fue eliminado de tu cuenta
- Creá un nuevo token si es necesario

### Error: "Permission denied"
- Revisá que tu token tenga los permisos necesarios (Write para subir contenido)
- Algunos modelos requieren aceptar términos de uso en la página del modelo

### Error: "Token expired"
Los tokens de Hugging Face no expiran automáticamente, pero si ves este error:
- Eliminá el token actual y creá uno nuevo
- Verificá que estés usando la versión más reciente de las librerías

---

## Instalación de librerías necesarias

Antes de usar tu token, asegurate de tener instaladas las librerías necesarias:

```python
# En Google Colab o Jupyter
!pip install --upgrade huggingface_hub transformers
```

---

## Recursos adicionales

- **Documentación oficial**: https://huggingface.co/docs
- **Explorador de modelos**: https://huggingface.co/models
- **Datasets disponibles**: https://huggingface.co/datasets
- **Spaces (aplicaciones)**: https://huggingface.co/spaces

---

## Preguntas frecuentes

**¿Cuántos tokens puedo crear?**
Podés crear múltiples tokens con diferentes permisos. Es buena práctica tener tokens separados para diferentes proyectos.

**¿El token tiene costo?**
No, crear y usar tokens es completamente gratuito. Solo algunos modelos o datasets privados pueden requerir suscripciones.

**¿Puedo compartir mi token con mi compañero de equipo?**
No es recomendable. Cada persona debe crear su propio token. Para colaboración, usá repositorios compartidos donde cada uno se autentique con su propio token.

---

**¿Dudas o consultas?** Contactá al docente o consultá en el foro del curso.
