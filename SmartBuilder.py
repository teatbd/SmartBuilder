# smartbuilder.py

class Function:
    def __init__(self, name, inputs, logic, is_view=False, is_pure=False):
        self.name = name
        self.inputs = inputs  # Lista de strings como ["user", "message"]
        self.logic = logic    # String con el contenido de la función
        self.is_view = is_view
        self.is_pure = is_pure

    def generate_solidity(self):
        input_str = ", ".join([f"string {i}" for i in self.inputs])  # asume tipos string por simplicidad
        modifier = "view" if self.is_view else "pure" if self.is_pure else ""
        modifier_str = f"{modifier} " if modifier else ""
        return f"""    function {self.name}({input_str}) {modifier_str}public {{
        {self.logic}
    }}"""


class Mapping:
    def __init__(self, key_type, value_type):
        self.key_type = key_type
        self.value_type = value_type

    def to_solidity(self):
        key = self.key_type if isinstance(self.key_type, str) else self.key_type.__name__
        value = self.value_type if isinstance(self.value_type, str) else self.value_type.__name__
        return f"mapping({key} => {value})"


class Contract:
    def __init__(self, name):
        self.name = name
        self.state_variables = []
        self.functions = []

    def add_state_variable(self, name, var_type):
        self.state_variables.append((name, var_type))

    def add_function(self, function):
        self.functions.append(function)

    def generate_solidity(self):
        lines = [f"pragma solidity ^0.8.0;", f"contract {self.name} {{"]

        for name, var_type in self.state_variables:
            if isinstance(var_type, Mapping):
                lines.append(f"    {var_type.to_solidity()} public {name};")
            else:
                lines.append(f"    {var_type} public {name};")

        for fn in self.functions:
            lines.append(fn.generate_solidity())

        lines.append("}")
        return "\n".join(lines)


# Ejemplo de uso
if __name__ == "__main__":
    my_contract = Contract("HelloWorld")
    my_contract.add_state_variable("messages", Mapping("string", "string"))

    hello_fn = Function(
        name="setMessage",
        inputs=["user", "message"],
        logic="messages[user] = message;"
    )
    my_contract.add_function(hello_fn)

    print(my_contract.generate_solidity())

