"""

Copyrights:\n
- © Qiskrypt, 2022 - All rights reserved.\n

Powered by:\n
- IBM
- IBM Quantum
- IBM Qiskit


Description:\n
- The Qiskrypt is a software suite of protocols of
  quantum cryptography, quantum communication and
  other protocols/algorithms, built using the IBM's Qiskit.

College(s):\n
- NOVA School of Science and Technology, NOVA University of Lisbon, Portugal.
- Faculty of Sciences, University of Lisbon, Portugal.
- Tecnico Lisboa, University of Lisbon, Portugal.
- School of Engineering, University of Connecticut, United States of America.

Other Institution(s):\n
- Instituto de Telecomunicacoes, Portugal.
- SQIG, Portugal.
- LASIGE, Portugal.
- UT Austin Program, Portugal.

Author(s):\n
- Ruben Barreiro (NOVA School of Science and Technology, NOVA University of Lisbon, Portugal).

Acknowledgement(s):\n
- Prof. Andre Souto (Faculty of Sciences, University of Lisbon, Portugal).
- Prof. Paulo Mateus (Tecnico Lisboa, University of Lisbon, Portugal).
- Prof. Nikola Paunkovic (Tecnico Lisboa, University of Lisbon, Portugal).
- Prof. Walter Krawec (School of Engineering, University of Connecticut, United States of America).
- Prof. Antonio Ravara (NOVA School of Science and Technology, NOVA University of Lisbon, Portugal).

"""

"""
Import required Libraries and Packages.
"""

from unittest import TestCase, TestLoader, TestSuite
"""
Import TestCase, TestLoader and TestSuite from Unittest.
"""

from qiskit import AncillaRegister
"""
Import Ancilla Register from IBM's Qiskit.
"""

from src.quantum.circuit.registers.quantum.QiskryptAncillaQuantumRegister import QiskryptAncillaQuantumRegister
"""
Import the Qiskrypt's Ancilla Quantum Register.
"""

from src.quantum.circuit.registers.quantum.fully_quantum.QiskryptAncillaFullyQuantumRegister import QiskryptAncillaFullyQuantumRegister
"""
Import the Qiskrypt's Ancilla Fully-Quantum Register.
"""

from src.quantum.circuit.registers.quantum.semi_quantum.QiskryptAncillaSemiQuantumRegister import QiskryptAncillaSemiQuantumRegister
"""
Import the Qiskrypt's Ancilla Semi-Quantum Register.
"""

from src.quantum.circuit.registers.classical.QiskryptClassicalRegister import QiskryptClassicalRegister
"""
Import the Qiskrypt's Classical Register.
"""


