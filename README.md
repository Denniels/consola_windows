# 🖥️ Curso Interactivo de Consolas Windows: PowerShell y CMD

Bienvenido al curso interactivo que te llevará desde cero hasta dominar las dos consolas más populares de Windows: **PowerShell** y **CMD**. Este curso está diseñado para ser práctico, progresivo y accesible, con una interfaz amigable en **Streamlit** que te guiará paso a paso.
---

## 📂 Estructura del Proyecto


```text
consola_windows/
│
├── streamlit_app/               # Interfaz principal del curso
│   ├── pages/                   # Módulos individuales del curso
│   │   ├── 01_intro.py
│   │   ├── 02_cmd_basics.py
│   │   ├── 03_powershell_basics.py
│   │   ├── 04_intermediate_cmd.py
│   │   ├── 05_intermediate_ps.py
│   │   ├── 06_advanced_cmd.py
│   │   ├── 07_advanced_ps.py
│   │   ├── 08_evaluations.py
│   │   └── 09_summary.py
│   ├── components/              # Elementos reutilizables (cards, quizzes, etc.)
│   ├── assets/                  # Imágenes, íconos y recursos visuales
│   ├── css/                    # Estilos personalizados para la app
│   │   ├── main.css            # Estilos globales (fuentes, colores, banners)
│   │   ├── console_cmd.css     # Estilos para simular CMD (fondo negro, texto claro, fuente monoespaciada)
│   │   └── console_ps.css      # Estilos para simular PowerShell (fondo negro, texto azul/blanco, fuente monoespaciada)
│   └── utils/                  # Funciones auxiliares (evaluación, navegación)
│
├── data/                       # Datos de usuario, progreso y evaluaciones
│   ├── users.json
│   └── progress_tracker.json
│
├── docs/                       # Documentación técnica y pedagógica
│   └── resumen.md              # Resumen visual y amigable del curso completo, con ejemplos, explicaciones y opción de descarga en PDF
│
├── requirements.txt            # Dependencias del proyecto
├── README.md                   # Este archivo
└── run.py                      # Script principal para lanzar la app
```

---

## 🎨 Recomendaciones de Diseño Visual y Educativo

- Todas las consolas deben tener fondo negro, fuente monoespaciada y colores de texto que reflejen la experiencia real:
  - **CMD:** texto blanco/gris claro sobre fondo negro.
  - **PowerShell:** texto blanco y azul sobre fondo negro.
- Los banners explicativos deben estar presentes en la página principal y en cada módulo, con colores elegantes (azul oscuro, gris, blanco) y tipografía legible.
- El banner principal debe incluir el nombre del curso, un resumen de objetivos y una invitación a explorar los módulos.
- Cada página/módulo debe tener su propio banner que explique el objetivo de la sección y lo que el usuario aprenderá.
- Usar contrastes altos y espaciados generosos para facilitar la lectura y la navegación.
- Los botones y elementos interactivos deben ser accesibles y con colores que transmitan confianza (azul, verde, gris oscuro).
- Incluir iconos o imágenes educativas en los banners para reforzar el aprendizaje visual.
- Mantener la coherencia visual en toda la app para que la experiencia sea profesional y amigable.
---
# 🚀 Cómo Ejecutar el Curso Localmente
## Requisitos Previos
### 1. Clona el repositorio
```bash

# En tu terminal, navega al directorio donde quieres clonar el repositorio
git clone https://github.com/tu_usuario/consola_windows.git
cd consola_windows
```

### (Opcional) Crear entorno virtual en local
```bash
# En Windows (CMD o PowerShell):
python -m venv consola_windows
consola_windows\Scripts\activate
# En Linux/macOS:
python3 -m venv consola_windows
source consola_windows/bin/activate
```
✅ Una vez activado, verás el nombre del entorno en tu terminal. Esto asegura que todas las dependencias se instalen de forma aislada.

### 3. Instala las dependencias
```bash
pip install -r requirements.txt

# 4. Ejecuta la app
streamlit run \streamlit_app\app.py
```

---

## 📑 Comandos CMD y PowerShell: De Básico a Avanzado

### CMD Básico
- dir
- cd
- cls
- copy
- del
- type
- echo
- mkdir
- rmdir
- move
- help

### CMD Intermedio/Avanzado
- find
- findstr
- xcopy
- tasklist
- taskkill
- netstat
- ipconfig
- set
- for /f %%i in (...)
- call
- start
- attrib
- chkdsk

### PowerShell Básico
- Get-Help
- Get-Command
- Get-Process
- Get-Service
- Set-Location
- Get-ChildItem
- Clear-Host
- Write-Output
- New-Item
- Remove-Item
- Copy-Item
- Move-Item

### PowerShell Intermedio/Avanzado
- Get-Content
- Set-Content
- Select-Object
- Where-Object
- ForEach-Object
- Start-Process
- Stop-Process
- Get-EventLog
- Get-WmiObject
- Test-Connection
- Import-Csv
- Export-Csv
- Invoke-WebRequest
- Register-ScheduledJob
- Get-Module
- Import-Module

---

## ❌ Errores Comunes en CMD y PowerShell

