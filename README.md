# Ataque DHCP Spoofing  
## Documentación Técnica Profesional

---

## Aviso Legal

Este proyecto ha sido desarrollado **exclusivamente con fines educativos y de auditoría de seguridad autorizada**.  
El uso de esta herramienta en redes, sistemas o infraestructuras **sin autorización expresa** es ilegal y puede acarrear consecuencias legales.

El autor no se hace responsable del uso indebido de la información o del código presentado.

---

## 1. Descripción General

El **DHCP Spoofing** es un ataque de red en el cual un atacante introduce un **servidor DHCP no autorizado (rogue DHCP)** dentro de una red de área local (LAN), con el objetivo de distribuir configuraciones de red maliciosas a clientes legítimos.

Al responder más rápido que el servidor DHCP legítimo, el atacante puede asignar:
- Gateway (puerta de enlace) falsa
- Servidor DNS controlado por el atacante
- Direccionamiento IP arbitrario

Este ataque suele utilizarse como paso inicial para ataques más avanzados como:
- Man-in-the-Middle (MitM)
- Intercepción y análisis de tráfico
- Redirección de comunicaciones
- Denegación de servicio (DoS)

---

## 2. Objetivo del Script

El objetivo del script es **demostrar y analizar el ataque DHCP Spoofing en un entorno de laboratorio controlado**, permitiendo a estudiantes y profesionales de seguridad:

- Comprender el funcionamiento del protocolo DHCP
- Identificar vulnerabilidades en redes sin controles de seguridad
- Evaluar el impacto de servidores DHCP falsos
- Aplicar medidas de mitigación adecuadas

Este proyecto está destinado únicamente a **laboratorios académicos y pruebas de seguridad autorizadas**.

---

## 3. Topología de Red

El laboratorio se basa en una red LAN simple compuesta por los siguientes elementos:

| Dispositivo | Descripción | Dirección IP |
|------------|------------|--------------|
| Router legítimo | Gateway autorizado de la red | 192.168.1.1 |
| Host víctima | Cliente DHCP | Asignada dinámicamente |
| Atacante | Kali Linux (DHCP falso) | 192.168.1.200 |
| Switch | Dispositivo de Capa 2 | VLAN 1 |

**VLAN utilizada:** VLAN 1 (por defecto)

---

## 4. Parámetros Utilizados

- Interfaz de red: `eth0`
- Gateway falso: `192.168.1.200`
- Servidor DNS malicioso: Controlado por el atacante
- Alcance DHCP: Configurado para responder antes que el servidor legítimo

---

## 5. Requisitos para Utilizar la Herramienta

### Requisitos de Software
- Sistema operativo Linux (Kali Linux recomendado)
- Python 3.x
- Librería Scapy

### Requisitos del Sistema
- Permisos de superusuario (root o sudo)
- Acceso directo a la red local objetivo

### Instalación de dependencias
```bash
sudo apt update
sudo apt install python3-scapy -y
```

---

## 6. Evidencias y Capturas de Pantalla

Las evidencias del laboratorio deben almacenarse en el siguiente directorio:

```
/images
```

Ejemplos de evidencias recomendadas:
- Cliente obteniendo configuración DHCP maliciosa
- Capturas de tráfico DHCP (DHCP Offer / DHCP ACK)
- Ejecución del script en la máquina atacante

---

## 7. Medidas de Mitigación

Para prevenir ataques de **DHCP Spoofing**, se recomiendan las siguientes medidas de seguridad:

- Habilitar **DHCP Snooping** en switches administrables
- Definir puertos **confiables (trusted)** y **no confiables (untrusted)**
- Segmentar la red mediante **VLANs**
- Monitorear continuamente el tráfico DHCP
- Implementar **802.1X** para control de acceso a la red

### Ejemplo de configuración en Cisco IOS
```bash
ip dhcp snooping
ip dhcp snooping vlan 1
```

---

## 8. Uso Ético

Esta herramienta debe utilizarse **únicamente** para:
- Prácticas académicas
- Laboratorios de ciberseguridad
- Auditorías de seguridad con autorización

🚫 Está estrictamente prohibido su uso en:
- Redes productivas
- Redes públicas
- Sistemas sin consentimiento del propietario

---

## 9. Autor

**Max (Reily Castillo Del Rosario)**  
Estudiante de Ciberseguridad  
República Dominicana  

---

## 10. Contribuciones

Las contribuciones son bienvenidas siempre que:
- Mantengan un enfoque educativo
- No promuevan actividades ilegales
- Incluyan documentación clara y profesional

Proceso de contribución:
1. Realizar un fork del repositorio
2. Crear una nueva rama
3. Enviar un Pull Request debidamente documentado

---

## 11. Licencia

Este proyecto se distribuye bajo la licencia **MIT**, permitiendo su uso, modificación y distribución con fines educativos, siempre que se mantenga la atribución correspondiente al autor.
