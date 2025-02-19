Configuración del Entorno Virtual y Dependencias

Este documento proporciona los pasos para crear, activar y administrar un entorno virtual en Windows y Linux, así como la instalación de dependencias desde un archivo requirements.txt.

1. Crear el Entorno Virtual

Antes de comenzar, asegúrese de tener Python instalado en su sistema. Puede verificarlo con:

python --version

Para crear el entorno virtual, ejecute el siguiente comando en la carpeta del proyecto:

python -m venv venv

Esto generará un directorio llamado venv, que contendrá los archivos necesarios para el entorno virtual.

2. Activar el Entorno Virtual

En Windows (CMD o PowerShell)

Ejecute:

venv\Scripts\activate

Si usa PowerShell, puede ser necesario habilitar permisos de ejecución:

Set-ExecutionPolicy Unrestricted -Scope Process
venv\Scripts\Activate

Si la activación es exitosa, verá (venv) al inicio de la línea de comandos.

En Linux/macOS

Ejecute:

source venv/bin/activate

Si la activación es exitosa, verá (venv) al inicio de la línea de comandos.

3. Instalar Dependencias

Si el proyecto ya tiene un archivo requirements.txt con las dependencias necesarias, instálelas con:

pip install -r requirements.txt

Si desea guardar las dependencias actuales en el archivo requirements.txt, use:

pip freeze > requirements.txt

4. Desactivar el Entorno Virtual

Para salir del entorno virtual y volver al sistema normal de Python, ejecute:

deactivate

5. Uso de Jupyter Notebook (Opcional)

Si desea usar Jupyter Notebook dentro del entorno virtual, instale los paquetes necesarios:

pip install jupyter ipykernel
python -m ipykernel install --user --name=venv --display-name "Python (venv)"

Luego, puede iniciar Jupyter Notebook con:

jupyter notebook

6. Instalación y Creación del Entorno Virtual en Otros Dispositivos (Windows)

Si necesita configurar el entorno virtual en otro dispositivo con Windows, siga estos pasos:

1. Clonar el Repositorio

Si el proyecto está en GitHub, clónelo con:

git clone https://github.com/tu-usuario/tu-repositorio.git

Luego, acceda a la carpeta del proyecto:

cd tu-repositorio

2. Crear y Activar el Entorno Virtual

python -m venv venv
venv\Scripts\activate

3. Instalar Dependencias

pip install -r requirements.txt

4. Verificar Instalación

pip list

Esto listará todas las bibliotecas instaladas en el entorno virtual.

5. Desactivar el Entorno Virtual

Para salir del entorno virtual:

deactivate

Con estos pasos, cualquier persona puede configurar el entorno virtual en un nuevo dispositivo Windows y estar listo para trabajar. 🚀
