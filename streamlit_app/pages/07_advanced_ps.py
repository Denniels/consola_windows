"""
Módulo 07: Administración del Sistema (PowerShell Avanzado)
"""

import streamlit as st
import sys
import os

# Add parent directories to path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
utils_dir = os.path.join(parent_dir, 'utils')
components_dir = os.path.join(parent_dir, 'components')

sys.path.insert(0, utils_dir)
sys.path.insert(0, components_dir)

from progress_tracker import create_section_header, create_info_card
from ui_components import (
    ConsoleSimulator, QuizComponent, CommandPracticeComponent,
    create_learning_objective_card, create_tip_card, create_code_example
)

def render_page():
    """Renderiza la página de PowerShell avanzado"""
    
    # Header principal
    create_section_header(
        title="Administración del Sistema con PowerShell",
        description="Convierte en un administrador de sistemas experto usando PowerShell",
        icon="🔵"
    )
    
    # Objetivos de aprendizaje
    objectives = [
        "Administrar servicios y procesos del sistema",
        "Gestionar usuarios y grupos locales",
        "Monitorear rendimiento y eventos del sistema",
        "Crear scripts de administración automatizados",
        "Implementar administración remota con PSRemoting"
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
    
    st.markdown("## � Administración del Sistema")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### Gestión de Servicios")
        st.markdown("""
        PowerShell excele en la administración de servicios de Windows, permitiendo control completo y automatización.
        """)
        
        create_code_example(
            "Administración de servicios",
            """# Listar servicios críticos
Get-Service | Where-Object {$_.Status -eq "Stopped" -and $_.StartType -eq "Automatic"}

# Reiniciar un servicio específico
Restart-Service -Name "Spooler" -Force

# Cambiar el tipo de inicio de un servicio
Set-Service -Name "Fax" -StartupType Disabled

# Monitorear servicios críticos
$CriticalServices = @("BITS", "Spooler", "Themes")
foreach ($service in $CriticalServices) {
    $svc = Get-Service -Name $service
    if ($svc.Status -ne "Running") {
        Write-Warning "Servicio $service no está ejecutándose!"
    }
}""",
            "powershell",
            "Control completo sobre servicios del sistema"
        )
        
        st.markdown("### Gestión de Procesos")
        st.markdown("""
        PowerShell permite monitoreo avanzado y gestión de procesos con información detallada.
        """)
        
        create_code_example(
            "Administración de procesos",
            """# Procesos que consumen más CPU
Get-Process | Sort-Object CPU -Descending | Select-Object -First 10

# Terminar procesos que no responden
Get-Process | Where-Object {$_.Responding -eq $false} | Stop-Process -Force

# Monitorear uso de memoria
$MemoryThreshold = 100MB
Get-Process | Where-Object {$_.WorkingSet -gt $MemoryThreshold} | 
    Select-Object Name, @{Name="Memory(MB)";Expression={$_.WorkingSet/1MB -as [int]}}

# Iniciar proceso con prioridad específica
Start-Process "notepad" -WindowStyle Maximized""",
            "powershell",
            "Monitoreo y control avanzado de procesos"
        )
        
        st.markdown("### Administración de Usuarios")
        st.markdown("""
        PowerShell incluye cmdlets para gestionar usuarios y grupos locales de forma eficiente.
        """)
        
        create_code_example(
            "Gestión de usuarios locales",
            """# Listar usuarios locales
Get-LocalUser

# Crear nuevo usuario local
New-LocalUser -Name "UsuarioTest" -Password (ConvertTo-SecureString "Password123!" -AsPlainText -Force) -FullName "Usuario de Prueba"

# Agregar usuario a grupo
Add-LocalGroupMember -Group "Administradores" -Member "UsuarioTest"

# Deshabilitar cuenta de usuario
Disable-LocalUser -Name "UsuarioTest"

# Obtener información de grupos
Get-LocalGroup | Select-Object Name, Description""",
            "powershell",
            "Administración completa de usuarios locales"
        )
        
        st.markdown("### Monitoreo del Sistema")
        st.markdown("""
        PowerShell permite crear scripts de monitoreo robustos para supervisar la salud del sistema.
        """)
        
        create_code_example(
            "Script de monitoreo básico",
            """# Función de monitoreo del sistema
function Get-SystemHealth {
    $Report = @{}
    
    # CPU Usage
    $CPU = Get-Counter "\\Processor(_Total)\\% Processor Time" -SampleInterval 1 -MaxSamples 3
    $Report.CPUAverage = ($CPU.CounterSamples | Measure-Object CookedValue -Average).Average
    
    # Memoria disponible
    $Memory = Get-Counter "\\Memory\\Available MBytes"
    $Report.AvailableMemoryMB = $Memory.CounterSamples.CookedValue
    
    # Espacio en disco C:
    $Disk = Get-PSDrive C
    $Report.DiskFreeGB = [math]::Round($Disk.Free / 1GB, 2)
    
    # Servicios detenidos críticos
    $StoppedServices = Get-Service | Where-Object {$_.Status -eq "Stopped" -and $_.StartType -eq "Automatic"}
    $Report.StoppedCriticalServices = $StoppedServices.Count
    
    return $Report
}

# Ejecutar monitoreo
$Health = Get-SystemHealth
Write-Output "=== Reporte del Sistema ==="
Write-Output "CPU Promedio: $([math]::Round($Health.CPUAverage, 2))%"
Write-Output "Memoria Disponible: $($Health.AvailableMemoryMB) MB"
Write-Output "Espacio Libre C:: $($Health.DiskFreeGB) GB"
Write-Output "Servicios Detenidos: $($Health.StoppedCriticalServices)"
""",
            "powershell",
            "Script completo para monitoreo automático del sistema"
        )
    
    with col2:
        create_tip_card(
            "💡 Execution Policy",
            "Para ejecutar scripts, configura la política: Set-ExecutionPolicy RemoteSigned -Scope CurrentUser",
            "info"
        )
        
        create_tip_card(
            "🔒 Seguridad",
            "Siempre valida permisos antes de realizar cambios críticos del sistema.",
            "warning"
        )
        
        create_tip_card(
            "📊 Performance Counters",
            "Get-Counter te da acceso a todos los contadores de rendimiento de Windows.",
            "success"
        )
        
        st.markdown("### Cmdlets de Administración")
        st.code("""
Get-Service     - Servicios
Get-Process     - Procesos
Get-LocalUser   - Usuarios locales
Get-LocalGroup  - Grupos locales
Get-Counter     - Contadores de rendimiento
Get-EventLog    - Logs de eventos
Get-WmiObject   - Info del sistema
Get-ComputerInfo - Info detallada del PC
        """)

def render_practice_section():
    """Renderiza la sección de práctica"""
    
    st.markdown("## 🏆 Ejercicios Prácticos")
    
    # Simulador de consola
    st.markdown("### 🔷 Consola PowerShell - Administración del Sistema")
    ps_simulator = ConsoleSimulator("powershell")
    ps_simulator.render(key_suffix="ps_advanced")
    
    st.markdown("---")
    st.markdown("## 🎯 Ejercicios de Administración")
    
    # Definir ejercicios prácticos
    practice_commands = [
        {
            "descripcion": "Lista todos los servicios que están detenidos pero configurados para iniciarse automáticamente",
            "ejemplo": "Get-Service | Where-Object {$_.Status -eq 'Stopped' -and $_.StartType -eq 'Automatic'}",
            "comando": "Get-Service",
            "tipo_consola": "powershell",
            "pista": "Combina Where-Object con dos condiciones usando -and",
            "solucion": "Get-Service | Where-Object {$_.Status -eq 'Stopped' -and $_.StartType -eq 'Automatic'}"
        },
        {
            "descripcion": "Muestra los 5 procesos que más memoria están consumiendo",
            "ejemplo": "Get-Process | Sort-Object WorkingSet -Descending | Select-Object -First 5",
            "comando": "Get-Process",
            "tipo_consola": "powershell",
            "pista": "Usa Sort-Object con WorkingSet y Select-Object -First",
            "solucion": "Get-Process | Sort-Object WorkingSet -Descending | Select-Object -First 5"
        },
        {
            "descripcion": "Obtén información básica del sistema como nombre y versión de Windows",
            "ejemplo": "Get-ComputerInfo | Select-Object WindowsProductName, WindowsVersion",
            "comando": "Get-ComputerInfo",
            "tipo_consola": "powershell",
            "pista": "Get-ComputerInfo tiene mucha información, usa Select-Object para filtrar",
            "solucion": "Get-ComputerInfo | Select-Object WindowsProductName, WindowsVersion"
        },
        {
            "descripcion": "Lista todos los usuarios locales y muestra solo el nombre y si están habilitados",
            "ejemplo": "Get-LocalUser | Select-Object Name, Enabled",
            "comando": "Get-LocalUser",
            "tipo_consola": "powershell",
            "pista": "Get-LocalUser seguido de Select-Object para elegir propiedades",
            "solucion": "Get-LocalUser | Select-Object Name, Enabled"
        },
        {
            "descripcion": "Verifica el espacio libre en el disco C: en GB",
            "ejemplo": "Get-PSDrive C | Select-Object @{Name='FreeGB';Expression={[math]::Round($_.Free/1GB,2)}}",
            "comando": "Get-PSDrive",
            "tipo_consola": "powershell",
            "pista": "Usa una expresión calculada para convertir bytes a GB",
            "solucion": "Get-PSDrive C: con conversión matemática a GB"
        }
    ]
    
    # Componente de práctica
    practice_component = CommandPracticeComponent(practice_commands)
    practice_component.render(key_suffix="ps_advanced_practice")

def render_quiz_section():
    """Renderiza la sección de quiz"""
    
    st.markdown("## 🧩 Evaluación: PowerShell Avanzado")
    
    # Definir preguntas del quiz
    quiz_questions = [
        {
            "pregunta": "¿Qué cmdlet usas para obtener información detallada del sistema?",
            "opciones": ["Get-SystemInfo", "Get-ComputerInfo", "Get-PCInfo", "Get-MachineInfo"],
            "respuesta_correcta": "Get-ComputerInfo",
            "explicacion": "Get-ComputerInfo proporciona información completa sobre el sistema."
        },
        {
            "pregunta": "¿Cómo reinicia un servicio de Windows en PowerShell?",
            "opciones": ["Restart-Service", "Reboot-Service", "Reset-Service", "Reload-Service"],
            "respuesta_correcta": "Restart-Service",
            "explicacion": "Restart-Service es el cmdlet estándar para reiniciar servicios."
        },
        {
            "pregunta": "¿Qué cmdlet permite crear usuarios locales?",
            "opciones": ["Add-LocalUser", "New-LocalUser", "Create-LocalUser", "Make-LocalUser"],
            "respuesta_correcta": "New-LocalUser",
            "explicacion": "New-LocalUser es el cmdlet correcto para crear nuevos usuarios locales."
        },
        {
            "pregunta": "¿Cuál es el propósito de Get-Counter?",
            "opciones": [
                "Contar archivos",
                "Acceder a contadores de rendimiento",
                "Contar líneas de código",
                "Enumerar objetos"
            ],
            "respuesta_correcta": "Acceder a contadores de rendimiento",
            "explicacion": "Get-Counter permite acceder a los contadores de rendimiento de Windows."
        }
    ]
    
    # Componente de quiz
    quiz_component = QuizComponent(quiz_questions)
    quiz_component.render(key_suffix="ps_advanced_quiz")

def render_reference_section():
    """Renderiza la sección de referencia"""
    
    st.markdown("## 📖 Referencia Rápida")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Administración de Servicios")
        st.code("""
Get-Service                    - Listar servicios
Start-Service -Name "nombre"   - Iniciar servicio
Stop-Service -Name "nombre"    - Detener servicio
Restart-Service -Name "nombre" - Reiniciar servicio
Set-Service -Name "nombre" -StartupType Automatic

# Servicios críticos detenidos
Get-Service | Where-Object {$_.Status -eq "Stopped" -and $_.StartType -eq "Automatic"}
        """, language="powershell")
        
        st.markdown("### Gestión de Procesos")
        st.code("""
Get-Process                    - Listar procesos
Stop-Process -Name "proceso"   - Terminar proceso
Start-Process "aplicacion"     - Iniciar aplicación

# Top procesos por CPU
Get-Process | Sort-Object CPU -Desc | Select-Object -First 10

# Procesos que no responden
Get-Process | Where-Object {$_.Responding -eq $false}
        """, language="powershell")
        
        st.markdown("### Usuarios y Grupos")
        st.code("""
Get-LocalUser                  - Listar usuarios
New-LocalUser                  - Crear usuario
Remove-LocalUser               - Eliminar usuario
Enable-LocalUser               - Habilitar usuario
Disable-LocalUser              - Deshabilitar usuario

Get-LocalGroup                 - Listar grupos
Add-LocalGroupMember           - Agregar a grupo
Remove-LocalGroupMember        - Quitar de grupo
        """, language="powershell")
    
    with col2:
        st.markdown("### Monitoreo del Sistema")
        st.code("""
Get-ComputerInfo               - Info del sistema
Get-Counter "\\Processor(_Total)\\% Processor Time"
Get-Counter "\\Memory\\Available MBytes"
Get-PSDrive                    - Info de discos

# Espacio libre en disco
Get-PSDrive C | Select-Object @{Name='FreeGB';Expression={$_.Free/1GB}}

# Uptime del sistema
(Get-Date) - (Get-CimInstance Win32_OperatingSystem).LastBootUpTime
        """, language="powershell")
        
        st.markdown("### Información del Sistema")
        st.code("""
Get-WmiObject Win32_ComputerSystem    - Info del hardware
Get-WmiObject Win32_OperatingSystem   - Info del SO
Get-WmiObject Win32_LogicalDisk       - Info de discos
Get-WmiObject Win32_NetworkAdapter    - Adaptadores de red

# Información específica
Get-ComputerInfo | Select-Object WindowsProductName, TotalPhysicalMemory
        """, language="powershell")
        
        st.markdown("### Scripts de Monitoreo")
        st.code("""
# Función de reporte del sistema
function Get-SystemReport {
    [PSCustomObject]@{
        ComputerName = $env:COMPUTERNAME
        LastBoot = (Get-CimInstance Win32_OperatingSystem).LastBootUpTime
        CPUUsage = (Get-Counter "\\Processor(_Total)\\% Processor Time").CounterSamples.CookedValue
        FreeMemoryGB = [math]::Round((Get-Counter "\\Memory\\Available MBytes").CounterSamples.CookedValue/1024, 2)
    }
}
        """, language="powershell")
    
    create_tip_card(
        "🚀 Próximo paso",
        "Con PowerShell avanzado, puedes automatizar prácticamente cualquier tarea de administración de Windows.",
        "success"
    )

if __name__ == "__main__":
    render_page()