class QiskryptAncillaQuantumRegisterTests(TestCase):
    """
    Object Class of the Unitary Tests for the Qiskrypt's Ancilla Quantum Register.
    """

    def test_no_1_qiskrypt_ancilla_quantum_register_1_qubit(self):
        """
        Test Case #1:

        - Create a Qiskrypt's Ancilla Quantum Register, with 1 qubit.

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        ancilla_quantum_register_name = "anc_qu_reg"
        """
        Set the name of the Qiskrypt's Ancilla Quantum Register.
        """

        ancilla_quantum_register_num_qubits = 1
        """
        Set the number of qubits for the Qiskrypt's Ancilla Quantum Register.
        """

        qiskrypt_ancilla_quantum_register = \
            QiskryptAncillaQuantumRegister(name=ancilla_quantum_register_name,
                                           num_ancilla_qubits=ancilla_quantum_register_num_qubits,
                                           qiskit_ancilla_quantum_register=None)
        """
        Create a Qiskrypt's Ancilla Quantum Register, given its name and number of qubits.
        """

        assert(ancilla_quantum_register_name == qiskrypt_ancilla_quantum_register.get_name())
        """
        Assertion for the name of the Qiskrypt's Ancilla Quantum Register.
        """

        assert(ancilla_quantum_register_num_qubits == qiskrypt_ancilla_quantum_register.get_num_ancilla_qubits())
        """
        Assertion for the number of qubits of the Qiskrypt's Ancilla Quantum Register.
        """

        assert(isinstance(qiskrypt_ancilla_quantum_register.get_qiskit_ancilla_quantum_register(), AncillaRegister))
        """
        Assertion for the IBM's Qiskit Ancilla Register of the Qiskrypt's Ancilla Quantum Register.
        """

        assert(isinstance(qiskrypt_ancilla_quantum_register, QiskryptAncillaQuantumRegister))
        """
        Assertion for the own Qiskrypt's Ancilla Quantum Register, regarding a Qiskrypt's Ancilla Quantum Register.
        """

        assert(not isinstance(qiskrypt_ancilla_quantum_register, QiskryptAncillaFullyQuantumRegister))
        """
        Assertion for the own Qiskrypt's Ancilla Quantum Register, regarding a Qiskrypt's Ancilla Fully-Quantum Register.
        """

        assert(not isinstance(qiskrypt_ancilla_quantum_register, QiskryptAncillaSemiQuantumRegister))
        """
        Assertion for the own Qiskrypt's Ancilla Quantum Register, regarding a Qiskrypt's Ancilla Semi-Quantum Register.
        """

        assert(not isinstance(qiskrypt_ancilla_quantum_register, QiskryptClassicalRegister))
        """
        Assertion for the own Qiskrypt's Ancilla Quantum Register, regarding a Qiskrypt's Classical Register.
        """

        """
        Dummy Assert Equal for the Unittest
        """
        self.assertEqual(True, True)

    def test_no_2_qiskrypt_ancilla_quantum_register_2_qubits(self):
        """
        Test Case #2:

        - Create a Qiskrypt's Ancilla Quantum Register, with 2 qubits.

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        ancilla_quantum_register_name = "anc_qu_reg"
        """
        Set the name of the Qiskrypt's Ancilla Quantum Register.
        """

        ancilla_quantum_register_num_qubits = 2
        """
        Set the number of qubits for the Qiskrypt's Ancilla Quantum Register.
        """

        qiskrypt_ancilla_quantum_register = \
            QiskryptAncillaQuantumRegister(name=ancilla_quantum_register_name,
                                           num_ancilla_qubits=ancilla_quantum_register_num_qubits,
                                           qiskit_ancilla_quantum_register=None)
        """
        Create a Qiskrypt's Ancilla Quantum Register, given its name and number of qubits.
        """

        assert(ancilla_quantum_register_name == qiskrypt_ancilla_quantum_register.get_name())
        """
        Assertion for the name of the Qiskrypt's Ancilla Quantum Register.
        """

        assert(ancilla_quantum_register_num_qubits == qiskrypt_ancilla_quantum_register.get_num_ancilla_qubits())
        """
        Assertion for the number of qubits of the Qiskrypt's Ancilla Quantum Register.
        """

        assert(isinstance(qiskrypt_ancilla_quantum_register.get_qiskit_ancilla_quantum_register(), AncillaRegister))
        """
        Assertion for the IBM's Qiskit Ancilla Register of the Qiskrypt's Ancilla Quantum Register.
        """

        assert(isinstance(qiskrypt_ancilla_quantum_register, QiskryptAncillaQuantumRegister))
        """
        Assertion for the own Qiskrypt's Ancilla Quantum Register, regarding a Qiskrypt's Ancilla Quantum Register.
        """

        assert(not isinstance(qiskrypt_ancilla_quantum_register, QiskryptAncillaFullyQuantumRegister))
        """
        Assertion for the own Qiskrypt's Ancilla Quantum Register, regarding a Qiskrypt's Ancilla Fully-Quantum Register.
        """

        assert(not isinstance(qiskrypt_ancilla_quantum_register, QiskryptAncillaSemiQuantumRegister))
        """
        Assertion for the own Qiskrypt's Ancilla Quantum Register, regarding a Qiskrypt's Ancilla Semi-Quantum Register.
        """

        assert(not isinstance(qiskrypt_ancilla_quantum_register, QiskryptClassicalRegister))
        """
        Assertion for the own Qiskrypt's Ancilla Quantum Register, regarding a Qiskrypt's Classical Register.
        """

        """
        Dummy Assert Equal for the Unittest
        """
        self.assertEqual(True, True)

    def test_no_3_qiskrypt_ancilla_quantum_register_4_qubits(self):
        """
        Test Case #3:

        - Create a Qiskrypt's Ancilla Quantum Register, with 4 qubits.

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        ancilla_quantum_register_name = "anc_qu_reg"
        """
        Set the name of the Qiskrypt's Ancilla Quantum Register.
        """

        ancilla_quantum_register_num_qubits = 4
        """
        Set the number of qubits for the Qiskrypt's Ancilla Quantum Register.
        """

        qiskrypt_ancilla_quantum_register = \
            QiskryptAncillaQuantumRegister(name=ancilla_quantum_register_name,
                                           num_ancilla_qubits=ancilla_quantum_register_num_qubits,
                                           qiskit_ancilla_quantum_register=None)
        """
        Create a Qiskrypt's Ancilla Quantum Register, given its name and number of qubits.
        """

        assert(ancilla_quantum_register_name == qiskrypt_ancilla_quantum_register.get_name())
        """
        Assertion for the name of the Qiskrypt's Ancilla Quantum Register.
        """

        assert(ancilla_quantum_register_num_qubits == qiskrypt_ancilla_quantum_register.get_num_ancilla_qubits())
        """
        Assertion for the number of qubits of the Qiskrypt's Ancilla Quantum Register.
        """

        assert(isinstance(qiskrypt_ancilla_quantum_register.get_qiskit_ancilla_quantum_register(), AncillaRegister))
        """
        Assertion for the IBM's Qiskit Ancilla Register of the Qiskrypt's Ancilla Quantum Register.
        """

        assert(isinstance(qiskrypt_ancilla_quantum_register, QiskryptAncillaQuantumRegister))
        """
        Assertion for the own Qiskrypt's Ancilla Quantum Register, regarding a Qiskrypt's Ancilla Quantum Register.
        """

        assert(not isinstance(qiskrypt_ancilla_quantum_register, QiskryptAncillaFullyQuantumRegister))
        """
        Assertion for the own Qiskrypt's Ancilla Quantum Register, regarding a Qiskrypt's Ancilla Fully-Quantum Register.
        """

        assert(not isinstance(qiskrypt_ancilla_quantum_register, QiskryptAncillaSemiQuantumRegister))
        """
        Assertion for the own Qiskrypt's Ancilla Quantum Register, regarding a Qiskrypt's Ancilla Semi-Quantum Register.
        """

        assert(not isinstance(qiskrypt_ancilla_quantum_register, QiskryptClassicalRegister))
        """
        Assertion for the own Qiskrypt's Ancilla Quantum Register, regarding a Qiskrypt's Classical Register.
        """

        """
        Dummy Assert Equal for the Unittest
        """
        self.assertEqual(True, True)

    def test_no_4_qiskrypt_ancilla_quantum_register_8_qubits(self):
        """
        Test Case #4:

        - Create a Qiskrypt's Ancilla Quantum Register, with 8 qubits.

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        ancilla_quantum_register_name = "anc_qu_reg"
        """
        Set the name of the Qiskrypt's Ancilla Quantum Register.
        """

        ancilla_quantum_register_num_qubits = 8
        """
        Set the number of qubits for the Qiskrypt's Ancilla Quantum Register.
        """

        qiskrypt_ancilla_quantum_register = \
            QiskryptAncillaQuantumRegister(name=ancilla_quantum_register_name,
                                           num_ancilla_qubits=ancilla_quantum_register_num_qubits,
                                           qiskit_ancilla_quantum_register=None)
        """
        Create a Qiskrypt's Ancilla Quantum Register, given its name and number of qubits.
        """

        assert(ancilla_quantum_register_name == qiskrypt_ancilla_quantum_register.get_name())
        """
        Assertion for the name of the Qiskrypt's Ancilla Quantum Register.
        """

        assert(ancilla_quantum_register_num_qubits == qiskrypt_ancilla_quantum_register.get_num_ancilla_qubits())
        """
        Assertion for the number of qubits of the Qiskrypt's Ancilla Quantum Register.
        """

        assert(isinstance(qiskrypt_ancilla_quantum_register.get_qiskit_ancilla_quantum_register(), AncillaRegister))
        """
        Assertion for the IBM's Qiskit Quantum Register of the Qiskrypt's Ancilla Quantum Register.
        """

        assert(isinstance(qiskrypt_ancilla_quantum_register, QiskryptAncillaQuantumRegister))
        """
        Assertion for the own Qiskrypt's Ancilla Quantum Register, regarding a Qiskrypt's Ancilla Quantum Register.
        """

        assert(not isinstance(qiskrypt_ancilla_quantum_register, QiskryptAncillaFullyQuantumRegister))
        """
        Assertion for the own Qiskrypt's Ancilla Quantum Register, regarding a Qiskrypt's Ancilla Fully-Quantum Register.
        """

        assert(not isinstance(qiskrypt_ancilla_quantum_register, QiskryptAncillaSemiQuantumRegister))
        """
        Assertion for the own Qiskrypt's Ancilla Quantum Register, regarding a Qiskrypt's Ancilla Semi-Quantum Register.
        """

        assert(not isinstance(qiskrypt_ancilla_quantum_register, QiskryptClassicalRegister))
        """
        Assertion for the own Qiskrypt's Ancilla Quantum Register, regarding a Qiskrypt's Classical Register.
        """

        """
        Dummy Assert Equal for the Unittest
        """
        self.assertEqual(True, True)


if __name__ == "__main__":
    """
    The Main Method for the Unitary Test.
    """

    qiskrypt_ancilla_quantum_register_test_cases = \
        TestLoader().loadTestsFromTestCase(QiskryptAncillaQuantumRegisterTests)
    """
    Load the Test Cases from the Unitary Tests for the Qiskrypt's Ancilla Quantum Register.
    """

    qiskrypt_ancilla_quantum_register_test_suite = \
        TestSuite([qiskrypt_ancilla_quantum_register_test_cases])
    """
    Load the Test Suite with the Test Cases for the Qiskrypt's Ancilla Quantum Register.
    """
