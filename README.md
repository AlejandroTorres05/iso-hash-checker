# Verificador de Hash - ISO

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

### Interfaz Gráfica

1. **Arrastra** el archivo ISO al primer recuadro (o haz click para seleccionar)
2. **Arrastra** el archivo de hash oficial al segundo recuadro (SHA256SUMS, etc.)
3. Presiona **"Verificar Integridad"**
4. **Espera** el resultado (puede tomar varios minutos para ISOs grandes)

## Cómo obtener los archivos necesarios

### 1. Descargar ISO de Ubuntu

Visita [ubuntu.com/download](https://ubuntu.com/download) y descarga la ISO deseada.

### 2. Descargar archivo de hash oficial

En la misma página de descarga, busca enlaces como:

- `SHA256SUMS`
- `SHA1SUMS`
- `MD5SUMS`

O visita directamente: `http://releases.ubuntu.com/[version]/`

### Ejemplo de archivo SHA256SUMS:

```
a1b2c3d4e5f6... *ubuntu-22.04.3-desktop-amd64.iso
f6e5d4c3b2a1... *ubuntu-22.04.3-live-server-amd64.iso
```

## Capturas de Pantalla

## Funcionamiento Interno

1. **Lectura**: Lee el archivo de hash oficial y detecta automáticamente el algoritmo
2. **Cálculo**: Calcula el hash del archivo ISO usando el mismo algoritmo
3. **Comparación**: Compara ambos hashes byte por byte
4. **Resultado**: Informa si la verificación fue exitosa o falló

## Seguridad

### ✅ Verificación Exitosa

- El archivo es **auténtico** y **no está corrupto**
- Seguro para usar en instalaciones

### ❌ Verificación Fallida

- El archivo puede estar **corrupto**
- Posible **manipulación** o **descarga incompleta**
- **NO usar** para instalaciones

## Autor

**Alejandro Torres Soto** - [@AlejandroTorres05](https://github.com/AlejandroTorres05)
