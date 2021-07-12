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

from qiskit import AncillaRegister
"""
Import Ancilla Register from IBM's Qiskit.
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

from src.circuit.registers.quantum.QiskryptAncillaQuantumRegister import QiskryptAncillaQuantumRegister
"""
Import the Qiskrypt's Ancilla Quantum Register.
"""

from src.circuit.registers.quantum.fully_quantum.QiskryptAncillaFullyQuantumRegister import QiskryptAncillaFullyQuantumRegister
"""
Import the Qiskrypt's Ancilla Fully-Quantum Register.
"""

from src.circuit.registers.quantum.semi_quantum.QiskryptAncillaSemiQuantumRegister import QiskryptAncillaSemiQuantumRegister
"""
Import the Qiskrypt's Ancilla Semi-Quantum Register.
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

    def test_no_1_creation_qiskrypt_quantum_circuit_with_1_quantum_register_1_qubit(self):
        """
        Test Case #1:

        - Create a Qiskrypt's Quantum Circuit with:
           (i) 1 Quantum Register (with 1 qubit).

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

        quantum_circuit_name = "qu_circ"
        """
        Set the name of the Qiskrypt's Quantum Circuit.
        """

        qiskrypt_quantum_circuit = \
            QiskryptQuantumCircuit(name=quantum_circuit_name,
                                   quantum_registers=[qiskrypt_quantum_register],
                                   fully_quantum_registers=None,
                                   semi_quantum_registers=None,
                                   ancilla_quantum_registers=None,
                                   ancilla_fully_quantum_registers=None,
                                   ancilla_semi_quantum_registers=None,
                                   classical_registers=None,
                                   global_phase=0)
        """
        Create a Qiskrypt's Quantum Circuit, given its name,
        Qiskrypt's Quantum Registers, Qiskrypt's Fully-Quantum Registers,
        Qiskrypt's Semi-Quantum Registers,
        Qiskrypt's Ancilla Quantum Registers, Qiskrypt's Ancilla Fully-Quantum Registers,
        Qiskrypt's Ancilla Semi-Quantum Registers,
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

            assert(not isinstance(qiskrypt_quantum_register, QiskryptAncillaQuantumRegister))
            """
            Assertion for the current Qiskrypt's Quantum Register of
            the Qiskrypt's Quantum Circuit do not be an actual Qiskrypt's Ancilla Quantum Register.
            """

            assert(not isinstance(qiskrypt_quantum_register, QiskryptAncillaFullyQuantumRegister))
            """
            Assertion for the current Qiskrypt's Quantum Register of
            the Qiskrypt's Quantum Circuit do not be an actual Qiskrypt's Ancilla Fully-Quantum Register.
            """

            assert(not isinstance(qiskrypt_quantum_register, QiskryptAncillaSemiQuantumRegister))
            """
            Assertion for the current Qiskrypt's Quantum Register of
            the Qiskrypt's Quantum Circuit do not be an actual Qiskrypt's Ancilla Semi-Quantum Register.
            """

            assert(not isinstance(qiskrypt_quantum_register, QiskryptClassicalRegister))
            """
            Assertion for the current Qiskrypt's Quantum Register of
            the Qiskrypt's Quantum Circuit do not be an actual Qiskrypt's Classical Register.
            """

            assert(isinstance(qiskrypt_quantum_register.get_quantum_register(), QuantumRegister))
            """
            Assertion for the current Qiskrypt's Quantum Register of
            the Qiskrypt's Quantum Circuit has an IBM's Qiskit Quantum Register.
            """

        assert(qiskrypt_quantum_circuit.get_total_num_qubits() == quantum_register_num_qubits)
        """
        Assertion for the total number of qubits of
        all the Qiskrypt's Quantum Registers of the Qiskrypt's Quantum Circuit.
        """

        assert(qiskrypt_quantum_circuit.get_num_qubits_in_qiskit_quantum_register(0) == quantum_register_num_qubits)
        """
        Assertion for the number of qubits of
        the 1st Qiskrypt's Quantum Register of the Qiskrypt's Quantum Circuit.
        """

        """
        Dummy Assert Equal for the Unittest
        """
        self.assertEqual(True, True)

    def test_no_2_creation_qiskrypt_quantum_circuit_with_1_fully_quantum_register_1_qubit(self):
        """
        Test Case #2:

        - Create a Qiskrypt's Quantum Circuit with:
           (i) 1 Fully-Quantum Register (with 1 qubit).

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        fully_quantum_register_name = "fully_qu_reg"
        """
        Set the name of the Qiskrypt's Fully-Quantum Register.
        """

        fully_quantum_register_num_qubits = 1
        """
        Set the number of qubits for the Qiskrypt's Fully-Quantum Register.
        """

        qiskrypt_fully_quantum_register = \
            QiskryptFullyQuantumRegister(name=fully_quantum_register_name,
                                         num_qubits=fully_quantum_register_num_qubits,
                                         quantum_register=None)
        """
        Create a Qiskrypt's Fully-Quantum Register, given its name and number of qubits.
        """

        quantum_circuit_name = "qu_circ"
        """
        Set the name of the Qiskrypt's Quantum Circuit.
        """

        qiskrypt_quantum_circuit = \
            QiskryptQuantumCircuit(name=quantum_circuit_name,
                                   quantum_registers=None,
                                   fully_quantum_registers=[qiskrypt_fully_quantum_register],
                                   semi_quantum_registers=None,
                                   ancilla_quantum_registers=None,
                                   ancilla_fully_quantum_registers=None,
                                   ancilla_semi_quantum_registers=None,
                                   classical_registers=None,
                                   global_phase=0)
        """
        Create a Qiskrypt's Quantum Circuit, given its name,
        Qiskrypt's Quantum Registers, Qiskrypt's Fully-Quantum Registers,
        Qiskrypt's Semi-Quantum Registers,
        Qiskrypt's Ancilla Quantum Registers, Qiskrypt's Ancilla Fully-Quantum Registers,
        Qiskrypt's Ancilla Semi-Quantum Registers,
        Qiskrypt's Classical Registers and
        Global Phase.
        """

        assert(qiskrypt_quantum_circuit.get_name() == quantum_circuit_name)
        """
        Assertion for the name of the Qiskrypt's Quantum Circuit.
        """

        for qiskrypt_fully_quantum_register in qiskrypt_quantum_circuit.get_qiskrypt_fully_quantum_registers():
            """
            For each supposed Qiskrypt's Fully-Quantum Register in the Qiskrypt's Quantum Circuit.
            """

            assert(isinstance(qiskrypt_fully_quantum_register, QiskryptQuantumRegister))
            """
            Assertion for the current Qiskrypt's Fully-Quantum Register of
            the Qiskrypt's Quantum Circuit be an actual Qiskrypt's Quantum Register.
            """

            assert(isinstance(qiskrypt_fully_quantum_register, QiskryptFullyQuantumRegister))
            """
            Assertion for the current Qiskrypt's Fully-Quantum Register of
            the Qiskrypt's Quantum Circuit be an actual Qiskrypt's Fully-Quantum Register.
            """

            assert(not isinstance(qiskrypt_fully_quantum_register, QiskryptSemiQuantumRegister))
            """
            Assertion for the current Qiskrypt's Fully-Quantum Register of
            the Qiskrypt's Quantum Circuit do not be an actual Qiskrypt's Semi-Quantum Register.
            """

            assert(not isinstance(qiskrypt_fully_quantum_register, QiskryptAncillaQuantumRegister))
            """
            Assertion for the current Qiskrypt's Fully-Quantum Register of
            the Qiskrypt's Quantum Circuit do not be an actual Qiskrypt's Ancilla Quantum Register.
            """

            assert(not isinstance(qiskrypt_fully_quantum_register, QiskryptAncillaFullyQuantumRegister))
            """
            Assertion for the current Qiskrypt's Fully-Quantum Register of
            the Qiskrypt's Quantum Circuit do not be an actual Qiskrypt's Ancilla Fully-Quantum Register.
            """

            assert(not isinstance(qiskrypt_fully_quantum_register, QiskryptAncillaSemiQuantumRegister))
            """
            Assertion for the current Qiskrypt's Fully-Quantum Register of
            the Qiskrypt's Quantum Circuit do not be an actual Qiskrypt's Ancilla Semi-Quantum Register.
            """

            assert(not isinstance(qiskrypt_fully_quantum_register, QiskryptClassicalRegister))
            """
            Assertion for the current Qiskrypt's Fully-Quantum Register of
            the Qiskrypt's Quantum Circuit do not be an actual Qiskrypt's Classical Register.
            """

            assert(isinstance(qiskrypt_fully_quantum_register.get_quantum_register(), QuantumRegister))
            """
            Assertion for the current Qiskrypt's Fully-Quantum Register of
            the Qiskrypt's Quantum Circuit has an IBM's Qiskit Quantum Register.
            """

        assert(qiskrypt_quantum_circuit.get_total_num_qubits() == fully_quantum_register_num_qubits)
        """
        Assertion for the total number of qubits of
        all the Qiskrypt's Fully-Quantum Registers of the Qiskrypt's Quantum Circuit.
        """

        assert(qiskrypt_quantum_circuit.get_num_qubits_in_qiskit_quantum_register(0) == fully_quantum_register_num_qubits)
        """
        Assertion for the number of qubits of
        the 1st Qiskrypt's Quantum Register of the Qiskrypt's Quantum Circuit.
        """

        """
        Dummy Assert Equal for the Unittest
        """
        self.assertEqual(True, True)

    def test_no_3_creation_qiskrypt_quantum_circuit_with_1_semi_quantum_register_1_qubit(self):
        """
        Test Case #3:

        - Create a Qiskrypt's Quantum Circuit with:
           (i) 1 Semi-Quantum Register (with 1 qubit).

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        semi_quantum_register_name = "semi_qu_reg"
        """
        Set the name of the Qiskrypt's Semi-Quantum Register.
        """

        semi_quantum_register_num_qubits = 1
        """
        Set the number of qubits for the Qiskrypt's Semi-Quantum Register.
        """

        qiskrypt_semi_quantum_register = \
            QiskryptSemiQuantumRegister(name=semi_quantum_register_name,
                                        num_qubits=semi_quantum_register_num_qubits,
                                        quantum_register=None)
        """
        Create a Qiskrypt's Semi-Quantum Register, given its name and number of qubits.
        """

        quantum_circuit_name = "qu_circ"
        """
        Set the name of the Qiskrypt's Quantum Circuit.
        """

        qiskrypt_quantum_circuit = \
            QiskryptQuantumCircuit(name=quantum_circuit_name,
                                   quantum_registers=None,
                                   fully_quantum_registers=None,
                                   semi_quantum_registers=[qiskrypt_semi_quantum_register],
                                   ancilla_quantum_registers=None,
                                   ancilla_fully_quantum_registers=None,
                                   ancilla_semi_quantum_registers=None,
                                   classical_registers=None,
                                   global_phase=0)
        """
        Create a Qiskrypt's Quantum Circuit, given its name,
        Qiskrypt's Quantum Registers, Qiskrypt's Fully-Quantum Registers,
        Qiskrypt's Semi-Quantum Registers,
        Qiskrypt's Ancilla Quantum Registers, Qiskrypt's Ancilla Fully-Quantum Registers,
        Qiskrypt's Ancilla Semi-Quantum Registers,
        Qiskrypt's Classical Registers and
        Global Phase.
        """

        assert(qiskrypt_quantum_circuit.get_name() == quantum_circuit_name)
        """
        Assertion for the name of the Qiskrypt's Quantum Circuit.
        """

        for qiskrypt_semi_quantum_register in qiskrypt_quantum_circuit.get_qiskrypt_semi_quantum_registers():
            """
            For each supposed Qiskrypt's Semi-Quantum Register in the Qiskrypt's Quantum Circuit.
            """

            assert(isinstance(qiskrypt_semi_quantum_register, QiskryptQuantumRegister))
            """
            Assertion for the current Qiskrypt's Semi-Quantum Register of
            the Qiskrypt's Quantum Circuit be an actual Qiskrypt's Quantum Register.
            """

            assert(not isinstance(qiskrypt_semi_quantum_register, QiskryptFullyQuantumRegister))
            """
            Assertion for the current Qiskrypt's Semi-Quantum Register of
            the Qiskrypt's Quantum Circuit do not be an actual Qiskrypt's Fully-Quantum Register.
            """

            assert(isinstance(qiskrypt_semi_quantum_register, QiskryptSemiQuantumRegister))
            """
            Assertion for the current Qiskrypt's Semi-Quantum Register of
            the Qiskrypt's Quantum Circuit be an actual Qiskrypt's Semi-Quantum Register.
            """

            assert(not isinstance(qiskrypt_semi_quantum_register, QiskryptAncillaQuantumRegister))
            """
            Assertion for the current Qiskrypt's Semi-Quantum Register of
            the Qiskrypt's Quantum Circuit do not be an actual Qiskrypt's Ancilla Quantum Register.
            """

            assert(not isinstance(qiskrypt_semi_quantum_register, QiskryptAncillaFullyQuantumRegister))
            """
            Assertion for the current Qiskrypt's Semi-Quantum Register of
            the Qiskrypt's Quantum Circuit do not be an actual Qiskrypt's Ancilla Fully-Quantum Register.
            """

            assert(not isinstance(qiskrypt_semi_quantum_register, QiskryptAncillaSemiQuantumRegister))
            """
            Assertion for the current Qiskrypt's Semi-Quantum Register of
            the Qiskrypt's Quantum Circuit do not be an actual Qiskrypt's Ancilla Semi-Quantum Register.
            """

            assert(not isinstance(qiskrypt_semi_quantum_register, QiskryptClassicalRegister))
            """
            Assertion for the current Qiskrypt's Semi-Quantum Register of
            the Qiskrypt's Quantum Circuit be an actual Qiskrypt's Classical Register.
            """

            assert(isinstance(qiskrypt_semi_quantum_register.get_quantum_register(), QuantumRegister))
            """
            Assertion for the current Qiskrypt's Semi-Quantum Register of
            the Qiskrypt's Quantum Circuit has an IBM's Qiskit Quantum Register.
            """

        assert(qiskrypt_quantum_circuit.get_total_num_qubits() == semi_quantum_register_num_qubits)
        """
        Assertion for the total number of qubits of
        all the Qiskrypt's Semi-Quantum Registers of the Qiskrypt's Quantum Circuit.
        """

        assert(qiskrypt_quantum_circuit.get_num_qubits_in_qiskit_quantum_register(0) == semi_quantum_register_num_qubits)
        """
        Assertion for the number of qubits of
        the 1st Qiskrypt's Quantum Register of the Qiskrypt's Quantum Circuit.
        """

        """
        Dummy Assert Equal for the Unittest
        """
        self.assertEqual(True, True)

    def test_no_4_creation_qiskrypt_quantum_circuit_with_1_ancilla_quantum_register_1_qubit(self):
        """
        Test Case #4:

        - Create a Qiskrypt's Quantum Circuit with:
           (i) 1 Ancilla Quantum Register (with 1 qubit).

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
                                           ancilla_quantum_register=None)
        """
        Create a Qiskrypt's Ancilla Quantum Register, given its name and number of qubits.
        """

        quantum_circuit_name = "qu_circ"
        """
        Set the name of the Qiskrypt's Quantum Circuit.
        """

        qiskrypt_quantum_circuit = \
            QiskryptQuantumCircuit(name=quantum_circuit_name,
                                   quantum_registers=None,
                                   fully_quantum_registers=None,
                                   semi_quantum_registers=None,
                                   ancilla_quantum_registers=[qiskrypt_ancilla_quantum_register],
                                   ancilla_fully_quantum_registers=None,
                                   ancilla_semi_quantum_registers=None,
                                   classical_registers=None,
                                   global_phase=0)
        """
        Create a Qiskrypt's Quantum Circuit, given its name,
        Qiskrypt's Quantum Registers, Qiskrypt's Fully-Quantum Registers,
        Qiskrypt's Semi-Quantum Registers,
        Qiskrypt's Ancilla Quantum Registers, Qiskrypt's Ancilla Fully-Quantum Registers,
        Qiskrypt's Ancilla Semi-Quantum Registers,
        Qiskrypt's Classical Registers and
        Global Phase.
        """

        assert(qiskrypt_quantum_circuit.get_name() == quantum_circuit_name)
        """
        Assertion for the name of the Qiskrypt's Quantum Circuit.
        """

        for qiskrypt_ancilla_quantum_register in qiskrypt_quantum_circuit.get_qiskrypt_ancilla_quantum_registers():
            """
            For each supposed Qiskrypt's Ancilla Quantum Register in the Qiskrypt's Quantum Circuit.
            """

            assert(not isinstance(qiskrypt_ancilla_quantum_register, QiskryptQuantumRegister))
            """
            Assertion for the current Qiskrypt's Ancilla Quantum Register of
            the Qiskrypt's Quantum Circuit do not be an actual Qiskrypt's Quantum Register.
            """

            assert(not isinstance(qiskrypt_ancilla_quantum_register, QiskryptFullyQuantumRegister))
            """
            Assertion for the current Qiskrypt's Ancilla Quantum Register of
            the Qiskrypt's Quantum Circuit do not be an actual Qiskrypt's Fully-Quantum Register.
            """

            assert(not isinstance(qiskrypt_ancilla_quantum_register, QiskryptSemiQuantumRegister))
            """
            Assertion for the current Qiskrypt's Ancilla Quantum Register of
            the Qiskrypt's Quantum Circuit do not be an actual Qiskrypt's Semi-Quantum Register.
            """

            assert(isinstance(qiskrypt_ancilla_quantum_register, QiskryptAncillaQuantumRegister))
            """
            Assertion for the current Qiskrypt's Ancilla Quantum Register of
            the Qiskrypt's Quantum Circuit be an actual Qiskrypt's Ancilla Quantum Register.
            """

            assert(not isinstance(qiskrypt_ancilla_quantum_register, QiskryptAncillaFullyQuantumRegister))
            """
            Assertion for the current Qiskrypt's Ancilla Quantum Register of
            the Qiskrypt's Quantum Circuit do not be an actual Qiskrypt's Ancilla Fully-Quantum Register.
            """

            assert(not isinstance(qiskrypt_ancilla_quantum_register, QiskryptAncillaSemiQuantumRegister))
            """
            Assertion for the current Qiskrypt's Ancilla Quantum Register of
            the Qiskrypt's Quantum Circuit do not be an actual Qiskrypt's Ancilla Semi-Quantum Register.
            """

            assert(not isinstance(qiskrypt_ancilla_quantum_register, QiskryptClassicalRegister))
            """
            Assertion for the current Qiskrypt's Ancilla Quantum Register of
            the Qiskrypt's Quantum Circuit do not be an actual Qiskrypt's Classical Register.
            """

            assert(isinstance(qiskrypt_ancilla_quantum_register.get_ancilla_quantum_register(), AncillaRegister))
            """
            Assertion for the current Qiskrypt's Ancilla Quantum Register of
            the Qiskrypt's Quantum Circuit has an IBM's Qiskit Ancilla Register.
            """

        assert(qiskrypt_quantum_circuit.get_total_num_qubits() == ancilla_quantum_register_num_qubits)
        """
        Assertion for the total number of qubits of
        all the Qiskrypt's Ancilla Quantum Registers of the Qiskrypt's Quantum Circuit.
        """

        assert(qiskrypt_quantum_circuit.get_num_qubits_in_qiskit_quantum_register(0) == ancilla_quantum_register_num_qubits)
        """
        Assertion for the number of qubits of
        the 1st Qiskrypt's Quantum Register of the Qiskrypt's Quantum Circuit.
        """

        """
        Dummy Assert Equal for the Unittest
        """
        self.assertEqual(True, True)

    def test_no_5_creation_qiskrypt_quantum_circuit_with_1_ancilla_fully_quantum_register_1_qubit(self):
        """
        Test Case #5:

        - Create a Qiskrypt's Quantum Circuit with:
           (i) 1 Ancilla Fully-Quantum Register (with 1 qubit).

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        ancilla_fully_quantum_register_name = "anc_fully_qu_reg"
        """
        Set the name of the Qiskrypt's Ancilla Fully-Quantum Register.
        """

        ancilla_fully_quantum_register_num_qubits = 1
        """
        Set the number of qubits for the Qiskrypt's Ancilla Fully-Quantum Register.
        """

        qiskrypt_ancilla_fully_quantum_register = \
            QiskryptAncillaFullyQuantumRegister(name=ancilla_fully_quantum_register_name,
                                                num_ancilla_qubits=ancilla_fully_quantum_register_num_qubits,
                                                ancilla_quantum_register=None)
        """
        Create a Qiskrypt's Ancilla Fully-Quantum Register, given its name and number of qubits.
        """

        quantum_circuit_name = "qu_circ"
        """
        Set the name of the Qiskrypt's Quantum Circuit.
        """

        qiskrypt_quantum_circuit = \
            QiskryptQuantumCircuit(name=quantum_circuit_name,
                                   quantum_registers=None,
                                   fully_quantum_registers=None,
                                   semi_quantum_registers=None,
                                   ancilla_quantum_registers=None,
                                   ancilla_fully_quantum_registers=[qiskrypt_ancilla_fully_quantum_register],
                                   ancilla_semi_quantum_registers=None,
                                   classical_registers=None,
                                   global_phase=0)
        """
        Create a Qiskrypt's Quantum Circuit, given its name,
        Qiskrypt's Quantum Registers, Qiskrypt's Fully-Quantum Registers,
        Qiskrypt's Semi-Quantum Registers,
        Qiskrypt's Ancilla Quantum Registers, Qiskrypt's Ancilla Fully-Quantum Registers,
        Qiskrypt's Ancilla Semi-Quantum Registers,
        Qiskrypt's Classical Registers and
        Global Phase.
        """

        assert(qiskrypt_quantum_circuit.get_name() == quantum_circuit_name)
        """
        Assertion for the name of the Qiskrypt's Quantum Circuit.
        """

        for qiskrypt_ancilla_fully_quantum_register in qiskrypt_quantum_circuit.get_qiskrypt_ancilla_fully_quantum_registers():
            """
            For each supposed Qiskrypt's Ancilla Fully-Quantum Register in the Qiskrypt's Quantum Circuit.
            """

            assert(not isinstance(qiskrypt_ancilla_fully_quantum_register, QiskryptQuantumRegister))
            """
            Assertion for the current Qiskrypt's Ancilla Fully-Quantum Register of
            the Qiskrypt's Quantum Circuit do not be an actual Qiskrypt's Quantum Register.
            """

            assert(not isinstance(qiskrypt_ancilla_fully_quantum_register, QiskryptFullyQuantumRegister))
            """
            Assertion for the current Qiskrypt's Ancilla Fully-Quantum Register of
            the Qiskrypt's Quantum Circuit do not be an actual Qiskrypt's Fully-Quantum Register.
            """

            assert(not isinstance(qiskrypt_ancilla_fully_quantum_register, QiskryptSemiQuantumRegister))
            """
            Assertion for the current Qiskrypt's Ancilla Fully-Quantum Register of
            the Qiskrypt's Quantum Circuit do not be an actual Qiskrypt's Semi-Quantum Register.
            """

            assert(isinstance(qiskrypt_ancilla_fully_quantum_register, QiskryptAncillaQuantumRegister))
            """
            Assertion for the current Qiskrypt's Ancilla Fully-Quantum Register of
            the Qiskrypt's Quantum Circuit be an actual Qiskrypt's Ancilla Quantum Register.
            """

            assert(isinstance(qiskrypt_ancilla_fully_quantum_register, QiskryptAncillaFullyQuantumRegister))
            """
            Assertion for the current Qiskrypt's Ancilla Fully-Quantum Register of
            the Qiskrypt's Quantum Circuit be an actual Qiskrypt's Ancilla Fully-Quantum Register.
            """

            assert(not isinstance(qiskrypt_ancilla_fully_quantum_register, QiskryptAncillaSemiQuantumRegister))
            """
            Assertion for the current Qiskrypt's Ancilla Fully-Quantum Register of
            the Qiskrypt's Quantum Circuit do not be an actual Qiskrypt's Ancilla Semi-Quantum Register.
            """

            assert(not isinstance(qiskrypt_ancilla_fully_quantum_register, ClassicalRegister))
            """
            Assertion for the current Qiskrypt's Ancilla Fully-Quantum Register of
            the Qiskrypt's Quantum Circuit do not be an actual Qiskrypt's Classical Register.
            """

            assert(isinstance(qiskrypt_ancilla_fully_quantum_register.get_ancilla_quantum_register(), AncillaRegister))
            """
            Assertion for the current Qiskrypt's Ancilla Fully-Quantum Register of
            the Qiskrypt's Quantum Circuit has an IBM's Qiskit Ancilla Register.
            """

        assert(qiskrypt_quantum_circuit.get_total_num_qubits() == ancilla_fully_quantum_register_num_qubits)
        """
        Assertion for the total number of qubits of
        all the Qiskrypt's Ancilla Fully-Quantum Registers of the Qiskrypt's Quantum Circuit.
        """

        assert(qiskrypt_quantum_circuit.get_num_qubits_in_qiskit_quantum_register(0) == ancilla_fully_quantum_register_num_qubits)
        """
        Assertion for the number of qubits of
        the 1st Qiskrypt's Quantum Register of the Qiskrypt's Quantum Circuit.
        """

        """
        Dummy Assert Equal for the Unittest
        """
        self.assertEqual(True, True)

    def test_no_6_creation_qiskrypt_quantum_circuit_with_1_ancilla_semi_quantum_register_1_qubit(self):
        """
        Test Case #6:

        - Create a Qiskrypt's Quantum Circuit with:
           (i) 1 Ancilla Semi-Quantum Register (with 1 qubit).

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        ancilla_semi_quantum_register_name = "anc_semi_qu_reg"
        """
        Set the name of the Qiskrypt's Ancilla Semi-Quantum Register.
        """

        ancilla_semi_quantum_register_num_qubits = 1
        """
        Set the number of qubits for the Qiskrypt's Ancilla Semi-Quantum Register.
        """

        qiskrypt_ancilla_semi_quantum_register = \
            QiskryptAncillaSemiQuantumRegister(name=ancilla_semi_quantum_register_name,
                                               num_ancilla_qubits=ancilla_semi_quantum_register_num_qubits,
                                               ancilla_quantum_register=None)
        """
        Create a Qiskrypt's Ancilla Semi-Quantum Register, given its name and number of qubits.
        """

        quantum_circuit_name = "qu_circ"
        """
        Set the name of the Qiskrypt's Quantum Circuit.
        """

        qiskrypt_quantum_circuit = \
            QiskryptQuantumCircuit(name=quantum_circuit_name,
                                   quantum_registers=None,
                                   fully_quantum_registers=None,
                                   semi_quantum_registers=None,
                                   ancilla_quantum_registers=None,
                                   ancilla_fully_quantum_registers=None,
                                   ancilla_semi_quantum_registers=[qiskrypt_ancilla_semi_quantum_register],
                                   classical_registers=None,
                                   global_phase=0)
        """
        Create a Qiskrypt's Quantum Circuit, given its name,
        Qiskrypt's Quantum Registers, Qiskrypt's Fully-Quantum Registers,
        Qiskrypt's Semi-Quantum Registers,
        Qiskrypt's Ancilla Quantum Registers, Qiskrypt's Ancilla Fully-Quantum Registers,
        Qiskrypt's Ancilla Semi-Quantum Registers,
        Qiskrypt's Classical Registers and
        Global Phase.
        """

        assert(qiskrypt_quantum_circuit.get_name() == quantum_circuit_name)
        """
        Assertion for the name of the Qiskrypt's Quantum Circuit.
        """

        for qiskrypt_ancilla_semi_quantum_register in qiskrypt_quantum_circuit.get_qiskrypt_ancilla_semi_quantum_registers():
            """
            For each supposed Qiskrypt's Ancilla Semi-Quantum Register in the Qiskrypt's Quantum Circuit.
            """

            assert(not isinstance(qiskrypt_ancilla_semi_quantum_register, QiskryptQuantumRegister))
            """
            Assertion for the current Qiskrypt's Ancilla Semi-Quantum Register of
            the Qiskrypt's Quantum Circuit do not be an actual Qiskrypt's Quantum Register.
            """

            assert(not isinstance(qiskrypt_ancilla_semi_quantum_register, QiskryptFullyQuantumRegister))
            """
            Assertion for the current Qiskrypt's Ancilla Semi-Quantum Register of
            the Qiskrypt's Quantum Circuit do not be an actual Qiskrypt's Fully-Quantum Register.
            """

            assert(not isinstance(qiskrypt_ancilla_semi_quantum_register, QiskryptSemiQuantumRegister))
            """
            Assertion for the current Qiskrypt's Ancilla Semi-Quantum Register of
            the Qiskrypt's Quantum Circuit do not be an actual Qiskrypt's Semi-Quantum Register.
            """

            assert(isinstance(qiskrypt_ancilla_semi_quantum_register, QiskryptAncillaQuantumRegister))
            """
            Assertion for the current Qiskrypt's Ancilla Semi-Quantum Register of
            the Qiskrypt's Quantum Circuit be an actual Qiskrypt's Ancilla Quantum Register.
            """

            assert(not isinstance(qiskrypt_ancilla_semi_quantum_register, QiskryptAncillaFullyQuantumRegister))
            """
            Assertion for the current Qiskrypt's Ancilla Semi-Quantum Register of
            the Qiskrypt's Quantum Circuit do not be an actual Qiskrypt's Ancilla Fully-Quantum Register.
            """

            assert(isinstance(qiskrypt_ancilla_semi_quantum_register, QiskryptAncillaSemiQuantumRegister))
            """
            Assertion for the current Qiskrypt's Ancilla Semi-Quantum Register of
            the Qiskrypt's Quantum Circuit be an actual Qiskrypt's Ancilla Semi-Quantum Register.
            """

            assert(not isinstance(qiskrypt_ancilla_semi_quantum_register, QiskryptClassicalRegister))
            """
            Assertion for the current Qiskrypt's Ancilla Semi-Quantum Register of
            the Qiskrypt's Quantum Circuit do not be an actual Qiskrypt's Classical Register.
            """

            assert(isinstance(qiskrypt_ancilla_semi_quantum_register.get_ancilla_quantum_register(), AncillaRegister))
            """
            Assertion for the current Qiskrypt's Ancilla Semi-Quantum Register of
            the Qiskrypt's Quantum Circuit has an IBM's Qiskit Ancilla Register.
            """

        assert(qiskrypt_quantum_circuit.get_total_num_qubits() == ancilla_semi_quantum_register_num_qubits)
        """
        Assertion for the total number of qubits of
        all the Qiskrypt's Ancilla Fully-Quantum Registers of the Qiskrypt's Quantum Circuit.
        """

        assert(qiskrypt_quantum_circuit.get_num_qubits_in_qiskit_quantum_register(0) == ancilla_semi_quantum_register_num_qubits)
        """
        Assertion for the number of qubits of
        the 1st Qiskrypt's Quantum Register of the Qiskrypt's Quantum Circuit.
        """

        """
        Dummy Assert Equal for the Unittest
        """
        self.assertEqual(True, True)

    def test_no_7_creation_qiskrypt_quantum_circuit_with_1_classical_register_1_bit(self):
        """
        Test Case #7:

        - Create a Qiskrypt's Quantum Circuit with:
           (i) 1 Classical Register (with 1 bit).

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
                                   quantum_registers=None,
                                   fully_quantum_registers=None,
                                   semi_quantum_registers=None,
                                   ancilla_quantum_registers=None,
                                   ancilla_fully_quantum_registers=None,
                                   ancilla_semi_quantum_registers=None,
                                   classical_registers=[qiskrypt_classical_register],
                                   global_phase=0)
        """
        Create a Qiskrypt's Quantum Circuit, given its name,
        Qiskrypt's Quantum Registers, Qiskrypt's Fully-Quantum Registers,
        Qiskrypt's Semi-Quantum Registers,
        Qiskrypt's Ancilla Quantum Registers, Qiskrypt's Ancilla Fully-Quantum Registers,
        Qiskrypt's Ancilla Semi-Quantum Registers,
        Qiskrypt's Classical Registers and
        Global Phase.
        """

        assert(qiskrypt_quantum_circuit.get_name() == quantum_circuit_name)
        """
        Assertion for the name of the Qiskrypt's Quantum Circuit.
        """

        for qiskrypt_classical_register in qiskrypt_quantum_circuit.get_qiskrypt_classical_registers():
            """
            For each supposed Qiskrypt's Classical Register in the Qiskrypt's Quantum Circuit.
            """

            assert(not isinstance(qiskrypt_classical_register, QiskryptQuantumRegister))
            """
            Assertion for the current Qiskrypt's Classical Register of
            the Qiskrypt's Quantum Circuit do not be an actual Qiskrypt's Quantum Register.
            """

            assert(not isinstance(qiskrypt_classical_register, QiskryptFullyQuantumRegister))
            """
            Assertion for the current Qiskrypt's Classical Register of
            the Qiskrypt's Quantum Circuit do not be an actual Qiskrypt's Fully-Quantum Register.
            """

            assert(not isinstance(qiskrypt_classical_register, QiskryptSemiQuantumRegister))
            """
            Assertion for the current Qiskrypt's Classical Register of
            the Qiskrypt's Quantum Circuit do not be an actual Qiskrypt's Semi-Quantum Register.
            """

            assert(not isinstance(qiskrypt_classical_register, QiskryptAncillaQuantumRegister))
            """
            Assertion for the current Qiskrypt's Classical Register of
            the Qiskrypt's Quantum Circuit do not be an actual Qiskrypt's Ancilla Quantum Register.
            """

            assert(not isinstance(qiskrypt_classical_register, QiskryptAncillaFullyQuantumRegister))
            """
            Assertion for the current Qiskrypt's Classical Register of
            the Qiskrypt's Quantum Circuit do not be an actual Qiskrypt's Ancilla Fully-Quantum Register.
            """

            assert(not isinstance(qiskrypt_classical_register, QiskryptAncillaSemiQuantumRegister))
            """
            Assertion for the current Qiskrypt's Classical Register of
            the Qiskrypt's Quantum Circuit do not be an actual Qiskrypt's Ancilla Semi-Quantum Register.
            """

            assert(isinstance(qiskrypt_classical_register, QiskryptClassicalRegister))
            """
            Assertion for the current Qiskrypt's Classical Register of
            the Qiskrypt's Quantum Circuit be an actual Qiskrypt's Classical Register.
            """

            assert(isinstance(qiskrypt_classical_register.get_classical_register(), ClassicalRegister))
            """
            Assertion for the current Qiskrypt's Ancilla Semi-Quantum Register of
            the Qiskrypt's Quantum Circuit has an IBM's Qiskit Classical Register.
            """

        assert(qiskrypt_quantum_circuit.get_total_num_bits() == classical_register_num_bits)
        """
        Assertion for the total number of bits of
        all the Qiskrypt's Classical Registers of the Qiskrypt's Quantum Circuit.
        """

        assert(qiskrypt_quantum_circuit.get_num_bits_in_qiskit_classical_register(0) == classical_register_num_bits)
        """
        Assertion for the number of bits of
        the 1st Qiskrypt's Classical Register of the Qiskrypt's Quantum Circuit.
        """

        """
        Dummy Assert Equal for the Unittest
        """
        self.assertEqual(True, True)

    def test_no_8_creation_qiskrypt_quantum_circuit_with_1_quantum_register_1_qubit_and_1_classical_register_1_bit(self):
        """
        Test Case #8:

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
                                   ancilla_quantum_registers=None,
                                   ancilla_fully_quantum_registers=None,
                                   ancilla_semi_quantum_registers=None,
                                   classical_registers=[qiskrypt_classical_register],
                                   global_phase=0)
        """
        Create a Qiskrypt's Quantum Circuit, given its name,
        Qiskrypt's Quantum Registers, Qiskrypt's Fully-Quantum Registers,
        Qiskrypt's Semi-Quantum Registers,
        Qiskrypt's Ancilla Quantum Registers, Qiskrypt's Ancilla Fully-Quantum Registers,
        Qiskrypt's Ancilla Semi-Quantum Registers,
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

            assert(not isinstance(qiskrypt_quantum_register, QiskryptAncillaQuantumRegister))
            """
            Assertion for the current Qiskrypt's Quantum Register of
            the Qiskrypt's Quantum Circuit do not be an actual Qiskrypt's Ancilla Quantum Register.
            """

            assert(not isinstance(qiskrypt_quantum_register, QiskryptAncillaFullyQuantumRegister))
            """
            Assertion for the current Qiskrypt's Quantum Register of
            the Qiskrypt's Quantum Circuit do not be an actual Qiskrypt's Ancilla Fully-Quantum Register.
            """

            assert(not isinstance(qiskrypt_quantum_register, QiskryptAncillaSemiQuantumRegister))
            """
            Assertion for the current Qiskrypt's Quantum Register of
            the Qiskrypt's Quantum Circuit do not be an actual Qiskrypt's Ancilla Semi-Quantum Register.
            """

            assert(not isinstance(qiskrypt_quantum_register, QiskryptClassicalRegister))
            """
            Assertion for the current Qiskrypt's Quantum Register of
            the Qiskrypt's Quantum Circuit do not be an actual Qiskrypt's Classical Register.
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

            assert(not isinstance(qiskrypt_classical_register, QiskryptQuantumRegister))
            """
            Assertion for the current Qiskrypt's Classical Register of
            the Qiskrypt's Quantum Circuit do not be an actual Qiskrypt's Quantum Register.
            """

            assert(not isinstance(qiskrypt_classical_register, QiskryptFullyQuantumRegister))
            """
            Assertion for the current Qiskrypt's Classical Register of
            the Qiskrypt's Quantum Circuit do not be an actual Qiskrypt's Fully-Quantum Register.
            """

            assert(not isinstance(qiskrypt_classical_register, QiskryptSemiQuantumRegister))
            """
            Assertion for the current Qiskrypt's Classical Register of
            the Qiskrypt's Quantum Circuit do not be an actual Qiskrypt's Semi-Quantum Register.
            """

            assert(not isinstance(qiskrypt_classical_register, QiskryptAncillaQuantumRegister))
            """
            Assertion for the current Qiskrypt's Classical Register of
            the Qiskrypt's Quantum Circuit do not be an actual Qiskrypt's Ancilla Quantum Register.
            """

            assert(not isinstance(qiskrypt_classical_register, QiskryptAncillaFullyQuantumRegister))
            """
            Assertion for the current Qiskrypt's Classical Register of
            the Qiskrypt's Quantum Circuit do not be an actual Qiskrypt's Ancilla Fully-Quantum Register.
            """

            assert(not isinstance(qiskrypt_classical_register, QiskryptAncillaSemiQuantumRegister))
            """
            Assertion for the current Qiskrypt's Classical Register of
            the Qiskrypt's Quantum Circuit do not be an actual Qiskrypt's Ancilla Semi-Quantum Register.
            """

            assert(isinstance(qiskrypt_classical_register, QiskryptClassicalRegister))
            """
            Assertion for the current Qiskrypt's Classical Register of
            the Qiskrypt's Quantum Circuit be an actual Qiskrypt's Classical Register.
            """

            assert(isinstance(qiskrypt_classical_register.get_classical_register(), ClassicalRegister))
            """
            Assertion for the current Qiskrypt's Ancilla Semi-Quantum Register of
            the Qiskrypt's Quantum Circuit has an IBM's Qiskit Classical Register.
            """

        assert(qiskrypt_quantum_circuit.get_total_num_qubits() == quantum_register_num_qubits)
        """
        Assertion for the total number of qubits of
        all the Qiskrypt's Quantum Registers of the Qiskrypt's Quantum Circuit.
        """

        assert(qiskrypt_quantum_circuit.get_num_qubits_in_qiskit_quantum_register(0) == quantum_register_num_qubits)
        """
        Assertion for the number of bits of
        the 1st Qiskrypt's Quantum Register of the Qiskrypt's Quantum Circuit.
        """

        assert(qiskrypt_quantum_circuit.get_total_num_bits() == classical_register_num_bits)
        """
        Assertion for the total number of bits of
        all the Qiskrypt's Classical Registers of the Qiskrypt's Quantum Circuit.
        """

        assert(qiskrypt_quantum_circuit.get_num_bits_in_qiskit_classical_register(0) == classical_register_num_bits)
        """
        Assertion for the number of bits of
        the 1st Qiskrypt's Classical Register of the Qiskrypt's Quantum Circuit.
        """

        """
        Dummy Assert Equal for the Unittest
        """
        self.assertEqual(True, True)

    def test_no_9_creation_qiskrypt_quantum_circuit_with_1_fully_quantum_register_1_qubit_and_1_classical_register_1_bit(self):
        """
        Test Case #9:

        - Create a Qiskrypt's Quantum Circuit with:
            (i) 1 Fully-Quantum Register (with 1 qubit).
           (ii) 1 Classical Register (with 1 bit).

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        fully_quantum_register_name = "fully_qu_reg"
        """
        Set the name of the Qiskrypt's Fully-Quantum Register.
        """

        fully_quantum_register_num_qubits = 1
        """
        Set the number of qubits for the Qiskrypt's Fully-Quantum Register.
        """

        qiskrypt_fully_quantum_register = \
            QiskryptFullyQuantumRegister(name=fully_quantum_register_name,
                                         num_qubits=fully_quantum_register_num_qubits,
                                         quantum_register=None)
        """
        Create a Qiskrypt's Fully-Quantum Register, given its name and number of qubits.
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
                                   quantum_registers=None,
                                   fully_quantum_registers=[qiskrypt_fully_quantum_register],
                                   semi_quantum_registers=None,
                                   ancilla_quantum_registers=None,
                                   ancilla_fully_quantum_registers=None,
                                   ancilla_semi_quantum_registers=None,
                                   classical_registers=[qiskrypt_classical_register],
                                   global_phase=0)
        """
        Create a Qiskrypt's Quantum Circuit, given its name,
        Qiskrypt's Quantum Registers, Qiskrypt's Fully-Quantum Registers,
        Qiskrypt's Semi-Quantum Registers,
        Qiskrypt's Ancilla Quantum Registers, Qiskrypt's Ancilla Fully-Quantum Registers,
        Qiskrypt's Ancilla Semi-Quantum Registers,
        Qiskrypt's Classical Registers and
        Global Phase.
        """

        assert(qiskrypt_quantum_circuit.get_name() == quantum_circuit_name)
        """
        Assertion for the name of the Qiskrypt's Quantum Circuit.
        """

        for qiskrypt_fully_quantum_register in qiskrypt_quantum_circuit.get_qiskrypt_fully_quantum_registers():
            """
            For each supposed Qiskrypt's Fully-Quantum Register in the Qiskrypt's Quantum Circuit.
            """

            assert(isinstance(qiskrypt_fully_quantum_register, QiskryptQuantumRegister))
            """
            Assertion for the current Qiskrypt's Fully-Quantum Register of
            the Qiskrypt's Quantum Circuit be an actual Qiskrypt's Quantum Register.
            """

            assert(isinstance(qiskrypt_fully_quantum_register, QiskryptFullyQuantumRegister))
            """
            Assertion for the current Qiskrypt's Fully-Quantum Register of
            the Qiskrypt's Quantum Circuit be an actual Qiskrypt's Fully-Quantum Register.
            """

            assert(not isinstance(qiskrypt_fully_quantum_register, QiskryptSemiQuantumRegister))
            """
            Assertion for the current Qiskrypt's Fully-Quantum Register of
            the Qiskrypt's Quantum Circuit do not be an actual Qiskrypt's Semi-Quantum Register.
            """

            assert(not isinstance(qiskrypt_fully_quantum_register, QiskryptAncillaQuantumRegister))
            """
            Assertion for the current Qiskrypt's Fully-Quantum Register of
            the Qiskrypt's Quantum Circuit do not be an actual Qiskrypt's Ancilla Quantum Register.
            """

            assert(not isinstance(qiskrypt_fully_quantum_register, QiskryptAncillaFullyQuantumRegister))
            """
            Assertion for the current Qiskrypt's Fully-Quantum Register of
            the Qiskrypt's Quantum Circuit do not be an actual Qiskrypt's Ancilla Fully-Quantum Register.
            """

            assert(not isinstance(qiskrypt_fully_quantum_register, QiskryptAncillaSemiQuantumRegister))
            """
            Assertion for the current Qiskrypt's Fully-Quantum Register of
            the Qiskrypt's Quantum Circuit do not be an actual Qiskrypt's Ancilla Semi-Quantum Register.
            """

            assert(not isinstance(qiskrypt_fully_quantum_register, QiskryptClassicalRegister))
            """
            Assertion for the current Qiskrypt's Fully-Quantum Register of
            the Qiskrypt's Quantum Circuit do not be an actual Qiskrypt's Classical Register.
            """

            assert(isinstance(qiskrypt_fully_quantum_register.get_quantum_register(), QuantumRegister))
            """
            Assertion for the current Qiskrypt's Fully-Quantum Register of
            the Qiskrypt's Quantum Circuit has an IBM's Qiskit Quantum Register.
            """

        for qiskrypt_classical_register in qiskrypt_quantum_circuit.get_qiskrypt_classical_registers():
            """
            For each supposed Qiskrypt's Classical Register in the Qiskrypt's Quantum Circuit.
            """

            assert(not isinstance(qiskrypt_classical_register, QiskryptQuantumRegister))
            """
            Assertion for the current Qiskrypt's Classical Register of
            the Qiskrypt's Quantum Circuit do not be an actual Qiskrypt's Quantum Register.
            """

            assert(not isinstance(qiskrypt_classical_register, QiskryptFullyQuantumRegister))
            """
            Assertion for the current Qiskrypt's Classical Register of
            the Qiskrypt's Quantum Circuit do not be an actual Qiskrypt's Fully-Quantum Register.
            """

            assert(not isinstance(qiskrypt_classical_register, QiskryptSemiQuantumRegister))
            """
            Assertion for the current Qiskrypt's Classical Register of
            the Qiskrypt's Quantum Circuit do not be an actual Qiskrypt's Semi-Quantum Register.
            """

            assert(not isinstance(qiskrypt_classical_register, QiskryptAncillaQuantumRegister))
            """
            Assertion for the current Qiskrypt's Classical Register of
            the Qiskrypt's Quantum Circuit do not be an actual Qiskrypt's Ancilla Quantum Register.
            """

            assert(not isinstance(qiskrypt_classical_register, QiskryptAncillaFullyQuantumRegister))
            """
            Assertion for the current Qiskrypt's Classical Register of
            the Qiskrypt's Quantum Circuit do not be an actual Qiskrypt's Ancilla Fully-Quantum Register.
            """

            assert(not isinstance(qiskrypt_classical_register, QiskryptAncillaSemiQuantumRegister))
            """
            Assertion for the current Qiskrypt's Classical Register of
            the Qiskrypt's Quantum Circuit do not be an actual Qiskrypt's Ancilla Semi-Quantum Register.
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

        assert(qiskrypt_quantum_circuit.get_total_num_qubits() == fully_quantum_register_num_qubits)
        """
        Assertion for the total number of qubits of
        all the Qiskrypt's Quantum Registers of the Qiskrypt's Quantum Circuit.
        """

        assert(qiskrypt_quantum_circuit.get_num_qubits_in_qiskit_quantum_register(0) == fully_quantum_register_num_qubits)
        """
        Assertion for the number of bits of
        the 1st Qiskrypt's Quantum Register of the Qiskrypt's Quantum Circuit.
        """

        assert(qiskrypt_quantum_circuit.get_total_num_bits() == classical_register_num_bits)
        """
        Assertion for the total number of bits of
        all the Qiskrypt's Classical Registers of the Qiskrypt's Quantum Circuit.
        """

        assert(qiskrypt_quantum_circuit.get_num_bits_in_qiskit_classical_register(0) == classical_register_num_bits)
        """
        Assertion for the number of bits of
        the 1st Qiskrypt's Classical Register of the Qiskrypt's Quantum Circuit.
        """

        """
        Dummy Assert Equal for the Unittest
        """
        self.assertEqual(True, True)

    def test_no_10_creation_qiskrypt_quantum_circuit_with_1_semi_quantum_register_1_qubit_and_1_classical_register_1_bit(self):
        """
        Test Case #10:

        - Create a Qiskrypt's Quantum Circuit with:
            (i) 1 Semi-Quantum Register (with 1 qubit).
           (ii) 1 Classical Register (with 1 bit).

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        semi_quantum_register_name = "semi_qu_reg"
        """
        Set the name of the Qiskrypt's Semi-Quantum Register.
        """

        semi_quantum_register_num_qubits = 1
        """
        Set the number of qubits for the Qiskrypt's Semi-Quantum Register.
        """

        qiskrypt_semi_quantum_register = \
            QiskryptSemiQuantumRegister(name=semi_quantum_register_name,
                                        num_qubits=semi_quantum_register_num_qubits,
                                        quantum_register=None)
        """
        Create a Qiskrypt's Semi-Quantum Register, given its name and number of qubits.
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
                                   quantum_registers=None,
                                   fully_quantum_registers=None,
                                   semi_quantum_registers=[qiskrypt_semi_quantum_register],
                                   ancilla_quantum_registers=None,
                                   ancilla_fully_quantum_registers=None,
                                   ancilla_semi_quantum_registers=None,
                                   classical_registers=[qiskrypt_classical_register],
                                   global_phase=0)
        """
        Create a Qiskrypt's Quantum Circuit, given its name,
        Qiskrypt's Quantum Registers, Qiskrypt's Fully-Quantum Registers,
        Qiskrypt's Semi-Quantum Registers,
        Qiskrypt's Ancilla Quantum Registers, Qiskrypt's Ancilla Fully-Quantum Registers,
        Qiskrypt's Ancilla Semi-Quantum Registers,
        Qiskrypt's Classical Registers and
        Global Phase.
        """

        assert(qiskrypt_quantum_circuit.get_name() == quantum_circuit_name)
        """
        Assertion for the name of the Qiskrypt's Quantum Circuit.
        """

        for qiskrypt_semi_quantum_register in qiskrypt_quantum_circuit.get_qiskrypt_semi_quantum_registers():
            """
            For each supposed Qiskrypt's Semi-Quantum Register in the Qiskrypt's Quantum Circuit.
            """

            assert(isinstance(qiskrypt_semi_quantum_register, QiskryptQuantumRegister))
            """
            Assertion for the current Qiskrypt's Semi-Quantum Register of
            the Qiskrypt's Quantum Circuit be an actual Qiskrypt's Quantum Register.
            """

            assert(not isinstance(qiskrypt_semi_quantum_register, QiskryptFullyQuantumRegister))
            """
            Assertion for the current Qiskrypt's Semi-Quantum Register of
            the Qiskrypt's Quantum Circuit do not be an actual Qiskrypt's Fully-Quantum Register.
            """

            assert(isinstance(qiskrypt_semi_quantum_register, QiskryptSemiQuantumRegister))
            """
            Assertion for the current Qiskrypt's Semi-Quantum Register of
            the Qiskrypt's Quantum Circuit be an actual Qiskrypt's Semi-Quantum Register.
            """

            assert(not isinstance(qiskrypt_semi_quantum_register, QiskryptAncillaQuantumRegister))
            """
            Assertion for the current Qiskrypt's Semi-Quantum Register of
            the Qiskrypt's Quantum Circuit do not be an actual Qiskrypt's Ancilla Quantum Register.
            """

            assert(not isinstance(qiskrypt_semi_quantum_register, QiskryptAncillaFullyQuantumRegister))
            """
            Assertion for the current Qiskrypt's Semi-Quantum Register of
            the Qiskrypt's Quantum Circuit do not be an actual Qiskrypt's Ancilla Fully-Quantum Register.
            """

            assert(not isinstance(qiskrypt_semi_quantum_register, QiskryptAncillaSemiQuantumRegister))
            """
            Assertion for the current Qiskrypt's Semi-Quantum Register of
            the Qiskrypt's Quantum Circuit do not be an actual Qiskrypt's Ancilla Semi-Quantum Register.
            """

            assert(not isinstance(qiskrypt_semi_quantum_register, QiskryptClassicalRegister))
            """
            Assertion for the current Qiskrypt's Semi-Quantum Register of
            the Qiskrypt's Quantum Circuit do not be an actual Qiskrypt's Classical Register.
            """

            assert(isinstance(qiskrypt_semi_quantum_register.get_quantum_register(), QuantumRegister))
            """
            Assertion for the current Qiskrypt's Semi-Quantum Register of
            the Qiskrypt's Quantum Circuit has an IBM's Qiskit Quantum Register.
            """

        for qiskrypt_classical_register in qiskrypt_quantum_circuit.get_qiskrypt_classical_registers():
            """
            For each supposed Qiskrypt's Classical Register in the Qiskrypt's Quantum Circuit.
            """

            assert(not isinstance(qiskrypt_classical_register, QiskryptQuantumRegister))
            """
            Assertion for the current Qiskrypt's Classical Register of
            the Qiskrypt's Quantum Circuit do not be an actual Qiskrypt's Quantum Register.
            """

            assert(not isinstance(qiskrypt_classical_register, QiskryptFullyQuantumRegister))
            """
            Assertion for the current Qiskrypt's Classical Register of
            the Qiskrypt's Quantum Circuit do not be an actual Qiskrypt's Fully-Quantum Register.
            """

            assert(not isinstance(qiskrypt_classical_register, QiskryptSemiQuantumRegister))
            """
            Assertion for the current Qiskrypt's Classical Register of
            the Qiskrypt's Quantum Circuit do not be an actual Qiskrypt's Semi-Quantum Register.
            """

            assert(not isinstance(qiskrypt_classical_register, QiskryptAncillaQuantumRegister))
            """
            Assertion for the current Qiskrypt's Classical Register of
            the Qiskrypt's Quantum Circuit do not be an actual Qiskrypt's Ancilla Quantum Register.
            """

            assert(not isinstance(qiskrypt_classical_register, QiskryptAncillaFullyQuantumRegister))
            """
            Assertion for the current Qiskrypt's Classical Register of
            the Qiskrypt's Quantum Circuit do not be an actual Qiskrypt's Ancilla Fully-Quantum Register.
            """

            assert(not isinstance(qiskrypt_classical_register, QiskryptAncillaSemiQuantumRegister))
            """
            Assertion for the current Qiskrypt's Classical Register of
            the Qiskrypt's Quantum Circuit do not be an actual Qiskrypt's Ancilla Semi-Quantum Register.
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

        assert(qiskrypt_quantum_circuit.get_total_num_qubits() == semi_quantum_register_num_qubits)
        """
        Assertion for the total number of qubits of
        all the Qiskrypt's Quantum Registers of the Qiskrypt's Quantum Circuit.
        """

        assert(qiskrypt_quantum_circuit.get_num_qubits_in_qiskit_quantum_register(0) == semi_quantum_register_num_qubits)
        """
        Assertion for the number of bits of
        the 1st Qiskrypt's Quantum Register of the Qiskrypt's Quantum Circuit.
        """

        assert(qiskrypt_quantum_circuit.get_total_num_bits() == classical_register_num_bits)
        """
        Assertion for the total number of bits of
        all the Qiskrypt's Classical Registers of the Qiskrypt's Quantum Circuit.
        """

        assert(qiskrypt_quantum_circuit.get_num_bits_in_qiskit_classical_register(0) == classical_register_num_bits)
        """
        Assertion for the number of bits of
        the 1st Qiskrypt's Classical Register of the Qiskrypt's Quantum Circuit.
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