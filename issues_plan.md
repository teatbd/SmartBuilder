# Plan de Issues para SmartBuilder

Este documento detalla las tareas previstas para el desarrollo y evolución de SmartBuilder. Cada ítem puede transformarse en un issue individual.

---

## ✅ Soporte para arrays

**Objetivo:** Permitir definir y compilar variables de tipo array (estáticos y dinámicos).

**Tareas:**
- Implementar clases `Array` y soporte en `StateVar`.
- Asegurar compatibilidad con el compilador Solidity.
- Agregar tests de ejemplo.

---

## ✅ Soporte para enums

**Objetivo:** Habilitar la creación de enumeraciones desde Python.

**Tareas:**
- Crear clase `Enum`.
- Añadir validaciones de tipo y uso en funciones.
- Agregar ejemplos y documentación.

---

## ✅ Comentarios en el código generado

**Objetivo:** Poder añadir comentarios en el código final para mayor claridad.

**Tareas:**
- Permitir al usuario ingresar comentarios descriptivos en los objetos.
- Incluir esos comentarios en el código Solidity generado.
- Opción para activar/desactivar comentarios al compilar.

---

## ✅ Funciones `view`, `pure`, `payable`

**Objetivo:** Soporte para las especificaciones Solidity más comunes.

**Tareas:**
- Añadir atributos a la clase `Function`: `view`, `pure`, `payable`.
- Validar combinaciones válidas.
- Reflejarlo correctamente en la salida Solidity.

---

## ✅ Generación en Rust (Ink!)

**Objetivo:** Extender el compilador para generar contratos en lenguaje Rust (usando Ink!).

**Tareas:**
- Crear generador Rust modular.
- Diseñar abstracciones compartidas entre Solidity y Rust.
- Agregar tests específicos por backend.

---

## ✅ Modularización multichain por backend

**Objetivo:** Separar la lógica por lenguaje de destino, para soportar múltiples targets.

**Tareas:**
- Crear carpeta `backends/solidity/` y `backends/rust/`
- Refactorizar `Contract.compile()` para elegir backend dinámicamente.
- Posibilidad futura de plugins (`Cairo`, `Move`, etc.)

---

## ✅ Interfaz visual web (modo no-code)

**Objetivo:** Diseñar una interfaz gráfica básica para usar SmartBuilder como herramienta no-code.

**Tareas:**
- Definir requerimientos (React, Flask, Streamlit).
- Mockup de pantallas.
- Prueba de concepto para creación visual de contratos.

---

## ✅ Exportación para Remix, Hardhat, Anchor

**Objetivo:** Facilitar la exportación de contratos generados para herramientas de desarrollo populares.

**Tareas:**
- Crear función `export()` con opciones de formato.
- Agregar metadata (como nombre de archivo, versión, etc.)
- Generar `.sol`, `package.json` o carpetas completas según necesidad.

---
