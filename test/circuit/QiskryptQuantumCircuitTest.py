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

from numpy import array, sqrt
"""
Import the N-Dimensional Arrays and Square Root functions from Python's NumPy.
"""

from numpy.testing import assert_allclose
"""
Import the function for the assertion of all close values of an array,
allowing a small value of error of the Testing Module from Python's NumPy.
"""

from qiskit import Aer, execute
"""
Import Aer Simulator and the Execute function from IBM's Qiskit.
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


class CreationQiskryptQuantumCircuitTests(TestCase):
    """
    Object Class of the Unitary Tests for the creation of a Qiskrypt's Quantum Circuit.
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
                                    qiskit_quantum_register=None)
        """
        Create a Qiskrypt's Quantum Register, given its name and number of qubits.
        """

        quantum_circuit_name = "qu_circ"
        """
        Set the name of the Qiskrypt's Quantum Circuit.
        """

        qiskrypt_quantum_circuit = \
            QiskryptQuantumCircuit(name=quantum_circuit_name,
                                   qiskrypt_quantum_registers=[qiskrypt_quantum_register],
                                   qiskrypt_fully_quantum_registers=None,
                                   qiskrypt_semi_quantum_registers=None,
                                   qiskrypt_ancilla_quantum_registers=None,
                                   qiskrypt_ancilla_fully_quantum_registers=None,
                                   qiskrypt_ancilla_semi_quantum_registers=None,
                                   qiskrypt_classical_registers=None,
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

            assert(isinstance(qiskrypt_quantum_register.get_qiskit_quantum_register(), QuantumRegister))
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
                                         qiskit_quantum_register=None)
        """
        Create a Qiskrypt's Fully-Quantum Register, given its name and number of qubits.
        """

        quantum_circuit_name = "qu_circ"
        """
        Set the name of the Qiskrypt's Quantum Circuit.
        """
        
        qiskrypt_quantum_circuit = \
            QiskryptQuantumCircuit(name=quantum_circuit_name,
                                   qiskrypt_quantum_registers=None,
                                   qiskrypt_fully_quantum_registers=[qiskrypt_fully_quantum_register],
                                   qiskrypt_semi_quantum_registers=None,
                                   qiskrypt_ancilla_quantum_registers=None,
                                   qiskrypt_ancilla_fully_quantum_registers=None,
                                   qiskrypt_ancilla_semi_quantum_registers=None,
                                   qiskrypt_classical_registers=None,
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

            assert(isinstance(qiskrypt_fully_quantum_register.get_qiskit_quantum_register(), QuantumRegister))
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
                                        qiskit_quantum_register=None)
        """
        Create a Qiskrypt's Semi-Quantum Register, given its name and number of qubits.
        """

        quantum_circuit_name = "qu_circ"
        """
        Set the name of the Qiskrypt's Quantum Circuit.
        """

        qiskrypt_quantum_circuit = \
            QiskryptQuantumCircuit(name=quantum_circuit_name,
                                   qiskrypt_quantum_registers=None,
                                   qiskrypt_fully_quantum_registers=None,
                                   qiskrypt_semi_quantum_registers=[qiskrypt_semi_quantum_register],
                                   qiskrypt_ancilla_quantum_registers=None,
                                   qiskrypt_ancilla_fully_quantum_registers=None,
                                   qiskrypt_ancilla_semi_quantum_registers=None,
                                   qiskrypt_classical_registers=None,
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

            assert(isinstance(qiskrypt_semi_quantum_register.get_qiskit_quantum_register(), QuantumRegister))
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
                                           qiskit_ancilla_quantum_register=None)
        """
        Create a Qiskrypt's Ancilla Quantum Register, given its name and number of qubits.
        """

        quantum_circuit_name = "qu_circ"
        """
        Set the name of the Qiskrypt's Quantum Circuit.
        """

        qiskrypt_quantum_circuit = \
            QiskryptQuantumCircuit(name=quantum_circuit_name,
                                   qiskrypt_quantum_registers=None,
                                   qiskrypt_fully_quantum_registers=None,
                                   qiskrypt_semi_quantum_registers=None,
                                   qiskrypt_ancilla_quantum_registers=[qiskrypt_ancilla_quantum_register],
                                   qiskrypt_ancilla_fully_quantum_registers=None,
                                   qiskrypt_ancilla_semi_quantum_registers=None,
                                   qiskrypt_classical_registers=None,
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

            assert(isinstance(qiskrypt_ancilla_quantum_register.get_qiskit_ancilla_quantum_register(), AncillaRegister))
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
                                                qiskit_ancilla_quantum_register=None)
        """
        Create a Qiskrypt's Ancilla Fully-Quantum Register, given its name and number of qubits.
        """

        quantum_circuit_name = "qu_circ"
        """
        Set the name of the Qiskrypt's Quantum Circuit.
        """

        qiskrypt_quantum_circuit = \
            QiskryptQuantumCircuit(name=quantum_circuit_name,
                                   qiskrypt_quantum_registers=None,
                                   qiskrypt_fully_quantum_registers=None,
                                   qiskrypt_semi_quantum_registers=None,
                                   qiskrypt_ancilla_quantum_registers=None,
                                   qiskrypt_ancilla_fully_quantum_registers=[qiskrypt_ancilla_fully_quantum_register],
                                   qiskrypt_ancilla_semi_quantum_registers=None,
                                   qiskrypt_classical_registers=None,
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

            assert(isinstance(qiskrypt_ancilla_fully_quantum_register.get_qiskit_ancilla_quantum_register(), AncillaRegister))
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
                                               qiskit_ancilla_quantum_register=None)
        """
        Create a Qiskrypt's Ancilla Semi-Quantum Register, given its name and number of qubits.
        """

        quantum_circuit_name = "qu_circ"
        """
        Set the name of the Qiskrypt's Quantum Circuit.
        """

        qiskrypt_quantum_circuit = \
            QiskryptQuantumCircuit(name=quantum_circuit_name,
                                   qiskrypt_quantum_registers=None,
                                   qiskrypt_fully_quantum_registers=None,
                                   qiskrypt_semi_quantum_registers=None,
                                   qiskrypt_ancilla_quantum_registers=None,
                                   qiskrypt_ancilla_fully_quantum_registers=None,
                                   qiskrypt_ancilla_semi_quantum_registers=[qiskrypt_ancilla_semi_quantum_register],
                                   qiskrypt_classical_registers=None,
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

            assert(isinstance(qiskrypt_ancilla_semi_quantum_register.get_qiskit_ancilla_quantum_register(), AncillaRegister))
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
                                      qiskit_classical_register=None)
        """
        Create a Qiskrypt's Classical Register, given its name and number of bits.
        """

        quantum_circuit_name = "qu_circ"
        """
        Set the name of the Qiskrypt's Quantum Circuit.
        """

        qiskrypt_quantum_circuit = \
            QiskryptQuantumCircuit(name=quantum_circuit_name,
                                   qiskrypt_quantum_registers=None,
                                   qiskrypt_fully_quantum_registers=None,
                                   qiskrypt_semi_quantum_registers=None,
                                   qiskrypt_ancilla_quantum_registers=None,
                                   qiskrypt_ancilla_fully_quantum_registers=None,
                                   qiskrypt_ancilla_semi_quantum_registers=None,
                                   qiskrypt_classical_registers=[qiskrypt_classical_register],
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

            assert(isinstance(qiskrypt_classical_register.get_qiskit_classical_register(), ClassicalRegister))
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
                                    qiskit_quantum_register=None)
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
                                      qiskit_classical_register=None)
        """
        Create a Qiskrypt's Classical Register, given its name and number of bits.
        """

        quantum_circuit_name = "qu_circ"
        """
        Set the name of the Qiskrypt's Quantum Circuit.
        """

        qiskrypt_quantum_circuit = \
            QiskryptQuantumCircuit(name=quantum_circuit_name,
                                   qiskrypt_quantum_registers=[qiskrypt_quantum_register],
                                   qiskrypt_fully_quantum_registers=None,
                                   qiskrypt_semi_quantum_registers=None,
                                   qiskrypt_ancilla_quantum_registers=None,
                                   qiskrypt_ancilla_fully_quantum_registers=None,
                                   qiskrypt_ancilla_semi_quantum_registers=None,
                                   qiskrypt_classical_registers=[qiskrypt_classical_register],
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

            assert(isinstance(qiskrypt_quantum_register.get_qiskit_quantum_register(), QuantumRegister))
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

            assert(isinstance(qiskrypt_classical_register.get_qiskit_classical_register(), ClassicalRegister))
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
        Assertion for the number of qubits of
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
                                         qiskit_quantum_register=None)
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
                                      qiskit_classical_register=None)
        """
        Create a Qiskrypt's Classical Register, given its name and number of bits.
        """

        quantum_circuit_name = "qu_circ"
        """
        Set the name of the Qiskrypt's Quantum Circuit.
        """

        qiskrypt_quantum_circuit = \
            QiskryptQuantumCircuit(name=quantum_circuit_name,
                                   qiskrypt_quantum_registers=None,
                                   qiskrypt_fully_quantum_registers=[qiskrypt_fully_quantum_register],
                                   qiskrypt_semi_quantum_registers=None,
                                   qiskrypt_ancilla_quantum_registers=None,
                                   qiskrypt_ancilla_fully_quantum_registers=None,
                                   qiskrypt_ancilla_semi_quantum_registers=None,
                                   qiskrypt_classical_registers=[qiskrypt_classical_register],
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

            assert(isinstance(qiskrypt_fully_quantum_register.get_qiskit_quantum_register(), QuantumRegister))
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

            assert(isinstance(qiskrypt_classical_register.get_qiskit_classical_register(), ClassicalRegister))
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
        Assertion for the number of qubits of
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
                                        qiskit_quantum_register=None)
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
                                      qiskit_classical_register=None)
        """
        Create a Qiskrypt's Classical Register, given its name and number of bits.
        """

        quantum_circuit_name = "qu_circ"
        """
        Set the name of the Qiskrypt's Quantum Circuit.
        """

        qiskrypt_quantum_circuit = \
            QiskryptQuantumCircuit(name=quantum_circuit_name,
                                   qiskrypt_quantum_registers=None,
                                   qiskrypt_fully_quantum_registers=None,
                                   qiskrypt_semi_quantum_registers=[qiskrypt_semi_quantum_register],
                                   qiskrypt_ancilla_quantum_registers=None,
                                   qiskrypt_ancilla_fully_quantum_registers=None,
                                   qiskrypt_ancilla_semi_quantum_registers=None,
                                   qiskrypt_classical_registers=[qiskrypt_classical_register],
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

            assert(isinstance(qiskrypt_semi_quantum_register.get_qiskit_quantum_register(), QuantumRegister))
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

            assert(isinstance(qiskrypt_classical_register.get_qiskit_classical_register(), ClassicalRegister))
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
        Assertion for the number of qubits of
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

    def test_no_11_creation_qiskrypt_quantum_circuit_with_1_ancilla_quantum_register_1_qubit_and_1_classical_register_1_bit(self):
        """
        Test Case #11:

        - Create a Qiskrypt's Quantum Circuit with:
            (i) 1 Ancilla Quantum Register (with 1 qubit).
           (ii) 1 Classical Register (with 1 bit).

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

        quantum_circuit_name = "qu_circ"
        """
        Set the name of the Qiskrypt's Quantum Circuit.
        """

        qiskrypt_quantum_circuit = \
            QiskryptQuantumCircuit(name=quantum_circuit_name,
                                   qiskrypt_quantum_registers=None,
                                   qiskrypt_fully_quantum_registers=None,
                                   qiskrypt_semi_quantum_registers=None,
                                   qiskrypt_ancilla_quantum_registers=[qiskrypt_ancilla_quantum_register],
                                   qiskrypt_ancilla_fully_quantum_registers=None,
                                   qiskrypt_ancilla_semi_quantum_registers=None,
                                   qiskrypt_classical_registers=[qiskrypt_classical_register],
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

            assert(isinstance(qiskrypt_ancilla_quantum_register.get_qiskit_ancilla_quantum_register(), AncillaRegister))
            """
            Assertion for the current Qiskrypt's Ancilla Quantum Register of
            the Qiskrypt's Quantum Circuit has an IBM's Qiskit Ancilla Register.
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

            assert(isinstance(qiskrypt_classical_register.get_qiskit_classical_register(), ClassicalRegister))
            """
            Assertion for the current Qiskrypt's Classical Register of
            the Qiskrypt's Quantum Circuit has an IBM's Qiskit Classical Register.
            """

        assert(qiskrypt_quantum_circuit.get_total_num_qubits() == ancilla_quantum_register_num_qubits)
        """
        Assertion for the total number of qubits of
        all the Qiskrypt's Ancilla Quantum Registers of the Qiskrypt's Quantum Circuit.
        """

        assert(qiskrypt_quantum_circuit.get_num_qubits_in_qiskit_quantum_register(0) == ancilla_quantum_register_num_qubits)
        """
        Assertion for the number of qubits of
        the 1st Qiskrypt's Ancilla Quantum Register of the Qiskrypt's Quantum Circuit.
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

    def test_no_12_creation_qiskrypt_quantum_circuit_with_1_ancilla_fully_quantum_register_1_qubit_and_1_classical_register_1_bit(self):
        """
        Test Case #12:

        - Create a Qiskrypt's Quantum Circuit with:
            (i) 1 Ancilla Fully-Quantum Register (with 1 qubit).
           (ii) 1 Classical Register (with 1 bit).

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
                                                qiskit_ancilla_quantum_register=None)
        """
        Create a Qiskrypt's Ancilla Fully-Quantum Register, given its name and number of qubits.
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

        quantum_circuit_name = "qu_circ"
        """
        Set the name of the Qiskrypt's Quantum Circuit.
        """

        qiskrypt_quantum_circuit = \
            QiskryptQuantumCircuit(name=quantum_circuit_name,
                                   qiskrypt_quantum_registers=None,
                                   qiskrypt_fully_quantum_registers=None,
                                   qiskrypt_semi_quantum_registers=None,
                                   qiskrypt_ancilla_quantum_registers=None,
                                   qiskrypt_ancilla_fully_quantum_registers=[qiskrypt_ancilla_fully_quantum_register],
                                   qiskrypt_ancilla_semi_quantum_registers=None,
                                   qiskrypt_classical_registers=[qiskrypt_classical_register],
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

            assert(not isinstance(qiskrypt_ancilla_fully_quantum_register, QiskryptClassicalRegister))
            """
            Assertion for the current Qiskrypt's Ancilla Fully-Quantum Register of
            the Qiskrypt's Quantum Circuit do not be an actual Qiskrypt's Classical Register.
            """

            assert(isinstance(qiskrypt_ancilla_fully_quantum_register.get_qiskit_ancilla_quantum_register(), AncillaRegister))
            """
            Assertion for the current Qiskrypt's Ancilla Fully-Quantum Register of
            the Qiskrypt's Quantum Circuit has an IBM's Qiskit Ancilla Register.
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

            assert(isinstance(qiskrypt_classical_register.get_qiskit_classical_register(), ClassicalRegister))
            """
            Assertion for the current Qiskrypt's Classical Register of
            the Qiskrypt's Quantum Circuit has an IBM's Qiskit Classical Register.
            """

        assert(qiskrypt_quantum_circuit.get_total_num_qubits() == ancilla_fully_quantum_register_num_qubits)
        """
        Assertion for the total number of qubits of
        all the Qiskrypt's Ancilla Fully-Quantum Registers of the Qiskrypt's Quantum Circuit.
        """

        assert(qiskrypt_quantum_circuit.get_num_qubits_in_qiskit_quantum_register(0) == ancilla_fully_quantum_register_num_qubits)
        """
        Assertion for the number of qubits of
        the 1st Qiskrypt's Ancilla Fully-Quantum Register of the Qiskrypt's Quantum Circuit.
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

    def test_no_13_creation_qiskrypt_quantum_circuit_with_1_ancilla_semi_quantum_register_1_qubit_and_1_classical_register_1_bit(self):
        """
        Test Case #13:

        - Create a Qiskrypt's Quantum Circuit with:
            (i) 1 Ancilla Semi-Quantum Register (with 1 qubit).
           (ii) 1 Classical Register (with 1 bit).

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
                                               qiskit_ancilla_quantum_register=None)
        """
        Create a Qiskrypt's Ancilla Semi-Quantum Register, given its name and number of qubits.
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

        quantum_circuit_name = "qu_circ"
        """
        Set the name of the Qiskrypt's Quantum Circuit.
        """

        qiskrypt_quantum_circuit = \
            QiskryptQuantumCircuit(name=quantum_circuit_name,
                                   qiskrypt_quantum_registers=None,
                                   qiskrypt_fully_quantum_registers=None,
                                   qiskrypt_semi_quantum_registers=None,
                                   qiskrypt_ancilla_quantum_registers=None,
                                   qiskrypt_ancilla_fully_quantum_registers=None,
                                   qiskrypt_ancilla_semi_quantum_registers=[qiskrypt_ancilla_semi_quantum_register],
                                   qiskrypt_classical_registers=[qiskrypt_classical_register],
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

            assert(isinstance(qiskrypt_ancilla_semi_quantum_register.get_qiskit_ancilla_quantum_register(), AncillaRegister))
            """
            Assertion for the current Qiskrypt's Ancilla Semi-Quantum Register of
            the Qiskrypt's Quantum Circuit has an IBM's Qiskit Ancilla Register.
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

            assert(isinstance(qiskrypt_classical_register.get_qiskit_classical_register(), ClassicalRegister))
            """
            Assertion for the current Qiskrypt's Classical Register of
            the Qiskrypt's Quantum Circuit has an IBM's Qiskit Classical Register.
            """

        assert(qiskrypt_quantum_circuit.get_total_num_qubits() == ancilla_semi_quantum_register_num_qubits)
        """
        Assertion for the total number of qubits of
        all the Qiskrypt's Ancilla Semi-Quantum Registers of the Qiskrypt's Quantum Circuit.
        """

        assert(qiskrypt_quantum_circuit.get_num_qubits_in_qiskit_quantum_register(0) == ancilla_semi_quantum_register_num_qubits)
        """
        Assertion for the number of qubits of
        the 1st Qiskrypt's Ancilla Semi-Quantum Register of the Qiskrypt's Quantum Circuit.
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

    def test_no_14_creation_qiskrypt_quantum_circuit_with_1_quantum_register_1_qubit_1_fully_quantum_register_1_qubit_and_1_classical_register_1_bit(self):
        """
        Test Case #14:

        - Create a Qiskrypt's Quantum Circuit with:
             (i) 1 Quantum Register (with 1 qubit).
            (ii) 1 Fully-Quantum Register (with 1 qubit).
           (iii) 1 Classical Register (with 1 bit).

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
                                    qiskit_quantum_register=None)
        """
        Create a Qiskrypt's Quantum Register, given its name and number of qubits.
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
                                         qiskit_quantum_register=None)
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
                                      qiskit_classical_register=None)
        """
        Create a Qiskrypt's Classical Register, given its name and number of bits.
        """

        quantum_circuit_name = "qu_circ"
        """
        Set the name of the Qiskrypt's Quantum Circuit.
        """

        qiskrypt_quantum_circuit = \
            QiskryptQuantumCircuit(name=quantum_circuit_name,
                                   qiskrypt_quantum_registers=[qiskrypt_quantum_register],
                                   qiskrypt_fully_quantum_registers=[qiskrypt_fully_quantum_register],
                                   qiskrypt_semi_quantum_registers=None,
                                   qiskrypt_ancilla_quantum_registers=None,
                                   qiskrypt_ancilla_fully_quantum_registers=None,
                                   qiskrypt_ancilla_semi_quantum_registers=None,
                                   qiskrypt_classical_registers=[qiskrypt_classical_register],
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

            assert(isinstance(qiskrypt_quantum_register.get_qiskit_quantum_register(), QuantumRegister))
            """
            Assertion for the current Qiskrypt's Quantum Register of
            the Qiskrypt's Quantum Circuit has an IBM's Qiskit Quantum Register.
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

            assert(isinstance(qiskrypt_fully_quantum_register.get_qiskit_quantum_register(), QuantumRegister))
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

            assert(isinstance(qiskrypt_classical_register.get_qiskit_classical_register(), ClassicalRegister))
            """
            Assertion for the current Qiskrypt's Classical Register of
            the Qiskrypt's Quantum Circuit has an IBM's Qiskit Classical Register.
            """

        assert(qiskrypt_quantum_circuit.get_total_num_qubits() == (quantum_register_num_qubits + fully_quantum_register_num_qubits))
        """
        Assertion for the total number of qubits of
        all the Qiskrypt's Quantum and Fully-Quantum Registers of the Qiskrypt's Quantum Circuit.
        """

        assert(qiskrypt_quantum_circuit.get_num_qubits_in_qiskit_quantum_register(0) == quantum_register_num_qubits)
        """
        Assertion for the number of qubits of
        the 1st Qiskrypt's Quantum Register of the Qiskrypt's Quantum Circuit.
        """

        assert(qiskrypt_quantum_circuit.get_num_qubits_in_qiskit_quantum_register(1) == fully_quantum_register_num_qubits)
        """
        Assertion for the number of qubits of
        the 2nd Qiskrypt's Fully-Quantum Register of the Qiskrypt's Quantum Circuit.
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

    def test_no_15_creation_qiskrypt_quantum_circuit_with_1_quantum_register_1_qubit_1_semi_quantum_register_1_qubit_and_1_classical_register_1_bit(self):
        """
        Test Case #15:

        - Create a Qiskrypt's Quantum Circuit with:
             (i) 1 Quantum Register (with 1 qubit).
            (ii) 1 Semi-Quantum Register (with 1 qubit).
           (iii) 1 Classical Register (with 1 bit).

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
                                    qiskit_quantum_register=None)
        """
        Create a Qiskrypt's Quantum Register, given its name and number of qubits.
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
                                        qiskit_quantum_register=None)
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
                                      qiskit_classical_register=None)
        """
        Create a Qiskrypt's Classical Register, given its name and number of bits.
        """

        quantum_circuit_name = "qu_circ"
        """
        Set the name of the Qiskrypt's Quantum Circuit.
        """

        qiskrypt_quantum_circuit = \
            QiskryptQuantumCircuit(name=quantum_circuit_name,
                                   qiskrypt_quantum_registers=[qiskrypt_quantum_register],
                                   qiskrypt_fully_quantum_registers=None,
                                   qiskrypt_semi_quantum_registers=[qiskrypt_semi_quantum_register],
                                   qiskrypt_ancilla_quantum_registers=None,
                                   qiskrypt_ancilla_fully_quantum_registers=None,
                                   qiskrypt_ancilla_semi_quantum_registers=None,
                                   qiskrypt_classical_registers=[qiskrypt_classical_register],
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

            assert(isinstance(qiskrypt_quantum_register.get_qiskit_quantum_register(), QuantumRegister))
            """
            Assertion for the current Qiskrypt's Quantum Register of
            the Qiskrypt's Quantum Circuit has an IBM's Qiskit Quantum Register.
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

            assert(isinstance(qiskrypt_semi_quantum_register.get_qiskit_quantum_register(), QuantumRegister))
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

            assert(isinstance(qiskrypt_classical_register.get_qiskit_classical_register(), ClassicalRegister))
            """
            Assertion for the current Qiskrypt's Classical Register of
            the Qiskrypt's Quantum Circuit has an IBM's Qiskit Classical Register.
            """

        assert(qiskrypt_quantum_circuit.get_total_num_qubits() == (quantum_register_num_qubits + semi_quantum_register_num_qubits))
        """
        Assertion for the total number of qubits of
        all the Qiskrypt's Quantum and Semi-Quantum Registers of the Qiskrypt's Quantum Circuit.
        """

        assert(qiskrypt_quantum_circuit.get_num_qubits_in_qiskit_quantum_register(0) == quantum_register_num_qubits)
        """
        Assertion for the number of qubits of
        the 1st Qiskrypt's Quantum Register of the Qiskrypt's Quantum Circuit.
        """

        assert(qiskrypt_quantum_circuit.get_num_qubits_in_qiskit_quantum_register(1) == semi_quantum_register_num_qubits)
        """
        Assertion for the number of qubits of
        the 2nd Qiskrypt's Semi-Quantum Register of the Qiskrypt's Quantum Circuit.
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

    def test_no_16_creation_qiskrypt_quantum_circuit_with_1_quantum_register_1_qubit_1_ancilla_quantum_register_1_qubit_and_1_classical_register_1_bit(self):
        """
        Test Case #16:

        - Create a Qiskrypt's Quantum Circuit with:
             (i) 1 Quantum Register (with 1 qubit).
            (ii) 1 Ancilla Quantum Register (with 1 qubit).
           (iii) 1 Classical Register (with 1 bit).

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
                                    qiskit_quantum_register=None)
        """
        Create a Qiskrypt's Quantum Register, given its name and number of qubits.
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

        quantum_circuit_name = "qu_circ"
        """
        Set the name of the Qiskrypt's Quantum Circuit.
        """

        qiskrypt_quantum_circuit = \
            QiskryptQuantumCircuit(name=quantum_circuit_name,
                                   qiskrypt_quantum_registers=[qiskrypt_quantum_register],
                                   qiskrypt_fully_quantum_registers=None,
                                   qiskrypt_semi_quantum_registers=None,
                                   qiskrypt_ancilla_quantum_registers=[qiskrypt_ancilla_quantum_register],
                                   qiskrypt_ancilla_fully_quantum_registers=None,
                                   qiskrypt_ancilla_semi_quantum_registers=None,
                                   qiskrypt_classical_registers=[qiskrypt_classical_register],
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

            assert(isinstance(qiskrypt_quantum_register.get_qiskit_quantum_register(), QuantumRegister))
            """
            Assertion for the current Qiskrypt's Quantum Register of
            the Qiskrypt's Quantum Circuit has an IBM's Qiskit Quantum Register.
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

            assert(isinstance(qiskrypt_ancilla_quantum_register.get_qiskit_ancilla_quantum_register(), QuantumRegister))
            """
            Assertion for the current Qiskrypt's Ancilla Quantum Register of
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

            assert(isinstance(qiskrypt_classical_register.get_qiskit_classical_register(), ClassicalRegister))
            """
            Assertion for the current Qiskrypt's Classical Register of
            the Qiskrypt's Quantum Circuit has an IBM's Qiskit Classical Register.
            """

        assert(qiskrypt_quantum_circuit.get_total_num_qubits() == (quantum_register_num_qubits + ancilla_quantum_register_num_qubits))
        """
        Assertion for the total number of qubits of
        all the Qiskrypt's Quantum and Ancilla Quantum Registers of the Qiskrypt's Quantum Circuit.
        """

        assert(qiskrypt_quantum_circuit.get_num_qubits_in_qiskit_quantum_register(0) == quantum_register_num_qubits)
        """
        Assertion for the number of qubits of
        the 1st Qiskrypt's Quantum Register of the Qiskrypt's Quantum Circuit.
        """

        assert(qiskrypt_quantum_circuit.get_num_qubits_in_qiskit_quantum_register(1) == ancilla_quantum_register_num_qubits)
        """
        Assertion for the number of qubits of
        the 2nd Qiskrypt's Ancilla Quantum Register of the Qiskrypt's Quantum Circuit.
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

    def test_no_17_creation_qiskrypt_quantum_circuit_with_1_quantum_register_1_qubit_1_ancilla_fully_quantum_register_1_qubit_and_1_classical_register_1_bit(self):
        """
        Test Case #17:

        - Create a Qiskrypt's Quantum Circuit with:
             (i) 1 Quantum Register (with 1 qubit).
            (ii) 1 Ancilla Fully-Quantum Register (with 1 qubit).
           (iii) 1 Classical Register (with 1 bit).

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
                                    qiskit_quantum_register=None)
        """
        Create a Qiskrypt's Quantum Register, given its name and number of qubits.
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
                                                qiskit_ancilla_quantum_register=None)
        """
        Create a Qiskrypt's Ancilla Quantum Register, given its name and number of qubits.
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

        quantum_circuit_name = "qu_circ"
        """
        Set the name of the Qiskrypt's Quantum Circuit.
        """

        qiskrypt_quantum_circuit = \
            QiskryptQuantumCircuit(name=quantum_circuit_name,
                                   qiskrypt_quantum_registers=[qiskrypt_quantum_register],
                                   qiskrypt_fully_quantum_registers=None,
                                   qiskrypt_semi_quantum_registers=None,
                                   qiskrypt_ancilla_quantum_registers=None,
                                   qiskrypt_ancilla_fully_quantum_registers=[qiskrypt_ancilla_fully_quantum_register],
                                   qiskrypt_ancilla_semi_quantum_registers=None,
                                   qiskrypt_classical_registers=[qiskrypt_classical_register],
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

            assert(isinstance(qiskrypt_quantum_register.get_qiskit_quantum_register(), QuantumRegister))
            """
            Assertion for the current Qiskrypt's Quantum Register of
            the Qiskrypt's Quantum Circuit has an IBM's Qiskit Quantum Register.
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

            assert(not isinstance(qiskrypt_ancilla_fully_quantum_register, QiskryptClassicalRegister))
            """
            Assertion for the current Qiskrypt's Ancilla Fully-Quantum Register of
            the Qiskrypt's Quantum Circuit do not be an actual Qiskrypt's Classical Register.
            """

            assert(isinstance(qiskrypt_ancilla_fully_quantum_register.get_qiskit_ancilla_quantum_register(), QuantumRegister))
            """
            Assertion for the current Qiskrypt's Ancilla Fully-Quantum Register of
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

            assert(isinstance(qiskrypt_classical_register.get_qiskit_classical_register(), ClassicalRegister))
            """
            Assertion for the current Qiskrypt's Classical Register of
            the Qiskrypt's Quantum Circuit has an IBM's Qiskit Classical Register.
            """

        assert(qiskrypt_quantum_circuit.get_total_num_qubits() == (quantum_register_num_qubits + ancilla_fully_quantum_register_num_qubits))
        """
        Assertion for the total number of qubits of
        all the Qiskrypt's Quantum and Ancilla Fully-Quantum Registers of the Qiskrypt's Quantum Circuit.
        """

        assert(qiskrypt_quantum_circuit.get_num_qubits_in_qiskit_quantum_register(0) == quantum_register_num_qubits)
        """
        Assertion for the number of qubits of
        the 1st Qiskrypt's Quantum Register of the Qiskrypt's Quantum Circuit.
        """

        assert(qiskrypt_quantum_circuit.get_num_qubits_in_qiskit_quantum_register(1) == ancilla_fully_quantum_register_num_qubits)
        """
        Assertion for the number of qubits of
        the 2nd Qiskrypt's Ancilla Fully-Quantum Register of the Qiskrypt's Quantum Circuit.
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

    def test_no_18_creation_qiskrypt_quantum_circuit_with_1_quantum_register_1_qubit_1_ancilla_semi_quantum_register_1_qubit_and_1_classical_register_1_bit(self):
        """
        Test Case #18:

        - Create a Qiskrypt's Quantum Circuit with:
             (i) 1 Quantum Register (with 1 qubit).
            (ii) 1 Ancilla Semi-Quantum Register (with 1 qubit).
           (iii) 1 Classical Register (with 1 bit).

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
                                    qiskit_quantum_register=None)
        """
        Create a Qiskrypt's Quantum Register, given its name and number of qubits.
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
                                               qiskit_ancilla_quantum_register=None)
        """
        Create a Qiskrypt's Ancilla Semi-Quantum Register, given its name and number of qubits.
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

        quantum_circuit_name = "qu_circ"
        """
        Set the name of the Qiskrypt's Quantum Circuit.
        """

        qiskrypt_quantum_circuit = \
            QiskryptQuantumCircuit(name=quantum_circuit_name,
                                   qiskrypt_quantum_registers=[qiskrypt_quantum_register],
                                   qiskrypt_fully_quantum_registers=None,
                                   qiskrypt_semi_quantum_registers=None,
                                   qiskrypt_ancilla_quantum_registers=None,
                                   qiskrypt_ancilla_fully_quantum_registers=None,
                                   qiskrypt_ancilla_semi_quantum_registers=[qiskrypt_ancilla_semi_quantum_register],
                                   qiskrypt_classical_registers=[qiskrypt_classical_register],
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

            assert(isinstance(qiskrypt_quantum_register.get_qiskit_quantum_register(), QuantumRegister))
            """
            Assertion for the current Qiskrypt's Quantum Register of
            the Qiskrypt's Quantum Circuit has an IBM's Qiskit Quantum Register.
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

            assert(isinstance(qiskrypt_ancilla_semi_quantum_register.get_qiskit_ancilla_quantum_register(), QuantumRegister))
            """
            Assertion for the current Qiskrypt's Ancilla Semi-Quantum Register of
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

            assert(isinstance(qiskrypt_classical_register.get_qiskit_classical_register(), ClassicalRegister))
            """
            Assertion for the current Qiskrypt's Classical Register of
            the Qiskrypt's Quantum Circuit has an IBM's Qiskit Classical Register.
            """

        assert(qiskrypt_quantum_circuit.get_total_num_qubits() == (quantum_register_num_qubits + ancilla_semi_quantum_register_num_qubits))
        """
        Assertion for the total number of qubits of
        all the Qiskrypt's Quantum and Ancilla Semi-Quantum Registers of the Qiskrypt's Quantum Circuit.
        """

        assert(qiskrypt_quantum_circuit.get_num_qubits_in_qiskit_quantum_register(0) == quantum_register_num_qubits)
        """
        Assertion for the number of qubits of
        the 1st Qiskrypt's Quantum Register of the Qiskrypt's Quantum Circuit.
        """

        assert(qiskrypt_quantum_circuit.get_num_qubits_in_qiskit_quantum_register(1) == ancilla_semi_quantum_register_num_qubits)
        """
        Assertion for the number of qubits of
        the 2nd Qiskrypt's Ancilla Semi-Quantum Register of the Qiskrypt's Quantum Circuit.
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

    def test_no_19_creation_qiskrypt_quantum_circuit_with_1_quantum_register_1_qubit_1_fully_quantum_register_1_qubit_1_semi_quantum_register_1_qubit_and_1_classical_register_1_bit(self):
        """
        Test Case #19:

        - Create a Qiskrypt's Quantum Circuit with:
             (i) 1 Quantum Register (with 1 qubit).
            (ii) 1 Fully-Quantum Register (with 1 qubit).
           (iii) 1 Semi-Quantum Register (with 1 qubit).
            (iv) 1 Classical Register (with 1 bit).

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
                                    qiskit_quantum_register=None)
        """
        Create a Qiskrypt's Quantum Register, given its name and number of qubits.
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
                                         qiskit_quantum_register=None)
        """
        Create a Qiskrypt's Fully-Quantum Register, given its name and number of qubits.
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
                                        qiskit_quantum_register=None)
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
                                      qiskit_classical_register=None)
        """
        Create a Qiskrypt's Classical Register, given its name and number of bits.
        """

        quantum_circuit_name = "qu_circ"
        """
        Set the name of the Qiskrypt's Quantum Circuit.
        """

        qiskrypt_quantum_circuit = \
            QiskryptQuantumCircuit(name=quantum_circuit_name,
                                   qiskrypt_quantum_registers=[qiskrypt_quantum_register],
                                   qiskrypt_fully_quantum_registers=[qiskrypt_fully_quantum_register],
                                   qiskrypt_semi_quantum_registers=[qiskrypt_semi_quantum_register],
                                   qiskrypt_ancilla_quantum_registers=None,
                                   qiskrypt_ancilla_fully_quantum_registers=None,
                                   qiskrypt_ancilla_semi_quantum_registers=None,
                                   qiskrypt_classical_registers=[qiskrypt_classical_register],
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

            assert(isinstance(qiskrypt_quantum_register.get_qiskit_quantum_register(), QuantumRegister))
            """
            Assertion for the current Qiskrypt's Quantum Register of
            the Qiskrypt's Quantum Circuit has an IBM's Qiskit Quantum Register.
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

            assert(isinstance(qiskrypt_fully_quantum_register.get_qiskit_fully_quantum_register(), QuantumRegister))
            """
            Assertion for the current Qiskrypt's Fully-Quantum Register of
            the Qiskrypt's Quantum Circuit has an IBM's Qiskit Quantum Register.
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

            assert(isinstance(qiskrypt_semi_quantum_register.get_qiskit_semi_quantum_register(), QuantumRegister))
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

            assert(isinstance(qiskrypt_classical_register.get_qiskit_classical_register(), ClassicalRegister))
            """
            Assertion for the current Qiskrypt's Classical Register of
            the Qiskrypt's Quantum Circuit has an IBM's Qiskit Classical Register.
            """

        assert(qiskrypt_quantum_circuit.get_total_num_qubits() == (quantum_register_num_qubits + fully_quantum_register_num_qubits + semi_quantum_register_num_qubits))
        """
        Assertion for the total number of qubits of
        all the Qiskrypt's Quantum, Fully-Quantum and Semi-Quantum Registers of the Qiskrypt's Quantum Circuit.
        """

        assert(qiskrypt_quantum_circuit.get_num_qubits_in_qiskit_quantum_register(0) == quantum_register_num_qubits)
        """
        Assertion for the number of qubits of
        the 1st Qiskrypt's Quantum Register of the Qiskrypt's Quantum Circuit.
        """

        assert(qiskrypt_quantum_circuit.get_num_qubits_in_qiskit_quantum_register(1) == fully_quantum_register_num_qubits)
        """
        Assertion for the number of qubits of
        the 2nd Qiskrypt's Fully-Quantum Register of the Qiskrypt's Quantum Circuit.
        """

        assert(qiskrypt_quantum_circuit.get_num_qubits_in_qiskit_quantum_register(2) == semi_quantum_register_num_qubits)
        """
        Assertion for the number of qubits of
        the 3rd Qiskrypt's Semi-Quantum Register of the Qiskrypt's Quantum Circuit.
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

    def test_no_20_creation_qiskrypt_quantum_circuit_with_1_quantum_register_1_qubit_1_fully_quantum_register_1_qubit_1_ancilla_quantum_register_1_qubit_and_1_classical_register_1_bit(self):
        """
        Test Case #20:

        - Create a Qiskrypt's Quantum Circuit with:
             (i) 1 Quantum Register (with 1 qubit).
            (ii) 1 Fully-Quantum Register (with 1 qubit).
           (iii) 1 Ancilla Quantum Register (with 1 qubit).
            (iv) 1 Classical Register (with 1 bit).

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
                                    qiskit_quantum_register=None)
        """
        Create a Qiskrypt's Quantum Register, given its name and number of qubits.
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
                                         qiskit_quantum_register=None)
        """
        Create a Qiskrypt's Fully-Quantum Register, given its name and number of qubits.
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

        quantum_circuit_name = "qu_circ"
        """
        Set the name of the Qiskrypt's Quantum Circuit.
        """

        qiskrypt_quantum_circuit = \
            QiskryptQuantumCircuit(name=quantum_circuit_name,
                                   qiskrypt_quantum_registers=[qiskrypt_quantum_register],
                                   qiskrypt_fully_quantum_registers=[qiskrypt_fully_quantum_register],
                                   qiskrypt_semi_quantum_registers=None,
                                   qiskrypt_ancilla_quantum_registers=[qiskrypt_ancilla_quantum_register],
                                   qiskrypt_ancilla_fully_quantum_registers=None,
                                   qiskrypt_ancilla_semi_quantum_registers=None,
                                   qiskrypt_classical_registers=[qiskrypt_classical_register],
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

            assert(isinstance(qiskrypt_quantum_register.get_qiskit_quantum_register(), QuantumRegister))
            """
            Assertion for the current Qiskrypt's Quantum Register of
            the Qiskrypt's Quantum Circuit has an IBM's Qiskit Quantum Register.
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

            assert(isinstance(qiskrypt_fully_quantum_register.get_qiskit_fully_quantum_register(), QuantumRegister))
            """
            Assertion for the current Qiskrypt's Fully-Quantum Register of
            the Qiskrypt's Quantum Circuit has an IBM's Qiskit Quantum Register.
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

            assert(isinstance(qiskrypt_ancilla_quantum_register.get_qiskit_ancilla_quantum_register(), QuantumRegister))
            """
            Assertion for the current Qiskrypt's Ancilla Quantum Register of
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

            assert(isinstance(qiskrypt_classical_register.get_qiskit_classical_register(), ClassicalRegister))
            """
            Assertion for the current Qiskrypt's Classical Register of
            the Qiskrypt's Quantum Circuit has an IBM's Qiskit Classical Register.
            """

        assert(qiskrypt_quantum_circuit.get_total_num_qubits() == (quantum_register_num_qubits + fully_quantum_register_num_qubits + ancilla_quantum_register_num_qubits))
        """
        Assertion for the total number of qubits of
        all the Qiskrypt's Quantum, Fully-Quantum and Ancilla Quantum Registers of the Qiskrypt's Quantum Circuit.
        """

        assert(qiskrypt_quantum_circuit.get_num_qubits_in_qiskit_quantum_register(0) == quantum_register_num_qubits)
        """
        Assertion for the number of qubits of
        the 1st Qiskrypt's Quantum Register of the Qiskrypt's Quantum Circuit.
        """

        assert(qiskrypt_quantum_circuit.get_num_qubits_in_qiskit_quantum_register(1) == fully_quantum_register_num_qubits)
        """
        Assertion for the number of qubits of
        the 2nd Qiskrypt's Fully-Quantum Register of the Qiskrypt's Quantum Circuit.
        """

        assert(qiskrypt_quantum_circuit.get_num_qubits_in_qiskit_quantum_register(2) == ancilla_quantum_register_num_qubits)
        """
        Assertion for the number of qubits of
        the 3rd Qiskrypt's Ancilla Quantum Register of the Qiskrypt's Quantum Circuit.
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

    def test_no_21_creation_qiskrypt_quantum_circuit_with_1_quantum_register_1_qubit_1_fully_quantum_register_1_qubit_1_ancilla_fully_quantum_register_1_qubit_and_1_classical_register_1_bit(self):
        """
        Test Case #21:

        - Create a Qiskrypt's Quantum Circuit with:
             (i) 1 Quantum Register (with 1 qubit).
            (ii) 1 Fully-Quantum Register (with 1 qubit).
           (iii) 1 Ancilla Fully-Quantum Register (with 1 qubit).
            (iv) 1 Classical Register (with 1 bit).

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
                                    qiskit_quantum_register=None)
        """
        Create a Qiskrypt's Quantum Register, given its name and number of qubits.
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
                                         qiskit_quantum_register=None)
        """
        Create a Qiskrypt's Fully-Quantum Register, given its name and number of qubits.
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
                                                qiskit_ancilla_quantum_register=None)
        """
        Create a Qiskrypt's Ancilla Fully-Quantum Register, given its name and number of qubits.
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

        quantum_circuit_name = "qu_circ"
        """
        Set the name of the Qiskrypt's Quantum Circuit.
        """

        qiskrypt_quantum_circuit = \
            QiskryptQuantumCircuit(name=quantum_circuit_name,
                                   qiskrypt_quantum_registers=[qiskrypt_quantum_register],
                                   qiskrypt_fully_quantum_registers=[qiskrypt_fully_quantum_register],
                                   qiskrypt_semi_quantum_registers=None,
                                   qiskrypt_ancilla_quantum_registers=None,
                                   qiskrypt_ancilla_fully_quantum_registers=[qiskrypt_ancilla_fully_quantum_register],
                                   qiskrypt_ancilla_semi_quantum_registers=None,
                                   qiskrypt_classical_registers=[qiskrypt_classical_register],
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

            assert(isinstance(qiskrypt_quantum_register.get_qiskit_quantum_register(), QuantumRegister))
            """
            Assertion for the current Qiskrypt's Quantum Register of
            the Qiskrypt's Quantum Circuit has an IBM's Qiskit Quantum Register.
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

            assert(isinstance(qiskrypt_fully_quantum_register.get_qiskit_fully_quantum_register(), QuantumRegister))
            """
            Assertion for the current Qiskrypt's Fully-Quantum Register of
            the Qiskrypt's Quantum Circuit has an IBM's Qiskit Quantum Register.
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

            assert(not isinstance(qiskrypt_ancilla_fully_quantum_register, QiskryptClassicalRegister))
            """
            Assertion for the current Qiskrypt's Ancilla Fully-Quantum Register of
            the Qiskrypt's Quantum Circuit do not be an actual Qiskrypt's Classical Register.
            """

            assert(isinstance(qiskrypt_ancilla_fully_quantum_register.get_qiskit_ancilla_quantum_register(), QuantumRegister))
            """
            Assertion for the current Qiskrypt's Ancilla Fully-Quantum Register of
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

            assert(isinstance(qiskrypt_classical_register.get_qiskit_classical_register(), ClassicalRegister))
            """
            Assertion for the current Qiskrypt's Classical Register of
            the Qiskrypt's Quantum Circuit has an IBM's Qiskit Classical Register.
            """

        assert(qiskrypt_quantum_circuit.get_total_num_qubits() == (quantum_register_num_qubits + fully_quantum_register_num_qubits + ancilla_fully_quantum_register_num_qubits))
        """
        Assertion for the total number of qubits of
        all the Qiskrypt's Quantum, Fully-Quantum and Ancilla Fully-Quantum Registers of the Qiskrypt's Quantum Circuit.
        """

        assert(qiskrypt_quantum_circuit.get_num_qubits_in_qiskit_quantum_register(0) == quantum_register_num_qubits)
        """
        Assertion for the number of qubits of
        the 1st Qiskrypt's Quantum Register of the Qiskrypt's Quantum Circuit.
        """

        assert(qiskrypt_quantum_circuit.get_num_qubits_in_qiskit_quantum_register(1) == fully_quantum_register_num_qubits)
        """
        Assertion for the number of qubits of
        the 2nd Qiskrypt's Fully-Quantum Register of the Qiskrypt's Quantum Circuit.
        """

        assert(qiskrypt_quantum_circuit.get_num_qubits_in_qiskit_quantum_register(2) == ancilla_fully_quantum_register_num_qubits)
        """
        Assertion for the number of qubits of
        the 3rd Qiskrypt's Ancilla Fully-Quantum Register of the Qiskrypt's Quantum Circuit.
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

    def test_no_22_creation_qiskrypt_quantum_circuit_with_1_quantum_register_1_qubit_1_fully_quantum_register_1_qubit_1_ancilla_semi_quantum_register_1_qubit_and_1_classical_register_1_bit(self):
        """
        Test Case #22:

        - Create a Qiskrypt's Quantum Circuit with:
             (i) 1 Quantum Register (with 1 qubit).
            (ii) 1 Fully-Quantum Register (with 1 qubit).
           (iii) 1 Ancilla Semi-Quantum Register (with 1 qubit).
            (iv) 1 Classical Register (with 1 bit).

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
                                    qiskit_quantum_register=None)
        """
        Create a Qiskrypt's Quantum Register, given its name and number of qubits.
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
                                         qiskit_quantum_register=None)
        """
        Create a Qiskrypt's Fully-Quantum Register, given its name and number of qubits.
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
                                               qiskit_ancilla_quantum_register=None)
        """
        Create a Qiskrypt's Ancilla Semi-Quantum Register, given its name and number of qubits.
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

        quantum_circuit_name = "qu_circ"
        """
        Set the name of the Qiskrypt's Quantum Circuit.
        """

        qiskrypt_quantum_circuit = \
            QiskryptQuantumCircuit(name=quantum_circuit_name,
                                   qiskrypt_quantum_registers=[qiskrypt_quantum_register],
                                   qiskrypt_fully_quantum_registers=[qiskrypt_fully_quantum_register],
                                   qiskrypt_semi_quantum_registers=None,
                                   qiskrypt_ancilla_quantum_registers=None,
                                   qiskrypt_ancilla_fully_quantum_registers=None,
                                   qiskrypt_ancilla_semi_quantum_registers=[qiskrypt_ancilla_semi_quantum_register],
                                   qiskrypt_classical_registers=[qiskrypt_classical_register],
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

            assert(isinstance(qiskrypt_quantum_register.get_qiskit_quantum_register(), QuantumRegister))
            """
            Assertion for the current Qiskrypt's Quantum Register of
            the Qiskrypt's Quantum Circuit has an IBM's Qiskit Quantum Register.
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

            assert(isinstance(qiskrypt_fully_quantum_register.get_qiskit_fully_quantum_register(), QuantumRegister))
            """
            Assertion for the current Qiskrypt's Fully-Quantum Register of
            the Qiskrypt's Quantum Circuit has an IBM's Qiskit Quantum Register.
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

            assert(isinstance(qiskrypt_ancilla_semi_quantum_register.get_qiskit_ancilla_quantum_register(), AncillaRegister))
            """
            Assertion for the current Qiskrypt's Ancilla Semi-Quantum Register of
            the Qiskrypt's Quantum Circuit has an IBM's Qiskit Ancilla Register.
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

            assert(isinstance(qiskrypt_classical_register.get_qiskit_classical_register(), ClassicalRegister))
            """
            Assertion for the current Qiskrypt's Classical Register of
            the Qiskrypt's Quantum Circuit has an IBM's Qiskit Classical Register.
            """

        assert(qiskrypt_quantum_circuit.get_total_num_qubits() == (quantum_register_num_qubits + fully_quantum_register_num_qubits + ancilla_semi_quantum_register_num_qubits))
        """
        Assertion for the total number of qubits of
        all the Qiskrypt's Quantum, Fully-Quantum and Ancilla Semi-Quantum Registers of the Qiskrypt's Quantum Circuit.
        """

        assert(qiskrypt_quantum_circuit.get_num_qubits_in_qiskit_quantum_register(0) == quantum_register_num_qubits)
        """
        Assertion for the number of qubits of
        the 1st Qiskrypt's Quantum Register of the Qiskrypt's Quantum Circuit.
        """

        assert(qiskrypt_quantum_circuit.get_num_qubits_in_qiskit_quantum_register(1) == fully_quantum_register_num_qubits)
        """
        Assertion for the number of qubits of
        the 2nd Qiskrypt's Fully-Quantum Register of the Qiskrypt's Quantum Circuit.
        """

        assert(qiskrypt_quantum_circuit.get_num_qubits_in_qiskit_quantum_register(2) == ancilla_semi_quantum_register_num_qubits)
        """
        Assertion for the number of qubits of
        the 3rd Qiskrypt's Ancilla Semi-Quantum Register of the Qiskrypt's Quantum Circuit.
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

    def test_no_23_creation_qiskrypt_quantum_circuit_with_1_quantum_register_1_qubit_1_fully_quantum_register_1_qubit_1_semi_quantum_register_1_qubit_1_ancilla_quantum_register_1_qubit_and_1_classical_register_1_bit(self):
        """
        Test Case #23:

        - Create a Qiskrypt's Quantum Circuit with:
             (i) 1 Quantum Register (with 1 qubit).
            (ii) 1 Fully-Quantum Register (with 1 qubit).
           (iii) 1 Semi-Quantum Register (with 1 qubit).
            (iv) 1 Ancilla Quantum Register (with 1 qubit).
             (v) 1 Classical Register (with 1 bit).

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
                                    qiskit_quantum_register=None)
        """
        Create a Qiskrypt's Quantum Register, given its name and number of qubits.
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
                                         qiskit_quantum_register=None)
        """
        Create a Qiskrypt's Fully-Quantum Register, given its name and number of qubits.
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
                                        qiskit_quantum_register=None)
        """
        Create a Qiskrypt's Semi-Quantum Register, given its name and number of qubits.
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

        quantum_circuit_name = "qu_circ"
        """
        Set the name of the Qiskrypt's Quantum Circuit.
        """

        qiskrypt_quantum_circuit = \
            QiskryptQuantumCircuit(name=quantum_circuit_name,
                                   qiskrypt_quantum_registers=[qiskrypt_quantum_register],
                                   qiskrypt_fully_quantum_registers=[qiskrypt_fully_quantum_register],
                                   qiskrypt_semi_quantum_registers=[qiskrypt_semi_quantum_register],
                                   qiskrypt_ancilla_quantum_registers=[qiskrypt_ancilla_quantum_register],
                                   qiskrypt_ancilla_fully_quantum_registers=None,
                                   qiskrypt_ancilla_semi_quantum_registers=None,
                                   qiskrypt_classical_registers=[qiskrypt_classical_register],
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

            assert(isinstance(qiskrypt_quantum_register.get_qiskit_quantum_register(), QuantumRegister))
            """
            Assertion for the current Qiskrypt's Quantum Register of
            the Qiskrypt's Quantum Circuit has an IBM's Qiskit Quantum Register.
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

            assert(isinstance(qiskrypt_fully_quantum_register.get_qiskit_fully_quantum_register(), QuantumRegister))
            """
            Assertion for the current Qiskrypt's Fully-Quantum Register of
            the Qiskrypt's Quantum Circuit has an IBM's Qiskit Quantum Register.
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

            assert(isinstance(qiskrypt_semi_quantum_register.get_qiskit_semi_quantum_register(), QuantumRegister))
            """
            Assertion for the current Qiskrypt's Semi-Quantum Register of
            the Qiskrypt's Quantum Circuit has an IBM's Qiskit Quantum Register.
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
            the Qiskrypt's Quantum Circuit be an actual Qiskrypt's Ancilla Semi-Quantum Register.
            """

            assert(not isinstance(qiskrypt_ancilla_quantum_register, QiskryptClassicalRegister))
            """
            Assertion for the current Qiskrypt's Ancilla Semi-Quantum Register of
            the Qiskrypt's Quantum Circuit do not be an actual Qiskrypt's Classical Register.
            """

            assert(isinstance(qiskrypt_ancilla_quantum_register.get_qiskit_ancilla_quantum_register(), AncillaRegister))
            """
            Assertion for the current Qiskrypt's Ancilla Semi-Quantum Register of
            the Qiskrypt's Quantum Circuit has an IBM's Qiskit Ancilla Register.
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

            assert(isinstance(qiskrypt_classical_register.get_qiskit_classical_register(), ClassicalRegister))
            """
            Assertion for the current Qiskrypt's Classical Register of
            the Qiskrypt's Quantum Circuit has an IBM's Qiskit Classical Register.
            """

        assert(qiskrypt_quantum_circuit.get_total_num_qubits() == (quantum_register_num_qubits + fully_quantum_register_num_qubits + semi_quantum_register_num_qubits + ancilla_quantum_register_num_qubits))
        """
        Assertion for the total number of qubits of
        all the Qiskrypt's Quantum, Fully-Quantum, Semi-Quantum and Ancilla Semi-Quantum Registers of the Qiskrypt's Quantum Circuit.
        """

        assert(qiskrypt_quantum_circuit.get_num_qubits_in_qiskit_quantum_register(0) == quantum_register_num_qubits)
        """
        Assertion for the number of qubits of
        the 1st Qiskrypt's Quantum Register of the Qiskrypt's Quantum Circuit.
        """

        assert(qiskrypt_quantum_circuit.get_num_qubits_in_qiskit_quantum_register(1) == fully_quantum_register_num_qubits)
        """
        Assertion for the number of qubits of
        the 2nd Qiskrypt's Fully-Quantum Register of the Qiskrypt's Quantum Circuit.
        """

        assert(qiskrypt_quantum_circuit.get_num_qubits_in_qiskit_quantum_register(2) == semi_quantum_register_num_qubits)
        """
        Assertion for the number of qubits of
        the 3rd Qiskrypt's Semi-Quantum Register of the Qiskrypt's Quantum Circuit.
        """

        assert(qiskrypt_quantum_circuit.get_num_qubits_in_qiskit_quantum_register(3) == ancilla_quantum_register_num_qubits)
        """
        Assertion for the number of qubits of
        the 4th Qiskrypt's Ancilla Quantum Register of the Qiskrypt's Quantum Circuit.
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

    def test_no_24_creation_qiskrypt_quantum_circuit_with_1_quantum_register_1_qubit_1_fully_quantum_register_1_qubit_1_semi_quantum_register_1_qubit_1_ancilla_fully_quantum_register_1_qubit_and_1_classical_register_1_bit(self):
        """
        Test Case #24:

        - Create a Qiskrypt's Quantum Circuit with:
             (i) 1 Quantum Register (with 1 qubit).
            (ii) 1 Fully-Quantum Register (with 1 qubit).
           (iii) 1 Semi-Quantum Register (with 1 qubit).
            (iv) 1 Ancilla Fully-Quantum Register (with 1 qubit).
             (v) 1 Classical Register (with 1 bit).

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
                                    qiskit_quantum_register=None)
        """
        Create a Qiskrypt's Quantum Register, given its name and number of qubits.
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
                                         qiskit_quantum_register=None)
        """
        Create a Qiskrypt's Fully-Quantum Register, given its name and number of qubits.
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
                                        qiskit_quantum_register=None)
        """
        Create a Qiskrypt's Fully-Quantum Register, given its name and number of qubits.
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
                                                qiskit_ancilla_quantum_register=None)
        """
        Create a Qiskrypt's Ancilla Fully-Quantum Register, given its name and number of qubits.
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

        quantum_circuit_name = "qu_circ"
        """
        Set the name of the Qiskrypt's Quantum Circuit.
        """

        qiskrypt_quantum_circuit = \
            QiskryptQuantumCircuit(name=quantum_circuit_name,
                                   qiskrypt_quantum_registers=[qiskrypt_quantum_register],
                                   qiskrypt_fully_quantum_registers=[qiskrypt_fully_quantum_register],
                                   qiskrypt_semi_quantum_registers=[qiskrypt_semi_quantum_register],
                                   qiskrypt_ancilla_quantum_registers=None,
                                   qiskrypt_ancilla_fully_quantum_registers=[qiskrypt_ancilla_fully_quantum_register],
                                   qiskrypt_ancilla_semi_quantum_registers=None,
                                   qiskrypt_classical_registers=[qiskrypt_classical_register],
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

            assert(isinstance(qiskrypt_quantum_register.get_qiskit_quantum_register(), QuantumRegister))
            """
            Assertion for the current Qiskrypt's Quantum Register of
            the Qiskrypt's Quantum Circuit has an IBM's Qiskit Quantum Register.
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

            assert(isinstance(qiskrypt_fully_quantum_register.get_qiskit_fully_quantum_register(), QuantumRegister))
            """
            Assertion for the current Qiskrypt's Fully-Quantum Register of
            the Qiskrypt's Quantum Circuit has an IBM's Qiskit Quantum Register.
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

            assert(isinstance(qiskrypt_semi_quantum_register.get_qiskit_semi_quantum_register(), QuantumRegister))
            """
            Assertion for the current Qiskrypt's Semi-Quantum Register of
            the Qiskrypt's Quantum Circuit has an IBM's Qiskit Quantum Register.
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

            assert(not isinstance(qiskrypt_ancilla_fully_quantum_register, QiskryptClassicalRegister))
            """
            Assertion for the current Qiskrypt's Ancilla Fully-Quantum Register of
            the Qiskrypt's Quantum Circuit do not be an actual Qiskrypt's Classical Register.
            """

            assert(isinstance(qiskrypt_ancilla_fully_quantum_register.get_qiskit_ancilla_quantum_register(), AncillaRegister))
            """
            Assertion for the current Qiskrypt's Ancilla Fully-Quantum Register of
            the Qiskrypt's Quantum Circuit has an IBM's Qiskit Ancilla Register.
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

            assert(isinstance(qiskrypt_classical_register.get_qiskit_classical_register(), ClassicalRegister))
            """
            Assertion for the current Qiskrypt's Classical Register of
            the Qiskrypt's Quantum Circuit has an IBM's Qiskit Classical Register.
            """

        assert(qiskrypt_quantum_circuit.get_total_num_qubits() == (quantum_register_num_qubits + fully_quantum_register_num_qubits + semi_quantum_register_num_qubits + ancilla_fully_quantum_register_num_qubits))
        """
        Assertion for the total number of qubits of
        all the Qiskrypt's Quantum, Fully-Quantum, Semi-Quantum and Ancilla Fully-Quantum Registers of the Qiskrypt's Quantum Circuit.
        """

        assert(qiskrypt_quantum_circuit.get_num_qubits_in_qiskit_quantum_register(0) == quantum_register_num_qubits)
        """
        Assertion for the number of qubits of
        the 1st Qiskrypt's Quantum Register of the Qiskrypt's Quantum Circuit.
        """

        assert(qiskrypt_quantum_circuit.get_num_qubits_in_qiskit_quantum_register(1) == fully_quantum_register_num_qubits)
        """
        Assertion for the number of qubits of
        the 2nd Qiskrypt's Fully-Quantum Register of the Qiskrypt's Quantum Circuit.
        """

        assert(qiskrypt_quantum_circuit.get_num_qubits_in_qiskit_quantum_register(2) == semi_quantum_register_num_qubits)
        """
        Assertion for the number of qubits of
        the 3rd Qiskrypt's Semi-Quantum Register of the Qiskrypt's Quantum Circuit.
        """

        assert(qiskrypt_quantum_circuit.get_num_qubits_in_qiskit_quantum_register(3) == ancilla_fully_quantum_register_num_qubits)
        """
        Assertion for the number of qubits of
        the 4th Qiskrypt's Ancilla Fully-Quantum Register of the Qiskrypt's Quantum Circuit.
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

    def test_no_25_creation_qiskrypt_quantum_circuit_with_1_quantum_register_1_qubit_1_fully_quantum_register_1_qubit_1_semi_quantum_register_1_qubit_1_ancilla_semi_quantum_register_1_qubit_and_1_classical_register_1_bit(self):
        """
        Test Case #25:

        - Create a Qiskrypt's Quantum Circuit with:
             (i) 1 Quantum Register (with 1 qubit).
            (ii) 1 Fully-Quantum Register (with 1 qubit).
           (iii) 1 Semi-Quantum Register (with 1 qubit).
            (iv) 1 Ancilla Semi-Quantum Register (with 1 qubit).
             (v) 1 Classical Register (with 1 bit).

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
                                    qiskit_quantum_register=None)
        """
        Create a Qiskrypt's Quantum Register, given its name and number of qubits.
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
                                         qiskit_quantum_register=None)
        """
        Create a Qiskrypt's Semi-Quantum Register, given its name and number of qubits.
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
                                        qiskit_quantum_register=None)
        """
        Create a Qiskrypt's Fully-Quantum Register, given its name and number of qubits.
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
                                               qiskit_ancilla_quantum_register=None)
        """
        Create a Qiskrypt's Ancilla Semi-Quantum Register, given its name and number of qubits.
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

        quantum_circuit_name = "qu_circ"
        """
        Set the name of the Qiskrypt's Quantum Circuit.
        """

        qiskrypt_quantum_circuit = \
            QiskryptQuantumCircuit(name=quantum_circuit_name,
                                   qiskrypt_quantum_registers=[qiskrypt_quantum_register],
                                   qiskrypt_fully_quantum_registers=[qiskrypt_fully_quantum_register],
                                   qiskrypt_semi_quantum_registers=[qiskrypt_semi_quantum_register],
                                   qiskrypt_ancilla_quantum_registers=None,
                                   qiskrypt_ancilla_fully_quantum_registers=None,
                                   qiskrypt_ancilla_semi_quantum_registers=[qiskrypt_ancilla_semi_quantum_register],
                                   qiskrypt_classical_registers=[qiskrypt_classical_register],
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

            assert(isinstance(qiskrypt_quantum_register.get_qiskit_quantum_register(), QuantumRegister))
            """
            Assertion for the current Qiskrypt's Quantum Register of
            the Qiskrypt's Quantum Circuit has an IBM's Qiskit Quantum Register.
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

            assert(isinstance(qiskrypt_fully_quantum_register.get_qiskit_fully_quantum_register(), QuantumRegister))
            """
            Assertion for the current Qiskrypt's Fully-Quantum Register of
            the Qiskrypt's Quantum Circuit has an IBM's Qiskit Quantum Register.
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

            assert(isinstance(qiskrypt_semi_quantum_register.get_qiskit_semi_quantum_register(), QuantumRegister))
            """
            Assertion for the current Qiskrypt's Semi-Quantum Register of
            the Qiskrypt's Quantum Circuit has an IBM's Qiskit Quantum Register.
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

            assert(isinstance(qiskrypt_ancilla_semi_quantum_register.get_qiskit_ancilla_quantum_register(), AncillaRegister))
            """
            Assertion for the current Qiskrypt's Ancilla Semi-Quantum Register of
            the Qiskrypt's Quantum Circuit has an IBM's Qiskit Ancilla Register.
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

            assert(isinstance(qiskrypt_classical_register.get_qiskit_classical_register(), ClassicalRegister))
            """
            Assertion for the current Qiskrypt's Classical Register of
            the Qiskrypt's Quantum Circuit has an IBM's Qiskit Classical Register.
            """

        assert(qiskrypt_quantum_circuit.get_total_num_qubits() == (quantum_register_num_qubits + fully_quantum_register_num_qubits + semi_quantum_register_num_qubits + ancilla_semi_quantum_register_num_qubits))
        """
        Assertion for the total number of qubits of
        all the Qiskrypt's Quantum, Fully-Quantum, Semi-Quantum and Ancilla Semi-Quantum Registers of the Qiskrypt's Quantum Circuit.
        """

        assert(qiskrypt_quantum_circuit.get_num_qubits_in_qiskit_quantum_register(0) == quantum_register_num_qubits)
        """
        Assertion for the number of qubits of
        the 1st Qiskrypt's Quantum Register of the Qiskrypt's Quantum Circuit.
        """

        assert(qiskrypt_quantum_circuit.get_num_qubits_in_qiskit_quantum_register(1) == fully_quantum_register_num_qubits)
        """
        Assertion for the number of qubits of
        the 2nd Qiskrypt's Fully-Quantum Register of the Qiskrypt's Quantum Circuit.
        """

        assert(qiskrypt_quantum_circuit.get_num_qubits_in_qiskit_quantum_register(2) == semi_quantum_register_num_qubits)
        """
        Assertion for the number of qubits of
        the 3rd Qiskrypt's Semi-Quantum Register of the Qiskrypt's Quantum Circuit.
        """

        assert(qiskrypt_quantum_circuit.get_num_qubits_in_qiskit_quantum_register(3) == ancilla_semi_quantum_register_num_qubits)
        """
        Assertion for the number of qubits of
        the 4th Qiskrypt's Ancilla Semi-Quantum Register of the Qiskrypt's Quantum Circuit.
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

    def test_no_26_creation_qiskrypt_quantum_circuit_with_1_quantum_register_1_qubit_1_fully_quantum_register_1_qubit_1_semi_quantum_register_1_qubit_1_ancilla_quantum_register_1_qubit_1_ancilla_fully_quantum_register_1_qubit_and_1_classical_register_1_bit(self):
        """
        Test Case #26:

        - Create a Qiskrypt's Quantum Circuit with:
             (i) 1 Quantum Register (with 1 qubit).
            (ii) 1 Fully-Quantum Register (with 1 qubit).
           (iii) 1 Semi-Quantum Register (with 1 qubit).
            (iv) 1 Ancilla Quantum Register (with 1 qubit).
             (v) 1 Ancilla Fully-Quantum Register (with 1 qubit).
            (vi) 1 Classical Register (with 1 bit).

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
                                    qiskit_quantum_register=None)
        """
        Create a Qiskrypt's Quantum Register, given its name and number of qubits.
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
                                         qiskit_quantum_register=None)
        """
        Create a Qiskrypt's Fully-Quantum Register, given its name and number of qubits.
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
                                        qiskit_quantum_register=None)
        """
        Create a Qiskrypt's Fully-Quantum Register, given its name and number of qubits.
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
                                                qiskit_ancilla_quantum_register=None)
        """
        Create a Qiskrypt's Ancilla Fully-Quantum Register, given its name and number of qubits.
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

        quantum_circuit_name = "qu_circ"
        """
        Set the name of the Qiskrypt's Quantum Circuit.
        """

        qiskrypt_quantum_circuit = \
            QiskryptQuantumCircuit(name=quantum_circuit_name,
                                   qiskrypt_quantum_registers=[qiskrypt_quantum_register],
                                   qiskrypt_fully_quantum_registers=[qiskrypt_fully_quantum_register],
                                   qiskrypt_semi_quantum_registers=[qiskrypt_semi_quantum_register],
                                   qiskrypt_ancilla_quantum_registers=[qiskrypt_ancilla_quantum_register],
                                   qiskrypt_ancilla_fully_quantum_registers=[qiskrypt_ancilla_fully_quantum_register],
                                   qiskrypt_ancilla_semi_quantum_registers=None,
                                   qiskrypt_classical_registers=[qiskrypt_classical_register],
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

            assert(isinstance(qiskrypt_quantum_register.get_qiskit_quantum_register(), QuantumRegister))
            """
            Assertion for the current Qiskrypt's Quantum Register of
            the Qiskrypt's Quantum Circuit has an IBM's Qiskit Quantum Register.
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

            assert(isinstance(qiskrypt_fully_quantum_register.get_qiskit_fully_quantum_register(), QuantumRegister))
            """
            Assertion for the current Qiskrypt's Fully-Quantum Register of
            the Qiskrypt's Quantum Circuit has an IBM's Qiskit Quantum Register.
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

            assert(isinstance(qiskrypt_semi_quantum_register.get_qiskit_semi_quantum_register(), QuantumRegister))
            """
            Assertion for the current Qiskrypt's Semi-Quantum Register of
            the Qiskrypt's Quantum Circuit has an IBM's Qiskit Quantum Register.
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

            assert(isinstance(qiskrypt_ancilla_quantum_register.get_qiskit_ancilla_quantum_register(), AncillaRegister))
            """
            Assertion for the current Qiskrypt's Ancilla Quantum Register of
            the Qiskrypt's Quantum Circuit has an IBM's Qiskit Ancilla Register.
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

            assert(not isinstance(qiskrypt_ancilla_fully_quantum_register, QiskryptClassicalRegister))
            """
            Assertion for the current Qiskrypt's Ancilla Fully-Quantum Register of
            the Qiskrypt's Quantum Circuit do not be an actual Qiskrypt's Classical Register.
            """

            assert(isinstance(qiskrypt_ancilla_fully_quantum_register.get_qiskit_ancilla_quantum_register(), AncillaRegister))
            """
            Assertion for the current Qiskrypt's Ancilla Fully-Quantum Register of
            the Qiskrypt's Quantum Circuit has an IBM's Qiskit Ancilla Register.
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

            assert(isinstance(qiskrypt_classical_register.get_qiskit_classical_register(), ClassicalRegister))
            """
            Assertion for the current Qiskrypt's Classical Register of
            the Qiskrypt's Quantum Circuit has an IBM's Qiskit Classical Register.
            """

        assert(qiskrypt_quantum_circuit.get_total_num_qubits() == (quantum_register_num_qubits + fully_quantum_register_num_qubits + semi_quantum_register_num_qubits +
                                                                   ancilla_quantum_register_num_qubits + ancilla_fully_quantum_register_num_qubits))
        """
        Assertion for the total number of qubits of
        all the Qiskrypt's Quantum, Fully-Quantum, Semi-Quantum, Ancilla Quantum and Ancilla Fully-Quantum Registers of the Qiskrypt's Quantum Circuit.
        """

        assert(qiskrypt_quantum_circuit.get_num_qubits_in_qiskit_quantum_register(0) == quantum_register_num_qubits)
        """
        Assertion for the number of qubits of
        the 1st Qiskrypt's Quantum Register of the Qiskrypt's Quantum Circuit.
        """

        assert(qiskrypt_quantum_circuit.get_num_qubits_in_qiskit_quantum_register(1) == fully_quantum_register_num_qubits)
        """
        Assertion for the number of qubits of
        the 2nd Qiskrypt's Fully-Quantum Register of the Qiskrypt's Quantum Circuit.
        """

        assert(qiskrypt_quantum_circuit.get_num_qubits_in_qiskit_quantum_register(2) == semi_quantum_register_num_qubits)
        """
        Assertion for the number of qubits of
        the 3rd Qiskrypt's Semi-Quantum Register of the Qiskrypt's Quantum Circuit.
        """

        assert(qiskrypt_quantum_circuit.get_num_qubits_in_qiskit_quantum_register(3) == ancilla_quantum_register_num_qubits)
        """
        Assertion for the number of qubits of
        the 4th Qiskrypt's Ancilla Quantum Register of the Qiskrypt's Quantum Circuit.
        """

        assert(qiskrypt_quantum_circuit.get_num_qubits_in_qiskit_quantum_register(4) == ancilla_fully_quantum_register_num_qubits)
        """
        Assertion for the number of qubits of
        the 5th Qiskrypt's Ancilla Fully-Quantum Register of the Qiskrypt's Quantum Circuit.
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

    def test_no_27_creation_qiskrypt_quantum_circuit_with_1_quantum_register_1_qubit_1_fully_quantum_register_1_qubit_1_semi_quantum_register_1_qubit_1_ancilla_quantum_register_1_qubit_1_ancilla_semi_quantum_register_1_qubit_and_1_classical_register_1_bit(self):
        """
        Test Case #27:

        - Create a Qiskrypt's Quantum Circuit with:
             (i) 1 Quantum Register (with 1 qubit).
            (ii) 1 Fully-Quantum Register (with 1 qubit).
           (iii) 1 Semi-Quantum Register (with 1 qubit).
            (iv) 1 Ancilla Quantum Register (with 1 qubit).
             (v) 1 Ancilla Semi-Quantum Register (with 1 qubit).
            (vi) 1 Classical Register (with 1 bit).

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
                                    qiskit_quantum_register=None)
        """
        Create a Qiskrypt's Quantum Register, given its name and number of qubits.
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
                                         qiskit_quantum_register=None)
        """
        Create a Qiskrypt's Fully-Quantum Register, given its name and number of qubits.
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
                                        qiskit_quantum_register=None)
        """
        Create a Qiskrypt's Fully-Quantum Register, given its name and number of qubits.
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
                                               qiskit_ancilla_quantum_register=None)
        """
        Create a Qiskrypt's Ancilla Semi-Quantum Register, given its name and number of qubits.
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

        quantum_circuit_name = "qu_circ"
        """
        Set the name of the Qiskrypt's Quantum Circuit.
        """

        qiskrypt_quantum_circuit = \
            QiskryptQuantumCircuit(name=quantum_circuit_name,
                                   qiskrypt_quantum_registers=[qiskrypt_quantum_register],
                                   qiskrypt_fully_quantum_registers=[qiskrypt_fully_quantum_register],
                                   qiskrypt_semi_quantum_registers=[qiskrypt_semi_quantum_register],
                                   qiskrypt_ancilla_quantum_registers=[qiskrypt_ancilla_quantum_register],
                                   qiskrypt_ancilla_fully_quantum_registers=None,
                                   qiskrypt_ancilla_semi_quantum_registers=[qiskrypt_ancilla_semi_quantum_register],
                                   qiskrypt_classical_registers=[qiskrypt_classical_register],
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

            assert(isinstance(qiskrypt_quantum_register.get_qiskit_quantum_register(), QuantumRegister))
            """
            Assertion for the current Qiskrypt's Quantum Register of
            the Qiskrypt's Quantum Circuit has an IBM's Qiskit Quantum Register.
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

            assert(isinstance(qiskrypt_fully_quantum_register.get_qiskit_fully_quantum_register(), QuantumRegister))
            """
            Assertion for the current Qiskrypt's Fully-Quantum Register of
            the Qiskrypt's Quantum Circuit has an IBM's Qiskit Quantum Register.
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

            assert(isinstance(qiskrypt_semi_quantum_register.get_qiskit_semi_quantum_register(), QuantumRegister))
            """
            Assertion for the current Qiskrypt's Semi-Quantum Register of
            the Qiskrypt's Quantum Circuit has an IBM's Qiskit Quantum Register.
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

            assert(isinstance(qiskrypt_ancilla_quantum_register.get_qiskit_ancilla_quantum_register(), AncillaRegister))
            """
            Assertion for the current Qiskrypt's Ancilla Quantum Register of
            the Qiskrypt's Quantum Circuit has an IBM's Qiskit Ancilla Register.
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

            assert(isinstance(qiskrypt_ancilla_semi_quantum_register.get_qiskit_ancilla_quantum_register(), AncillaRegister))
            """
            Assertion for the current Qiskrypt's Ancilla Semi-Quantum Register of
            the Qiskrypt's Quantum Circuit has an IBM's Qiskit Ancilla Register.
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

            assert(isinstance(qiskrypt_classical_register.get_qiskit_classical_register(), ClassicalRegister))
            """
            Assertion for the current Qiskrypt's Classical Register of
            the Qiskrypt's Quantum Circuit has an IBM's Qiskit Classical Register.
            """

        assert(qiskrypt_quantum_circuit.get_total_num_qubits() == (quantum_register_num_qubits + fully_quantum_register_num_qubits + semi_quantum_register_num_qubits +
                                                                   ancilla_quantum_register_num_qubits + ancilla_semi_quantum_register_num_qubits))
        """
        Assertion for the total number of qubits of
        all the Qiskrypt's Quantum, Fully-Quantum, Semi-Quantum, Ancilla Quantum and Ancilla Semi-Quantum Registers of the Qiskrypt's Quantum Circuit.
        """

        assert(qiskrypt_quantum_circuit.get_num_qubits_in_qiskit_quantum_register(0) == quantum_register_num_qubits)
        """
        Assertion for the number of qubits of
        the 1st Qiskrypt's Quantum Register of the Qiskrypt's Quantum Circuit.
        """

        assert(qiskrypt_quantum_circuit.get_num_qubits_in_qiskit_quantum_register(1) == fully_quantum_register_num_qubits)
        """
        Assertion for the number of qubits of
        the 2nd Qiskrypt's Fully-Quantum Register of the Qiskrypt's Quantum Circuit.
        """

        assert(qiskrypt_quantum_circuit.get_num_qubits_in_qiskit_quantum_register(2) == semi_quantum_register_num_qubits)
        """
        Assertion for the number of qubits of
        the 3rd Qiskrypt's Semi-Quantum Register of the Qiskrypt's Quantum Circuit.
        """

        assert(qiskrypt_quantum_circuit.get_num_qubits_in_qiskit_quantum_register(3) == ancilla_quantum_register_num_qubits)
        """
        Assertion for the number of qubits of
        the 4th Qiskrypt's Ancilla Quantum Register of the Qiskrypt's Quantum Circuit.
        """

        assert(qiskrypt_quantum_circuit.get_num_qubits_in_qiskit_quantum_register(4) == ancilla_semi_quantum_register_num_qubits)
        """
        Assertion for the number of qubits of
        the 5th Qiskrypt's Ancilla Semi-Quantum Register of the Qiskrypt's Quantum Circuit.
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

    def test_no_28_creation_qiskrypt_quantum_circuit_with_1_quantum_register_1_qubit_1_fully_quantum_register_1_qubit_1_semi_quantum_register_1_qubit_1_ancilla_quantum_register_1_qubit_1_ancilla_fully_quantum_register_1_qubit_1_ancilla_semi_quantum_register_1_qubit_and_1_classical_register_1_bit(self):
        """
        Test Case #28:

        - Create a Qiskrypt's Quantum Circuit with:
             (i) 1 Quantum Register (with 1 qubit).
            (ii) 1 Fully-Quantum Register (with 1 qubit).
           (iii) 1 Semi-Quantum Register (with 1 qubit).
            (iv) 1 Ancilla Quantum Register (with 1 qubit).
             (v) 1 Ancilla Fully-Quantum Register (with 1 qubit).
            (vi) 1 Ancilla Semi-Quantum Register (with 1 qubit).
           (vii) 1 Classical Register (with 1 bit).

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
                                    qiskit_quantum_register=None)
        """
        Create a Qiskrypt's Quantum Register, given its name and number of qubits.
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
                                         qiskit_quantum_register=None)
        """
        Create a Qiskrypt's Fully-Quantum Register, given its name and number of qubits.
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
                                        qiskit_quantum_register=None)
        """
        Create a Qiskrypt's Fully-Quantum Register, given its name and number of qubits.
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
                                                qiskit_ancilla_quantum_register=None)
        """
        Create a Qiskrypt's Ancilla Fully-Quantum Register, given its name and number of qubits.
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
                                               qiskit_ancilla_quantum_register=None)
        """
        Create a Qiskrypt's Ancilla Semi-Quantum Register, given its name and number of qubits.
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

        quantum_circuit_name = "qu_circ"
        """
        Set the name of the Qiskrypt's Quantum Circuit.
        """

        qiskrypt_quantum_circuit = \
            QiskryptQuantumCircuit(name=quantum_circuit_name,
                                   qiskrypt_quantum_registers=[qiskrypt_quantum_register],
                                   qiskrypt_fully_quantum_registers=[qiskrypt_fully_quantum_register],
                                   qiskrypt_semi_quantum_registers=[qiskrypt_semi_quantum_register],
                                   qiskrypt_ancilla_quantum_registers=[qiskrypt_ancilla_quantum_register],
                                   qiskrypt_ancilla_fully_quantum_registers=[qiskrypt_ancilla_fully_quantum_register],
                                   qiskrypt_ancilla_semi_quantum_registers=[qiskrypt_ancilla_semi_quantum_register],
                                   qiskrypt_classical_registers=[qiskrypt_classical_register],
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

            assert(isinstance(qiskrypt_quantum_register.get_qiskit_quantum_register(), QuantumRegister))
            """
            Assertion for the current Qiskrypt's Quantum Register of
            the Qiskrypt's Quantum Circuit has an IBM's Qiskit Quantum Register.
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

            assert(isinstance(qiskrypt_fully_quantum_register.get_qiskit_fully_quantum_register(), QuantumRegister))
            """
            Assertion for the current Qiskrypt's Fully-Quantum Register of
            the Qiskrypt's Quantum Circuit has an IBM's Qiskit Quantum Register.
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

            assert(isinstance(qiskrypt_semi_quantum_register.get_qiskit_semi_quantum_register(), QuantumRegister))
            """
            Assertion for the current Qiskrypt's Semi-Quantum Register of
            the Qiskrypt's Quantum Circuit has an IBM's Qiskit Quantum Register.
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

            assert(isinstance(qiskrypt_ancilla_quantum_register.get_qiskit_ancilla_quantum_register(), AncillaRegister))
            """
            Assertion for the current Qiskrypt's Ancilla Quantum Register of
            the Qiskrypt's Quantum Circuit has an IBM's Qiskit Ancilla Register.
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

            assert(not isinstance(qiskrypt_ancilla_fully_quantum_register, QiskryptClassicalRegister))
            """
            Assertion for the current Qiskrypt's Ancilla Fully-Quantum Register of
            the Qiskrypt's Quantum Circuit do not be an actual Qiskrypt's Classical Register.
            """

            assert(isinstance(qiskrypt_ancilla_fully_quantum_register.get_qiskit_ancilla_quantum_register(), AncillaRegister))
            """
            Assertion for the current Qiskrypt's Ancilla Fully-Quantum Register of
            the Qiskrypt's Quantum Circuit has an IBM's Qiskit Ancilla Register.
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

            assert(isinstance(qiskrypt_ancilla_semi_quantum_register.get_qiskit_ancilla_quantum_register(), AncillaRegister))
            """
            Assertion for the current Qiskrypt's Ancilla Semi-Quantum Register of
            the Qiskrypt's Quantum Circuit has an IBM's Qiskit Ancilla Register.
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

            assert(isinstance(qiskrypt_classical_register.get_qiskit_classical_register(), ClassicalRegister))
            """
            Assertion for the current Qiskrypt's Classical Register of
            the Qiskrypt's Quantum Circuit has an IBM's Qiskit Classical Register.
            """

        assert(qiskrypt_quantum_circuit.get_total_num_qubits() == (quantum_register_num_qubits + fully_quantum_register_num_qubits + semi_quantum_register_num_qubits +
                                                                   ancilla_quantum_register_num_qubits + ancilla_fully_quantum_register_num_qubits + ancilla_semi_quantum_register_num_qubits))
        """
        Assertion for the total number of qubits of
        all the Qiskrypt's Quantum, Fully-Quantum, Semi-Quantum, Ancilla Quantum and Ancilla Semi-Quantum Registers of the Qiskrypt's Quantum Circuit.
        """

        assert(qiskrypt_quantum_circuit.get_num_qubits_in_qiskit_quantum_register(0) == quantum_register_num_qubits)
        """
        Assertion for the number of qubits of
        the 1st Qiskrypt's Quantum Register of the Qiskrypt's Quantum Circuit.
        """

        assert(qiskrypt_quantum_circuit.get_num_qubits_in_qiskit_quantum_register(1) == fully_quantum_register_num_qubits)
        """
        Assertion for the number of qubits of
        the 2nd Qiskrypt's Fully-Quantum Register of the Qiskrypt's Quantum Circuit.
        """

        assert(qiskrypt_quantum_circuit.get_num_qubits_in_qiskit_quantum_register(2) == semi_quantum_register_num_qubits)
        """
        Assertion for the number of qubits of
        the 3rd Qiskrypt's Semi-Quantum Register of the Qiskrypt's Quantum Circuit.
        """

        assert(qiskrypt_quantum_circuit.get_num_qubits_in_qiskit_quantum_register(3) == ancilla_quantum_register_num_qubits)
        """
        Assertion for the number of qubits of
        the 4th Qiskrypt's Ancilla Quantum Register of the Qiskrypt's Quantum Circuit.
        """

        assert(qiskrypt_quantum_circuit.get_num_qubits_in_qiskit_quantum_register(4) == ancilla_fully_quantum_register_num_qubits)
        """
        Assertion for the number of qubits of
        the 5th Qiskrypt's Ancilla Fully-Quantum Register of the Qiskrypt's Quantum Circuit.
        """

        assert(qiskrypt_quantum_circuit.get_num_qubits_in_qiskit_quantum_register(5) == ancilla_semi_quantum_register_num_qubits)
        """
        Assertion for the number of qubits of
        the 6th Qiskrypt's Ancilla Semi-Quantum Register of the Qiskrypt's Quantum Circuit.
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


