"""

Copyrights:\n
- © Qiskrypt, 2021 - All rights reserved.\n

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

"""

"""
Import required Libraries and Packages.
"""

from unittest import TestCase, TestLoader, TestSuite
"""
Import TestCase, TestLoader and TestSuite from Unittest.
"""

from qiskit import QuantumRegister
"""
Import Quantum Register from IBM's Qiskit.
"""

from qiskit import ClassicalRegister
"""
Import Classical Register from IBM's Qiskit.
"""

from src.circuit.registers.quantum.QiskryptQuantumRegister import QiskryptQuantumRegister
"""
Import the Qiskrypt's Quantum Register.
"""

from src.circuit.registers.quantum.fully_quantum.QiskryptFullyQuantumRegister import QiskryptFullyQuantumRegister
"""
Import the Qiskrypt's Fully-Quantum Register.
"""

from src.circuit.registers.quantum.semi_quantum.QiskryptSemiQuantumRegister import QiskryptSemiQuantumRegister
"""
Import the Qiskrypt's Semi-Quantum Register.
"""

from src.circuit.registers.classical.QiskryptClassicalRegister import QiskryptClassicalRegister
"""
Import the Qiskrypt's Classical Register.
"""

from src.circuit.QiskryptQuantumCircuit import QiskryptQuantumCircuit
"""
Import the Qiskrypt's Quantum Circuit.
"""


