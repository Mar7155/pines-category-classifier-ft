# Instrucciones de instalación y creación de venv (Windows - PowerShell)

Este archivo explica cómo crear un entorno virtual (venv) en Windows usando PowerShell e instalar las dependencias listadas en `requirements.txt` del proyecto.

## Requisitos previos

- Python 3.8+ instalado y en PATH (ej. `python --version`).
- Conexión a Internet para descargar paquetes.
- Espacio suficiente en disco si vas a instalar `torch` (si instalas versiones con CUDA puede requerir más espacio).

## Pasos (PowerShell)

1) Abrir PowerShell en la carpeta del proyecto (donde están `requirements.txt`, `fine_tuning.py` y `clasificando.py`).

2) Crear el entorno virtual:

```powershell
python -m venv .venv
```

3) Activar el entorno virtual:

```powershell
# En PowerShell
.\.venv\Scripts\Activate.ps1
```

Si PowerShell bloquea la ejecución de scripts, puedes permitir scripts firmados para el usuario actual:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
# Luego vuelve a activar:
.\.venv\Scripts\Activate.ps1
```

4) (Opcional) Actualizar pip:

```powershell
python -m pip install --upgrade pip
```

5) Instalar las dependencias desde `requirements.txt`:

```powershell
python -m pip install -r .\requirements.txt
```

Nota sobre `torch` (PyTorch):

- En Windows la instalación de `torch` suele requerir descargar la rueda correcta para CPU o la versión de CUDA correspondiente a tu GPU.
- Si la instalación directa falla o quieres instalar una versión específica, visita https://pytorch.org y copia el comando recomendado para tu sistema.
- Ejemplo (CPU) — usar la instrucción oficial si pip directo no resuelve la rueda:

```powershell
python -m pip install --index-url https://download.pytorch.org/whl/cpu torch
```

O si prefieres fijar una versión (ejemplo):

```powershell
python -m pip install torch==2.2.0 --index-url https://download.pytorch.org/whl/cpu
```

(Reemplaza la versión por la que necesites; consulta la web oficial para la última recomendada.)

## Verificar la instalación

Con el entorno activo, puedes ejecutar un pequeño chequeo:

```powershell
python -c "import transformers, datasets, pandas, sklearn; print('transformers', transformers.__version__, 'datasets', datasets.__version__, 'pandas', pandas.__version__)"
```

Si el comando no imprime errores y muestra versiones, las librerías principales se instalaron correctamente.

Para chequear `torch`:

```powershell
python -c "import torch; print('torch', torch.__version__, 'cuda_available', torch.cuda.is_available())"
```

## Ejecutar los scripts del proyecto

Con el entorno activado y las dependencias instaladas:

- Para entrenar / fine-tuning (puede tardar dependiendo de hardware):

```powershell
python .\fine_tuning.py
```

- Para probar el clasificador guardado (usa la carpeta `./ms_pines_funcion_classifier` creada por `fine_tuning.py`):

```powershell
python .\clasificando.py
```

## Troubleshooting rápido

- Error: "ImportError: No module named 'torch'" → instala `torch` con el comando recomendado en https://pytorch.org.
- Error al activar el venv (ExecutionPolicy) → ejecuta `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` en PowerShell (puede pedir permisos).
- Problemas de permisos al instalar paquetes → asegúrate de tener el venv activado (no uses `pip` global por accidente) y prueba a ejecutar PowerShell como administrador si es necesario.

## Notas finales

- El archivo `requirements.txt` en este proyecto contiene las dependencias principales: `transformers`, `datasets`, `pandas`, `scikit-learn`, y menciona `torch` por separado (debido a sus requerimientos especiales en Windows).
- Si quieres, puedo ejecutar estos pasos aquí (crear/activar venv e intentar instalar las dependencias) y reportar el resultado. Dime si deseas que los ejecute.

---
Generado automáticamente: instrucciones para crear venv e instalar dependencias en Windows (PowerShell).