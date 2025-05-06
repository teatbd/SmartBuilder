# SmartBuilder

SmartBuilder is a Python-based educational library designed to help developers learn the structure of Solidity smart contracts using familiar Python syntax. This tool serves as a conceptual bridge for Python developers entering the world of blockchain and smart contract development.

##  Overview

SmartBuilder allows you to simulate key components of Solidity such as:

- `Contract` definitions
- `Mapping` variables
- `Function` declarations
- Basic logic generation

This is **not** a Solidity compiler or interpreter. It is a learning tool to explore how smart contracts are structured, and how we can think about them from a Pythonic perspective.

##  Example

```python
from smartbuilder import Contract, Function, Mapping

# Create a smart contract
my_contract = Contract("Voting")

# Add state variables
my_contract.add_state_variable("candidates", Mapping(str, int))

# Add a function to vote
my_contract.add_function(Function(
    name="vote",
    inputs=["candidate"],
    logic="candidates[candidate] += 1"
))

# Generate Solidity code
print(my_contract.generate_solidity())
