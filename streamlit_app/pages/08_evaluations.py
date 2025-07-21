"""
Módulo 08: Evaluaciones Interactivas
"""

import streamlit as st
import sys
import os
from datetime import datetime

# Agregar paths necesarios
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'utils'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'components'))

from progress_tracker import create_section_header, create_info_card
from ui_components import (
    QuizComponent, ProgressCard, create_learning_objective_card, create_tip_card
)
from user_manager import CertificateGenerator, EmailSender

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
        progress_data = {
            'sections': st.session_state.progress_tracker.progress_data.get('user_progress', {}).get(st.session_state.progress_tracker.get_user_id(), {})
        }
        ProgressCard.render(progress_data)
    
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
    
    if quiz.render(key_suffix="evaluation_cmd_advanced"):
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
    
    if quiz.render(key_suffix="evaluation_ps_advanced"):
        if 'progress_tracker' in st.session_state:
            st.session_state.progress_tracker.add_quiz_score("powershell_advanced", quiz.score, 100)

def render_certificate_section():
    """Renderiza la sección de certificado"""
    
    st.markdown("## 🏆 Certificado de Completación")
    
    if 'progress_tracker' in st.session_state:
        # Obtener el progreso usando el mismo método que la barra lateral
        overall_progress = st.session_state.progress_tracker.get_overall_progress()
        
        # También obtener el progreso basado en módulos completados
        modules_progress = st.session_state.progress_tracker.calculate_overall_progress()
        
        # Usar el progreso más alto para ser justo con el usuario
        final_progress = max(overall_progress, modules_progress)
        
        # Mostrar progreso actual
        col1, col2 = st.columns([2, 1])
        with col1:
            st.progress(final_progress / 100)
            st.caption(f"Progreso actual: {final_progress:.1f}%")
            
            # Mostrar información de debug
            with st.expander("📊 Detalles del progreso", expanded=False):
                st.write(f"**Progreso por quizzes:** {overall_progress:.1f}%")
                st.write(f"**Progreso por módulos:** {modules_progress:.1f}%")
                st.write(f"**Progreso final (usado):** {final_progress:.1f}%")
        
        with col2:
            if final_progress >= 70:
                st.success("✅ Elegible para certificado")
            else:
                remaining = 70 - final_progress
                st.warning(f"📈 Necesitas {remaining:.1f}% más")
        
        # Modo de prueba para desarrolladores
        st.markdown("---")
        with st.expander("🔧 Modo Desarrollador (Para Pruebas)", expanded=False):
            st.warning("⚠️ Este modo es solo para pruebas de desarrollo")
            test_progress = st.slider("Simular progreso para prueba", 0, 100, int(final_progress), 5)
            
            col_test1, col_test2 = st.columns(2)
            with col_test1:
                test_certificate = st.button("🧪 Probar Certificado", type="secondary")
            with col_test2:
                force_show = st.checkbox("Forzar mostrar certificado", value=False)
            
            if test_certificate or force_show:
                st.info(f"🧪 Modo de prueba activado - Simulando progreso: {test_progress}%")
                # Usar el progreso de prueba en lugar del real
                final_progress = test_progress
        
        st.markdown("---")
        
        if final_progress >= 70:
            st.success("🎉 ¡Felicitaciones! Has completado suficiente del curso para obtener tu certificado.")
            
            # Verificar si el usuario está registrado
            if 'user_manager' in st.session_state:
                user_id = st.session_state.progress_tracker.get_user_id()
                user_info = st.session_state.user_manager.get_user_info(user_id)
                
                if user_info:
                    # Vista previa del certificado
                    current_date = datetime.now().strftime("%d de %B de %Y")
                    full_name = f"{user_info['name']} {user_info['lastname']}"
                    
                    # Crear la vista previa del certificado usando componentes Streamlit más simples
                    st.markdown("### 🏆 Vista Previa de tu Certificado")
                    
                    # Container principal del certificado - CSS muy simple
                    st.markdown("""
                    <div style="
                        background: linear-gradient(45deg, #f0fdf4, #ecfdf5);
                        border: 3px solid #059669;
                        border-radius: 10px;
                        padding: 30px;
                        margin: 20px 0;
                        text-align: center;
                    ">
                        <h1 style="color: #059669; margin: 10px 0;">🏆 CERTIFICADO DE COMPLETACIÓN</h1>
                        <h2 style="color: #065f46; margin: 10px 0;">Curso Interactivo de Consolas Windows</h2>
                        <p style="color: #374151; margin: 20px 0;">
                            Se certifica que el usuario ha completado exitosamente<br>
                            el curso de <strong>CMD y PowerShell</strong>
                        </p>
                        <div style="
                            background: white;
                            border: 2px solid #059669;
                            border-radius: 8px;
                            padding: 20px;
                            margin: 20px auto;
                            max-width: 400px;
                        ">
                            <h3 style="color: #059669; margin: 0;">{full_name}</h3>
                        </div>
                    </div>
                    """.format(full_name=full_name), unsafe_allow_html=True)
                    
                    # Información adicional con componentes nativos
                    col1, col2 = st.columns(2)
                    with col1:
                        st.metric("📊 Progreso Completado", f"{final_progress:.1f}%")
                    with col2:
                        st.metric("📅 Fecha de Completación", current_date)
                    
                    # Información del instructor
                    st.markdown("**Instructor:** Daniel Mardones  \n💻 Especialista en Python y Administración de Sistemas")
                    
                    
                    # Botones de acción
                    st.markdown("### 🎯 Acciones disponibles")
                    st.markdown("Descarga tu certificado en formato PDF o recíbelo directamente en tu correo electrónico:")
                    
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        if st.button("📥 Descargar Certificado", type="primary", use_container_width=True):
                            try:
                                with st.spinner("📄 Generando certificado PDF..."):
                                    generator = CertificateGenerator()
                                    certificate_pdf = generator.generate_certificate(
                                    user_info['name'], 
                                    user_info['lastname'], 
                                    final_progress
                                )
                                
                                if certificate_pdf:
                                    st.success("✅ Certificado generado correctamente")
                                    st.download_button(
                                        label="💾 Descargar PDF",
                                        data=certificate_pdf,
                                        file_name=f"Certificado_Consolas_Windows_{user_info['name']}_{user_info['lastname']}.pdf",
                                        mime="application/pdf",
                                        use_container_width=True,
                                        key="download_cert_btn"
                                    )
                                else:
                                    st.error("❌ Error: No se pudo generar el certificado")
                                
                            except ImportError as e:
                                st.error("❌ Error: Falta la librería ReportLab. Instálala con: pip install reportlab")
                                st.code("pip install reportlab")
                            except Exception as e:
                                st.error(f"❌ Error generando certificado: {str(e)}")
                                st.info("💡 Intenta actualizar la página y volver a intentar")
                                
                                # Mostrar información de debug
                                with st.expander("🔍 Información de Debug"):
                                    st.code(f"""
Tipo de error: {type(e).__name__}
Mensaje: {str(e)}
Usuario: {user_info['name']} {user_info['lastname']}
Progreso: {final_progress}%
                                    """)
                    
                    with col2:
                        if st.button("📧 Enviar por Correo", type="secondary", use_container_width=True):
                            try:
                                # Generar certificado
                                generator = CertificateGenerator()
                                certificate_pdf = generator.generate_certificate(
                                    user_info['name'], 
                                    user_info['lastname'], 
                                    final_progress
                                )
                                
                                # Configurar envío de email
                                email_sender = EmailSender()
                                
                                if email_sender.is_configured():
                                    with st.spinner("📧 Enviando certificado..."):
                                        success = email_sender.send_certificate(
                                            user_info['email'],
                                            f"{user_info['name']} {user_info['lastname']}",
                                            certificate_pdf
                                        )
                                    
                                    if success:
                                        st.success(f"✅ ¡Certificado enviado a {user_info['email']}!")
                                        
                                        # Registrar envío
                                        if "certificates_sent" not in user_info:
                                            user_info["certificates_sent"] = []
                                        user_info["certificates_sent"].append({
                                            "date": datetime.now().isoformat(),
                                            "progress": overall_progress
                                        })
                                        st.session_state.user_manager._save_users_data()
                                    else:
                                        st.error("❌ Error enviando el certificado. Intenta más tarde.")
                                else:
                                    st.warning("""
                                    ⚠️ El servicio de correo no está configurado.
                                    
                                    Para configurar el envío automático de certificados:
                                    1. Configura las variables de entorno SMTP_EMAIL y SMTP_PASSWORD
                                    2. Usa una contraseña de aplicación de Gmail
                                    """)
                                
                            except Exception as e:
                                st.error(f"Error enviando certificado: {e}")
                    
                    # Información adicional
                    st.markdown("---")
                    st.markdown("""
                    ### 📋 Información del Certificado
                    
                    Tu certificado incluye:
                    - ✅ Tu nombre completo
                    - ✅ Fecha de completación
                    - ✅ Porcentaje de progreso alcanzado
                    - ✅ Firma del instructor
                    - ✅ Validación oficial del curso
                    
                    💡 **Consejo:** Agrega este certificado a tu perfil de LinkedIn o CV para demostrar tus habilidades en administración de sistemas Windows.
                    """)
                    
                else:
                    st.error("❌ Error: No se encontró información del usuario. Por favor, reinicia la aplicación.")
            else:
                st.error("❌ Error: Sistema de usuarios no inicializado.")
        else:
            st.info(f"""
            📚 **Para obtener tu certificado necesitas completar al menos 70% del curso.**
            
            **Tu progreso actual:** {overall_progress:.1f}%
            **Te falta:** {70 - overall_progress:.1f}%
            
            **Sugerencias para mejorar tu progreso:**
            - Completa todos los quizzes con al menos 70% de acierto
            - Revisa los módulos que no has visitado
            - Practica con los ejercicios interactivos
            """)
    else:
        st.error("❌ Sistema de progreso no disponible")

if __name__ == "__main__":
    render_page()
