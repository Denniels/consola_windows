"""
Módulo 06: Automatización y Tareas Programadas (CMD Avanzado)
"""

import streamlit as st
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'utils'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'components'))

from progress_tracker import create_section_header, create_info_card
from ui_components import (
    ConsoleSimulator, QuizComponent, CommandPracticeComponent,
    create_learning_objective_card, create_tip_card, create_code_example
)

def render_page():
    """Renderiza la página de CMD avanzado"""
    
    # Header principal
    create_section_header(
        title="Automatización y Tareas Programadas (CMD)",
        description="Crea scripts avanzados y automatiza tareas del sistema con CMD",
        icon="⚫"
    )
    
    # Objetivos de aprendizaje
    objectives = [
        "Crear scripts batch complejos con estructuras de control",
        "Automatizar backups y mantenimiento del sistema",
        "Programar tareas con schtasks",
        "Implementar logging y manejo de errores",
        "Crear herramientas de monitoreo básicas"
    ]
    create_learning_objective_card(objectives)
    
    # Tabs principales
    tab1, tab2, tab3, tab4 = st.tabs(["📚 Teoría", "🎯 Práctica", "🧩 Cuestionario", "📖 Referencia"])
    
    with tab1:
        render_theory_section()
    
    with tab2:
        render_practice_section()
    
    with tab3:
        render_quiz_section()
    
    with tab4:
        render_reference_section()

def render_theory_section():
    """Renderiza la sección de teoría"""
    
    st.markdown("## � Scripts Batch Avanzados")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### Estructuras de Control")
        st.markdown("""
        Los scripts batch avanzados incluyen estructuras de control que permiten tomar decisiones y repetir acciones automáticamente.
        """)
        
        create_code_example(
            "Estructura IF-ELSE",
            """@echo off
if exist "archivo.txt" (
    echo El archivo existe
    type archivo.txt
) else (
    echo El archivo no existe
    echo Creando archivo...
    echo Contenido inicial > archivo.txt
)""",
            "batch",
            "IF permite ejecutar comandos basándose en condiciones"
        )
        
        create_code_example(
            "Bucle FOR",
            """@echo off
rem Procesar todos los archivos .txt
for %%f in (*.txt) do (
    echo Procesando: %%f
    copy "%%f" "backup\\"
)

rem Iterar números del 1 al 10
for /L %%i in (1,1,10) do (
    echo Número: %%i
)""",
            "batch",
            "FOR permite repetir acciones para conjuntos de archivos o números"
        )
        
        st.markdown("### Automatización de Backups")
        st.markdown("""
        Un caso común de automatización es crear backups automáticos de archivos importantes.
        """)
        
        create_code_example(
            "Script de backup automático",
            """@echo off
setlocal EnableDelayedExpansion

rem Configuración
set SOURCE=C:\\Documentos\\Importantes
set BACKUP_DIR=D:\\Backups
set DATE_STAMP=%DATE:~6,4%-%DATE:~3,2%-%DATE:~0,2%
set BACKUP_FOLDER=%BACKUP_DIR%\\Backup_%DATE_STAMP%

rem Crear carpeta de backup
if not exist "%BACKUP_FOLDER%" mkdir "%BACKUP_FOLDER%"

rem Copiar archivos
echo Iniciando backup en %BACKUP_FOLDER%...
xcopy "%SOURCE%" "%BACKUP_FOLDER%" /E /H /Y

rem Log del resultado
echo %DATE% %TIME% - Backup completado >> %BACKUP_DIR%\\backup.log

echo Backup completado exitosamente!
pause""",
            "batch",
            "Script completo para backup automatizado con logging"
        )
        
        st.markdown("### Tareas Programadas")
        st.markdown("""
        Windows incluye `schtasks` para programar la ejecución automática de scripts.
        """)
        
        create_code_example(
            "Programar tareas con schtasks",
            """rem Crear tarea que se ejecuta diariamente a las 2:00 AM
schtasks /create /tn "BackupDiario" /tr "C:\\Scripts\\backup.bat" /sc daily /st 02:00

rem Crear tarea que se ejecuta cada hora
schtasks /create /tn "Monitoreo" /tr "C:\\Scripts\\monitor.bat" /sc hourly

rem Listar todas las tareas programadas
schtasks /query

rem Eliminar una tarea
schtasks /delete /tn "BackupDiario" /f""",
            "batch",
            "schtasks permite automatizar completamente la ejecución de scripts"
        )
    
    with col2:
        create_tip_card(
            "💡 setlocal EnableDelayedExpansion",
            "Habilita la expansión retardada de variables, útil para variables que cambian dentro de bucles.",
            "info"
        )
        
        create_tip_card(
            "⚠️ Paths con espacios",
            "Siempre usa comillas dobles alrededor de rutas que puedan contener espacios.",
            "warning"
        )
        
        create_tip_card(
            "🔄 Logging",
            "Incluye logging en tus scripts para poder diagnosticar problemas cuando se ejecuten automáticamente.",
            "success"
        )
        
        st.markdown("### Códigos de Error")
        st.code("""
%ERRORLEVEL% = 0  → Éxito
%ERRORLEVEL% ≠ 0  → Error

if %ERRORLEVEL% neq 0 (
    echo Error detectado!
    goto :error
)
        """)

