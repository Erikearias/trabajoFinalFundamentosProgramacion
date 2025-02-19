# Configuración del Entorno Virtual y Dependencias

Este documento proporciona los pasos para crear, activar y administrar un entorno virtual en **Windows** y **Linux**, así como la instalación de dependencias desde un archivo `requirements.txt`.

## 1. Crear el Entorno Virtual

Antes de comenzar, asegúrese de tener **Python** instalado en su sistema. Puede verificarlo con:

```bash
python --version

python -m venv venv

## 2. Activacion del entorno virtual
venv\Scripts\activate

##3. Instalacion de dependencias
pip install -r requirements.txt

##4. Desactivacion del entorno virtual
deactivate



