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

from qiskit import ClassicalRegister
"""
Import Classical Register from IBM's Qiskit.
"""

from src.quantum_regime.circuit.registers.quantum.QiskryptQuantumRegister import QiskryptQuantumRegister
"""
Import the Qiskrypt's Quantum Register.
"""

from src.quantum_regime.circuit.registers.quantum.fully_quantum.QiskryptFullyQuantumRegister import QiskryptFullyQuantumRegister
"""
Import the Qiskrypt's Fully-Quantum Register.
"""

from src.quantum_regime.circuit.registers.quantum.semi_quantum.QiskryptSemiQuantumRegister import QiskryptSemiQuantumRegister
"""
Import the Qiskrypt's Semi-Quantum Register.
"""

from src.quantum_regime.circuit.registers.classical.QiskryptClassicalRegister import QiskryptClassicalRegister
"""
Import the Qiskrypt's Classical Register.
"""


class QiskryptClassicalRegisterTests(TestCase):
    """
    Object Class of the Unitary Tests for the Qiskrypt's Classical Register.
    """

    def test_no_1_qiskrypt_classical_register_1_bit(self):
        """
        Test Case #1:

        - Create a Qiskrypt's Classical Register, with 1 bit.

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        classical_register_name = "cl_reg"
        """
        Set the name of the Qiskrypt's Classical Register.
        """

        classical_register_num_bits = 1
        """
        Set the number of bits for the Qiskrypt's Classical Register.
        """

        qiskrypt_classical_register = \
            QiskryptClassicalRegister(name=classical_register_name,
                                      num_bits=classical_register_num_bits,
                                      qiskit_classical_register=None)
        """
        Create a Qiskrypt's Classical Register, given its name and number of bits.
        """

        assert(classical_register_name == qiskrypt_classical_register.get_name())
        """
        Assertion for the name of the Qiskrypt's Classical Register.
        """

        assert(classical_register_num_bits == qiskrypt_classical_register.get_num_bits())
        """
        Assertion for the number of bits of the Qiskrypt's Classical Register.
        """

        assert(isinstance(qiskrypt_classical_register.get_qiskit_classical_register(), ClassicalRegister))
        """
        Assertion for the IBM's Qiskit Classical Register of the Qiskrypt's Classical Register.
        """

        assert(not isinstance(qiskrypt_classical_register, QiskryptQuantumRegister))
        """
        Assertion for the own Qiskrypt's Classical Register, regarding a Qiskrypt's Quantum Register.
        """

        assert(not isinstance(qiskrypt_classical_register, QiskryptFullyQuantumRegister))
        """
        Assertion for the own Qiskrypt's Classical Register, regarding a Qiskrypt's Fully-Quantum Register.
        """

        assert(not isinstance(qiskrypt_classical_register, QiskryptSemiQuantumRegister))
        """
        Assertion for the own Qiskrypt's Classical Register, regarding a Qiskrypt's Semi-Quantum Register.
        """

        assert(isinstance(qiskrypt_classical_register, QiskryptClassicalRegister))
        """
        Assertion for the own Qiskrypt's Classical Register, regarding a Qiskrypt's Classical Register.
        """

        """
        Dummy Assert Equal for the Unittest
        """
        self.assertEqual(True, True)

    def test_no_2_qiskrypt_classical_register_2_bits(self):
        """
        Test Case #2:

        - Create a Qiskrypt's Classical Register, with 2 bits.

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        classical_register_name = "cl_reg"
        """
        Set the name of the Qiskrypt's Classical Register.
        """

        classical_register_num_bits = 2
        """
        Set the number of bits for the Qiskrypt's Classical Register.
        """

        qiskrypt_classical_register = \
            QiskryptClassicalRegister(name=classical_register_name,
                                      num_bits=classical_register_num_bits,
                                      qiskit_classical_register=None)
        """
        Create a Qiskrypt's Classical Register, given its name and number of bits.
        """

        assert(classical_register_name == qiskrypt_classical_register.get_name())
        """
        Assertion for the name of the Qiskrypt's Classical Register.
        """

        assert(classical_register_num_bits == qiskrypt_classical_register.get_num_bits())
        """
        Assertion for the number of bits of the Qiskrypt's Classical Register.
        """

        assert(isinstance(qiskrypt_classical_register.get_qiskit_classical_register(), ClassicalRegister))
        """
        Assertion for the IBM's Qiskit Classical Register of the Qiskrypt's Classical Register.
        """

        assert(not isinstance(qiskrypt_classical_register, QiskryptQuantumRegister))
        """
        Assertion for the own Qiskrypt's Classical Register, regarding a Qiskrypt's Quantum Register.
        """

        assert(not isinstance(qiskrypt_classical_register, QiskryptFullyQuantumRegister))
        """
        Assertion for the own Qiskrypt's Classical Register, regarding a Qiskrypt's Fully-Quantum Register.
        """

        assert(not isinstance(qiskrypt_classical_register, QiskryptSemiQuantumRegister))
        """
        Assertion for the own Qiskrypt's Classical Register, regarding a Qiskrypt's Semi-Quantum Register.
        """

        assert(isinstance(qiskrypt_classical_register, QiskryptClassicalRegister))
        """
        Assertion for the own Qiskrypt's Classical Register, regarding a Qiskrypt's Classical Register.
        """

        """
        Dummy Assert Equal for the Unittest
        """
        self.assertEqual(True, True)

    def test_no_3_qiskrypt_classical_register_4_bits(self):
        """
        Test Case #3:

        - Create a Qiskrypt's Classical Register, with 4 bits.

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        classical_register_name = "cl_reg"
        """
        Set the name of the Qiskrypt's Classical Register.
        """

        classical_register_num_bits = 4
        """
        Set the number of bits for the Qiskrypt's Classical Register.
        """

        qiskrypt_classical_register = \
            QiskryptClassicalRegister(name=classical_register_name,
                                      num_bits=classical_register_num_bits,
                                      qiskit_classical_register=None)
        """
        Create a Qiskrypt's Classical Register, given its name and number of bits.
        """

        assert(classical_register_name == qiskrypt_classical_register.get_name())
        """
        Assertion for the name of the Qiskrypt's Classical Register.
        """

        assert(classical_register_num_bits == qiskrypt_classical_register.get_num_bits())
        """
        Assertion for the number of bits of the Qiskrypt's Classical Register.
        """

        assert(isinstance(qiskrypt_classical_register.get_qiskit_classical_register(), ClassicalRegister))
        """
        Assertion for the IBM's Qiskit Classical Register of the Qiskrypt's Classical Register.
        """

        assert(not isinstance(qiskrypt_classical_register, QiskryptQuantumRegister))
        """
        Assertion for the own Qiskrypt's Classical Register, regarding a Qiskrypt's Quantum Register.
        """

        assert(not isinstance(qiskrypt_classical_register, QiskryptFullyQuantumRegister))
        """
        Assertion for the own Qiskrypt's Classical Register, regarding a Qiskrypt's Fully-Quantum Register.
        """

        assert(not isinstance(qiskrypt_classical_register, QiskryptSemiQuantumRegister))
        """
        Assertion for the own Qiskrypt's Classical Register, regarding a Qiskrypt's Semi-Quantum Register.
        """

        assert(isinstance(qiskrypt_classical_register, QiskryptClassicalRegister))
        """
        Assertion for the own Qiskrypt's Classical Register, regarding a Qiskrypt's Classical Register.
        """

        """
        Dummy Assert Equal for the Unittest
        """
        self.assertEqual(True, True)

    def test_no_4_qiskrypt_classical_register_8_bits(self):
        """
        Test Case #4:

        - Create a Qiskrypt's Classical Register, with 8 bits.

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        classical_register_name = "cl_reg"
        """
        Set the name of the Qiskrypt's Classical Register.
        """

        classical_register_num_bits = 8
        """
        Set the number of bits for the Qiskrypt's Classical Register.
        """

        qiskrypt_classical_register = \
            QiskryptClassicalRegister(name=classical_register_name,
                                      num_bits=classical_register_num_bits,
                                      qiskit_classical_register=None)
        """
        Create a Qiskrypt's Classical Register, given its name and number of bits.
        """

        assert(classical_register_name == qiskrypt_classical_register.get_name())
        """
        Assertion for the name of the Qiskrypt's Classical Register.
        """

        assert(classical_register_num_bits == qiskrypt_classical_register.get_num_bits())
        """
        Assertion for the number of bits of the Qiskrypt's Classical Register.
        """

        assert(isinstance(qiskrypt_classical_register.get_qiskit_classical_register(), ClassicalRegister))
        """
        Assertion for the IBM's Qiskit Classical Register of the Qiskrypt's Classical Register.
        """

        assert(not isinstance(qiskrypt_classical_register, QiskryptQuantumRegister))
        """
        Assertion for the own Qiskrypt's Classical Register, regarding a Qiskrypt's Quantum Register.
        """

        assert(not isinstance(qiskrypt_classical_register, QiskryptFullyQuantumRegister))
        """
        Assertion for the own Qiskrypt's Classical Register, regarding a Qiskrypt's Fully-Quantum Register.
        """

        assert(not isinstance(qiskrypt_classical_register, QiskryptSemiQuantumRegister))
        """
        Assertion for the own Qiskrypt's Classical Register, regarding a Qiskrypt's Semi-Quantum Register.
        """

        assert(isinstance(qiskrypt_classical_register, QiskryptClassicalRegister))
        """
        Assertion for the own Qiskrypt's Classical Register, regarding a Qiskrypt's Classical Register.
        """

        """
        Dummy Assert Equal for the Unittest
        """
        self.assertEqual(True, True)


if __name__ == "__main__":
    """
    The Main Method for the Unitary Test.
    """

    qiskrypt_classical_register_test_cases = \
        TestLoader().loadTestsFromTestCase(QiskryptClassicalRegisterTests)
    """
    Load the Test Cases from the Unitary Tests for the Qiskrypt's Classical Register.
    """

    qiskrypt_classical_register_test_suite = \
        TestSuite([qiskrypt_classical_register_test_cases])
    """
    Load the Test Suite with the Test Cases for the Qiskrypt's Classical Register.
    """
