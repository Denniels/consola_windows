"""
Módulo para manejar la información del usuario y certificados
"""

import json
import os
import smtplib
import ssl
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from typing import Dict, Optional
import streamlit as st
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfutils
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
import io

class UserManager:
    """Maneja la información del usuario y certificados"""
    
    def __init__(self, data_file: str = "data/users.json"):
        self.data_file = data_file
        self.users_data = self._load_users_data()
    
    def _load_users_data(self) -> Dict:
        """Carga los datos de usuarios desde el archivo JSON"""
        try:
            base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
            file_path = os.path.join(base_dir, self.data_file)
            
            if os.path.exists(file_path):
                with open(file_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
        except Exception as e:
            st.error(f"Error cargando datos de usuarios: {e}")
        
        return {"users": {}}
    
    def _save_users_data(self):
        """Guarda los datos de usuarios al archivo JSON"""
        try:
            base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
            file_path = os.path.join(base_dir, self.data_file)
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(self.users_data, f, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            st.error(f"Error guardando datos de usuarios: {e}")
            return False
    
    def register_user(self, user_id: str, name: str, lastname: str, email: str):
        """Registra un nuevo usuario"""
        try:
            if "users" not in self.users_data:
                self.users_data["users"] = {}
            self.users_data["users"][user_id] = {
                "name": name,
                "lastname": lastname,
                "email": email,
                "registration_date": datetime.now().isoformat(),
                "certificates_sent": []
            }
            return self._save_users_data()
        except Exception as e:
            st.error(f"Error registrando usuario: {e}")
            return False
    
    def get_user_info(self, user_id: str) -> Optional[Dict]:
        """Obtiene información de un usuario"""
        return self.users_data.get("users", {}).get(user_id)
    
    def is_user_registered(self, user_id: str) -> bool:
        """Verifica si un usuario está registrado"""
        return user_id in self.users_data.get("users", {})
    
    def update_user_info(self, user_id: str, name: str, lastname: str, email: str):
        """Actualiza información de un usuario existente"""
        if self.is_user_registered(user_id):
            self.users_data["users"][user_id].update({
                "name": name,
                "lastname": lastname,
                "email": email,
                "last_updated": datetime.now().isoformat()
            })
            self._save_users_data()

class CertificateGenerator:
    """Genera certificados PDF personalizados"""
    
    def __init__(self):
        self.page_width, self.page_height = landscape(A4)
    
    def generate_certificate(self, user_name: str, user_lastname: str, progress: float) -> bytes:
        """Genera un certificado PDF personalizado"""
        buffer = io.BytesIO()
        
        # Crear el canvas
        c = canvas.Canvas(buffer, pagesize=landscape(A4))
        
        # Configurar colores
        primary_color = HexColor('#059669')  # Verde
        secondary_color = HexColor('#065f46')  # Verde oscuro
        text_color = HexColor('#1f2937')  # Gris oscuro
        
        # Fondo y bordes
        c.setFillColor(HexColor('#f0fdf4'))  # Verde muy claro
        c.rect(0, 0, self.page_width, self.page_height, fill=True, stroke=False)
        
        # Borde decorativo
        c.setStrokeColor(primary_color)
        c.setLineWidth(4)
        c.rect(30, 30, self.page_width - 60, self.page_height - 60, fill=False, stroke=True)
        
        # Borde interior
        c.setLineWidth(1)
        c.rect(50, 50, self.page_width - 100, self.page_height - 100, fill=False, stroke=True)
        
        # Título principal
        c.setFillColor(primary_color)
        c.setFont("Helvetica-Bold", 32)
        c.drawCentredString(self.page_width / 2, self.page_height - 120, "🏆 CERTIFICADO DE COMPLETACIÓN")
        
        # Subtítulo
        c.setFillColor(secondary_color)
        c.setFont("Helvetica-Bold", 24)
        c.drawCentredString(self.page_width / 2, self.page_height - 170, "Curso Interactivo de Consolas Windows")
        
        # Texto de certificación
        c.setFillColor(text_color)
        c.setFont("Helvetica", 16)
        c.drawCentredString(self.page_width / 2, self.page_height - 220, "Se certifica que el usuario ha completado exitosamente")
        c.drawCentredString(self.page_width / 2, self.page_height - 245, "el curso de CMD y PowerShell")
        
        # Nombre del usuario (destacado)
        c.setFillColor(primary_color)
        c.setFont("Helvetica-Bold", 28)
        full_name = f"{user_name} {user_lastname}"
        c.drawCentredString(self.page_width / 2, self.page_height - 300, full_name)
        
        # Información del progreso
        c.setFillColor(text_color)
        c.setFont("Helvetica", 14)
        c.drawCentredString(self.page_width / 2, self.page_height - 340, f"Progreso completado: {progress:.1f}%")
        
        # Fecha
        current_date = datetime.now().strftime("%d de %B de %Y")
        c.drawCentredString(self.page_width / 2, self.page_height - 365, f"Fecha: {current_date}")
        
        # Instructor
        c.setFont("Helvetica-Bold", 14)
        c.drawCentredString(self.page_width / 2, self.page_height - 400, "Instructor: Daniel Mardones")
        
        # Credencial
        c.setFillColor(secondary_color)
        c.setFont("Helvetica", 12)
        c.drawCentredString(self.page_width / 2, self.page_height - 430, "💻 Certificado en CMD y PowerShell")
        
        # Pie de página
        c.setFillColor(HexColor('#6b7280'))
        c.setFont("Helvetica", 10)
        c.drawCentredString(self.page_width / 2, 80, "Curso Interactivo de Consolas Windows - Desarrollado por Daniel Mardones")
        c.drawCentredString(self.page_width / 2, 65, "📚 Especialista en Python y Automatización")
        
        c.save()
        buffer.seek(0)
        return buffer.getvalue()

class EmailSender:
    """Maneja el envío de correos electrónicos"""
    
    def __init__(self):
        # Configuración SMTP (usando Gmail como ejemplo)
        self.smtp_server = "smtp.gmail.com"
        self.smtp_port = 587
        # Estas credenciales deberían estar en variables de entorno en producción
        self.sender_email = os.getenv("SMTP_EMAIL", "tu_email@gmail.com")
        self.sender_password = os.getenv("SMTP_PASSWORD", "tu_app_password")
    
    def send_certificate(self, recipient_email: str, recipient_name: str, 
                        certificate_pdf: bytes) -> bool:
        """Envía el certificado por correo electrónico"""
        try:
            # Crear mensaje
            message = MIMEMultipart()
            message["From"] = self.sender_email
            message["To"] = recipient_email
            message["Subject"] = "🎉 ¡Felicitaciones! Tu Certificado del Curso de Consolas Windows"
            
            # Cuerpo del mensaje
            html_body = f"""
            <html>
            <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
                <div style="max-width: 600px; margin: 0 auto; padding: 20px;">
                    <div style="background: linear-gradient(135deg, #059669, #065f46); color: white; padding: 30px; border-radius: 10px; text-align: center;">
                        <h1 style="margin: 0; font-size: 28px;">🎉 ¡Felicitaciones!</h1>
                        <p style="margin: 10px 0 0 0; font-size: 18px;">Has completado el Curso de Consolas Windows</p>
                    </div>
                    
                    <div style="background: #f8f9fa; padding: 30px; border-radius: 10px; margin: 20px 0;">
                        <h2 style="color: #059669; margin-top: 0;">Hola {recipient_name},</h2>
                        
                        <p>¡Excelente trabajo! Has completado exitosamente el <strong>Curso Interactivo de Consolas Windows</strong>.</p>
                        
                        <p>Durante este curso has aprendido:</p>
                        <ul style="color: #555;">
                            <li>🖤 Comandos básicos e intermedios de CMD</li>
                            <li>🔵 Comandos básicos e intermedios de PowerShell</li>
                            <li>📜 Automatización con scripts</li>
                            <li>⚙️ Administración del sistema</li>
                            <li>🔧 Técnicas avanzadas de consola</li>
                        </ul>
                        
                        <p>Adjunto encontrarás tu <strong>certificado oficial</strong> que acredita tus nuevas habilidades.</p>
                        
                        <div style="background: #e8f5e8; border-left: 4px solid #059669; padding: 15px; margin: 20px 0;">
                            <p style="margin: 0;"><strong>💡 Consejo:</strong> Guarda este certificado y agrégalo a tu perfil profesional en LinkedIn o tu CV.</p>
                        </div>
                    </div>
                    
                    <div style="text-align: center; padding: 20px; background: #fff; border-radius: 10px; border: 1px solid #e5e5e5;">
                        <h3 style="color: #059669; margin-top: 0;">¿Qué sigue ahora?</h3>
                        <p>Continúa practicando y explorando las posibilidades de CMD y PowerShell en tu trabajo diario.</p>
                        <p>¡Sigue aprendiendo y automatizando!</p>
                        
                        <div style="margin-top: 30px; padding-top: 20px; border-top: 1px solid #e5e5e5;">
                            <p style="color: #666; font-size: 14px; margin: 0;">
                                <strong>Daniel Mardones</strong><br>
                                Instructor del curso<br>
                                📧 Especialista en Python y Automatización
                            </p>
                        </div>
                    </div>
                </div>
            </body>
            </html>
            """
            
            message.attach(MIMEText(html_body, "html"))
            
            # Adjuntar certificado PDF
            pdf_attachment = MIMEBase('application', 'octet-stream')
            pdf_attachment.set_payload(certificate_pdf)
            encoders.encode_base64(pdf_attachment)
            pdf_attachment.add_header(
                'Content-Disposition',
                f'attachment; filename="Certificado_Consolas_Windows_{recipient_name.replace(" ", "_")}.pdf"'
            )
            message.attach(pdf_attachment)
            
            # Enviar correo
            context = ssl.create_default_context()
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls(context=context)
                server.login(self.sender_email, self.sender_password)
                server.sendmail(self.sender_email, recipient_email, message.as_string())
            
            return True
            
        except Exception as e:
            st.error(f"Error enviando correo: {e}")
            return False
    
    def is_configured(self) -> bool:
        """Verifica si el servicio de email está configurado"""
        return (self.sender_email != "tu_email@gmail.com" and 
                self.sender_password != "tu_app_password" and
                bool(self.sender_email) and bool(self.sender_password))

def show_user_registration_form():
    """Muestra el formulario de registro de usuario"""
    st.markdown("""
    <div style="background: linear-gradient(135deg, #059669, #065f46); padding: 2rem; border-radius: 10px; margin-bottom: 2rem;">
        <h2 style="color: white; text-align: center; margin: 0;">👋 ¡Bienvenido al Curso de Consolas Windows!</h2>
        <p style="color: #d1fae5; text-align: center; margin: 1rem 0 0 0;">Por favor, completa tus datos para personalizar tu experiencia</p>
    </div>
    """, unsafe_allow_html=True)
    
    with st.form("user_registration"):
        col1, col2 = st.columns(2)
        
        with col1:
            name = st.text_input("👤 Nombre *", placeholder="Ej: Juan")
        
        with col2:
            lastname = st.text_input("👤 Apellido *", placeholder="Ej: Pérez")
        
        email = st.text_input("📧 Correo Electrónico *", placeholder="ejemplo@correo.com")
        
        st.markdown("---")
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            submitted = st.form_submit_button("✅ Comenzar el Curso", type="primary", use_container_width=True)
        
        if submitted:
            if name and lastname and email:
                # Validar email básico
                if "@" in email and "." in email:
                    return {
                        "name": name.strip(),
                        "lastname": lastname.strip(),
                        "email": email.strip().lower()
                    }
                else:
                    st.error("❌ Por favor, ingresa un correo electrónico válido")
            else:
                st.error("❌ Por favor, completa todos los campos obligatorios")
    
    return None

def show_user_profile():
    """Muestra el perfil del usuario en la barra lateral"""
    if 'user_manager' in st.session_state and 'progress_tracker' in st.session_state:
        user_id = st.session_state.progress_tracker.get_user_id()
        user_info = st.session_state.user_manager.get_user_info(user_id)
        
        if user_info:
            st.sidebar.markdown("---")
            st.sidebar.markdown("### 👤 Perfil de Usuario")
            st.sidebar.markdown(f"**Nombre:** {user_info['name']} {user_info['lastname']}")
            st.sidebar.markdown(f"**Email:** {user_info['email']}")
            
            # Botón para editar perfil
            if st.sidebar.button("✏️ Editar Perfil"):
                st.session_state.show_edit_profile = True

def show_registration_form():
    """Muestra el formulario de registro de usuario"""
    st.markdown("## 👤 Registro de Usuario")
    st.markdown("**Bienvenido al Curso Interactivo de Consolas Windows**")
    st.markdown("Para personalizar tu experiencia y generar tu certificado, necesitamos algunos datos:")
    
    with st.form("user_registration"):
        col1, col2 = st.columns(2)
        
        with col1:
            name = st.text_input("Nombre *", placeholder="Ej: Juan")
            
        with col2:
            lastname = st.text_input("Apellido *", placeholder="Ej: Pérez")
        
        email = st.text_input("Correo Electrónico *", placeholder="Ej: juan.perez@email.com")
        
        st.markdown("*Campos obligatorios")
        st.markdown("📧 Tu correo será usado únicamente para enviarte el certificado al completar el curso.")
        
        submitted = st.form_submit_button("📝 Comenzar Curso", type="primary")
        
        if submitted:
            if name and lastname and email:
                # Validar email básico
                if "@" in email and "." in email:
                    # Obtener ID del usuario desde progress_tracker
                    if 'progress_tracker' in st.session_state:
                        user_id = st.session_state.progress_tracker.get_user_id()
                        # Si el usuario ya está registrado, no mostrar el formulario
                        if st.session_state.user_manager.is_user_registered(user_id):
                            st.success(f"¡Ya estás registrado, {name}!")
                            st.rerun()
                        elif st.session_state.user_manager.register_user(user_id, name, lastname, email):
                            st.success(f"✅ ¡Registro exitoso! Bienvenido/a {name} {lastname}")
                            st.balloons()
                            st.rerun()
                        else:
                            st.error("❌ Error en el registro. Verifica permisos de escritura o formato de datos.")
                    else:
                        st.error("❌ Error: Sistema de progreso no disponible.")
                else:
                    st.error("❌ Por favor ingresa un correo electrónico válido.")
            else:
                st.error("❌ Por favor completa todos los campos obligatorios.")

def check_user_registration():
    """Verifica si el usuario está registrado y muestra el formulario si es necesario"""
    if 'user_manager' not in st.session_state:
        st.session_state.user_manager = UserManager()
    
    if 'progress_tracker' in st.session_state:
        user_id = st.session_state.progress_tracker.get_user_id()
        
        if not st.session_state.user_manager.is_user_registered(user_id):
            show_registration_form()
            return False
        else:
            # Usuario registrado, mostrar mensaje de bienvenida en sidebar
            user_info = st.session_state.user_manager.get_user_info(user_id)
            if user_info:
                st.sidebar.success(f"👋 Hola {user_info['name']}!")
        return True
    else:
        st.error("❌ Sistema de progreso no disponible.")
        return False