def render_practice_section():
    """Renderiza la sección de práctica"""
    
    st.markdown("## 🏆 Ejercicios Prácticos")
    
    # Simulador de consola
    st.markdown("### 🖤 Consola CMD - Scripts Avanzados")
    cmd_simulator = ConsoleSimulator("cmd")
    cmd_simulator.render(key_suffix="cmd_advanced")
    
    st.markdown("---")
    st.markdown("## 🎯 Ejercicios de Automatización")
    
    # Definir ejercicios prácticos
    practice_commands = [
        {
            "descripcion": "Verifica si existe un archivo llamado 'test.txt' en el directorio actual",
            "ejemplo": "if exist test.txt echo Archivo encontrado",
            "comando": "if",
            "tipo_consola": "cmd",
            "pista": "Usa 'if exist nombre_archivo comando' para verificar existencia",
            "solucion": "if exist test.txt echo Archivo encontrado - Verifica y ejecuta si existe"
        },
        {
            "descripcion": "Lista todas las tareas programadas del sistema",
            "ejemplo": "schtasks /query",
            "comando": "schtasks",
            "tipo_consola": "cmd",
            "pista": "schtasks /query muestra todas las tareas programadas",
            "solucion": "schtasks /query - Lista tareas del programador de Windows"
        },
        {
            "descripcion": "Crea una variable con la fecha actual y muéstrala",
            "ejemplo": "set fecha=%DATE% && echo %fecha%",
            "comando": "set",
            "tipo_consola": "cmd",
            "pista": "Usa && para ejecutar múltiples comandos en secuencia",
            "solucion": "set fecha=%DATE% && echo %fecha% - Almacena y muestra fecha"
        },
        {
            "descripcion": "Copia todos los archivos .txt a una carpeta llamada 'backup'",
            "ejemplo": "xcopy *.txt backup\\ /Y",
            "comando": "xcopy",
            "tipo_consola": "cmd",
            "pista": "xcopy es más potente que copy para múltiples archivos",
            "solucion": "xcopy *.txt backup\\ /Y - Copia con sobrescritura automática"
        },
        {
            "descripcion": "Muestra el nivel de error del último comando ejecutado",
            "ejemplo": "echo %ERRORLEVEL%",
            "comando": "echo",
            "tipo_consola": "cmd",
            "pista": "%ERRORLEVEL% contiene el código de retorno del último comando",
            "solucion": "echo %ERRORLEVEL% - 0 = éxito, ≠0 = error"
        }
    ]
    
    # Componente de práctica
    practice_component = CommandPracticeComponent(practice_commands)
    practice_component.render(key_suffix="cmd_advanced_practice")

