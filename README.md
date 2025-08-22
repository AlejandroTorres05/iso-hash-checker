# Verificador de Hash - Ubuntu ISO

Un verificador de integridad con interfaz gráfica para validar la autenticidad de imágenes ISO comparando su hash con el archivo oficial.

## Descripción

Este programa permite verificar la integridad de archivos ISO comparando su hash SHA256/SHA1/MD5 con el hash oficial. Incluye una interfaz gráfica intuitiva con funcionalidad de arrastrar y soltar.

### Características

- **Interfaz gráfica** con drag & drop
- **Múltiples algoritmos** de hash (SHA256, SHA1, MD5)
- **Detección automática** del algoritmo desde el archivo oficial
- **Procesamiento eficiente** de archivos grandes (lee en bloques)
- **Interfaz visual** con indicadores de estado por colores
- **Barra de progreso** durante la verificación
- **Multihilo** para no bloquear la interfaz
- **Log detallado** del proceso de verificación

### Configuración para correr el proyecto

Inicialmente, vamos a clonar el repositorio

```bash
git clone https://github.com/AlejandroTorres05/iso-hash-checker
cd iso-hash-checker
```

Posteriormente, crear y correr un entorno virtual para no instalar dependencias directamente en tu máquina.

> Está guia de comandos aplica solo para linux.

```bash
python3 -m venv env
source env/bin/activate
```

Una vez instalado y activado el entorno virtual, correr:

```bash
pip install tkinterdnd2
```

Para instalar `tkinterdnd2` (Herramienta usada para el Drag and Drop).

Finalmente, para correr el proyecto usar el comando:

```bash
python3 verificador_hash_gui.py
```