class OtherBasicAndFundamentalMethodsOfQiskryptQuantumCircuitTests(TestCase):
    """
    Object Class of the Unitary Tests for other basic and fundamental methods of a Qiskrypt's Quantum Circuit.
    """

    def test_no_1_revert_qiskit_quantum_circuit_operations(self):
        """
        Test Case #1:

        - Revert the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit.

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        """
        Dummy Assert Equal for the Unittest
        """
        self.assertEqual(True, True)

    def test_no_2_revert_qiskit_quantum_circuit_wires_order(self):
        """
        Test Case #2:

        - Revert the order of the wires of the IBM Qiskit's Quantum Circuit of
          the Qiskrypt's Quantum Circuit.

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        """
        Dummy Assert Equal for the Unittest
        """
        self.assertEqual(True, True)

    def test_no_3_invert_qiskit_quantum_circuit(self):
        """
        Test Case #3:

        - Invert the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit,
          reverting the order of the Quantum Gates/Operations and
          setting the symmetric values for their parameters.

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        """
        Dummy Assert Equal for the Unittest
        """
        self.assertEqual(True, True)


class PrepareAndMeasureQubitInQiskryptQuantumCircuitTests(TestCase):
    """
    Object Class of the Unitary Tests for Prepare (and Measure) a qubit in a Qiskrypt's Quantum Circuit.
    """

    def test_no_1_prepare_measure_x_basis_1_qubit(self):
        """
        Test Case #1:

        - Prepare (and Measure) a qubit in the IBM Qiskit's Quantum Circuit of
          the Qiskrypt's Quantum Circuit, in the X-Basis (Diagonal Basis).

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Quantum Circuit is created with a Qiskrypt's Quantum Register,
           with 1 qubit initialized in the state |0⟩;
        2) The 1st qubit is prepared (and measured) in the X-Basis (Diagonal Basis), such that, |0⟩ ↦ |+⟩;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        num_qubits = num_bits = 1
        """
        Set the number of qubits and bits,
        for the Qiskrypt's Quantum and Classical Registers, respectively.
        """

        qiskrypt_quantum_register_prepare_and_measure_in_x_basis_1_qubit = \
            QiskryptQuantumRegister("qu_reg_1", num_qubits)
        """
        Create a Qiskrypt's Quantum Register with 1 qubit.
        """

        qiskrypt_classical_register_prepare_and_measure_in_x_basis_1_qubit = \
            QiskryptClassicalRegister("cl_reg_1", num_bits)
        """
        Create a Qiskrypt's Classical Register with 1 bit.
        """

        qiskrypt_quantum_circuit_prepare_and_measure_in_x_basis_1_qubit = \
            QiskryptQuantumCircuit("qu_circ_1",
                                   qiskrypt_quantum_registers=[qiskrypt_quantum_register_prepare_and_measure_in_x_basis_1_qubit],
                                   qiskrypt_fully_quantum_registers=None,
                                   qiskrypt_semi_quantum_registers=None,
                                   qiskrypt_ancilla_quantum_registers=None,
                                   qiskrypt_ancilla_fully_quantum_registers=None,
                                   qiskrypt_ancilla_semi_quantum_registers=None,
                                   qiskrypt_classical_registers=[qiskrypt_classical_register_prepare_and_measure_in_x_basis_1_qubit],
                                   global_phase=0, qiskit_quantum_circuit=None)
        """
        Create a Qiskrypt's Quantum Circuit with
        the previously created Qiskrypt's Quantum and Classical Registers.
        """

        qiskrypt_quantum_circuit_prepare_and_measure_in_x_basis_1_qubit \
            .prepare_and_measure_single_qubit_in_qiskit_quantum_register_in_x_basis(0, 0, 0, 0,
                                                                                    is_final_measurement=False)
        """
        Prepare (not Measuring) the given index for the single qubit of
        the given IBM Qiskit's Quantum Register, in the X-Basis (Diagonal Basis).
        """

        qiskit_state_vector_backend = Aer.get_backend("statevector_simulator")
        """
        Getting the Aer Simulator Backend for the State Vector Representation
        (i.e., the quantum state represented as its state vector).
        """

        final_quantum_state_vector_state = \
            execute(qiskrypt_quantum_circuit_prepare_and_measure_in_x_basis_1_qubit.qiskit_quantum_circuit,
                    qiskit_state_vector_backend).result().get_statevector()
        """
        Execute the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit
        and store the resulted quantum state represented in a final state vector.
        """

        assert_allclose(final_quantum_state_vector_state,
                        array([((1. / sqrt(2.)) + 0.j), ((1. / sqrt(2.)) + 0.j)]),
                        rtol=1e-7, atol=1e-7)
        """
        Perform the Assertion of all close values in the values of the quantum state,
        represented by its state vector describing the given qubit,
        after being prepared (not measured) in the X-Basis (Diagonal Basis), such that, |0⟩ ↦ |+⟩.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_2_prepare_measure_x_basis_1_qubit(self):
        """
        Test Case #2:

        - Prepare (and Measure) a qubit in the IBM Qiskit's Quantum Circuit of
          the Qiskrypt's Quantum Circuit, in the X-Basis (Diagonal Basis).

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Quantum Circuit is created with a Qiskrypt's Quantum Register,
           with 1 qubit initialized in the state |0⟩;
        2) It is applied the Pauli-X (Bit Flip/NOT) Gate/Operation to the 1st qubit, such that, |0⟩ ↦ |1⟩;
        3) The 1st qubit is prepared (and measured) in the X-Basis (Diagonal Basis), such that, |1⟩ ↦ |-⟩;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        num_qubits = num_bits = 1
        """
        Set the number of qubits and bits,
        for the Qiskrypt's Quantum and Classical Registers, respectively.
        """

        qiskrypt_quantum_register_prepare_and_measure_in_x_basis_1_qubit = \
            QiskryptQuantumRegister("qu_reg_2", num_qubits)
        """
        Create a Qiskrypt's Quantum Register with 1 qubit.
        """

        qiskrypt_classical_register_prepare_and_measure_in_x_basis_1_qubit = \
            QiskryptClassicalRegister("cl_reg_2", num_bits)
        """
        Create a Qiskrypt's Classical Register with 1 bit.
        """

        qiskrypt_quantum_circuit_prepare_and_measure_in_x_basis_1_qubit = \
            QiskryptQuantumCircuit("qu_circ_2",
                                   qiskrypt_quantum_registers=[qiskrypt_quantum_register_prepare_and_measure_in_x_basis_1_qubit],
                                   qiskrypt_fully_quantum_registers=None,
                                   qiskrypt_semi_quantum_registers=None,
                                   qiskrypt_ancilla_quantum_registers=None,
                                   qiskrypt_ancilla_fully_quantum_registers=None,
                                   qiskrypt_ancilla_semi_quantum_registers=None,
                                   qiskrypt_classical_registers=[qiskrypt_classical_register_prepare_and_measure_in_x_basis_1_qubit],
                                   global_phase=0, qiskit_quantum_circuit=None)
        """
        Create a Qiskrypt's Quantum Circuit with
        the previously created Qiskrypt's Quantum and Classical Registers.
        """

        qiskrypt_quantum_circuit_prepare_and_measure_in_x_basis_1_qubit \
            .apply_pauli_x(0, 0)
        """
        Apply the Pauli-X (Bit Flip/NOT) Gate/Operation to the given index for
        the single qubit of the given IBM Qiskit's Quantum Register (|0⟩ ↦ |1⟩).
        """

        qiskrypt_quantum_circuit_prepare_and_measure_in_x_basis_1_qubit \
            .prepare_and_measure_single_qubit_in_qiskit_quantum_register_in_x_basis(0, 0, 0, 0,
                                                                                    is_final_measurement=False)
        """
        Prepare (not Measuring) the given index for the single qubit of
        the given IBM Qiskit's Quantum Register, in the X-Basis (Diagonal Basis).
        """

        qiskit_state_vector_backend = Aer.get_backend("statevector_simulator")
        """
        Getting the Aer Simulator Backend for the State Vector Representation
        (i.e., the quantum state represented as its state vector).
        """

        final_quantum_state_vector_state = \
            execute(qiskrypt_quantum_circuit_prepare_and_measure_in_x_basis_1_qubit.qiskit_quantum_circuit,
                    qiskit_state_vector_backend).result().get_statevector()
        """
        Execute the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit
        and store the resulted quantum state represented in a final state vector.
        """

        assert_allclose(final_quantum_state_vector_state,
                        array([((1. / sqrt(2.)) + 0.j), (-(1. / sqrt(2.)) + 0.j)]),
                        rtol=1e-7, atol=1e-7)
        """
        Perform the Assertion of all close values in the values of the quantum state,
        represented by its state vector describing the given qubit,
        after being prepared (not measured) in the X-Basis (Diagonal Basis), such that, |1⟩ ↦ |-⟩.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_3_prepare_measure_x_basis_1_qubit(self):
        """
        Test Case #3:

        - Prepare (and Measure) a qubit in the IBM Qiskit's Quantum Circuit of
          the Qiskrypt's Quantum Circuit, in the X-Basis (Diagonal Basis).

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Quantum Circuit is created with a Qiskrypt's Quantum Register,
           with 1 qubit initialized in the state |0⟩;
        2) It is applied the Hadamard Gate/Operation to the 1st qubit, such that, |0⟩ ↦ |+⟩;
        3) The 1st qubit is prepared (and measured) in the X-Basis (Diagonal Basis), such that, |+⟩ ↦ |0⟩;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        num_qubits = num_bits = 1
        """
        Set the number of qubits and bits,
        for the Qiskrypt's Quantum and Classical Registers, respectively.
        """

        qiskrypt_quantum_register_prepare_and_measure_in_x_basis_1_qubit = \
            QiskryptQuantumRegister("qu_reg_3", num_qubits)
        """
        Create a Qiskrypt's Quantum Register with 1 qubit.
        """

        qiskrypt_classical_register_prepare_and_measure_in_x_basis_1_qubit = \
            QiskryptClassicalRegister("cl_reg_3", num_bits)
        """
        Create a Qiskrypt's Classical Register with 1 bit.
        """

        qiskrypt_quantum_circuit_prepare_and_measure_in_x_basis_1_qubit = \
            QiskryptQuantumCircuit("qu_circ_3",
                                   qiskrypt_quantum_registers=[qiskrypt_quantum_register_prepare_and_measure_in_x_basis_1_qubit],
                                   qiskrypt_fully_quantum_registers=None,
                                   qiskrypt_semi_quantum_registers=None,
                                   qiskrypt_ancilla_quantum_registers=None,
                                   qiskrypt_ancilla_fully_quantum_registers=None,
                                   qiskrypt_ancilla_semi_quantum_registers=None,
                                   qiskrypt_classical_registers=[qiskrypt_classical_register_prepare_and_measure_in_x_basis_1_qubit],
                                   global_phase=0, qiskit_quantum_circuit=None)
        """
        Create a Qiskrypt's Quantum Circuit with
        the previously created Qiskrypt's Quantum and Classical Registers.
        """

        qiskrypt_quantum_circuit_prepare_and_measure_in_x_basis_1_qubit \
            .apply_hadamard(0, 0)
        """
        Apply the Hadamard Gate/Operation to the given index for
        the single qubit of the given IBM Qiskit's Quantum Register (|0⟩ ↦ |+⟩).
        """

        qiskrypt_quantum_circuit_prepare_and_measure_in_x_basis_1_qubit \
            .prepare_and_measure_single_qubit_in_qiskit_quantum_register_in_x_basis(0, 0, 0, 0,
                                                                                    is_final_measurement=False)
        """
        Prepare (not Measuring) the given index for the single qubit of
        the given IBM Qiskit's Quantum Register, in the X-Basis (Diagonal Basis).
        """

        qiskit_state_vector_backend = Aer.get_backend("statevector_simulator")
        """
        Getting the Aer Simulator Backend for the State Vector Representation
        (i.e., the quantum state represented as its state vector).
        """

        final_quantum_state_vector_state = \
            execute(qiskrypt_quantum_circuit_prepare_and_measure_in_x_basis_1_qubit.qiskit_quantum_circuit,
                    qiskit_state_vector_backend).result().get_statevector()
        """
        Execute the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit
        and store the resulted quantum state represented in a final state vector.
        """

        assert_allclose(final_quantum_state_vector_state,
                        array([(1. + 0.j), (0. + 0.j)]),
                        rtol=1e-7, atol=1e-7)
        """
        Perform the Assertion of all close values in the values of the quantum state,
        represented by its state vector describing the given qubit,
        after being prepared (not measured) in the X-Basis (Diagonal Basis), such that, |+⟩ ↦ |0⟩.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_4_prepare_measure_x_basis_1_qubit(self):
        """
        Test Case #4:

        - Prepare (and Measure) a qubit in the IBM Qiskit's Quantum Circuit of
          the Qiskrypt's Quantum Circuit, in the X-Basis (Diagonal Basis).

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Quantum Circuit is created with a Qiskrypt's Quantum Register,
           with 1 qubit initialized in the state |0⟩;
        2) It is applied the Pauli-X (Bit Flip/NOT) Gate/Operation to the 1st qubit, such that, |0⟩ ↦ |1⟩;
        3) It is applied the Hadamard Gate/Operation to the 1st qubit, such that, |1⟩ ↦ |-⟩;
        4) The 1st qubit is prepared (and measured) in the X-Basis (Diagonal Basis), such that, |-⟩ ↦ |1⟩;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        num_qubits = num_bits = 1
        """
        Set the number of qubits and bits,
        for the Qiskrypt's Quantum and Classical Registers, respectively.
        """

        qiskrypt_quantum_register_prepare_and_measure_in_x_basis_1_qubit = \
            QiskryptQuantumRegister("qu_reg_4", num_qubits)
        """
        Create a Qiskrypt's Quantum Register with 1 qubit.
        """

        qiskrypt_classical_register_prepare_and_measure_in_x_basis_1_qubit = \
            QiskryptClassicalRegister("cl_reg_4", num_bits)
        """
        Create a Qiskrypt's Classical Register with 1 bit.
        """

        qiskrypt_quantum_circuit_prepare_and_measure_in_x_basis_1_qubit = \
            QiskryptQuantumCircuit("qu_circ_4",
                                   qiskrypt_quantum_registers=[qiskrypt_quantum_register_prepare_and_measure_in_x_basis_1_qubit],
                                   qiskrypt_fully_quantum_registers=None,
                                   qiskrypt_semi_quantum_registers=None,
                                   qiskrypt_ancilla_quantum_registers=None,
                                   qiskrypt_ancilla_fully_quantum_registers=None,
                                   qiskrypt_ancilla_semi_quantum_registers=None,
                                   qiskrypt_classical_registers=[qiskrypt_classical_register_prepare_and_measure_in_x_basis_1_qubit],
                                   global_phase=0, qiskit_quantum_circuit=None)
        """
        Create a Qiskrypt's Quantum Circuit with
        the previously created Qiskrypt's Quantum and Classical Registers.
        """

        qiskrypt_quantum_circuit_prepare_and_measure_in_x_basis_1_qubit \
            .apply_pauli_x(0, 0)
        """
        Apply the Pauli-X (Bit Flip/NOT) Gate/Operation to the given index for
        the single qubit of the given IBM Qiskit's Quantum Register (|0⟩ ↦ |1⟩).
        """

        qiskrypt_quantum_circuit_prepare_and_measure_in_x_basis_1_qubit \
            .apply_hadamard(0, 0)
        """
        Apply the Hadamard Gate/Operation to the given index for
        the single qubit of the given IBM Qiskit's Quantum Register (|1⟩ ↦ |-⟩).
        """

        qiskrypt_quantum_circuit_prepare_and_measure_in_x_basis_1_qubit \
            .prepare_and_measure_single_qubit_in_qiskit_quantum_register_in_x_basis(0, 0, 0, 0,
                                                                                    is_final_measurement=False)
        """
        Prepare (not Measuring) the given index for the single qubit of
        the given IBM Qiskit's Quantum Register, in the X-Basis (Diagonal Basis).
        """

        qiskit_state_vector_backend = Aer.get_backend("statevector_simulator")
        """
        Getting the Aer Simulator Backend for the State Vector Representation
        (i.e., the quantum state represented as its state vector).
        """

        final_quantum_state_vector_state = \
            execute(qiskrypt_quantum_circuit_prepare_and_measure_in_x_basis_1_qubit.qiskit_quantum_circuit,
                    qiskit_state_vector_backend).result().get_statevector()
        """
        Execute the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit
        and store the resulted quantum state represented in a final state vector.
        """

        assert_allclose(final_quantum_state_vector_state,
                        array([(0. + 0.j), (1. + 0.j)]),
                        rtol=1e-7, atol=1e-7)
        """
        Perform the Assertion of all close values in the values of the quantum state,
        represented by its state vector describing the given qubit,
        after being prepared (not measured) in the X-Basis (Diagonal Basis), such that, |-⟩ ↦ |1⟩.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_5_prepare_measure_y_basis_1_qubit(self):
        """
        Test Case #5:

        - Prepare (and Measure) a qubit in the IBM Qiskit's Quantum Circuit of
          the Qiskrypt's Quantum Circuit, in the Y-Basis (Diagonal Basis).

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Quantum Circuit is created with a Qiskrypt's Quantum Register,
           with 1 qubit initialized in the state |0⟩;
        2) The 1st qubit is prepared (and measured) in the Y-Basis (Diagonal Basis), such that, |0⟩ ↦ |+i⟩;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        num_qubits = num_bits = 1
        """
        Set the number of qubits and bits,
        for the Qiskrypt's Quantum and Classical Registers, respectively.
        """

        qiskrypt_quantum_register_prepare_and_measure_in_y_basis_1_qubit = \
            QiskryptQuantumRegister("qu_reg_5", num_qubits)
        """
        Create a Qiskrypt's Quantum Register with 1 qubit.
        """

        qiskrypt_classical_register_prepare_and_measure_in_y_basis_1_qubit = \
            QiskryptClassicalRegister("cl_reg_5", num_bits)
        """
        Create a Qiskrypt's Classical Register with 1 bit.
        """

        qiskrypt_quantum_circuit_prepare_and_measure_in_y_basis_1_qubit = \
            QiskryptQuantumCircuit("qu_circ_5",
                                   qiskrypt_quantum_registers=[qiskrypt_quantum_register_prepare_and_measure_in_y_basis_1_qubit],
                                   qiskrypt_fully_quantum_registers=None,
                                   qiskrypt_semi_quantum_registers=None,
                                   qiskrypt_ancilla_quantum_registers=None,
                                   qiskrypt_ancilla_fully_quantum_registers=None,
                                   qiskrypt_ancilla_semi_quantum_registers=None,
                                   qiskrypt_classical_registers=[qiskrypt_classical_register_prepare_and_measure_in_y_basis_1_qubit],
                                   global_phase=0, qiskit_quantum_circuit=None)
        """
        Create a Qiskrypt's Quantum Circuit with
        the previously created Qiskrypt's Quantum and Classical Registers.
        """

        qiskrypt_quantum_circuit_prepare_and_measure_in_y_basis_1_qubit \
            .prepare_and_measure_single_qubit_in_qiskit_quantum_register_in_y_basis(0, 0, 0, 0,
                                                                                    is_final_measurement=False)
        """
        Prepare (not Measuring) the given index for the single qubit of
        the given IBM Qiskit's Quantum Register, in the Y-Basis (Diagonal Basis).
        """

        qiskit_state_vector_backend = Aer.get_backend("statevector_simulator")
        """
        Getting the Aer Simulator Backend for the State Vector Representation
        (i.e., the quantum state represented as its state vector).
        """

        final_quantum_state_vector_state = \
            execute(qiskrypt_quantum_circuit_prepare_and_measure_in_y_basis_1_qubit.qiskit_quantum_circuit,
                    qiskit_state_vector_backend).result().get_statevector()
        """
        Execute the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit
        and store the resulted quantum state represented in a final state vector.
        """

        assert_allclose(final_quantum_state_vector_state,
                        array([((1. / sqrt(2.)) + 0.j), (1. / sqrt(2.)) * (0. + 1.j)]),
                        rtol=1e-7, atol=1e-7)
        """
        Perform the Assertion of all close values in the values of the quantum state,
        represented by its state vector describing the given qubit,
        after being prepared (not measured) in the Y-Basis (Diagonal Basis), such that, |0⟩ ↦ |+i⟩.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_6_prepare_measure_y_basis_1_qubit(self):
        """
        Test Case #6:

        - Prepare (and Measure) a qubit in the IBM Qiskit's Quantum Circuit of
          the Qiskrypt's Quantum Circuit, in the Y-Basis (Diagonal Basis).

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Quantum Circuit is created with a Qiskrypt's Quantum Register,
           with 1 qubit initialized in the state |0⟩;
        2) It is applied the Pauli-X (Bit Flip/NOT) Gate/Operation to the 1st qubit, such that, |0⟩ ↦ |1⟩;
        3) The 1st qubit is prepared (and measured) in the Y-Basis (Diagonal Basis), such that, |1⟩ ↦ |-i⟩;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        num_qubits = num_bits = 1
        """
        Set the number of qubits and bits,
        for the Qiskrypt's Quantum and Classical Registers, respectively.
        """

        qiskrypt_quantum_register_prepare_and_measure_in_y_basis_1_qubit = \
            QiskryptQuantumRegister("qu_reg_6", num_qubits)
        """
        Create a Qiskrypt's Quantum Register with 1 qubit.
        """

        qiskrypt_classical_register_prepare_and_measure_in_y_basis_1_qubit = \
            QiskryptClassicalRegister("cl_reg_6", num_bits)
        """
        Create a Qiskrypt's Classical Register with 1 bit.
        """

        qiskrypt_quantum_circuit_prepare_and_measure_in_y_basis_1_qubit = \
            QiskryptQuantumCircuit("qu_circ_6",
                                   qiskrypt_quantum_registers=[qiskrypt_quantum_register_prepare_and_measure_in_y_basis_1_qubit],
                                   qiskrypt_fully_quantum_registers=None,
                                   qiskrypt_semi_quantum_registers=None,
                                   qiskrypt_ancilla_quantum_registers=None,
                                   qiskrypt_ancilla_fully_quantum_registers=None,
                                   qiskrypt_ancilla_semi_quantum_registers=None,
                                   qiskrypt_classical_registers=[qiskrypt_classical_register_prepare_and_measure_in_y_basis_1_qubit],
                                   global_phase=0, qiskit_quantum_circuit=None)
        """
        Create a Qiskrypt's Quantum Circuit with
        the previously created Qiskrypt's Quantum and Classical Registers.
        """

        qiskrypt_quantum_circuit_prepare_and_measure_in_y_basis_1_qubit \
            .apply_pauli_x(0, 0)
        """
        Apply the Pauli-X (Bit Flip/NOT) Gate/Operation to the given index for
        the single qubit of the given IBM Qiskit's Quantum Register (|0⟩ ↦ |1⟩).
        """

        qiskrypt_quantum_circuit_prepare_and_measure_in_y_basis_1_qubit \
            .prepare_and_measure_single_qubit_in_qiskit_quantum_register_in_y_basis(0, 0, 0, 0,
                                                                                    is_final_measurement=False)
        """
        Prepare (not Measuring) the given index for the single qubit of
        the given IBM Qiskit's Quantum Register, in the Y-Basis (Diagonal Basis).
        """

        qiskit_state_vector_backend = Aer.get_backend("statevector_simulator")
        """
        Getting the Aer Simulator Backend for the State Vector Representation
        (i.e., the quantum state represented as its state vector).
        """

        final_quantum_state_vector_state = \
            execute(qiskrypt_quantum_circuit_prepare_and_measure_in_y_basis_1_qubit.qiskit_quantum_circuit,
                    qiskit_state_vector_backend).result().get_statevector()
        """
        Execute the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit
        and store the resulted quantum state represented in a final state vector.
        """

        assert_allclose(final_quantum_state_vector_state,
                        array([((1. / sqrt(2.)) + 0.j), -(1. / sqrt(2.)) * (0. + 1.j)]),
                        rtol=1e-7, atol=1e-7)
        """
        Perform the Assertion of all close values in the values of the quantum state,
        represented by its state vector describing the given qubit,
        after being prepared (not measured) in the Y-Basis (Diagonal Basis), such that, |1⟩ ↦ |-i⟩.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_7_prepare_measure_y_basis_1_qubit(self):
        """
        Test Case #7:

        - Prepare (and Measure) a qubit in the IBM Qiskit's Quantum Circuit of
          the Qiskrypt's Quantum Circuit, in the Y-Basis (Diagonal Basis).

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Quantum Circuit is created with a Qiskrypt's Quantum Register,
           with 1 qubit initialized in the state |0⟩;
        2) It is applied the Hadamard Gate/Operation to the 1st qubit, such that, |0⟩ ↦ |+⟩;
        3) The 1st qubit is prepared (and measured) in the Y-Basis (Diagonal Basis), such that, |+⟩ ↦ |0⟩;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        num_qubits = num_bits = 1
        """
        Set the number of qubits and bits,
        for the Qiskrypt's Quantum and Classical Registers, respectively.
        """

        qiskrypt_quantum_register_prepare_and_measure_in_y_basis_1_qubit = \
            QiskryptQuantumRegister("qu_reg_7", num_qubits)
        """
        Create a Qiskrypt's Quantum Register with 1 qubit.
        """

        qiskrypt_classical_register_prepare_and_measure_in_y_basis_1_qubit = \
            QiskryptClassicalRegister("cl_reg_7", num_bits)
        """
        Create a Qiskrypt's Classical Register with 1 bit.
        """

        qiskrypt_quantum_circuit_prepare_and_measure_in_y_basis_1_qubit = \
            QiskryptQuantumCircuit("qu_circ_7",
                                   qiskrypt_quantum_registers=[qiskrypt_quantum_register_prepare_and_measure_in_y_basis_1_qubit],
                                   qiskrypt_fully_quantum_registers=None,
                                   qiskrypt_semi_quantum_registers=None,
                                   qiskrypt_ancilla_quantum_registers=None,
                                   qiskrypt_ancilla_fully_quantum_registers=None,
                                   qiskrypt_ancilla_semi_quantum_registers=None,
                                   qiskrypt_classical_registers=[qiskrypt_classical_register_prepare_and_measure_in_y_basis_1_qubit],
                                   global_phase=0, qiskit_quantum_circuit=None)
        """
        Create a Qiskrypt's Quantum Circuit with
        the previously created Qiskrypt's Quantum and Classical Registers.
        """

        qiskrypt_quantum_circuit_prepare_and_measure_in_y_basis_1_qubit \
            .apply_hadamard(0, 0)
        """
        Apply the Hadamard Gate/Operation to the given index for
        the single qubit of the given IBM Qiskit's Quantum Register (|0⟩ ↦ |+⟩).
        """

        qiskrypt_quantum_circuit_prepare_and_measure_in_y_basis_1_qubit \
            .prepare_and_measure_single_qubit_in_qiskit_quantum_register_in_y_basis(0, 0, 0, 0,
                                                                                    is_final_measurement=False)
        """
        Prepare (not Measuring) the given index for the single qubit of
        the given IBM Qiskit's Quantum Register, in the Y-Basis (Diagonal Basis).
        """

        qiskit_state_vector_backend = Aer.get_backend("statevector_simulator")
        """
        Getting the Aer Simulator Backend for the State Vector Representation
        (i.e., the quantum state represented as its state vector).
        """

        final_quantum_state_vector_state = \
            execute(qiskrypt_quantum_circuit_prepare_and_measure_in_y_basis_1_qubit.qiskit_quantum_circuit,
                    qiskit_state_vector_backend).result().get_statevector()
        """
        Execute the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit
        and store the resulted quantum state represented in a final state vector.
        """

        assert_allclose(final_quantum_state_vector_state,
                        array([(1. + 0.j), (0. + 0.j)]),
                        rtol=1e-7, atol=1e-7)
        """
        Perform the Assertion of all close values in the values of the quantum state,
        represented by its state vector describing the given qubit,
        after being prepared (not measured) in the Y-Basis (Diagonal Basis), such that, |+⟩ ↦ |0⟩.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_8_prepare_measure_y_basis_1_qubit(self):
        """
        Test Case #8:

        - Prepare (and Measure) a qubit in the IBM Qiskit's Quantum Circuit of
          the Qiskrypt's Quantum Circuit, in the Y-Basis (Diagonal Basis).

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Quantum Circuit is created with a Qiskrypt's Quantum Register,
           with 1 qubit initialized in the state |0⟩;
        2) It is applied the Pauli-X (Bit Flip/NOT) Gate/Operation to the 1st qubit, such that, |0⟩ ↦ |1⟩;
        3) It is applied the Hadamard Gate/Operation to the 1st qubit, such that, |1⟩ ↦ |-⟩;
        4) The 1st qubit is prepared (and measured) in the Y-Basis (Diagonal Basis), such that, |-⟩ ↦ |1⟩;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        num_qubits = num_bits = 1
        """
        Set the number of qubits and bits,
        for the Qiskrypt's Quantum and Classical Registers, respectively.
        """

        qiskrypt_quantum_register_prepare_and_measure_in_y_basis_1_qubit = \
            QiskryptQuantumRegister("qu_reg_8", num_qubits)
        """
        Create a Qiskrypt's Quantum Register with 1 qubit.
        """

        qiskrypt_classical_register_prepare_and_measure_in_y_basis_1_qubit = \
            QiskryptClassicalRegister("cl_reg_8", num_bits)
        """
        Create a Qiskrypt's Classical Register with 1 bit.
        """

        qiskrypt_quantum_circuit_prepare_and_measure_in_y_basis_1_qubit = \
            QiskryptQuantumCircuit("qu_circ_8",
                                   qiskrypt_quantum_registers=[qiskrypt_quantum_register_prepare_and_measure_in_y_basis_1_qubit],
                                   qiskrypt_fully_quantum_registers=None,
                                   qiskrypt_semi_quantum_registers=None,
                                   qiskrypt_ancilla_quantum_registers=None,
                                   qiskrypt_ancilla_fully_quantum_registers=None,
                                   qiskrypt_ancilla_semi_quantum_registers=None,
                                   qiskrypt_classical_registers=[qiskrypt_classical_register_prepare_and_measure_in_y_basis_1_qubit],
                                   global_phase=0, qiskit_quantum_circuit=None)
        """
        Create a Qiskrypt's Quantum Circuit with
        the previously created Qiskrypt's Quantum and Classical Registers.
        """

        qiskrypt_quantum_circuit_prepare_and_measure_in_y_basis_1_qubit \
            .apply_pauli_x(0, 0)
        """
        Apply the Pauli-X (Bit Flip/NOT) Gate/Operation to the given index for
        the single qubit of the given IBM Qiskit's Quantum Register (|0⟩ ↦ |1⟩).
        """

        qiskrypt_quantum_circuit_prepare_and_measure_in_y_basis_1_qubit \
            .apply_hadamard(0, 0)
        """
        Apply the Hadamard Gate/Operation to the given index for
        the single qubit of the given IBM Qiskit's Quantum Register (|1⟩ ↦ |-⟩).
        """

        qiskrypt_quantum_circuit_prepare_and_measure_in_y_basis_1_qubit \
            .prepare_and_measure_single_qubit_in_qiskit_quantum_register_in_y_basis(0, 0, 0, 0,
                                                                                    is_final_measurement=False)
        """
        Prepare (not Measuring) the given index for the single qubit of
        the given IBM Qiskit's Quantum Register, in the Y-Basis (Diagonal Basis).
        """

        qiskit_state_vector_backend = Aer.get_backend("statevector_simulator")
        """
        Getting the Aer Simulator Backend for the State Vector Representation
        (i.e., the quantum state represented as its state vector).
        """

        final_quantum_state_vector_state = \
            execute(qiskrypt_quantum_circuit_prepare_and_measure_in_y_basis_1_qubit.qiskit_quantum_circuit,
                    qiskit_state_vector_backend).result().get_statevector()
        """
        Execute the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit
        and store the resulted quantum state represented in a final state vector.
        """

        assert_allclose(final_quantum_state_vector_state,
                        array([(0. + 0.j), (0. + 1.j)]),
                        rtol=1e-7, atol=1e-7)
        """
        Perform the Assertion of all close values in the values of the quantum state,
        represented by its state vector describing the given qubit,
        after being prepared (not measured) in the Y-Basis (Diagonal Basis), such that, |-⟩ ↦ i|1⟩.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_9_prepare_measure_y_basis_1_qubit(self):
        """
        Test Case #9:

        - Prepare (and Measure) a qubit in the IBM Qiskit's Quantum Circuit of
          the Qiskrypt's Quantum Circuit, in the Z-Basis (Computational Basis).

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Quantum Circuit is created with a Qiskrypt's Quantum Register,
           with 1 qubit initialized in the state |0⟩;
        2) The 1st qubit is prepared (and measured) in the Z-Basis (Computational Basis), such that, |0⟩ ↦ |0⟩;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        num_qubits = num_bits = 1
        """
        Set the number of qubits and bits,
        for the Qiskrypt's Quantum and Classical Registers, respectively.
        """

        qiskrypt_quantum_register_prepare_and_measure_in_z_basis_1_qubit = \
            QiskryptQuantumRegister("qu_reg_9", num_qubits)
        """
        Create a Qiskrypt's Quantum Register with 1 qubit.
        """

        qiskrypt_classical_register_prepare_and_measure_in_z_basis_1_qubit = \
            QiskryptClassicalRegister("cl_reg_9", num_bits)
        """
        Create a Qiskrypt's Classical Register with 1 bit.
        """

        qiskrypt_quantum_circuit_prepare_and_measure_in_z_basis_1_qubit = \
            QiskryptQuantumCircuit("qu_circ_9",
                                   qiskrypt_quantum_registers=[qiskrypt_quantum_register_prepare_and_measure_in_z_basis_1_qubit],
                                   qiskrypt_fully_quantum_registers=None,
                                   qiskrypt_semi_quantum_registers=None,
                                   qiskrypt_ancilla_quantum_registers=None,
                                   qiskrypt_ancilla_fully_quantum_registers=None,
                                   qiskrypt_ancilla_semi_quantum_registers=None,
                                   qiskrypt_classical_registers=[qiskrypt_classical_register_prepare_and_measure_in_z_basis_1_qubit],
                                   global_phase=0, qiskit_quantum_circuit=None)
        """
        Create a Qiskrypt's Quantum Circuit with
        the previously created Qiskrypt's Quantum and Classical Registers.
        """

        qiskrypt_quantum_circuit_prepare_and_measure_in_z_basis_1_qubit \
            .prepare_and_measure_single_qubit_in_qiskit_quantum_register_in_z_basis(0, 0, 0, 0,
                                                                                    is_final_measurement=False)
        """
        Prepare (not Measuring) the given index for the single qubit of
        the given IBM Qiskit's Quantum Register, in the Z-Basis (Computational Basis).
        """

        qiskit_state_vector_backend = Aer.get_backend("statevector_simulator")
        """
        Getting the Aer Simulator Backend for the State Vector Representation
        (i.e., the quantum state represented as its state vector).
        """

        final_quantum_state_vector_state = \
            execute(qiskrypt_quantum_circuit_prepare_and_measure_in_z_basis_1_qubit.qiskit_quantum_circuit,
                    qiskit_state_vector_backend).result().get_statevector()
        """
        Execute the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit
        and store the resulted quantum state represented in a final state vector.
        """

        assert_allclose(final_quantum_state_vector_state,
                        array([(1. + 0.j), (0. + 0.j)]),
                        rtol=1e-7, atol=1e-7)
        """
        Perform the Assertion of all close values in the values of the quantum state,
        represented by its state vector describing the given qubit,
        after being prepared (not measured) in the Z-Basis (Computational Basis), such that, |0⟩ ↦ |0⟩.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_10_prepare_measure_z_basis_1_qubit(self):
        """
        Test Case #10:

        - Prepare (and Measure) a qubit in the IBM Qiskit's Quantum Circuit of
          the Qiskrypt's Quantum Circuit, in the Z-Basis (Computational Basis).

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Quantum Circuit is created with a Qiskrypt's Quantum Register,
           with 1 qubit initialized in the state |0⟩;
        2) It is applied the Pauli-X (Bit Flip/NOT) Gate/Operation to the 1st qubit, such that, |0⟩ ↦ |1⟩;
        3) The 1st qubit is prepared (and measured) in the Z-Basis (Computational Basis), such that, |1⟩ ↦ |1⟩;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        num_qubits = num_bits = 1
        """
        Set the number of qubits and bits,
        for the Qiskrypt's Quantum and Classical Registers, respectively.
        """

        qiskrypt_quantum_register_prepare_and_measure_in_z_basis_1_qubit = \
            QiskryptQuantumRegister("qu_reg_10", num_qubits)
        """
        Create a Qiskrypt's Quantum Register with 1 qubit.
        """

        qiskrypt_classical_register_prepare_and_measure_in_z_basis_1_qubit = \
            QiskryptClassicalRegister("cl_reg_10", num_bits)
        """
        Create a Qiskrypt's Classical Register with 1 bit.
        """

        qiskrypt_quantum_circuit_prepare_and_measure_in_z_basis_1_qubit = \
            QiskryptQuantumCircuit("qu_circ_10",
                                   qiskrypt_quantum_registers=[qiskrypt_quantum_register_prepare_and_measure_in_z_basis_1_qubit],
                                   qiskrypt_fully_quantum_registers=None,
                                   qiskrypt_semi_quantum_registers=None,
                                   qiskrypt_ancilla_quantum_registers=None,
                                   qiskrypt_ancilla_fully_quantum_registers=None,
                                   qiskrypt_ancilla_semi_quantum_registers=None,
                                   qiskrypt_classical_registers=[qiskrypt_classical_register_prepare_and_measure_in_z_basis_1_qubit],
                                   global_phase=0, qiskit_quantum_circuit=None)
        """
        Create a Qiskrypt's Quantum Circuit with
        the previously created Qiskrypt's Quantum and Classical Registers.
        """

        qiskrypt_quantum_circuit_prepare_and_measure_in_z_basis_1_qubit \
            .apply_pauli_x(0, 0)
        """
        Apply the Pauli-X (Bit Flip/NOT) Gate/Operation to the given index for
        the single qubit of the given IBM Qiskit's Quantum Register (|0⟩ ↦ |1⟩).
        """

        qiskrypt_quantum_circuit_prepare_and_measure_in_z_basis_1_qubit \
            .prepare_and_measure_single_qubit_in_qiskit_quantum_register_in_z_basis(0, 0, 0, 0,
                                                                                    is_final_measurement=False)
        """
        Prepare (not Measuring) the given index for the single qubit of
        the given IBM Qiskit's Quantum Register, in the Z-Basis (Computational Basis).
        """

        qiskit_state_vector_backend = Aer.get_backend("statevector_simulator")
        """
        Getting the Aer Simulator Backend for the State Vector Representation
        (i.e., the quantum state represented as its state vector).
        """

        final_quantum_state_vector_state = \
            execute(qiskrypt_quantum_circuit_prepare_and_measure_in_z_basis_1_qubit.qiskit_quantum_circuit,
                    qiskit_state_vector_backend).result().get_statevector()
        """
        Execute the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit
        and store the resulted quantum state represented in a final state vector.
        """

        assert_allclose(final_quantum_state_vector_state,
                        array([(0. + 0.j), (1. + 0.j)]),
                        rtol=1e-7, atol=1e-7)
        """
        Perform the Assertion of all close values in the values of the quantum state,
        represented by its state vector describing the given qubit,
        after being prepared (not measured) in the Z-Basis (Computational Basis), such that, |1⟩ ↦ |1⟩.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_11_prepare_measure_z_basis_1_qubit(self):
        """
        Test Case #11:

        - Prepare (and Measure) a qubit in the IBM Qiskit's Quantum Circuit of
          the Qiskrypt's Quantum Circuit, in the Z-Basis (Computational Basis).

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Quantum Circuit is created with a Qiskrypt's Quantum Register,
           with 1 qubit initialized in the state |0⟩;
        2) It is applied the Hadamard Gate/Operation to the 1st qubit, such that, |0⟩ ↦ |+⟩;
        3) The 1st qubit is prepared (and measured) in the Z-Basis (Computational Basis), such that, |+⟩ ↦ |+⟩;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        num_qubits = num_bits = 1
        """
        Set the number of qubits and bits,
        for the Qiskrypt's Quantum and Classical Registers, respectively.
        """

        qiskrypt_quantum_register_prepare_and_measure_in_z_basis_1_qubit = \
            QiskryptQuantumRegister("qu_reg_11", num_qubits)
        """
        Create a Qiskrypt's Quantum Register with 1 qubit.
        """

        qiskrypt_classical_register_prepare_and_measure_in_z_basis_1_qubit = \
            QiskryptClassicalRegister("cl_reg_11", num_bits)
        """
        Create a Qiskrypt's Classical Register with 1 bit.
        """

        qiskrypt_quantum_circuit_prepare_and_measure_in_z_basis_1_qubit = \
            QiskryptQuantumCircuit("qu_circ_11",
                                   qiskrypt_quantum_registers=[qiskrypt_quantum_register_prepare_and_measure_in_z_basis_1_qubit],
                                   qiskrypt_fully_quantum_registers=None,
                                   qiskrypt_semi_quantum_registers=None,
                                   qiskrypt_ancilla_quantum_registers=None,
                                   qiskrypt_ancilla_fully_quantum_registers=None,
                                   qiskrypt_ancilla_semi_quantum_registers=None,
                                   qiskrypt_classical_registers=[qiskrypt_classical_register_prepare_and_measure_in_z_basis_1_qubit],
                                   global_phase=0, qiskit_quantum_circuit=None)
        """
        Create a Qiskrypt's Quantum Circuit with
        the previously created Qiskrypt's Quantum and Classical Registers.
        """

        qiskrypt_quantum_circuit_prepare_and_measure_in_z_basis_1_qubit \
            .apply_hadamard(0, 0)
        """
        Apply the Hadamard Gate/Operation to the given index for
        the single qubit of the given IBM Qiskit's Quantum Register (|0⟩ ↦ |+⟩).
        """

        qiskrypt_quantum_circuit_prepare_and_measure_in_z_basis_1_qubit \
            .prepare_and_measure_single_qubit_in_qiskit_quantum_register_in_z_basis(0, 0, 0, 0,
                                                                                    is_final_measurement=False)
        """
        Prepare (not Measuring) the given index for the single qubit of
        the given IBM Qiskit's Quantum Register, in the Z-Basis (Computational Basis).
        """

        qiskit_state_vector_backend = Aer.get_backend("statevector_simulator")
        """
        Getting the Aer Simulator Backend for the State Vector Representation
        (i.e., the quantum state represented as its state vector).
        """

        final_quantum_state_vector_state = \
            execute(qiskrypt_quantum_circuit_prepare_and_measure_in_z_basis_1_qubit.qiskit_quantum_circuit,
                    qiskit_state_vector_backend).result().get_statevector()
        """
        Execute the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit
        and store the resulted quantum state represented in a final state vector.
        """

        assert_allclose(final_quantum_state_vector_state,
                        array([((1. / sqrt(2.)) + 0.j), ((1. / sqrt(2.)) + 0.j)]),
                        rtol=1e-7, atol=1e-7)
        """
        Perform the Assertion of all close values in the values of the quantum state,
        represented by its state vector describing the given qubit,
        after being prepared (not measured) in the Z-Basis (Computational Basis), such that, |+⟩ ↦ |+⟩.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_12_prepare_measure_z_basis_1_qubit(self):
        """
        Test Case #12:

        - Prepare (and Measure) a qubit in the IBM Qiskit's Quantum Circuit of
          the Qiskrypt's Quantum Circuit, in the Z-Basis (Computational Basis).

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Quantum Circuit is created with a Qiskrypt's Quantum Register,
           with 1 qubit initialized in the state |0⟩;
        2) It is applied the Pauli-X (Bit Flip/NOT) Gate/Operation to the 1st qubit, such that, |0⟩ ↦ |1⟩;
        3) It is applied the Hadamard Gate/Operation to the 1st qubit, such that, |1⟩ ↦ |-⟩;
        4) The 1st qubit is prepared (and measured) in the Z-Basis (Computational Basis), such that, |-⟩ ↦ |-⟩;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        num_qubits = num_bits = 1
        """
        Set the number of qubits and bits,
        for the Qiskrypt's Quantum and Classical Registers, respectively.
        """

        qiskrypt_quantum_register_prepare_and_measure_in_z_basis_1_qubit = \
            QiskryptQuantumRegister("qu_reg_12", num_qubits)
        """
        Create a Qiskrypt's Quantum Register with 1 qubit.
        """

        qiskrypt_classical_register_prepare_and_measure_in_z_basis_1_qubit = \
            QiskryptClassicalRegister("cl_reg_12", num_bits)
        """
        Create a Qiskrypt's Classical Register with 1 bit.
        """

        qiskrypt_quantum_circuit_prepare_and_measure_in_z_basis_1_qubit = \
            QiskryptQuantumCircuit("qu_circ_12",
                                   qiskrypt_quantum_registers=[qiskrypt_quantum_register_prepare_and_measure_in_z_basis_1_qubit],
                                   qiskrypt_fully_quantum_registers=None,
                                   qiskrypt_semi_quantum_registers=None,
                                   qiskrypt_ancilla_quantum_registers=None,
                                   qiskrypt_ancilla_fully_quantum_registers=None,
                                   qiskrypt_ancilla_semi_quantum_registers=None,
                                   qiskrypt_classical_registers=[qiskrypt_classical_register_prepare_and_measure_in_z_basis_1_qubit],
                                   global_phase=0, qiskit_quantum_circuit=None)
        """
        Create a Qiskrypt's Quantum Circuit with
        the previously created Qiskrypt's Quantum and Classical Registers.
        """

        qiskrypt_quantum_circuit_prepare_and_measure_in_z_basis_1_qubit \
            .apply_pauli_x(0, 0)
        """
        Apply the Pauli-X (Bit Flip/NOT) Gate/Operation to the given index for
        the single qubit of the given IBM Qiskit's Quantum Register (|0⟩ ↦ |1⟩).
        """

        qiskrypt_quantum_circuit_prepare_and_measure_in_z_basis_1_qubit \
            .apply_hadamard(0, 0)
        """
        Apply the Hadamard Gate/Operation to the given index for
        the single qubit of the given IBM Qiskit's Quantum Register (|1⟩ ↦ |-⟩).
        """

        qiskrypt_quantum_circuit_prepare_and_measure_in_z_basis_1_qubit \
            .prepare_and_measure_single_qubit_in_qiskit_quantum_register_in_z_basis(0, 0, 0, 0,
                                                                                    is_final_measurement=False)
        """
        Prepare (not Measuring) the given index for the single qubit of
        the given IBM Qiskit's Quantum Register, in the Z-Basis (Computational Basis).
        """

        qiskit_state_vector_backend = Aer.get_backend("statevector_simulator")
        """
        Getting the Aer Simulator Backend for the State Vector Representation
        (i.e., the quantum state represented as its state vector).
        """

        final_quantum_state_vector_state = \
            execute(qiskrypt_quantum_circuit_prepare_and_measure_in_z_basis_1_qubit.qiskit_quantum_circuit,
                    qiskit_state_vector_backend).result().get_statevector()
        """
        Execute the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit
        and store the resulted quantum state represented in a final state vector.
        """

        assert_allclose(final_quantum_state_vector_state,
                        array([((1. / sqrt(2.)) + 0.j), -((1. / sqrt(2.)) + 0.j)]),
                        rtol=1e-7, atol=1e-7)
        """
        Perform the Assertion of all close values in the values of the quantum state,
        represented by its state vector describing the given qubit,
        after being prepared (not measured) in the Z-Basis (Computational Basis), such that, |-⟩ ↦ |-⟩.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)


class SingleQubitGatesOperations(TestCase):
    """
    Object Class of the Unitary Tests for the Single Qubit Gates/Operations in a Qiskrypt's Quantum Circuit.
    """

    def test_no_1_apply_pauli_i(self):
        """
        Test Case #1:

        - Apply the Pauli-I (Idle) Gate/Operation to a qubit of an IBM Qiskit's Quantum Register of
          the Qiskrypt's Quantum Register of a Qiskrypt's Quantum Circuit.

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Quantum Circuit is created with a Qiskrypt's Quantum Register,
           with 1 qubit initialized in the state |0⟩;
        2) It is applied the Pauli-I (Idle) Gate/Operation to the 1st qubit, such that, |0⟩ ↦ |0⟩;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        num_qubits = num_bits = 1
        """
        Set the number of qubits and bits, for Quantum and Classical Registers, respectively.
        """

        qiskrypt_quantum_register_pauli_i_gate_1_qubit = \
            QiskryptQuantumRegister("qu_reg_1", num_qubits)
        """
        Create a Qiskrypt's Quantum Register with 1 qubit.
        """

        qiskrypt_classical_register_pauli_i_gate_1_qubit = \
            QiskryptClassicalRegister("cl_reg_1", num_bits)
        """
        Create a Qiskrypt's Classical Register with 1 bit.
        """

        qiskrypt_quantum_circuit_pauli_i_gate_1_qubit = \
            QiskryptQuantumCircuit("qu_circ_1",
                                   qiskrypt_quantum_registers=[qiskrypt_quantum_register_pauli_i_gate_1_qubit],
                                   qiskrypt_fully_quantum_registers=None,
                                   qiskrypt_semi_quantum_registers=None,
                                   qiskrypt_ancilla_quantum_registers=None,
                                   qiskrypt_ancilla_fully_quantum_registers=None,
                                   qiskrypt_ancilla_semi_quantum_registers=None,
                                   qiskrypt_classical_registers=[qiskrypt_classical_register_pauli_i_gate_1_qubit],
                                   global_phase=0, qiskit_quantum_circuit=None)
        """
        Create a Qiskrypt's Quantum Circuit with
        the previously created Qiskrypt's Quantum and Classical Registers.
        """

        qiskrypt_quantum_circuit_pauli_i_gate_1_qubit \
            .apply_pauli_i(0, 0)
        """
        Apply the Pauli-I (Idle) Gate/Operation to the given index for
        the single qubit of the given IBM Qiskit's Quantum Register (|0⟩ ↦ |0⟩).
        """

        qiskit_state_vector_backend = Aer.get_backend("statevector_simulator")
        """
        Getting the Aer Simulator Backend for the State Vector Representation
        (i.e., the quantum state represented as its state vector).
        """

        final_quantum_state_vector_state = \
            execute(qiskrypt_quantum_circuit_pauli_i_gate_1_qubit.qiskit_quantum_circuit,
                    qiskit_state_vector_backend).result().get_statevector()
        """
        Execute the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit
        and store the resulted quantum state represented in a final state vector.
        """

        assert_allclose(final_quantum_state_vector_state,
                        array([(1. + 0.j), (0. + 0.j)]),
                        rtol=1e-7, atol=1e-7)
        """
        Perform the Assertion of all close values in the values of the quantum state,
        represented by its state vector describing the given qubit,
        after being applied the Pauli-I (Idle) Quantum Gate/Operation.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_2_apply_pauli_i(self):
        """
        Test Case #2:

        - Apply the Pauli-I (Idle) Gate/Operation to a qubit of an IBM Qiskit's Quantum Register of
          the Qiskrypt's Quantum Register of a Qiskrypt's Quantum Circuit.

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Quantum Circuit is created with a Qiskrypt's Quantum Register,
           with 1 qubit initialized in the state |0⟩;
        2) It is applied the Pauli-X (Bit Flip/NOT) Gate/Operation to the 1st qubit, such that, |0⟩ ↦ |1⟩;
        3) It is applied the Pauli-I (Idle) Gate/Operation to the 1st qubit, such that, |1⟩ ↦ |1⟩;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        num_qubits = num_bits = 1
        """
        Set the number of qubits and bits, for Quantum and Classical Registers, respectively.
        """

        qiskrypt_quantum_register_pauli_i_gate_1_qubit = \
            QiskryptQuantumRegister("qu_reg_2", num_qubits)
        """
        Create a Qiskrypt's Quantum Register with 1 qubit.
        """

        qiskrypt_classical_register_pauli_i_gate_1_qubit = \
            QiskryptClassicalRegister("cl_reg_2", num_bits)
        """
        Create a Qiskrypt's Classical Register with 1 bit.
        """

        qiskrypt_quantum_circuit_pauli_i_gate_1_qubit = \
            QiskryptQuantumCircuit("qu_circ_2",
                                   qiskrypt_quantum_registers=[qiskrypt_quantum_register_pauli_i_gate_1_qubit],
                                   qiskrypt_fully_quantum_registers=None,
                                   qiskrypt_semi_quantum_registers=None,
                                   qiskrypt_ancilla_quantum_registers=None,
                                   qiskrypt_ancilla_fully_quantum_registers=None,
                                   qiskrypt_ancilla_semi_quantum_registers=None,
                                   qiskrypt_classical_registers=[qiskrypt_classical_register_pauli_i_gate_1_qubit],
                                   global_phase=0, qiskit_quantum_circuit=None)
        """
        Create a Qiskrypt's Quantum Circuit with
        the previously created Qiskrypt's Quantum and Classical Registers.
        """

        qiskrypt_quantum_circuit_pauli_i_gate_1_qubit \
            .apply_pauli_x(0, 0)
        """
        Apply the Pauli-X (Bit Flip/NOT) Gate/Operation to the given index for
        the single qubit of the given IBM Qiskit's Quantum Register (|0⟩ ↦ |1⟩).
        """

        qiskrypt_quantum_circuit_pauli_i_gate_1_qubit \
            .apply_pauli_i(0, 0)
        """
        Apply the Pauli-I (Idle) Gate/Operation to the given index for
        the single qubit of the given IBM Qiskit's Quantum Register (|1⟩ ↦ |1⟩).
        """

        qiskit_state_vector_backend = Aer.get_backend("statevector_simulator")
        """
        Getting the Aer Simulator Backend for the State Vector Representation
        (i.e., the quantum state represented as its state vector).
        """

        final_quantum_state_vector_state = \
            execute(qiskrypt_quantum_circuit_pauli_i_gate_1_qubit.qiskit_quantum_circuit,
                    qiskit_state_vector_backend).result().get_statevector()
        """
        Execute the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit
        and store the resulted quantum state represented in a final state vector.
        """

        assert_allclose(final_quantum_state_vector_state,
                        array([(0. + 0.j), (1. + 0.j)]),
                        rtol=1e-7, atol=1e-7)
        """
        Perform the Assertion of all close values in the values of the quantum state,
        represented by its state vector describing the given qubit,
        after being applied the Pauli-I (Idle) Quantum Gate/Operation.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_3_apply_pauli_i(self):
        """
        Test Case #3:

        - Apply the Pauli-I (Idle) Gate/Operation to a qubit of an IBM Qiskit's Quantum Register of
          the Qiskrypt's Quantum Register of a Qiskrypt's Quantum Circuit.

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Quantum Circuit is created with a Qiskrypt's Quantum Register,
           with 1 qubit initialized in the state |0⟩;
        2) It is applied the Hadamard Gate/Operation to the 1st qubit, such that, |0⟩ ↦ |+⟩;
        3) It is applied the Pauli-I (Idle) Gate/Operation to the 1st qubit, such that, |+⟩ ↦ |+⟩;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        num_qubits = num_bits = 1
        """
        Set the number of qubits and bits, for Quantum and Classical Registers, respectively.
        """

        qiskrypt_quantum_register_pauli_i_gate_1_qubit = \
            QiskryptQuantumRegister("qu_reg_3", num_qubits)
        """
        Create a Qiskrypt's Quantum Register with 1 qubit.
        """

        qiskrypt_classical_register_pauli_i_gate_1_qubit = \
            QiskryptClassicalRegister("cl_reg_3", num_bits)
        """
        Create a Qiskrypt's Classical Register with 1 bit.
        """

        qiskrypt_quantum_circuit_pauli_i_gate_1_qubit = \
            QiskryptQuantumCircuit("qu_circ_3",
                                   qiskrypt_quantum_registers=[qiskrypt_quantum_register_pauli_i_gate_1_qubit],
                                   qiskrypt_fully_quantum_registers=None,
                                   qiskrypt_semi_quantum_registers=None,
                                   qiskrypt_ancilla_quantum_registers=None,
                                   qiskrypt_ancilla_fully_quantum_registers=None,
                                   qiskrypt_ancilla_semi_quantum_registers=None,
                                   qiskrypt_classical_registers=[qiskrypt_classical_register_pauli_i_gate_1_qubit],
                                   global_phase=0, qiskit_quantum_circuit=None)
        """
        Create a Qiskrypt's Quantum Circuit with
        the previously created Qiskrypt's Quantum and Classical Registers.
        """

        qiskrypt_quantum_circuit_pauli_i_gate_1_qubit \
            .apply_hadamard(0, 0)
        """
        Apply the Hadamard Gate/Operation to the given index for
        the single qubit of the given IBM Qiskit's Quantum Register (|0⟩ ↦ |+⟩).
        """

        qiskrypt_quantum_circuit_pauli_i_gate_1_qubit \
            .apply_pauli_i(0, 0)
        """
        Apply the Pauli-I (Idle) Gate/Operation to the given index for
        the single qubit of the given IBM Qiskit's Quantum Register (|+⟩ ↦ |+⟩).
        """

        qiskit_state_vector_backend = Aer.get_backend("statevector_simulator")
        """
        Getting the Aer Simulator Backend for the State Vector Representation
        (i.e., the quantum state represented as its state vector).
        """

        final_quantum_state_vector_state = \
            execute(qiskrypt_quantum_circuit_pauli_i_gate_1_qubit.qiskit_quantum_circuit,
                    qiskit_state_vector_backend).result().get_statevector()
        """
        Execute the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit
        and store the resulted quantum state represented in a final state vector.
        """

        assert_allclose(final_quantum_state_vector_state,
                        array([((1. / sqrt(2.)) + 0.j), ((1. / sqrt(2.)) + 0.j)]),
                        rtol=1e-7, atol=1e-7)
        """
        Perform the Assertion of all close values in the values of the quantum state,
        represented by its state vector describing the given qubit,
        after being applied the Pauli-I (Idle) Quantum Gate/Operation.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_4_apply_pauli_i(self):
        """
        Test Case 4#:

        - Apply the Pauli-I (Idle) Gate/Operation to a qubit of an IBM Qiskit's Quantum Register of
          the Qiskrypt's Quantum Register of a Qiskrypt's Quantum Circuit.

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Quantum Circuit is created with a Qiskrypt's Quantum Register,
           with 1 qubit initialized in the state |0⟩;
        2) It is applied the Pauli-X (Bit Flip/NOT) Gate/Operation to the 1st qubit, such that, |0⟩ ↦ |1⟩;
        3) It is applied the Hadamard Gate/Operation to the 1st qubit, such that, |1⟩ ↦ |-⟩;
        4) It is applied the Pauli-I (Idle) Gate/Operation to the 1st qubit, such that, |-⟩ ↦ |-⟩;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        num_qubits = num_bits = 1
        """
        Set the number of qubits and bits, for Quantum and Classical Registers, respectively.
        """

        qiskrypt_quantum_register_pauli_i_gate_1_qubit = \
            QiskryptQuantumRegister("qu_reg_4", num_qubits)
        """
        Create a Qiskrypt's Quantum Register with 1 qubit.
        """

        qiskrypt_classical_register_pauli_i_gate_1_qubit = \
            QiskryptClassicalRegister("cl_reg_4", num_bits)
        """
        Create a Qiskrypt's Classical Register with 1 bit.
        """

        qiskrypt_quantum_circuit_pauli_i_gate_1_qubit = \
            QiskryptQuantumCircuit("qu_circ_4",
                                   qiskrypt_quantum_registers=[qiskrypt_quantum_register_pauli_i_gate_1_qubit],
                                   qiskrypt_fully_quantum_registers=None,
                                   qiskrypt_semi_quantum_registers=None,
                                   qiskrypt_ancilla_quantum_registers=None,
                                   qiskrypt_ancilla_fully_quantum_registers=None,
                                   qiskrypt_ancilla_semi_quantum_registers=None,
                                   qiskrypt_classical_registers=[qiskrypt_classical_register_pauli_i_gate_1_qubit],
                                   global_phase=0, qiskit_quantum_circuit=None)
        """
        Create a Qiskrypt's Quantum Circuit with
        the previously created Qiskrypt's Quantum and Classical Registers.
        """

        qiskrypt_quantum_circuit_pauli_i_gate_1_qubit \
            .apply_pauli_x(0, 0)
        """
        Apply the Pauli-X (Bit Flip/NOT) Gate/Operation to the given index for
        the single qubit of the given IBM Qiskit's Quantum Register (|0⟩ ↦ |1⟩).
        """

        qiskrypt_quantum_circuit_pauli_i_gate_1_qubit \
            .apply_hadamard(0, 0)
        """
        Apply the Hadamard Gate/Operation to the given index for
        the single qubit of the given IBM Qiskit's Quantum Register (|1⟩ ↦ |-⟩).
        """

        qiskrypt_quantum_circuit_pauli_i_gate_1_qubit \
            .apply_pauli_i(0, 0)
        """
        Apply the Pauli-I (Idle) Gate/Operation to the given index for
        the single qubit of the given IBM Qiskit's Quantum Register (|-⟩ ↦ |-⟩).
        """

        qiskit_state_vector_backend = Aer.get_backend("statevector_simulator")
        """
        Getting the Aer Simulator Backend for the State Vector Representation
        (i.e., the quantum state represented as its state vector).
        """

        final_quantum_state_vector_state = \
            execute(qiskrypt_quantum_circuit_pauli_i_gate_1_qubit.qiskit_quantum_circuit,
                    qiskit_state_vector_backend).result().get_statevector()
        """
        Execute the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit
        and store the resulted quantum state represented in a final state vector.
        """

        assert_allclose(final_quantum_state_vector_state,
                        array([((1. / sqrt(2.)) + 0.j), -((1. / sqrt(2.)) + 0.j)]),
                        rtol=1e-7, atol=1e-7)
        """
        Perform the Assertion of all close values in the values of the quantum state,
        represented by its state vector describing the given qubit,
        after being applied the Pauli-I (Idle) Quantum Gate/Operation.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_5_apply_pauli_x(self):
        """
        Test Case #5:

        - Apply the Pauli-X (Bit Flip/NOT) Gate/Operation to a qubit of an IBM Qiskit's Quantum Register of
          the Qiskrypt's Quantum Register of a Qiskrypt's Quantum Circuit.

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Quantum Circuit is created with a Qiskrypt's Quantum Register,
           with 1 qubit initialized in the state |0⟩;
        2) It is applied the Pauli-X (Bit Flip/NOT) Gate/Operation to the 1st qubit, such that, |0⟩ ↦ |1⟩;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        num_qubits = num_bits = 1
        """
        Set the number of qubits and bits, for Quantum and Classical Registers, respectively.
        """

        qiskrypt_quantum_register_pauli_x_gate_1_qubit = \
            QiskryptQuantumRegister("qu_reg_5", num_qubits)
        """
        Create a Qiskrypt's Quantum Register with 1 qubit.
        """

        qiskrypt_classical_register_pauli_x_gate_1_qubit = \
            QiskryptClassicalRegister("cl_reg_5", num_bits)
        """
        Create a Qiskrypt's Classical Register with 1 bit.
        """

        qiskrypt_quantum_circuit_pauli_x_gate_1_qubit = \
            QiskryptQuantumCircuit("qu_circ_5",
                                   qiskrypt_quantum_registers=[qiskrypt_quantum_register_pauli_x_gate_1_qubit],
                                   qiskrypt_fully_quantum_registers=None,
                                   qiskrypt_semi_quantum_registers=None,
                                   qiskrypt_ancilla_quantum_registers=None,
                                   qiskrypt_ancilla_fully_quantum_registers=None,
                                   qiskrypt_ancilla_semi_quantum_registers=None,
                                   qiskrypt_classical_registers=[qiskrypt_classical_register_pauli_x_gate_1_qubit],
                                   global_phase=0, qiskit_quantum_circuit=None)
        """
        Create a Qiskrypt's Quantum Circuit with
        the previously created Qiskrypt's Quantum and Classical Registers.
        """

        qiskrypt_quantum_circuit_pauli_x_gate_1_qubit \
            .apply_pauli_x(0, 0)
        """
        Apply the Pauli-X (Bit Flip/NOT) Gate/Operation to the given index for
        the single qubit of the given IBM Qiskit's Quantum Register (|0⟩ ↦ |1⟩).
        """

        qiskit_state_vector_backend = Aer.get_backend("statevector_simulator")
        """
        Getting the Aer Simulator Backend for the State Vector Representation
        (i.e., the quantum state represented as its state vector).
        """

        final_quantum_state_vector_state = \
            execute(qiskrypt_quantum_circuit_pauli_x_gate_1_qubit.qiskit_quantum_circuit,
                    qiskit_state_vector_backend).result().get_statevector()
        """
        Execute the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit
        and store the resulted quantum state represented in a final state vector.
        """

        assert_allclose(final_quantum_state_vector_state,
                        array([(0. + 0.j), (1. + 0.j)]),
                        rtol=1e-7, atol=1e-7)
        """
        Perform the Assertion of all close values in the values of the quantum state,
        represented by its state vector describing the given qubit,
        after being applied the Pauli-X (Bit Flip/NOT) Quantum Gate/Operation.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_6_apply_pauli_x(self):
        """
        Test Case #6:

        - Apply the Pauli-X (Bit Flip/NOT) Gate/Operation to a qubit of an IBM Qiskit's Quantum Register of
          the Qiskrypt's Quantum Register of a Qiskrypt's Quantum Circuit.

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Quantum Circuit is created with a Qiskrypt's Quantum Register,
           with 1 qubit initialized in the state |0⟩;
        2) It is applied the Pauli-X (Bit Flip/NOT) Gate/Operation to the 1st qubit, such that, |0⟩ ↦ |1⟩;
        3) It is applied the Pauli-X (Bit Flip/NOT) Gate/Operation to the 1st qubit, such that, |1⟩ ↦ |0⟩;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        num_qubits = num_bits = 1
        """
        Set the number of qubits and bits, for Quantum and Classical Registers, respectively.
        """

        qiskrypt_quantum_register_pauli_x_gate_1_qubit = \
            QiskryptQuantumRegister("qu_reg_6", num_qubits)
        """
        Create a Qiskrypt's Quantum Register with 1 qubit.
        """

        qiskrypt_classical_register_pauli_x_gate_1_qubit = \
            QiskryptClassicalRegister("cl_reg_6", num_bits)
        """
        Create a Qiskrypt's Classical Register with 1 bit.
        """

        qiskrypt_quantum_circuit_pauli_x_gate_1_qubit = \
            QiskryptQuantumCircuit("qu_circ_6",
                                   qiskrypt_quantum_registers=[qiskrypt_quantum_register_pauli_x_gate_1_qubit],
                                   qiskrypt_fully_quantum_registers=None,
                                   qiskrypt_semi_quantum_registers=None,
                                   qiskrypt_ancilla_quantum_registers=None,
                                   qiskrypt_ancilla_fully_quantum_registers=None,
                                   qiskrypt_ancilla_semi_quantum_registers=None,
                                   qiskrypt_classical_registers=[qiskrypt_classical_register_pauli_x_gate_1_qubit],
                                   global_phase=0, qiskit_quantum_circuit=None)
        """
        Create a Qiskrypt's Quantum Circuit with
        the previously created Qiskrypt's Quantum and Classical Registers.
        """

        qiskrypt_quantum_circuit_pauli_x_gate_1_qubit \
            .apply_pauli_x(0, 0)
        """
        Apply the Pauli-X (Bit Flip/NOT) Gate/Operation to the given index for
        the single qubit of the given IBM Qiskit's Quantum Register (|0⟩ ↦ |1⟩).
        """

        qiskrypt_quantum_circuit_pauli_x_gate_1_qubit \
            .apply_pauli_x(0, 0)
        """
        Apply the Pauli-X (Bit Flip/NOT) Gate/Operation to the given index for
        the single qubit of the given IBM Qiskit's Quantum Register (|1⟩ ↦ |0⟩).
        """

        qiskit_state_vector_backend = Aer.get_backend("statevector_simulator")
        """
        Getting the Aer Simulator Backend for the State Vector Representation
        (i.e., the quantum state represented as its state vector).
        """

        final_quantum_state_vector_state = \
            execute(qiskrypt_quantum_circuit_pauli_x_gate_1_qubit.qiskit_quantum_circuit,
                    qiskit_state_vector_backend).result().get_statevector()
        """
        Execute the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit
        and store the resulted quantum state represented in a final state vector.
        """

        assert_allclose(final_quantum_state_vector_state,
                        array([(1. + 0.j), (0. + 0.j)]),
                        rtol=1e-7, atol=1e-7)
        """
        Perform the Assertion of all close values in the values of the quantum state,
        represented by its state vector describing the given qubit,
        after being applied the Pauli-X (Bit Flip/NOT) Quantum Gate/Operation.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_7_apply_pauli_x(self):
        """
        Test Case #7:

        - Apply the Pauli-X (Bit Flip/NOT) Gate/Operation to a qubit of an IBM Qiskit's Quantum Register of
          the Qiskrypt's Quantum Register of a Qiskrypt's Quantum Circuit.

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Quantum Circuit is created with a Qiskrypt's Quantum Register,
           with 1 qubit initialized in the state |0⟩;
        2) It is applied the Hadamard Gate/Operation to the 1st qubit, such that, |0⟩ ↦ |+⟩;
        3) It is applied the Pauli-X (Bit Flip/NOT) Gate/Operation to the 1st qubit, such that, |+⟩ ↦ |+⟩;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        num_qubits = num_bits = 1
        """
        Set the number of qubits and bits, for Quantum and Classical Registers, respectively.
        """

        qiskrypt_quantum_register_pauli_x_gate_1_qubit = \
            QiskryptQuantumRegister("qu_reg_7", num_qubits)
        """
        Create a Qiskrypt's Quantum Register with 1 qubit.
        """

        qiskrypt_classical_register_pauli_x_gate_1_qubit = \
            QiskryptClassicalRegister("cl_reg_7", num_bits)
        """
        Create a Qiskrypt's Classical Register with 1 bit.
        """

        qiskrypt_quantum_circuit_pauli_x_gate_1_qubit = \
            QiskryptQuantumCircuit("qu_circ_7",
                                   qiskrypt_quantum_registers=[qiskrypt_quantum_register_pauli_x_gate_1_qubit],
                                   qiskrypt_fully_quantum_registers=None,
                                   qiskrypt_semi_quantum_registers=None,
                                   qiskrypt_ancilla_quantum_registers=None,
                                   qiskrypt_ancilla_fully_quantum_registers=None,
                                   qiskrypt_ancilla_semi_quantum_registers=None,
                                   qiskrypt_classical_registers=[qiskrypt_classical_register_pauli_x_gate_1_qubit],
                                   global_phase=0, qiskit_quantum_circuit=None)
        """
        Create a Qiskrypt's Quantum Circuit with
        the previously created Qiskrypt's Quantum and Classical Registers.
        """

        qiskrypt_quantum_circuit_pauli_x_gate_1_qubit \
            .apply_hadamard(0, 0)
        """
        Apply the Hadamard Gate/Operation to the given index for
        the single qubit of the given IBM Qiskit's Quantum Register (|0⟩ ↦ |+⟩).
        """

        qiskrypt_quantum_circuit_pauli_x_gate_1_qubit \
            .apply_pauli_x(0, 0)
        """
        Apply the Pauli-X (Bit Flip/NOT) Gate/Operation to the given index for
        the single qubit of the given IBM Qiskit's Quantum Register (|+⟩ ↦ |+⟩).
        """

        qiskit_state_vector_backend = Aer.get_backend("statevector_simulator")
        """
        Getting the Aer Simulator Backend for the State Vector Representation
        (i.e., the quantum state represented as its state vector).
        """

        final_quantum_state_vector_state = \
            execute(qiskrypt_quantum_circuit_pauli_x_gate_1_qubit.qiskit_quantum_circuit,
                    qiskit_state_vector_backend).result().get_statevector()
        """
        Execute the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit
        and store the resulted quantum state represented in a final state vector.
        """

        assert_allclose(final_quantum_state_vector_state,
                        array([((1. / sqrt(2.)) + 0.j), ((1. / sqrt(2.)) + 0.j)]),
                        rtol=1e-7, atol=1e-7)
        """
        Perform the Assertion of all close values in the values of the quantum state,
        represented by its state vector describing the given qubit,
        after being applied the Pauli-X (Bit Flip/NOT) Quantum Gate/Operation.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_8_apply_pauli_x(self):
        """
        Test Case 8#:

        - Apply the Pauli-X (Bit Flip/NOT) Gate/Operation to a qubit of an IBM Qiskit's Quantum Register of
          the Qiskrypt's Quantum Register of a Qiskrypt's Quantum Circuit.

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Quantum Circuit is created with a Qiskrypt's Quantum Register,
           with 1 qubit initialized in the state |0⟩;
        2) It is applied the Pauli-X (Bit Flip/NOT) Gate/Operation to the 1st qubit, such that, |0⟩ ↦ |1⟩;
        3) It is applied the Hadamard Gate/Operation to the 1st qubit, such that, |1⟩ ↦ |-⟩;
        4) It is applied the Pauli-X (Bit Flip/NOT) Gate/Operation to the 1st qubit, such that,
           |-⟩ ↦ |Ψ⟩ = 1/sqrt(2) × (-|0⟩ + |1⟩);

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        num_qubits = num_bits = 1
        """
        Set the number of qubits and bits, for Quantum and Classical Registers, respectively.
        """

        qiskrypt_quantum_register_pauli_x_gate_1_qubit = \
            QiskryptQuantumRegister("qu_reg_8", num_qubits)
        """
        Create a Qiskrypt's Quantum Register with 1 qubit.
        """

        qiskrypt_classical_register_pauli_x_gate_1_qubit = \
            QiskryptClassicalRegister("cl_reg_8", num_bits)
        """
        Create a Qiskrypt's Classical Register with 1 bit.
        """

        qiskrypt_quantum_circuit_pauli_x_gate_1_qubit = \
            QiskryptQuantumCircuit("qu_circ_8",
                                   qiskrypt_quantum_registers=[qiskrypt_quantum_register_pauli_x_gate_1_qubit],
                                   qiskrypt_fully_quantum_registers=None,
                                   qiskrypt_semi_quantum_registers=None,
                                   qiskrypt_ancilla_quantum_registers=None,
                                   qiskrypt_ancilla_fully_quantum_registers=None,
                                   qiskrypt_ancilla_semi_quantum_registers=None,
                                   qiskrypt_classical_registers=[qiskrypt_classical_register_pauli_x_gate_1_qubit],
                                   global_phase=0, qiskit_quantum_circuit=None)
        """
        Create a Qiskrypt's Quantum Circuit with
        the previously created Qiskrypt's Quantum and Classical Registers.
        """

        qiskrypt_quantum_circuit_pauli_x_gate_1_qubit \
            .apply_pauli_x(0, 0)
        """
        Apply the Pauli-X (Bit Flip/NOT) Gate/Operation to the given index for
        the single qubit of the given IBM Qiskit's Quantum Register (|0⟩ ↦ |1⟩).
        """

        qiskrypt_quantum_circuit_pauli_x_gate_1_qubit \
            .apply_hadamard(0, 0)
        """
        Apply the Hadamard Gate/Operation to the given index for
        the single qubit of the given IBM Qiskit's Quantum Register (|1⟩ ↦ |-⟩).
        """

        qiskrypt_quantum_circuit_pauli_x_gate_1_qubit \
            .apply_pauli_x(0, 0)
        """
        Apply the Pauli-X (Bit Flip/NOT) Gate/Operation to the given index for
        the single qubit of the given IBM Qiskit's Quantum Register (|-⟩ ↦ |Ψ⟩ = 1/sqrt(2) × (-|0⟩ + |1⟩)).
        """

        qiskit_state_vector_backend = Aer.get_backend("statevector_simulator")
        """
        Getting the Aer Simulator Backend for the State Vector Representation
        (i.e., the quantum state represented as its state vector).
        """

        final_quantum_state_vector_state = \
            execute(qiskrypt_quantum_circuit_pauli_x_gate_1_qubit.qiskit_quantum_circuit,
                    qiskit_state_vector_backend).result().get_statevector()
        """
        Execute the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit
        and store the resulted quantum state represented in a final state vector.
        """

        assert_allclose(final_quantum_state_vector_state,
                        array([-((1. / sqrt(2.)) + 0.j), ((1. / sqrt(2.)) + 0.j)]),
                        rtol=1e-7, atol=1e-7)
        """
        Perform the Assertion of all close values in the values of the quantum state,
        represented by its state vector describing the given qubit,
        after being applied the Pauli-X (Bit Flip/NOT) Quantum Gate/Operation.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_9_apply_pauli_y(self):
        """
        Test Case #9:

        - Apply the Pauli-Y Gate/Operation to a qubit of an IBM Qiskit's Quantum Register of
          the Qiskrypt's Quantum Register of a Qiskrypt's Quantum Circuit.

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Quantum Circuit is created with a Qiskrypt's Quantum Register,
           with 1 qubit initialized in the state |0⟩;
        2) It is applied the Pauli-Y Gate/Operation to the 1st qubit, such that, |0⟩ ↦ i|1⟩;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        num_qubits = num_bits = 1
        """
        Set the number of qubits and bits, for Quantum and Classical Registers, respectively.
        """

        qiskrypt_quantum_register_pauli_y_gate_1_qubit = \
            QiskryptQuantumRegister("qu_reg_9", num_qubits)
        """
        Create a Qiskrypt's Quantum Register with 1 qubit.
        """

        qiskrypt_classical_register_pauli_y_gate_1_qubit = \
            QiskryptClassicalRegister("cl_reg_9", num_bits)
        """
        Create a Qiskrypt's Classical Register with 1 bit.
        """

        qiskrypt_quantum_circuit_pauli_y_gate_1_qubit = \
            QiskryptQuantumCircuit("qu_circ_9",
                                   qiskrypt_quantum_registers=[qiskrypt_quantum_register_pauli_y_gate_1_qubit],
                                   qiskrypt_fully_quantum_registers=None,
                                   qiskrypt_semi_quantum_registers=None,
                                   qiskrypt_ancilla_quantum_registers=None,
                                   qiskrypt_ancilla_fully_quantum_registers=None,
                                   qiskrypt_ancilla_semi_quantum_registers=None,
                                   qiskrypt_classical_registers=[qiskrypt_classical_register_pauli_y_gate_1_qubit],
                                   global_phase=0, qiskit_quantum_circuit=None)
        """
        Create a Qiskrypt's Quantum Circuit with
        the previously created Qiskrypt's Quantum and Classical Registers.
        """

        qiskrypt_quantum_circuit_pauli_y_gate_1_qubit \
            .apply_pauli_y(0, 0)
        """
        Apply the Pauli-Y Gate/Operation to the given index for
        the single qubit of the given IBM Qiskit's Quantum Register (|0⟩ ↦ i|1⟩).
        """

        qiskit_state_vector_backend = Aer.get_backend("statevector_simulator")
        """
        Getting the Aer Simulator Backend for the State Vector Representation
        (i.e., the quantum state represented as its state vector).
        """

        final_quantum_state_vector_state = \
            execute(qiskrypt_quantum_circuit_pauli_y_gate_1_qubit.qiskit_quantum_circuit,
                    qiskit_state_vector_backend).result().get_statevector()
        """
        Execute the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit
        and store the resulted quantum state represented in a final state vector.
        """

        assert_allclose(final_quantum_state_vector_state,
                        array([(0. + 0.j), (0. + 1.j)]),
                        rtol=1e-7, atol=1e-7)
        """
        Perform the Assertion of all close values in the values of the quantum state,
        represented by its state vector describing the given qubit,
        after being applied the Pauli-Y Quantum Gate/Operation.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_10_apply_pauli_y(self):
        """
        Test Case #10:

        - Apply the Pauli-Y Gate/Operation to a qubit of an IBM Qiskit's Quantum Register of
          the Qiskrypt's Quantum Register of a Qiskrypt's Quantum Circuit.

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Quantum Circuit is created with a Qiskrypt's Quantum Register,
           with 1 qubit initialized in the state |0⟩;
        2) It is applied the Pauli-X (Bit Flip/NOT) Gate/Operation to the 1st qubit, such that, |0⟩ ↦ |1⟩;
        3) It is applied the Pauli-Y Gate/Operation to the 1st qubit, such that, |1⟩ ↦ -i|0⟩;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        num_qubits = num_bits = 1
        """
        Set the number of qubits and bits, for Quantum and Classical Registers, respectively.
        """

        qiskrypt_quantum_register_pauli_y_gate_1_qubit = \
            QiskryptQuantumRegister("qu_reg_10", num_qubits)
        """
        Create a Qiskrypt's Quantum Register with 1 qubit.
        """

        qiskrypt_classical_register_pauli_y_gate_1_qubit = \
            QiskryptClassicalRegister("cl_reg_10", num_bits)
        """
        Create a Qiskrypt's Classical Register with 1 bit.
        """

        qiskrypt_quantum_circuit_pauli_y_gate_1_qubit = \
            QiskryptQuantumCircuit("qu_circ_10",
                                   qiskrypt_quantum_registers=[qiskrypt_quantum_register_pauli_y_gate_1_qubit],
                                   qiskrypt_fully_quantum_registers=None,
                                   qiskrypt_semi_quantum_registers=None,
                                   qiskrypt_ancilla_quantum_registers=None,
                                   qiskrypt_ancilla_fully_quantum_registers=None,
                                   qiskrypt_ancilla_semi_quantum_registers=None,
                                   qiskrypt_classical_registers=[qiskrypt_classical_register_pauli_y_gate_1_qubit],
                                   global_phase=0, qiskit_quantum_circuit=None)
        """
        Create a Qiskrypt's Quantum Circuit with
        the previously created Qiskrypt's Quantum and Classical Registers.
        """

        qiskrypt_quantum_circuit_pauli_y_gate_1_qubit \
            .apply_pauli_x(0, 0)
        """
        Apply the Pauli-X (Bit Flip/NOT) Gate/Operation to the given index for
        the single qubit of the given IBM Qiskit's Quantum Register (|0⟩ ↦ |1⟩).
        """

        qiskrypt_quantum_circuit_pauli_y_gate_1_qubit \
            .apply_pauli_y(0, 0)
        """
        Apply the Pauli-Y Gate/Operation to the given index for
        the single qubit of the given IBM Qiskit's Quantum Register (|1⟩ ↦ -i|0⟩).
        """

        qiskit_state_vector_backend = Aer.get_backend("statevector_simulator")
        """
        Getting the Aer Simulator Backend for the State Vector Representation
        (i.e., the quantum state represented as its state vector).
        """

        final_quantum_state_vector_state = \
            execute(qiskrypt_quantum_circuit_pauli_y_gate_1_qubit.qiskit_quantum_circuit,
                    qiskit_state_vector_backend).result().get_statevector()
        """
        Execute the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit
        and store the resulted quantum state represented in a final state vector.
        """

        assert_allclose(final_quantum_state_vector_state,
                        array([(0. - 1.j), (0. + 0.j)]),
                        rtol=1e-7, atol=1e-7)
        """
        Perform the Assertion of all close values in the values of the quantum state,
        represented by its state vector describing the given qubit,
        after being applied the Pauli-Y Quantum Gate/Operation.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_11_apply_pauli_y(self):
        """
        Test Case #11:

        - Apply the Pauli-Y Gate/Operation to a qubit of an IBM Qiskit's Quantum Register of
          the Qiskrypt's Quantum Register of a Qiskrypt's Quantum Circuit.

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Quantum Circuit is created with a Qiskrypt's Quantum Register,
           with 1 qubit initialized in the state |0⟩;
        2) It is applied the Hadamard Gate/Operation to the 1st qubit, such that, |0⟩ ↦ |+⟩;
        3) It is applied the Pauli-Y Gate/Operation to the 1st qubit, such that,
           |+⟩ ↦ |Ψ⟩ = 1/sqrt(2)i × (-|0⟩ + |1⟩);

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        num_qubits = num_bits = 1
        """
        Set the number of qubits and bits, for Quantum and Classical Registers, respectively.
        """

        qiskrypt_quantum_register_pauli_y_gate_1_qubit = \
            QiskryptQuantumRegister("qu_reg_11", num_qubits)
        """
        Create a Qiskrypt's Quantum Register with 1 qubit.
        """

        qiskrypt_classical_register_pauli_y_gate_1_qubit = \
            QiskryptClassicalRegister("cl_reg_11", num_bits)
        """
        Create a Qiskrypt's Classical Register with 1 bit.
        """

        qiskrypt_quantum_circuit_pauli_y_gate_1_qubit = \
            QiskryptQuantumCircuit("qu_circ_11",
                                   qiskrypt_quantum_registers=[qiskrypt_quantum_register_pauli_y_gate_1_qubit],
                                   qiskrypt_fully_quantum_registers=None,
                                   qiskrypt_semi_quantum_registers=None,
                                   qiskrypt_ancilla_quantum_registers=None,
                                   qiskrypt_ancilla_fully_quantum_registers=None,
                                   qiskrypt_ancilla_semi_quantum_registers=None,
                                   qiskrypt_classical_registers=[qiskrypt_classical_register_pauli_y_gate_1_qubit],
                                   global_phase=0, qiskit_quantum_circuit=None)
        """
        Create a Qiskrypt's Quantum Circuit with
        the previously created Qiskrypt's Quantum and Classical Registers.
        """

        qiskrypt_quantum_circuit_pauli_y_gate_1_qubit \
            .apply_hadamard(0, 0)
        """
        Apply the Hadamard Gate/Operation to the given index for
        the single qubit of the given IBM Qiskit's Quantum Register (|0⟩ ↦ |+⟩).
        """

        qiskrypt_quantum_circuit_pauli_y_gate_1_qubit \
            .apply_pauli_y(0, 0)
        """
        Apply the Pauli-Y Gate/Operation to the given index for
        the single qubit of the given IBM Qiskit's Quantum Register
        (|+⟩ ↦ |Ψ⟩ = 1/sqrt(2)i × (-|0⟩ + |1⟩)).
        """

        qiskit_state_vector_backend = Aer.get_backend("statevector_simulator")
        """
        Getting the Aer Simulator Backend for the State Vector Representation
        (i.e., the quantum state represented as its state vector).
        """

        final_quantum_state_vector_state = \
            execute(qiskrypt_quantum_circuit_pauli_y_gate_1_qubit.qiskit_quantum_circuit,
                    qiskit_state_vector_backend).result().get_statevector()
        """
        Execute the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit
        and store the resulted quantum state represented in a final state vector.
        """

        assert_allclose(final_quantum_state_vector_state,
                        array([(0. - ((1. / sqrt(2.)) * 1.j)), (0. + ((1. / sqrt(2.)) * 1.j))]),
                        rtol=1e-7, atol=1e-7)
        """
        Perform the Assertion of all close values in the values of the quantum state,
        represented by its state vector describing the given qubit,
        after being applied the Pauli-Y Quantum Gate/Operation.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_12_apply_pauli_y(self):
        """
        Test Case 12#:

        - Apply the Pauli-Y Gate/Operation to a qubit of an IBM Qiskit's Quantum Register of
          the Qiskrypt's Quantum Register of a Qiskrypt's Quantum Circuit.

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Quantum Circuit is created with a Qiskrypt's Quantum Register,
           with 1 qubit initialized in the state |0⟩;
        2) It is applied the Pauli-X (Bit Flip/NOT) Gate/Operation to the 1st qubit, such that, |0⟩ ↦ |1⟩;
        3) It is applied the Hadamard Gate/Operation to the 1st qubit, such that, |1⟩ ↦ |-⟩;
        4) It is applied the Pauli-Y Gate/Operation to the 1st qubit, such that,
           |-⟩ ↦ |Ψ⟩ = 1/sqrt(2) × (-|0⟩ + |1⟩);

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        num_qubits = num_bits = 1
        """
        Set the number of qubits and bits, for Quantum and Classical Registers, respectively.
        """

        qiskrypt_quantum_register_pauli_y_gate_1_qubit = \
            QiskryptQuantumRegister("qu_reg_12", num_qubits)
        """
        Create a Qiskrypt's Quantum Register with 1 qubit.
        """

        qiskrypt_classical_register_pauli_y_gate_1_qubit = \
            QiskryptClassicalRegister("cl_reg_12", num_bits)
        """
        Create a Qiskrypt's Classical Register with 1 bit.
        """

        qiskrypt_quantum_circuit_pauli_y_gate_1_qubit = \
            QiskryptQuantumCircuit("qu_circ_12",
                                   qiskrypt_quantum_registers=[qiskrypt_quantum_register_pauli_y_gate_1_qubit],
                                   qiskrypt_fully_quantum_registers=None,
                                   qiskrypt_semi_quantum_registers=None,
                                   qiskrypt_ancilla_quantum_registers=None,
                                   qiskrypt_ancilla_fully_quantum_registers=None,
                                   qiskrypt_ancilla_semi_quantum_registers=None,
                                   qiskrypt_classical_registers=[qiskrypt_classical_register_pauli_y_gate_1_qubit],
                                   global_phase=0, qiskit_quantum_circuit=None)
        """
        Create a Qiskrypt's Quantum Circuit with
        the previously created Qiskrypt's Quantum and Classical Registers.
        """

        qiskrypt_quantum_circuit_pauli_y_gate_1_qubit \
            .apply_pauli_x(0, 0)
        """
        Apply the Pauli-X (Bit Flip/NOT) Gate/Operation to the given index for
        the single qubit of the given IBM Qiskit's Quantum Register (|0⟩ ↦ |1⟩).
        """

        qiskrypt_quantum_circuit_pauli_y_gate_1_qubit \
            .apply_hadamard(0, 0)
        """
        Apply the Hadamard Gate/Operation to the given index for
        the single qubit of the given IBM Qiskit's Quantum Register (|1⟩ ↦ |-⟩).
        """

        qiskrypt_quantum_circuit_pauli_y_gate_1_qubit \
            .apply_pauli_y(0, 0)
        """
        Apply the Pauli-Y Gate/Operation to the given index for
        the single qubit of the given IBM Qiskit's Quantum Register
        (|-⟩ ↦ |Ψ⟩ = 1/sqrt(2)i × (|0⟩ + |1⟩)).
        """

        qiskit_state_vector_backend = Aer.get_backend("statevector_simulator")
        """
        Getting the Aer Simulator Backend for the State Vector Representation
        (i.e., the quantum state represented as its state vector).
        """

        final_quantum_state_vector_state = \
            execute(qiskrypt_quantum_circuit_pauli_y_gate_1_qubit.qiskit_quantum_circuit,
                    qiskit_state_vector_backend).result().get_statevector()
        """
        Execute the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit
        and store the resulted quantum state represented in a final state vector.
        """

        assert_allclose(final_quantum_state_vector_state,
                        array([(0. + ((1. / sqrt(2.)) * 1.j)), (0. + ((1. / sqrt(2.)) * 1.j))]),
                        rtol=1e-7, atol=1e-7)
        """
        Perform the Assertion of all close values in the values of the quantum state,
        represented by its state vector describing the given qubit,
        after being applied the Pauli-Y Quantum Gate/Operation.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)


if __name__ == "__main__":
    """
    The Main Method for the Unitary Test.
    """

    creation_qiskrypt_quantum_circuit_test_cases = \
        TestLoader().loadTestsFromTestCase(CreationQiskryptQuantumCircuitTests)
    """
    Load the Test Cases from the Unitary Tests for the creation of a Qiskrypt's Quantum Circuit.
    """

    other_basic_and_fundamental_methods_of_qiskrypt_quantum_circuit_test_cases = \
        TestLoader().loadTestsFromTestCase(OtherBasicAndFundamentalMethodsOfQiskryptQuantumCircuitTests)
    """
    Load the Test Cases from the Unitary Tests for other basic and fundamental methods of
    a Qiskrypt's Quantum Circuit.
    """

    creation_qiskrypt_quantum_circuit_test_suite = \
        TestSuite([creation_qiskrypt_quantum_circuit_test_cases,
                   other_basic_and_fundamental_methods_of_qiskrypt_quantum_circuit_test_cases])
    """
    Load the Test Suite with all the Test Cases for the Qiskrypt's Quantum Circuit.
    """
