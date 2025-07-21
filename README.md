# 🖥️ Curso Interactivo de Consolas Windows: PowerShell y CMD

Bienvenido al curso interactivo que te llevará desde cero hasta dominar las dos consolas más populares de Windows: **PowerShell** y **CMD**. Este curso está diseñado para ser práctico, progresivo y accesible, con una interfaz amigable en **Streamlit** que te guiará paso a paso.
---

## 📂 Estructura del Proyecto


```text
consola_windows/
│
├── streamlit_app/               # Interfaz principal del curso
│   ├── app.py                  # Aplicación principal de Streamlit
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
│   ├── components/              # Componentes modulares reutilizables
│   │   ├── ui_components.py    # Componente principal y hub de imports (180 líneas)
│   │   ├── quiz_components.py  # Componentes de quiz y práctica interactiva (234 líneas)
│   │   ├── console_components.py # Simulador de consolas CMD y PowerShell (156 líneas)
│   │   └── ui_helpers.py       # Funciones auxiliares y elementos UI (211 líneas)
│   ├── assets/                  # Imágenes, íconos y recursos visuales
│   ├── css/                    # Estilos personalizados para la app
│   │   ├── main.css            # Estilos globales (fuentes, colores, banners)
│   │   ├── console_cmd.css     # Estilos auténticos CMD (negro, plata, Consolas 12px)
│   │   ├── console_ps.css      # Estilos auténticos PowerShell (azul, blanco, Consolas 12px)
│   │   ├── console_fonts.css   # Fuentes monoespaciadas y fallbacks web
│   │   └── antitranslation.css # Protección contra traducción automática
│   └── utils/                  # Funciones auxiliares del sistema
│       ├── command_parser.py   # Parser de comandos CMD y PowerShell
│       ├── progress_tracker.py # Sistema de seguimiento de progreso
│       └── user_manager.py     # Gestión de usuarios y autenticación
│
├── data/                       # Datos de usuario, progreso y evaluaciones
│   ├── users.json             # Base de datos de usuarios registrados
│   └── progress_tracker.json  # Seguimiento de progreso por usuario
│
├── docs/                       # Documentación técnica y pedagógica
│   └── resumen.md              # Resumen visual del curso completo
│
├── requirements.txt            # Dependencias del proyecto
├── README.md                   # Este archivo de documentación
└── run.py                      # Script principal para lanzar la app
```

---

## 🏗️ Arquitectura Modular

### 📦 Componentes Principales

El proyecto ha sido refactorizado desde un archivo monolítico de 860+ líneas hacia una **arquitectura modular** que mejora la mantenibilidad, escalabilidad y legibilidad del código:

#### `ui_components.py` (180 líneas) - Hub Central
- **Función**: Punto de entrada principal y gestor de imports
- **Responsabilidades**: 
  - Importación centralizada de todos los componentes
  - Clases principales como `NavigationComponent` y `ProgressCard`
  - Sistema de fallback para garantizar disponibilidad de componentes
- **Reducción**: 87% de reducción de tamaño (de 860+ a 180 líneas)

#### `quiz_components.py` (234 líneas) - Sistema de Evaluación
- **Función**: Componentes interactivos de quiz y práctica
- **Clases principales**:
  - `QuizComponent`: Sistema de preguntas con puntuación
  - `CommandPracticeComponent`: Práctica interactiva de comandos
- **Características**: Navegación de preguntas, sistema de puntuación, integración con progreso

#### `console_components.py` (156 líneas) - Simulación de Consolas
- **Función**: Simulador de consolas CMD y PowerShell
- **Clase principal**: `ConsoleSimulator`
- **Características**: 
  - Simulación realista de comportamiento de consolas
  - Parser de comandos integrado
  - Retroalimentación educativa en tiempo real

#### `ui_helpers.py` (211 líneas) - Utilidades UI
- **Función**: Funciones auxiliares y elementos de interfaz
- **Incluye**:
  - Creación de cards informativos
  - Tablas de referencia de comandos protegidas contra traducción
  - Elementos de interfaz reutilizables
  - Sistema anti-traducción para mantener comandos en inglés

### 🔄 Beneficios de la Modularización

#### ✅ Mantenibilidad Mejorada
- **Separación clara de responsabilidades**: Cada módulo tiene una función específica
- **Reducción de acoplamiento**: Los componentes son independientes y reutilizables
- **Facilidad de debugging**: Errores localizados en módulos específicos

#### ✅ Escalabilidad
- **Adición de nuevos componentes**: Fácil extensión sin afectar código existente
- **Reutilización**: Componentes disponibles para múltiples páginas
- **Carga modular**: Importación bajo demanda mejora rendimiento

#### ✅ Calidad del Código
- **87% de reducción en tamaño**: Archivo principal pasó de 860+ a 180 líneas
- **Código más legible**: Funciones y clases organizadas por propósito
- **Testeo simplificado**: Cada módulo puede ser probado independientemente

#### ✅ Estrategia de Imports Robusta
- **Imports absolutos**: Rutas consistentes y predecibles
- **Sistema de fallback**: Clases de respaldo si falla la importación principal
- **Gestión de errores**: Logging y manejo graceful de fallos de importación

