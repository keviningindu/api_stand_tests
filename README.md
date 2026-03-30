Pruebas de creación de usuario – parámetro firstName
Este proyecto contiene un conjunto de pruebas automatizadas enfocadas en validar el parámetro firstName al momento de crear un/a usuario/a en la API de [].
El objetivo es asegurar que el sistema maneje correctamente diferentes escenarios de entrada, incluyendo valores válidos, inválidos y casos límite.
🧪 Tecnologías utilizadas
- Python 3.x
- pytest – framework de pruebas
- requests – librería para realizar llamadas HTTP
📋 Requisitos previos
Antes de ejecutar las pruebas, asegúrate de tener instalados los paquetes necesarios:
-pip install pytest requests

▶️ Ejecución de pruebas
Para correr todas las pruebas, utiliza el siguiente comando en la raíz del proyecto:
-pytest

ambién puedes ejecutar pruebas específicas indicando el archivo o la función de prueba:
-pytest tests/test_firstname.py::test_nombre_valido

📂 Estructura del proyecto
.
├── tests/
│   ├── test_firstname.py   # Pruebas unitarias y de integración para el parámetro firstName
├── README.md               # Documentación del proyecto


✅ Casos cubiertos
Las pruebas incluyen:
- Creación de usuario con firstName válido.
- Manejo de valores vacíos o nulos.
- Validación de caracteres especiales y longitud máxima.
- Respuesta de la API ante entradas inválidas.
🎯 Objetivo
Este proyecto busca garantizar la robustez y consistencia del sistema de creación de usuarios, reduciendo defectos y mejorando la calidad del software.
