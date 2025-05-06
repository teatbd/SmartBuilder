# SmartBuilder

SmartBuilder es una librería educativa escrita en Python que actúa como puente entre Python y Solidity, permitiendo a los desarrolladores aprender y prototipar contratos inteligentes de manera simple y comprensible.

## Objetivo
Simplificar el aprendizaje de contratos inteligentes en Solidity a través de una sintaxis familiar en Python y herramientas automáticas de conversión.

## Instalación
Por ahora, cloná este repositorio:

```bash
git clone https://github.com/tuusuario/smartbuilder.git
cd smartbuilder
```

## Ejemplo básico
```python
from smartbuilder.contract import Contract
from smartbuilder.function import Function
from smartbuilder.mapping import Mapping

# Crear el contrato
my_contract = Contract("HelloWorld")

# Agregar variables de estado
my_contract.add_state_variable("messages", Mapping(str, str))

# Agregar función
hello_fn = Function(
    name="setMessage",
    inputs=["user", "message"],
    logic="""
    messages[user] = message
    """
)
my_contract.add_function(hello_fn)

# Generar Solidity
print(my_contract.generate_solidity())
```

## 🛠 Estructura del proyecto
```
smartbuilder/
├── contract.py
├── function.py
├── mapping.py
├── generator.py
examples/
└── hello_world.py
tests/
└── test_contract.py
```

## Futuro
- Generación directa de archivos `.sol`
- Integración con Remix o Truffle
- Visualización web con Streamlit o Gradio

## Licencia
Este proyecto está licenciado bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más información.

---

### examples/hello_world.py
```python
from smartbuilder.contract import Contract
from smartbuilder.function import Function
from smartbuilder.mapping import Mapping

contract = Contract("HelloWorld")
contract.add_state_variable("messages", Mapping(str, str))

fn = Function(
    name="setMessage",
    inputs=["user", "message"],
    logic="""
    messages[user] = message
    """
)

contract.add_function(fn)
print(contract.generate_solidity())
```