---

## 🎨 Experiencia Visual Auténtica

### 🖥️ Simuladores de Consola con Colores Originales

Las consolas simuladas replican **exactamente** la apariencia visual de las consolas reales de Windows:

#### ⬛ **CMD (Símbolo del sistema)**
- **Fondo**: Negro puro (#000000) como la consola real
- **Texto**: Gris plata (#c0c0c0) para máximo contraste  
- **Fuente**: Consolas 12px (tamaño auténtico de Windows)
- **Errores**: Rojo puro (#ff0000) como CMD real
- **Éxito**: Verde brillante (#00ff00) 
- **Sin bordes redondeados**: Mantiene la estética clásica de CMD

#### 🔷 **PowerShell**  
- **Fondo**: Azul oscuro auténtico (#012456) de PowerShell original
- **Texto**: Blanco puro (#ffffff) para legibilidad óptima
- **Path**: Cyan brillante (#00ffff) como PowerShell real
- **Fuente**: Consolas 12px (tamaño auténtico de PowerShell)
- **Advertencias**: Texto negro sobre fondo amarillo brillante (como PowerShell real)
- **Cmdlets**: Amarillo (#ffff00) para destacar comandos

### 🎯 Detalles de Autenticidad Visual

- **Fuentes monoespaciadas**: Consolas, Lucida Console, Monaco con fallbacks web
- **Tamaños auténticos**: 12px como en las consolas reales (no 14px genérico)
- **Interlineado compacto**: 1.2 para replicar la densidad visual real  
- **Sin efectos modernos**: Sin sombras, gradientes o bordes redondeados
- **Scrollbars personalizadas**: Colores que combinan con cada consola
- **Cursores auténticos**: Simulación del cursor parpadeante real

### 🖌️ Principios de Diseño Educativo

- **Coherencia visual** en toda la aplicación con paleta elegante (azul, gris, blanco)
- **Banners informativos** en cada módulo explicando objetivos y contenido
- **Contrastes altos** para facilitar lectura y accesibilidad
- **Espaciado generoso** entre elementos para navegación cómoda  
- **Iconos educativos** que refuerzan el aprendizaje visual
- **Botones accesibles** con colores que transmiten confianza (azul, verde, gris)
- **Experiencia profesional** manteniendo coherencia en toda la interfaz
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

- 🐍 **Python 3.10+** - Lenguaje base del proyecto
- 📊 **Streamlit Cloud** - Framework de aplicaciones web interactivas
- 🪟 **Simulación de PowerShell & CMD** - Entorno seguro de práctica
- 🧠 **JSON** - Almacenamiento de progreso y datos de usuario
- 🏗️ **Arquitectura Modular** - Separación de responsabilidades en 4 módulos principales
- 🔄 **Sistema de Imports Robusto** - Gestión avanzada de dependencias con fallbacks
- 🧩 **Componentes Reutilizables** - Quiz, consola, UI helpers modulares
- 🎨 **CSS Personalizado** - Estilos específicos para simulación de consolas
- 📈 **Sistema de Progreso** - Seguimiento detallado del avance del usuario

### 🚀 Estado Actual del Proyecto

#### ✅ Completadas (2025)
- **Refactorización Major**: Modularización completa de 860+ líneas a 4 módulos especializados
- **Sistema de Registro Robusto**: Prevención de usuarios duplicados con validación completa  
- **Protección de Comandos**: Sistema anti-traducción para mantener referencias en inglés
- **Componentes Interactivos**: Quiz y práctica totalmente funcionales con navegación
- **Simulador de Consolas**: CMD y PowerShell con parser de comandos integrado
- **Contenido Educativo**: Actualización de preguntas con cmdlets reales de PowerShell
- **🎨 Experiencia Visual Auténtica**: Colores y fuentes exactas de consolas originales de Windows
- **Estilos CSS Mejorados**: CMD negro/plata y PowerShell azul/blanco con Consolas 12px
- **Interfaz Realista**: Sin bordes redondeados, cursores auténticos, scrollbars personalizadas

#### 🔧 Arquitectura Técnica
- **Imports Estratégicos**: Sistema de fallback que garantiza disponibilidad de componentes
- **Separación de Concerns**: Cada módulo maneja una responsabilidad específica
- **Reutilización de Código**: Componentes disponibles en múltiples páginas
- **Gestión de Estado**: Seguimiento de progreso integrado en toda la aplicación

#### 📊 Métricas de Mejora
- **87% Reducción**: ui_components.py de 860+ a 180 líneas
- **4 Módulos**: Especialización en quiz, consola, UI helpers y componentes principales  
- **100% Funcional**: Todas las características originales preservadas y mejoradas
- **Modularidad**: Facilita mantenimiento, testing y extensión futura

### 🤝 Contribuciones

¿Quieres mejorar el curso o agregar nuevos módulos? ¡Bienvenido! Puedes abrir un issue o enviar un pull request.

### 📄 Licencia

Este proyecto está bajo la licencia MIT. Puedes usarlo, modificarlo y compartirlo libremente.

### ✨ Autor

Desarrollado por Daniel Mardones — Especialista en python.
