# Asistente-Experto

## Entorno local

Crear y activar el entorno virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

En Windows PowerShell:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

Instalar dependencias:

```bash
python -m pip install -r requirements.txt
```

Copiar los valores de desarrollo en `.env` y ejecutar la prueba:

```bash
python test_env.py
```