def render_quiz_section():
    """Renderiza la sección de quiz"""
    
    st.markdown("## 🧩 Evaluación: CMD Avanzado")
    
    # Definir preguntas del quiz
    quiz_questions = [
        {
            "pregunta": "¿Qué comando usas para programar una tarea que se ejecute diariamente?",
            "opciones": ["at", "schedule", "schtasks", "timer"],
            "respuesta_correcta": "schtasks",
            "explicacion": "schtasks es la herramienta moderna para programar tareas en Windows."
        },
        {
            "pregunta": "¿Cuál es el valor de %ERRORLEVEL% cuando un comando se ejecuta exitosamente?",
            "opciones": ["1", "0", "-1", "null"],
            "respuesta_correcta": "0",
            "explicacion": "Un ERRORLEVEL de 0 indica que el comando se ejecutó sin errores."
        },
        {
            "pregunta": "¿Qué hace 'setlocal EnableDelayedExpansion' en un script?",
            "opciones": [
                "Acelera la ejecución",
                "Habilita variables que cambian en bucles",
                "Evita errores de sintaxis",
                "Oculta la salida de comandos"
            ],
            "respuesta_correcta": "Habilita variables que cambian en bucles",
            "explicacion": "Permite que las variables se expandan correctamente dentro de bucles FOR."
        },
        {
            "pregunta": "¿Cuál es la diferencia principal entre 'copy' y 'xcopy'?",
            "opciones": [
                "xcopy es más rápido",
                "copy solo funciona con archivos individuales",
                "xcopy puede copiar directorios completos",
                "No hay diferencias"
            ],
            "respuesta_correcta": "xcopy puede copiar directorios completos",
            "explicacion": "xcopy es más avanzado y puede manejar estructuras de directorios completas."
        }
    ]
    
    # Componente de quiz
    quiz_component = QuizComponent(quiz_questions)
    quiz_component.render(key_suffix="cmd_advanced_quiz")

def render_reference_section():
    """Renderiza la sección de referencia"""
    
    st.markdown("## 📖 Referencia Rápida")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Estructuras de Control")
        st.code("""
rem IF básico
if condition comando

rem IF-ELSE
if condition (
    comandos
) else (
    otros comandos
)

rem Comparaciones
if "%var%"=="valor" comando
if exist archivo comando
if %num% gtr 5 comando

rem FOR archivos
for %%f in (*.txt) do comando

rem FOR números
for /L %%i in (1,1,10) do comando
        """, language="batch")
        
        st.markdown("### Programación de Tareas")
        st.code("""
rem Crear tarea diaria
schtasks /create /tn "Nombre" /tr "script.bat" /sc daily

rem Crear tarea semanal
schtasks /create /tn "Nombre" /tr "script.bat" /sc weekly

rem Listar tareas
schtasks /query

rem Eliminar tarea
schtasks /delete /tn "Nombre" /f

rem Ejecutar tarea inmediatamente
schtasks /run /tn "Nombre"
        """, language="batch")
    
    with col2:
        st.markdown("### Comandos de Sistema")
        st.code("""
xcopy source dest /E /H /Y  - Copia completa
robocopy src dest /MIR     - Backup espejo
forfiles /m *.log /c "cmd /c del @path" - Eliminar archivos viejos

tasklist                   - Listar procesos
taskkill /im proceso.exe   - Terminar proceso
net start servicio        - Iniciar servicio
net stop servicio         - Detener servicio

systeminfo                - Info del sistema
wmic os get caption        - Versión de Windows
        """, language="batch")
        
        st.markdown("### Manejo de Errores")
        st.code("""
comando
if %ERRORLEVEL% neq 0 (
    echo Error en comando
    goto :error
)

:error
echo Se produjo un error
exit /b 1

rem Logging básico
echo %DATE% %TIME% - Mensaje >> log.txt
        """, language="batch")
    
    create_tip_card(
        "🚀 Próximo paso",
        "Con CMD avanzado dominado, estarás listo para automatizar prácticamente cualquier tarea en Windows.",
        "success"
    )

if __name__ == "__main__":
    render_page()