### Sintaxis
- Escribir mal el nombre del comando (ej: `ecoh` en vez de `echo`)
- Olvidar comillas en rutas con espacios
- Usar `/` en vez de `-` en PowerShell
- No respetar mayúsculas/minúsculas en variables de PowerShell

### Errores de Uso
- Intentar borrar archivos protegidos
- No tener permisos de administrador
- Usar rutas relativas incorrectas
- Olvidar el parámetro obligatorio de un comando

### Errores Avanzados
- Redirección incorrecta de salida (`>` vs `>>`)
- Pipes mal formados (`|`)
- Variables no inicializadas en scripts
- Uso de comandos de CMD en PowerShell y viceversa
- Errores de encoding al leer/escribir archivos

---

## 🤖 Lógica del Parser Interactivo para Simulación en la Nube

La app utiliza un parser interno que permite:

- Detectar si el comando es CMD o PowerShell.
- Validar sintaxis y parámetros.
- Buscar el comando en una base de comandos simulados.
- Devolver una salida simulada realista o explicación pedagógica.
- Identificar errores comunes y sugerir correcciones.
- Permitir feedback inmediato y personalizado.

### Ejemplo de flujo del parser:

1. El usuario ingresa: `Get-Process`.
2. El parser detecta PowerShell y busca el comando.
3. Si es válido, devuelve una tabla simulada de procesos.
4. Si hay error de sintaxis, muestra el error y cómo corregirlo.
5. Si el comando no existe, sugiere alternativas o explica por qué no es válido.

Este enfoque permite una experiencia interactiva, segura y educativa, completamente desplegada en la nube con Streamlit Cloud.

## 🧪 ¿Cómo Simula la App las Consolas CMD y PowerShell?

La simulación de las consolas se realiza mediante una combinación de procesamiento de comandos, visualización interactiva y ejecución segura.

### 🔍 Arquitectura de Simulación

- **Entrada de comandos:** El usuario escribe comandos en un campo de texto tipo terminal.
- **Parser de comandos:** La app identifica si el comando pertenece a CMD o PowerShell y lo procesa según su sintaxis.
- **Ejecución controlada:**
  - En la nube: Se simula la salida con respuestas predefinidas o entornos restringidos.
- **Salida formateada:** La respuesta se muestra en un área tipo consola, con colores y estilos que imitan el terminal real.
- **Validación pedagógica:** Se analiza el comando para dar retroalimentación educativa, incluso si el resultado es incorrecto.

### 🛡️ Seguridad

- Todos los comandos peligrosos o no reconocidos son bloqueados y explicados.
- No hay riesgo de afectar el sistema del usuario ni el servidor.


### 🧩 Componentes clave

- **CommandInput:** Campo de entrada tipo terminal.
- **CommandParser:** Detecta consola y estructura del comando.
- **CommandSimulator:** Simula la ejecución y genera la salida.
- **FeedbackEngine:** Da retroalimentación educativa y sugerencias.
- **ConsoleRenderer:** Muestra la salida con estilo terminal.

### 🎯 Objetivos del Curso

- Comprender la diferencia entre CMD y PowerShell.
- Ejecutar comandos básicos y avanzados en ambas consolas.
- Automatizar tareas con scripts.
- Navegar el sistema de archivos desde la terminal.
- Crear scripts útiles para administración de sistemas.
- Evaluar tu nivel de dominio sin presión de calificaciones.

### 🧠 Metodología

Cada módulo incluye:
- 📖 Teoría clara y concisa.
- 🧪 Prácticas interactivas con retroalimentación.
- 🧩 Mini-desafíos para aplicar lo aprendido.
- 📊 Evaluaciones diagnósticas para conocer tu nivel.

### 📚 Contenido del Curso

| Módulo | Tema | Consola | Nivel |
|--------|-------------------------------|----------|-------------|
| 01     | Introducción a las Consolas   | Ambas    | Principiante|
| 02     | Comandos Básicos en CMD       | CMD      | Principiante|
| 03     | Comandos Básicos en PowerShell| PowerShell| Principiante|
| 04     | Scripts y Variables           | CMD      | Intermedio  |
| 05     | Pipes, Objetos y Funciones    | PowerShell| Intermedio  |
| 06     | Automatización y Tareas Prog. | CMD      | Avanzado    |
| 07     | Administración del Sistema    | PowerShell| Avanzado    |
| 08     | Evaluaciones Interactivas     | Ambas    | Todos       |
| 09     | Recursos y Siguientes Pasos   | -        | -           |

### 🧩 Evaluaciones

Las evaluaciones están diseñadas para:
- Identificar tu nivel actual.
- Recomendar módulos según tu progreso.
- No asignan notas, solo te orientan.

### 🛠️ Tecnologías Utilizadas

- 🐍 Python 3.10+
- 📊 Streamlit Cloud
- 🪟 Simulación de PowerShell & CMD
- 🧠 JSON para seguimiento de progreso
- 🧩 Componentes interactivos personalizados

### 🤝 Contribuciones

¿Quieres mejorar el curso o agregar nuevos módulos? ¡Bienvenido! Puedes abrir un issue o enviar un pull request.

### 📄 Licencia

Este proyecto está bajo la licencia MIT. Puedes usarlo, modificarlo y compartirlo libremente.

### ✨ Autor

Desarrollado por Daniel Mardones — Especialista en python.
