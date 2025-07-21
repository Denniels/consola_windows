# Configuración de Email para el sistema de certificados
# Copia este archivo como email_config.py y configura tus credenciales

# Configuración del servidor SMTP
SMTP_SERVER = "smtp.gmail.com"  # Para Gmail
SMTP_PORT = 587
SMTP_USE_TLS = True

# Credenciales del remitente
EMAIL_SENDER = "tu_correo@gmail.com"
EMAIL_PASSWORD = "tu_contraseña_de_aplicación"  # Usa contraseña de aplicación para Gmail

# Configuración del mensaje
EMAIL_FROM_NAME = "Curso CMD y PowerShell"
EMAIL_SUBJECT = "🏆 ¡Felicitaciones! Tu Certificado de Completación"

# Plantilla HTML del correo
EMAIL_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Certificado de Completación</title>
</head>
<body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
    <div style="max-width: 600px; margin: 0 auto; padding: 20px;">
        <h1 style="color: #2c3e50; text-align: center;">🏆 ¡Felicitaciones!</h1>
        
        <p>Estimado/a <strong>{name} {lastname}</strong>,</p>
        
        <p>Es un placer informarte que has completado exitosamente el <strong>Curso Interactivo de Consolas Windows (CMD y PowerShell)</strong>.</p>
        
        <div style="background-color: #f8f9fa; padding: 20px; border-radius: 8px; margin: 20px 0;">
            <h3 style="margin-top: 0; color: #28a745;">📊 Detalles de tu logro:</h3>
            <ul>
                <li><strong>Progreso completado:</strong> {progress:.1f}%</li>
                <li><strong>Fecha de completación:</strong> {completion_date}</li>
                <li><strong>Duración del curso:</strong> 9 módulos interactivos</li>
                <li><strong>Habilidades adquiridas:</strong> Administración avanzada de sistemas Windows</li>
            </ul>
        </div>
        
        <p>Adjunto a este correo encontrarás tu <strong>certificado oficial en formato PDF</strong>, el cual puedes:</p>
        
        <ul>
            <li>📎 Agregar a tu perfil de LinkedIn</li>
            <li>📄 Incluir en tu CV o portafolio profesional</li>
            <li>🎯 Usar como evidencia de tus habilidades técnicas</li>
        </ul>
        
        <div style="background-color: #e3f2fd; padding: 15px; border-radius: 8px; margin: 20px 0;">
            <p style="margin: 0;"><strong>💡 Consejo profesional:</strong> Las habilidades en administración de sistemas Windows son altamente valoradas en el mercado laboral. ¡Sigue practicando y explorando nuevas tecnologías!</p>
        </div>
        
        <p>Gracias por tu dedicación y esfuerzo durante el curso. Esperamos que continues desarrollando tus habilidades técnicas.</p>
        
        <div style="text-align: center; margin: 30px 0;">
            <p><strong>Daniel Mardones</strong><br>
            Desarrollador del Curso<br>
            Especialista en Python y Administración de Sistemas</p>
        </div>
        
        <hr style="border: none; border-top: 1px solid #eee; margin: 30px 0;">
        
        <p style="font-size: 12px; color: #666; text-align: center;">
            Este certificado fue generado automáticamente por el sistema del Curso Interactivo de Consolas Windows.<br>
            Si tienes alguna pregunta, no dudes en contactarnos.
        </p>
    </div>
</body>
</html>
"""
