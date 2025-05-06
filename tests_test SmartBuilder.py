import unittest
from smartbuilder import Contract, Function, Mapping

class TestSmartBuilder(unittest.TestCase):

    def test_mapping_generate_solidity(self):
        mapping = Mapping("address", "uint")
        solidity_code = mapping.generate_solidity()
        self.assertEqual(solidity_code, "mapping(address => uint)")

    def test_function_generate_solidity(self):
        fn = Function(
            name="vote",
            inputs=["candidate"],
            logic="candidates[candidate] += 1"
        )
        solidity = fn.generate_solidity()
        self.assertIn("function vote(candidate)", solidity)
        self.assertIn("candidates[candidate] += 1", solidity)

    def test_contract_generate_solidity(self):
        contract = Contract("Voting")
        contract.add_state_variable("candidates", Mapping("string", "uint"))
        contract.add_function(Function("vote", ["candidate"], "candidates[candidate] += 1"))

        solidity_code = contract.generate_solidity()
        self.assertIn("contract Voting", solidity_code)
        self.assertIn("mapping(string, uint) public candidates;", solidity_code)
        self.assertIn("function vote(candidate)", solidity_code)

if __name__ == '__main__':
    unittest.main()
