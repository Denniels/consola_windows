"""
Módulo 08: Evaluaciones Interactivas
"""

import streamlit as st
import sys
import os

# Agregar paths necesarios
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'utils'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'components'))

from progress_tracker import create_section_header, create_info_card
from ui_components import (
    QuizComponent, ProgressCard, create_learning_objective_card, create_tip_card
)

def render_page():
    """Renderiza la página de evaluaciones"""
    
    # Header principal
    create_section_header(
        title="Evaluaciones Interactivas",
        description="Evalúa tu conocimiento en CMD y PowerShell con quizzes y ejercicios prácticos",
        icon="📊"
    )
    
    # Mostrar progreso del usuario
    if 'progress_tracker' in st.session_state:
        progress_card = ProgressCard(st.session_state.progress_tracker)
        progress_card.render()
    
    # Pestañas para diferentes tipos de evaluación
    tab1, tab2, tab3, tab4 = st.tabs(["🎯 Evaluación General", "⚫ Quiz CMD", "🔵 Quiz PowerShell", "🏆 Certificado"])
    
    with tab1:
        render_general_evaluation()
    
    with tab2:
        render_cmd_quiz()
    
    with tab3:
        render_powershell_quiz()
    
    with tab4:
        render_certificate_section()
    
    # Marcar progreso
    if 'progress_tracker' in st.session_state:
        st.session_state.progress_tracker.update_module_progress("08_evaluations", "evaluations_viewed")

def render_general_evaluation():
    """Renderiza la evaluación general"""
    
    st.markdown("## 🎯 Evaluación Integral: CMD y PowerShell")
    
    # Quiz combinado
    mixed_questions = [
        {
            "pregunta": "¿Cuál es el comando CMD para listar archivos?",
            "opciones": ["ls", "dir", "list", "show"],
            "respuesta_correcta": "dir",
            "explicacion": "El comando 'dir' en CMD lista archivos y directorios."
        },
        {
            "pregunta": "¿Cuál es el cmdlet PowerShell equivalente a 'dir'?",
            "opciones": ["Get-Files", "Get-ChildItem", "List-Items", "Show-Directory"],
            "respuesta_correcta": "Get-ChildItem",
            "explicacion": "Get-ChildItem es el cmdlet de PowerShell para listar contenido."
        },
        {
            "pregunta": "¿Qué comando usarías para limpiar la pantalla en ambas consolas?",
            "opciones": ["cls", "clear", "clean", "clr"],
            "respuesta_correcta": "cls",
            "explicacion": "'cls' funciona tanto en CMD como en PowerShell (aunque en PS también puedes usar Clear-Host)."
        },
        {
            "pregunta": "¿Cuál es la principal ventaja de PowerShell sobre CMD?",
            "opciones": [
                "Es más rápido",
                "Trabaja con objetos en lugar de solo texto",
                "Tiene mejor interfaz gráfica",
                "Consume menos recursos"
            ],
            "respuesta_correcta": "Trabaja con objetos en lugar de solo texto",
            "explicacion": "PowerShell es orientado a objetos, lo que permite mayor funcionalidad."
        },
        {
            "pregunta": "¿Cómo obtienes ayuda en PowerShell?",
            "opciones": ["Get-Help", "Help", "?", "Todas las anteriores"],
            "respuesta_correcta": "Todas las anteriores",
            "explicacion": "Get-Help, Help y ? son formas válidas de obtener ayuda en PowerShell."
        }
    ]

    quiz = QuizComponent(mixed_questions)
    
    if quiz.render(key_suffix="general_eval"):
        if 'progress_tracker' in st.session_state:
            st.session_state.progress_tracker.add_quiz_score("08_evaluations", quiz.score, 100)

def render_cmd_quiz():
    """Renderiza el quiz específico de CMD"""
    
    st.markdown("## ⚫ Quiz Avanzado de CMD")
    
    cmd_questions = [
        {
            "pregunta": "¿Qué parámetro de 'dir' muestra archivos ocultos?",
            "opciones": ["/a", "/h", "/hidden", "/all"],
            "respuesta_correcta": "/a",
            "explicacion": "El parámetro /a (attributes) con modificadores puede mostrar archivos ocultos."
        },
        {
            "pregunta": "¿Cómo rediriges la salida de un comando a un archivo en CMD?",
            "opciones": ["comando > archivo.txt", "comando >> archivo.txt", "comando | archivo.txt", "comando -> archivo.txt"],
            "respuesta_correcta": "comando > archivo.txt",
            "explicacion": "El símbolo > redirige la salida a un archivo."
        },
        {
            "pregunta": "¿Qué comando usas para ver el contenido de un archivo de texto?",
            "opciones": ["read", "type", "show", "cat"],
            "respuesta_correcta": "type",
            "explicacion": "'type' muestra el contenido de archivos de texto en CMD."
        },
        {
            "pregunta": "¿Cómo eliminas un directorio con contenido usando CMD?",
            "opciones": ["rmdir /s directorio", "del /s directorio", "remove directorio", "delete directorio"],
            "respuesta_correcta": "rmdir /s directorio",
            "explicacion": "rmdir con el parámetro /s elimina directorios con contenido."
        }
    ]

    quiz = QuizComponent(cmd_questions)
    
    if quiz.render(key_suffix="cmd_advanced_quiz"):
        if 'progress_tracker' in st.session_state:
            st.session_state.progress_tracker.add_quiz_score("cmd_advanced", quiz.score, 100)

