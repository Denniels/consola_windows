# 📧 Configuración del Sistema de Correos para Certificados

## Configuración Rápida

### 1. Configurar Gmail (Recomendado)

1. **Crear una contraseña de aplicación:**
   - Ve a tu cuenta de Gmail
   - Configuración → Seguridad → Verificación en 2 pasos
   - Contraseñas de aplicaciones → Generar nueva
   - Copia la contraseña generada

2. **Configurar las credenciales:**
   - Copia `email_config_example.py` como `email_config.py`
   - Edita `email_config.py` con tus datos:

```python
# Configuración del servidor SMTP
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USE_TLS = True

# Credenciales del remitente
EMAIL_SENDER = "tu_email@gmail.com"
EMAIL_PASSWORD = "tu_contraseña_de_aplicación"  # La que generaste
```

### 2. Otros Proveedores de Email

#### Outlook/Hotmail:
```python
SMTP_SERVER = "smtp-mail.outlook.com"
SMTP_PORT = 587
SMTP_USE_TLS = True
```

#### Yahoo:
```python
SMTP_SERVER = "smtp.mail.yahoo.com"
SMTP_PORT = 587
SMTP_USE_TLS = True
```

## Funcionalidades del Sistema

### ✅ Registro de Usuario
- Formulario al inicio de la aplicación
- Captura: Nombre, Apellido, Email
- Almacenamiento seguro en JSON

### ✅ Generación de Certificados
- PDF profesional con diseño personalizado
- Nombre completo del usuario
- Fecha de completación
- Porcentaje de progreso
- Firma del instructor

### ✅ Envío Automático
- Email HTML profesional
- Certificado adjunto automáticamente
- Confirmación de envío
- Registro de certificados enviados

## Estructura de Archivos

```
streamlit_app/
├── utils/
│   ├── user_manager.py          # Lógica principal
│   ├── email_config_example.py  # Plantilla de configuración
│   └── email_config.py          # Tu configuración (crear)
└── data/
    └── users.json               # Base de datos de usuarios
```

## Seguridad

- ⚠️ **NUNCA** subas `email_config.py` a repositorios públicos
- ✅ Usa contraseñas de aplicación, no tu contraseña principal
- ✅ El archivo está en `.gitignore` por seguridad

## Solución de Problemas

### Error de autenticación:
- Verifica que tengas 2FA activado
- Usa contraseña de aplicación, no la personal
- Verifica que el email sea correcto

### Error de conexión:
- Verifica tu conexión a internet
- Algunos firewalls bloquean SMTP
- Prueba con otros puertos si es necesario

### Certificado no se genera:
- Verifica que `reportlab` esté instalado: `pip install reportlab`
- Verifica permisos de escritura en la carpeta temporal

## Personalización

### Modificar el diseño del certificado:
Edita la función `generate_certificate()` en `user_manager.py`

### Cambiar la plantilla del email:
Modifica `EMAIL_TEMPLATE` en `email_config.py`

### Agregar más campos al registro:
Actualiza las funciones en `user_manager.py` y el formulario en `check_user_registration()`