class QiskryptQuantumCircuitTests(TestCase):
    """
    Object Class of the Unitary Tests for the Qiskrypt's Quantum Circuit.
    """

    def test_no_1_qiskrypt_quantum_circuit_1_quantum_register_1_qubit_and_1_classical_register_1_bit(self):
        """
        Test Case #1:

        - Create a Qiskrypt's Quantum Circuit with:
           (i) 1 Quantum Register (with 1 qubit).
          (ii) 1 Classical Register (with 1 bit).

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        quantum_register_name = "qu_reg"
        """
        Set the name of the Qiskrypt's Quantum Register.
        """

        quantum_register_num_qubits = 1
        """
        Set the number of qubits for the Qiskrypt's Quantum Register.
        """

        qiskrypt_quantum_register = \
            QiskryptQuantumRegister(name=quantum_register_name,
                                    num_qubits=quantum_register_num_qubits,
                                    quantum_register=None)
        """
        Create a Qiskrypt's Quantum Register, given its name and number of qubits.
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
                                      classical_register=None)
        """
        Create a Qiskrypt's Classical Register, given its name and number of bits.
        """

        quantum_circuit_name = "qu_circ"
        """
        Set the name of the Qiskrypt's Quantum Circuit.
        """

        qiskrypt_quantum_circuit = \
            QiskryptQuantumCircuit(name=quantum_circuit_name,
                                   quantum_registers=[qiskrypt_quantum_register],
                                   fully_quantum_registers=None,
                                   semi_quantum_registers=None,
                                   classical_registers=[qiskrypt_classical_register],
                                   global_phase=0)
        """
        Create a Qiskrypt's Quantum Circuit, given its name,
        Qiskrypt's Quantum Registers,
        Qiskrypt's Fully-Quantum Registers, Qiskrypt's Semi-Quantum Registers,
        Qiskrypt's Classical Registers and
        Global Phase.
        """

        assert(qiskrypt_quantum_circuit.get_name() == quantum_circuit_name)
        """
        Assertion for the name of the Qiskrypt's Quantum Circuit.
        """

        for qiskrypt_quantum_register in qiskrypt_quantum_circuit.get_qiskrypt_quantum_registers():
            """
            For each supposed Qiskrypt's Quantum Register in the Qiskrypt's Quantum Circuit.
            """

            assert(isinstance(qiskrypt_quantum_register, QiskryptQuantumRegister))
            """
            Assertion for the current Qiskrypt's Quantum Register of
            the Qiskrypt's Quantum Circuit be an actual Qiskrypt's Quantum Register.
            """

            assert(not isinstance(qiskrypt_quantum_register, QiskryptFullyQuantumRegister))
            """
            Assertion for the current Qiskrypt's Quantum Register of
            the Qiskrypt's Quantum Circuit do not be an actual Qiskrypt's Fully-Quantum Register.
            """

            assert(not isinstance(qiskrypt_quantum_register, QiskryptSemiQuantumRegister))
            """
            Assertion for the current Qiskrypt's Quantum Register of
            the Qiskrypt's Quantum Circuit do not be an actual Qiskrypt's Semi-Quantum Register.
            """

            assert(isinstance(qiskrypt_quantum_register.get_quantum_register(), QuantumRegister))
            """
            Assertion for the current Qiskrypt's Quantum Register of
            the Qiskrypt's Quantum Circuit has an IBM's Qiskit Quantum Register.
            """

        for qiskrypt_classical_register in qiskrypt_quantum_circuit.get_qiskrypt_classical_registers():
            """
            For each supposed Qiskrypt's Classical Register in the Qiskrypt's Quantum Circuit.
            """

            assert(isinstance(qiskrypt_classical_register, QiskryptClassicalRegister))
            """
            Assertion for the current Qiskrypt's Classical Register of
            the Qiskrypt's Quantum Circuit be an actual Qiskrypt's Classical Register.
            """

            assert(isinstance(qiskrypt_classical_register.get_classical_register(), ClassicalRegister))
            """
            Assertion for the current Qiskrypt's Classical Register of
            the Qiskrypt's Quantum Circuit has an IBM's Qiskit Classical Register.
            """

        """
        Dummy Assert Equal for the Unittest
        """
        self.assertEqual(True, True)

    def test_no_2_qiskrypt_quantum_circuit_2_quantum_registers_1_qubit_and_1_classical_register_1_bit(self):
        """
        Test Case #2:

        - Create a Qiskrypt's Quantum Circuit with:
           (i) 2 Quantum Registers (each one with 1 qubit).
          (ii) 1 Classical Register (with 1 bit).

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        quantum_register_1_name = "qu_reg_1"
        """
        Set the name of the Qiskrypt's Quantum Register no. 1.
        """

        quantum_register_1_num_qubits = 1
        """
        Set the number of qubits for the Qiskrypt's Quantum Register no. 1.
        """

        qiskrypt_quantum_register_1 = \
            QiskryptQuantumRegister(name=quantum_register_1_name,
                                    num_qubits=quantum_register_1_num_qubits,
                                    quantum_register=None)
        """
        Create a Qiskrypt's Quantum Register no. 2, given its name and number of qubits.
        """

        quantum_register_2_name = "qu_reg_2"
        """
        Set the name of the Qiskrypt's Quantum Register no. 2.
        """

        quantum_register_2_num_qubits = 1
        """
        Set the number of qubits for the Qiskrypt's Quantum Register no. 2.
        """

        qiskrypt_quantum_register_2 = \
            QiskryptQuantumRegister(name=quantum_register_2_name,
                                    num_qubits=quantum_register_2_num_qubits,
                                    quantum_register=None)
        """
        Create a Qiskrypt's Quantum Register no. 2, given its name and number of qubits.
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
                                      classical_register=None)
        """
        Create a Qiskrypt's Classical Register, given its name and number of bits.
        """

        quantum_circuit_name = "qu_circ"
        """
        Set the name of the Qiskrypt's Quantum Circuit.
        """

        qiskrypt_quantum_circuit = \
            QiskryptQuantumCircuit(name=quantum_circuit_name,
                                   quantum_registers=[qiskrypt_quantum_register_1, qiskrypt_quantum_register_2],
                                   fully_quantum_registers=None,
                                   semi_quantum_registers=None,
                                   classical_registers=[qiskrypt_classical_register],
                                   global_phase=0)
        """
        Create a Qiskrypt's Quantum Circuit, given its name,
        Qiskrypt's Quantum Registers,
        Qiskrypt's Fully-Quantum Registers, Qiskrypt's Semi-Quantum Registers,
        Qiskrypt's Classical Registers and
        Global Phase.
        """

        assert(qiskrypt_quantum_circuit.get_name() == quantum_circuit_name)
        """
        Assertion for the name of the Qiskrypt's Quantum Circuit.
        """

        """
        Dummy Assert Equal for the Unittest
        """
        self.assertEqual(True, True)


if __name__ == "__main__":
    """
    The Main Method for the Unitary Test.
    """

    qiskrypt_quantum_circuit_test_cases = \
        TestLoader().loadTestsFromTestCase(QiskryptQuantumCircuitTests)
    """
    Load the Test Cases from the Unitary Tests for the Qiskrypt's Quantum Circuit.
    """

    qiskrypt_quantum_circuit_test_suite = \
        TestSuite([qiskrypt_quantum_circuit_test_cases])
    """
    Load the Test Suite with the Test Cases for the Qiskrypt's Quantum Circuit.
    """