def render_powershell_quiz():
    """Renderiza el quiz específico de PowerShell"""
    
    st.markdown("## 🔵 Quiz Avanzado de PowerShell")
    
    ps_questions = [
        {
            "pregunta": "¿Qué símbolo se usa para pipeline en PowerShell?",
            "opciones": [">", "|", "&", ">>"],
            "respuesta_correcta": "|",
            "explicacion": "El símbolo | (pipe) conecta cmdlets en PowerShell."
        },
        {
            "pregunta": "¿Cómo filtras procesos que usan más de 100MB de memoria?",
            "opciones": [
                "Get-Process | Where-Object {$_.WorkingSet -gt 100MB}",
                "Get-Process -Memory 100MB",
                "Get-Process | Filter-Memory 100MB",
                "Get-Process | Select-Memory 100MB"
            ],
            "respuesta_correcta": "Get-Process | Where-Object {$_.WorkingSet -gt 100MB}",
            "explicacion": "Where-Object filtra objetos basado en propiedades."
        },
        {
            "pregunta": "¿Qué cmdlet usas para detener un servicio?",
            "opciones": ["Stop-Service", "End-Service", "Kill-Service", "Terminate-Service"],
            "respuesta_correcta": "Stop-Service",
            "explicacion": "Stop-Service detiene servicios de Windows."
        },
        {
            "pregunta": "¿Cómo exportas una lista de procesos a CSV?",
            "opciones": [
                "Get-Process | Export-Csv procesos.csv",
                "Get-Process | Out-Csv procesos.csv",
                "Get-Process | Save-Csv procesos.csv",
                "Get-Process | Write-Csv procesos.csv"
            ],
            "respuesta_correcta": "Get-Process | Export-Csv procesos.csv",
            "explicacion": "Export-Csv convierte objetos a formato CSV."
        }
    ]

    quiz = QuizComponent(ps_questions)
    
    if quiz.render(key_suffix="ps_advanced_quiz"):
        if 'progress_tracker' in st.session_state:
            st.session_state.progress_tracker.add_quiz_score("powershell_advanced", quiz.score, 100)

def render_certificate_section():
    """Renderiza la sección de certificado"""
    
    st.markdown("## 🏆 Certificado de Completación")
    
    if 'progress_tracker' in st.session_state:
        overall_progress = st.session_state.progress_tracker.calculate_overall_progress()
        
        if overall_progress >= 70:
            st.success("🎉 ¡Felicitaciones! Has completado suficiente del curso para obtener tu certificado.")
            
            st.markdown(f"""
            <div style="
                border: 3px solid #10b981;
                border-radius: 10px;
                padding: 2rem;
                text-align: center;
                background: linear-gradient(135deg, #ecfdf5, #f0fdf4);
                margin: 2rem 0;
            ">
                <h2 style="color: #065f46; margin-bottom: 1rem;">
                    🏆 CERTIFICADO DE COMPLETACIÓN
                </h2>
                <h3 style="color: #047857;">
                    Curso Interactivo de Consolas Windows
                </h3>
                <p style="font-size: 1.2rem; color: #065f46; margin: 1rem 0;">
                    Se certifica que el usuario ha completado exitosamente<br>
                    el curso de <strong>CMD y PowerShell</strong>
                </p>
                <p style="color: #047857;">
                    <strong>Progreso completado:</strong> {overall_progress:.1f}%<br>
                    <strong>Fecha:</strong> {st.session_state.get('current_date', 'Hoy')}<br>
                    <strong>Instructor:</strong> Daniel Mardones
                </p>
                <div style="margin-top: 2rem;">
                    <strong style="color: #065f46;">🖥️ CMD & PowerShell Certified</strong>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button("📄 Descargar Certificado (PDF)"):
                st.info("🚧 Función de descarga en desarrollo. Por ahora puedes hacer captura de pantalla del certificado.")
        
        else:
            st.warning(f"Necesitas completar al menos 70% del curso para obtener el certificado. Tu progreso actual: {overall_progress:.1f}%")
            
            create_tip_card(
                "📚 ¿Cómo obtener el certificado?",
                "Completa los módulos de teoría, realiza las prácticas y aprueba los quizzes para alcanzar el 70% de progreso necesario.",
                "info"
            )
    
    else:
        st.error("No se pudo cargar el progreso del usuario.")

if __name__ == "__main__":
    render_page()
