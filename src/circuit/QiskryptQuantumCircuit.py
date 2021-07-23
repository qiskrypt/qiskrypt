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

from __future__ import annotations

"""
Import the annotations for Python
(must be imported at the beginning of the source-code).
"""

"""
Import required Libraries and Packages.
"""

from typing import Tuple
"""
Import Tuple from Typing built-in Module of Python.
"""

from math import pi, radians
"""
Import the pi constant and the function to convert degrees to radians from Math.
"""

from numpy import sqrt, exp, zeros
"""
Import the function to compute the Squared Root,
the Exponential and a matrix of Zeros from NumPy.
"""

from qiskit import QuantumCircuit
"""
Import Quantum Circuit from IBM's Qiskit.
"""

from qiskit.quantum_info.operators import Operator
"""
Import Operator of the Quantum_Info.Operators Module from IBM's Qiskit.
"""

from qiskit.circuit.library import GMS, Diagonal
"""
Import the Global Mølmer-Sørensen (GMS) and the Diagonal Quantum Gates/Operations of
the Circuit.Library Module from IBM's Qiskit.
"""

from src.circuit.registers.quantum.QiskryptQuantumRegister \
    import QiskryptQuantumRegister
"""
Import Qiskrypt's Quantum Register of
the Src.Circuit.Registers.Quantum.QiskryptQuantumRegister Module from Qiskrypt.
"""

from src.circuit.registers.quantum.fully_quantum.QiskryptFullyQuantumRegister \
    import QiskryptFullyQuantumRegister
"""
Import Qiskrypt's Fully-Quantum Register of
the Src.Circuit.Registers.Quantum.Fully_Quantum.QiskryptFullyQuantumRegister Module from Qiskrypt.
"""

from src.circuit.registers.quantum.semi_quantum.QiskryptSemiQuantumRegister \
    import QiskryptSemiQuantumRegister
"""
Import Qiskrypt's Semi-Quantum Register of
the Src.Circuit.Registers.Quantum.Semi_Quantum.QiskryptSemiQuantumRegister Module from Qiskrypt.
"""

from src.circuit.registers.quantum.QiskryptAncillaQuantumRegister \
    import QiskryptAncillaQuantumRegister
"""
Import Qiskrypt's Ancilla Quantum Register of
the Src.Circuit.Registers.Quantum.QiskryptAncillaQuantumRegister Module from Qiskrypt.
"""

from src.circuit.registers.quantum.fully_quantum.QiskryptAncillaFullyQuantumRegister \
    import QiskryptAncillaFullyQuantumRegister
"""
Import Qiskrypt's Ancilla Fully-Quantum Register of
the Src.Circuit.Registers.Quantum.Fully_Quantum.QiskryptAncillaFullyQuantumRegister Module from Qiskrypt.
"""

from src.circuit.registers.quantum.semi_quantum.QiskryptAncillaSemiQuantumRegister \
    import QiskryptAncillaSemiQuantumRegister
"""
Import Qiskrypt's Ancilla Semi-Quantum Register of
the Src.Circuit.Registers.Quantum.Semi_Quantum.QiskryptAncillaSemiQuantumRegister Module from Qiskrypt.
"""

from src.circuit.registers.classical.QiskryptClassicalRegister import QiskryptClassicalRegister
"""
Import Qiskrypt's Classical Register of
the Src.Circuit.Registers.Classical.QiskryptClassicalRegister Module from Qiskrypt.
"""

from src.circuit.exception.QiskryptQuantumCircuitException \
    import QiskryptQuantumCircuitUnsupportedTypeRegistersError
"""
Import the Unsupported Type of Registers Error for the Qiskrypt's Quantum Circuit.
"""

from src.circuit.exception.QiskryptQuantumCircuitException \
    import QiskryptQuantumCircuitInvalidQiskitQuantumRegisterIndexGivenError
"""
Import the Invalid IBM Qiskit's Quantum Register Index Given Error for the Qiskrypt's Quantum Circuit.
"""

from src.circuit.exception.QiskryptQuantumCircuitException \
    import QiskryptQuantumCircuitInvalidQubitIndexGivenError
"""
Import the Invalid Qubit Index Given Error for the Qiskrypt's Quantum Circuit.
"""

from src.circuit.registers.quantum.semi_quantum.exception.QiskryptSemiQuantumRegisterException \
    import QiskryptSemiQuantumRegisterUnsupportedOperationError
"""
Import the Unsupported Operation for 
"""

from src.circuit.exception.QiskryptQuantumCircuitException \
    import QiskryptQuantumCircuitInvalidQiskitClassicalRegisterIndexGivenError
"""
Import the Invalid IBM Qiskit's Classical Register Index Given Error for the Qiskrypt's Quantum Circuit.
"""

from src.circuit.exception.QiskryptQuantumCircuitException \
    import QiskryptQuantumCircuitInvalidBitIndexGivenError
"""
Import the Invalid Bit Index Given Error for the Qiskrypt's Quantum Circuit.
"""

from src.circuit.exception.QiskryptQuantumCircuitException \
    import QiskryptQuantumCircuitRegisterNotFoundError
"""
Import the Register Not Found Error for the Qiskrypt's Quantum Circuit.
"""

from src.circuit.exception.QiskryptQuantumCircuitException \
    import QiskryptQuantumCircuitNumQuantumRegistersAndNumClassicalRegistersAreNotEqualForOperationOrMeasurementError
"""
Import the Number of Quantum Registers and Number of Classical Registers Are Not Equal for
Operation or Measurement Error for the Qiskrypt's Quantum Circuit.
"""

from src.circuit.exception.QiskryptQuantumCircuitException \
    import QiskryptQuantumCircuitNumQubitsAndNumBitsAreNotEqualForOperationOrMeasurementError
"""
Import the Number of Qubits and Number of Bits Are Not Equal for Operation or Measurement Error for
the Qiskrypt's Quantum Circuit.
"""

from src.circuit.exception.QiskryptQuantumCircuitException \
    import QiskryptQuantumCircuitListDoNotRepresentASquareUnitaryMatrixOperatorError
"""
Import the List Do Not Represent a Square Unitary Matrix Operator Error for
the Qiskrypt's Quantum Circuit.
"""


class QiskryptQuantumCircuit:
    """
    Class for the Qiskrypt's Quantum Circuit.
    """

    def __init__(self, name="qu_circ",
                 qiskrypt_quantum_registers=None,
                 qiskrypt_fully_quantum_registers=None,
                 qiskrypt_semi_quantum_registers=None,
                 qiskrypt_ancilla_quantum_registers=None,
                 qiskrypt_ancilla_fully_quantum_registers=None,
                 qiskrypt_ancilla_semi_quantum_registers=None,
                 qiskrypt_classical_registers=None,
                 global_phase=0, qiskit_quantum_circuit=None):
        """
        :param name: the name for the Qiskrypt's Quantum Circuit.
        :param qiskrypt_quantum_registers: the Qiskrypt's Quantum Registers for the Qiskrypt's Quantum Circuit.
        :param qiskrypt_fully_quantum_registers: the Qiskrypt's Fully-Quantum Registers for the Qiskrypt's Quantum Circuit.
        :param qiskrypt_semi_quantum_registers: the Qiskrypt's Semi-Quantum Registers for the Qiskrypt's Quantum Circuit.
        :param qiskrypt_ancilla_quantum_registers: the Qiskrypt's Ancilla Quantum Registers for the Qiskrypt's Quantum Circuit.
        :param qiskrypt_ancilla_fully_quantum_registers: the Qiskrypt's Ancilla Fully-Quantum Registers for the Qiskrypt's Quantum Circuit.
        :param qiskrypt_ancilla_semi_quantum_registers: the Qiskrypt's Ancilla Semi-Quantum Registers for the Qiskrypt's Quantum Circuit.
        :param qiskrypt_classical_registers: the Qiskrypt's Classical Registers for the Qiskrypt's Quantum Circuit.
        :param global_phase: the global phase for the Qiskrypt's Quantum Circuit.
        :param qiskit_quantum_circuit: the IBM's Qiskit Quantum Circuit.
        """

        self.name = name
        """
        Set the name of the Qiskrypt's Quantum Circuit.
        """

        if qiskit_quantum_circuit is None:
            """
            If there is no given any IBM's Quantum Circuit, it will be created a new one,
            according to the given Qiskrypt's Quantum, Fully-Quantum, Semi-Quantum,
            Ancilla Quantum, Ancilla Fully-Quantum, Ancilla Semi-Quantum and
            Classical Registers.
            """

            if (qiskrypt_quantum_registers is not None) and \
                    (qiskrypt_fully_quantum_registers is None) and \
                    (qiskrypt_semi_quantum_registers is None) and \
                    (qiskrypt_ancilla_quantum_registers is None) and \
                    (qiskrypt_ancilla_fully_quantum_registers is None) and \
                    (qiskrypt_ancilla_semi_quantum_registers is None) and \
                    (qiskrypt_classical_registers is None):
                """
                If the Qiskrypt's Quantum Registers given as arguments are not None,
                but both the Qiskrypt's Fully-Quantum, Semi-Quantum,
                Ancilla Quantum, Ancilla Fully-Quantum, Ancilla Semi-Quantum and Classical Registers are None
                (i.e., a Qiskrypt's Quantum Circuit equivalent to a single Quantum Memory).
                """

                if isinstance(qiskrypt_quantum_registers, list):
                    """
                    If the Qiskrypt's Quantum Registers are lists.
                    """

                    for quantum_register in qiskrypt_quantum_registers:
                        """
                        For each supposed Qiskrypt's Quantum Register in the list of the Qiskrypt's Quantum Registers.
                        """

                        if not (isinstance(quantum_register, QiskryptQuantumRegister)):
                            """
                            If the current supposed Qiskrypt's Quantum Register is not an actual Qiskrypt's Quantum Register.
                            """

                            QiskryptQuantumRegister.raise_not_quantum_register_error()
                            """
                            Return/Raise a Not a Quantum Register Error for the Qiskrypt's Quantum Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    self.qiskrypt_quantum_registers = qiskrypt_quantum_registers
                    """
                    Set the Qiskrypt's Quantum Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskrypt_fully_quantum_registers = None
                    """
                    Set the Qiskrypt's Fully-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_semi_quantum_registers = None
                    """
                    Set the Qiskrypt's Semi-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_ancilla_quantum_registers = None
                    """
                    Set the Qiskrypt's Ancilla Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_ancilla_fully_quantum_registers = None
                    """
                    Set the Qiskrypt's Ancilla Fully-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_ancilla_semi_quantum_registers = None
                    """
                    Set the Qiskrypt's Ancilla Semi-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_classical_registers = None
                    """
                    Set the Qiskrypt's Classical Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.global_phase = global_phase
                    """
                    Set the global phase of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskit_quantum_circuit = \
                        QuantumCircuit(*[quantum_register.get_qiskit_quantum_register() for quantum_register in self.qiskrypt_quantum_registers],
                                       name=name, global_phase=global_phase)
                    """
                    Set the IBM's Qiskit Quantum Circuit of the Qiskrypt's Quantum Circuit.
                    """

                else:
                    """
                    If the Qiskrypt's Quantum Registers are not lists.
                    """

                    """
                    Raise an Unsupported Type of Registers Error for the Qiskrypt's Quantum Circuit.
                    """
                    self.raise_unsupported_type_registers_error()

            elif (qiskrypt_quantum_registers is None) and \
                    (qiskrypt_fully_quantum_registers is not None) and \
                    (qiskrypt_semi_quantum_registers is None) and \
                    (qiskrypt_ancilla_quantum_registers is None) and \
                    (qiskrypt_ancilla_fully_quantum_registers is None) and \
                    (qiskrypt_ancilla_semi_quantum_registers is None) and \
                    (qiskrypt_classical_registers is None):
                """
                If the Qiskrypt's Fully-Quantum Registers given as arguments are not None,
                but both the Qiskrypt's Quantum, Semi-Quantum,
                Ancilla Quantum, Ancilla Fully-Quantum, Ancilla Semi-Quantum and Classical Registers are None
                (i.e., a Qiskrypt's Quantum Circuit equivalent to a single Fully-Quantum Memory).
                """

                if isinstance(qiskrypt_fully_quantum_registers, list):
                    """
                    If the Qiskrypt's Fully-Quantum Registers are lists.
                    """

                    for fully_quantum_register in qiskrypt_fully_quantum_registers:
                        """
                        For each supposed Qiskrypt's Fully-Quantum Register in the list of the Qiskrypt's Fully-Quantum Registers.
                        """

                        if not (isinstance(fully_quantum_register, QiskryptFullyQuantumRegister)):
                            """
                            If the current supposed Qiskrypt's Fully-Quantum Register is not an actual Qiskrypt's Fully-Quantum Register.
                            """

                            QiskryptFullyQuantumRegister.raise_not_fully_quantum_register_error()
                            """
                            Return/Raise a Not a Fully-Quantum Register Error for the Qiskrypt's Fully-Quantum Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    self.qiskrypt_quantum_registers = None
                    """
                    Set the Qiskrypt's Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_fully_quantum_registers = qiskrypt_fully_quantum_registers
                    """
                    Set the Qiskrypt's Fully-Quantum Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskrypt_semi_quantum_registers = None
                    """
                    Set the Qiskrypt's Semi-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_ancilla_quantum_registers = None
                    """
                    Set the Qiskrypt's Ancilla Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_ancilla_fully_quantum_registers = None
                    """
                    Set the Qiskrypt's Ancilla Fully-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_ancilla_semi_quantum_registers = None
                    """
                    Set the Qiskrypt's Ancilla Semi-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_classical_registers = None
                    """
                    Set the Qiskrypt's Classical Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.global_phase = global_phase
                    """
                    Set the global phase of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskit_quantum_circuit = \
                        QuantumCircuit(
                            *[fully_quantum_register.get_qiskit_fully_quantum_register() for fully_quantum_register in
                              self.qiskrypt_fully_quantum_registers],
                            name=name, global_phase=global_phase)
                    """
                    Set the IBM's Qiskit Quantum Circuit of the Qiskrypt's Quantum Circuit.
                    """

                else:
                    """
                    If the Qiskrypt's Fully-Quantum Registers are not lists.
                    """

                    """
                    Raise an Unsupported Type of Registers Error for the Qiskrypt's Quantum Circuit.
                    """
                    self.raise_unsupported_type_registers_error()

            elif (qiskrypt_quantum_registers is None) and (qiskrypt_fully_quantum_registers is None) and (
                    qiskrypt_semi_quantum_registers is not None) and \
                    (qiskrypt_ancilla_quantum_registers is None) and (qiskrypt_ancilla_fully_quantum_registers is None) and (
                    qiskrypt_ancilla_semi_quantum_registers is None) and \
                    (qiskrypt_classical_registers is None):
                """
                If the Qiskrypt's Semi-Quantum Registers given as arguments are not None,
                but both the Qiskrypt's Quantum, Fully-Quantum,
                Ancilla Quantum, Ancilla Fully-Quantum, Ancilla Semi-Quantum and Classical Registers are None
                (i.e., a Qiskrypt's Quantum Circuit equivalent to a single Semi-Quantum Memory).
                """

                if isinstance(qiskrypt_semi_quantum_registers, list):
                    """
                    If the Qiskrypt's Semi-Quantum Registers are lists.
                    """

                    for semi_quantum_register in qiskrypt_semi_quantum_registers:
                        """
                        For each supposed Qiskrypt's Semi-Quantum Register in the list of the Qiskrypt's Semi-Quantum Registers.
                        """

                        if not (isinstance(semi_quantum_register, QiskryptSemiQuantumRegister)):
                            """
                            If the current supposed Qiskrypt's Semi-Quantum Register is not an actual Qiskrypt's Semi-Quantum Register.
                            """

                            QiskryptSemiQuantumRegister.raise_not_semi_quantum_register_error()
                            """
                            Return/Raise a Not a Semi-Quantum Register Error for the Qiskrypt's Semi-Quantum Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    self.qiskrypt_quantum_registers = None
                    """
                    Set the Qiskrypt's Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_fully_quantum_registers = None
                    """
                    Set the Qiskrypt's Fully-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_semi_quantum_registers = qiskrypt_semi_quantum_registers
                    """
                    Set the Qiskrypt's Semi-Quantum Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskrypt_ancilla_quantum_registers = None
                    """
                    Set the Qiskrypt's Ancilla Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_ancilla_fully_quantum_registers = None
                    """
                    Set the Qiskrypt's Ancilla Fully-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_ancilla_semi_quantum_registers = None
                    """
                    Set the Qiskrypt's Ancilla Semi-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_classical_registers = None
                    """
                    Set the Qiskrypt's Classical Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.global_phase = global_phase
                    """
                    Set the global phase of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskit_quantum_circuit = \
                        QuantumCircuit(*[semi_quantum_register.get_qiskit_semi_quantum_register() for semi_quantum_register in
                                         self.qiskrypt_semi_quantum_registers],
                                       name=name, global_phase=global_phase)
                    """
                    Set the IBM's Qiskit Quantum Circuit of the Qiskrypt's Quantum Circuit.
                    """

                else:
                    """
                    If the Qiskrypt's Fully-Quantum Registers are not lists.
                    """

                    """
                    Raise an Unsupported Type of Registers Error for the Qiskrypt's Quantum Circuit.
                    """
                    self.raise_unsupported_type_registers_error()

            elif (qiskrypt_quantum_registers is None) and (qiskrypt_fully_quantum_registers is None) and (
                    qiskrypt_semi_quantum_registers is None) and \
                    (qiskrypt_ancilla_quantum_registers is not None) and (qiskrypt_ancilla_fully_quantum_registers is None) and (
                    qiskrypt_ancilla_semi_quantum_registers is None) and \
                    (qiskrypt_classical_registers is None):
                """
                If the Qiskrypt's Ancilla Quantum Registers given as arguments are not None,
                but both the Qiskrypt's Quantum, Fully-Quantum, Semi-Quantum,
                Ancilla Fully-Quantum, Ancilla Semi-Quantum and Classical Registers are None
                (i.e., a Qiskrypt's Quantum Circuit equivalent to a single Ancilla Quantum Memory).
                """

                if isinstance(qiskrypt_ancilla_quantum_registers, list):
                    """
                    If the Qiskrypt's Ancilla Quantum Registers are lists.
                    """

                    for ancilla_quantum_register in qiskrypt_ancilla_quantum_registers:
                        """
                        For each supposed Qiskrypt's Ancilla Quantum Register in the list of the Qiskrypt's Ancilla Quantum Registers.
                        """

                        if not (isinstance(ancilla_quantum_register, QiskryptAncillaQuantumRegister)):
                            """
                            If the current supposed Qiskrypt's Ancilla Quantum Register is not an actual Qiskrypt's Ancilla Quantum Register.
                            """

                            QiskryptAncillaQuantumRegister.raise_not_ancilla_quantum_register_error()
                            """
                            Return/Raise a Not an Ancilla Quantum Register Error for the Qiskrypt's Ancilla Quantum Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    self.qiskrypt_quantum_registers = None
                    """
                    Set the Qiskrypt's Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_fully_quantum_registers = None
                    """
                    Set the Qiskrypt's Fully-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_semi_quantum_registers = None
                    """
                    Set the Qiskrypt's Semi-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_ancilla_quantum_registers = qiskrypt_ancilla_quantum_registers
                    """
                    Set the Qiskrypt's Ancilla Quantum Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskrypt_ancilla_fully_quantum_registers = None
                    """
                    Set the Qiskrypt's Ancilla Fully-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_ancilla_semi_quantum_registers = None
                    """
                    Set the Qiskrypt's Ancilla Semi-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_classical_registers = None
                    """
                    Set the Qiskrypt's Classical Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.global_phase = global_phase
                    """
                    Set the global phase of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskit_quantum_circuit = \
                        QuantumCircuit(
                            *[ancilla_quantum_register.get_qiskit_ancilla_quantum_register() for ancilla_quantum_register in
                              self.qiskrypt_ancilla_quantum_registers],
                            name=name, global_phase=global_phase)
                    """
                    Set the IBM's Qiskit Quantum Circuit of the Qiskrypt's Quantum Circuit.
                    """

                else:
                    """
                    If the Qiskrypt's Ancilla Quantum Registers are not lists.
                    """

                    """
                    Raise an Unsupported Type of Registers Error for the Qiskrypt's Quantum Circuit.
                    """
                    self.raise_unsupported_type_registers_error()

            elif (qiskrypt_quantum_registers is None) and (qiskrypt_fully_quantum_registers is None) and (
                    qiskrypt_semi_quantum_registers is None) and \
                    (qiskrypt_ancilla_quantum_registers is None) and (qiskrypt_ancilla_fully_quantum_registers is not None) and (
                    qiskrypt_ancilla_semi_quantum_registers is None) and \
                    (qiskrypt_classical_registers is None):
                """
                If the Qiskrypt's Ancilla Fully-Quantum Registers given as arguments are not None,
                but both the Qiskrypt's Quantum, Fully-Quantum, Semi-Quantum,
                Ancilla Quantum, Ancilla Semi-Quantum and Classical Registers are None
                (i.e., a Qiskrypt's Quantum Circuit equivalent to a single Ancilla Fully-Quantum Memory).
                """

                if isinstance(qiskrypt_ancilla_fully_quantum_registers, list):
                    """
                    If the Qiskrypt's Ancilla Fully-Quantum Registers are lists.
                    """

                    for ancilla_fully_quantum_register in qiskrypt_ancilla_fully_quantum_registers:
                        """
                        For each supposed Qiskrypt's Ancilla Fully-Quantum Register in the list of the Qiskrypt's Ancilla Fully-Quantum Registers.
                        """

                        if not (isinstance(ancilla_fully_quantum_register, QiskryptAncillaFullyQuantumRegister)):
                            """
                            If the current supposed Qiskrypt's Ancilla Fully-Quantum Register is not an actual Qiskrypt's Ancilla Fully-Quantum Register.
                            """

                            QiskryptAncillaFullyQuantumRegister.raise_not_ancilla_fully_quantum_register_error()
                            """
                            Return/Raise a Not an Ancilla Fully-Quantum Register Error for the Qiskrypt's Ancilla Fully-Quantum Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    self.qiskrypt_quantum_registers = None
                    """
                    Set the Qiskrypt's Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_fully_quantum_registers = None
                    """
                    Set the Qiskrypt's Fully-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_semi_quantum_registers = None
                    """
                    Set the Qiskrypt's Semi-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_ancilla_quantum_registers = None
                    """
                    Set the Qiskrypt's Ancilla Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_ancilla_fully_quantum_registers = qiskrypt_ancilla_fully_quantum_registers
                    """
                    Set the Qiskrypt's Ancilla Fully-Quantum Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskrypt_ancilla_semi_quantum_registers = None
                    """
                    Set the Qiskrypt's Ancilla Semi-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_classical_registers = None
                    """
                    Set the Qiskrypt's Classical Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.global_phase = global_phase
                    """
                    Set the global phase of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskit_quantum_circuit = \
                        QuantumCircuit(*[ancilla_fully_quantum_register.get_qiskit_ancilla_fully_quantum_register() for
                                         ancilla_fully_quantum_register in self.qiskrypt_ancilla_fully_quantum_registers],
                                       name=name, global_phase=global_phase)
                    """
                    Set the IBM's Qiskit Quantum Circuit of the Qiskrypt's Quantum Circuit.
                    """

                else:
                    """
                    If the Qiskrypt's Ancilla Fully-Quantum Registers are not lists.
                    """

                    """
                    Raise an Unsupported Type of Registers Error for the Qiskrypt's Quantum Circuit.
                    """
                    self.raise_unsupported_type_registers_error()

            elif (qiskrypt_quantum_registers is None) and (qiskrypt_fully_quantum_registers is None) and (
                    qiskrypt_semi_quantum_registers is None) and \
                    (qiskrypt_ancilla_quantum_registers is None) and (qiskrypt_ancilla_fully_quantum_registers is None) and (
                    qiskrypt_ancilla_semi_quantum_registers is not None) and \
                    (qiskrypt_classical_registers is None):
                """
                If the Qiskrypt's Ancilla Semi-Quantum Registers given as arguments are not None,
                but both the Qiskrypt's Quantum, Fully-Quantum, Semi-Quantum,
                Ancilla Quantum, Ancilla Fully-Quantum and Classical Registers are None
                (i.e., a Qiskrypt's Quantum Circuit equivalent to a single Ancilla Semi-Quantum Memory).
                """

                if isinstance(qiskrypt_ancilla_semi_quantum_registers, list):
                    """
                    If the Qiskrypt's Ancilla Semi-Quantum Registers are lists.
                    """

                    for ancilla_semi_quantum_register in qiskrypt_ancilla_semi_quantum_registers:
                        """
                        For each supposed Qiskrypt's Ancilla Semi-Quantum Register in the list of the Qiskrypt's Ancilla Semi-Quantum Registers.
                        """

                        if not (isinstance(ancilla_semi_quantum_register, QiskryptAncillaSemiQuantumRegister)):
                            """
                            If the current supposed Qiskrypt's Ancilla Semi-Quantum Register is not an actual Qiskrypt's Ancilla Semi-Quantum Register.
                            """

                            QiskryptAncillaSemiQuantumRegister.raise_not_ancilla_semi_quantum_register_error()
                            """
                            Return/Raise a Not an Ancilla Semi-Quantum Register Error for the Qiskrypt's Ancilla Semi-Quantum Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    self.qiskrypt_quantum_registers = None
                    """
                    Set the Qiskrypt's Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_fully_quantum_registers = None
                    """
                    Set the Qiskrypt's Fully-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_semi_quantum_registers = None
                    """
                    Set the Qiskrypt's Semi-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_ancilla_quantum_registers = None
                    """
                    Set the Qiskrypt's Ancilla Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_ancilla_fully_quantum_registers = None
                    """
                    Set the Qiskrypt's Ancilla Fully-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_ancilla_semi_quantum_registers = qiskrypt_ancilla_semi_quantum_registers
                    """
                    Set the Qiskrypt's Ancilla Semi-Quantum Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskrypt_classical_registers = None
                    """
                    Set the Qiskrypt's Classical Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.global_phase = global_phase
                    """
                    Set the global phase of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskit_quantum_circuit = \
                        QuantumCircuit(*[ancilla_semi_quantum_register.get_qiskit_ancilla_semi_quantum_register() for
                                         ancilla_semi_quantum_register in self.qiskrypt_ancilla_semi_quantum_registers],
                                       name=name, global_phase=global_phase)
                    """
                    Set the IBM's Qiskit Quantum Circuit of the Qiskrypt's Quantum Circuit.
                    """

                else:
                    """
                    If the Qiskrypt's Ancilla Semi-Quantum Registers are not lists.
                    """

                    """
                    Raise an Unsupported Type of Registers Error for the Qiskrypt's Quantum Circuit.
                    """
                    self.raise_unsupported_type_registers_error()

            elif (qiskrypt_quantum_registers is None) and (qiskrypt_fully_quantum_registers is None) and (
                    qiskrypt_semi_quantum_registers is None) and \
                    (qiskrypt_ancilla_quantum_registers is None) and (qiskrypt_ancilla_fully_quantum_registers is None) and (
                    qiskrypt_ancilla_semi_quantum_registers is None) and \
                    (qiskrypt_classical_registers is not None):
                """
                If the Qiskrypt's Classical Registers given as arguments are not None,
                but both the Qiskrypt's Quantum, Fully-Quantum, Semi-Quantum,
                Ancilla Quantum, Ancilla Fully-Quantum and Ancilla Semi-Quantum Registers are None
                (i.e., a Qiskrypt's Quantum Circuit equivalent to a single Classical Memory).
                """

                if isinstance(qiskrypt_classical_registers, list):
                    """
                    If the Qiskrypt's Classical Registers are lists.
                    """

                    for classical_register in qiskrypt_classical_registers:
                        """
                        For each supposed Qiskrypt's Classical Register in the list of the Qiskrypt's Classical Registers.
                        """

                        if not (isinstance(classical_register, QiskryptClassicalRegister)):
                            """
                            If the current supposed Qiskrypt's Classical Register is not an actual Qiskrypt's Classical Register.
                            """

                            QiskryptClassicalRegister.raise_not_classical_register_error()
                            """
                            Return/Raise a Not a Classical Register Error for the Qiskrypt's Classical Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    self.qiskrypt_quantum_registers = None
                    """
                    Set the Qiskrypt's Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_fully_quantum_registers = None
                    """
                    Set the Qiskrypt's Fully-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_semi_quantum_registers = None
                    """
                    Set the Qiskrypt's Semi-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_ancilla_quantum_registers = None
                    """
                    Set the Qiskrypt's Ancilla Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_ancilla_fully_quantum_registers = None
                    """
                    Set the Qiskrypt's Ancilla Fully-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_ancilla_semi_quantum_registers = None
                    """
                    Set the Qiskrypt's Ancilla Semi-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_classical_registers = qiskrypt_classical_registers
                    """
                    Set the Qiskrypt's Classical Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.global_phase = global_phase
                    """
                    Set the global phase of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskit_quantum_circuit = \
                        QuantumCircuit(*[classical_register.get_qiskit_classical_register() for classical_register in
                                         self.qiskrypt_classical_registers],
                                       name=name, global_phase=global_phase)
                    """
                    Set the IBM's Qiskit Quantum Circuit of the Qiskrypt's Quantum Circuit.
                    """

                else:
                    """
                    If the Qiskrypt's Classical Registers are not lists.
                    """

                    """
                    Raise an Unsupported Type of Registers Error for the Qiskrypt's Quantum Circuit.
                    """
                    self.raise_unsupported_type_registers_error()

            elif (qiskrypt_quantum_registers is not None) and (qiskrypt_fully_quantum_registers is None) and (
                    qiskrypt_semi_quantum_registers is None) and \
                    (qiskrypt_ancilla_quantum_registers is None) and (qiskrypt_ancilla_fully_quantum_registers is None) and (
                    qiskrypt_ancilla_semi_quantum_registers is None) and \
                    (qiskrypt_classical_registers is not None):
                """
                If the Qiskrypt's Quantum and Classical Registers given as arguments are not None,
                but both the Qiskrypt's Fully-Quantum, Semi-Quantum,
                Ancilla Quantum, Ancilla Fully-Quantum and Ancilla Semi-Quantum Registers are None
                (i.e., a Qiskrypt's Quantum Circuit equivalent to a hybrid Quantum/Classical Memory).
                """

                if (isinstance(qiskrypt_quantum_registers, list)) and (isinstance(qiskrypt_classical_registers, list)):
                    """
                    If the Qiskrypt's Quantum and Classical Registers are lists.
                    """

                    for quantum_register in qiskrypt_quantum_registers:
                        """
                        For each supposed Qiskrypt's Quantum Register in the list of the Qiskrypt's Quantum Registers.
                        """

                        if not (isinstance(quantum_register, QiskryptQuantumRegister)):
                            """
                            If the current supposed Qiskrypt's Quantum Register is not an actual Qiskrypt's Quantum Register.
                            """

                            QiskryptQuantumRegister.raise_not_quantum_register_error()
                            """
                            Return/Raise a Not a Quantum Register Error for the Qiskrypt's Quantum Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    for classical_register in qiskrypt_classical_registers:
                        """
                        For each supposed Qiskrypt's Classical Register in the list of the Qiskrypt's Classical Registers.
                        """

                        if not (isinstance(classical_register, QiskryptClassicalRegister)):
                            """
                            If the current supposed Qiskrypt's Classical Register is not an actual Qiskrypt's Classical Register.
                            """

                            QiskryptClassicalRegister.raise_not_classical_register_error()
                            """
                            Return/Raise a Not a Classical Register Error for the Qiskrypt's Classical Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    self.qiskrypt_quantum_registers = qiskrypt_quantum_registers
                    """
                    Set the Qiskrypt's Quantum Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskrypt_fully_quantum_registers = None
                    """
                    Set the Qiskrypt's Fully-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_semi_quantum_registers = None
                    """
                    Set the Qiskrypt's Semi-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_ancilla_quantum_registers = None
                    """
                    Set the Qiskrypt's Ancilla Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_ancilla_fully_quantum_registers = None
                    """
                    Set the Qiskrypt's Ancilla Fully-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_ancilla_semi_quantum_registers = None
                    """
                    Set the Qiskrypt's Ancilla Semi-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_classical_registers = qiskrypt_classical_registers
                    """
                    Set the Qiskrypt's Classical Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.global_phase = global_phase
                    """
                    Set the global phase of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskit_quantum_circuit = \
                        QuantumCircuit(
                            *[quantum_register.get_qiskit_quantum_register() for quantum_register in self.qiskrypt_quantum_registers],
                            *[classical_register.get_qiskit_classical_register() for classical_register in
                              self.qiskrypt_classical_registers],
                            name=name, global_phase=global_phase)
                    """
                    Set the IBM's Qiskit Quantum Circuit of the Qiskrypt's Quantum Circuit.
                    """

                else:
                    """
                    If the Qiskrypt's Quantum and Classical Registers are not lists.
                    """

                    """
                    Raise an Unsupported Type of Registers Error for the Qiskrypt's Quantum Circuit.
                    """
                    self.raise_unsupported_type_registers_error()

            elif (qiskrypt_quantum_registers is None) and (qiskrypt_fully_quantum_registers is not None) and (
                    qiskrypt_semi_quantum_registers is None) and \
                    (qiskrypt_ancilla_quantum_registers is None) and (qiskrypt_ancilla_fully_quantum_registers is None) and (
                    qiskrypt_ancilla_semi_quantum_registers is None) and \
                    (qiskrypt_classical_registers is not None):
                """
                If the Qiskrypt's Fully-Quantum and Classical Registers given as arguments are not None,
                but both the Qiskrypt's Quantum, Semi-Quantum,
                Ancilla Quantum, Ancilla Fully-Quantum and Ancilla Semi-Quantum Registers are None
                (i.e., a Qiskrypt's Quantum Circuit equivalent to a hybrid Fully-Quantum/Classical Memory).
                """

                if (isinstance(qiskrypt_fully_quantum_registers, list)) and (isinstance(qiskrypt_classical_registers, list)):
                    """
                    If the Qiskrypt's Fully-Quantum and Classical Registers are lists.
                    """

                    for fully_quantum_register in qiskrypt_fully_quantum_registers:
                        """
                        For each supposed Qiskrypt's Fully-Quantum Register in the list of the Qiskrypt's Fully-Quantum Registers.
                        """

                        if not (isinstance(fully_quantum_register, QiskryptFullyQuantumRegister)):
                            """
                            If the current supposed Qiskrypt's Fully-Quantum Register is not an actual Qiskrypt's Fully-Quantum Register.
                            """

                            QiskryptFullyQuantumRegister.raise_not_quantum_register_error()
                            """
                            Return/Raise a Not a Fully-Quantum Register Error for the Qiskrypt's Fully-Quantum Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    for classical_register in qiskrypt_classical_registers:
                        """
                        For each supposed Qiskrypt's Classical Register in the list of the Qiskrypt's Classical Registers.
                        """

                        if not (isinstance(classical_register, QiskryptClassicalRegister)):
                            """
                            If the current supposed Qiskrypt's Classical Register is not an actual Qiskrypt's Classical Register.
                            """

                            QiskryptClassicalRegister.raise_not_classical_register_error()
                            """
                            Return/Raise a Not a Classical Register Error for the Qiskrypt's Classical Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    self.qiskrypt_quantum_registers = None
                    """
                    Set the Qiskrypt's Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_fully_quantum_registers = qiskrypt_fully_quantum_registers
                    """
                    Set the Qiskrypt's Fully-Quantum Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskrypt_semi_quantum_registers = None
                    """
                    Set the Qiskrypt's Semi-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_ancilla_quantum_registers = None
                    """
                    Set the Qiskrypt's Ancilla Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_ancilla_fully_quantum_registers = None
                    """
                    Set the Qiskrypt's Ancilla Fully-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_ancilla_semi_quantum_registers = None
                    """
                    Set the Qiskrypt's Ancilla Semi-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_classical_registers = qiskrypt_classical_registers
                    """
                    Set the Qiskrypt's Classical Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.global_phase = global_phase
                    """
                    Set the global phase of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskit_quantum_circuit = \
                        QuantumCircuit(
                            *[fully_quantum_register.get_qiskit_fully_quantum_register() for fully_quantum_register in
                              self.qiskrypt_fully_quantum_registers],
                            *[classical_register.get_qiskit_classical_register() for classical_register in
                              self.qiskrypt_classical_registers],
                            name=name, global_phase=global_phase)
                    """
                    Set the IBM's Qiskit Quantum Circuit of the Qiskrypt's Quantum Circuit.
                    """

                else:
                    """
                    If the Qiskrypt's Fully-Quantum and Classical Registers are not lists.
                    """

                    """
                    Raise an Unsupported Type of Registers Error for the Qiskrypt's Quantum Circuit.
                    """
                    self.raise_unsupported_type_registers_error()

            elif (qiskrypt_quantum_registers is None) and (qiskrypt_fully_quantum_registers is None) and (
                    qiskrypt_semi_quantum_registers is not None) and \
                    (qiskrypt_ancilla_quantum_registers is None) and (qiskrypt_ancilla_fully_quantum_registers is None) and (
                    qiskrypt_ancilla_semi_quantum_registers is None) and \
                    (qiskrypt_classical_registers is not None):
                """
                If the Qiskrypt's Semi-Quantum and Classical Registers given as arguments are not None,
                but both the Qiskrypt's Quantum, Fully-Quantum,
                Ancilla Quantum, Ancilla Fully-Quantum and Ancilla Semi-Quantum Registers are None
                (i.e., a Qiskrypt's Quantum Circuit equivalent to a hybrid Semi-Quantum/Classical Memory).
                """

                if (isinstance(qiskrypt_semi_quantum_registers, list)) and (isinstance(qiskrypt_classical_registers, list)):
                    """
                    If the Qiskrypt's Semi-Quantum and Classical Registers are lists.
                    """

                    for semi_quantum_register in qiskrypt_semi_quantum_registers:
                        """
                        For each supposed Qiskrypt's Semi-Quantum Register in the list of the Qiskrypt's Semi-Quantum Registers.
                        """

                        if not (isinstance(semi_quantum_register, QiskryptSemiQuantumRegister)):
                            """
                            If the current supposed Qiskrypt's Semi-Quantum Register is not an actual Qiskrypt's Semi-Quantum Register.
                            """

                            QiskryptFullyQuantumRegister.raise_not_quantum_register_error()
                            """
                            Return/Raise a Not a Fully-Quantum Register Error for the Qiskrypt's Fully-Quantum Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    for classical_register in qiskrypt_classical_registers:
                        """
                        For each supposed Qiskrypt's Classical Register in the list of the Qiskrypt's Classical Registers.
                        """

                        if not (isinstance(classical_register, QiskryptClassicalRegister)):
                            """
                            If the current supposed Qiskrypt's Classical Register is not an actual Qiskrypt's Classical Register.
                            """

                            QiskryptClassicalRegister.raise_not_classical_register_error()
                            """
                            Return/Raise a Not a Classical Register Error for the Qiskrypt's Classical Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    self.qiskrypt_quantum_registers = None
                    """
                    Set the Qiskrypt's Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_fully_quantum_registers = None
                    """
                    Set the Qiskrypt's Fully-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_semi_quantum_registers = qiskrypt_semi_quantum_registers
                    """
                    Set the Qiskrypt's Semi-Quantum Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskrypt_ancilla_quantum_registers = None
                    """
                    Set the Qiskrypt's Ancilla Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_ancilla_fully_quantum_registers = None
                    """
                    Set the Qiskrypt's Ancilla Fully-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_ancilla_semi_quantum_registers = None
                    """
                    Set the Qiskrypt's Ancilla Semi-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_classical_registers = qiskrypt_classical_registers
                    """
                    Set the Qiskrypt's Classical Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.global_phase = global_phase
                    """
                    Set the global phase of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskit_quantum_circuit = \
                        QuantumCircuit(*[semi_quantum_register.get_qiskit_semi_quantum_register() for semi_quantum_register in
                                         self.qiskrypt_semi_quantum_registers],
                                       *[classical_register.get_qiskit_classical_register() for classical_register in
                                         self.qiskrypt_classical_registers],
                                       name=name, global_phase=global_phase)
                    """
                    Set the IBM's Qiskit Quantum Circuit of the Qiskrypt's Quantum Circuit.
                    """

                else:
                    """
                    If the Qiskrypt's Semi-Quantum and Classical Registers are not lists.
                    """

                    """
                    Raise an Unsupported Type of Registers Error for the Qiskrypt's Quantum Circuit.
                    """
                    self.raise_unsupported_type_registers_error()

            elif (qiskrypt_quantum_registers is None) and (qiskrypt_fully_quantum_registers is None) and (
                    qiskrypt_semi_quantum_registers is None) and \
                    (qiskrypt_ancilla_quantum_registers is not None) and (qiskrypt_ancilla_fully_quantum_registers is None) and (
                    qiskrypt_ancilla_semi_quantum_registers is None) and \
                    (qiskrypt_classical_registers is not None):
                """
                If the Qiskrypt's Ancilla Quantum and Classical Registers given as arguments are not None,
                but both the Qiskrypt's Quantum, Fully-Quantum, Semi-Quantum,
                Ancilla Fully-Quantum and Ancilla Semi-Quantum Registers are None
                (i.e., a Qiskrypt's Quantum Circuit equivalent to a hybrid Ancilla Quantum/Classical Memory).
                """

                if (isinstance(qiskrypt_ancilla_quantum_registers, list)) and (isinstance(qiskrypt_classical_registers, list)):
                    """
                    If the Qiskrypt's Ancilla Quantum and Classical Registers are lists.
                    """

                    for ancilla_quantum_register in qiskrypt_ancilla_quantum_registers:
                        """
                        For each supposed Qiskrypt's Ancilla Quantum Register in the list of the Qiskrypt's Ancilla Quantum Registers.
                        """

                        if not (isinstance(ancilla_quantum_register, QiskryptAncillaQuantumRegister)):
                            """
                            If the current supposed Qiskrypt's Ancilla Quantum Register is not an actual Qiskrypt's Ancilla Quantum Register.
                            """

                            QiskryptAncillaQuantumRegister.raise_not_ancilla_quantum_register_error()
                            """
                            Return/Raise a Not an Ancilla Quantum Register Error for the Qiskrypt's Ancilla Quantum Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    for classical_register in qiskrypt_classical_registers:
                        """
                        For each supposed Qiskrypt's Classical Register in the list of the Qiskrypt's Classical Registers.
                        """

                        if not (isinstance(classical_register, QiskryptClassicalRegister)):
                            """
                            If the current supposed Qiskrypt's Classical Register is not an actual Qiskrypt's Classical Register.
                            """

                            QiskryptClassicalRegister.raise_not_classical_register_error()
                            """
                            Return/Raise a Not a Classical Register Error for the Qiskrypt's Classical Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    self.qiskrypt_quantum_registers = None
                    """
                    Set the Qiskrypt's Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_fully_quantum_registers = None
                    """
                    Set the Qiskrypt's Fully-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_semi_quantum_registers = None
                    """
                    Set the Qiskrypt's Semi-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_ancilla_quantum_registers = qiskrypt_ancilla_quantum_registers
                    """
                    Set the Qiskrypt's Ancilla Quantum Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskrypt_ancilla_fully_quantum_registers = None
                    """
                    Set the Qiskrypt's Ancilla Fully-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_ancilla_semi_quantum_registers = None
                    """
                    Set the Qiskrypt's Ancilla Semi-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_classical_registers = qiskrypt_classical_registers
                    """
                    Set the Qiskrypt's Classical Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.global_phase = global_phase
                    """
                    Set the global phase of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskit_quantum_circuit = \
                        QuantumCircuit(
                            *[ancilla_quantum_register.get_qiskit_ancilla_quantum_register() for ancilla_quantum_register in
                              self.qiskrypt_ancilla_quantum_registers],
                            *[classical_register.get_qiskit_classical_register() for classical_register in
                              self.qiskrypt_classical_registers],
                            name=name, global_phase=global_phase)
                    """
                    Set the IBM's Qiskit Quantum Circuit of the Qiskrypt's Quantum Circuit.
                    """

                else:
                    """
                    If the Qiskrypt's Ancilla Quantum and Classical Registers are not lists.
                    """

                    """
                    Raise an Unsupported Type of Registers Error for the Qiskrypt's Quantum Circuit.
                    """
                    self.raise_unsupported_type_registers_error()

            elif (qiskrypt_quantum_registers is None) and (qiskrypt_fully_quantum_registers is None) and (
                    qiskrypt_semi_quantum_registers is None) and \
                    (qiskrypt_ancilla_quantum_registers is None) and (qiskrypt_ancilla_fully_quantum_registers is not None) and (
                    qiskrypt_ancilla_semi_quantum_registers is None) and \
                    (qiskrypt_classical_registers is not None):
                """
                If the Qiskrypt's Ancilla Fully-Quantum and Classical Registers given as arguments are not None,
                but both the Qiskrypt's Quantum, Fully-Quantum, Semi-Quantum,
                Ancilla Quantum and Ancilla Semi-Quantum Registers are None
                (i.e., a Qiskrypt's Quantum Circuit equivalent to a hybrid Ancilla Fully-Quantum/Classical Memory).
                """

                if (isinstance(qiskrypt_ancilla_fully_quantum_registers, list)) and (isinstance(qiskrypt_classical_registers, list)):
                    """
                    If the Qiskrypt's Ancilla Fully-Quantum and Classical Registers are lists.
                    """

                    for ancilla_fully_quantum_register in qiskrypt_ancilla_fully_quantum_registers:
                        """
                        For each supposed Qiskrypt's Ancilla Fully-Quantum Register in the list of the Qiskrypt's Ancilla Fully-Quantum Registers.
                        """

                        if not (isinstance(ancilla_fully_quantum_register, QiskryptAncillaFullyQuantumRegister)):
                            """
                            If the current supposed Qiskrypt's Ancilla Fully-Quantum Register is not an actual Qiskrypt's Ancilla Fully-Quantum Register.
                            """

                            QiskryptAncillaFullyQuantumRegister.raise_not_ancilla_fully_quantum_register_error()
                            """
                            Return/Raise a Not an Ancilla Fully-Quantum Register Error for the Qiskrypt's Ancilla Fully-Quantum Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    for classical_register in qiskrypt_classical_registers:
                        """
                        For each supposed Qiskrypt's Classical Register in the list of the Qiskrypt's Classical Registers.
                        """

                        if not (isinstance(classical_register, QiskryptClassicalRegister)):
                            """
                            If the current supposed Qiskrypt's Classical Register is not an actual Qiskrypt's Classical Register.
                            """

                            QiskryptClassicalRegister.raise_not_classical_register_error()
                            """
                            Return/Raise a Not a Classical Register Error for the Qiskrypt's Classical Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    self.qiskrypt_quantum_registers = None
                    """
                    Set the Qiskrypt's Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_fully_quantum_registers = None
                    """
                    Set the Qiskrypt's Fully-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_semi_quantum_registers = None
                    """
                    Set the Qiskrypt's Semi-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_ancilla_quantum_registers = None
                    """
                    Set the Qiskrypt's Ancilla Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_ancilla_fully_quantum_registers = qiskrypt_ancilla_fully_quantum_registers
                    """
                    Set the Qiskrypt's Ancilla Fully-Quantum Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskrypt_ancilla_semi_quantum_registers = None
                    """
                    Set the Qiskrypt's Ancilla Semi-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_classical_registers = qiskrypt_classical_registers
                    """
                    Set the Qiskrypt's Classical Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.global_phase = global_phase
                    """
                    Set the global phase of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskit_quantum_circuit = \
                        QuantumCircuit(*[ancilla_fully_quantum_register.get_qiskit_ancilla_fully_quantum_register() for
                                         ancilla_fully_quantum_register in self.qiskrypt_ancilla_fully_quantum_registers],
                                       *[classical_register.get_qiskit_classical_register() for classical_register in
                                         self.qiskrypt_classical_registers],
                                       name=name, global_phase=global_phase)
                    """
                    Set the IBM's Qiskit Quantum Circuit of the Qiskrypt's Quantum Circuit.
                    """

                else:
                    """
                    If the Qiskrypt's Ancilla Fully-Quantum and Classical Registers are not lists.
                    """

                    """
                    Raise an Unsupported Type of Registers Error for the Qiskrypt's Quantum Circuit.
                    """
                    self.raise_unsupported_type_registers_error()

            elif (qiskrypt_quantum_registers is None) and (qiskrypt_fully_quantum_registers is None) and (
                    qiskrypt_semi_quantum_registers is None) and \
                    (qiskrypt_ancilla_quantum_registers is None) and (qiskrypt_ancilla_fully_quantum_registers is None) and (
                    qiskrypt_ancilla_semi_quantum_registers is not None) and \
                    (qiskrypt_classical_registers is not None):
                """
                If the Qiskrypt's Ancilla Semi-Quantum and Classical Registers given as arguments are not None,
                but both the Qiskrypt's Quantum, Fully-Quantum, Semi-Quantum,
                Ancilla Quantum and Ancilla Fully-Quantum Registers are None
                (i.e., a Qiskrypt's Quantum Circuit equivalent to a hybrid Ancilla Semi-Quantum/Classical Memory).
                """

                if (isinstance(qiskrypt_ancilla_semi_quantum_registers, list)) and (isinstance(qiskrypt_classical_registers, list)):
                    """
                    If the Qiskrypt's Ancilla Semi-Quantum and Classical Registers are lists.
                    """

                    for ancilla_semi_quantum_register in qiskrypt_ancilla_semi_quantum_registers:
                        """
                        For each supposed Qiskrypt's Ancilla Semi-Quantum Register in the list of the Qiskrypt's Ancilla Semi-Quantum Registers.
                        """

                        if not (isinstance(ancilla_semi_quantum_register, QiskryptAncillaSemiQuantumRegister)):
                            """
                            If the current supposed Qiskrypt's Ancilla Semi-Quantum Register is not an actual Qiskrypt's Ancilla Semi-Quantum Register.
                            """

                            QiskryptAncillaSemiQuantumRegister.raise_not_ancilla_semi_quantum_register_error()
                            """
                            Return/Raise a Not an Ancilla Semi-Quantum Register Error for the Qiskrypt's Ancilla Semi-Quantum Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    for classical_register in qiskrypt_classical_registers:
                        """
                        For each supposed Qiskrypt's Classical Register in the list of the Qiskrypt's Classical Registers.
                        """

                        if not (isinstance(classical_register, QiskryptClassicalRegister)):
                            """
                            If the current supposed Qiskrypt's Classical Register is not an actual Qiskrypt's Classical Register.
                            """

                            QiskryptClassicalRegister.raise_not_classical_register_error()
                            """
                            Return/Raise a Not a Classical Register Error for the Qiskrypt's Classical Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    self.qiskrypt_quantum_registers = None
                    """
                    Set the Qiskrypt's Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_fully_quantum_registers = None
                    """
                    Set the Qiskrypt's Fully-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_semi_quantum_registers = None
                    """
                    Set the Qiskrypt's Semi-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_ancilla_quantum_registers = None
                    """
                    Set the Qiskrypt's Ancilla Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_ancilla_fully_quantum_registers = None
                    """
                    Set the Qiskrypt's Ancilla Fully-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_ancilla_semi_quantum_registers = qiskrypt_ancilla_semi_quantum_registers
                    """
                    Set the Qiskrypt's Ancilla Semi-Quantum Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskrypt_classical_registers = qiskrypt_classical_registers
                    """
                    Set the Qiskrypt's Classical Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.global_phase = global_phase
                    """
                    Set the global phase of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskit_quantum_circuit = \
                        QuantumCircuit(*[ancilla_semi_quantum_register.get_qiskit_ancilla_semi_quantum_register() for
                                         ancilla_semi_quantum_register in self.qiskrypt_ancilla_semi_quantum_registers],
                                       *[classical_register.get_qiskit_classical_register() for classical_register in
                                         self.qiskrypt_classical_registers],
                                       name=name, global_phase=global_phase)
                    """
                    Set the IBM's Qiskit Quantum Circuit of the Qiskrypt's Quantum Circuit.
                    """

                else:
                    """
                    If the Qiskrypt's Ancilla Semi-Quantum and Classical Registers are not lists.
                    """

                    """
                    Raise an Unsupported Type of Registers Error for the Qiskrypt's Quantum Circuit.
                    """
                    self.raise_unsupported_type_registers_error()

            elif (qiskrypt_quantum_registers is not None) and (qiskrypt_fully_quantum_registers is not None) and (
                    qiskrypt_semi_quantum_registers is None) and \
                    (qiskrypt_ancilla_quantum_registers is None) and (qiskrypt_ancilla_fully_quantum_registers is None) and (
                    qiskrypt_ancilla_semi_quantum_registers is None) and \
                    (qiskrypt_classical_registers is not None):
                """
                If the Qiskrypt's Quantum, Fully-Quantum and Classical Registers given as arguments are not None,
                but both the Qiskrypt's Semi-Quantum, Ancilla Quantum, Ancilla Fully-Quantum and Ancilla Semi-Quantum Registers are None
                (i.e., a Qiskrypt's Quantum Circuit equivalent to a hybrid Quantum/Fully-Quantum/Classical Memory).
                """

                if (isinstance(qiskrypt_quantum_registers, list)) and (isinstance(qiskrypt_fully_quantum_registers, list)) and (
                    isinstance(qiskrypt_classical_registers, list)):
                    """
                    If the Qiskrypt's Quantum, Fully-Quantum and Classical Registers are lists.
                    """

                    for quantum_register in qiskrypt_quantum_registers:
                        """
                        For each supposed Qiskrypt's Quantum Register in the list of the Qiskrypt's Quantum Registers.
                        """

                        if not (isinstance(quantum_register, QiskryptQuantumRegister)):
                            """
                            If the current supposed Qiskrypt's Quantum Register is not an actual Qiskrypt's Quantum Register.
                            """

                            QiskryptQuantumRegister.raise_not_quantum_register_error()
                            """
                            Return/Raise a Not a Quantum Register Error for the Qiskrypt's Quantum Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    for fully_quantum_register in qiskrypt_fully_quantum_registers:
                        """
                        For each supposed Qiskrypt's Fully-Quantum Register in the list of the Qiskrypt's Fully-Quantum Registers.
                        """

                        if not (isinstance(fully_quantum_register, QiskryptFullyQuantumRegister)):
                            """
                            If the current supposed Qiskrypt's Fully-Quantum Register is not an actual Qiskrypt's Fully-Quantum Register.
                            """

                            QiskryptFullyQuantumRegister.raise_not_fully_quantum_register_error()
                            """
                            Return/Raise a Not a Fully-Quantum Register Error for the Qiskrypt's Fully-Quantum Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    for classical_register in qiskrypt_classical_registers:
                        """
                        For each supposed Qiskrypt's Classical Register in the list of the Qiskrypt's Classical Registers.
                        """

                        if not (isinstance(classical_register, QiskryptClassicalRegister)):
                            """
                            If the current supposed Qiskrypt's Classical Register is not an actual Qiskrypt's Classical Register.
                            """

                            QiskryptClassicalRegister.raise_not_classical_register_error()
                            """
                            Return/Raise a Not a Classical Register Error for the Qiskrypt's Classical Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    self.qiskrypt_quantum_registers = qiskrypt_quantum_registers
                    """
                    Set the Qiskrypt's Quantum Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskrypt_fully_quantum_registers = qiskrypt_fully_quantum_registers
                    """
                    Set the Qiskrypt's Fully-Quantum Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskrypt_semi_quantum_registers = None
                    """
                    Set the Qiskrypt's Semi-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_ancilla_quantum_registers = None
                    """
                    Set the Qiskrypt's Ancilla Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_ancilla_fully_quantum_registers = None
                    """
                    Set the Qiskrypt's Ancilla Fully-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_ancilla_semi_quantum_registers = None
                    """
                    Set the Qiskrypt's Ancilla Semi-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_classical_registers = qiskrypt_classical_registers
                    """
                    Set the Qiskrypt's Classical Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.global_phase = global_phase
                    """
                    Set the global phase of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskit_quantum_circuit = \
                        QuantumCircuit(
                            *[quantum_register.get_qiskit_quantum_register() for quantum_register in self.qiskrypt_quantum_registers],
                            *[fully_quantum_register.get_qiskit_fully_quantum_register() for fully_quantum_register in
                              self.qiskrypt_fully_quantum_registers],
                            *[classical_register.get_qiskit_classical_register() for classical_register in
                              self.qiskrypt_classical_registers],
                            name=name, global_phase=global_phase)
                    """
                    Set the IBM's Qiskit Quantum Circuit of the Qiskrypt's Quantum Circuit.
                    """

                else:
                    """
                    If the Qiskrypt's Quantum, Fully-Quantum and Classical Registers are not lists.
                    """

                    """
                    Raise an Unsupported Type of Registers Error for the Qiskrypt's Quantum Circuit.
                    """
                    self.raise_unsupported_type_registers_error()

            elif (qiskrypt_quantum_registers is not None) and (qiskrypt_fully_quantum_registers is None) and (
                    qiskrypt_semi_quantum_registers is not None) and \
                    (qiskrypt_ancilla_quantum_registers is None) and (qiskrypt_ancilla_fully_quantum_registers is None) and (
                    qiskrypt_ancilla_semi_quantum_registers is None) and \
                    (qiskrypt_classical_registers is not None):
                """
                If the Qiskrypt's Quantum, Semi-Quantum and Classical Registers given as arguments are not None,
                but both the Qiskrypt's Fully-Quantum, Ancilla Quantum, Ancilla Fully-Quantum and Ancilla Semi-Quantum Registers are None
                (i.e., a Qiskrypt's Quantum Circuit equivalent to a hybrid Quantum/Semi-Quantum/Classical Memory).
                """

                if (isinstance(qiskrypt_quantum_registers, list)) and (isinstance(qiskrypt_semi_quantum_registers, list)) and (
                    isinstance(qiskrypt_classical_registers, list)):
                    """
                    If the Qiskrypt's Quantum, Semi-Quantum and Classical Registers are lists.
                    """

                    for quantum_register in qiskrypt_quantum_registers:
                        """
                        For each supposed Qiskrypt's Quantum Register in the list of the Qiskrypt's Quantum Registers.
                        """

                        if not (isinstance(quantum_register, QiskryptQuantumRegister)):
                            """
                            If the current supposed Qiskrypt's Quantum Register is not an actual Qiskrypt's Quantum Register.
                            """

                            QiskryptQuantumRegister.raise_not_quantum_register_error()
                            """
                            Return/Raise a Not a Quantum Register Error for the Qiskrypt's Quantum Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    for semi_quantum_register in qiskrypt_semi_quantum_registers:
                        """
                        For each supposed Qiskrypt's Semi-Quantum Register in the list of the Qiskrypt's Semi-Quantum Registers.
                        """

                        if not (isinstance(semi_quantum_register, QiskryptSemiQuantumRegister)):
                            """
                            If the current supposed Qiskrypt's Semi-Quantum Register is not an actual Qiskrypt's Semi-Quantum Register.
                            """

                            QiskryptSemiQuantumRegister.raise_not_semi_quantum_register_error()
                            """
                            Return/Raise a Not a Semi-Quantum Register Error for the Qiskrypt's Semi-Quantum Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    for classical_register in qiskrypt_classical_registers:
                        """
                        For each supposed Qiskrypt's Classical Register in the list of the Qiskrypt's Classical Registers.
                        """

                        if not (isinstance(classical_register, QiskryptClassicalRegister)):
                            """
                            If the current supposed Qiskrypt's Classical Register is not an actual Qiskrypt's Classical Register.
                            """

                            QiskryptClassicalRegister.raise_not_classical_register_error()
                            """
                            Return/Raise a Not a Classical Register Error for the Qiskrypt's Classical Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    self.qiskrypt_quantum_registers = qiskrypt_quantum_registers
                    """
                    Set the Qiskrypt's Quantum Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskrypt_fully_quantum_registers = None
                    """
                    Set the Qiskrypt's Fully-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_semi_quantum_registers = qiskrypt_semi_quantum_registers
                    """
                    Set the Qiskrypt's Semi-Quantum Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskrypt_ancilla_quantum_registers = None
                    """
                    Set the Qiskrypt's Ancilla Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_ancilla_fully_quantum_registers = None
                    """
                    Set the Qiskrypt's Ancilla Fully-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_ancilla_semi_quantum_registers = None
                    """
                    Set the Qiskrypt's Ancilla Semi-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_classical_registers = qiskrypt_classical_registers
                    """
                    Set the Qiskrypt's Classical Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.global_phase = global_phase
                    """
                    Set the global phase of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskit_quantum_circuit = \
                        QuantumCircuit(
                            *[quantum_register.get_qiskit_quantum_register() for quantum_register in self.qiskrypt_quantum_registers],
                            *[semi_quantum_register.get_qiskit_semi_quantum_register() for semi_quantum_register in
                              self.qiskrypt_semi_quantum_registers],
                            *[classical_register.get_qiskit_classical_register() for classical_register in
                              self.qiskrypt_classical_registers],
                            name=name, global_phase=global_phase)
                    """
                    Set the IBM's Qiskit Quantum Circuit of the Qiskrypt's Quantum Circuit.
                    """

                else:
                    """
                    If the Qiskrypt's Quantum, Semi-Quantum and Classical Registers are not lists.
                    """

                    """
                    Raise an Unsupported Type of Registers Error for the Qiskrypt's Quantum Circuit.
                    """
                    self.raise_unsupported_type_registers_error()

            elif (qiskrypt_quantum_registers is not None) and (qiskrypt_fully_quantum_registers is None) and (
                    qiskrypt_semi_quantum_registers is None) and \
                    (qiskrypt_ancilla_quantum_registers is not None) and (qiskrypt_ancilla_fully_quantum_registers is None) and (
                    qiskrypt_ancilla_semi_quantum_registers is None) and \
                    (qiskrypt_classical_registers is not None):
                """
                If the Qiskrypt's Quantum, Ancilla Quantum and Classical Registers given as arguments are not None,
                but both the Qiskrypt's Fully-Quantum, Semi-Quantum,
                Ancilla Fully-Quantum and Ancilla Semi-Quantum Registers are None
                (i.e., a Qiskrypt's Quantum Circuit equivalent to a hybrid Quantum/Ancilla Quantum/Classical Memory).
                """

                if (isinstance(qiskrypt_quantum_registers, list)) and (isinstance(qiskrypt_ancilla_quantum_registers, list)) and (isinstance(qiskrypt_classical_registers, list)):
                    """
                    If the Qiskrypt's Quantum, Ancilla Quantum and Classical Registers are lists.
                    """

                    for quantum_register in qiskrypt_quantum_registers:
                        """
                        For each supposed Qiskrypt's Quantum Register in the list of the Qiskrypt's Quantum Registers.
                        """

                        if not (isinstance(quantum_register, QiskryptQuantumRegister)):
                            """
                            If the current supposed Qiskrypt's Quantum Register is not an actual Qiskrypt's Quantum Register.
                            """

                            QiskryptQuantumRegister.raise_not_quantum_register_error()
                            """
                            Return/Raise a Not a Quantum Register Error for the Qiskrypt's Quantum Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    for ancilla_quantum_register in qiskrypt_ancilla_quantum_registers:
                        """
                        For each supposed Qiskrypt's Ancilla Quantum Register in the list of the Qiskrypt's Ancilla Quantum Registers.
                        """

                        if not (isinstance(ancilla_quantum_register, QiskryptAncillaQuantumRegister)):
                            """
                            If the current supposed Qiskrypt's Ancilla Quantum Register is not an actual Qiskrypt's Ancilla Quantum Register.
                            """

                            QiskryptAncillaQuantumRegister.raise_not_ancilla_quantum_register_error()
                            """
                            Return/Raise a Not a Ancilla Quantum Register Error for the Qiskrypt's Ancilla Quantum Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    for classical_register in qiskrypt_classical_registers:
                        """
                        For each supposed Qiskrypt's Classical Register in the list of the Qiskrypt's Classical Registers.
                        """

                        if not (isinstance(classical_register, QiskryptClassicalRegister)):
                            """
                            If the current supposed Qiskrypt's Classical Register is not an actual Qiskrypt's Classical Register.
                            """

                            QiskryptClassicalRegister.raise_not_classical_register_error()
                            """
                            Return/Raise a Not a Classical Register Error for the Qiskrypt's Classical Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    self.qiskrypt_quantum_registers = qiskrypt_quantum_registers
                    """
                    Set the Qiskrypt's Quantum Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskrypt_fully_quantum_registers = None
                    """
                    Set the Qiskrypt's Fully-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_semi_quantum_registers = None
                    """
                    Set the Qiskrypt's Semi-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_ancilla_quantum_registers = qiskrypt_ancilla_quantum_registers
                    """
                    Set the Qiskrypt's Ancilla Quantum Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskrypt_ancilla_fully_quantum_registers = None
                    """
                    Set the Qiskrypt's Ancilla Fully-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_ancilla_semi_quantum_registers = None
                    """
                    Set the Qiskrypt's Ancilla Semi-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_classical_registers = qiskrypt_classical_registers
                    """
                    Set the Qiskrypt's Classical Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.global_phase = global_phase
                    """
                    Set the global phase of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskit_quantum_circuit = \
                        QuantumCircuit(
                            *[quantum_register.get_qiskit_quantum_register() for quantum_register in self.qiskrypt_quantum_registers],
                            *[ancilla_quantum_register.get_qiskit_ancilla_quantum_register() for ancilla_quantum_register in
                              self.qiskrypt_ancilla_quantum_registers],
                            *[classical_register.get_qiskit_classical_register() for classical_register in
                              self.qiskrypt_classical_registers],
                            name=name, global_phase=global_phase)
                    """
                    Set the IBM's Qiskit Quantum Circuit of the Qiskrypt's Quantum Circuit.
                    """

                else:
                    """
                    If the Qiskrypt's Quantum, Ancilla Quantum and Classical Registers are not lists.
                    """

                    """
                    Raise an Unsupported Type of Registers Error for the Qiskrypt's Quantum Circuit.
                    """
                    self.raise_unsupported_type_registers_error()

            elif (qiskrypt_quantum_registers is not None) and (qiskrypt_fully_quantum_registers is None) and (
                    qiskrypt_semi_quantum_registers is None) and \
                    (qiskrypt_ancilla_quantum_registers is None) and (qiskrypt_ancilla_fully_quantum_registers is not None) and (
                    qiskrypt_ancilla_semi_quantum_registers is None) and \
                    (qiskrypt_classical_registers is not None):
                """
                If the Qiskrypt's Quantum, Ancilla Fully-Quantum and Classical Registers given as arguments are not None,
                but both the Qiskrypt's Fully-Quantum, Semi-Quantum,
                Ancilla Quantum and Ancilla Semi-Quantum Registers are None
                (i.e., a Qiskrypt's Quantum Circuit equivalent to a hybrid Quantum/Ancilla Fully-Quantum/Classical Memory).
                """

                if (isinstance(qiskrypt_quantum_registers, list)) and (isinstance(qiskrypt_ancilla_fully_quantum_registers, list)) and (
                    isinstance(qiskrypt_classical_registers, list)):
                    """
                    If the Qiskrypt's Quantum, Ancilla Fully-Quantum and Classical Registers are lists.
                    """

                    for quantum_register in qiskrypt_quantum_registers:
                        """
                        For each supposed Qiskrypt's Quantum Register in the list of the Qiskrypt's Quantum Registers.
                        """

                        if not (isinstance(quantum_register, QiskryptQuantumRegister)):
                            """
                            If the current supposed Qiskrypt's Quantum Register is not an actual Qiskrypt's Quantum Register.
                            """

                            QiskryptQuantumRegister.raise_not_quantum_register_error()
                            """
                            Return/Raise a Not a Quantum Register Error for the Qiskrypt's Quantum Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    for ancilla_fully_quantum_register in qiskrypt_ancilla_fully_quantum_registers:
                        """
                        For each supposed Qiskrypt's Ancilla Fully-Quantum Register in the list of the Qiskrypt's Ancilla Fully-Quantum Registers.
                        """

                        if not (isinstance(ancilla_fully_quantum_register, QiskryptAncillaFullyQuantumRegister)):
                            """
                            If the current supposed Qiskrypt's Ancilla Fully-Quantum Register is not an actual Qiskrypt's Ancilla Fully-Quantum Register.
                            """

                            QiskryptAncillaFullyQuantumRegister.raise_not_ancilla_fully_quantum_register_error()
                            """
                            Return/Raise a Not a Ancilla Fully-Quantum Register Error for the Qiskrypt's Ancilla Fully-Quantum Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    for classical_register in qiskrypt_classical_registers:
                        """
                        For each supposed Qiskrypt's Classical Register in the list of the Qiskrypt's Classical Registers.
                        """

                        if not (isinstance(classical_register, QiskryptClassicalRegister)):
                            """
                            If the current supposed Qiskrypt's Classical Register is not an actual Qiskrypt's Classical Register.
                            """

                            QiskryptClassicalRegister.raise_not_classical_register_error()
                            """
                            Return/Raise a Not a Classical Register Error for the Qiskrypt's Classical Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    self.qiskrypt_quantum_registers = qiskrypt_quantum_registers
                    """
                    Set the Qiskrypt's Quantum Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskrypt_fully_quantum_registers = None
                    """
                    Set the Qiskrypt's Fully-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_semi_quantum_registers = None
                    """
                    Set the Qiskrypt's Semi-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_ancilla_quantum_registers = None
                    """
                    Set the Qiskrypt's Ancilla Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_ancilla_fully_quantum_registers = qiskrypt_ancilla_fully_quantum_registers
                    """
                    Set the Qiskrypt's Ancilla Fully-Quantum Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskrypt_ancilla_semi_quantum_registers = None
                    """
                    Set the Qiskrypt's Ancilla Semi-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_classical_registers = qiskrypt_classical_registers
                    """
                    Set the Qiskrypt's Classical Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.global_phase = global_phase
                    """
                    Set the global phase of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskit_quantum_circuit = \
                        QuantumCircuit(
                            *[quantum_register.get_qiskit_quantum_register() for quantum_register in self.qiskrypt_quantum_registers],
                            *[ancilla_fully_quantum_register.get_qiskit_ancilla_fully_quantum_register() for
                              ancilla_fully_quantum_register in self.qiskrypt_ancilla_fully_quantum_registers],
                            *[classical_register.get_qiskit_classical_register() for classical_register in
                              self.qiskrypt_classical_registers],
                            name=name, global_phase=global_phase)
                    """
                    Set the IBM's Qiskit Quantum Circuit of the Qiskrypt's Quantum Circuit.
                    """

                else:
                    """
                    If the Qiskrypt's Quantum, Ancilla Fully-Quantum and Classical Registers are not lists.
                    """

                    """
                    Raise an Unsupported Type of Registers Error for the Qiskrypt's Quantum Circuit.
                    """
                    self.raise_unsupported_type_registers_error()

            elif (qiskrypt_quantum_registers is not None) and (qiskrypt_fully_quantum_registers is None) and (
                    qiskrypt_semi_quantum_registers is None) and \
                    (qiskrypt_ancilla_quantum_registers is None) and (qiskrypt_ancilla_fully_quantum_registers is None) and (
                    qiskrypt_ancilla_semi_quantum_registers is not None) and \
                    (qiskrypt_classical_registers is not None):
                """
                If the Qiskrypt's Quantum, Ancilla Semi-Quantum and Classical Registers given as arguments are not None,
                but both the Qiskrypt's Fully-Quantum, Semi-Quantum,
                Ancilla Quantum and Ancilla Fully-Quantum Registers are None
                (i.e., a Qiskrypt's Quantum Circuit equivalent to a hybrid Quantum/Ancilla Semi-Quantum/Classical Memory).
                """

                if (isinstance(qiskrypt_quantum_registers, list)) and (isinstance(qiskrypt_ancilla_semi_quantum_registers, list)) and (isinstance(qiskrypt_classical_registers, list)):
                    """
                    If the Qiskrypt's Quantum, Ancilla Semi-Quantum and Classical Registers are lists.
                    """

                    for quantum_register in qiskrypt_quantum_registers:
                        """
                        For each supposed Qiskrypt's Quantum Register in the list of the Qiskrypt's Quantum Registers.
                        """

                        if not (isinstance(quantum_register, QiskryptQuantumRegister)):
                            """
                            If the current supposed Qiskrypt's Quantum Register is not an actual Qiskrypt's Quantum Register.
                            """

                            QiskryptQuantumRegister.raise_not_quantum_register_error()
                            """
                            Return/Raise a Not a Quantum Register Error for the Qiskrypt's Quantum Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    for ancilla_semi_quantum_register in qiskrypt_ancilla_semi_quantum_registers:
                        """
                        For each supposed Qiskrypt's Ancilla Semi-Quantum Register in the list of the Qiskrypt's Ancilla Semi-Quantum Registers.
                        """

                        if not (isinstance(ancilla_semi_quantum_register, QiskryptAncillaSemiQuantumRegister)):
                            """
                            If the current supposed Qiskrypt's Ancilla Semi-Quantum Register is not an actual Qiskrypt's Ancilla Semi-Quantum Register.
                            """

                            QiskryptAncillaSemiQuantumRegister.raise_not_ancilla_semi_quantum_register_error()
                            """
                            Return/Raise a Not a Ancilla Semi-Quantum Register Error for the Qiskrypt's Ancilla Semi-Quantum Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    for classical_register in qiskrypt_classical_registers:
                        """
                        For each supposed Qiskrypt's Classical Register in the list of the Qiskrypt's Classical Registers.
                        """

                        if not (isinstance(classical_register, QiskryptClassicalRegister)):
                            """
                            If the current supposed Qiskrypt's Classical Register is not an actual Qiskrypt's Classical Register.
                            """

                            QiskryptClassicalRegister.raise_not_classical_register_error()
                            """
                            Return/Raise a Not a Classical Register Error for the Qiskrypt's Classical Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    self.qiskrypt_quantum_registers = qiskrypt_quantum_registers
                    """
                    Set the Qiskrypt's Quantum Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskrypt_fully_quantum_registers = None
                    """
                    Set the Qiskrypt's Fully-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_semi_quantum_registers = None
                    """
                    Set the Qiskrypt's Semi-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_ancilla_quantum_registers = None
                    """
                    Set the Qiskrypt's Ancilla Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_ancilla_fully_quantum_registers = None
                    """
                    Set the Qiskrypt's Ancilla Fully-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_ancilla_semi_quantum_registers = qiskrypt_ancilla_semi_quantum_registers
                    """
                    Set the Qiskrypt's Ancilla Semi-Quantum Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskrypt_classical_registers = qiskrypt_classical_registers
                    """
                    Set the Qiskrypt's Classical Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.global_phase = global_phase
                    """
                    Set the global phase of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskit_quantum_circuit = \
                        QuantumCircuit(
                            *[quantum_register.get_qiskit_quantum_register() for quantum_register in self.qiskrypt_quantum_registers],
                            *[ancilla_semi_quantum_register.get_qiskit_ancilla_semi_quantum_register() for
                              ancilla_semi_quantum_register in self.qiskrypt_ancilla_semi_quantum_registers],
                            *[classical_register.get_qiskit_classical_register() for classical_register in
                              self.qiskrypt_classical_registers],
                            name=name, global_phase=global_phase)
                    """
                    Set the IBM's Qiskit Quantum Circuit of the Qiskrypt's Quantum Circuit.
                    """

                else:
                    """
                    If the Qiskrypt's Quantum, Ancilla Semi-Quantum and Classical Registers are not lists.
                    """

                    """
                    Raise an Unsupported Type of Registers Error for the Qiskrypt's Quantum Circuit.
                    """
                    self.raise_unsupported_type_registers_error()

            elif (qiskrypt_quantum_registers is not None) and (qiskrypt_fully_quantum_registers is not None) and (
                    qiskrypt_semi_quantum_registers is not None) and \
                    (qiskrypt_ancilla_quantum_registers is None) and (qiskrypt_ancilla_fully_quantum_registers is None) and (
                    qiskrypt_ancilla_semi_quantum_registers is None) and \
                    (qiskrypt_classical_registers is not None):
                """
                If the Qiskrypt's Quantum, Fully-Quantum, Semi-Quantum and Classical Registers given as arguments are not None,
                but both the Ancilla Quantum, Ancilla Fully-Quantum Registers and Ancilla Semi-Quantum are None
                (i.e., a Qiskrypt's Quantum Circuit equivalent to a hybrid Quantum/Fully-Quantum/Semi-Quantum/Classical Memory).
                """

                if (isinstance(qiskrypt_quantum_registers, list)) and (isinstance(qiskrypt_fully_quantum_registers, list)) and \
                        (isinstance(qiskrypt_semi_quantum_registers, list)) and (isinstance(qiskrypt_classical_registers, list)):
                    """
                    If the Qiskrypt's Quantum, Fully-Quantum, Semi-Quantum and Classical Registers are lists.
                    """

                    for quantum_register in qiskrypt_quantum_registers:
                        """
                        For each supposed Qiskrypt's Quantum Register in the list of the Qiskrypt's Quantum Registers.
                        """

                        if not (isinstance(quantum_register, QiskryptQuantumRegister)):
                            """
                            If the current supposed Qiskrypt's Quantum Register is not an actual Qiskrypt's Quantum Register.
                            """

                            QiskryptQuantumRegister.raise_not_quantum_register_error()
                            """
                            Return/Raise a Not a Quantum Register Error for the Qiskrypt's Quantum Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    for fully_quantum_register in qiskrypt_fully_quantum_registers:
                        """
                        For each supposed Qiskrypt's Fully-Quantum Register in the list of the Qiskrypt's Fully-Quantum Registers.
                        """

                        if not (isinstance(fully_quantum_register, QiskryptFullyQuantumRegister)):
                            """
                            If the current supposed Qiskrypt's Fully-Quantum Register is not an actual Qiskrypt's Fully-Quantum Register.
                            """

                            QiskryptFullyQuantumRegister.raise_not_fully_quantum_register_error()
                            """
                            Return/Raise a Not a Fully-Quantum Register Error for the Qiskrypt's Fully-Quantum Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    for semi_quantum_register in qiskrypt_semi_quantum_registers:
                        """
                        For each supposed Qiskrypt's Semi-Quantum Register in the list of the Qiskrypt's Semi-Quantum Registers.
                        """

                        if not (isinstance(semi_quantum_register, QiskryptSemiQuantumRegister)):
                            """
                            If the current supposed Qiskrypt's Semi-Quantum Register is not an actual Qiskrypt's Semi-Quantum Register.
                            """

                            QiskryptSemiQuantumRegister.raise_not_semi_quantum_register_error()
                            """
                            Return/Raise a Not a Semi-Quantum Register Error for the Qiskrypt's Semi-Quantum Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    for classical_register in qiskrypt_classical_registers:
                        """
                        For each supposed Qiskrypt's Classical Register in the list of the Qiskrypt's Classical Registers.
                        """

                        if not (isinstance(classical_register, QiskryptClassicalRegister)):
                            """
                            If the current supposed Qiskrypt's Classical Register is not an actual Qiskrypt's Classical Register.
                            """

                            QiskryptClassicalRegister.raise_not_classical_register_error()
                            """
                            Return/Raise a Not a Classical Register Error for the Qiskrypt's Classical Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    self.qiskrypt_quantum_registers = qiskrypt_quantum_registers
                    """
                    Set the Qiskrypt's Quantum Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskrypt_fully_quantum_registers = qiskrypt_fully_quantum_registers
                    """
                    Set the Qiskrypt's Fully-Quantum Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskrypt_semi_quantum_registers = qiskrypt_semi_quantum_registers
                    """
                    Set the Qiskrypt's Semi-Quantum Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskrypt_ancilla_quantum_registers = None
                    """
                    Set the Qiskrypt's Ancilla Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_ancilla_fully_quantum_registers = None
                    """
                    Set the Qiskrypt's Ancilla Fully-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_ancilla_semi_quantum_registers = None
                    """
                    Set the Qiskrypt's Ancilla Semi-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_classical_registers = qiskrypt_classical_registers
                    """
                    Set the Qiskrypt's Classical Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.global_phase = global_phase
                    """
                    Set the global phase of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskit_quantum_circuit = \
                        QuantumCircuit(
                            *[quantum_register.get_qiskit_quantum_register() for quantum_register in self.qiskrypt_quantum_registers],
                            *[fully_quantum_register.get_qiskit_fully_quantum_register() for fully_quantum_register in
                              self.qiskrypt_fully_quantum_registers],
                            *[semi_quantum_register.get_qiskit_semi_quantum_register() for semi_quantum_register in
                              self.qiskrypt_semi_quantum_registers],
                            *[classical_register.get_qiskit_classical_register() for classical_register in
                              self.qiskrypt_classical_registers],
                            name=name, global_phase=global_phase)
                    """
                    Set the IBM's Qiskit Quantum Circuit of the Qiskrypt's Quantum Circuit.
                    """

                else:
                    """
                    If the Qiskrypt's Quantum, Fully-Quantum, Semi-Quantum and Classical Registers are not lists.
                    """

                    """
                    Raise an Unsupported Type of Registers Error for the Qiskrypt's Quantum Circuit.
                    """
                    self.raise_unsupported_type_registers_error()

            elif (qiskrypt_quantum_registers is not None) and (qiskrypt_fully_quantum_registers is not None) and (
                    qiskrypt_semi_quantum_registers is None) and \
                    (qiskrypt_ancilla_quantum_registers is not None) and (qiskrypt_ancilla_fully_quantum_registers is None) and (
                    qiskrypt_ancilla_semi_quantum_registers is None) and \
                    (qiskrypt_classical_registers is not None):
                """
                If the Qiskrypt's Quantum, Fully-Quantum, Ancilla Quantum and Classical Registers given as arguments are not None,
                but both the Semi-Quantum, Ancilla Fully-Quantum Registers and Ancilla Semi-Quantum are None
                (i.e., a Qiskrypt's Quantum Circuit equivalent to a hybrid Quantum/Fully-Quantum/Ancilla Quantum/Classical Memory).
                """

                if (isinstance(qiskrypt_quantum_registers, list)) and (isinstance(qiskrypt_fully_quantum_registers, list)) and \
                        (isinstance(qiskrypt_ancilla_quantum_registers, list)) and (isinstance(qiskrypt_classical_registers, list)):
                    """
                    If the Qiskrypt's Quantum, Fully-Quantum, Ancilla Quantum and Classical Registers are lists.
                    """

                    for quantum_register in qiskrypt_quantum_registers:
                        """
                        For each supposed Qiskrypt's Quantum Register in the list of the Qiskrypt's Quantum Registers.
                        """

                        if not (isinstance(quantum_register, QiskryptQuantumRegister)):
                            """
                            If the current supposed Qiskrypt's Quantum Register is not an actual Qiskrypt's Quantum Register.
                            """

                            QiskryptQuantumRegister.raise_not_quantum_register_error()
                            """
                            Return/Raise a Not a Quantum Register Error for the Qiskrypt's Quantum Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    for fully_quantum_register in qiskrypt_fully_quantum_registers:
                        """
                        For each supposed Qiskrypt's Fully-Quantum Register in the list of the Qiskrypt's Fully-Quantum Registers.
                        """

                        if not (isinstance(fully_quantum_register, QiskryptFullyQuantumRegister)):
                            """
                            If the current supposed Qiskrypt's Fully-Quantum Register is not an actual Qiskrypt's Fully-Quantum Register.
                            """

                            QiskryptFullyQuantumRegister.raise_not_fully_quantum_register_error()
                            """
                            Return/Raise a Not a Fully-Quantum Register Error for the Qiskrypt's Fully-Quantum Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    for ancilla_quantum_register in qiskrypt_ancilla_quantum_registers:
                        """
                        For each supposed Qiskrypt's Ancilla Quantum Register in the list of the Qiskrypt's Ancilla Quantum Registers.
                        """

                        if not (isinstance(ancilla_quantum_register, QiskryptAncillaQuantumRegister)):
                            """
                            If the current supposed Qiskrypt's Ancilla Quantum Register is not an actual Qiskrypt's Ancilla Quantum Register.
                            """

                            QiskryptAncillaQuantumRegister.raise_not_ancilla_quantum_register_error()
                            """
                            Return/Raise a Not an Ancilla Quantum Register Error for the Qiskrypt's Ancilla Quantum Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    for classical_register in qiskrypt_classical_registers:
                        """
                        For each supposed Qiskrypt's Classical Register in the list of the Qiskrypt's Classical Registers.
                        """

                        if not (isinstance(classical_register, QiskryptClassicalRegister)):
                            """
                            If the current supposed Qiskrypt's Classical Register is not an actual Qiskrypt's Classical Register.
                            """

                            QiskryptClassicalRegister.raise_not_classical_register_error()
                            """
                            Return/Raise a Not a Classical Register Error for the Qiskrypt's Classical Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    self.qiskrypt_quantum_registers = qiskrypt_quantum_registers
                    """
                    Set the Qiskrypt's Quantum Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskrypt_fully_quantum_registers = qiskrypt_fully_quantum_registers
                    """
                    Set the Qiskrypt's Fully-Quantum Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskrypt_semi_quantum_registers = None
                    """
                    Set the Qiskrypt's Semi-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_ancilla_quantum_registers = qiskrypt_ancilla_quantum_registers
                    """
                    Set the Qiskrypt's Ancilla Quantum Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskrypt_ancilla_fully_quantum_registers = None
                    """
                    Set the Qiskrypt's Ancilla Fully-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_ancilla_semi_quantum_registers = None
                    """
                    Set the Qiskrypt's Ancilla Semi-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_classical_registers = qiskrypt_classical_registers
                    """
                    Set the Qiskrypt's Classical Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.global_phase = global_phase
                    """
                    Set the global phase of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskit_quantum_circuit = \
                        QuantumCircuit(
                            *[quantum_register.get_qiskit_quantum_register() for quantum_register in self.qiskrypt_quantum_registers],
                            *[fully_quantum_register.get_qiskit_fully_quantum_register() for fully_quantum_register in
                              self.qiskrypt_fully_quantum_registers],
                            *[ancilla_quantum_register.get_qiskit_ancilla_quantum_register() for ancilla_quantum_register in
                              self.qiskrypt_ancilla_quantum_registers],
                            *[classical_register.get_qiskit_classical_register() for classical_register in
                              self.qiskrypt_classical_registers],
                            name=name, global_phase=global_phase)
                    """
                    Set the IBM's Qiskit Quantum Circuit of the Qiskrypt's Quantum Circuit.
                    """

                else:
                    """
                    If the Qiskrypt's Quantum, Fully-Quantum, Ancilla Quantum and Classical Registers are not lists.
                    """

                    """
                    Raise an Unsupported Type of Registers Error for the Qiskrypt's Quantum Circuit.
                    """
                    self.raise_unsupported_type_registers_error()

            elif (qiskrypt_quantum_registers is not None) and (qiskrypt_fully_quantum_registers is not None) and (
                    qiskrypt_semi_quantum_registers is None) and \
                    (qiskrypt_ancilla_quantum_registers is None) and (qiskrypt_ancilla_fully_quantum_registers is not None) and (
                    qiskrypt_ancilla_semi_quantum_registers is None) and \
                    (qiskrypt_classical_registers is not None):
                """
                If the Qiskrypt's Quantum, Fully-Quantum, Ancilla Fully-Quantum and Classical Registers given as arguments are not None,
                but both the Semi-Quantum, Ancilla Quantum Registers and Ancilla Semi-Quantum are None
                (i.e., a Qiskrypt's Quantum Circuit equivalent to a hybrid Quantum/Fully-Quantum/Ancilla Fully-Quantum/Classical Memory).
                """

                if (isinstance(qiskrypt_quantum_registers, list)) and (isinstance(qiskrypt_fully_quantum_registers, list)) and \
                        (isinstance(qiskrypt_ancilla_fully_quantum_registers, list)) and (isinstance(qiskrypt_classical_registers, list)):
                    """
                    If the Qiskrypt's Quantum, Fully-Quantum, Ancilla Fully-Quantum and Classical Registers are lists.
                    """

                    for quantum_register in qiskrypt_quantum_registers:
                        """
                        For each supposed Qiskrypt's Quantum Register in the list of the Qiskrypt's Quantum Registers.
                        """

                        if not (isinstance(quantum_register, QiskryptQuantumRegister)):
                            """
                            If the current supposed Qiskrypt's Quantum Register is not an actual Qiskrypt's Quantum Register.
                            """

                            QiskryptQuantumRegister.raise_not_quantum_register_error()
                            """
                            Return/Raise a Not a Quantum Register Error for the Qiskrypt's Quantum Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    for fully_quantum_register in qiskrypt_fully_quantum_registers:
                        """
                        For each supposed Qiskrypt's Fully-Quantum Register in the list of the Qiskrypt's Fully-Quantum Registers.
                        """

                        if not (isinstance(fully_quantum_register, QiskryptFullyQuantumRegister)):
                            """
                            If the current supposed Qiskrypt's Fully-Quantum Register is not an actual Qiskrypt's Fully-Quantum Register.
                            """

                            QiskryptFullyQuantumRegister.raise_not_fully_quantum_register_error()
                            """
                            Return/Raise a Not a Fully-Quantum Register Error for the Qiskrypt's Fully-Quantum Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    for ancilla_fully_quantum_register in qiskrypt_ancilla_fully_quantum_registers:
                        """
                        For each supposed Qiskrypt's Ancilla Fully-Quantum Register in the list of the Qiskrypt's Ancilla Fully-Quantum Registers.
                        """

                        if not (isinstance(ancilla_fully_quantum_register, QiskryptAncillaFullyQuantumRegister)):
                            """
                            If the current supposed Qiskrypt's Ancilla Fully-Quantum Register is not an actual Qiskrypt's Ancilla Fully-Quantum Register.
                            """

                            QiskryptAncillaFullyQuantumRegister.raise_not_ancilla_fully_quantum_register_error()
                            """
                            Return/Raise a Not an Ancilla Fully-Quantum Register Error for the Qiskrypt's Ancilla Fully-Quantum Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    for classical_register in qiskrypt_classical_registers:
                        """
                        For each supposed Qiskrypt's Classical Register in the list of the Qiskrypt's Classical Registers.
                        """

                        if not (isinstance(classical_register, QiskryptClassicalRegister)):
                            """
                            If the current supposed Qiskrypt's Classical Register is not an actual Qiskrypt's Classical Register.
                            """

                            QiskryptClassicalRegister.raise_not_classical_register_error()
                            """
                            Return/Raise a Not a Classical Register Error for the Qiskrypt's Classical Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    self.qiskrypt_quantum_registers = qiskrypt_quantum_registers
                    """
                    Set the Qiskrypt's Quantum Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskrypt_fully_quantum_registers = qiskrypt_fully_quantum_registers
                    """
                    Set the Qiskrypt's Fully-Quantum Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskrypt_semi_quantum_registers = None
                    """
                    Set the Qiskrypt's Semi-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_ancilla_quantum_registers = None
                    """
                    Set the Qiskrypt's Ancilla Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_ancilla_fully_quantum_registers = qiskrypt_ancilla_fully_quantum_registers
                    """
                    Set the Qiskrypt's Ancilla Fully-Quantum Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskrypt_ancilla_semi_quantum_registers = None
                    """
                    Set the Qiskrypt's Ancilla Semi-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_classical_registers = qiskrypt_classical_registers
                    """
                    Set the Qiskrypt's Classical Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.global_phase = global_phase
                    """
                    Set the global phase of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskit_quantum_circuit = \
                        QuantumCircuit(
                            *[quantum_register.get_qiskit_quantum_register() for quantum_register in self.qiskrypt_quantum_registers],
                            *[fully_quantum_register.get_qiskit_fully_quantum_register() for fully_quantum_register in
                              self.qiskrypt_fully_quantum_registers],
                            *[ancilla_fully_quantum_register.get_qiskit_ancilla_fully_quantum_register() for
                              ancilla_fully_quantum_register in self.qiskrypt_ancilla_fully_quantum_registers],
                            *[classical_register.get_qiskit_classical_register() for classical_register in
                              self.qiskrypt_classical_registers],
                            name=name, global_phase=global_phase)
                    """
                    Set the IBM's Qiskit Quantum Circuit of the Qiskrypt's Quantum Circuit.
                    """

                else:
                    """
                    If the Qiskrypt's Quantum, Fully-Quantum, Ancilla Fully-Quantum and Classical Registers are not lists.
                    """

                    """
                    Raise an Unsupported Type of Registers Error for the Qiskrypt's Quantum Circuit.
                    """
                    self.raise_unsupported_type_registers_error()

            elif (qiskrypt_quantum_registers is not None) and (qiskrypt_fully_quantum_registers is not None) and (
                    qiskrypt_semi_quantum_registers is None) and \
                    (qiskrypt_ancilla_quantum_registers is None) and (qiskrypt_ancilla_fully_quantum_registers is None) and (
                    qiskrypt_ancilla_semi_quantum_registers is not None) and \
                    (qiskrypt_classical_registers is not None):
                """
                If the Qiskrypt's Quantum, Fully-Quantum, Ancilla Semi-Quantum and Classical Registers given as arguments are not None,
                but both the Semi-Quantum, Ancilla Quantum Registers and Ancilla Fully-Quantum are None
                (i.e., a Qiskrypt's Quantum Circuit equivalent to a hybrid Quantum/Fully-Quantum/Ancilla Semi-Quantum/Classical Memory).
                """

                if (isinstance(qiskrypt_quantum_registers, list)) and (isinstance(qiskrypt_fully_quantum_registers, list)) and \
                        (isinstance(qiskrypt_ancilla_semi_quantum_registers, list)) and (isinstance(qiskrypt_classical_registers, list)):
                    """
                    If the Qiskrypt's Quantum, Fully-Quantum, Ancilla Semi-Quantum and Classical Registers are lists.
                    """

                    for quantum_register in qiskrypt_quantum_registers:
                        """
                        For each supposed Qiskrypt's Quantum Register in the list of the Qiskrypt's Quantum Registers.
                        """

                        if not (isinstance(quantum_register, QiskryptQuantumRegister)):
                            """
                            If the current supposed Qiskrypt's Quantum Register is not an actual Qiskrypt's Quantum Register.
                            """

                            QiskryptQuantumRegister.raise_not_quantum_register_error()
                            """
                            Return/Raise a Not a Quantum Register Error for the Qiskrypt's Quantum Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    for fully_quantum_register in qiskrypt_fully_quantum_registers:
                        """
                        For each supposed Qiskrypt's Fully-Quantum Register in the list of the Qiskrypt's Fully-Quantum Registers.
                        """

                        if not (isinstance(fully_quantum_register, QiskryptFullyQuantumRegister)):
                            """
                            If the current supposed Qiskrypt's Fully-Quantum Register is not an actual Qiskrypt's Fully-Quantum Register.
                            """

                            QiskryptFullyQuantumRegister.raise_not_fully_quantum_register_error()
                            """
                            Return/Raise a Not a Fully-Quantum Register Error for the Qiskrypt's Fully-Quantum Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    for ancilla_semi_quantum_register in qiskrypt_ancilla_semi_quantum_registers:
                        """
                        For each supposed Qiskrypt's Ancilla Semi-Quantum Register in the list of the Qiskrypt's Ancilla Semi-Quantum Registers.
                        """

                        if not (isinstance(ancilla_semi_quantum_register, QiskryptAncillaSemiQuantumRegister)):
                            """
                            If the current supposed Qiskrypt's Ancilla Semi-Quantum Register is not an actual Qiskrypt's Ancilla Semi-Quantum Register.
                            """

                            QiskryptAncillaSemiQuantumRegister.raise_not_ancilla_semi_quantum_register_error()
                            """
                            Return/Raise a Not an Ancilla Semi-Quantum Register Error for the Qiskrypt's Ancilla Semi-Quantum Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    for classical_register in qiskrypt_classical_registers:
                        """
                        For each supposed Qiskrypt's Classical Register in the list of the Qiskrypt's Classical Registers.
                        """

                        if not (isinstance(classical_register, QiskryptClassicalRegister)):
                            """
                            If the current supposed Qiskrypt's Classical Register is not an actual Qiskrypt's Classical Register.
                            """

                            QiskryptClassicalRegister.raise_not_classical_register_error()
                            """
                            Return/Raise a Not a Classical Register Error for the Qiskrypt's Classical Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    self.qiskrypt_quantum_registers = qiskrypt_quantum_registers
                    """
                    Set the Qiskrypt's Quantum Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskrypt_fully_quantum_registers = qiskrypt_fully_quantum_registers
                    """
                    Set the Qiskrypt's Fully-Quantum Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskrypt_semi_quantum_registers = None
                    """
                    Set the Qiskrypt's Semi-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_ancilla_quantum_registers = None
                    """
                    Set the Qiskrypt's Ancilla Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_ancilla_fully_quantum_registers = None
                    """
                    Set the Qiskrypt's Ancilla Fully-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_ancilla_semi_quantum_registers = qiskrypt_ancilla_semi_quantum_registers
                    """
                    Set the Qiskrypt's Ancilla Semi-Quantum Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskrypt_classical_registers = qiskrypt_classical_registers
                    """
                    Set the Qiskrypt's Classical Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.global_phase = global_phase
                    """
                    Set the global phase of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskit_quantum_circuit = \
                        QuantumCircuit(
                            *[quantum_register.get_qiskit_quantum_register() for quantum_register in self.qiskrypt_quantum_registers],
                            *[fully_quantum_register.get_qiskit_fully_quantum_register() for fully_quantum_register in
                              self.qiskrypt_fully_quantum_registers],
                            *[ancilla_semi_quantum_register.get_qiskit_ancilla_semi_quantum_register() for
                              ancilla_semi_quantum_register in self.qiskrypt_ancilla_semi_quantum_registers],
                            *[classical_register.get_qiskit_classical_register() for classical_register in
                              self.qiskrypt_classical_registers],
                            name=name, global_phase=global_phase)
                    """
                    Set the IBM's Qiskit Quantum Circuit of the Qiskrypt's Quantum Circuit.
                    """

                else:
                    """
                    If the Qiskrypt's Quantum, Fully-Quantum, Ancilla Semi-Quantum and Classical Registers are not lists.
                    """

                    """
                    Raise an Unsupported Type of Registers Error for the Qiskrypt's Quantum Circuit.
                    """
                    self.raise_unsupported_type_registers_error()

            elif (qiskrypt_quantum_registers is not None) and (qiskrypt_fully_quantum_registers is not None) and (
                    qiskrypt_semi_quantum_registers is not None) and \
                    (qiskrypt_ancilla_quantum_registers is not None) and (qiskrypt_ancilla_fully_quantum_registers is None) and (
                    qiskrypt_ancilla_semi_quantum_registers is None) and \
                    (qiskrypt_classical_registers is not None):
                """
                If the Qiskrypt's Quantum, Fully-Quantum, Semi-Quantum, Ancilla Quantum and Classical Registers given as arguments are not None,
                but both the Ancilla Fully-Quantum Registers and Ancilla Semi-Quantum are None
                (i.e., a Qiskrypt's Quantum Circuit equivalent to a hybrid Quantum/Fully-Quantum/Semi-Quantum/Ancilla Quantum/Classical Memory).
                """

                if (isinstance(qiskrypt_quantum_registers, list)) and (isinstance(qiskrypt_fully_quantum_registers, list)) and \
                        (isinstance(qiskrypt_semi_quantum_registers, list)) and (isinstance(qiskrypt_ancilla_quantum_registers, list)) and \
                        (isinstance(qiskrypt_classical_registers, list)):
                    """
                    If the Qiskrypt's Quantum, Fully-Quantum, Semi-Quantum, Ancilla Quantum and Classical Registers are lists.
                    """

                    for quantum_register in qiskrypt_quantum_registers:
                        """
                        For each supposed Qiskrypt's Quantum Register in the list of the Qiskrypt's Quantum Registers.
                        """

                        if not (isinstance(quantum_register, QiskryptQuantumRegister)):
                            """
                            If the current supposed Qiskrypt's Quantum Register is not an actual Qiskrypt's Quantum Register.
                            """

                            QiskryptQuantumRegister.raise_not_quantum_register_error()
                            """
                            Return/Raise a Not a Quantum Register Error for the Qiskrypt's Quantum Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    for fully_quantum_register in qiskrypt_fully_quantum_registers:
                        """
                        For each supposed Qiskrypt's Fully-Quantum Register in the list of the Qiskrypt's Fully-Quantum Registers.
                        """

                        if not (isinstance(fully_quantum_register, QiskryptFullyQuantumRegister)):
                            """
                            If the current supposed Qiskrypt's Fully-Quantum Register is not an actual Qiskrypt's Fully-Quantum Register.
                            """

                            QiskryptFullyQuantumRegister.raise_not_fully_quantum_register_error()
                            """
                            Return/Raise a Not a Fully-Quantum Register Error for the Qiskrypt's Fully-Quantum Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    for semi_quantum_register in qiskrypt_semi_quantum_registers:
                        """
                        For each supposed Qiskrypt's Semi-Quantum Register in the list of the Qiskrypt's Semi-Quantum Registers.
                        """

                        if not (isinstance(semi_quantum_register, QiskryptSemiQuantumRegister)):
                            """
                            If the current supposed Qiskrypt's Semi-Quantum Register is not an actual Qiskrypt's Semi-Quantum Register.
                            """

                            QiskryptSemiQuantumRegister.raise_not_semi_quantum_register_error()
                            """
                            Return/Raise a Not a Semi-Quantum Register Error for the Qiskrypt's Semi-Quantum Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    for ancilla_quantum_register in qiskrypt_ancilla_quantum_registers:
                        """
                        For each supposed Qiskrypt's Ancilla Quantum Register in the list of the Qiskrypt's Ancilla Quantum Registers.
                        """

                        if not (isinstance(ancilla_quantum_register, QiskryptAncillaQuantumRegister)):
                            """
                            If the current supposed Qiskrypt's Ancilla Quantum Register is not an actual Qiskrypt's Ancilla Quantum Register.
                            """

                            QiskryptAncillaQuantumRegister.raise_not_ancilla_quantum_register_error()
                            """
                            Return/Raise a Not an Ancilla Quantum Register Error for the Qiskrypt's Ancilla Quantum Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    for classical_register in qiskrypt_classical_registers:
                        """
                        For each supposed Qiskrypt's Classical Register in the list of the Qiskrypt's Classical Registers.
                        """

                        if not (isinstance(classical_register, QiskryptClassicalRegister)):
                            """
                            If the current supposed Qiskrypt's Classical Register is not an actual Qiskrypt's Classical Register.
                            """

                            QiskryptClassicalRegister.raise_not_classical_register_error()
                            """
                            Return/Raise a Not a Classical Register Error for the Qiskrypt's Classical Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    self.qiskrypt_quantum_registers = qiskrypt_quantum_registers
                    """
                    Set the Qiskrypt's Quantum Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskrypt_fully_quantum_registers = qiskrypt_fully_quantum_registers
                    """
                    Set the Qiskrypt's Fully-Quantum Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskrypt_semi_quantum_registers = qiskrypt_semi_quantum_registers
                    """
                    Set the Qiskrypt's Semi-Quantum Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskrypt_ancilla_quantum_registers = qiskrypt_ancilla_quantum_registers
                    """
                    Set the Qiskrypt's Ancilla Quantum Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskrypt_ancilla_fully_quantum_registers = None
                    """
                    Set the Qiskrypt's Ancilla Fully-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_ancilla_semi_quantum_registers = None
                    """
                    Set the Qiskrypt's Ancilla Semi-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_classical_registers = qiskrypt_classical_registers
                    """
                    Set the Qiskrypt's Classical Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.global_phase = global_phase
                    """
                    Set the global phase of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskit_quantum_circuit = \
                        QuantumCircuit(
                            *[quantum_register.get_qiskit_quantum_register() for quantum_register in self.qiskrypt_quantum_registers],
                            *[fully_quantum_register.get_qiskit_fully_quantum_register() for fully_quantum_register in
                              self.qiskrypt_fully_quantum_registers],
                            *[semi_quantum_register.get_qiskit_semi_quantum_register() for semi_quantum_register in
                              self.qiskrypt_semi_quantum_registers],
                            *[ancilla_quantum_register.get_qiskit_ancilla_quantum_register() for ancilla_quantum_register in
                              self.qiskrypt_ancilla_quantum_registers],
                            *[classical_register.get_qiskit_classical_register() for classical_register in
                              self.qiskrypt_classical_registers],
                            name=name, global_phase=global_phase)
                    """
                    Set the IBM's Qiskit Quantum Circuit of the Qiskrypt's Quantum Circuit.
                    """

                else:
                    """
                    If the Qiskrypt's Quantum, Fully-Quantum, Semi-Quantum, Ancilla Quantum and Classical Registers are not lists.
                    """

                    """
                    Raise an Unsupported Type of Registers Error for the Qiskrypt's Quantum Circuit.
                    """
                    self.raise_unsupported_type_registers_error()

            elif (qiskrypt_quantum_registers is not None) and (qiskrypt_fully_quantum_registers is not None) and (
                    qiskrypt_semi_quantum_registers is not None) and \
                    (qiskrypt_ancilla_quantum_registers is None) and (qiskrypt_ancilla_fully_quantum_registers is not None) and (
                    qiskrypt_ancilla_semi_quantum_registers is None) and \
                    (qiskrypt_classical_registers is not None):
                """
                If the Qiskrypt's Quantum, Fully-Quantum, Semi-Quantum, Ancilla Fully-Quantum and Classical Registers given as arguments are not None,
                but both the Ancilla Quantum Registers and Ancilla Semi-Quantum are None
                (i.e., a Qiskrypt's Quantum Circuit equivalent to a hybrid Quantum/Fully-Quantum/Semi-Quantum/Ancilla Fully-Quantum/Classical Memory).
                """

                if (isinstance(qiskrypt_quantum_registers, list)) and (isinstance(qiskrypt_fully_quantum_registers, list)) and \
                        (isinstance(qiskrypt_semi_quantum_registers, list)) and (isinstance(qiskrypt_ancilla_fully_quantum_registers, list)) and \
                        (isinstance(qiskrypt_classical_registers, list)):
                    """
                    If the Qiskrypt's Quantum, Fully-Quantum, Semi-Quantum, Ancilla Fully-Quantum and Classical Registers are lists.
                    """

                    for quantum_register in qiskrypt_quantum_registers:
                        """
                        For each supposed Qiskrypt's Quantum Register in the list of the Qiskrypt's Quantum Registers.
                        """

                        if not (isinstance(quantum_register, QiskryptQuantumRegister)):
                            """
                            If the current supposed Qiskrypt's Quantum Register is not an actual Qiskrypt's Quantum Register.
                            """

                            QiskryptQuantumRegister.raise_not_quantum_register_error()
                            """
                            Return/Raise a Not a Quantum Register Error for the Qiskrypt's Quantum Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    for fully_quantum_register in qiskrypt_fully_quantum_registers:
                        """
                        For each supposed Qiskrypt's Fully-Quantum Register in the list of the Qiskrypt's Fully-Quantum Registers.
                        """

                        if not (isinstance(fully_quantum_register, QiskryptFullyQuantumRegister)):
                            """
                            If the current supposed Qiskrypt's Fully-Quantum Register is not an actual Qiskrypt's Fully-Quantum Register.
                            """

                            QiskryptFullyQuantumRegister.raise_not_fully_quantum_register_error()
                            """
                            Return/Raise a Not a Fully-Quantum Register Error for the Qiskrypt's Fully-Quantum Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    for semi_quantum_register in qiskrypt_semi_quantum_registers:
                        """
                        For each supposed Qiskrypt's Semi-Quantum Register in the list of the Qiskrypt's Semi-Quantum Registers.
                        """

                        if not (isinstance(semi_quantum_register, QiskryptSemiQuantumRegister)):
                            """
                            If the current supposed Qiskrypt's Semi-Quantum Register is not an actual Qiskrypt's Semi-Quantum Register.
                            """

                            QiskryptSemiQuantumRegister.raise_not_semi_quantum_register_error()
                            """
                            Return/Raise a Not a Semi-Quantum Register Error for the Qiskrypt's Semi-Quantum Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    for ancilla_fully_quantum_register in qiskrypt_ancilla_fully_quantum_registers:
                        """
                        For each supposed Qiskrypt's Ancilla Fully-Quantum Register in the list of the Qiskrypt's Ancilla Fully-Quantum Registers.
                        """

                        if not (isinstance(ancilla_fully_quantum_register, QiskryptAncillaFullyQuantumRegister)):
                            """
                            If the current supposed Qiskrypt's Ancilla Fully-Quantum Register is not an actual Qiskrypt's Ancilla Fully-Quantum Register.
                            """

                            QiskryptAncillaFullyQuantumRegister.raise_not_ancilla_fully_quantum_register_error()
                            """
                            Return/Raise a Not an Ancilla Fully-Quantum Register Error for the Qiskrypt's Ancilla Fully-Quantum Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    for classical_register in qiskrypt_classical_registers:
                        """
                        For each supposed Qiskrypt's Classical Register in the list of the Qiskrypt's Classical Registers.
                        """

                        if not (isinstance(classical_register, QiskryptClassicalRegister)):
                            """
                            If the current supposed Qiskrypt's Classical Register is not an actual Qiskrypt's Classical Register.
                            """

                            QiskryptClassicalRegister.raise_not_classical_register_error()
                            """
                            Return/Raise a Not a Classical Register Error for the Qiskrypt's Classical Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    self.qiskrypt_quantum_registers = qiskrypt_quantum_registers
                    """
                    Set the Qiskrypt's Quantum Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskrypt_fully_quantum_registers = qiskrypt_fully_quantum_registers
                    """
                    Set the Qiskrypt's Fully-Quantum Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskrypt_semi_quantum_registers = qiskrypt_semi_quantum_registers
                    """
                    Set the Qiskrypt's Semi-Quantum Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskrypt_ancilla_quantum_registers = None
                    """
                    Set the Qiskrypt's Ancilla Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_ancilla_fully_quantum_registers = qiskrypt_ancilla_fully_quantum_registers
                    """
                    Set the Qiskrypt's Ancilla Fully-Quantum Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskrypt_ancilla_semi_quantum_registers = None
                    """
                    Set the Qiskrypt's Ancilla Semi-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_classical_registers = qiskrypt_classical_registers
                    """
                    Set the Qiskrypt's Classical Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.global_phase = global_phase
                    """
                    Set the global phase of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskit_quantum_circuit = \
                        QuantumCircuit(
                            *[quantum_register.get_qiskit_quantum_register() for quantum_register in self.qiskrypt_quantum_registers],
                            *[fully_quantum_register.get_qiskit_fully_quantum_register() for fully_quantum_register in
                              self.qiskrypt_fully_quantum_registers],
                            *[semi_quantum_register.get_qiskit_semi_quantum_register() for semi_quantum_register in
                              self.qiskrypt_semi_quantum_registers],
                            *[ancilla_fully_quantum_register.get_qiskit_ancilla_fully_quantum_register() for
                              ancilla_fully_quantum_register in self.qiskrypt_ancilla_fully_quantum_registers],
                            *[classical_register.get_qiskit_classical_register() for classical_register in
                              self.qiskrypt_classical_registers],
                            name=name, global_phase=global_phase)
                    """
                    Set the IBM's Qiskit Quantum Circuit of the Qiskrypt's Quantum Circuit.
                    """

                else:
                    """
                    If the Qiskrypt's Quantum, Fully-Quantum, Semi-Quantum, Ancilla Fully-Quantum and Classical Registers are not lists.
                    """

                    """
                    Raise an Unsupported Type of Registers Error for the Qiskrypt's Quantum Circuit.
                    """
                    self.raise_unsupported_type_registers_error()

            elif (qiskrypt_quantum_registers is not None) and (qiskrypt_fully_quantum_registers is not None) and (
                    qiskrypt_semi_quantum_registers is not None) and \
                    (qiskrypt_ancilla_quantum_registers is None) and (qiskrypt_ancilla_fully_quantum_registers is None) and (
                    qiskrypt_ancilla_semi_quantum_registers is not None) and \
                    (qiskrypt_classical_registers is not None):
                """
                If the Qiskrypt's Quantum, Fully-Quantum, Semi-Quantum, Ancilla Semi-Quantum and Classical Registers given as arguments are not None,
                but both the Ancilla Quantum Registers and Ancilla Fully-Quantum are None
                (i.e., a Qiskrypt's Quantum Circuit equivalent to a hybrid Quantum/Fully-Quantum/Semi-Quantum/Ancilla Semi-Quantum/Classical Memory).
                """

                if (isinstance(qiskrypt_quantum_registers, list)) and (isinstance(qiskrypt_fully_quantum_registers, list)) and \
                        (isinstance(qiskrypt_semi_quantum_registers, list)) and (isinstance(qiskrypt_ancilla_semi_quantum_registers, list)) and \
                        (isinstance(qiskrypt_classical_registers, list)):
                    """
                    If the Qiskrypt's Quantum, Fully-Quantum, Semi-Quantum, Ancilla Semi-Quantum and Classical Registers are lists.
                    """

                    for quantum_register in qiskrypt_quantum_registers:
                        """
                        For each supposed Qiskrypt's Quantum Register in the list of the Qiskrypt's Quantum Registers.
                        """

                        if not (isinstance(quantum_register, QiskryptQuantumRegister)):
                            """
                            If the current supposed Qiskrypt's Quantum Register is not an actual Qiskrypt's Quantum Register.
                            """

                            QiskryptQuantumRegister.raise_not_quantum_register_error()
                            """
                            Return/Raise a Not a Quantum Register Error for the Qiskrypt's Quantum Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    for fully_quantum_register in qiskrypt_fully_quantum_registers:
                        """
                        For each supposed Qiskrypt's Fully-Quantum Register in the list of the Qiskrypt's Fully-Quantum Registers.
                        """

                        if not (isinstance(fully_quantum_register, QiskryptFullyQuantumRegister)):
                            """
                            If the current supposed Qiskrypt's Fully-Quantum Register is not an actual Qiskrypt's Fully-Quantum Register.
                            """

                            QiskryptFullyQuantumRegister.raise_not_fully_quantum_register_error()
                            """
                            Return/Raise a Not a Fully-Quantum Register Error for the Qiskrypt's Fully-Quantum Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    for semi_quantum_register in qiskrypt_semi_quantum_registers:
                        """
                        For each supposed Qiskrypt's Semi-Quantum Register in the list of the Qiskrypt's Semi-Quantum Registers.
                        """

                        if not (isinstance(semi_quantum_register, QiskryptSemiQuantumRegister)):
                            """
                            If the current supposed Qiskrypt's Semi-Quantum Register is not an actual Qiskrypt's Semi-Quantum Register.
                            """

                            QiskryptSemiQuantumRegister.raise_not_semi_quantum_register_error()
                            """
                            Return/Raise a Not a Semi-Quantum Register Error for the Qiskrypt's Semi-Quantum Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    for ancilla_semi_quantum_register in qiskrypt_ancilla_semi_quantum_registers:
                        """
                        For each supposed Qiskrypt's Ancilla Semi-Quantum Register in the list of the Qiskrypt's Ancilla Semi-Quantum Registers.
                        """

                        if not (isinstance(ancilla_semi_quantum_register, QiskryptAncillaSemiQuantumRegister)):
                            """
                            If the current supposed Qiskrypt's Ancilla Semi-Quantum Register is not an actual Qiskrypt's Ancilla Semi-Quantum Register.
                            """

                            QiskryptAncillaSemiQuantumRegister.raise_not_ancilla_semi_quantum_register_error()
                            """
                            Return/Raise a Not an Ancilla Semi-Quantum Register Error for the Qiskrypt's Ancilla Semi-Quantum Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    for classical_register in qiskrypt_classical_registers:
                        """
                        For each supposed Qiskrypt's Classical Register in the list of the Qiskrypt's Classical Registers.
                        """

                        if not (isinstance(classical_register, QiskryptClassicalRegister)):
                            """
                            If the current supposed Qiskrypt's Classical Register is not an actual Qiskrypt's Classical Register.
                            """

                            QiskryptClassicalRegister.raise_not_classical_register_error()
                            """
                            Return/Raise a Not a Classical Register Error for the Qiskrypt's Classical Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    self.qiskrypt_quantum_registers = qiskrypt_quantum_registers
                    """
                    Set the Qiskrypt's Quantum Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskrypt_fully_quantum_registers = qiskrypt_fully_quantum_registers
                    """
                    Set the Qiskrypt's Fully-Quantum Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskrypt_semi_quantum_registers = qiskrypt_semi_quantum_registers
                    """
                    Set the Qiskrypt's Semi-Quantum Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskrypt_ancilla_quantum_registers = None
                    """
                    Set the Qiskrypt's Ancilla Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_ancilla_fully_quantum_registers = None
                    """
                    Set the Qiskrypt's Ancilla Fully-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_ancilla_semi_quantum_registers = qiskrypt_ancilla_semi_quantum_registers
                    """
                    Set the Qiskrypt's Ancilla Semi-Quantum Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskrypt_classical_registers = qiskrypt_classical_registers
                    """
                    Set the Qiskrypt's Classical Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.global_phase = global_phase
                    """
                    Set the global phase of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskit_quantum_circuit = \
                        QuantumCircuit(
                            *[quantum_register.get_qiskit_quantum_register() for quantum_register in self.qiskrypt_quantum_registers],
                            *[fully_quantum_register.get_qiskit_fully_quantum_register() for fully_quantum_register in
                              self.qiskrypt_fully_quantum_registers],
                            *[semi_quantum_register.get_qiskit_semi_quantum_register() for semi_quantum_register in
                              self.qiskrypt_semi_quantum_registers],
                            *[ancilla_semi_quantum_register.get_qiskit_ancilla_semi_quantum_register() for
                              ancilla_semi_quantum_register in self.qiskrypt_ancilla_semi_quantum_registers],
                            *[classical_register.get_qiskit_classical_register() for classical_register in
                              self.qiskrypt_classical_registers],
                            name=name, global_phase=global_phase)
                    """
                    Set the IBM's Qiskit Quantum Circuit of the Qiskrypt's Quantum Circuit.
                    """

                else:
                    """
                    If the Qiskrypt's Quantum, Fully-Quantum, Semi-Quantum, Ancilla Semi-Quantum and Classical Registers are not lists.
                    """

                    """
                    Raise an Unsupported Type of Registers Error for the Qiskrypt's Quantum Circuit.
                    """
                    self.raise_unsupported_type_registers_error()

            elif (qiskrypt_quantum_registers is not None) and (qiskrypt_fully_quantum_registers is not None) and (
                    qiskrypt_semi_quantum_registers is not None) and \
                    (qiskrypt_ancilla_quantum_registers is not None) and (qiskrypt_ancilla_fully_quantum_registers is not None) and (
                    qiskrypt_ancilla_semi_quantum_registers is None) and \
                    (qiskrypt_classical_registers is not None):
                """
                If the Qiskrypt's Quantum, Fully-Quantum, Semi-Quantum,
                Ancilla Quantum, Ancilla Fully-Quantum and Classical Registers given as arguments are not None,
                but the Ancilla Semi-Quantum is None
                (i.e., a Qiskrypt's Quantum Circuit equivalent to a hybrid Quantum/Fully-Quantum/Semi-Quantum/Ancilla Quantum/Ancilla Fully-Quantum/Classical Memory).
                """

                if (isinstance(qiskrypt_quantum_registers, list)) and (isinstance(qiskrypt_fully_quantum_registers, list)) and \
                        (isinstance(qiskrypt_semi_quantum_registers, list)) and (isinstance(qiskrypt_ancilla_quantum_registers, list)) and \
                        (isinstance(qiskrypt_ancilla_fully_quantum_registers, list)) and (isinstance(qiskrypt_classical_registers, list)):
                    """
                    If the Qiskrypt's Quantum, Fully-Quantum, Semi-Quantum, Ancilla Quantum, Ancilla Fully-Quantum and Classical Registers are lists.
                    """

                    for quantum_register in qiskrypt_quantum_registers:
                        """
                        For each supposed Qiskrypt's Quantum Register in the list of the Qiskrypt's Quantum Registers.
                        """

                        if not (isinstance(quantum_register, QiskryptQuantumRegister)):
                            """
                            If the current supposed Qiskrypt's Quantum Register is not an actual Qiskrypt's Quantum Register.
                            """

                            QiskryptQuantumRegister.raise_not_quantum_register_error()
                            """
                            Return/Raise a Not a Quantum Register Error for the Qiskrypt's Quantum Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    for fully_quantum_register in qiskrypt_fully_quantum_registers:
                        """
                        For each supposed Qiskrypt's Fully-Quantum Register in the list of the Qiskrypt's Fully-Quantum Registers.
                        """

                        if not (isinstance(fully_quantum_register, QiskryptFullyQuantumRegister)):
                            """
                            If the current supposed Qiskrypt's Fully-Quantum Register is not an actual Qiskrypt's Fully-Quantum Register.
                            """

                            QiskryptFullyQuantumRegister.raise_not_fully_quantum_register_error()
                            """
                            Return/Raise a Not a Fully-Quantum Register Error for the Qiskrypt's Fully-Quantum Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    for semi_quantum_register in qiskrypt_semi_quantum_registers:
                        """
                        For each supposed Qiskrypt's Semi-Quantum Register in the list of the Qiskrypt's Semi-Quantum Registers.
                        """

                        if not (isinstance(semi_quantum_register, QiskryptSemiQuantumRegister)):
                            """
                            If the current supposed Qiskrypt's Semi-Quantum Register is not an actual Qiskrypt's Semi-Quantum Register.
                            """

                            QiskryptSemiQuantumRegister.raise_not_semi_quantum_register_error()
                            """
                            Return/Raise a Not a Semi-Quantum Register Error for the Qiskrypt's Semi-Quantum Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    for ancilla_quantum_register in qiskrypt_ancilla_quantum_registers:
                        """
                        For each supposed Qiskrypt's Ancilla Quantum Register in the list of the Qiskrypt's Ancilla Quantum Registers.
                        """

                        if not (isinstance(ancilla_quantum_register, QiskryptAncillaQuantumRegister)):
                            """
                            If the current supposed Qiskrypt's Ancilla Quantum Register is not an actual Qiskrypt's Ancilla Quantum Register.
                            """

                            QiskryptAncillaQuantumRegister.raise_not_ancilla_quantum_register_error()
                            """
                            Return/Raise a Not an Ancilla Quantum Register Error for the Qiskrypt's Ancilla Quantum Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    for ancilla_fully_quantum_register in qiskrypt_ancilla_fully_quantum_registers:
                        """
                        For each supposed Qiskrypt's Ancilla Fully-Quantum Register in the list of the Qiskrypt's Ancilla Fully-Quantum Registers.
                        """

                        if not (isinstance(ancilla_fully_quantum_register, QiskryptAncillaFullyQuantumRegister)):
                            """
                            If the current supposed Qiskrypt's Ancilla Fully-Quantum Register is not an actual Qiskrypt's Ancilla Fully-Quantum Register.
                            """

                            QiskryptAncillaFullyQuantumRegister.raise_not_ancilla_fully_quantum_register_error()
                            """
                            Return/Raise a Not an Ancilla Fully-Quantum Register Error for the Qiskrypt's Ancilla Fully-Quantum Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    for classical_register in qiskrypt_classical_registers:
                        """
                        For each supposed Qiskrypt's Classical Register in the list of the Qiskrypt's Classical Registers.
                        """

                        if not (isinstance(classical_register, QiskryptClassicalRegister)):
                            """
                            If the current supposed Qiskrypt's Classical Register is not an actual Qiskrypt's Classical Register.
                            """

                            QiskryptClassicalRegister.raise_not_classical_register_error()
                            """
                            Return/Raise a Not a Classical Register Error for the Qiskrypt's Classical Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    self.qiskrypt_quantum_registers = qiskrypt_quantum_registers
                    """
                    Set the Qiskrypt's Quantum Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskrypt_fully_quantum_registers = qiskrypt_fully_quantum_registers
                    """
                    Set the Qiskrypt's Fully-Quantum Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskrypt_semi_quantum_registers = qiskrypt_semi_quantum_registers
                    """
                    Set the Qiskrypt's Semi-Quantum Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskrypt_ancilla_quantum_registers = qiskrypt_ancilla_quantum_registers
                    """
                    Set the Qiskrypt's Ancilla Quantum Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskrypt_ancilla_fully_quantum_registers = qiskrypt_ancilla_fully_quantum_registers
                    """
                    Set the Qiskrypt's Ancilla Fully-Quantum Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskrypt_ancilla_semi_quantum_registers = None
                    """
                    Set the Qiskrypt's Ancilla Semi-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_classical_registers = qiskrypt_classical_registers
                    """
                    Set the Qiskrypt's Classical Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.global_phase = global_phase
                    """
                    Set the global phase of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskit_quantum_circuit = \
                        QuantumCircuit(
                            *[quantum_register.get_qiskit_quantum_register() for quantum_register in self.qiskrypt_quantum_registers],
                            *[fully_quantum_register.get_qiskit_fully_quantum_register() for fully_quantum_register in
                              self.qiskrypt_fully_quantum_registers],
                            *[semi_quantum_register.get_qiskit_semi_quantum_register() for semi_quantum_register in
                              self.qiskrypt_semi_quantum_registers],
                            *[ancilla_quantum_register.get_qiskit_ancilla_quantum_register() for ancilla_quantum_register in
                              self.qiskrypt_ancilla_quantum_registers],
                            *[ancilla_fully_quantum_register.get_qiskit_ancilla_fully_quantum_register() for
                              ancilla_fully_quantum_register in self.qiskrypt_ancilla_fully_quantum_registers],
                            *[classical_register.get_qiskit_classical_register() for classical_register in
                              self.qiskrypt_classical_registers],
                            name=name, global_phase=global_phase)
                    """
                    Set the IBM's Qiskit Quantum Circuit of the Qiskrypt's Quantum Circuit.
                    """

                else:
                    """
                    If the Qiskrypt's Quantum, Fully-Quantum, Semi-Quantum, Ancilla Quantum, Ancilla Fully-Quantum and Classical Registers are not lists.
                    """

                    """
                    Raise an Unsupported Type of Registers Error for the Qiskrypt's Quantum Circuit.
                    """
                    self.raise_unsupported_type_registers_error()

            elif (qiskrypt_quantum_registers is not None) and (qiskrypt_fully_quantum_registers is not None) and (
                    qiskrypt_semi_quantum_registers is not None) and \
                    (qiskrypt_ancilla_quantum_registers is not None) and (qiskrypt_ancilla_fully_quantum_registers is None) and (
                    qiskrypt_ancilla_semi_quantum_registers is not None) and \
                    (qiskrypt_classical_registers is not None):
                """
                If the Qiskrypt's Quantum, Fully-Quantum, Semi-Quantum,
                Ancilla Quantum, Ancilla Semi-Quantum and Classical Registers given as arguments are not None,
                but the Ancilla Fully-Quantum is None
                (i.e., a Qiskrypt's Quantum Circuit equivalent to a hybrid Quantum/Fully-Quantum/Semi-Quantum/Ancilla Quantum/Ancilla Semi-Quantum/Classical Memory).
                """

                if (isinstance(qiskrypt_quantum_registers, list)) and (isinstance(qiskrypt_fully_quantum_registers, list)) and \
                        (isinstance(qiskrypt_semi_quantum_registers, list)) and (isinstance(qiskrypt_ancilla_quantum_registers, list)) and \
                        (isinstance(qiskrypt_ancilla_semi_quantum_registers, list)) and (isinstance(qiskrypt_classical_registers, list)):
                    """
                    If the Qiskrypt's Quantum, Fully-Quantum, Semi-Quantum, Ancilla Quantum, Ancilla Semi-Quantum and Classical Registers are lists.
                    """

                    for quantum_register in qiskrypt_quantum_registers:
                        """
                        For each supposed Qiskrypt's Quantum Register in the list of the Qiskrypt's Quantum Registers.
                        """

                        if not (isinstance(quantum_register, QiskryptQuantumRegister)):
                            """
                            If the current supposed Qiskrypt's Quantum Register is not an actual Qiskrypt's Quantum Register.
                            """

                            QiskryptQuantumRegister.raise_not_quantum_register_error()
                            """
                            Return/Raise a Not a Quantum Register Error for the Qiskrypt's Quantum Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    for fully_quantum_register in qiskrypt_fully_quantum_registers:
                        """
                        For each supposed Qiskrypt's Fully-Quantum Register in the list of the Qiskrypt's Fully-Quantum Registers.
                        """

                        if not (isinstance(fully_quantum_register, QiskryptFullyQuantumRegister)):
                            """
                            If the current supposed Qiskrypt's Fully-Quantum Register is not an actual Qiskrypt's Fully-Quantum Register.
                            """

                            QiskryptFullyQuantumRegister.raise_not_fully_quantum_register_error()
                            """
                            Return/Raise a Not a Fully-Quantum Register Error for the Qiskrypt's Fully-Quantum Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    for semi_quantum_register in qiskrypt_semi_quantum_registers:
                        """
                        For each supposed Qiskrypt's Semi-Quantum Register in the list of the Qiskrypt's Semi-Quantum Registers.
                        """

                        if not (isinstance(semi_quantum_register, QiskryptSemiQuantumRegister)):
                            """
                            If the current supposed Qiskrypt's Semi-Quantum Register is not an actual Qiskrypt's Semi-Quantum Register.
                            """

                            QiskryptSemiQuantumRegister.raise_not_semi_quantum_register_error()
                            """
                            Return/Raise a Not a Semi-Quantum Register Error for the Qiskrypt's Semi-Quantum Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    for ancilla_quantum_register in qiskrypt_ancilla_quantum_registers:
                        """
                        For each supposed Qiskrypt's Ancilla Quantum Register in the list of the Qiskrypt's Ancilla Quantum Registers.
                        """

                        if not (isinstance(ancilla_quantum_register, QiskryptAncillaQuantumRegister)):
                            """
                            If the current supposed Qiskrypt's Ancilla Quantum Register is not an actual Qiskrypt's Ancilla Quantum Register.
                            """

                            QiskryptAncillaQuantumRegister.raise_not_ancilla_quantum_register_error()
                            """
                            Return/Raise a Not an Ancilla Quantum Register Error for the Qiskrypt's Ancilla Quantum Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    for ancilla_semi_quantum_register in qiskrypt_ancilla_semi_quantum_registers:
                        """
                        For each supposed Qiskrypt's Ancilla Semi-Quantum Register in the list of the Qiskrypt's Ancilla Semi-Quantum Registers.
                        """

                        if not (isinstance(ancilla_semi_quantum_register, QiskryptAncillaSemiQuantumRegister)):
                            """
                            If the current supposed Qiskrypt's Ancilla Semi-Quantum Register is not an actual Qiskrypt's Ancilla Semi-Quantum Register.
                            """

                            QiskryptAncillaSemiQuantumRegister.raise_not_ancilla_semi_quantum_register_error()
                            """
                            Return/Raise a Not an Ancilla Semi-Quantum Register Error for the Qiskrypt's Ancilla Semi-Quantum Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    for classical_register in qiskrypt_classical_registers:
                        """
                        For each supposed Qiskrypt's Classical Register in the list of the Qiskrypt's Classical Registers.
                        """

                        if not (isinstance(classical_register, QiskryptClassicalRegister)):
                            """
                            If the current supposed Qiskrypt's Classical Register is not an actual Qiskrypt's Classical Register.
                            """

                            QiskryptClassicalRegister.raise_not_classical_register_error()
                            """
                            Return/Raise a Not a Classical Register Error for the Qiskrypt's Classical Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    self.qiskrypt_quantum_registers = qiskrypt_quantum_registers
                    """
                    Set the Qiskrypt's Quantum Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskrypt_fully_quantum_registers = qiskrypt_fully_quantum_registers
                    """
                    Set the Qiskrypt's Fully-Quantum Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskrypt_semi_quantum_registers = qiskrypt_semi_quantum_registers
                    """
                    Set the Qiskrypt's Semi-Quantum Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskrypt_ancilla_quantum_registers = qiskrypt_ancilla_quantum_registers
                    """
                    Set the Qiskrypt's Ancilla Quantum Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskrypt_ancilla_fully_quantum_registers = None
                    """
                    Set the Qiskrypt's Ancilla Fully-Quantum Registers of the Qiskrypt's Quantum Circuit, as None.
                    """

                    self.qiskrypt_ancilla_semi_quantum_registers = qiskrypt_ancilla_semi_quantum_registers
                    """
                    Set the Qiskrypt's Ancilla Semi-Quantum Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskrypt_classical_registers = qiskrypt_classical_registers
                    """
                    Set the Qiskrypt's Classical Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.global_phase = global_phase
                    """
                    Set the global phase of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskit_quantum_circuit = \
                        QuantumCircuit(
                            *[quantum_register.get_qiskit_quantum_register() for quantum_register in self.qiskrypt_quantum_registers],
                            *[fully_quantum_register.get_qiskit_fully_quantum_register() for fully_quantum_register in
                              self.qiskrypt_fully_quantum_registers],
                            *[semi_quantum_register.get_qiskit_semi_quantum_register() for semi_quantum_register in
                              self.qiskrypt_semi_quantum_registers],
                            *[ancilla_quantum_register.get_qiskit_ancilla_quantum_register() for ancilla_quantum_register in
                              self.qiskrypt_ancilla_quantum_registers],
                            *[ancilla_semi_quantum_register.get_qiskit_ancilla_semi_quantum_register() for
                              ancilla_semi_quantum_register in self.qiskrypt_ancilla_semi_quantum_registers],
                            *[classical_register.get_qiskit_classical_register() for classical_register in
                              self.qiskrypt_classical_registers],
                            name=name, global_phase=global_phase)
                    """
                    Set the IBM's Qiskit Quantum Circuit of the Qiskrypt's Quantum Circuit.
                    """

                else:
                    """
                    If the Qiskrypt's Quantum, Fully-Quantum, Semi-Quantum, Ancilla Quantum, Ancilla Semi-Quantum and Classical Registers are not lists.
                    """

                    """
                    Raise an Unsupported Type of Registers Error for the Qiskrypt's Quantum Circuit.
                    """
                    self.raise_unsupported_type_registers_error()

            elif (qiskrypt_quantum_registers is not None) and (qiskrypt_fully_quantum_registers is not None) and (
                    qiskrypt_semi_quantum_registers is not None) and \
                    (qiskrypt_ancilla_quantum_registers is not None) and (qiskrypt_ancilla_fully_quantum_registers is not None) and (
                    qiskrypt_ancilla_semi_quantum_registers is not None) and \
                    (qiskrypt_classical_registers is not None):
                """
                If the Qiskrypt's Quantum, Fully-Quantum, Semi-Quantum,
                Ancilla Quantum, Ancilla Fully-Quantum, Ancilla Semi-Quantum and Classical Registers given as arguments are not None
                (i.e., a Qiskrypt's Quantum Circuit equivalent to a hybrid Quantum/Fully-Quantum/Semi-Quantum/Ancilla Quantum/Ancilla Fully-Quantum/Ancilla Semi-Quantum/Classical Memory).
                """

                if (isinstance(qiskrypt_quantum_registers, list)) and (isinstance(qiskrypt_fully_quantum_registers, list)) and \
                        (isinstance(qiskrypt_semi_quantum_registers, list)) and (isinstance(qiskrypt_ancilla_quantum_registers, list)) and \
                        (isinstance(qiskrypt_ancilla_fully_quantum_registers, list)) and (isinstance(qiskrypt_ancilla_semi_quantum_registers, list)) and (isinstance(qiskrypt_classical_registers, list)):
                    """
                    If the Qiskrypt's Quantum, Fully-Quantum, Semi-Quantum, Ancilla Quantum, Ancilla Fully-Quantum, Ancilla Semi-Quantum and Classical Registers are lists.
                    """

                    for quantum_register in qiskrypt_quantum_registers:
                        """
                        For each supposed Qiskrypt's Quantum Register in the list of the Qiskrypt's Quantum Registers.
                        """

                        if not (isinstance(quantum_register, QiskryptQuantumRegister)):
                            """
                            If the current supposed Qiskrypt's Quantum Register is not an actual Qiskrypt's Quantum Register.
                            """

                            QiskryptQuantumRegister.raise_not_quantum_register_error()
                            """
                            Return/Raise a Not a Quantum Register Error for the Qiskrypt's Quantum Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    for fully_quantum_register in qiskrypt_fully_quantum_registers:
                        """
                        For each supposed Qiskrypt's Fully-Quantum Register in the list of the Qiskrypt's Fully-Quantum Registers.
                        """

                        if not (isinstance(fully_quantum_register, QiskryptFullyQuantumRegister)):
                            """
                            If the current supposed Qiskrypt's Fully-Quantum Register is not an actual Qiskrypt's Fully-Quantum Register.
                            """

                            QiskryptFullyQuantumRegister.raise_not_fully_quantum_register_error()
                            """
                            Return/Raise a Not a Fully-Quantum Register Error for the Qiskrypt's Fully-Quantum Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    for semi_quantum_register in qiskrypt_semi_quantum_registers:
                        """
                        For each supposed Qiskrypt's Semi-Quantum Register in the list of the Qiskrypt's Semi-Quantum Registers.
                        """

                        if not (isinstance(semi_quantum_register, QiskryptSemiQuantumRegister)):
                            """
                            If the current supposed Qiskrypt's Semi-Quantum Register is not an actual Qiskrypt's Semi-Quantum Register.
                            """

                            QiskryptSemiQuantumRegister.raise_not_semi_quantum_register_error()
                            """
                            Return/Raise a Not a Semi-Quantum Register Error for the Qiskrypt's Semi-Quantum Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    for ancilla_quantum_register in qiskrypt_ancilla_quantum_registers:
                        """
                        For each supposed Qiskrypt's Ancilla Quantum Register in the list of the Qiskrypt's Ancilla Quantum Registers.
                        """

                        if not (isinstance(ancilla_quantum_register, QiskryptAncillaQuantumRegister)):
                            """
                            If the current supposed Qiskrypt's Ancilla Quantum Register is not an actual Qiskrypt's Ancilla Quantum Register.
                            """

                            QiskryptAncillaQuantumRegister.raise_not_ancilla_quantum_register_error()
                            """
                            Return/Raise a Not an Ancilla Quantum Register Error for the Qiskrypt's Ancilla Quantum Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    for ancilla_fully_quantum_register in qiskrypt_ancilla_fully_quantum_registers:
                        """
                        For each supposed Qiskrypt's Ancilla Fully-Quantum Register in the list of the Qiskrypt's Ancilla Fully-Quantum Registers.
                        """

                        if not (isinstance(ancilla_fully_quantum_register, QiskryptAncillaFullyQuantumRegister)):
                            """
                            If the current supposed Qiskrypt's Ancilla Fully-Quantum Register is not an actual Qiskrypt's Ancilla Fully-Quantum Register.
                            """

                            QiskryptAncillaFullyQuantumRegister.raise_not_ancilla_fully_quantum_register_error()
                            """
                            Return/Raise a Not an Ancilla Fully-Quantum Register Error for the Qiskrypt's Ancilla Fully-Quantum Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    for ancilla_semi_quantum_register in qiskrypt_ancilla_semi_quantum_registers:
                        """
                        For each supposed Qiskrypt's Ancilla Semi-Quantum Register in the list of the Qiskrypt's Ancilla Semi-Quantum Registers.
                        """

                        if not (isinstance(ancilla_semi_quantum_register, QiskryptAncillaSemiQuantumRegister)):
                            """
                            If the current supposed Qiskrypt's Ancilla Semi-Quantum Register is not an actual Qiskrypt's Ancilla Semi-Quantum Register.
                            """

                            QiskryptAncillaSemiQuantumRegister.raise_not_ancilla_semi_quantum_register_error()
                            """
                            Return/Raise a Not an Ancilla Semi-Quantum Register Error for the Qiskrypt's Ancilla Semi-Quantum Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    for classical_register in qiskrypt_classical_registers:
                        """
                        For each supposed Qiskrypt's Classical Register in the list of the Qiskrypt's Classical Registers.
                        """

                        if not (isinstance(classical_register, QiskryptClassicalRegister)):
                            """
                            If the current supposed Qiskrypt's Classical Register is not an actual Qiskrypt's Classical Register.
                            """

                            QiskryptClassicalRegister.raise_not_classical_register_error()
                            """
                            Return/Raise a Not a Classical Register Error for the Qiskrypt's Classical Register.
                            """

                            """
                            Break the current for loop.
                            """
                            break

                    self.qiskrypt_quantum_registers = qiskrypt_quantum_registers
                    """
                    Set the Qiskrypt's Quantum Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskrypt_fully_quantum_registers = qiskrypt_fully_quantum_registers
                    """
                    Set the Qiskrypt's Fully-Quantum Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskrypt_semi_quantum_registers = qiskrypt_semi_quantum_registers
                    """
                    Set the Qiskrypt's Semi-Quantum Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskrypt_ancilla_quantum_registers = qiskrypt_ancilla_quantum_registers
                    """
                    Set the Qiskrypt's Ancilla Quantum Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskrypt_ancilla_fully_quantum_registers = qiskrypt_ancilla_fully_quantum_registers
                    """
                    Set the Qiskrypt's Ancilla Fully-Quantum Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskrypt_ancilla_semi_quantum_registers = qiskrypt_ancilla_semi_quantum_registers
                    """
                    Set the Qiskrypt's Ancilla Semi-Quantum Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskrypt_classical_registers = qiskrypt_classical_registers
                    """
                    Set the Qiskrypt's Classical Registers of the Qiskrypt's Quantum Circuit.
                    """

                    self.global_phase = global_phase
                    """
                    Set the global phase of the Qiskrypt's Quantum Circuit.
                    """

                    self.qiskit_quantum_circuit = \
                        QuantumCircuit(
                            *[quantum_register.get_qiskit_quantum_register() for quantum_register in self.qiskrypt_quantum_registers],
                            *[fully_quantum_register.get_qiskit_fully_quantum_register() for fully_quantum_register in
                              self.qiskrypt_fully_quantum_registers],
                            *[semi_quantum_register.get_qiskit_semi_quantum_register() for semi_quantum_register in
                              self.qiskrypt_semi_quantum_registers],
                            *[ancilla_quantum_register.get_qiskit_ancilla_quantum_register() for ancilla_quantum_register in
                              self.qiskrypt_ancilla_quantum_registers],
                            *[ancilla_fully_quantum_register.get_qiskit_ancilla_fully_quantum_register() for
                              ancilla_fully_quantum_register in self.qiskrypt_ancilla_fully_quantum_registers],
                            *[ancilla_semi_quantum_register.get_qiskit_ancilla_semi_quantum_register() for
                              ancilla_semi_quantum_register in self.qiskrypt_ancilla_semi_quantum_registers],
                            *[classical_register.get_qiskit_classical_register() for classical_register in
                              self.qiskrypt_classical_registers],
                            name=name, global_phase=global_phase)
                    """
                    Set the IBM's Qiskit Quantum Circuit of the Qiskrypt's Quantum Circuit.
                    """

                else:
                    """
                    If the Qiskrypt's Quantum, Fully-Quantum, Semi-Quantum, Ancilla Quantum, Ancilla Fully-Quantum, Ancilla Semi-Quantum and Classical Registers are not lists.
                    """

                    """
                    Raise an Unsupported Type of Registers Error for the Qiskrypt's Quantum Circuit.
                    """
                    self.raise_unsupported_type_registers_error()

        else:
            """
            If there is given any IBM's Quantum Circuit, it will be used.
            """

            num_qiskit_quantum_registers = len(qiskit_quantum_circuit.qregs)
            """
            Retrieve the number of IBM Qiskit's Quantum Registers.
            """

            qiskrypt_quantum_registers = []
            """
            Create a new list of Qiskrypt's Quantum Registers.
            """

            for qiskit_quantum_register_index in range(num_qiskit_quantum_registers):
                """
                For each index of a IBM Qiskit's Quantum Register.
                """

                qiskit_quantum_register = qiskit_quantum_circuit.qregs[qiskit_quantum_register_index]
                """
                Retrieve the current IBM Qiskit's Quantum Register.
                """

                qiskit_quantum_register_name = qiskit_quantum_register.name
                """
                Retrieve the name of the current IBM Qiskit's Quantum Register.
                """

                qiskit_quantum_register_num_qubits = qiskit_quantum_register.size
                """
                Retrieve the number of qubits of the current IBM Qiskit's Quantum Register.
                """

                qiskrypt_quantum_register = QiskryptQuantumRegister(qiskit_quantum_register_name,
                                                                    qiskit_quantum_register_num_qubits,
                                                                    qiskit_quantum_register)
                """
                Create the Qiskrypt's Quantum Register from the retrieved IBM Qiskit's Quantum Register.
                """

                qiskrypt_quantum_registers.append(qiskrypt_quantum_register)
                """
                Append the created Qiskrypt's Quantum Register to
                the list of the Qiskrypt's Quantum Registers.
                """

            num_qiskit_classical_registers = len(qiskit_quantum_circuit.cregs)
            """
            Retrieve the number of IBM Qiskit's Classical Registers.
            """

            qiskrypt_classical_registers = []
            """
            Create a new list of Qiskrypt's Classical Registers.
            """

            for qiskit_classical_register_index in range(num_qiskit_classical_registers):
                """
                For each index of a IBM Qiskit's Classical Register.
                """

                qiskit_classical_register = qiskit_quantum_circuit.cregs[qiskit_classical_register_index]
                """
                Retrieve the current IBM Qiskit's Classical Register.
                """

                qiskit_classical_register_name = qiskit_classical_register.name
                """
                Retrieve the name of the current IBM Qiskit's Classical Register.
                """

                qiskit_classical_register_num_bits = qiskit_classical_register.size
                """
                Retrieve the number of bits of the current IBM Qiskit's Classical Register.
                """

                qiskrypt_classical_register = QiskryptClassicalRegister(qiskit_classical_register_name,
                                                                        qiskit_classical_register_num_bits,
                                                                        qiskit_classical_register)
                """
                Create the Qiskrypt's Classical Register from the retrieved IBM Qiskit's Classical Register.
                """

                qiskrypt_classical_registers.append(qiskrypt_classical_register)
                """
                Append the created Qiskrypt's Classical Register to
                the list of the Qiskrypt's Classical Registers.
                """

            self.qiskrypt_quantum_registers = qiskrypt_quantum_registers
            """
            Set the Qiskrypt's Quantum Registers from the respective list of them.
            """

            self.qiskrypt_fully_quantum_registers = None
            """
            Set the Qiskrypt's Fully-Quantum Registers as None.
            """

            self.qiskrypt_semi_quantum_registers = None
            """
            Set the Qiskrypt's Semi-Quantum Registers as None.
            """

            self.qiskrypt_ancilla_quantum_registers = None
            """
            Set the Qiskrypt's Ancilla Quantum Registers as None.
            """

            self.qiskrypt_ancilla_fully_quantum_registers = None
            """
            Set the Qiskrypt's Ancilla Fully-Quantum Registers as None.
            """

            self.qiskrypt_ancilla_semi_quantum_registers = None
            """
            Set the Qiskrypt's Ancilla Semi-Quantum Registers as None.
            """

            self.qiskrypt_classical_registers = qiskrypt_classical_registers
            """
            Set the Qiskrypt's Classical Registers from the respective list of them.
            """

            self.qiskit_quantum_circuit = qiskit_quantum_circuit
            """
            Set the given IBM's Qiskit Quantum Circuit of the Qiskrypt's Quantum Circuit.
            """

    """
    1) Basic and Fundamental Methods:
    """

    def get_name(self) -> str:
        """
        Return the name of the Qiskrypt's Quantum Circuit.

        :return self.name: the name of the Qiskrypt's Quantum Circuit.
        """

        """
        Return the name of the Qiskrypt's Quantum Circuit.
        """
        return self.name

    def get_qiskrypt_quantum_registers(self) -> list:
        """
        Return the Qiskrypt's Quantum Registers of the Qiskrypt's Quantum Circuit.

        :return self.qiskrypt_quantum_registers: the Qiskrypt's Quantum Registers of the Qiskrypt's Quantum Circuit.
        """

        """
        Return the Qiskrypt's Quantum Registers of the Qiskrypt's Quantum Circuit.
        """
        return self.qiskrypt_quantum_registers

    def get_qiskrypt_fully_quantum_registers(self) -> list:
        """
        Return the Qiskrypt's Fully-Quantum Registers of the Qiskrypt's Quantum Circuit.

        :return self.qiskrypt_fully_quantum_registers: the Qiskrypt's Fully-Quantum Registers of the Qiskrypt's Quantum Circuit.
        """

        """
        Return the Qiskrypt's Fully-Quantum Registers of the Qiskrypt's Quantum Circuit.
        """
        return self.qiskrypt_fully_quantum_registers

    def get_qiskrypt_semi_quantum_registers(self) -> list:
        """
        Return the Qiskrypt's Semi-Quantum Registers of the Qiskrypt's Quantum Circuit.

        :return self.qiskrypt_semi_quantum_registers: the Qiskrypt's Semi-Quantum Registers of the Qiskrypt's Quantum Circuit.
        """

        """
        Return the Qiskrypt's Semi-Quantum Registers of the Qiskrypt's Quantum Circuit.
        """
        return self.qiskrypt_semi_quantum_registers

    def get_qiskrypt_ancilla_quantum_registers(self) -> list:
        """
        Return the Qiskrypt's Ancilla Quantum Registers of the Qiskrypt's Quantum Circuit.

        :return self.qiskrypt_ancilla_quantum_registers: the Qiskrypt's Ancilla Quantum Registers of the Qiskrypt's Quantum Circuit.
        """

        """
        Return the Qiskrypt's Ancilla Quantum Registers of the Qiskrypt's Quantum Circuit.
        """
        return self.qiskrypt_ancilla_quantum_registers

    def get_qiskrypt_ancilla_fully_quantum_registers(self) -> list:
        """
        Return the Qiskrypt's Ancilla Fully-Quantum Registers of the Qiskrypt's Quantum Circuit.

        :return self.qiskrypt_ancilla_fully_quantum_registers: the Qiskrypt's Ancilla Fully-Quantum Registers of the Qiskrypt's Quantum Circuit.
        """

        """
        Return the Qiskrypt's Ancilla Fully-Quantum Registers of the Qiskrypt's Quantum Circuit.
        """
        return self.qiskrypt_ancilla_fully_quantum_registers

    def get_qiskrypt_ancilla_semi_quantum_registers(self) -> list:
        """
        Return the Qiskrypt's Ancilla Semi-Quantum Registers of the Qiskrypt's Quantum Circuit.

        :return self.qiskrypt_ancilla_semi_quantum_registers: the Qiskrypt's Ancilla Semi-Quantum Registers of the Qiskrypt's Quantum Circuit.
        """

        """
        Return the Qiskrypt's Ancilla Semi-Quantum Registers of the Qiskrypt's Quantum Circuit.
        """
        return self.qiskrypt_ancilla_semi_quantum_registers

    def get_qiskrypt_classical_registers(self) -> list:
        """
        Return the Qiskrypt's Classical Registers of the Qiskrypt's Quantum Circuit.

        :return self.qiskrypt_classical_registers: the Qiskrypt's Classical Registers of the Qiskrypt's Quantum Circuit.
        """

        """
        Return the Qiskrypt's Classical Registers of the Qiskrypt's Quantum Circuit.
        """
        return self.qiskrypt_classical_registers

    def get_qiskrypt_quantum_register(self, qiskrypt_quantum_register_index: int) -> QiskryptQuantumRegister:
        """
        Return a specific Qiskrypt's Quantum Register of the Qiskrypt's Quantum Circuit, given its index.

        :param qiskrypt_quantum_register_index: the index of the Qiskrypt's Quantum Register of the Qiskrypt's Quantum Circuit.

        :return self.qiskrypt_quantum_registers[qiskrypt_quantum_register_index]: a specific Qiskrypt's Quantum Register of
                                                                                  the Qiskrypt's Quantum Circuit, given its index.
        """

        if qiskrypt_quantum_register_index < self.get_num_qiskrypt_quantum_registers():
            """
            If the given index for the specific Qiskrypt's Quantum Register of
            the Qiskrypt's Quantum Circuit is valid.
            """

            """
            Return a specific Qiskrypt's Quantum Register of the Qiskrypt's Quantum Circuit, given its index.
            """
            return self.qiskrypt_quantum_registers[qiskrypt_quantum_register_index]

        else:
            """
            If the given index for the specific Qiskrypt's Quantum Register of
            the Qiskrypt's Quantum Circuit is not valid.
            """

            """
            Raise a Not a Valid Qiskrypt's Quantum Register Index Given Error for the Qiskrypt's Quantum Circuit.
            """
            QiskryptQuantumRegister.raise_not_valid_qiskrypt_quantum_register_index_error()

    def get_qiskrypt_fully_quantum_register(self, qiskrypt_fully_quantum_register_index: int) -> QiskryptFullyQuantumRegister:
        """
        Return a specific Qiskrypt's Fully-Quantum Register of the Qiskrypt's Quantum Circuit, given its index.

        :param qiskrypt_fully_quantum_register_index: the index of the Qiskrypt's Fully-Quantum Register of the Qiskrypt's Quantum Circuit.

        :return self.qiskrypt_fully_quantum_registers[qiskrypt_fully_quantum_register_index]: a specific Qiskrypt's Fully-Quantum Register of
                                                                                              the Qiskrypt's Quantum Circuit, given its index.
        """

        if qiskrypt_fully_quantum_register_index < self.get_num_qiskrypt_fully_quantum_registers():
            """
            If the given index for the specific Qiskrypt's Fully-Quantum Register of
            the Qiskrypt's Quantum Circuit is valid.
            """

            """
            Return a specific Qiskrypt's Fully-Quantum Register of the Qiskrypt's Quantum Circuit, given its index.
            """
            return self.qiskrypt_fully_quantum_registers[qiskrypt_fully_quantum_register_index]

        else:
            """
            If the given index for the specific Qiskrypt's Fully-Quantum Register of
            the Qiskrypt's Quantum Circuit is not valid.
            """

            """
            Raise a Not a Valid Qiskrypt's Fully-Quantum Register Index Given Error for
            the Qiskrypt's Quantum Circuit.
            """
            QiskryptFullyQuantumRegister.raise_not_valid_qiskrypt_fully_quantum_register_index_error()

    def get_qiskrypt_semi_quantum_register(self, qiskrypt_semi_quantum_register_index: int) -> QiskryptSemiQuantumRegister:
        """
        Return a specific Qiskrypt's Semi-Quantum Register of the Qiskrypt's Quantum Circuit, given its index.

        :param qiskrypt_semi_quantum_register_index: the index of the Qiskrypt's Semi-Quantum Register of the Qiskrypt's Quantum Circuit.

        :return self.qiskrypt_semi_quantum_registers[qiskrypt_semi_quantum_register_index]: a specific Qiskrypt's Semi-Quantum Register of
                                                                                            the Qiskrypt's Quantum Circuit, given its index.
        """

        if qiskrypt_semi_quantum_register_index < self.get_num_qiskrypt_semi_quantum_registers():
            """
            If the given index for the specific Qiskrypt's Semi-Quantum Register of
            the Qiskrypt's Quantum Circuit is valid.
            """

            """
            Return a specific Qiskrypt's Semi-Quantum Register of the Qiskrypt's Quantum Circuit, given its index.
            """
            return self.qiskrypt_semi_quantum_registers[qiskrypt_semi_quantum_register_index]

        else:
            """
            If the given index for the specific Qiskrypt's Semi-Quantum Register of
            the Qiskrypt's Quantum Circuit is not valid.
            """

            """
            Raise a Not a Valid Qiskrypt's Semi-Quantum Register Index Given Error for
            the Qiskrypt's Quantum Circuit.
            """
            QiskryptSemiQuantumRegister.raise_not_valid_qiskrypt_semi_quantum_register_index_error()

    def get_qiskrypt_ancilla_quantum_register(self, qiskrypt_ancilla_quantum_register_index: int) -> QiskryptAncillaQuantumRegister:
        """
        Return a specific Qiskrypt's Ancilla Quantum Register of the Qiskrypt's Quantum Circuit, given its index.

        :param qiskrypt_ancilla_quantum_register_index: the index of the Qiskrypt's Ancilla Quantum Register of the Qiskrypt's Quantum Circuit.

        :return self.qiskrypt_ancilla_quantum_registers[qiskrypt_ancilla_quantum_register_index]: a specific Qiskrypt's Ancilla Quantum Register of
                                                                                         the Qiskrypt's Quantum Circuit, given its index.
        """

        if qiskrypt_ancilla_quantum_register_index < self.get_num_qiskrypt_ancilla_quantum_registers():
            """
            If the given index for the specific Qiskrypt's Ancilla Quantum Register of
            the Qiskrypt's Quantum Circuit is valid.
            """

            """
            Return a specific Qiskrypt's Ancilla Quantum Register of the Qiskrypt's Quantum Circuit, given its index.
            """
            return self.qiskrypt_ancilla_quantum_registers[qiskrypt_ancilla_quantum_register_index]

        else:
            """
            If the given index for the specific Qiskrypt's Ancilla Quantum Register of
            the Qiskrypt's Quantum Circuit is not valid.
            """

            """
            Raise a Not a Valid Qiskrypt's Ancilla Quantum Register Index Given Error for
            the Qiskrypt's Quantum Circuit.
            """
            QiskryptAncillaQuantumRegister.raise_not_valid_qiskrypt_ancilla_quantum_register_index_error()

    def get_qiskrypt_ancilla_fully_quantum_register(self, qiskrypt_ancilla_fully_quantum_register_index: int) -> QiskryptAncillaFullyQuantumRegister:
        """
        Return a specific Qiskrypt's Ancilla Fully-Quantum Register of the Qiskrypt's Quantum Circuit, given its index.

        :param qiskrypt_ancilla_fully_quantum_register_index: the index of the Qiskrypt's Ancilla Fully-Quantum Register of the Qiskrypt's Quantum Circuit.

        :return self.qiskrypt_ancilla_fully_quantum_registers[qiskrypt_ancilla_fully_quantum_register_index]: a specific Qiskrypt's Ancilla Fully-Quantum Register of
                                                                                                              the Qiskrypt's Quantum Circuit, given its index.
        """

        if qiskrypt_ancilla_fully_quantum_register_index < self.get_num_qiskrypt_ancilla_fully_quantum_registers():
            """
            If the given index for the specific Qiskrypt's Ancilla Fully-Quantum Register of
            the Qiskrypt's Quantum Circuit is valid.
            """

            """
            Return a specific Qiskrypt's Ancilla Fully-Quantum Register of the Qiskrypt's Quantum Circuit, given its index.
            """
            return self.qiskrypt_ancilla_fully_quantum_registers[qiskrypt_ancilla_fully_quantum_register_index]

        else:
            """
            If the given index for the specific Qiskrypt's Ancilla Fully-Quantum Register of
            the Qiskrypt's Quantum Circuit is not valid.
            """

            """
            Raise a Not a Valid Qiskrypt's Ancilla Fully-Quantum Register Index Given Error for
            the Qiskrypt's Quantum Circuit.
            """
            QiskryptAncillaFullyQuantumRegister.raise_not_valid_qiskrypt_ancilla_fully_quantum_register_index_error()

    def get_qiskrypt_ancilla_semi_quantum_register(self, qiskrypt_ancilla_semi_quantum_register_index: int) -> QiskryptAncillaSemiQuantumRegister:
        """
        Return a specific Qiskrypt's Ancilla Semi-Quantum Register of the Qiskrypt's Quantum Circuit, given its index.

        :param qiskrypt_ancilla_semi_quantum_register_index: the index of the Qiskrypt's Ancilla Semi-Quantum Register of the Qiskrypt's Quantum Circuit.

        :return self.qiskrypt_ancilla_semi_quantum_registers[qiskrypt_ancilla_semi_quantum_register_index]: a specific Qiskrypt's Ancilla Semi-Quantum Register of
                                                                                                            the Qiskrypt's Quantum Circuit, given its index.
        """

        if qiskrypt_ancilla_semi_quantum_register_index < self.get_num_qiskrypt_ancilla_semi_quantum_registers():
            """
            If the given index for the specific Qiskrypt's Ancilla Semi-Quantum Register of
            the Qiskrypt's Quantum Circuit is valid.
            """

            """
            Return a specific Qiskrypt's Ancilla Semi-Quantum Register of the Qiskrypt's Quantum Circuit, given its index.
            """
            return self.qiskrypt_ancilla_semi_quantum_registers[qiskrypt_ancilla_semi_quantum_register_index]

        else:
            """
            If the given index for the specific Qiskrypt's Ancilla Semi-Quantum Register of
            the Qiskrypt's Quantum Circuit is not valid.
            """

            """
            Raise a Not a Valid Qiskrypt's Ancilla Semi-Quantum Register Index Given Error for
            the Qiskrypt's Quantum Circuit.
            """
            QiskryptAncillaSemiQuantumRegister.raise_not_valid_qiskrypt_ancilla_semi_quantum_register_index_error()

    def get_qiskrypt_classical_register(self, qiskrypt_classical_register_index: int) -> QiskryptClassicalRegister:
        """
        Return a specific Qiskrypt's Classical Register of the Qiskrypt's Quantum Circuit, given its index.

        :param qiskrypt_classical_register_index: the index of the Qiskrypt's Classical Register of the Qiskrypt's Quantum Circuit.

        :return self.qiskrypt_classical_registers[qiskrypt_classical_register_index]: a specific Qiskrypt's Classical Register of
                                                                                      the Qiskrypt's Quantum Circuit, given its index.
        """

        if qiskrypt_classical_register_index < self.get_num_qiskrypt_classical_registers():
            """
            If the given index for the specific Qiskrypt's Classical Register of
            the Qiskrypt's Quantum Circuit is valid.
            """

            """
            Return a specific Qiskrypt's Classical Register of the Qiskrypt's Quantum Circuit, given its index.
            """
            return self.qiskrypt_classical_registers[qiskrypt_classical_register_index]

        else:
            """
            If the given index for the specific Qiskrypt's Classical Register of
            the Qiskrypt's Quantum Circuit is not valid.
            """

            """
            Raise a Not a Valid Qiskrypt's Classical Register Index Given Error for
            the Qiskrypt's Quantum Circuit.
            """
            QiskryptClassicalRegister.raise_not_valid_qiskrypt_classical_register_index_error()

    def find_qiskrypt_register_by_name(self, register_name: str) -> Tuple[bool, object]:
        """
        Return the Qiskrypt's Register in the Qiskrypt's Quantum Circuit with the given name.
        It returns the answer to the query, in the form of a Tuple [bool, object],
        with the Tuple [True, Register] if it is found. Or a Tuple [False, None], otherwise.

        :param register_name: the name of the Qiskrypt's Register to be found.

        :return: the Qiskrypt's Register in the Qiskrypt's Quantum Circuit with the given name.
                 It returns the answer to the query, in the form of a Tuple [bool, object],
                 with the Tuple [True, Register] if it is found. Or a Tuple [False, None], otherwise.
        """

        qiskrypt_quantum_registers = self.get_qiskrypt_quantum_registers()
        """
        Retrieve the list of the Qiskrypt's Quantum Registers.
        """

        for qiskrypt_quantum_register in qiskrypt_quantum_registers:
            """
            For each Qiskrypt's Quantum Register in the list of
            the Qiskrypt's Quantum Registers.
            """

            if qiskrypt_quantum_register.get_name() == register_name:
                """
                If it was found a Qiskrypt's Quantum Register with the given name.
                """

                """
                Returns True a Tuple of True and the Register's object.
                """
                return True, qiskrypt_quantum_register

        qiskrypt_fully_quantum_registers = self.get_qiskrypt_fully_quantum_registers()
        """
        Retrieve the list of the Qiskrypt's Fully-Quantum Registers.
        """

        for qiskrypt_fully_quantum_register in qiskrypt_fully_quantum_registers:
            """
            For each Qiskrypt's Fully-Quantum Register in the list of
            the Qiskrypt's Fully-Quantum Registers.
            """

            if qiskrypt_fully_quantum_register.get_name() == register_name:
                """
                If it was found a Qiskrypt's Fully-Quantum Register with the given name.
                """

                """
                Returns True a Tuple of True and the Register's object.
                """
                return True, qiskrypt_fully_quantum_register

        qiskrypt_semi_quantum_registers = self.get_qiskrypt_semi_quantum_registers()
        """
        Retrieve the list of the Qiskrypt's Semi-Quantum Registers.
        """

        for qiskrypt_semi_quantum_register in qiskrypt_semi_quantum_registers:
            """
            For each Qiskrypt's Semi-Quantum Register in the list of
            the Qiskrypt's Semi-Quantum Registers.
            """

            if qiskrypt_semi_quantum_register.get_name() == register_name:
                """
                If it was found a Qiskrypt's Semi-Quantum Register with the given name.
                """

                """
                Returns True a Tuple of True and the Register's object.
                """
                return True, qiskrypt_semi_quantum_register

        qiskrypt_ancilla_quantum_registers = self.get_qiskrypt_ancilla_quantum_registers()
        """
        Retrieve the list of the Qiskrypt's Ancilla Quantum Registers.
        """

        for qiskrypt_ancilla_quantum_register in qiskrypt_ancilla_quantum_registers:
            """
            For each Qiskrypt's Ancilla Quantum Register in the list of
            the Qiskrypt's Ancilla Quantum Registers.
            """

            if qiskrypt_ancilla_quantum_register.get_name() == register_name:
                """
                If it was found a Qiskrypt's Ancilla Quantum Register with the given name.
                """

                """
                Returns True a Tuple of True and the Register's object.
                """
                return True, qiskrypt_ancilla_quantum_register

        qiskrypt_ancilla_fully_quantum_registers = self.get_qiskrypt_ancilla_fully_quantum_registers()
        """
        Retrieve the list of the Qiskrypt's Ancilla Fully-Quantum Registers.
        """

        for qiskrypt_ancilla_fully_quantum_register in qiskrypt_ancilla_fully_quantum_registers:
            """
            For each Qiskrypt's Ancilla Fully-Quantum Register in the list of
            the Qiskrypt's Ancilla Fully-Quantum Registers.
            """

            if qiskrypt_ancilla_fully_quantum_register.get_name() == register_name:
                """
                If it was found a Qiskrypt's Ancilla Fully-Quantum Register with the given name.
                """

                """
                Returns True a Tuple of True and the Register's object.
                """
                return True, qiskrypt_ancilla_fully_quantum_register

        qiskrypt_ancilla_semi_quantum_registers = self.get_qiskrypt_semi_quantum_registers()
        """
        Retrieve the list of the Qiskrypt's Ancilla Semi-Quantum Registers.
        """

        for qiskrypt_ancilla_semi_quantum_register in qiskrypt_ancilla_semi_quantum_registers:
            """
            For each Qiskrypt's Ancilla Semi-Quantum Register in the list of
            the Qiskrypt's Ancilla Semi-Quantum Registers.
            """

            if qiskrypt_ancilla_semi_quantum_register.get_name() == register_name:
                """
                If it was found a Qiskrypt's Ancilla Semi-Quantum Register with the given name.
                """

                """
                Returns True a Tuple of True and the Register's object.
                """
                return True, qiskrypt_ancilla_semi_quantum_register

        """
        If no Register was found with the given name, returns a Tuple of False and None.
        """
        return False, None

    def get_num_qiskrypt_quantum_registers(self) -> int:
        """
        Return the number of Qiskrypt's Quantum Registers of the Qiskrypt's Quantum Circuit.

        :return len(self.get_qiskrypt_quantum_registers()): the number of Qiskrypt's Quantum Registers of
                                                            the Qiskrypt's Quantum Circuit.
        """

        """
        Return the number of Qiskrypt's Quantum Registers of the Qiskrypt's Quantum Circuit.
        """
        return len(self.get_qiskrypt_quantum_registers())

    def get_num_qiskrypt_fully_quantum_registers(self) -> int:
        """
        Return the number of Qiskrypt's Fully-Quantum Registers of the Qiskrypt's Quantum Circuit.

        :return len(self.get_qiskrypt_fully_quantum_registers()): the number of Qiskrypt's Fully-Quantum Registers of
                                                                  the Qiskrypt's Quantum Circuit.
        """

        """
        Return the number of Qiskrypt's Fully-Quantum Registers of the Qiskrypt's Quantum Circuit.
        """
        return len(self.get_qiskrypt_fully_quantum_registers())

    def get_num_qiskrypt_semi_quantum_registers(self) -> int:
        """
        Return the number of Qiskrypt's Semi-Quantum Registers of the Qiskrypt's Quantum Circuit.

        :return len(self.get_qiskrypt_semi_quantum_registers()): the number of Qiskrypt's Semi-Quantum Registers of
                                                                 the Qiskrypt's Quantum Circuit.
        """

        """
        Return the number of Qiskrypt's Semi-Quantum Registers of the Qiskrypt's Quantum Circuit.
        """
        return len(self.get_qiskrypt_semi_quantum_registers())

    def get_num_qiskrypt_ancilla_quantum_registers(self) -> int:
        """
        Return the number of Qiskrypt's Ancilla Quantum Registers of the Qiskrypt's Quantum Circuit.

        :return len(self.get_qiskrypt_ancilla_quantum_registers()): the number of Qiskrypt's Ancilla Quantum Registers of
                                                                    the Qiskrypt's Quantum Circuit.
        """

        """
        Return the number of Qiskrypt's Ancilla Quantum Registers of the Qiskrypt's Quantum Circuit.
        """
        return len(self.get_qiskrypt_ancilla_quantum_registers())

    def get_num_qiskrypt_ancilla_fully_quantum_registers(self) -> int:
        """
        Return the number of Qiskrypt's Ancilla Fully-Quantum Registers of the Qiskrypt's Quantum Circuit.

        :return len(self.get_qiskrypt_ancilla_fully_quantum_registers()): the number of Qiskrypt's Ancilla Fully-Quantum Registers of
                                                                          the Qiskrypt's Quantum Circuit.
        """

        """
        Return the number of Qiskrypt's Ancilla Fully-Quantum Registers of the Qiskrypt's Quantum Circuit.
        """
        return len(self.get_qiskrypt_ancilla_fully_quantum_registers())

    def get_num_qiskrypt_ancilla_semi_quantum_registers(self) -> int:
        """
        Return the number of Qiskrypt's Ancilla Semi-Quantum Registers of the Qiskrypt's Quantum Circuit.

        :return len(self.get_qiskrypt_ancilla_semi_quantum_registers()): the number of Qiskrypt's Ancilla Semi-Quantum Registers of
                                                                         the Qiskrypt's Quantum Circuit.
        """

        """
        Return the number of Qiskrypt's Ancilla Semi-Quantum Registers of the Qiskrypt's Quantum Circuit.
        """
        return len(self.get_qiskrypt_ancilla_semi_quantum_registers())

    def get_num_qiskrypt_classical_registers(self) -> int:
        """
        Return the number of Qiskrypt's Classical Registers of the Qiskrypt's Quantum Circuit.

        :return len(self.get_qiskrypt_classical_registers()): the number of Qiskrypt's Classical Registers of
                                                              the Qiskrypt's Quantum Circuit.
        """

        """
        Return the number of Qiskrypt's Classical Registers of the Qiskrypt's Quantum Circuit.
        """
        return len(self.get_qiskrypt_classical_registers())

    def get_global_phase(self) -> float:
        """
        Return the global phase of the Qiskrypt's Quantum Circuit.

        :return self.global_phase: the global phase of the Qiskrypt's Quantum Circuit.
        """

        """
        Return the global phase of the Qiskrypt's Quantum Circuit.
        """
        return self.global_phase

    def get_total_num_qubits(self) -> int:
        """
        Return the total number of qubits of the Qiskrypt's Quantum Circuit.

        :return self.quantum_circuit.num_qubits: the total number of qubits of
                                                 the Qiskrypt's Quantum Circuit.
        """

        """
        Return the total number of qubits of the Qiskrypt's Quantum Circuit.
        """
        return self.qiskit_quantum_circuit.num_qubits

    def get_total_num_bits(self) -> int:
        """
        Return the total number of bits of the Qiskrypt's Quantum Circuit.

        :return self.quantum_circuit.num_qubits: the total number of bits of
                                                 the Qiskrypt's Quantum Circuit.
        """

        """
        Return the total number of bits of the Qiskrypt's Quantum Circuit.
        """
        return self.qiskit_quantum_circuit.num_clbits

    def get_num_qubits_in_qiskit_quantum_register(self, qiskit_quantum_register_index: int) -> int:
        """
        Return the number of qubits in a given quantum register of the Qiskrypt's Quantum Circuit.

        :param qiskit_quantum_register_index: the IBM Qiskit's Quantum Register index.

        :return self.quantum_circuit.qregs[qiskit_quantum_register_index].size: the number of qubits in
                                                                                a given quantum register of
                                                                                the Qiskrypt's Quantum Circuit.
        """

        """
        Return the number of qubits in a given IBM Qiskit's Quantum Register of the Qiskrypt's Quantum Circuit.
        """
        return self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_index].size

    def get_num_bits_in_qiskit_classical_register(self, qiskit_classical_register_index: int) -> int:
        """
        Return the number of bits in a given IBM Qiskit's Classical Register of the Qiskrypt's Quantum Circuit.

        :param qiskit_classical_register_index: the IBM Qiskit's Classical Register index.

        :return self.quantum_circuit.qregs[qiskit_classical_register_index].size: the number of bits in
                                                                                  a given classical register of
                                                                                  the Qiskrypt's Quantum Circuit.
        """

        """
        Return the number of bits in a given IBM Qiskit's Classical Register of the Qiskrypt's Quantum Circuit.
        """
        return self.qiskit_quantum_circuit.cregs[qiskit_classical_register_index].size

    def get_reversed_qiskit_quantum_circuit_operations(self) -> QuantumCircuit:
        """
        Return the reversed IBM Qiskit's Quantum Circuit of
        the Qiskrypt's Quantum Circuit
        (i.e., with the reversed order of Quantum Gates/Operations).

        :return self.quantum_circuit.reverse_ops(): the reversed IBM Qiskit's Quantum Circuit of
                                                    the Qiskrypt's Quantum Circuit.
        """

        """
        Return the reversed IBM Qiskit's Quantum Circuit of
        the Qiskrypt's Quantum Circuit
        (i.e., with the reversed order of Quantum Gates/Operations).
        """
        return self.qiskit_quantum_circuit.reverse_ops()

    def get_qiskit_quantum_circuit_with_reversed_wires_order(self) -> QuantumCircuit:
        """
        Return the IBM Qiskit's Quantum Circuit of
        the Qiskrypt's Quantum Circuit, with the reversed order of wires
        (i.e., the IBM Qiskit's Quantum Circuit is "vertically" flipped).

        :return self.quantum_circuit.reverse_bits(): the IBM Qiskit's Quantum Circuit of
                                                     the Qiskrypt's Quantum Circuit,
                                                     with the reversed order of wires.
        """

        """
        Return the IBM Qiskit's Quantum Circuit of
        the Qiskrypt's Quantum Circuit, with the reversed order of wires
        (i.e., the IBM Qiskit's Quantum Circuit is "vertically" flipped).
        """
        return self.qiskit_quantum_circuit.reverse_bits()

    def get_inverted_qiskit_quantum_circuit(self) -> QuantumCircuit:
        """
        Return the inverted IBM Qiskit's Quantum Circuit of
        the Qiskrypt's Quantum Circuit
        (i.e., with the reversed order of the Quantum Gates/Operations
         and setting the symmetric values given for their parameters).

        :return self.quantum_circuit.inverse(): the inverted IBM Qiskit's Quantum Circuit of
                                                the Qiskrypt's Quantum Circuit.
        """

        """
        Return the inverted IBM Qiskit's Quantum Circuit of
        the Qiskrypt's Quantum Circuit
        (i.e., with the reversed order of the Quantum Gates/Operations
         and setting the symmetric values given for their parameters).
        """
        return self.qiskit_quantum_circuit.inverse()

    def get_repeated_qiskit_quantum_circuit(self, num_repetitions: int) -> QuantumCircuit:
        """
        Return the IBM Qiskit's Quantum Circuit of
        the Qiskrypt's Quantum Circuit a given number of repetitions.

        :param num_repetitions: the number of repetitions for the IBM Qiskit's Quantum Circuit of
                                the Qiskrypt's Quantum Circuit.

        :return self.quantum_circuit.repeat(num_repetitions): the IBM Qiskit's Quantum Circuit of
                                                              the Qiskrypt's Quantum Circuit a given number of
                                                              repetitions.
        """

        """
        Return the IBM Qiskit's Quantum Circuit of
        the Qiskrypt's Quantum Circuit a given number of repetitions.
        """
        return self.qiskit_quantum_circuit.repeat(num_repetitions)

    def get_powered_qiskit_quantum_circuit(self, power: int, is_to_compute_matrix_power=False) -> QuantumCircuit:
        """
        Return the IBM Qiskit's Quantum Circuit of
        the Qiskrypt's Quantum Circuit raised to a given power term.

        :param power: the power for the IBM Qiskit's Quantum Circuit of
                      the Qiskrypt's Quantum Circuit be raised.
        :param is_to_compute_matrix_power: If True, the IBM Qiskit's Quantum Circuit is converted to
                                           a matrix and then, the matrix power is computed.
                                           Otherwise, and if the power term is a positive integer,
                                           the implementation defaults to the ``repeat`` method of
                                           the IBM Qiskit's Quantum Circuit.

        :return self.quantum_circuit.power(power, is_to_compute_matrix_power): the IBM Qiskit's Quantum Circuit of
                                                                               the Qiskrypt's Quantum Circuit raised to
                                                                               a given power term.
        """

        """
        Return the IBM Qiskit's Quantum Circuit of
        the Qiskrypt's Quantum Circuit raised to a given power term.
        """
        return self.qiskit_quantum_circuit.power(power, is_to_compute_matrix_power)

    def combine_qiskrypt_quantum_circuit(self, quantum_circuit_new_name: str,
                                         other_qiskrypt_quantum_circuit: QiskryptQuantumCircuit,
                                         new_global_phase=0) -> QiskryptQuantumCircuit:
        """


        :param quantum_circuit_new_name:
        :param other_qiskrypt_quantum_circuit:
        :param new_global_phase:

        :return:
        """

    def check_if_is_possible_to_apply_operation(self, qiskit_quantum_register_index: int, qubit_index: int,
                                                is_operation_only_supported_for_fully_quantum_registers: bool) -> bool:
        """
        Check if it is possible to apply a specific Operation,
        regarding a given IBM Qiskit's Quantum Register index and a qubit index.

        :param qiskit_quantum_register_index: the index of an IBM Qiskit's Quantum Register.
        :param qubit_index: the index of a qubit inside that IBM Qiskit's Quantum Register.
        :param is_operation_only_supported_for_fully_quantum_registers: the boolean flag to check if
                                                                        the Qiskrypt's Register is
                                                                        a Semi-Quantum one or not, for the case of
                                                                        the Quantum Gate/Operation be supported
                                                                        only by a Fully-Quantum.
        """

        if qiskit_quantum_register_index < len(self.qiskit_quantum_circuit.qregs):
            """
            If the given index of the IBM Qiskit's Quantum Register is valid.
            """

            if qubit_index < self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_index].size:
                """
                If the given index of the qubit in the given IBM Qiskit's Quantum Register is also valid.
                """

                has_qiskrypt_register, qiskrypt_register = \
                    self.find_qiskrypt_register_by_name(self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_index].name)
                """
                Find and retrieve the Qiskrypt's Register in the Qiskrypt's Quantum Circuit, given its name.
                """

                if has_qiskrypt_register:
                    """
                    If it was found some Qiskrypt's Register in the Qiskrypt's Quantum Circuit, with the given name.
                    """

                    if is_operation_only_supported_for_fully_quantum_registers:
                        """
                        If the pretended operation is only supported
                        for Qiskrypt's Fully-Quantum Registers.
                        """

                        if not self.check_if_is_a_qiskrypt_semi_quantum_register(qiskrypt_register):
                            """
                            If the founded Qiskrypt's Register with the given name is a Semi-Quantum one.
                            """

                            """
                            It is everything ok and it is possible to apply the pretended Quantum Operation/Gate.
                            """
                            return True

                        else:
                            """
                            If the founded Qiskrypt's Register with the given name is not a Semi-Quantum one.
                            """

                            if isinstance(qiskrypt_register, QiskryptSemiQuantumRegister):
                                """
                                If the Qiskrypt's Register with the given name is a Semi-Quantum Register.
                                """

                                """
                                Raise an Unsupported Operation for Semi-Quantum Register Error.
                                """
                                self.raise_unsupported_operation_for_semi_quantum_register_error()

                            elif isinstance(qiskrypt_register, QiskryptAncillaSemiQuantumRegister):
                                """
                                If the Qiskrypt's Register with the given name is a Ancilla Semi-Quantum Register.
                                """

                                """
                                Raise an Unsupported Operation for Ancilla Semi-Quantum Register Error.
                                """
                                self.raise_unsupported_operation_for_ancilla_semi_quantum_register_error()

                    else:
                        """
                        If the pretended operation is supported
                        by any Qiskrypt's Quantum Registers.
                        """

                        """
                        It is everything ok and it is possible to apply the pretended Quantum Operation/Gate.
                        """
                        return True

                else:
                    """
                    If it was not found no Qiskrypt's Register in the Qiskrypt's Quantum Circuit, with the given name.
                    """

                    """
                    Raise a Register Not Found Error for the Qiskrypt's Quantum Circuit.
                    """
                    self.raise_register_not_found_error()

            else:
                """
                If the given index of the qubit in the given IBM Qiskit's Quantum Register is not valid.
                """

                self.raise_invalid_qubit_index_given_error()
                """
                Raise an Invalid Qubit Index Given Error for the Qiskrypt's Quantum Circuit.
                """

        else:
            """
            If the given index of the IBM Qiskit's Quantum Register is not valid.
            """

            self.raise_invalid_qiskit_quantum_register_index_given_error()
            """
            Raise an Invalid IBM Qiskit's Quantum Register Index Given Error for the Qiskrypt's Quantum Circuit.
            """

    def check_if_is_possible_measure_single_qubit_into_single_bit(self, qiskit_quantum_register_index: int,
                                                                  qiskit_classical_register_index: int,
                                                                  qubit_index: int, bit_index: int) -> bool:
        """
        Check if it is possible to measure a single qubit into a single bit,
        regarding given IBM Qiskit's Quantum Register and Classical Register indexes, as also,
        the respective qubit and bit indexes.

        :param qiskit_quantum_register_index: the index of an IBM Qiskit's Quantum Register.
        :param qiskit_classical_register_index: the index of an IBM Qiskit's Classical Register.
        :param qubit_index: index of a qubit inside that IBM Qiskit's Quantum Register.
        :param bit_index: index of a bit inside that IBM Qiskit's Classical Register.
        """

        if qiskit_quantum_register_index < len(self.qiskit_quantum_circuit.qregs):
            """
            If the given index of the IBM Qiskit's Quantum Register is valid.
            """

            if qubit_index < self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_index].size:
                """
                If the given index of the qubit in the given IBM Qiskit's Quantum Register is also valid.
                """

                has_qiskrypt_quantum_register, qiskrypt_quantum_register = \
                    self.find_qiskrypt_register_by_name(self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_index].name)
                """
                Find and retrieve the Qiskrypt's Quantum Register in the Qiskrypt's Quantum Circuit, given its name.
                """

                if has_qiskrypt_quantum_register:
                    """
                    If it was found some Qiskrypt's Quantum Register in
                    the Qiskrypt's Quantum Circuit, with the given name.
                    """

                    if qiskit_classical_register_index < len(self.qiskit_quantum_circuit.cregs):
                        """
                        If the given index of the IBM Qiskit's Classical Register is valid.
                        """

                        if bit_index < self.qiskit_quantum_circuit.cregs[qiskit_classical_register_index].size:
                            """
                            If the given index of the bit in the given IBM Qiskit's Classical Register is also valid.
                            """

                            has_qiskrypt_classical_register, qiskrypt_classical_register = \
                                self.find_qiskrypt_register_by_name(self.qiskit_quantum_circuit.cregs[qiskit_classical_register_index].name)
                            """
                            Find and retrieve the Qiskrypt's Classical Register in
                            the Qiskrypt's Quantum Circuit, given its name.
                            """

                            if has_qiskrypt_classical_register:
                                """
                                If it was found some Qiskrypt's Classical Register in
                                the Qiskrypt's Quantum Circuit, with the given name.
                                """

                                """
                                It is everything ok and it is possible to measure
                                the pretended qubit in the given index of the Quantum Register into
                                the pretended bit in the given index of the Classical Register,
                                inside the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit.
                                """
                                return True

                else:
                    """
                    If it was not found no Qiskrypt's Register in the Qiskrypt's Quantum Circuit, with the given name.
                    """

                    """
                    Raise a Register Not Found Error for the Qiskrypt's Quantum Circuit.
                    """
                    self.raise_register_not_found_error()

            else:
                """
                If the given index of the qubit in the given IBM Qiskit's Quantum Register is not valid.
                """

                self.raise_invalid_qubit_index_given_error()
                """
                Raise an Invalid Qubit Index Given Error for the Qiskrypt's Quantum Circuit.
                """

        else:
            """
            If the given index of the IBM Qiskit's Quantum Register is not valid.
            """

            self.raise_invalid_qiskit_quantum_register_index_given_error()
            """
            Raise an Invalid IBM Qiskit's Quantum Register Index Given Error for the Qiskrypt's Quantum Circuit.
            """

    def apply_barrier_to_single_qubit_in_qiskit_quantum_register(self, qiskit_quantum_register_index: int,
                                                                 qubit_index: int) -> None:
        """
        Apply the Barrier Operation to a given index of an IBM Qiskit's Quantum Register
        and a given index of a target qubit.

        :param qiskit_quantum_register_index: the index of an IBM Qiskit's Quantum Register.
        :param qubit_index: the index of a qubit inside that IBM Qiskit's Quantum Register.
        """

        is_possible_to_apply_operation = \
            self.check_if_is_possible_to_apply_operation(qiskit_quantum_register_index, qubit_index, False)
        """
        Check if it is possible to apply the pretended operation.
        """

        if is_possible_to_apply_operation:
            """
            It is possible to apply the pretended operation.
            """

            self.qiskit_quantum_circuit.barrier(self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_index][qubit_index])
            """
            Apply the Barrier Operation to the given qubit of the given IBM Qiskit's Quantum Register. 
            """

    def apply_barriers_set_qubits_in_qiskit_quantum_register(self, qiskit_quantum_register_index: int,
                                                             qubits_indexes: list) -> None:
        """
        Apply Barriers Operations to given indexes of
        an IBM Qiskit's Quantum Register and a list of target qubits indexes.

        :param qiskit_quantum_register_index: the index of an IBM Qiskit's Quantum Register.
        :param qubits_indexes: the list of indexes of qubits inside that IBM Qiskit's Quantum Register.
        """

        if qiskit_quantum_register_index < len(self.qiskit_quantum_circuit.qregs):
            """
            If the given index of the IBM Qiskit's Quantum Register is valid.
            """

            qubits_indexes = list(dict.fromkeys(qubits_indexes))
            """
            Remove indexes of duplicated qubits.
            """

            max_qubit_index = max(qubits_indexes)
            """
            Retrieve the maximum index value of the list of indexes of qubits.
            """

            if max_qubit_index < self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_index].size:
                """
                If the maximum index value of the list of indexes of qubits in
                the given IBM Qiskit's Quantum Register is also valid.
                """

                for qubit_index in qubits_indexes:
                    """
                    For each qubit index in the list of indexes of qubits inside the IBM Qiskit's Quantum Register.
                    """

                    self.apply_barrier_to_single_qubit_in_qiskit_quantum_register(qiskit_quantum_register_index,
                                                                                  qubit_index)
                    """
                    Apply the Barrier Operation to the IBM Qiskit's Quantum Register and the current qubit index.
                    """

            else:
                """
                If the maximum index value of the list of indexes of qubits in
                the given IBM Qiskit's Quantum Register is not valid.
                """

                self.raise_invalid_qubit_index_given_error()
                """
                Raise an Invalid Qubit Index Given Error for the Qiskrypt's Quantum Circuit.
                """

        else:
            """
            If the given index of the IBM Qiskit's Quantum Register is not valid.
            """

            self.raise_invalid_qiskit_quantum_register_index_given_error()
            """
            Raise an Invalid IBM Qiskit's Quantum Register Index Given Error for the Qiskrypt's Quantum Circuit.
            """

    def apply_barriers_to_all_qubits_in_qiskit_quantum_register(self, qiskit_quantum_register_index: int) -> None:
        """
        Apply Barriers Operations to all qubit indexes in
        a given index of an IBM Qiskit's Quantum Register.

        :param qiskit_quantum_register_index: the index of an IBM Qiskit's Quantum Register.
        """

        if qiskit_quantum_register_index < len(self.qiskit_quantum_circuit.qregs):
            """
            If the given index of the IBM Qiskit's Quantum Register is valid.
            """

            qiskit_quantum_register = self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_index]
            """
            Retrieve the IBM Qiskit's Quantum Register, from the given index.
            """

            num_total_qubits_in_qiskit_quantum_register = qiskit_quantum_register.size
            """
            Retrieve the number of qubits in the retrieved IBM Qiskit's Quantum Register.
            """

            for qubit_index in range(num_total_qubits_in_qiskit_quantum_register):
                """
                For each qubit index in the retrieved IBM Qiskit's Quantum Register.
                """

                self.apply_barrier_to_single_qubit_in_qiskit_quantum_register(qiskit_quantum_register_index, qubit_index)
                """
                Apply the Barrier Operation to the IBM Qiskit's Quantum Register and the current qubit index.
                """

        else:
            """
            If the given index of the IBM Qiskit's Quantum Register is not valid.
            """

            self.raise_invalid_qiskit_quantum_register_index_given_error()
            """
            Raise an Invalid IBM Qiskit's Quantum Register Index Given Error for the Qiskrypt's Quantum Circuit.
            """

    def apply_barriers_set_qubits_in_all_qiskit_quantum_registers(self, qubits_indexes: list) -> None:
        """
        Apply Barriers Operations to the given qubit indexes in
        all the IBM Qiskit's Quantum Registers in the IBM Qiskit's Quantum Circuit of
        the Qiskrypt's Quantum Circuit.

        :param qubits_indexes: the list of indexes of qubits inside all the IBM Qiskit's Quantum Registers.
        """

        num_total_qiskit_quantum_registers = len(self.qiskit_quantum_circuit.qregs)
        """
        Retrieve the total number of IBM Qiskit's Quantum Registers
        in the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit.
        """

        for current_qiskit_quantum_register_index in range(num_total_qiskit_quantum_registers):
            """
            For each index of the IBM Qiskit's Quantum Register in
            the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit.
            """

            self.apply_barriers_set_qubits_in_qiskit_quantum_register(current_qiskit_quantum_register_index,
                                                                      qubits_indexes)
            """
            Apply Barriers Operations to the IBM Qiskit's Quantum Register and the list of target qubits.
            """

    def apply_barriers_to_all_qubits_in_all_qiskit_quantum_registers(self) -> None:
        """
        Apply Barriers Operations to all the qubit indexes in
        all the IBM Qiskit's Quantum Registers in the IBM Qiskit's Quantum Circuit of
        the Qiskrypt's Quantum Circuit.
        """

        num_total_qiskit_quantum_registers = len(self.qiskit_quantum_circuit.qregs)
        """
        Retrieve the total number of IBM Qiskit's Quantum Registers
        in the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit.
        """

        for current_qiskit_quantum_register_index in range(num_total_qiskit_quantum_registers):
            """
            For each index of the IBM Qiskit's Quantum Register in
            the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit.
            """

            self.apply_barriers_to_all_qubits_in_qiskit_quantum_register(current_qiskit_quantum_register_index)
            """
            Apply Barriers Operations to all the qubit indexes of the IBM Qiskit's Quantum Register.
            """

    def reset_single_qubit_in_qiskit_quantum_register(self, quantum_register_index: int,
                                                      qubit_index: int) -> None:
        """
        Reset a target qubit given its index on a given
        index of an IBM Qiskit's Quantum Register.

        :param quantum_register_index: the index of an IBM Qiskit's Quantum Register.
        :param qubit_index: the index of a qubit inside that IBM Qiskit's Quantum Register.
        """

        is_possible_to_apply_operation = \
            self.check_if_is_possible_to_apply_operation(quantum_register_index, qubit_index, False)
        """
        Check if it is possible to apply the pretended operation.
        """

        if is_possible_to_apply_operation:
            """
            It is possible to apply the pretended operation.
            """

            self.qiskit_quantum_circuit.reset(self.qiskit_quantum_circuit.qregs[quantum_register_index][qubit_index])
            """
            Reset the qubit of the given IBM Qiskit's Quantum Register and the current qubit index. 
            """

    def reset_set_qubits_in_qiskit_quantum_register(self, qiskit_quantum_register_index: int,
                                                    qubits_indexes: list) -> None:
        """
        Reset target qubits given their indexes on a given
        index of an IBM Qiskit's Quantum Register and a list of target qubits.

        :param qiskit_quantum_register_index: the index of an IBM Qiskit's Quantum Register.
        :param qubits_indexes: the list of indexes of qubits inside that IBM Qiskit's Quantum Register.
        """

        if qiskit_quantum_register_index < len(self.qiskit_quantum_circuit.qregs):
            """
            If the given index of the IBM Qiskit's Quantum Register is valid.
            """

            qubits_indexes = list(dict.fromkeys(qubits_indexes))
            """
            Remove indexes of duplicated qubits.
            """

            max_qubit_index = max(qubits_indexes)
            """
            Retrieve the maximum index value of the list of indexes of qubits.
            """

            if max_qubit_index < self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_index].size:
                """
                If the maximum index value of the list of indexes of qubits in
                the given IBM Qiskit's Quantum Register is also valid.
                """

                for qubit_index in qubits_indexes:
                    """
                    For each qubit index in the list of indexes of qubits inside the IBM Qiskit's Quantum Register.
                    """

                    self.reset_single_qubit_in_qiskit_quantum_register(qiskit_quantum_register_index, qubit_index)
                    """
                    Reset the current qubit index of the given IBM Qiskit's Quantum Register. 
                    """

            else:
                """
                If the maximum index value of the list of indexes of qubits in
                the given IBM Qiskit's Quantum Register is not valid.
                """

                self.raise_invalid_qubit_index_given_error()
                """
                Raise an Invalid Qubit Index Given Error for the Qiskrypt's Quantum Circuit.
                """

        else:
            """
            If the given index of the IBM Qiskit's Quantum Register is not valid.
            """

            self.raise_invalid_qiskit_quantum_register_index_given_error()
            """
            Raise an Invalid IBM Qiskit's Quantum Register Index Given Error for the Qiskrypt's Quantum Circuit.
            """

    def reset_all_qubits_in_qiskit_quantum_register(self, qiskit_quantum_register_index: int) -> None:
        """
        Reset all the target qubits on a given index of
        an IBM Qiskit's Quantum Register.

        :param qiskit_quantum_register_index: the index of an IBM Qiskit's Quantum Register.
        """

        if qiskit_quantum_register_index < len(self.qiskit_quantum_circuit.qregs):
            """
            If the given index of the IBM Qiskit's Quantum Register is valid.
            """

            qiskit_quantum_register = self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_index]
            """
            Retrieve the IBM Qiskit's Quantum Register, from the given index.
            """

            num_total_qubits_in_qiskit_quantum_register = qiskit_quantum_register.size
            """
            Retrieve the number of qubits in the retrieved IBM Qiskit's Quantum Register.
            """

            for qubit_index in range(num_total_qubits_in_qiskit_quantum_register):
                """
                For each qubit index in the retrieved IBM Qiskit's Quantum Register.
                """

                self.reset_single_qubit_in_qiskit_quantum_register(qiskit_quantum_register_index, qubit_index)
                """
                Reset the current qubit index of the given IBM Qiskit's Quantum Register. 
                """

        else:
            """
            If the given index of the IBM Qiskit's Quantum Register is not valid.
            """

            self.raise_invalid_qiskit_quantum_register_index_given_error()
            """
            Raise an Invalid IBM Qiskit's Quantum Register Index Given Error for the Qiskrypt's Quantum Circuit.
            """

    def reset_set_qubits_in_all_qiskit_quantum_registers(self, qubits_indexes: list) -> None:
        """
        Reset all the qubits in the given qubit indexes in
        all the IBM Qiskit's Quantum Registers in the IBM Qiskit's Quantum Circuit of
        the Qiskrypt's Quantum Circuit.

        :param qubits_indexes: the list of indexes of qubits inside all the IBM Qiskit's Quantum Registers.
        """

        num_total_qiskit_quantum_registers = len(self.qiskit_quantum_circuit.qregs)
        """
        Retrieve the total number of IBM Qiskit's Quantum Registers
        in the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit.
        """

        for current_qiskit_quantum_register_index in range(num_total_qiskit_quantum_registers):
            """
            For each index of the IBM Qiskit's Quantum Register in
            the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit.
            """

            self.reset_set_qubits_in_qiskit_quantum_register(current_qiskit_quantum_register_index, qubits_indexes)
            """
            Reset all the qubits in the list of target qubits of the current IBM Qiskit's Quantum Register.
            """

    def reset_all_qubits_in_all_qiskit_quantum_registers(self) -> None:
        """
        Reset all the target qubits on all the IBM Qiskit's Quantum Registers
        in the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit.
        """

        num_total_qiskit_quantum_registers = len(self.qiskit_quantum_circuit.qregs)
        """
        Retrieve the total number of IBM Qiskit's Quantum Registers
        in the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit.
        """

        for current_qiskit_quantum_register_index in range(num_total_qiskit_quantum_registers):
            """
            For each index of the IBM Qiskit's Quantum Register in
            the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit.
            """

            self.reset_all_qubits_in_qiskit_quantum_register(current_qiskit_quantum_register_index)
            """
            Reset all the qubit indexes of the current IBM Qiskit's Quantum Register.
            """

    """
    2) Methods for Measurement and Preparation of Quantum States:
    """

    def measure_single_qubit_in_qiskit_quantum_register(self,
                                                        qiskit_quantum_register_index: int,
                                                        qiskit_classical_register_index: int,
                                                        qubit_index: int, bit_index: int) -> None:
        """
        Measure a single qubit in an IBM Qiskit's Quantum Register into
        a single bit in an IBM Qiskit's Classical Register,
        inside the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit.

        :param qiskit_quantum_register_index: the index of an IBM Qiskit's Quantum Register.
        :param qiskit_classical_register_index: the index of an IBM Qiskit's Classical Register.
        :param qubit_index: the index of a qubit inside that IBM Qiskit's Quantum Register.
        :param bit_index: the index of a bit inside that IBM Qiskit's Classical Register.
        """

        is_possible_to_measure_single_qubit = \
            self.check_if_is_possible_measure_single_qubit_into_single_bit(qiskit_quantum_register_index,
                                                                           qiskit_classical_register_index,
                                                                           qubit_index, bit_index)
        """        
        Check if it is possible to measure the pretended qubit into the pretended bit.
        """

        if is_possible_to_measure_single_qubit:
            """
            It is possible to measure the pretended qubit into the pretended bit.
            """

            self.qiskit_quantum_circuit.measure(self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_index][qubit_index],
                                                self.qiskit_quantum_circuit.cregs[qiskit_classical_register_index][bit_index])
            """
            Measure the given qubit of the given IBM Qiskit's Quantum Register into
            the given bit of the given IBM Qiskit's Classical Register. 
            """

    def measure_set_qubits_in_qiskit_quantum_register(self,
                                                      qiskit_quantum_register_index: int,
                                                      qiskit_classical_register_index: int,
                                                      qubits_indexes: list, bits_indexes: list) -> None:
        """
        Measure a set of qubits in an IBM Qiskit's Quantum Register into
        another set of bits in an IBM Qiskit's Classical Register,
        inside the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit.

        :param qiskit_quantum_register_index: the index of an IBM Qiskit's Quantum Register.
        :param qiskit_classical_register_index: the index of an IBM Qiskit's Classical Register.
        :param qubits_indexes: the list of indexes of qubits inside that IBM Qiskit's Quantum Register.
        :param bits_indexes: the list of indexes of bits inside that IBM Qiskit's Classical Register.
        """

        if qiskit_quantum_register_index < len(self.qiskit_quantum_circuit.qregs):
            """
            If the given index of the IBM Qiskit's Quantum Register is valid.
            """

            qubits_indexes = list(dict.fromkeys(qubits_indexes))
            """
            Remove indexes of duplicated qubits.
            """

            max_qubit_index = max(qubits_indexes)
            """
            Retrieve the maximum index value of the list of indexes of qubits.
            """

            if max_qubit_index < self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_index].size:
                """
                If the maximum index value of the list of indexes of qubits in
                the given IBM Qiskit's Quantum Register is also valid.
                """

                if qiskit_classical_register_index < len(self.qiskit_quantum_circuit.cregs):
                    """
                    If the given index of the IBM Qiskit's Classical Register is valid.
                    """

                    bits_indexes = list(dict.fromkeys(bits_indexes))
                    """
                    Remove indexes of duplicated bits.
                    """

                    max_bit_index = max(bits_indexes)
                    """
                    Retrieve the maximum index value of the list of indexes of bits.
                    """

                    if max_bit_index < self.qiskit_quantum_circuit.cregs[qiskit_classical_register_index].size:
                        """
                        If the maximum index value of the list of indexes of bits in
                        the given IBM Qiskit's Classical Register is also valid.
                        """

                        if len(qubits_indexes) == len(bits_indexes):
                            """
                            If the number of distinct qubits given and the number of distinct bits given is the same.
                            """

                            for qubit_index, bit_index in zip(qubits_indexes, bits_indexes):
                                """
                                For each pair of indexes of qubits and bits.
                                """

                                self.measure_single_qubit_in_qiskit_quantum_register(qiskit_quantum_register_index,
                                                                                     qiskit_classical_register_index,
                                                                                     qubit_index, bit_index)
                                """
                                Measure the current qubit of the given IBM Qiskit's Quantum Register into
                                the current bit of the given IBM Qiskit's Classical Register. 
                                """

                        else:
                            """
                            If the number of distinct qubits given and the number of distinct bits given is not the same.
                            """

                            self.raise_num_qubits_and_num_bits_are_not_equal_for_operation_or_measurement_error()
                            """
                            Raise the Number of Qubits and Number of Bits are Not Equal for
                            Operation or Measurement Error for the Qiskrypt's Quantum Circuit.
                            """

                    else:
                        """
                        If the maximum index value of the list of indexes of bits in
                        the given IBM Qiskit's Classical Register is not valid.
                        """

                        self.raise_invalid_bit_index_given_error()
                        """
                        Raise an Invalid Bit Index Given Error for the Qiskrypt's Quantum Circuit.
                        """

                else:
                    """
                    If the given index of the IBM Qiskit's Classical Register is not valid.
                    """

                    self.raise_invalid_qiskit_classical_register_index_given_error()
                    """
                    Raise an Invalid IBM Qiskit's Classical Register Index Given Error for
                    the Qiskrypt's Quantum Circuit.
                    """

            else:
                """
                If the maximum index value of the list of indexes of qubits in
                the given IBM Qiskit's Quantum Register is not valid.
                """

                self.raise_invalid_qubit_index_given_error()
                """
                Raise an Invalid Qubit Index Given Error for the Qiskrypt's Quantum Circuit.
                """

        else:
            """
            If the given index of the IBM Qiskit's Quantum Register is not valid.
            """

            self.raise_invalid_qiskit_quantum_register_index_given_error()
            """
            Raise an Invalid IBM Qiskit's Quantum Register Index Given Error for
            the Qiskrypt's Quantum Circuit.
            """

    def measure_all_qubits_in_qiskit_quantum_register(self,
                                                      qiskit_quantum_register_index: int,
                                                      qiskit_classical_register_index: int) -> None:
        """
        Measure all the qubits in an IBM Qiskit's Quantum Register into
        another all the of bits in an IBM Qiskit's Classical Register,
        inside the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit.

        :param qiskit_quantum_register_index: the index of an IBM Qiskit's Quantum Register.
        :param qiskit_classical_register_index: the index of an IBM Qiskit's Classical Register.
        """

        if qiskit_quantum_register_index < len(self.qiskit_quantum_circuit.qregs):
            """
            If the given index of the IBM Qiskit's Quantum Register is valid.
            """

            if qiskit_classical_register_index < len(self.qiskit_quantum_circuit.cregs):
                """
                If the given index of the IBM Qiskit's Classical Register is valid.
                """

                num_qubits_qiskit_quantum_register = self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_index].size
                """
                Retrieve the number of qubits in the given IBM Qiskit's Quantum Register inside the IBM Qiskit's Quantum Circuit.
                """

                num_bits_qiskit_classical_register = self.qiskit_quantum_circuit.cregs[qiskit_classical_register_index].size
                """
                Retrieve the number of bits in the given IBM Qiskit's Classical Register inside the IBM Qiskit's Quantum Circuit.
                """

                if num_qubits_qiskit_quantum_register == num_bits_qiskit_classical_register:
                    """
                    If the number of qubits of the given IBM Qiskit's Quantum Register is equal to
                    the number of bits of the given IBM Qiskit's Classical Register,
                    inside the IBM Qiskit's Quantum Circuit.
                    """

                    qubits_indexes = range(num_qubits_qiskit_quantum_register)
                    """
                    Retrieve the list of the range of qubits in the given IBM Qiskit's Quantum Register of
                    the IBM Qiskit's Quantum Circuit.
                    """

                    bits_indexes = range(num_bits_qiskit_classical_register)
                    """
                    Retrieve the list of the range of bits in the given IBM Qiskit's Classical Register of
                    the IBM Qiskit's Quantum Circuit.
                    """

                    for qubit_index, bit_index in zip(qubits_indexes, bits_indexes):
                        """
                        For each pair of indexes of qubits and bits.
                        """

                        self.measure_single_qubit_in_qiskit_quantum_register(qiskit_quantum_register_index,
                                                                             qiskit_classical_register_index,
                                                                             qubit_index, bit_index)
                        """
                        Measure the current qubit of the given IBM Qiskit's Quantum Register into
                        the current bit of the given IBM Qiskit's Classical Register. 
                        """

                else:
                    """
                    If the number of qubits of the given IBM Qiskit's Quantum Register is not equal to
                    the number of bits of the given IBM Qiskit's Classical Register,
                    inside the IBM Qiskit's Quantum Circuit.
                    """

                    self.raise_num_qubits_and_num_bits_are_not_equal_for_operation_or_measurement_error()
                    """
                    Raise the Number of Qubits and Number of Bits are Not Equal for
                    Operation or Measurement Error for the Qiskrypt's Quantum Circuit.
                    """

            else:
                """
                If the given index of the IBM Qiskit's Classical Register is not valid.
                """

                self.raise_invalid_qiskit_classical_register_index_given_error()
                """
                Raise an Invalid IBM Qiskit's Classical Register Index Given Error for
                the Qiskrypt's Quantum Circuit.
                """

        else:
            """
            If the given index of the IBM Qiskit's Quantum Register is not valid.
            """

            self.raise_invalid_qiskit_quantum_register_index_given_error()
            """
            Raise an Invalid IBM Qiskit's Quantum Register Index Given Error for
            the Qiskrypt's Quantum Circuit.
            """

    def measure_set_qubits_in_all_qiskit_quantum_registers(self, qubits_indexes: list, bits_indexes: list) -> None:
        """
        Measure all the given indexes of qubits of
        all the available IBM Qiskit's Quantum Registers into
        all the given indexes of bits of
        all the available IBM Qiskit's Classical Registers inside
        the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit.

        :param qubits_indexes: the list of indexes of qubits inside all the IBM Qiskit's Quantum Registers.
        :param bits_indexes: the list of indexes of bits inside all the IBM Qiskit's Classical Registers.
        """

        num_total_qiskit_quantum_registers = len(self.qiskit_quantum_circuit.qregs)
        """
        Retrieve the total number of IBM Qiskit's Quantum Registers
        in the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit.
        """

        num_total_qiskit_classical_registers = len(self.qiskit_quantum_circuit.cregs)
        """
        Retrieve the total number of IBM Qiskit's Classical Registers
        in the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit.
        """

        if num_total_qiskit_quantum_registers == num_total_qiskit_classical_registers:
            """
            If the total number of IBM Qiskit's Quantum Registers and
            the total number of IBM Qiskit's Classical Registers are equal.
            """

            qubits_indexes = list(dict.fromkeys(qubits_indexes))
            """
            Remove indexes of duplicated qubits.
            """

            bits_indexes = list(dict.fromkeys(bits_indexes))
            """
            Remove indexes of duplicated bits.
            """

            num_qubits_indexes = len(qubits_indexes)
            """
            Retrieve the number of distinct indexes of qubits.
            """

            num_bits_indexes = len(bits_indexes)
            """
            Retrieve the number of distinct indexes of bits.
            """

            if num_qubits_indexes == num_bits_indexes:
                """
                The number of indexes of qubits and the number of indexes of bits are equal.
                """

                qiskit_quantum_registers_indexes = range(num_total_qiskit_quantum_registers)
                """
                Retrieve the indexes of all the IBM Qiskit's Quantum Registers.
                """

                qiskit_classical_registers_indexes = range(num_total_qiskit_classical_registers)
                """
                Retrieve the indexes of all the IBM Qiskit's Classical Registers.
                """

                for qiskit_quantum_register_index, qiskit_classical_register_index \
                        in zip(qiskit_quantum_registers_indexes, qiskit_classical_registers_indexes):
                    """
                    For each pair of indexes of IBM Qiskit's Quantum Registers and IBM Qiskit's Classical Registers.
                    """

                    self.measure_set_qubits_in_qiskit_quantum_register(qiskit_quantum_register_index,
                                                                       qiskit_classical_register_index,
                                                                       qubits_indexes, bits_indexes)
                    """
                    Measure the resulted set of distinct qubits in the current IBM Qiskit's Quantum Register into
                    the other resulted set of distinct bits in the current IBM Qiskit's Classical Register,
                    inside the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit.
                    """

            else:
                """
                The number of indexes of qubits and the number of indexes of bits are not equal.
                """

                self.raise_num_qubits_and_num_bits_are_not_equal_for_operation_or_measurement_error()
                """
                Raise the Number of Qubits and Number of Bits are Not Equal for
                Operation or Measurement Error for the Qiskrypt's Quantum Circuit.
                """

        else:
            """
            If the total number of IBM Qiskit's Quantum Registers and
            the total number of IBM Qiskit's Classical Registers are not equal.
            """

            self.raise_num_quantum_registers_and_num_classical_registers_are_not_equal_for_operation_or_measurement_error()
            """
            Raise the Number of Quantum Registers and Number of Classical Registers are Not Equal for
            Operation or Measurement Error for the Qiskrypt's Quantum Circuit.
            """

    def measure_all_qubits_in_all_qiskit_quantum_registers(self) -> None:
        """
        Measure all the available qubits of
        all the available IBM Qiskit's Quantum Registers into
        all the available bits of
        all the available IBM Qiskit's Classical Registers inside
        the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit.
        """

        num_total_qiskit_quantum_registers = len(self.qiskit_quantum_circuit.qregs)
        """
        Retrieve the total number of IBM Qiskit's Quantum Registers
        in the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit.
        """

        num_total_qiskit_classical_registers = len(self.qiskit_quantum_circuit.cregs)
        """
        Retrieve the total number of IBM Qiskit's Classical Registers
        in the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit.
        """

        if num_total_qiskit_quantum_registers == num_total_qiskit_classical_registers:
            """
            If the total number of IBM Qiskit's Quantum Registers and
            the total number of IBM Qiskit's Classical Registers are equal.
            """

            qiskit_quantum_registers_indexes = range(num_total_qiskit_quantum_registers)
            """
            Retrieve the indexes of the IBM Qiskit's Quantum Registers in the IBM Qiskit's Quantum Circuit.
            """

            qiskit_classical_registers_indexes = range(num_total_qiskit_classical_registers)
            """
            Retrieve the indexes of the IBM Qiskit's Classical Registers in the IBM Qiskit's Quantum Circuit.            
            """

            for qiskit_quantum_register_index, qiskit_classical_register_index \
                    in zip(qiskit_quantum_registers_indexes, qiskit_classical_registers_indexes):
                """
                For each pair of indexes of IBM Qiskit's Quantum Registers and IBM Qiskit's Classical Registers.
                """

                self.measure_all_qubits_in_qiskit_quantum_register(qiskit_quantum_register_index,
                                                                   qiskit_classical_register_index)
                """
                Measure all the qubits in the current IBM Qiskit's Quantum Register into
                all the bits in the current IBM Qiskit's Classical Register,
                inside the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit.
                """

        else:
            """
            If the total number of IBM Qiskit's Quantum Registers and
            the total number of IBM Qiskit's Classical Registers are not equal.
            """

            self.raise_num_quantum_registers_and_num_classical_registers_are_not_equal_for_operation_or_measurement_error()
            """
            Raise the Number of Quantum Registers and Number of Classical Registers are Not Equal for
            Operation or Measurement Error for the Qiskrypt's Quantum Circuit.
            """

    def measure_all_qubits_predefined_from_qiskit(self) -> None:
        """
        Measure all the qubits in some available IBM Qiskit's Quantum Register(s) into
        all the bits in some available IBM Qiskit's Classical Register(s),
        using the predefined "measure_all()" method of the IBM Qiskit's Quantum Circuit.
        """

        self.qiskit_quantum_circuit.measure_all()
        """
        Measure all the qubits in some available IBM Qiskit's Quantum Register(s) into
        another all the of bits in an IBM Qiskit's Classical Register(s).
        """

    def prepare_and_measure_single_qubit_in_qiskit_quantum_register_in_x_basis(self,
                                                                               qiskit_quantum_register_index: int,
                                                                               qiskit_classical_register_index: int,
                                                                               qubit_index: int, bit_index: int,
                                                                               is_final_measurement=True) -> None:
        """
        Prepare (and possibly, Measure) a given index of a single qubit of a given IBM Qiskit's Quantum Register
        (into a given index of a single bit of an IBM Qiskit's Classical Register), in the X-Basis.

        :param qiskit_quantum_register_index: the index of an IBM Qiskit's Quantum Register.
        :param qiskit_classical_register_index: the index of an IBM Qiskit's Classical Register.
        :param qubit_index: the index of a qubit inside that IBM Qiskit's Quantum Register.
        :param bit_index: the index of a bit inside that IBM Qiskit's Classical Register.
        :param is_final_measurement: a boolean flag to indicate that the given index of a qubit of
                                     a given index of an IBM Qiskit's Quantum Register is pretended to
                                     be measured into the given index of a bit of
                                     given index of an IBM Qiskit's Classical Register,
                                     in the Computational Basis (Z-Basis), after being prepared in the X-Basis.
        """

        is_possible_to_apply_operation = \
            self.check_if_is_possible_to_apply_operation(qiskit_quantum_register_index, qubit_index, True)
        """
        Check if it is possible to apply the pretended operation.
        """

        if is_possible_to_apply_operation:
            """
            It is possible to apply the pretended operation.
            """

            self.apply_barrier_to_single_qubit_in_qiskit_quantum_register(qiskit_quantum_register_index, qubit_index)
            """
            Apply the 1st Barrier Operation to the given index of
            the IBM Qiskit's Quantum Register and the given index of the target qubit.
            """

            self.apply_hadamard(qiskit_quantum_register_index, qubit_index)
            """
            Apply the Hadamard Gate/Operation to the given qubit in the given IBM Qiskit's Quantum Circuit.
            """

            self.apply_barrier_to_single_qubit_in_qiskit_quantum_register(qiskit_quantum_register_index, qubit_index)
            """
            Apply the 2nd Barrier Operation to the given index of
            the IBM Qiskit's Quantum Register and the given index of the target qubit.
            """

            if is_final_measurement:
                """
                If it is pretended that the given qubit is pretended to
                be measured into the given bit, in the Computational Basis (Z-Basis),
                after being prepared in the X-Basis.
                """

                self.measure_single_qubit_in_qiskit_quantum_register(qiskit_quantum_register_index,
                                                                     qiskit_classical_register_index,
                                                                     qubit_index, bit_index)
                """
                Measure the pretended that the given qubit is pretended to
                be measured into the given bit, in the Computational Basis (Z-Basis),
                after being prepared in the X-Basis.
                """

    def prepare_and_measure_single_qubit_in_qiskit_quantum_register_in_y_basis(self,
                                                                               qiskit_quantum_register_index: int,
                                                                               qiskit_classical_register_index: int,
                                                                               qubit_index: int, bit_index: int,
                                                                               is_final_measurement=True) -> None:
        """
        Prepare (and possibly, Measure) a given index of a single qubit of a given IBM Qiskit's Quantum Register
        (into a given index of a single bit of an IBM Qiskit's Classical Register), in the X-Basis.

        :param qiskit_quantum_register_index: the index of an IBM Qiskit's Quantum Register.
        :param qiskit_classical_register_index: the index of an IBM Qiskit's Classical Register.
        :param qubit_index: the index of a qubit inside that IBM Qiskit's Quantum Register.
        :param bit_index: the index of a bit inside that IBM Qiskit's Classical Register.
        :param is_final_measurement: a boolean flag to indicate that the given index of a qubit of
                                     a given index of an IBM Qiskit's Quantum Register is pretended to
                                     be measured into the given index of a bit of
                                     given index of an IBM Qiskit's Classical Register,
                                     in the Computational Basis (Z-Basis), after being prepared in the Y-Basis.
        """

        is_possible_to_apply_operation = \
            self.check_if_is_possible_to_apply_operation(qiskit_quantum_register_index, qubit_index, True)
        """
        Check if it is possible to apply the pretended operation.
        """

        if is_possible_to_apply_operation:
            """
            It is possible to apply the pretended operation.
            """

            self.apply_barrier_to_single_qubit_in_qiskit_quantum_register(qiskit_quantum_register_index, qubit_index)
            """
            Apply the 1st Barrier Operation to the given index of
            the IBM Qiskit's Quantum Register and the given index of the target qubit.
            """

            self.apply_hadamard(qiskit_quantum_register_index, qubit_index)
            """
            Apply the Hadamard Gate/Operation to the given qubit in the given IBM Qiskit's Quantum Circuit.
            """

            self.apply_phase_s(qiskit_quantum_register_index, qubit_index)
            """
            Apply the Phase S (pi/2) Gate/Operation to the given qubit in the given IBM Qiskit's Quantum Circuit.
            """

            self.apply_barrier_to_single_qubit_in_qiskit_quantum_register(qiskit_quantum_register_index, qubit_index)
            """
            Apply the 2nd Barrier Operation to the given index of
            the IBM Qiskit's Quantum Register and the given index of the target qubit.
            """

            if is_final_measurement:
                """
                If it is pretended that the given qubit is pretended to
                be measured into the given bit, in the Computational Basis (Z-Basis),
                after being prepared in the Y-Basis.
                """

                self.measure_single_qubit_in_qiskit_quantum_register(qiskit_quantum_register_index,
                                                                     qiskit_classical_register_index,
                                                                     qubit_index, bit_index)
                """
                Measure the pretended that the given qubit is pretended to
                be measured into the given bit, in the Computational Basis (Z-Basis),
                after being prepared in the Y-Basis.
                """

    def prepare_and_measure_single_qubit_in_qiskit_quantum_register_in_z_basis(self,
                                                                               qiskit_quantum_register_index: int,
                                                                               qiskit_classical_register_index: int,
                                                                               qubit_index: int, bit_index: int,
                                                                               is_final_measurement=True) -> None:
        """
        Prepare (and possibly, Measure) a given index of a single qubit of a given IBM Qiskit's Quantum Register
        (into a given index of a single bit of an IBM Qiskit's Classical Register), in the X-Basis.

        :param qiskit_quantum_register_index: the index of an IBM Qiskit's Quantum Register.
        :param qiskit_classical_register_index: the index of an IBM Qiskit's Classical Register.
        :param qubit_index: the index of a qubit inside that IBM Qiskit's Quantum Register.
        :param bit_index: the index of a bit inside that IBM Qiskit's Classical Register.
        :param is_final_measurement: a boolean flag to indicate that the given index of a qubit of
                                     a given index of an IBM Qiskit's Quantum Register is pretended to
                                     be measured into the given index of a bit of
                                     given index of an IBM Qiskit's Classical Register,
                                     in the Computational Basis (Z-Basis), after being prepared in the Z-Basis.
        """

        is_possible_to_apply_operation = \
            self.check_if_is_possible_to_apply_operation(qiskit_quantum_register_index, qubit_index, True)
        """
        Check if it is possible to apply the pretended operation.
        """

        if is_possible_to_apply_operation:
            """
            It is possible to apply the pretended operation.
            """

            self.apply_barrier_to_single_qubit_in_qiskit_quantum_register(qiskit_quantum_register_index, qubit_index)
            """
            Apply the 1st Barrier Operation to the given index of
            the IBM Qiskit's Quantum Register and the given index of the target qubit.
            """

            self.apply_pauli_i(qiskit_quantum_register_index, qubit_index)
            """
            Apply the Pauli-I Gate/Operation to the given qubit in the given IBM Qiskit's Quantum Circuit.
            """

            self.apply_barrier_to_single_qubit_in_qiskit_quantum_register(qiskit_quantum_register_index, qubit_index)
            """
            Apply the 2nd Barrier Operation to the given index of
            the IBM Qiskit's Quantum Register and the given index of the target qubit.
            """

            if is_final_measurement:
                """
                If it is pretended that the given qubit is pretended to
                be measured into the given bit, in the Computational Basis (Z-Basis),
                after being prepared in the Z-Basis.
                """

                self.measure_single_qubit_in_qiskit_quantum_register(qiskit_quantum_register_index,
                                                                     qiskit_classical_register_index,
                                                                     qubit_index, bit_index)
                """
                Measure the pretended that the given qubit is pretended to
                be measured into the given bit, in the Computational Basis (Z-Basis),
                after being prepared in the Z-Basis.
                """

    def prepare_and_measure_set_qubits_in_qiskit_quantum_register_in_x_basis(self,
                                                                             qiskit_quantum_register_index: int,
                                                                             qiskit_classical_register_index: int,
                                                                             qubits_indexes: list,
                                                                             bits_indexes: list,
                                                                             is_final_measurement=True) -> None:
        """
        Prepare (and possibly, Measure) a given list of indexes of qubits of the given index of
        an IBM Qiskit's Quantum Register (into a given list of indexes of bits of the given index of
        an IBM Qiskit's Classical Register), in the X-Basis.

        :param qiskit_quantum_register_index: the index of an IBM Qiskit's Quantum Register.
        :param qiskit_classical_register_index: the index of an IBM Qiskit's Classical Register.
        :param qubits_indexes: the list of indexes of qubits inside that IBM Qiskit's Quantum Register.
        :param bits_indexes: the list of indexes of bits inside that IBM Qiskit's Classical Register.
        :param is_final_measurement: a boolean flag to indicate that the given indexes of qubits of
                                     a given index of an IBM Qiskit's Quantum Register are pretended to
                                     be measured into the given indexes of bits of
                                     given index of an IBM Qiskit's Classical Register,
                                     in the Computational Basis (Z-Basis), after being prepared in the X-Basis.
        """

        if qiskit_quantum_register_index < len(self.qiskit_quantum_circuit.qregs):
            """
            If the given index of the IBM Qiskit's Quantum Register is valid.
            """

            qubits_indexes = list(dict.fromkeys(qubits_indexes))
            """
            Remove indexes of duplicated qubits.
            """

            max_qubit_index = max(qubits_indexes)
            """
            Retrieve the maximum index value of the list of indexes of qubits.
            """

            if max_qubit_index < self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_index].size:
                """
                If the maximum index value of the list of indexes of qubits in
                the given IBM Qiskit's Quantum Register is also valid.
                """

                if qiskit_classical_register_index < len(self.qiskit_quantum_circuit.cregs):
                    """
                    If the given index of the IBM Qiskit's Classical Register is valid.
                    """

                    bits_indexes = list(dict.fromkeys(bits_indexes))
                    """
                    Remove indexes of duplicated bits.
                    """

                    max_bit_index = max(bits_indexes)
                    """
                    Retrieve the maximum index value of the list of indexes of bits.
                    """

                    if max_bit_index < self.qiskit_quantum_circuit.cregs[qiskit_classical_register_index].size:
                        """
                        If the maximum index value of the list of indexes of bits in
                        the given IBM Qiskit's Classical Register is also valid.
                        """

                        if len(qubits_indexes) == len(bits_indexes):
                            """
                            If the number of distinct qubits given and the number of distinct bits given is the same.
                            """

                            for qubit_index, bit_index in zip(qubits_indexes, bits_indexes):
                                """
                                For each pair of indexes of qubits and bits.
                                """

                                self.prepare_and_measure_single_qubit_in_qiskit_quantum_register_in_x_basis(qiskit_quantum_register_index,
                                                                                                            qiskit_classical_register_index,
                                                                                                            qubit_index, bit_index,
                                                                                                            is_final_measurement)
                                """
                                Prepare (and possibly, Measure) a given index of
                                a single qubit of a given IBM Qiskit's Quantum Register
                                (into a given index of a single bit of an IBM Qiskit's Classical Register),
                                in the X-Basis.
                                """

                        else:
                            """
                            If the number of distinct qubits given and
                            the number of distinct bits given is not the same.
                            """

                            self.raise_num_qubits_and_num_bits_are_not_equal_for_operation_or_measurement_error()
                            """
                            Raise the Number of Qubits and Number of Bits are Not Equal for
                            Operation or Measurement Error for the Qiskrypt's Quantum Circuit.
                            """

                    else:
                        """
                        If the maximum index value of the list of indexes of bits in
                        the given IBM Qiskit's Classical Register is not valid.
                        """

                        self.raise_invalid_bit_index_given_error()
                        """
                        Raise an Invalid Bit Index Given Error for the Qiskrypt's Quantum Circuit.
                        """

                else:
                    """
                    If the given index of the IBM Qiskit's Classical Register is not valid.
                    """

                    self.raise_invalid_qiskit_classical_register_index_given_error()
                    """
                    Raise an Invalid IBM Qiskit's Classical Register Index Given Error for
                    the Qiskrypt's Quantum Circuit.
                    """

            else:
                """
                If the maximum index value of the list of indexes of qubits in
                the given IBM Qiskit's Quantum Register is not valid.
                """

                self.raise_invalid_qubit_index_given_error()
                """
                Raise an Invalid Qubit Index Given Error for the Qiskrypt's Quantum Circuit.
                """

        else:
            """
            If the given index of the IBM Qiskit's Quantum Register is not valid.
            """

            self.raise_invalid_qiskit_quantum_register_index_given_error()
            """
            Raise an Invalid IBM Qiskit's Quantum Register Index Given Error for
            the Qiskrypt's Quantum Circuit.
            """

    def prepare_and_measure_set_qubits_in_qiskit_quantum_register_in_y_basis(self,
                                                                             qiskit_quantum_register_index: int,
                                                                             qiskit_classical_register_index: int,
                                                                             qubits_indexes: list,
                                                                             bits_indexes: list,
                                                                             is_final_measurement=True) -> None:
        """
        Prepare (and possibly, Measure) a given list of indexes of qubits of the given index of
        an IBM Qiskit's Quantum Register (into a given list of indexes of bits of the given index of
        an IBM Qiskit's Classical Register), in the Y-Basis.

        :param qiskit_quantum_register_index: the index of an IBM Qiskit's Quantum Register.
        :param qiskit_classical_register_index: the index of an IBM Qiskit's Classical Register.
        :param qubits_indexes: the list of indexes of qubits inside that IBM Qiskit's Quantum Register.
        :param bits_indexes: the list of indexes of bits inside that IBM Qiskit's Classical Register.
        :param is_final_measurement: a boolean flag to indicate that the given indexes of qubits of
                                     a given index of an IBM Qiskit's Quantum Register are pretended to
                                     be measured into the given indexes of bits of
                                     given index of an IBM Qiskit's Classical Register,
                                     in the Computational Basis (Z-Basis), after being prepared in the Y-Basis.
        """

        if qiskit_quantum_register_index < len(self.qiskit_quantum_circuit.qregs):
            """
            If the given index of the IBM Qiskit's Quantum Register is valid.
            """

            qubits_indexes = list(dict.fromkeys(qubits_indexes))
            """
            Remove indexes of duplicated qubits.
            """

            max_qubit_index = max(qubits_indexes)
            """
            Retrieve the maximum index value of the list of indexes of qubits.
            """

            if max_qubit_index < self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_index].size:
                """
                If the maximum index value of the list of indexes of qubits in
                the given IBM Qiskit's Quantum Register is also valid.
                """

                if qiskit_classical_register_index < len(self.qiskit_quantum_circuit.cregs):
                    """
                    If the given index of the IBM Qiskit's Classical Register is valid.
                    """

                    bits_indexes = list(dict.fromkeys(bits_indexes))
                    """
                    Remove indexes of duplicated bits.
                    """

                    max_bit_index = max(bits_indexes)
                    """
                    Retrieve the maximum index value of the list of indexes of bits.
                    """

                    if max_bit_index < self.qiskit_quantum_circuit.cregs[qiskit_classical_register_index].size:
                        """
                        If the maximum index value of the list of indexes of bits in
                        the given IBM Qiskit's Classical Register is also valid.
                        """

                        if len(qubits_indexes) == len(bits_indexes):
                            """
                            If the number of distinct qubits given and the number of distinct bits given is the same.
                            """

                            for qubit_index, bit_index in zip(qubits_indexes, bits_indexes):
                                """
                                For each pair of indexes of qubits and bits.
                                """

                                self.prepare_and_measure_single_qubit_in_qiskit_quantum_register_in_y_basis(qiskit_quantum_register_index,
                                                                                                            qiskit_classical_register_index,
                                                                                                            qubit_index, bit_index,
                                                                                                            is_final_measurement)
                                """
                                Prepare (and possibly, Measure) a given index of
                                a single qubit of a given IBM Qiskit's Quantum Register
                                (into a given index of a single bit of an IBM Qiskit's Classical Register),
                                in the Y-Basis.
                                """

                        else:
                            """
                            If the number of distinct qubits given and
                            the number of distinct bits given is not the same.
                            """

                            self.raise_num_qubits_and_num_bits_are_not_equal_for_operation_or_measurement_error()
                            """
                            Raise the Number of Qubits and Number of Bits are Not Equal for
                            Operation or Measurement Error for the Qiskrypt's Quantum Circuit.
                            """

                    else:
                        """
                        If the maximum index value of the list of indexes of bits in
                        the given IBM Qiskit's Classical Register is not valid.
                        """

                        self.raise_invalid_bit_index_given_error()
                        """
                        Raise an Invalid Bit Index Given Error for the Qiskrypt's Quantum Circuit.
                        """

                else:
                    """
                    If the given index of the IBM Qiskit's Classical Register is not valid.
                    """

                    self.raise_invalid_qiskit_classical_register_index_given_error()
                    """
                    Raise an Invalid IBM Qiskit's Classical Register Index Given Error for
                    the Qiskrypt's Quantum Circuit.
                    """

            else:
                """
                If the maximum index value of the list of indexes of qubits in
                the given IBM Qiskit's Quantum Register is not valid.
                """

                self.raise_invalid_qubit_index_given_error()
                """
                Raise an Invalid Qubit Index Given Error for the Qiskrypt's Quantum Circuit.
                """

        else:
            """
            If the given index of the IBM Qiskit's Quantum Register is not valid.
            """

            self.raise_invalid_qiskit_quantum_register_index_given_error()
            """
            Raise an Invalid IBM Qiskit's Quantum Register Index Given Error for
            the Qiskrypt's Quantum Circuit.
            """

    def prepare_and_measure_set_qubits_in_qiskit_quantum_register_in_z_basis(self,
                                                                             qiskit_quantum_register_index: int,
                                                                             qiskit_classical_register_index: int,
                                                                             qubits_indexes: list,
                                                                             bits_indexes: list,
                                                                             is_final_measurement=True) -> None:
        """
        Prepare (and possibly, Measure) a given list of indexes of qubits of the given index of
        an IBM Qiskit's Quantum Register (into a given list of indexes of bits of the given index of
        an IBM Qiskit's Classical Register), in the Y-Basis.

        :param qiskit_quantum_register_index: the index of an IBM Qiskit's Quantum Register.
        :param qiskit_classical_register_index: the index of an IBM Qiskit's Classical Register.
        :param qubits_indexes: the list of indexes of qubits inside that IBM Qiskit's Quantum Register.
        :param bits_indexes: the list of indexes of bits inside that IBM Qiskit's Classical Register.
        :param is_final_measurement: a boolean flag to indicate that the given indexes of qubits of
                                     a given index of an IBM Qiskit's Quantum Register are pretended to
                                     be measured into the given indexes of bits of
                                     given index of an IBM Qiskit's Classical Register,
                                     in the Computational Basis (Z-Basis), after being prepared in the Z-Basis.
        """

        if qiskit_quantum_register_index < len(self.qiskit_quantum_circuit.qregs):
            """
            If the given index of the IBM Qiskit's Quantum Register is valid.
            """

            qubits_indexes = list(dict.fromkeys(qubits_indexes))
            """
            Remove indexes of duplicated qubits.
            """

            max_qubit_index = max(qubits_indexes)
            """
            Retrieve the maximum index value of the list of indexes of qubits.
            """

            if max_qubit_index < self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_index].size:
                """
                If the maximum index value of the list of indexes of qubits in
                the given IBM Qiskit's Quantum Register is also valid.
                """

                if qiskit_classical_register_index < len(self.qiskit_quantum_circuit.cregs):
                    """
                    If the given index of the IBM Qiskit's Classical Register is valid.
                    """

                    bits_indexes = list(dict.fromkeys(bits_indexes))
                    """
                    Remove indexes of duplicated bits.
                    """

                    max_bit_index = max(bits_indexes)
                    """
                    Retrieve the maximum index value of the list of indexes of bits.
                    """

                    if max_bit_index < self.qiskit_quantum_circuit.cregs[qiskit_classical_register_index].size:
                        """
                        If the maximum index value of the list of indexes of bits in
                        the given IBM Qiskit's Classical Register is also valid.
                        """

                        if len(qubits_indexes) == len(bits_indexes):
                            """
                            If the number of distinct qubits given and the number of distinct bits given is the same.
                            """

                            for qubit_index, bit_index in zip(qubits_indexes, bits_indexes):
                                """
                                For each pair of indexes of qubits and bits.
                                """

                                self.prepare_and_measure_single_qubit_in_qiskit_quantum_register_in_z_basis(qiskit_quantum_register_index,
                                                                                                            qiskit_classical_register_index,
                                                                                                            qubit_index, bit_index,
                                                                                                            is_final_measurement)
                                """
                                Prepare (and possibly, Measure) a given index of
                                a single qubit of a given IBM Qiskit's Quantum Register
                                (into a given index of a single bit of an IBM Qiskit's Classical Register),
                                in the Z-Basis.
                                """

                        else:
                            """
                            If the number of distinct qubits given and
                            the number of distinct bits given is not the same.
                            """

                            self.raise_num_qubits_and_num_bits_are_not_equal_for_operation_or_measurement_error()
                            """
                            Raise the Number of Qubits and Number of Bits are Not Equal for
                            Operation or Measurement Error for the Qiskrypt's Quantum Circuit.
                            """

                    else:
                        """
                        If the maximum index value of the list of indexes of bits in
                        the given IBM Qiskit's Classical Register is not valid.
                        """

                        self.raise_invalid_bit_index_given_error()
                        """
                        Raise an Invalid Bit Index Given Error for the Qiskrypt's Quantum Circuit.
                        """

                else:
                    """
                    If the given index of the IBM Qiskit's Classical Register is not valid.
                    """

                    self.raise_invalid_qiskit_classical_register_index_given_error()
                    """
                    Raise an Invalid IBM Qiskit's Classical Register Index Given Error for
                    the Qiskrypt's Quantum Circuit.
                    """

            else:
                """
                If the maximum index value of the list of indexes of qubits in
                the given IBM Qiskit's Quantum Register is not valid.
                """

                self.raise_invalid_qubit_index_given_error()
                """
                Raise an Invalid Qubit Index Given Error for the Qiskrypt's Quantum Circuit.
                """

        else:
            """
            If the given index of the IBM Qiskit's Quantum Register is not valid.
            """

            self.raise_invalid_qiskit_quantum_register_index_given_error()
            """
            Raise an Invalid IBM Qiskit's Quantum Register Index Given Error for
            the Qiskrypt's Quantum Circuit.
            """

    def prepare_and_measure_all_qubits_in_qiskit_quantum_register_in_x_basis(self,
                                                                             qiskit_quantum_register_index: int,
                                                                             qiskit_classical_register_index: int,
                                                                             is_final_measurement=True) -> None:
        """
        Prepare (and possibly, Measure) all the indexes of qubits of the given index of
        an IBM Qiskit's Quantum Register (into all the indexes of bits of the given index of
        an IBM Qiskit's Classical Register), in the X-Basis.

        :param qiskit_quantum_register_index: the index of an IBM Qiskit's Quantum Register.
        :param qiskit_classical_register_index: the index of an IBM Qiskit's Classical Register.
        :param is_final_measurement: a boolean flag to indicate that all the indexes of qubits of
                                     a given index of an IBM Qiskit's Quantum Register are pretended to
                                     be measured into all the indexes of bits of
                                     given index of an IBM Qiskit's Classical Register,
                                     in the Computational Basis (Z-Basis), after being prepared in the X-Basis.
        """

        if qiskit_quantum_register_index < len(self.qiskit_quantum_circuit.qregs):
            """
            If the given index of the IBM Qiskit's Quantum Register is valid.
            """

            if qiskit_classical_register_index < len(self.qiskit_quantum_circuit.cregs):
                """
                If the given index of the IBM Qiskit's Classical Register is valid.
                """

                num_qubits_qiskit_quantum_register = self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_index].size
                """
                Retrieve the number of qubits in the given IBM Qiskit's Quantum Register inside
                the IBM Qiskit's Quantum Circuit.
                """

                num_bits_qiskit_classical_register = self.qiskit_quantum_circuit.cregs[qiskit_classical_register_index].size
                """
                Retrieve the number of bits in the given IBM Qiskit's Classical Register inside
                the IBM Qiskit's Quantum Circuit.
                """

                if num_qubits_qiskit_quantum_register == num_bits_qiskit_classical_register:
                    """
                    If the number of qubits of the given IBM Qiskit's Quantum Register is equal to
                    the number of bits of the given IBM Qiskit's Classical Register,
                    inside the IBM Qiskit's Quantum Circuit.
                    """

                    qubits_indexes = range(num_qubits_qiskit_quantum_register)
                    """
                    Retrieve the list of the range of qubits in the given IBM Qiskit's Quantum Register of
                    the IBM Qiskit's Quantum Circuit.
                    """

                    bits_indexes = range(num_bits_qiskit_classical_register)
                    """
                    Retrieve the list of the range of bits in the given IBM Qiskit's Classical Register of
                    the IBM Qiskit's Quantum Circuit.
                    """

                    for qubit_index, bit_index in zip(qubits_indexes, bits_indexes):
                        """
                        For each pair of indexes of qubits and bits.
                        """

                        self.prepare_and_measure_single_qubit_in_qiskit_quantum_register_in_x_basis(qiskit_quantum_register_index,
                                                                                                    qiskit_classical_register_index,
                                                                                                    qubit_index, bit_index,
                                                                                                    is_final_measurement)
                        """
                        Prepare (and possibly, Measure) the current index of the single qubit of
                        the given IBM Qiskit's Quantum Register (into the current index of
                        the single bit of the given IBM Qiskit's Classical Register), in the X-Basis.
                        """

                else:
                    """
                    If the number of qubits of the given IBM Qiskit's Quantum Register is not equal to
                    the number of bits of the given IBM Qiskit's Classical Register,
                    inside the IBM Qiskit's Quantum Circuit.
                    """

                    self.raise_num_qubits_and_num_bits_are_not_equal_for_operation_or_measurement_error()
                    """
                    Raise the Number of Qubits and Number of Bits are Not Equal for
                    Operation or Measurement Error for the Qiskrypt's Quantum Circuit.
                    """

            else:
                """
                If the given index of the IBM Qiskit's Classical Register is not valid.
                """

                self.raise_invalid_qiskit_classical_register_index_given_error()
                """
                Raise an Invalid IBM Qiskit's Classical Register Index Given Error for
                the Qiskrypt's Quantum Circuit.
                """

        else:
            """
            If the given index of the IBM Qiskit's Quantum Register is not valid.
            """

            self.raise_invalid_qiskit_quantum_register_index_given_error()
            """
            Raise an Invalid IBM Qiskit's Quantum Register Index Given Error for
            the Qiskrypt's Quantum Circuit.
            """

    def prepare_and_measure_all_qubits_in_qiskit_quantum_register_in_y_basis(self,
                                                                             qiskit_quantum_register_index: int,
                                                                             qiskit_classical_register_index: int,
                                                                             is_final_measurement=True) -> None:
        """
        Prepare (and possibly, Measure) all the indexes of qubits of the given index of
        an IBM Qiskit's Quantum Register (into all the indexes of bits of the given index of
        an IBM Qiskit's Classical Register), in the Y-Basis.

        :param qiskit_quantum_register_index: the index of an IBM Qiskit's Quantum Register.
        :param qiskit_classical_register_index: the index of an IBM Qiskit's Classical Register.
        :param is_final_measurement: a boolean flag to indicate that all the indexes of qubits of
                                     a given index of an IBM Qiskit's Quantum Register are pretended to
                                     be measured into all the indexes of bits of
                                     given index of an IBM Qiskit's Classical Register,
                                     in the Computational Basis (Z-Basis), after being prepared in the Y-Basis.
        """

        if qiskit_quantum_register_index < len(self.qiskit_quantum_circuit.qregs):
            """
            If the given index of the IBM Qiskit's Quantum Register is valid.
            """

            if qiskit_classical_register_index < len(self.qiskit_quantum_circuit.cregs):
                """
                If the given index of the IBM Qiskit's Classical Register is valid.
                """

                num_qubits_qiskit_quantum_register = self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_index].size
                """
                Retrieve the number of qubits in the given IBM Qiskit's Quantum Register inside
                the IBM Qiskit's Quantum Circuit.
                """

                num_bits_qiskit_classical_register = self.qiskit_quantum_circuit.cregs[qiskit_classical_register_index].size
                """
                Retrieve the number of bits in the given IBM Qiskit's Classical Register inside
                the IBM Qiskit's Quantum Circuit.
                """

                if num_qubits_qiskit_quantum_register == num_bits_qiskit_classical_register:
                    """
                    If the number of qubits of the given IBM Qiskit's Quantum Register is equal to
                    the number of bits of the given IBM Qiskit's Classical Register,
                    inside the IBM Qiskit's Quantum Circuit.
                    """

                    qubits_indexes = range(num_qubits_qiskit_quantum_register)
                    """
                    Retrieve the list of the range of qubits in the given IBM Qiskit's Quantum Register of
                    the IBM Qiskit's Quantum Circuit.
                    """

                    bits_indexes = range(num_bits_qiskit_classical_register)
                    """
                    Retrieve the list of the range of bits in the given IBM Qiskit's Classical Register of
                    the IBM Qiskit's Quantum Circuit.
                    """

                    for qubit_index, bit_index in zip(qubits_indexes, bits_indexes):
                        """
                        For each pair of indexes of qubits and bits.
                        """

                        self.prepare_and_measure_single_qubit_in_qiskit_quantum_register_in_y_basis(qiskit_quantum_register_index,
                                                                                                    qiskit_classical_register_index,
                                                                                                    qubit_index, bit_index,
                                                                                                    is_final_measurement)
                        """
                        Prepare (and possibly, Measure) the current index of the single qubit of
                        the given IBM Qiskit's Quantum Register (into the current index of
                        the single bit of the given IBM Qiskit's Classical Register), in the Y-Basis.
                        """

                else:
                    """
                    If the number of qubits of the given IBM Qiskit's Quantum Register is not equal to
                    the number of bits of the given IBM Qiskit's Classical Register,
                    inside the IBM Qiskit's Quantum Circuit.
                    """

                    self.raise_num_qubits_and_num_bits_are_not_equal_for_operation_or_measurement_error()
                    """
                    Raise the Number of Qubits and Number of Bits are Not Equal for
                    Operation or Measurement Error for the Qiskrypt's Quantum Circuit.
                    """

            else:
                """
                If the given index of the IBM Qiskit's Classical Register is not valid.
                """

                self.raise_invalid_qiskit_classical_register_index_given_error()
                """
                Raise an Invalid IBM Qiskit's Classical Register Index Given Error for
                the Qiskrypt's Quantum Circuit.
                """

        else:
            """
            If the given index of the IBM Qiskit's Quantum Register is not valid.
            """

            self.raise_invalid_qiskit_quantum_register_index_given_error()
            """
            Raise an Invalid IBM Qiskit's Quantum Register Index Given Error for
            the Qiskrypt's Quantum Circuit.
            """

    def prepare_and_measure_all_qubits_in_qiskit_quantum_register_in_z_basis(self,
                                                                             qiskit_quantum_register_index: int,
                                                                             qiskit_classical_register_index: int,
                                                                             is_final_measurement=True) -> None:
        """
        Prepare (and possibly, Measure) all the indexes of qubits of the given index of
        an IBM Qiskit's Quantum Register (into all the indexes of bits of the given index of
        an IBM Qiskit's Classical Register), in the Z-Basis.

        :param qiskit_quantum_register_index: the index of an IBM Qiskit's Quantum Register.
        :param qiskit_classical_register_index: the index of an IBM Qiskit's Classical Register.
        :param is_final_measurement: a boolean flag to indicate that all the indexes of qubits of
                                     a given index of an IBM Qiskit's Quantum Register are pretended to
                                     be measured into all the indexes of bits of
                                     given index of an IBM Qiskit's Classical Register,
                                     in the Computational Basis (Z-Basis), after being prepared in the Z-Basis.
        """

        if qiskit_quantum_register_index < len(self.qiskit_quantum_circuit.qregs):
            """
            If the given index of the IBM Qiskit's Quantum Register is valid.
            """

            if qiskit_classical_register_index < len(self.qiskit_quantum_circuit.cregs):
                """
                If the given index of the IBM Qiskit's Classical Register is valid.
                """

                num_qubits_qiskit_quantum_register = self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_index].size
                """
                Retrieve the number of qubits in the given IBM Qiskit's Quantum Register inside
                the IBM Qiskit's Quantum Circuit.
                """

                num_bits_qiskit_classical_register = self.qiskit_quantum_circuit.cregs[qiskit_classical_register_index].size
                """
                Retrieve the number of bits in the given IBM Qiskit's Classical Register inside
                the IBM Qiskit's Quantum Circuit.
                """

                if num_qubits_qiskit_quantum_register == num_bits_qiskit_classical_register:
                    """
                    If the number of qubits of the given IBM Qiskit's Quantum Register is equal to
                    the number of bits of the given IBM Qiskit's Classical Register,
                    inside the IBM Qiskit's Quantum Circuit.
                    """

                    qubits_indexes = range(num_qubits_qiskit_quantum_register)
                    """
                    Retrieve the list of the range of qubits in the given IBM Qiskit's Quantum Register of
                    the IBM Qiskit's Quantum Circuit.
                    """

                    bits_indexes = range(num_bits_qiskit_classical_register)
                    """
                    Retrieve the list of the range of bits in the given IBM Qiskit's Classical Register of
                    the IBM Qiskit's Quantum Circuit.
                    """

                    for qubit_index, bit_index in zip(qubits_indexes, bits_indexes):
                        """
                        For each pair of indexes of qubits and bits.
                        """

                        self.prepare_and_measure_single_qubit_in_qiskit_quantum_register_in_z_basis(qiskit_quantum_register_index,
                                                                                                    qiskit_classical_register_index,
                                                                                                    qubit_index, bit_index,
                                                                                                    is_final_measurement)
                        """
                        Prepare (and possibly, Measure) the current index of the single qubit of
                        the given IBM Qiskit's Quantum Register (into the current index of
                        the single bit of the given IBM Qiskit's Classical Register), in the Z-Basis.
                        """

                else:
                    """
                    If the number of qubits of the given IBM Qiskit's Quantum Register is not equal to
                    the number of bits of the given IBM Qiskit's Classical Register,
                    inside the IBM Qiskit's Quantum Circuit.
                    """

                    self.raise_num_qubits_and_num_bits_are_not_equal_for_operation_or_measurement_error()
                    """
                    Raise the Number of Qubits and Number of Bits are Not Equal for
                    Operation or Measurement Error for the Qiskrypt's Quantum Circuit.
                    """

            else:
                """
                If the given index of the IBM Qiskit's Classical Register is not valid.
                """

                self.raise_invalid_qiskit_classical_register_index_given_error()
                """
                Raise an Invalid IBM Qiskit's Classical Register Index Given Error for
                the Qiskrypt's Quantum Circuit.
                """

        else:
            """
            If the given index of the IBM Qiskit's Quantum Register is not valid.
            """

            self.raise_invalid_qiskit_quantum_register_index_given_error()
            """
            Raise an Invalid IBM Qiskit's Quantum Register Index Given Error for
            the Qiskrypt's Quantum Circuit.
            """

    def prepare_and_measure_set_qubits_in_all_qiskit_quantum_registers_in_x_basis(self,
                                                                                  qubits_indexes: list,
                                                                                  bits_indexes: list,
                                                                                  is_final_measurement=True) -> None:
        """
        Prepare (and possibly, Measure) a set of indexes of qubits of all the indexes of
        IBM Qiskit's Quantum Registers (into a set of the indexes of bits of all the indexes of
        IBM Qiskit's Classical Registers), in the X-Basis.

        :param qubits_indexes: the list of indexes of qubits inside all the IBM Qiskit's Quantum Registers.
        :param bits_indexes: the list of indexes of bits inside all the IBM Qiskit's Classical Registers.
        :param is_final_measurement: a boolean flag to indicate that all the indexes of qubits of
                                     all the indexes of IBM Qiskit's Quantum Registers are pretended to
                                     be measured into all the indexes of bits of
                                     all the indexes of IBM Qiskit's Classical Registers,
                                     in the Computational Basis (Z-Basis), after being prepared in the X-Basis.
        """

        num_total_qiskit_quantum_registers = len(self.qiskit_quantum_circuit.qregs)
        """
        Retrieve the total number of IBM Qiskit's Quantum Registers
        in the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit.
        """

        num_total_qiskit_classical_registers = len(self.qiskit_quantum_circuit.cregs)
        """
        Retrieve the total number of IBM Qiskit's Classical Registers
        in the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit.
        """

        if num_total_qiskit_quantum_registers == num_total_qiskit_classical_registers:
            """
            If the total number of IBM Qiskit's Quantum Registers and
            the total number of IBM Qiskit's Classical Registers are equal.
            """

            qubits_indexes = list(dict.fromkeys(qubits_indexes))
            """
            Remove indexes of duplicated qubits.
            """

            bits_indexes = list(dict.fromkeys(bits_indexes))
            """
            Remove indexes of duplicated bits.
            """

            num_qubits_indexes = len(qubits_indexes)
            """
            Retrieve the number of distinct indexes of qubits.
            """

            num_bits_indexes = len(bits_indexes)
            """
            Retrieve the number of distinct indexes of bits.
            """

            if num_qubits_indexes == num_bits_indexes:
                """
                The number of indexes of qubits and the number of indexes of bits are equal.
                """

                qiskit_quantum_registers_indexes = range(num_total_qiskit_quantum_registers)
                """
                Retrieve the indexes of all the IBM Qiskit's Quantum Registers.
                """

                qiskit_classical_registers_indexes = range(num_total_qiskit_classical_registers)
                """
                Retrieve the indexes of all the IBM Qiskit's Classical Registers.
                """

                for qiskit_quantum_register_index, qiskit_classical_register_index \
                        in zip(qiskit_quantum_registers_indexes, qiskit_classical_registers_indexes):
                    """
                    For each pair of indexes of IBM Qiskit's Quantum Registers and IBM Qiskit's Classical Registers.
                    """

                    self.prepare_and_measure_set_qubits_in_qiskit_quantum_register_in_x_basis(qiskit_quantum_register_index,
                                                                                              qiskit_classical_register_index,
                                                                                              qubits_indexes, bits_indexes,
                                                                                              is_final_measurement)
                    """
                    Prepare (and possibly, Measure) the given list of indexes of qubits of 
                    the current index of an IBM Qiskit's Quantum Register
                    (into a given list of indexes of bits of the current index of
                    an IBM Qiskit's Classical Register), in the X-Basis.
                    """

            else:
                """
                The number of indexes of qubits and the number of indexes of bits are not equal.
                """

                self.raise_num_qubits_and_num_bits_are_not_equal_for_operation_or_measurement_error()
                """
                Raise the Number of Qubits and Number of Bits are Not Equal for
                Operation or Measurement Error for the Qiskrypt's Quantum Circuit.
                """

        else:
            """
            If the total number of IBM Qiskit's Quantum Registers and
            the total number of IBM Qiskit's Classical Registers are not equal.
            """

            self.raise_num_quantum_registers_and_num_classical_registers_are_not_equal_for_operation_or_measurement_error()
            """
            Raise the Number of Quantum Registers and Number of Classical Registers are Not Equal for
            Operation or Measurement Error for the Qiskrypt's Quantum Circuit.
            """

    def prepare_and_measure_set_qubits_in_all_qiskit_quantum_registers_in_y_basis(self,
                                                                                  qubits_indexes: list,
                                                                                  bits_indexes: list,
                                                                                  is_final_measurement=True) -> None:
        """
        Prepare (and possibly, Measure) a set of indexes of qubits of all the indexes of
        IBM Qiskit's Quantum Registers (into a set of the indexes of bits of all the indexes of
        IBM Qiskit's Classical Registers), in the Y-Basis.

        :param qubits_indexes: the list of indexes of qubits inside all the IBM Qiskit's Quantum Registers.
        :param bits_indexes: the list of indexes of bits inside all the IBM Qiskit's Classical Registers.
        :param is_final_measurement: a boolean flag to indicate that all the indexes of qubits of
                                     all the indexes of IBM Qiskit's Quantum Registers are pretended to
                                     be measured into all the indexes of bits of
                                     all the indexes of IBM Qiskit's Classical Registers,
                                     in the Computational Basis (Z-Basis), after being prepared in the Y-Basis.
        """

        num_total_qiskit_quantum_registers = len(self.qiskit_quantum_circuit.qregs)
        """
        Retrieve the total number of IBM Qiskit's Quantum Registers
        in the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit.
        """

        num_total_qiskit_classical_registers = len(self.qiskit_quantum_circuit.cregs)
        """
        Retrieve the total number of IBM Qiskit's Classical Registers
        in the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit.
        """

        if num_total_qiskit_quantum_registers == num_total_qiskit_classical_registers:
            """
            If the total number of IBM Qiskit's Quantum Registers and
            the total number of IBM Qiskit's Classical Registers are equal.
            """

            qubits_indexes = list(dict.fromkeys(qubits_indexes))
            """
            Remove indexes of duplicated qubits.
            """

            bits_indexes = list(dict.fromkeys(bits_indexes))
            """
            Remove indexes of duplicated bits.
            """

            num_qubits_indexes = len(qubits_indexes)
            """
            Retrieve the number of distinct indexes of qubits.
            """

            num_bits_indexes = len(bits_indexes)
            """
            Retrieve the number of distinct indexes of bits.
            """

            if num_qubits_indexes == num_bits_indexes:
                """
                The number of indexes of qubits and the number of indexes of bits are equal.
                """

                qiskit_quantum_registers_indexes = range(num_total_qiskit_quantum_registers)
                """
                Retrieve the indexes of all the IBM Qiskit's Quantum Registers.
                """

                qiskit_classical_registers_indexes = range(num_total_qiskit_classical_registers)
                """
                Retrieve the indexes of all the IBM Qiskit's Classical Registers.
                """

                for qiskit_quantum_register_index, qiskit_classical_register_index \
                        in zip(qiskit_quantum_registers_indexes, qiskit_classical_registers_indexes):
                    """
                    For each pair of indexes of IBM Qiskit's Quantum Registers and IBM Qiskit's Classical Registers.
                    """

                    self.prepare_and_measure_set_qubits_in_qiskit_quantum_register_in_y_basis(qiskit_quantum_register_index,
                                                                                              qiskit_classical_register_index,
                                                                                              qubits_indexes, bits_indexes,
                                                                                              is_final_measurement)
                    """
                    Prepare (and possibly, Measure) the given list of indexes of qubits of 
                    the current index of an IBM Qiskit's Quantum Register
                    (into a given list of indexes of bits of the current index of
                    an IBM Qiskit's Classical Register), in the Y-Basis.
                    """

            else:
                """
                The number of indexes of qubits and the number of indexes of bits are not equal.
                """

                self.raise_num_qubits_and_num_bits_are_not_equal_for_operation_or_measurement_error()
                """
                Raise the Number of Qubits and Number of Bits are Not Equal for
                Operation or Measurement Error for the Qiskrypt's Quantum Circuit.
                """

        else:
            """
            If the total number of IBM Qiskit's Quantum Registers and
            the total number of IBM Qiskit's Classical Registers are not equal.
            """

            self.raise_num_quantum_registers_and_num_classical_registers_are_not_equal_for_operation_or_measurement_error()
            """
            Raise the Number of Quantum Registers and Number of Classical Registers are Not Equal for
            Operation or Measurement Error for the Qiskrypt's Quantum Circuit.
            """

    def prepare_and_measure_set_qubits_in_all_qiskit_quantum_register_in_z_basis(self,
                                                                                 qubits_indexes: list,
                                                                                 bits_indexes: list,
                                                                                 is_final_measurement=True) -> None:
        """
        Prepare (and possibly, Measure) a set of indexes of qubits of all the indexes of
        IBM Qiskit's Quantum Registers (into a set of the indexes of bits of all the indexes of
        IBM Qiskit's Classical Registers), in the Z-Basis.

        :param qubits_indexes: the list of indexes of qubits inside all the IBM Qiskit's Quantum Registers.
        :param bits_indexes: the list of indexes of bits inside all the IBM Qiskit's Classical Registers.
        :param is_final_measurement: a boolean flag to indicate that all the indexes of qubits of
                                     all the indexes of IBM Qiskit's Quantum Registers are pretended to
                                     be measured into all the indexes of bits of
                                     all the indexes of IBM Qiskit's Classical Registers,
                                     in the Computational Basis (Z-Basis), after being prepared in the Z-Basis.
        """

        num_total_qiskit_quantum_registers = len(self.qiskit_quantum_circuit.qregs)
        """
        Retrieve the total number of IBM Qiskit's Quantum Registers
        in the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit.
        """

        num_total_qiskit_classical_registers = len(self.qiskit_quantum_circuit.cregs)
        """
        Retrieve the total number of IBM Qiskit's Classical Registers
        in the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit.
        """

        if num_total_qiskit_quantum_registers == num_total_qiskit_classical_registers:
            """
            If the total number of IBM Qiskit's Quantum Registers and
            the total number of IBM Qiskit's Classical Registers are equal.
            """

            qubits_indexes = list(dict.fromkeys(qubits_indexes))
            """
            Remove indexes of duplicated qubits.
            """

            bits_indexes = list(dict.fromkeys(bits_indexes))
            """
            Remove indexes of duplicated bits.
            """

            num_qubits_indexes = len(qubits_indexes)
            """
            Retrieve the number of distinct indexes of qubits.
            """

            num_bits_indexes = len(bits_indexes)
            """
            Retrieve the number of distinct indexes of bits.
            """

            if num_qubits_indexes == num_bits_indexes:
                """
                The number of indexes of qubits and the number of indexes of bits are equal.
                """

                qiskit_quantum_registers_indexes = range(num_total_qiskit_quantum_registers)
                """
                Retrieve the indexes of all the IBM Qiskit's Quantum Registers.
                """

                qiskit_classical_registers_indexes = range(num_total_qiskit_classical_registers)
                """
                Retrieve the indexes of all the IBM Qiskit's Classical Registers.
                """

                for qiskit_quantum_register_index, qiskit_classical_register_index \
                        in zip(qiskit_quantum_registers_indexes, qiskit_classical_registers_indexes):
                    """
                    For each pair of indexes of IBM Qiskit's Quantum Registers and IBM Qiskit's Classical Registers.
                    """

                    self.prepare_and_measure_set_qubits_in_qiskit_quantum_register_in_z_basis(qiskit_quantum_register_index,
                                                                                              qiskit_classical_register_index,
                                                                                              qubits_indexes, bits_indexes,
                                                                                              is_final_measurement)
                    """
                    Prepare (and possibly, Measure) the given list of indexes of qubits of 
                    the current index of an IBM Qiskit's Quantum Register
                    (into a given list of indexes of bits of the current index of
                    an IBM Qiskit's Classical Register), in the Z-Basis.
                    """

            else:
                """
                The number of indexes of qubits and the number of indexes of bits are not equal.
                """

                self.raise_num_qubits_and_num_bits_are_not_equal_for_operation_or_measurement_error()
                """
                Raise the Number of Qubits and Number of Bits are Not Equal for
                Operation or Measurement Error for the Qiskrypt's Quantum Circuit.
                """

        else:
            """
            If the total number of IBM Qiskit's Quantum Registers and
            the total number of IBM Qiskit's Classical Registers are not equal.
            """

            self.raise_num_quantum_registers_and_num_classical_registers_are_not_equal_for_operation_or_measurement_error()
            """
            Raise the Number of Quantum Registers and Number of Classical Registers are Not Equal for
            Operation or Measurement Error for the Qiskrypt's Quantum Circuit.
            """

    def prepare_and_measure_all_qubits_in_all_qiskit_quantum_registers_in_x_basis(self,
                                                                                  is_final_measurement=True) -> None:
        """
        Prepare (and possibly, Measure) all the indexes of qubits of all the indexes of
        IBM Qiskit's Quantum Registers (into all the indexes of bits of all the indexes of
        IBM Qiskit's Classical Registers), in the X-Basis.

        :param is_final_measurement: a boolean flag to indicate that all the indexes of qubits of
                                     all the indexes of IBM Qiskit's Quantum Registers are pretended to
                                     be measured into all the indexes of bits of
                                     all the indexes of IBM Qiskit's Classical Registers,
                                     in the Computational Basis (Z-Basis), after being prepared in the X-Basis.
        """

        num_total_qiskit_quantum_registers = len(self.qiskit_quantum_circuit.qregs)
        """
        Retrieve the total number of IBM Qiskit's Quantum Registers
        in the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit.
        """

        num_total_qiskit_classical_registers = len(self.qiskit_quantum_circuit.cregs)
        """
        Retrieve the total number of IBM Qiskit's Classical Registers
        in the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit.
        """

        if num_total_qiskit_quantum_registers == num_total_qiskit_classical_registers:
            """
            If the total number of IBM Qiskit's Quantum Registers and
            the total number of IBM Qiskit's Classical Registers are equal.
            """

            qiskit_quantum_registers_indexes = range(num_total_qiskit_quantum_registers)
            """
            Retrieve the indexes of the IBM Qiskit's Quantum Registers in the IBM Qiskit's Quantum Circuit.
            """

            qiskit_classical_registers_indexes = range(num_total_qiskit_classical_registers)
            """
            Retrieve the indexes of the IBM Qiskit's Classical Registers in the IBM Qiskit's Quantum Circuit.            
            """

            for qiskit_quantum_register_index, qiskit_classical_register_index \
                    in zip(qiskit_quantum_registers_indexes, qiskit_classical_registers_indexes):
                """
                For each pair of indexes of IBM Qiskit's Quantum Registers and IBM Qiskit's Classical Registers.
                """

                self.prepare_and_measure_all_qubits_in_qiskit_quantum_register_in_x_basis(qiskit_quantum_register_index,
                                                                                          qiskit_classical_register_index,
                                                                                          is_final_measurement)
                """
                Prepare (and possibly, Measure) all the indexes of qubits of the given index of
                the current IBM Qiskit's Quantum Register
                (into all the indexes of bits of the given index of
                the current IBM Qiskit's Classical Register), in the X-Basis.
                """

        else:
            """
            If the total number of IBM Qiskit's Quantum Registers and
            the total number of IBM Qiskit's Classical Registers are not equal.
            """

            self.raise_num_quantum_registers_and_num_classical_registers_are_not_equal_for_operation_or_measurement_error()
            """
            Raise the Number of Quantum Registers and Number of Classical Registers are Not Equal for
            Operation or Measurement Error for the Qiskrypt's Quantum Circuit.
            """

    def prepare_and_measure_all_qubits_in_all_qiskit_quantum_registers_in_y_basis(self,
                                                                                  is_final_measurement=True) -> None:
        """
        Prepare (and possibly, Measure) all the indexes of qubits of all the indexes of
        IBM Qiskit's Quantum Registers (into all the indexes of bits of all the indexes of
        IBM Qiskit's Classical Registers), in the Y-Basis.

        :param is_final_measurement: a boolean flag to indicate that all the indexes of qubits of
                                     all the indexes of IBM Qiskit's Quantum Registers are pretended to
                                     be measured into all the indexes of bits of
                                     all the indexes of IBM Qiskit's Classical Registers,
                                     in the Computational Basis (Z-Basis), after being prepared in the Y-Basis.
        """

        num_total_qiskit_quantum_registers = len(self.qiskit_quantum_circuit.qregs)
        """
        Retrieve the total number of IBM Qiskit's Quantum Registers
        in the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit.
        """

        num_total_qiskit_classical_registers = len(self.qiskit_quantum_circuit.cregs)
        """
        Retrieve the total number of IBM Qiskit's Classical Registers
        in the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit.
        """

        if num_total_qiskit_quantum_registers == num_total_qiskit_classical_registers:
            """
            If the total number of IBM Qiskit's Quantum Registers and
            the total number of IBM Qiskit's Classical Registers are equal.
            """

            qiskit_quantum_registers_indexes = range(num_total_qiskit_quantum_registers)
            """
            Retrieve the indexes of the IBM Qiskit's Quantum Registers in the IBM Qiskit's Quantum Circuit.
            """

            qiskit_classical_registers_indexes = range(num_total_qiskit_classical_registers)
            """
            Retrieve the indexes of the IBM Qiskit's Classical Registers in the IBM Qiskit's Quantum Circuit.            
            """

            for qiskit_quantum_register_index, qiskit_classical_register_index \
                    in zip(qiskit_quantum_registers_indexes, qiskit_classical_registers_indexes):
                """
                For each pair of indexes of IBM Qiskit's Quantum Registers and IBM Qiskit's Classical Registers.
                """

                self.prepare_and_measure_all_qubits_in_qiskit_quantum_register_in_y_basis(qiskit_quantum_register_index,
                                                                                          qiskit_classical_register_index,
                                                                                          is_final_measurement)
                """
                Prepare (and possibly, Measure) all the indexes of qubits of the given index of
                the current IBM Qiskit's Quantum Register
                (into all the indexes of bits of the given index of
                the current IBM Qiskit's Classical Register), in the Y-Basis.
                """

        else:
            """
            If the total number of IBM Qiskit's Quantum Registers and
            the total number of IBM Qiskit's Classical Registers are not equal.
            """

            self.raise_num_quantum_registers_and_num_classical_registers_are_not_equal_for_operation_or_measurement_error()
            """
            Raise the Number of Quantum Registers and Number of Classical Registers are Not Equal for
            Operation or Measurement Error for the Qiskrypt's Quantum Circuit.
            """

    def prepare_and_measure_all_qubits_in_all_qiskit_quantum_registers_in_z_basis(self,
                                                                                  is_final_measurement=True) -> None:
        """
        Prepare (and possibly, Measure) all the indexes of qubits of all the indexes of
        IBM Qiskit's Quantum Registers (into all the indexes of bits of all the indexes of
        IBM Qiskit's Classical Registers), in the Z-Basis.

        :param is_final_measurement: a boolean flag to indicate that all the indexes of qubits of
                                     all the indexes of IBM Qiskit's Quantum Registers are pretended to
                                     be measured into all the indexes of bits of
                                     all the indexes of IBM Qiskit's Classical Registers,
                                     in the Computational Basis (Z-Basis), after being prepared in the Z-Basis.
        """

        num_total_qiskit_quantum_registers = len(self.qiskit_quantum_circuit.qregs)
        """
        Retrieve the total number of IBM Qiskit's Quantum Registers
        in the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit.
        """

        num_total_qiskit_classical_registers = len(self.qiskit_quantum_circuit.cregs)
        """
        Retrieve the total number of IBM Qiskit's Classical Registers
        in the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit.
        """

        if num_total_qiskit_quantum_registers == num_total_qiskit_classical_registers:
            """
            If the total number of IBM Qiskit's Quantum Registers and
            the total number of IBM Qiskit's Classical Registers are equal.
            """

            qiskit_quantum_registers_indexes = range(num_total_qiskit_quantum_registers)
            """
            Retrieve the indexes of the IBM Qiskit's Quantum Registers in the IBM Qiskit's Quantum Circuit.
            """

            qiskit_classical_registers_indexes = range(num_total_qiskit_classical_registers)
            """
            Retrieve the indexes of the IBM Qiskit's Classical Registers in the IBM Qiskit's Quantum Circuit.            
            """

            for qiskit_quantum_register_index, qiskit_classical_register_index \
                    in zip(qiskit_quantum_registers_indexes, qiskit_classical_registers_indexes):
                """
                For each pair of indexes of IBM Qiskit's Quantum Registers and IBM Qiskit's Classical Registers.
                """

                self.prepare_and_measure_all_qubits_in_qiskit_quantum_register_in_z_basis(qiskit_quantum_register_index,
                                                                                          qiskit_classical_register_index,
                                                                                          is_final_measurement)
                """
                Prepare (and possibly, Measure) all the indexes of qubits of the given index of
                the current IBM Qiskit's Quantum Register
                (into all the indexes of bits of the given index of
                the current IBM Qiskit's Classical Register), in the Z-Basis.
                """

        else:
            """
            If the total number of IBM Qiskit's Quantum Registers and
            the total number of IBM Qiskit's Classical Registers are not equal.
            """

            self.raise_num_quantum_registers_and_num_classical_registers_are_not_equal_for_operation_or_measurement_error()
            """
            Raise the Number of Quantum Registers and Number of Classical Registers are Not Equal for
            Operation or Measurement Error for the Qiskrypt's Quantum Circuit.
            """

    """
    3) Single Qubit Gates/Operations Methods:
    """

    def apply_pauli_i(self, qiskit_quantum_register_index: int, qubit_index: int) -> None:
        """
        Apply the Pauli-I (Idle) Gate/Operation to given indexes of
        an IBM Qiskit's Quantum Register and a target qubit.

        :param qiskit_quantum_register_index: the index of an IBM Qiskit's Quantum Register.
        :param qubit_index: the index of a qubit inside that IBM Qiskit's Quantum Register.
        """

        is_possible_to_apply_operation = \
            self.check_if_is_possible_to_apply_operation(qiskit_quantum_register_index, qubit_index, True)
        """
        Check if it is possible to apply the pretended operation.
        """

        if is_possible_to_apply_operation:
            """
            It is possible to apply the pretended operation.
            """

            self.qiskit_quantum_circuit.id(self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_index][qubit_index])
            """
            Apply the Pauli-I (Idle) Gate/Operation to the given qubit of the given IBM Qiskit's Quantum Register. 
            """

    def apply_pauli_x(self, qiskit_quantum_register_index: int, qubit_index: int) -> None:
        """
        Apply the Pauli-X (NOT/Bit Flip) Gate/Operation to given indexes of
        an IBM Qiskit's Quantum Register and a target qubit.

        :param qiskit_quantum_register_index: the index of an IBM Qiskit's Quantum Register.
        :param qubit_index: the index of a qubit inside that IBM Qiskit's Quantum Register.
        """

        is_possible_to_apply_operation = \
            self.check_if_is_possible_to_apply_operation(qiskit_quantum_register_index, qubit_index, False)
        """
        Check if it is possible to apply the pretended operation.
        """

        if is_possible_to_apply_operation:
            """
            It is possible to apply the pretended operation.
            """

            self.qiskit_quantum_circuit.x(self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_index][qubit_index])
            """
            Apply the Pauli-X (NOT/Bit Flip) Gate/Operation to the given qubit of the given IBM Qiskit's Quantum Register. 
            """

    def apply_pauli_y(self, qiskit_quantum_register_index: int, qubit_index: int) -> None:
        """
        Apply the Pauli-Y Gate/Operation to given indexes of
        an IBM Qiskit's Quantum Register and a target qubit.

        :param qiskit_quantum_register_index: the index of an IBM Qiskit's Quantum Register.
        :param qubit_index: the index of a qubit inside that IBM Qiskit's Quantum Register.
        """

        is_possible_to_apply_operation = \
            self.check_if_is_possible_to_apply_operation(qiskit_quantum_register_index, qubit_index, True)
        """
        Check if it is possible to apply the pretended operation.
        """

        if is_possible_to_apply_operation:
            """
            It is possible to apply the pretended operation.
            """

            self.qiskit_quantum_circuit.y(self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_index][qubit_index])
            """
            Apply the Pauli-Y Gate/Operation to the given qubit of the given IBM Qiskit's Quantum Register. 
            """

    def apply_pauli_z(self, qiskit_quantum_register_index: int, qubit_index: int) -> None:
        """
        Apply the Pauli-Z (Phase Flip/Shift) Gate/Operation to given indexes of
        an IBM Qiskit's Quantum Register and a target qubit.

        :param qiskit_quantum_register_index: the index of an IBM Qiskit's Quantum Register.
        :param qubit_index: the index of a qubit inside that IBM Qiskit's Quantum Register.
        """

        is_possible_to_apply_operation = \
            self.check_if_is_possible_to_apply_operation(qiskit_quantum_register_index, qubit_index, True)
        """
        Check if it is possible to apply the pretended operation.
        """

        if is_possible_to_apply_operation:
            """
            It is possible to apply the pretended operation.
            """

            self.qiskit_quantum_circuit.z(self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_index][qubit_index])
            """
            Apply the Pauli-Z (Phase Flip/Shift) Gate/Operation to the given qubit of the given IBM Qiskit's Quantum Register. 
            """

    def apply_hadamard(self, qiskit_quantum_register_index: int, qubit_index: int) -> None:
        """
        Apply the Hadamard Gate/Operation to given indexes of
        an IBM Qiskit's Quantum Register and a target qubit.

        :param qiskit_quantum_register_index: the index of an IBM Qiskit's Quantum Register.
        :param qubit_index: the index of a qubit inside that IBM Qiskit's Quantum Register.
        """

        is_possible_to_apply_operation = \
            self.check_if_is_possible_to_apply_operation(qiskit_quantum_register_index, qubit_index, True)
        """
        Check if it is possible to apply the pretended operation.
        """

        if is_possible_to_apply_operation:
            """
            It is possible to apply the pretended operation.
            """

            self.qiskit_quantum_circuit.h(self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_index][qubit_index])
            """
            Apply the Hadamard Gate/Operation to the given qubit of the given IBM Qiskit's Quantum Register. 
            """

    def apply_phase_s(self, qiskit_quantum_register_index: int, qubit_index: int) -> None:
        """
        Apply the Phase S (pi/2) Gate/Operation to given indexes of
        an IBM Qiskit's Quantum Register and a target qubit.

        :param qiskit_quantum_register_index: the index of an IBM Qiskit's Quantum Register.
        :param qubit_index: the index of a qubit inside that IBM Qiskit's Quantum Register.
        """

        is_possible_to_apply_operation = \
            self.check_if_is_possible_to_apply_operation(qiskit_quantum_register_index, qubit_index, True)
        """
        Check if it is possible to apply the pretended operation.
        """

        if is_possible_to_apply_operation:
            """
            It is possible to apply the pretended operation.
            """

            self.qiskit_quantum_circuit.s(self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_index][qubit_index])
            """
            Apply the Phase S (pi/2) Gate/Operation to the given qubit of the given IBM Qiskit's Quantum Register. 
            """

    def apply_phase_t(self, qiskit_quantum_register_index: int, qubit_index: int) -> None:
        """
        Apply the Phase T (pi/4) Gate/Operation to given indexes of
        an IBM Qiskit's Quantum Register and a target qubit.

        :param qiskit_quantum_register_index: the index of an IBM Qiskit's Quantum Register.
        :param qubit_index: the index of a qubit inside that IBM Qiskit's Quantum Register.
        """

        is_possible_to_apply_operation = \
            self.check_if_is_possible_to_apply_operation(qiskit_quantum_register_index, qubit_index, True)
        """
        Check if it is possible to apply the pretended operation.
        """

        if is_possible_to_apply_operation:
            """
            It is possible to apply the pretended operation.
            """

            self.qiskit_quantum_circuit.t(self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_index][qubit_index])
            """
            Apply the Phase T (pi/4) Gate/Operation to the given qubit of the given IBM Qiskit's Quantum Register. 
            """

    def apply_phase_p_radians(self, theta_radians: float, qiskit_quantum_register_index: int, qubit_index: int) -> None:
        """
        Apply the Phase-P(theta_radians) Gate/Operation to given indexes of
        an IBM Qiskit's Quantum Register and a target qubit,
        considering also the given theta angle in radians.

        :param theta_radians: the theta angle in radians, for the Phase-P(theta_radians) Gate/Operation.
        :param qiskit_quantum_register_index: the index of an IBM Qiskit's Quantum Register.
        :param qubit_index: the index of a qubit inside that IBM Qiskit's Quantum Register.
        """

        is_possible_to_apply_operation = \
            self.check_if_is_possible_to_apply_operation(qiskit_quantum_register_index, qubit_index, True)
        """
        Check if it is possible to apply the pretended operation.
        """

        if is_possible_to_apply_operation:
            """
            It is possible to apply the pretended operation.
            """

            self.qiskit_quantum_circuit.p(theta_radians,
                                          self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_index][qubit_index])
            """
            Apply the Phase-P(theta_radians) Gate/Operation to
            the given qubit of the given IBM Qiskit's Quantum Register. 
            """

    def apply_phase_p_degrees(self, theta_degrees: float, qiskit_quantum_register_index: int, qubit_index: int) -> None:
        """
        Apply the Phase-P(theta_degrees) Gate/Operation to given indexes of
        an IBM Qiskit's Quantum Register and a target qubit,
        considering also the given theta angle in radians.

        :param theta_degrees: the theta angle in degrees, for the Phase-P(theta_radians) Gate/Operation.
        :param qiskit_quantum_register_index: the index of an IBM Qiskit's Quantum Register.
        :param qubit_index: the index of a qubit inside that IBM Qiskit's Quantum Register.
        """

        theta_radians = radians(theta_degrees)
        """
        Convert the theta angle in degrees to radians.
        """

        self.apply_phase_p_radians(theta_radians, qiskit_quantum_register_index, qubit_index)
        """
        Apply the Phase-P(theta_radians) Gate/Operation to given indexes of
        an IBM Qiskit's Quantum Register and a target qubit,
        considering also the given theta angle in radians.
        """

    def apply_bit_flip(self, qiskit_quantum_register_index: int, qubit_index: int) -> None:
        """
        Apply the Bit Flip Gate/Operation to given indexes of
        an IBM Qiskit's Quantum Register and a target qubit.

        :param qiskit_quantum_register_index: the index of an IBM Qiskit's Quantum Register.
        :param qubit_index: the index of a qubit inside that IBM Qiskit's Quantum Register.
        """

        self.apply_pauli_x(qiskit_quantum_register_index, qubit_index)
        """
        Apply the equivalent Pauli-X (NOT/Bit Flip) Gate/Operation to the given qubit of
        the given IBM Qiskit's Quantum Register. 
        """

    def apply_phase_shifter_radians(self,
                                    theta_radians: float,
                                    qiskit_quantum_register_index: int,
                                    qubit_index: int) -> None:
        """
        Apply the Phase-Shifter(theta_radians) Gate/Operation to given indexes of
        an IBM Qiskit's Quantum Register and a target qubit.

        :param theta_radians: the theta angle in radians, for the Phase-Shifter(theta_radians) Gate/Operation.
        :param qiskit_quantum_register_index: the index of an IBM Qiskit's Quantum Register.
        :param qubit_index: the index of a qubit inside that IBM Qiskit's Quantum Register.
        """

        self.apply_phase_p_radians(theta_radians, qiskit_quantum_register_index, qubit_index)
        """
        Apply the equivalent Phase-P(theta_radians) Gate/Operation to the given qubit of
        the given IBM Qiskit's Quantum Register. 
        """

    def apply_phase_shifter_degrees(self,
                                    theta_degrees: float,
                                    qiskit_quantum_register_index: int,
                                    qubit_index: int) -> None:
        """
        Apply the Phase-Shifter(theta_degrees) Gate/Operation to given indexes of
        an IBM Qiskit's Quantum Register and a target qubit.

        :param theta_degrees: the theta angle in radians, for the Phase-Shifter(theta_radians) Gate/Operation.
        :param qiskit_quantum_register_index: the index of an IBM Qiskit's Quantum Register.
        :param qubit_index: the index of a qubit inside that IBM Qiskit's Quantum Register.
        """

        self.apply_phase_p_degrees(theta_degrees, qiskit_quantum_register_index, qubit_index)
        """
        Apply the equivalent Phase-P(theta_degrees) Gate/Operation to the given qubit of
        the given IBM Qiskit's Quantum Register. 
        """

    def apply_beamsplitter(self, qiskit_quantum_register_index: int, qubit_index: int) -> None:
        """
        Apply the Beamsplitter Gate/Operation to given indexes of
        an IBM Qiskit's Quantum Register and a target qubit.

        :param qiskit_quantum_register_index: the index of an IBM Qiskit's Quantum Register.
        :param qubit_index: the index of a qubit inside that IBM Qiskit's Quantum Register.
        """

        self.apply_hadamard(qiskit_quantum_register_index, qubit_index)
        """
        Apply the equivalent Hadamard Gate/Operation to the given qubit of
        the given IBM Qiskit's Quantum Register. 
        """

    def apply_phase_s_adjoint(self, qiskit_quantum_register_index: int, qubit_index: int) -> None:
        """
        Apply the Phase S (-pi/2) Adjoint Gate/Operation to given indexes of
        an IBM Qiskit's Quantum Register and a target qubit.

        :param qiskit_quantum_register_index: the index of an IBM Qiskit's Quantum Register.
        :param qubit_index: the index of a qubit inside that IBM Qiskit's Quantum Register.
        """

        is_possible_to_apply_operation = \
            self.check_if_is_possible_to_apply_operation(qiskit_quantum_register_index, qubit_index, True)
        """
        Check if it is possible to apply the pretended operation.
        """

        if is_possible_to_apply_operation:
            """
            It is possible to apply the pretended operation.
            """

            self.qiskit_quantum_circuit.sdg(self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_index][qubit_index])
            """
            Apply the Phase S (-pi/2) Adjoint Gate/Operation to the given qubit of the given IBM Qiskit's Quantum Register. 
            """

    def apply_phase_t_adjoint(self, qiskit_quantum_register_index: int, qubit_index: int) -> None:
        """
        Apply the Phase T (-pi/4) Adjoint Gate/Operation to given indexes of
        an IBM Qiskit's Quantum Register and a target qubit.

        :param qiskit_quantum_register_index: the index of an IBM Qiskit's Quantum Register.
        :param qubit_index: the index of a qubit inside that IBM Qiskit's Quantum Register.
        """

        is_possible_to_apply_operation = \
            self.check_if_is_possible_to_apply_operation(qiskit_quantum_register_index, qubit_index, True)
        """
        Check if it is possible to apply the pretended operation.
        """

        if is_possible_to_apply_operation:
            """
            It is possible to apply the pretended operation.
            """

            self.qiskit_quantum_circuit.tdg(self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_index][qubit_index])
            """
            Apply the Phase T (-pi/4) Adjoint Gate/Operation to the given qubit of the given IBM Qiskit's Quantum Register. 
            """

    def apply_squared_root_pauli_x(self, qiskit_quantum_register_index: int, qubit_index: int) -> None:
        """
        Apply the Squared Root of the Pauli-X (NOT/Bit Flip) Gate/Operation to given indexes of
        an IBM Qiskit's Quantum Register and a target qubit.

        :param qiskit_quantum_register_index: the index of an IBM Qiskit's Quantum Register.
        :param qubit_index: the index of a qubit inside that IBM Qiskit's Quantum Register.
        """

        is_possible_to_apply_operation = \
            self.check_if_is_possible_to_apply_operation(qiskit_quantum_register_index, qubit_index, True)
        """
        Check if it is possible to apply the pretended operation.
        """

        if is_possible_to_apply_operation:
            """
            It is possible to apply the pretended operation.
            """

            self.qiskit_quantum_circuit.sx(self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_index][qubit_index])
            """
            Apply the Squared Root of the Pauli-X (NOT/Bit Flip) to
            the given qubit of the given IBM Qiskit's Quantum Register. 
            """

    def apply_squared_root_pauli_y(self, qiskit_quantum_register_index: int, qubit_index: int) -> None:
        """
        Apply the Squared Root of the Pauli-Y Gate/Operation to given indexes of
        an IBM Qiskit's Quantum Register and a target qubit.

        :param qiskit_quantum_register_index: the index of an IBM Qiskit's Quantum Register.
        :param qubit_index: the index of a qubit inside that IBM Qiskit's Quantum Register.
        """

        is_possible_to_apply_operation = \
            self.check_if_is_possible_to_apply_operation(qiskit_quantum_register_index, qubit_index, True)
        """
        Check if it is possible to apply the pretended operation.
        """

        if is_possible_to_apply_operation:
            """
            It is possible to apply the pretended operation.
            """

            squared_root_pauli_y_unitary_matrix_operator = Operator([
                [(1 + 1j) * (1 / 2), (1 + 1j) * -(1 / 2)],
                [(1 + 1j) * (1 / 2), (1 + 1j) * (1 / 2)]
            ])
            """
            Set the Unitary Matrix/Operator for the Squared Root of the Pauli-Y Gate/Operation.
            """

            self.qiskit_quantum_circuit.unitary(squared_root_pauli_y_unitary_matrix_operator,
                                                self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_index][qubit_index],
                                                label="sy")
            """
            Apply the Squared Root of the Pauli-Y Gate/Operation to
            the given qubit of the given IBM Qiskit's Quantum Register. 
            """

    def apply_squared_root_pauli_z(self, qiskit_quantum_register_index: int, qubit_index: int) -> None:
        """
        Apply the Squared Root of the Pauli-Z (Phase Flip/Shift) Gate/Operation to given indexes of
        an IBM Qiskit's Quantum Register and a target qubit.

        :param qiskit_quantum_register_index: the index of an IBM Qiskit's Quantum Register.
        :param qubit_index: the index of a qubit inside that IBM Qiskit's Quantum Register.
        """

        is_possible_to_apply_operation = \
            self.check_if_is_possible_to_apply_operation(qiskit_quantum_register_index, qubit_index, True)
        """
        Check if it is possible to apply the pretended operation.
        """

        if is_possible_to_apply_operation:
            """
            It is possible to apply the pretended operation.
            """

            squared_root_pauli_z_unitary_matrix_operator = Operator([
                [1, 0],
                [0, 1j]
            ])
            """
            Set the Unitary Matrix/Operator for the Squared Root of the Pauli-Z (Phase Flip/Shift) Gate/Operation.
            """

            self.qiskit_quantum_circuit.unitary(squared_root_pauli_z_unitary_matrix_operator,
                                                self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_index][qubit_index],
                                                label="sz")
            """
            Apply the Squared Root of the Pauli-Z (Phase Flip/Shift) Gate/Operation to
            the given qubit of the given IBM Qiskit's Quantum Register. 
            """

    def apply_squared_root_hadamard(self, qiskit_quantum_register_index: int, qubit_index: int) -> None:
        """
        Apply the Squared Root of the Hadamard Gate/Operation to given indexes of
        an IBM Qiskit's Quantum Register and a target qubit.

        :param qiskit_quantum_register_index: the index of an IBM Qiskit's Quantum Register.
        :param qubit_index: the index of a qubit inside that IBM Qiskit's Quantum Register.
        """

        is_possible_to_apply_operation = \
            self.check_if_is_possible_to_apply_operation(qiskit_quantum_register_index, qubit_index, True)
        """
        Check if it is possible to apply the pretended operation.
        """

        if is_possible_to_apply_operation:
            """
            It is possible to apply the pretended operation.
            """

            squared_root_hadamard_unitary_matrix_operator = Operator([
                [((2 + sqrt(2)) / 4) + (((2 - sqrt(2)) / 4) * 1j), ((sqrt(2) / 4) - (sqrt(2) / 4) * 1j)],
                [((sqrt(2) / 4) - (sqrt(2) / 4) * 1j), ((2 - sqrt(2)) / 4) + (((2 + sqrt(2)) / 4) * 1j)]
            ])
            """
            Set the Unitary Matrix/Operator for the Squared Root of the Hadamard Gate/Operation.
            """

            self.qiskit_quantum_circuit.unitary(squared_root_hadamard_unitary_matrix_operator,
                                                self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_index][qubit_index],
                                                label="sh")
            """
            Apply the Squared Root of the Hadamard Gate/Operation to
            the given qubit of the given IBM Qiskit's Quantum Register. 
            """

    def apply_squared_root_phase_s(self, qiskit_quantum_register_index: int, qubit_index: int) -> None:
        """
        Apply the Squared Root of the Phase S (sqrt(pi/2)) Gate/Operation to given indexes of
        an IBM Qiskit's Quantum Register and a target qubit.

        :param qiskit_quantum_register_index: the index of an IBM Qiskit's Quantum Register.
        :param qubit_index: the index of a qubit inside that IBM Qiskit's Quantum Register.
        """

        is_possible_to_apply_operation = \
            self.check_if_is_possible_to_apply_operation(qiskit_quantum_register_index, qubit_index, True)
        """
        Check if it is possible to apply the pretended operation.
        """

        if is_possible_to_apply_operation:
            """
            It is possible to apply the pretended operation.
            """

            squared_root_phase_s_unitary_matrix_operator = Operator([
                [1,        0],
                [0, sqrt(1j)]
            ])
            """
            Set the Unitary Matrix/Operator for the Squared Root of the S (sqrt(pi/2)) Gate/Operation.
            """

            self.qiskit_quantum_circuit.unitary(squared_root_phase_s_unitary_matrix_operator,
                                                self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_index][qubit_index],
                                                label="ss")
            """
            Apply the Squared Root of the S (sqrt(pi/2)) Gate/Operation to
            the given qubit of the given IBM Qiskit's Quantum Register. 
            """

    def apply_squared_root_phase_t(self, qiskit_quantum_register_index: int, qubit_index: int) -> None:
        """
        Apply the Squared Root of the Phase T (sqrt(pi/4)) Gate/Operation to given indexes of
        an IBM Qiskit's Quantum Register and a target qubit.

        :param qiskit_quantum_register_index: the index of an IBM Qiskit's Quantum Register.
        :param qubit_index: the index of a qubit inside that IBM Qiskit's Quantum Register.
        """

        is_possible_to_apply_operation = \
            self.check_if_is_possible_to_apply_operation(qiskit_quantum_register_index, qubit_index, True)
        """
        Check if it is possible to apply the pretended operation.
        """

        if is_possible_to_apply_operation:
            """
            It is possible to apply the pretended operation.
            """

            squared_root_phase_t_unitary_matrix_operator = Operator([
                [1,                                   0],
                [0, sqrt(exp((1 / sqrt(2) * (1 + 1j))))]
            ])
            """
            Set the Unitary Matrix/Operator for the Squared Root of the T (sqrt(pi/4)) Gate/Operation.
            """

            self.qiskit_quantum_circuit.unitary(squared_root_phase_t_unitary_matrix_operator,
                                                self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_index][qubit_index],
                                                label="st")
            """
            Apply the Squared Root of the T (sqrt(pi/4)) Gate/Operation to
            the given qubit of the given IBM Qiskit's Quantum Register. 
            """

    def apply_rx_radians(self, theta_radians: float, qiskit_quantum_register_index: int, qubit_index: int) -> None:
        """
        Apply the Rotation-X (R_x(theta_radians)) Gate/Operation to given indexes of
        an IBM Qiskit's Quantum Register and a target qubit, as also, a given theta angle in radians.

        :param theta_radians: the theta angle in radians, for the Rotation-X (R_x(theta_radians)) Gate/Operation.
        :param qiskit_quantum_register_index: the index of an IBM Qiskit's Quantum Register.
        :param qubit_index: the index of a qubit inside that IBM Qiskit's Quantum Register.
        """

        if theta_radians == pi:
            """
            If the theta angle in radians is equal to pi, the Rotation-X (R_x(theta)) Gate/Operation will be
            equivalent to the Pauli-X Gate/Operation, which can be also executed by a Semi-Quantum Register.
            """

            is_possible_to_apply_operation = \
                self.check_if_is_possible_to_apply_operation(qiskit_quantum_register_index,
                                                             qubit_index, False)
            """
            Check if it is possible to apply the pretended operation.
            """

        else:
            """
            If the theta angle in radians is different than pi, the Rotation-X (R_x(theta)) Gate/Operation will not be
            equivalent to the Pauli-X Gate/Operation, and thus, can be only executed by a Fully-Quantum Register.
            """

            is_possible_to_apply_operation = \
                self.check_if_is_possible_to_apply_operation(qiskit_quantum_register_index,
                                                             qubit_index, True)
            """
            Check if it is possible to apply the pretended operation.
            """

        if is_possible_to_apply_operation:
            """
            It is possible to apply the pretended operation.
            """

            self.qiskit_quantum_circuit.rx(theta_radians,
                                           self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_index][qubit_index])
            """
            Apply the Rotation-X (R_x(theta)) Gate/Operation to
            given indexes of an IBM Qiskit's Quantum Register and
            a target qubit, as also, a given theta angle in radians.
            """

    def apply_rx_degrees(self, theta_degrees: float, qiskit_quantum_register_index: int, qubit_index: int) -> None:
        """
        Apply the Rotation-X (R_x(theta_degrees)) Gate/Operation to given indexes of
        an IBM Qiskit's Quantum Register and a target qubit, as also, a given theta angle in degrees.

        :param theta_degrees: the theta angle in degrees, for the Rotation-X (R_x(theta_degrees)) Gate/Operation.
        :param qiskit_quantum_register_index: the index of an IBM Qiskit's Quantum Register.
        :param qubit_index: the index of a qubit inside that IBM Qiskit's Quantum Register.
        """

        theta_radians = radians(theta_degrees)
        """
        Convert the theta angle in degrees to radians.
        """

        self.apply_rx_radians(theta_radians, qiskit_quantum_register_index, qubit_index)
        """
        Apply the equivalent Rotation-X (R_x(theta)) Gate/Operation to the given indexes of
        an IBM Qiskit's Quantum Register and a target qubit, as also, a given theta angle, now in radians.
        """

    def apply_ry_radians(self, theta_radians: float, qiskit_quantum_register_index: int, qubit_index: int) -> None:
        """
        Apply the Rotation-Y (R_y(theta_radians)) Gate/Operation to given indexes of
        an IBM Qiskit's Quantum Register and a target qubit, as also, a given theta angle in radians.

        :param theta_radians: the theta angle in radians, for the Rotation-Y (R_y(theta_radians)) Gate/Operation.
        :param qiskit_quantum_register_index: the index of an IBM Qiskit's Quantum Register.
        :param qubit_index: the index of a qubit inside that IBM Qiskit's Quantum Register.
        """

        is_possible_to_apply_operation = \
            self.check_if_is_possible_to_apply_operation(qiskit_quantum_register_index,
                                                         qubit_index, True)
        """
        Check if it is possible to apply the pretended operation.
        """

        if is_possible_to_apply_operation:
            """
            It is possible to apply the pretended operation.
            """

            self.qiskit_quantum_circuit.ry(theta_radians,
                                           self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_index][qubit_index])
            """
            Apply the Rotation-Y (R_y(theta)) Gate/Operation to
            given indexes of an IBM Qiskit's Quantum Register and
            a target qubit, as also, a given theta angle in radians.
            """

    def apply_ry_degrees(self, theta_degrees: float, qiskit_quantum_register_index: int, qubit_index: int) -> None:
        """
        Apply the Rotation-Y (R_y(theta_degrees)) Gate/Operation to given indexes of
        an IBM Qiskit's Quantum Register and a target qubit, as also, a given theta angle in degrees.

        :param theta_degrees: the theta angle in degrees, for the Rotation-Y (R_y(theta_degrees)) Gate/Operation.
        :param qiskit_quantum_register_index: the index of an IBM Qiskit's Quantum Register.
        :param qubit_index: the index of a qubit inside that IBM Qiskit's Quantum Register.
        """

        theta_radians = radians(theta_degrees)
        """
        Convert the theta angle in degrees to radians.
        """

        self.apply_ry_radians(theta_radians, qiskit_quantum_register_index, qubit_index)
        """
        Apply the equivalent Rotation-Y (R_y(theta)) Gate/Operation to the given indexes of
        an IBM Qiskit's Quantum Register and a target qubit, as also, a given theta angle, now in radians.
        """

    def apply_rz_radians(self, theta_radians: float, qiskit_quantum_register_index: int, qubit_index: int) -> None:
        """
        Apply the Rotation-Z (R_z(theta_radians)) Gate/Operation to given indexes of
        an IBM Qiskit's Quantum Register and a target qubit, as also, a given theta angle in radians.

        :param theta_radians: the theta angle in radians, for the Rotation-Z (R_z(theta_radians)) Gate/Operation.
        :param qiskit_quantum_register_index: the index of an IBM Qiskit's Quantum Register.
        :param qubit_index: the index of a qubit inside that IBM Qiskit's Quantum Register.
        """

        is_possible_to_apply_operation = \
            self.check_if_is_possible_to_apply_operation(qiskit_quantum_register_index,
                                                         qubit_index, True)
        """
        Check if it is possible to apply the pretended operation.
        """

        if is_possible_to_apply_operation:
            """
            It is possible to apply the pretended operation.
            """

            self.qiskit_quantum_circuit.rz(theta_radians,
                                           self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_index][qubit_index])
            """
            Apply the Rotation-Z (R_z(theta)) Gate/Operation to
            given indexes of an IBM Qiskit's Quantum Register and
            a target qubit, as also, a given theta angle in radians.
            """

    def apply_rz_degrees(self, theta_degrees: float, qiskit_quantum_register_index: int, qubit_index: int) -> None:
        """
        Apply the Rotation-Z (R_z(theta_degrees)) Gate/Operation to given indexes of
        an IBM Qiskit's Quantum Register and a target qubit, as also, a given theta angle in degrees.

        :param theta_degrees: the theta angle in degrees, for the Rotation-Z (R_z(theta_degrees)) Gate/Operation.
        :param qiskit_quantum_register_index: index of an IBM Qiskit's Quantum Register.
        :param qubit_index: index of a qubit inside that IBM Qiskit's Quantum Register.
        """

        theta_radians = radians(theta_degrees)
        """
        Convert the theta angle in degrees to radians.
        """

        self.apply_rz_radians(theta_radians, qiskit_quantum_register_index, qubit_index)
        """
        Apply the equivalent Rotation-Z (R_z(theta)) Gate/Operation to the given indexes of
        an IBM Qiskit's Quantum Register and a target qubit, as also, a given theta angle, now in radians.
        """

    def apply_u1_radians(self, theta_radians: float, qiskit_quantum_register_index: int, qubit_index: int) -> None:
        """
        Apply the U1(theta_radians) Gate/Operation to given indexes of
        an IBM Qiskit's Quantum Register and a target qubit, as also, a given theta angle in radians.

        :param theta_radians: the theta angle in radians, for the U1(theta_radians) Gate/Operation.
        :param qiskit_quantum_register_index: the index of an IBM Qiskit's Quantum Register.
        :param qubit_index: the index of a qubit inside that IBM Qiskit's Quantum Register.
        """

        is_possible_to_apply_operation = \
            self.check_if_is_possible_to_apply_operation(qiskit_quantum_register_index,
                                                         qubit_index, True)
        """
        Check if it is possible to apply the pretended operation.
        """

        if is_possible_to_apply_operation:
            """
            It is possible to apply the pretended operation.
            """

            self.qiskit_quantum_circuit.u1(theta_radians,
                                           self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_index][qubit_index])
            """
            Apply the U1(theta) Gate/Operation to
            given indexes of an IBM Qiskit's Quantum Register and
            a target qubit, as also, a given theta angle in radians.
            """

    def apply_u1_degrees(self, theta_degrees: float, qiskit_quantum_register_index: int, qubit_index: int) -> None:
        """
        Apply the U1(theta_degrees) Gate/Operation to given indexes of
        an IBM Qiskit's Quantum Register and a target qubit, as also, a given theta angle in degrees.

        :param theta_degrees: the theta angle in degrees, for the U1(theta_degrees) Gate/Operation.
        :param qiskit_quantum_register_index: the index of an IBM Qiskit's Quantum Register.
        :param qubit_index: the index of a qubit inside that IBM Qiskit's Quantum Register.
        """

        theta_radians = radians(theta_degrees)
        """
        Convert the theta angle in degrees to radians.
        """

        self.apply_u1_radians(theta_radians, qiskit_quantum_register_index, qubit_index)
        """
        Apply the equivalent U1(theta_radians) Gate/Operation to the given indexes of
        an IBM Qiskit's Quantum Register and a target qubit, as also, a given theta angle, now in radians.
        """

    def apply_u2_radians(self, phi_radians: float, lamb_radians: float,
                         qiskit_quantum_register_index: int, qubit_index: int) -> None:
        """
        Apply the U2(phi_radians, lamb_radians) Gate/Operation to given indexes of
        an IBM Qiskit's Quantum Register and a target qubit, as also, given phi and lambda angles in radians.

        :param phi_radians: the phi angle in radians, for the U2(phi_radians, lamb_radians) Gate/Operation.
        :param lamb_radians: the lambda angle in radians, for the U2(phi_radians, lamb_radians) Gate/Operation.
        :param qiskit_quantum_register_index: the index of an IBM Qiskit's Quantum Register.
        :param qubit_index: the index of a qubit inside that IBM Qiskit's Quantum Register.
        """

        is_possible_to_apply_operation = \
            self.check_if_is_possible_to_apply_operation(qiskit_quantum_register_index,
                                                         qubit_index, True)
        """
        Check if it is possible to apply the pretended operation.
        """

        if is_possible_to_apply_operation:
            """
            It is possible to apply the pretended operation.
            """

            self.qiskit_quantum_circuit.u2(phi_radians, lamb_radians,
                                           self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_index][qubit_index])
            """
            Apply the U2(phi_radians, lamb_radians) Gate/Operation to
            given indexes of an IBM Qiskit's Quantum Register and
            a target qubit, as also, given phi and lambda angles in radians.
            """

    def apply_u2_degrees(self, phi_degrees: float, lamb_degrees: float,
                         qiskit_quantum_register_index: int, qubit_index: int) -> None:
        """
        Apply the U2(phi_degrees, lamb_degrees) Gate/Operation to given indexes of
        an IBM Qiskit's Quantum Register and a target qubit, as also, given phi and lambda angles in degrees.

        :param phi_degrees: the phi angle in degrees, for the U2(phi_degrees, lamb_degrees) Gate/Operation.
        :param lamb_degrees: the lambda angle in degrees, for the U2(phi_degrees, lamb_degrees) Gate/Operation.
        :param qiskit_quantum_register_index: the index of an IBM Qiskit's Quantum Register.
        :param qubit_index: the index of a qubit inside that IBM Qiskit's Quantum Register.
        """

        phi_radians = radians(phi_degrees)
        """
        Convert the phi angle in degrees to radians.
        """

        lamb_radians = radians(lamb_degrees)
        """
        Convert the lambda angle in degrees to radians.
        """

        self.apply_u2_radians(phi_radians, lamb_radians, qiskit_quantum_register_index, qubit_index)
        """
        Apply the equivalent U2(phi_radians, lamb_radians) Gate/Operation to the given indexes of
        an IBM Qiskit's Quantum Register and a target qubit, as also, given phi and lambda angles, now in radians.
        """

    def apply_u3_radians(self, theta_radians: float, phi_radians: float, lamb_radians: float,
                         qiskit_quantum_register_index: int, qubit_index: int) -> None:
        """
        Apply the U3(theta_radians, phi_radians, lamb_radians) Gate/Operation to given indexes of
        an IBM Qiskit's Quantum Register and a target qubit, as also, given theta, phi and lambda angles in radians.

        :param theta_radians: the theta angle in radians, for the U3(theta_radians, phi_radians, lamb_radians) Gate/Operation.
        :param phi_radians: the phi angle in radians, for the U3(theta_radians, phi_radians, lamb_radians) Gate/Operation.
        :param lamb_radians: the lambda angle in radians, for the U3(theta_radians, phi_radians, lamb_radians) Gate/Operation.
        :param qiskit_quantum_register_index: the index of an IBM Qiskit's Quantum Register.
        :param qubit_index: the index of a qubit inside that IBM Qiskit's Quantum Register.
        """

        is_possible_to_apply_operation = \
            self.check_if_is_possible_to_apply_operation(qiskit_quantum_register_index,
                                                         qubit_index, True)
        """
        Check if it is possible to apply the pretended operation.
        """

        if is_possible_to_apply_operation:
            """
            It is possible to apply the pretended operation.
            """

            self.qiskit_quantum_circuit.u3(theta_radians, phi_radians, lamb_radians,
                                           self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_index][qubit_index])
            """
            Apply the U3(theta_radians, phi_radians, lamb_radians) Gate/Operation to
            given indexes of an IBM Qiskit's Quantum Register and
            a target qubit, as also, given phi and lambda angles in radians.
            """

    def apply_u3_degrees(self, theta_degrees: float, phi_degrees: float, lamb_degrees: float,
                         qiskit_quantum_register_index: int, qubit_index: int) -> None:
        """
        Apply the U3(theta_degrees, phi_degrees, lamb_degrees) Gate/Operation to given indexes of
        an IBM Qiskit's Quantum Register and a target qubit, as also, given theta, phi and lambda angles in degrees.

        :param theta_degrees: the theta angle in degrees, for the U3(theta_degrees, phi_degrees, lamb_degrees) Gate/Operation.
        :param phi_degrees: the phi angle in degrees, for the U3(theta_degrees, phi_degrees, lamb_degrees) Gate/Operation.
        :param lamb_degrees: the theta angle in degrees, for the U3(theta_degrees, phi_degrees, lamb_degrees) Gate/Operation.
        :param qiskit_quantum_register_index: the index of an IBM Qiskit's Quantum Register.
        :param qubit_index: the index of a qubit inside that IBM Qiskit's Quantum Register.
        """

        theta_radians = radians(theta_degrees)
        """
        Convert the theta angle in degrees to radians.
        """

        phi_radians = radians(phi_degrees)
        """
        Convert the phi angle in degrees to radians.
        """

        lamb_radians = radians(lamb_degrees)
        """
        Convert the lambda angle in degrees to radians.
        """

        self.apply_u3_radians(theta_radians, phi_radians, lamb_radians, qiskit_quantum_register_index, qubit_index)
        """
        Apply the equivalent U3(theta_degrees, phi_degrees, lamb_degrees) Gate/Operation to the given indexes of
        an IBM Qiskit's Quantum Register and a target qubit, as also, given theta, phi and lambda angles, now in radians.
        """

    """
    4) Multi Qubit Gates/Operations Methods:
    """

    def apply_swap(self, qiskit_quantum_register_index_1: int, qiskit_quantum_register_index_2: int,
                   qubit_index_1: int, qubit_index_2: int) -> None:
        """
        Apply the SWAP Gate/Operation to given indexes of
        a 1st IBM Qiskit's Quantum Register and a target qubit on it, as also,
        another 2nd IBM Qiskit's Quantum Register and a target qubit on it.

        :param qiskit_quantum_register_index_1: the index of the 1st IBM Qiskit's Quantum Register.
        :param qiskit_quantum_register_index_2: the index of the 2nd IBM Qiskit's Quantum Register.
        :param qubit_index_1: the index of a qubit inside the 1st IBM Qiskit's Quantum Register.
        :param qubit_index_2: the index of a qubit inside the 2nd IBM Qiskit's Quantum Register.
        """

        is_possible_to_apply_operation_1 = \
            self.check_if_is_possible_to_apply_operation(qiskit_quantum_register_index_1,
                                                         qubit_index_1, False)
        """
        Check if it is possible to apply the pretended operation for
        the 1st IBM Qiskit's Quantum Register and the respective target qubit.
        """

        is_possible_to_apply_operation_2 = \
            self.check_if_is_possible_to_apply_operation(qiskit_quantum_register_index_2,
                                                         qubit_index_2, False)
        """
        Check if it is possible to apply the pretended operation for
        the 2nd IBM Qiskit's Quantum Register and the respective target qubit.
        """

        if is_possible_to_apply_operation_1 and is_possible_to_apply_operation_2:
            """
            It is possible to apply the pretended operation for both
            the IBM Qiskit's Quantum Registers and their respective target qubits.
            """

            self.qiskit_quantum_circuit.swap(self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_index_1][qubit_index_1],
                                             self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_index_2][qubit_index_2])
            """
            Apply the SWAP Gate/Operation to the two given indexes of
            IBM Qiskit's Quantum Registers and their respective target qubits.
            """

    def apply_i_swap(self, qiskit_quantum_register_index_1: int, qiskit_quantum_register_index_2: int,
                     qubit_index_1: int, qubit_index_2: int) -> None:
        """
        Apply the iSWAP Gate/Operation to given indexes of
        a 1st IBM Qiskit's Quantum Register and a target qubit on it, as also,
        another 2nd IBM Qiskit's Quantum Register and a target qubit on it.

        :param qiskit_quantum_register_index_1: the index of the 1st IBM Qiskit's Quantum Register.
        :param qiskit_quantum_register_index_2: the index of the 2nd IBM Qiskit's Quantum Register.
        :param qubit_index_1: the index of a qubit inside the 1st IBM Qiskit's Quantum Register.
        :param qubit_index_2: the index of a qubit inside the 2nd IBM Qiskit's Quantum Register.
        """

        is_possible_to_apply_operation_1 = \
            self.check_if_is_possible_to_apply_operation(qiskit_quantum_register_index_1,
                                                         qubit_index_1, True)
        """
        Check if it is possible to apply the pretended operation for
        the 1st IBM Qiskit's Quantum Register and the respective target qubit.
        """

        is_possible_to_apply_operation_2 = \
            self.check_if_is_possible_to_apply_operation(qiskit_quantum_register_index_2,
                                                         qubit_index_2, True)
        """
        Check if it is possible to apply the pretended operation for
        the 2nd IBM Qiskit's Quantum Register and the respective target qubit.
        """

        if is_possible_to_apply_operation_1 and is_possible_to_apply_operation_2:
            """
            It is possible to apply the pretended operation for both
            the IBM Qiskit's Quantum Registers and their respective target qubits.
            """

            self.qiskit_quantum_circuit.iswap(self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_index_1][qubit_index_1],
                                              self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_index_2][qubit_index_2])
            """
            Apply the iSWAP Gate/Operation to the two given indexes of
            IBM Qiskit's Quantum Registers and their respective target qubits.
            """

    def apply_controlled_pauli_x(self,
                                 qiskit_quantum_register_control_index: int,
                                 qiskit_quantum_register_target_index: int,
                                 control_qubit_index: int, target_qubit_index: int) -> None:
        """
        Apply the Controlled-Pauli-X (Controlled-NOT) Gate/Operation to given indexes of
        a control IBM Qiskit's Quantum Register and the respective qubit on it, as also,
        a target IBM Qiskit's Quantum Register and the respective qubit on it.

        :param qiskit_quantum_register_control_index: the index of the control IBM Qiskit's Quantum Register.
        :param qiskit_quantum_register_target_index: the index of the target IBM Qiskit's Quantum Register.
        :param control_qubit_index: the index of a qubit inside the control IBM Qiskit's Quantum Register.
        :param target_qubit_index: the index of a qubit inside the target IBM Qiskit's Quantum Register.
        """

        is_possible_to_apply_operation_control = \
            self.check_if_is_possible_to_apply_operation(qiskit_quantum_register_control_index,
                                                         control_qubit_index, True)
        """
        Check if it is possible to apply the pretended operation for
        the control IBM Qiskit's Quantum Register and the respective control qubit.
        """

        is_possible_to_apply_operation_target = \
            self.check_if_is_possible_to_apply_operation(qiskit_quantum_register_target_index,
                                                         target_qubit_index, True)
        """
        Check if it is possible to apply the pretended operation for
        the target IBM Qiskit's Quantum Register and the respective target qubit.
        """

        if is_possible_to_apply_operation_control and is_possible_to_apply_operation_target:
            """
            It is possible to apply the pretended operation for both
            the control and target IBM Qiskit's Quantum Registers and their respective qubits.
            """

            self.qiskit_quantum_circuit.cx(self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_control_index][control_qubit_index],
                                           self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_target_index][target_qubit_index])
            """
            Apply the Controlled-Pauli-X (Controlled-NOT) Gate/Operation to the given indexes of
            control and target IBM Qiskit's Quantum Registers and their respective qubits.
            """

    def apply_controlled_pauli_y(self,
                                 qiskit_quantum_register_control_index: int,
                                 qiskit_quantum_register_target_index: int,
                                 control_qubit_index: int, target_qubit_index: int) -> None:
        """
        Apply the Controlled-Pauli-Y Gate/Operation to given indexes of
        a control IBM Qiskit's Quantum Register and the respective qubit on it, as also,
        a target IBM Qiskit's Quantum Register and the respective qubit on it.

        :param qiskit_quantum_register_control_index: the index of the control IBM Qiskit's Quantum Register.
        :param qiskit_quantum_register_target_index: the index of the target IBM Qiskit's Quantum Register.
        :param control_qubit_index: the index of a qubit inside the control IBM Qiskit's Quantum Register.
        :param target_qubit_index: the index of a qubit inside the target IBM Qiskit's Quantum Register.
        """

        is_possible_to_apply_operation_control = \
            self.check_if_is_possible_to_apply_operation(qiskit_quantum_register_control_index,
                                                         control_qubit_index, True)
        """
        Check if it is possible to apply the pretended operation for
        the control IBM Qiskit's Quantum Register and the respective control qubit.
        """

        is_possible_to_apply_operation_target = \
            self.check_if_is_possible_to_apply_operation(qiskit_quantum_register_target_index,
                                                         target_qubit_index, True)
        """
        Check if it is possible to apply the pretended operation for
        the target IBM Qiskit's Quantum Register and the respective target qubit.
        """

        if is_possible_to_apply_operation_control and is_possible_to_apply_operation_target:
            """
            It is possible to apply the pretended operation for both
            the control and target IBM Qiskit's Quantum Registers and their respective qubits.
            """

            self.qiskit_quantum_circuit.cy(self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_control_index][control_qubit_index],
                                           self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_target_index][target_qubit_index])
            """
            Apply the Controlled-Pauli-Y Gate/Operation to the given indexes of
            control and target IBM Qiskit's Quantum Registers and their respective qubits.
            """

    def apply_controlled_pauli_z(self,
                                 qiskit_quantum_register_control_index: int,
                                 qiskit_quantum_register_target_index: int,
                                 control_qubit_index: int, target_qubit_index: int) -> None:
        """
        Apply the Controlled-Pauli-Z (Controlled-Phase-Flip/Controlled-Phase-Shifter) Gate/Operation to
        given indexes of a control IBM Qiskit's Quantum Register and the respective qubit on it, as also,
        a target IBM Qiskit's Quantum Register and the respective qubit on it.

        :param qiskit_quantum_register_control_index: the index of the control IBM Qiskit's Quantum Register.
        :param qiskit_quantum_register_target_index: the index of the target IBM Qiskit's Quantum Register.
        :param control_qubit_index: the index of a qubit inside the control IBM Qiskit's Quantum Register.
        :param target_qubit_index: the index of a qubit inside the target IBM Qiskit's Quantum Register.
        """

        is_possible_to_apply_operation_control = \
            self.check_if_is_possible_to_apply_operation(qiskit_quantum_register_control_index,
                                                         control_qubit_index, True)
        """
        Check if it is possible to apply the pretended operation for
        the control IBM Qiskit's Quantum Register and the respective control qubit.
        """

        is_possible_to_apply_operation_target = \
            self.check_if_is_possible_to_apply_operation(qiskit_quantum_register_target_index,
                                                         target_qubit_index, True)
        """
        Check if it is possible to apply the pretended operation for
        the target IBM Qiskit's Quantum Register and the respective target qubit.
        """

        if is_possible_to_apply_operation_control and is_possible_to_apply_operation_target:
            """
            It is possible to apply the pretended operation for both
            the control and target IBM Qiskit's Quantum Registers and their respective qubits.
            """

            self.qiskit_quantum_circuit.cz(self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_control_index][control_qubit_index],
                                           self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_target_index][target_qubit_index])
            """
            Apply the Controlled-Pauli-Z (Controlled-Phase-Flip/Controlled-Phase-Shifter) Gate/Operation to
            the given indexes of control and target IBM Qiskit's Quantum Registers and their respective qubits.
            """

    def apply_controlled_hadamard(self,
                                  qiskit_quantum_register_control_index: int,
                                  qiskit_quantum_register_target_index: int,
                                  control_qubit_index: int, target_qubit_index: int) -> None:

        """
        Apply the Controlled-Hadamard Gate/Operation to
        given indexes of a control IBM Qiskit's Quantum Register and the respective qubit on it, as also,
        a target IBM Qiskit's Quantum Register and the respective qubit on it.

        :param qiskit_quantum_register_control_index: the index of the control IBM Qiskit's Quantum Register.
        :param qiskit_quantum_register_target_index: the index of the target IBM Qiskit's Quantum Register.
        :param control_qubit_index: the index of a qubit inside the control IBM Qiskit's Quantum Register.
        :param target_qubit_index: the index of a qubit inside the target IBM Qiskit's Quantum Register.
        """

        is_possible_to_apply_operation_control = \
            self.check_if_is_possible_to_apply_operation(qiskit_quantum_register_control_index,
                                                         control_qubit_index, True)
        """
        Check if it is possible to apply the pretended operation for
        the control IBM Qiskit's Quantum Register and the respective control qubit.
        """

        is_possible_to_apply_operation_target = \
            self.check_if_is_possible_to_apply_operation(qiskit_quantum_register_target_index,
                                                         target_qubit_index, True)
        """
        Check if it is possible to apply the pretended operation for
        the target IBM Qiskit's Quantum Register and the respective target qubit.
        """

        if is_possible_to_apply_operation_control and is_possible_to_apply_operation_target:
            """
            It is possible to apply the pretended operation for both
            the control and target IBM Qiskit's Quantum Registers and their respective qubits.
            """

            self.qiskit_quantum_circuit.ch(self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_control_index][control_qubit_index],
                                           self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_target_index][target_qubit_index])
            """
            Apply the Controlled-Hadamard Gate/Operation to
            the given indexes of control and target IBM Qiskit's Quantum Registers and their respective qubits.
            """

    def apply_controlled_phase_s(self,
                                 qiskit_quantum_register_control_index: int,
                                 qiskit_quantum_register_target_index: int,
                                 control_qubit_index: int, target_qubit_index: int) -> None:

        """
        Apply the Controlled-Phase-S (pi/2) Gate/Operation to
        given indexes of a control IBM Qiskit's Quantum Register and the respective qubit on it, as also,
        a target IBM Qiskit's Quantum Register and the respective qubit on it.

        :param qiskit_quantum_register_control_index: the index of the control IBM Qiskit's Quantum Register.
        :param qiskit_quantum_register_target_index: the index of the target IBM Qiskit's Quantum Register.
        :param control_qubit_index: the index of a qubit inside the control IBM Qiskit's Quantum Register.
        :param target_qubit_index: the index of a qubit inside the target IBM Qiskit's Quantum Register.
        """

        is_possible_to_apply_operation_control = \
            self.check_if_is_possible_to_apply_operation(qiskit_quantum_register_control_index,
                                                         control_qubit_index, True)
        """
        Check if it is possible to apply the pretended operation for
        the control IBM Qiskit's Quantum Register and the respective control qubit.
        """

        is_possible_to_apply_operation_target = \
            self.check_if_is_possible_to_apply_operation(qiskit_quantum_register_target_index,
                                                         target_qubit_index, True)
        """
        Check if it is possible to apply the pretended operation for
        the target IBM Qiskit's Quantum Register and the respective target qubit.
        """

        if is_possible_to_apply_operation_control and is_possible_to_apply_operation_target:
            """
            It is possible to apply the pretended operation for both
            the control and target IBM Qiskit's Quantum Registers and their respective qubits.
            """

            controlled_phase_s_unitary_matrix_operator = Operator([
                [1, 0, 0,  0],
                [0, 1, 0,  0],
                [0, 0, 1,  0],
                [0, 0, 0, 1j]
            ])
            """
            Set the Unitary Matrix/Operator for the Controlled-Phase-S (pi/2) Gate/Operation.
            """

            self.qiskit_quantum_circuit.unitary(controlled_phase_s_unitary_matrix_operator,
                                                [self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_control_index][control_qubit_index],
                                                 self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_target_index][target_qubit_index]],
                                                label="cs")
            """
            Apply the Controlled-Phase-S (pi/2) Gate/Operation to
            the given indexes of control and target IBM Qiskit's Quantum Registers and their respective qubits.
            """

    def apply_controlled_phase_t(self,
                                 qiskit_quantum_register_control_index: int,
                                 qiskit_quantum_register_target_index: int,
                                 control_qubit_index: int, target_qubit_index: int) -> None:

        """
        Apply the Controlled-Phase-T (pi/4) Gate/Operation to
        given indexes of a control IBM Qiskit's Quantum Register and the respective qubit on it, as also,
        a target IBM Qiskit's Quantum Register and the respective qubit on it.

        :param qiskit_quantum_register_control_index: the index of the control IBM Qiskit's Quantum Register.
        :param qiskit_quantum_register_target_index: the index of the target IBM Qiskit's Quantum Register.
        :param control_qubit_index: the index of a qubit inside the control IBM Qiskit's Quantum Register.
        :param target_qubit_index: the index of a qubit inside the target IBM Qiskit's Quantum Register.
        """

        is_possible_to_apply_operation_control = \
            self.check_if_is_possible_to_apply_operation(qiskit_quantum_register_control_index,
                                                         control_qubit_index, True)
        """
        Check if it is possible to apply the pretended operation for
        the control IBM Qiskit's Quantum Register and the respective control qubit.
        """

        is_possible_to_apply_operation_target = \
            self.check_if_is_possible_to_apply_operation(qiskit_quantum_register_target_index,
                                                         target_qubit_index, True)
        """
        Check if it is possible to apply the pretended operation for
        the target IBM Qiskit's Quantum Register and the respective target qubit.
        """

        if is_possible_to_apply_operation_control and is_possible_to_apply_operation_target:
            """
            It is possible to apply the pretended operation for both
            the control and target IBM Qiskit's Quantum Registers and their respective qubits.
            """

            controlled_phase_t_unitary_matrix_operator = Operator([
                [1, 0, 0,                             0],
                [0, 1, 0,                             0],
                [0, 0, 1,                             0],
                [0, 0, 0, exp((1 / sqrt(2) * (1 + 1j)))]
            ])
            """
            Set the Unitary Matrix/Operator for the Controlled-Phase-T (pi/4) Gate/Operation.
            """

            self.qiskit_quantum_circuit.unitary(controlled_phase_t_unitary_matrix_operator,
                                                [self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_control_index][control_qubit_index],
                                                 self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_target_index][target_qubit_index]],
                                                label="ct")
            """
            Apply the Controlled-Phase-T (pi/4) Gate/Operation to
            the given indexes of control and target IBM Qiskit's Quantum Registers and their respective qubits.
            """

    def apply_controlled_phase_s_adjoint(self,
                                         qiskit_quantum_register_control_index: int,
                                         qiskit_quantum_register_target_index: int,
                                         control_qubit_index: int, target_qubit_index: int) -> None:

        """
        Apply the Controlled-Phase-S (-pi/2) Adjoint Gate/Operation to
        given indexes of a control IBM Qiskit's Quantum Register and the respective qubit on it, as also,
        a target IBM Qiskit's Quantum Register and the respective qubit on it.

        :param qiskit_quantum_register_control_index: the index of the control IBM Qiskit's Quantum Register.
        :param qiskit_quantum_register_target_index: the index of the target IBM Qiskit's Quantum Register.
        :param control_qubit_index: the index of a qubit inside the control IBM Qiskit's Quantum Register.
        :param target_qubit_index: the index of a qubit inside the target IBM Qiskit's Quantum Register.
        """

        is_possible_to_apply_operation_control = \
            self.check_if_is_possible_to_apply_operation(qiskit_quantum_register_control_index,
                                                         control_qubit_index, True)
        """
        Check if it is possible to apply the pretended operation for
        the control IBM Qiskit's Quantum Register and the respective control qubit.
        """

        is_possible_to_apply_operation_target = \
            self.check_if_is_possible_to_apply_operation(qiskit_quantum_register_target_index,
                                                         target_qubit_index, True)
        """
        Check if it is possible to apply the pretended operation for
        the target IBM Qiskit's Quantum Register and the respective target qubit.
        """

        if is_possible_to_apply_operation_control and is_possible_to_apply_operation_target:
            """
            It is possible to apply the pretended operation for both
            the control and target IBM Qiskit's Quantum Registers and their respective qubits.
            """

            controlled_phase_s_adjoint_unitary_matrix_operator = Operator([
                [1, 0, 0,   0],
                [0, 1, 0,   0],
                [0, 0, 1,   0],
                [0, 0, 0, -1j]
            ])
            """
            Set the Unitary Matrix/Operator for the Controlled-Phase-S (-pi/2) Adjoint Gate/Operation.
            """

            self.qiskit_quantum_circuit.unitary(controlled_phase_s_adjoint_unitary_matrix_operator,
                                                [self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_control_index][control_qubit_index],
                                                 self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_target_index][target_qubit_index]],
                                                label="csdg")
            """
            Apply the Controlled-Phase-S (-pi/2) Adjoint Gate/Operation to
            the given indexes of control and target IBM Qiskit's Quantum Registers and their respective qubits.
            """

    def apply_controlled_phase_t_adjoint(self,
                                         qiskit_quantum_register_control_index: int,
                                         qiskit_quantum_register_target_index: int,
                                         control_qubit_index: int, target_qubit_index: int) -> None:

        """
        Apply the Controlled-Phase-T (-pi/4) Adjoint Gate/Operation to
        given indexes of a control IBM Qiskit's Quantum Register and the respective qubit on it, as also,
        a target IBM Qiskit's Quantum Register and the respective qubit on it.

        :param qiskit_quantum_register_control_index: the index of the control IBM Qiskit's Quantum Register.
        :param qiskit_quantum_register_target_index: the index of the target IBM Qiskit's Quantum Register.
        :param control_qubit_index: the index of a qubit inside the control IBM Qiskit's Quantum Register.
        :param target_qubit_index: the index of a qubit inside the target IBM Qiskit's Quantum Register.
        """

        is_possible_to_apply_operation_control = \
            self.check_if_is_possible_to_apply_operation(qiskit_quantum_register_control_index,
                                                         control_qubit_index, True)
        """
        Check if it is possible to apply the pretended operation for
        the control IBM Qiskit's Quantum Register and the respective control qubit.
        """

        is_possible_to_apply_operation_target = \
            self.check_if_is_possible_to_apply_operation(qiskit_quantum_register_target_index,
                                                         target_qubit_index, True)
        """
        Check if it is possible to apply the pretended operation for
        the target IBM Qiskit's Quantum Register and the respective target qubit.
        """

        if is_possible_to_apply_operation_control and is_possible_to_apply_operation_target:
            """
            It is possible to apply the pretended operation for both
            the control and target IBM Qiskit's Quantum Registers and their respective qubits.
            """

            controlled_phase_t_adjoint_unitary_matrix_operator = Operator([
                [1, 0, 0,                             0],
                [0, 1, 0,                             0],
                [0, 0, 1,                             0],
                [0, 0, 0, exp((1 / sqrt(2) * (1 - 1j)))]
            ])
            """
            Set the Unitary Matrix/Operator for the Controlled-Phase-T (-pi/4) Adjoint Gate/Operation.
            """

            self.qiskit_quantum_circuit.unitary(controlled_phase_t_adjoint_unitary_matrix_operator,
                                                [self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_control_index][control_qubit_index],
                                                 self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_target_index][target_qubit_index]],
                                                label="ctdg")
            """
            Apply the Controlled-Phase-T (-pi/4) Adjoint Gate/Operation to
            the given indexes of control and target IBM Qiskit's Quantum Registers and their respective qubits.
            """

    def apply_controlled_swap(self,
                              qiskit_quantum_register_control_index: int,
                              qiskit_quantum_register_target_index_1: int,
                              qiskit_quantum_register_target_index_2: int,
                              control_qubit_index: int, target_qubit_index_1: int, target_qubit_index_2: int) -> None:
        """
        Apply the Controlled-SWAP (Fredkin) Gate/Operation to
        given indexes of a control IBM Qiskit's Quantum Register and the respective qubit on it, as also,
        two target IBM Qiskit's Quantum Registers and the respective qubits on them.

        :param qiskit_quantum_register_control_index: the index of the control IBM Qiskit's Quantum Register.
        :param qiskit_quantum_register_target_index_1: the index of the 1st target IBM Qiskit's Quantum Register.
        :param qiskit_quantum_register_target_index_2: the index of the 2nd target IBM Qiskit's Quantum Register.
        :param control_qubit_index: the index of a qubit inside the control IBM Qiskit's Quantum Register.
        :param target_qubit_index_1: the index of a qubit inside the 1st target IBM Qiskit's Quantum Register.
        :param target_qubit_index_2: the index of a qubit inside the 2nd target IBM Qiskit's Quantum Register.
        """

        is_possible_to_apply_operation_control = \
            self.check_if_is_possible_to_apply_operation(qiskit_quantum_register_control_index,
                                                         control_qubit_index, True)
        """
        Check if it is possible to apply the pretended operation for
        the control IBM Qiskit's Quantum Register and the respective control qubit.
        """

        is_possible_to_apply_operation_target_1 = \
            self.check_if_is_possible_to_apply_operation(qiskit_quantum_register_target_index_1,
                                                         target_qubit_index_1, True)
        """
        Check if it is possible to apply the pretended operation for
        the 1st target IBM Qiskit's Quantum Register and the respective target qubit.
        """

        is_possible_to_apply_operation_target_2 = \
            self.check_if_is_possible_to_apply_operation(qiskit_quantum_register_target_index_2,
                                                         target_qubit_index_2, True)
        """
        Check if it is possible to apply the pretended operation for
        the 2nd target IBM Qiskit's Quantum Register and the respective target qubit.
        """

        if is_possible_to_apply_operation_control and \
                is_possible_to_apply_operation_target_1 and is_possible_to_apply_operation_target_2:
            """
            It is possible to apply the pretended operation for both
            the control and targets IBM Qiskit's Quantum Registers and their respective qubits.
            """

            self.qiskit_quantum_circuit.cswap(self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_control_index][control_qubit_index],
                                              self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_target_index_1][target_qubit_index_1],
                                              self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_target_index_2][target_qubit_index_2])
            """
            Apply the Controlled-SWAP (Fredkin) Gate/Operation to the given indexes of
            control and targets IBM Qiskit's Quantum Registers and their respective qubits.
            """

    def apply_fredkin(self,
                      qiskit_quantum_register_control_index: int,
                      qiskit_quantum_register_target_index_1: int,
                      qiskit_quantum_register_target_index_2: int,
                      control_qubit_index: int, target_qubit_index_1: int, target_qubit_index_2: int) -> None:
        """
        Apply the Controlled-SWAP (Fredkin) Gate/Operation to
        given indexes of a control IBM Qiskit's Quantum Register and the respective qubit on it, as also,
        two target IBM Qiskit's Quantum Registers and the respective qubits on them.

        :param qiskit_quantum_register_control_index: the index of the control IBM Qiskit's Quantum Register.
        :param qiskit_quantum_register_target_index_1: the index of the 1st target IBM Qiskit's Quantum Register.
        :param qiskit_quantum_register_target_index_2: the index of the 2nd target IBM Qiskit's Quantum Register.
        :param control_qubit_index: the index of a qubit inside the control IBM Qiskit's Quantum Register.
        :param target_qubit_index_1: the index of a qubit inside the 1st target IBM Qiskit's Quantum Register.
        :param target_qubit_index_2: the index of a qubit inside the 2nd target IBM Qiskit's Quantum Register.
        """

        self.apply_controlled_swap(qiskit_quantum_register_control_index,
                                   qiskit_quantum_register_target_index_1, qiskit_quantum_register_target_index_2,
                                   control_qubit_index, target_qubit_index_1, target_qubit_index_2)
        """
        Apply the equivalent Controlled-SWAP (Fredkin) Gate/Operation to the given indexes of
        control and targets IBM Qiskit's Quantum Registers and their respective qubits.
        """

    def apply_double_controlled_pauli_x(self,
                                        qiskit_quantum_register_index_1: int,
                                        qiskit_quantum_register_index_2: int,
                                        qubit_index_1: int, qubit_index_2: int) -> None:
        """
        Apply the Double Controlled-Pauli-X (Double Controlled-NOT) Gate/Operation to given indexes of
        IBM Qiskit's Quantum Registers and the respective qubits on them.

        :param qiskit_quantum_register_index_1: the index of the 1st IBM Qiskit's Quantum Register.
        :param qiskit_quantum_register_index_2: the index of the 2nd IBM Qiskit's Quantum Register.
        :param qubit_index_1: the index of a qubit inside the 1st IBM Qiskit's Quantum Register.
        :param qubit_index_2: the index of a qubit inside the 2nd IBM Qiskit's Quantum Register.
        """

        is_possible_to_apply_operation_1 = \
            self.check_if_is_possible_to_apply_operation(qiskit_quantum_register_index_1,
                                                         qubit_index_1, True)
        """
        Check if it is possible to apply the pretended operation for
        the control IBM Qiskit's 1st Quantum Register and the respective qubit.
        """

        is_possible_to_apply_operation_2 = \
            self.check_if_is_possible_to_apply_operation(qiskit_quantum_register_index_2,
                                                         qubit_index_2, True)
        """
        Check if it is possible to apply the pretended operation for
        the target IBM Qiskit's 2nd Quantum Register and the respective qubit.
        """

        if is_possible_to_apply_operation_1 and is_possible_to_apply_operation_2:
            """
            It is possible to apply the pretended operation for both
            the IBM Qiskit's Quantum Registers and their respective qubits.
            """

            self.qiskit_quantum_circuit.dcx(self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_index_1][qubit_index_1],
                                            self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_index_2][qubit_index_2])
            """
            Apply the Double Controlled-Pauli-X (Double Controlled-NOT) Gate/Operation to the given indexes of
            IBM Qiskit's Quantum Registers and their respective qubits.
            """

    def apply_controlled_controlled_pauli_x(self,
                                            qiskit_quantum_register_control_index_1: int,
                                            qiskit_quantum_register_control_index_2: int,
                                            qiskit_quantum_register_target_index: int,
                                            control_qubit_index_1: int, control_qubit_index_2: int,
                                            target_qubit_index: int) -> None:
        """
        Apply the Controlled-Controlled-Pauli-X (Toffolli) Gate/Operation to
        given indexes of a control IBM Qiskit's Quantum Register and the respective qubit on it, as also,
        two target IBM Qiskit's Quantum Registers and the respective qubits on them.

        :param qiskit_quantum_register_control_index_1: the index of the 1st control IBM Qiskit's Quantum Register.
        :param qiskit_quantum_register_control_index_2: the index of the 2nd control IBM Qiskit's Quantum Register.
        :param qiskit_quantum_register_target_index: the index of the target IBM Qiskit's Quantum Register.
        :param control_qubit_index_1: the index of a qubit inside the 1st control IBM Qiskit's Quantum Register.
        :param control_qubit_index_2: the index of a qubit inside the 2nd control IBM Qiskit's Quantum Register.
        :param target_qubit_index: the index of a qubit inside the target IBM Qiskit's Quantum Register.
        """

        is_possible_to_apply_operation_control_1 = \
            self.check_if_is_possible_to_apply_operation(qiskit_quantum_register_control_index_1,
                                                         control_qubit_index_1, True)
        """
        Check if it is possible to apply the pretended operation for
        the 1st control IBM Qiskit's Quantum Register and the respective control qubit.
        """

        is_possible_to_apply_operation_control_2 = \
            self.check_if_is_possible_to_apply_operation(qiskit_quantum_register_control_index_2,
                                                         control_qubit_index_2, True)
        """
        Check if it is possible to apply the pretended operation for
        the 2nd control IBM Qiskit's Quantum Register and the respective control qubit.
        """

        is_possible_to_apply_operation_target = \
            self.check_if_is_possible_to_apply_operation(qiskit_quantum_register_target_index,
                                                         target_qubit_index, True)
        """
        Check if it is possible to apply the pretended operation for
        the target IBM Qiskit's Quantum Register and the respective target qubit.
        """

        if is_possible_to_apply_operation_control_1 and is_possible_to_apply_operation_control_2 and \
                is_possible_to_apply_operation_target:
            """
            It is possible to apply the pretended operation for both
            the controls and target IBM Qiskit's Quantum Registers and their respective qubits.
            """

            self.qiskit_quantum_circuit.ccx(self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_control_index_1][control_qubit_index_1],
                                            self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_control_index_2][control_qubit_index_2],
                                            self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_target_index][target_qubit_index])
            """
            Apply the Controlled-Controlled-Pauli-X (Toffolli) Gate/Operation to the given indexes of
            controls and target IBM Qiskit's Quantum Registers and their respective qubits.
            """

    def apply_controlled_controlled_pauli_y(self,
                                            qiskit_quantum_register_control_index_1: int,
                                            qiskit_quantum_register_control_index_2: int,
                                            qiskit_quantum_register_target_index: int,
                                            control_qubit_index_1: int, control_qubit_index_2: int,
                                            target_qubit_index: int) -> None:
        """
        Apply the Controlled-Controlled-Pauli-Y Gate/Operation to
        given indexes of a control IBM Qiskit's Quantum Register and the respective qubit on it, as also,
        two target IBM Qiskit's Quantum Registers and the respective qubits on them.

        :param qiskit_quantum_register_control_index_1: the index of the 1st control IBM Qiskit's Quantum Register.
        :param qiskit_quantum_register_control_index_2: the index of the 2nd control IBM Qiskit's Quantum Register.
        :param qiskit_quantum_register_target_index: the index of the target IBM Qiskit's Quantum Register.
        :param control_qubit_index_1: the index of a qubit inside the 1st control IBM Qiskit's Quantum Register.
        :param control_qubit_index_2: the index of a qubit inside the 2nd control IBM Qiskit's Quantum Register.
        :param target_qubit_index: the index of a qubit inside the target IBM Qiskit's Quantum Register.
        """

        is_possible_to_apply_operation_control_1 = \
            self.check_if_is_possible_to_apply_operation(qiskit_quantum_register_control_index_1,
                                                         control_qubit_index_1, True)
        """
        Check if it is possible to apply the pretended operation for
        the 1st control IBM Qiskit's Quantum Register and the respective control qubit.
        """

        is_possible_to_apply_operation_control_2 = \
            self.check_if_is_possible_to_apply_operation(qiskit_quantum_register_control_index_2,
                                                         control_qubit_index_2, True)
        """
        Check if it is possible to apply the pretended operation for
        the 2nd control IBM Qiskit's Quantum Register and the respective control qubit.
        """

        is_possible_to_apply_operation_target = \
            self.check_if_is_possible_to_apply_operation(qiskit_quantum_register_target_index,
                                                         target_qubit_index, True)
        """
        Check if it is possible to apply the pretended operation for
        the target IBM Qiskit's Quantum Register and the respective target qubit.
        """

        if is_possible_to_apply_operation_control_1 and is_possible_to_apply_operation_control_2 and \
                is_possible_to_apply_operation_target:
            """
            It is possible to apply the pretended operation for both
            the controls and target IBM Qiskit's Quantum Registers and their respective qubits.
            """

            controlled_controlled_pauli_y_unitary_matrix_operator = Operator([
                [1, 0, 0, 0, 0, 0,  0,   0],
                [0, 1, 0, 0, 0, 0,  0,   0],
                [0, 0, 1, 0, 0, 0,  0,   0],
                [0, 0, 0, 1, 0, 0,  0,   0],
                [0, 0, 0, 0, 1, 0,  0,   0],
                [0, 0, 0, 0, 0, 1,  0,   0],
                [0, 0, 0, 0, 0, 0,  0, -1j],
                [0, 0, 0, 0, 0, 0, 1j,   0]
            ])
            """
            Set the Unitary Matrix/Operator for the Controlled-Controlled-Pauli-Y Gate/Operation.
            """

            self.qiskit_quantum_circuit.unitary(controlled_controlled_pauli_y_unitary_matrix_operator,
                                                [self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_control_index_1][control_qubit_index_1],
                                                 self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_control_index_2][control_qubit_index_2],
                                                 self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_target_index][target_qubit_index]],
                                                label="ccy")
            """
            Apply the Controlled-Controlled-Pauli-Y Gate/Operation to the given indexes of
            controls and target IBM Qiskit's Quantum Registers and their respective qubits.
            """

    def apply_controlled_controlled_pauli_z(self,
                                            qiskit_quantum_register_control_index_1: int,
                                            qiskit_quantum_register_control_index_2: int,
                                            qiskit_quantum_register_target_index: int,
                                            control_qubit_index_1: int, control_qubit_index_2: int,
                                            target_qubit_index: int) -> None:
        """
        Apply the Controlled-Controlled-Pauli-Z Gate/Operation to
        given indexes of a control IBM Qiskit's Quantum Register and the respective qubit on it, as also,
        two target IBM Qiskit's Quantum Registers and the respective qubits on them.

        :param qiskit_quantum_register_control_index_1: the index of the 1st control IBM Qiskit's Quantum Register.
        :param qiskit_quantum_register_control_index_2: the index of the 2nd control IBM Qiskit's Quantum Register.
        :param qiskit_quantum_register_target_index: the index of the target IBM Qiskit's Quantum Register.
        :param control_qubit_index_1: the index of a qubit inside the 1st control IBM Qiskit's Quantum Register.
        :param control_qubit_index_2: the index of a qubit inside the 2nd control IBM Qiskit's Quantum Register.
        :param target_qubit_index: the index of a qubit inside the target IBM Qiskit's Quantum Register.
        """

        is_possible_to_apply_operation_control_1 = \
            self.check_if_is_possible_to_apply_operation(qiskit_quantum_register_control_index_1,
                                                         control_qubit_index_1, True)
        """
        Check if it is possible to apply the pretended operation for
        the 1st control IBM Qiskit's Quantum Register and the respective control qubit.
        """

        is_possible_to_apply_operation_control_2 = \
            self.check_if_is_possible_to_apply_operation(qiskit_quantum_register_control_index_2,
                                                         control_qubit_index_2, True)
        """
        Check if it is possible to apply the pretended operation for
        the 2nd control IBM Qiskit's Quantum Register and the respective control qubit.
        """

        is_possible_to_apply_operation_target = \
            self.check_if_is_possible_to_apply_operation(qiskit_quantum_register_target_index,
                                                         target_qubit_index, True)
        """
        Check if it is possible to apply the pretended operation for
        the target IBM Qiskit's Quantum Register and the respective target qubit.
        """

        if is_possible_to_apply_operation_control_1 and is_possible_to_apply_operation_control_2 and \
                is_possible_to_apply_operation_target:
            """
            It is possible to apply the pretended operation for both
            the controls and target IBM Qiskit's Quantum Registers and their respective qubits.
            """

            controlled_controlled_pauli_z_unitary_matrix_operator = Operator([
                [1, 0, 0, 0, 0, 0, 0,  0],
                [0, 1, 0, 0, 0, 0, 0,  0],
                [0, 0, 1, 0, 0, 0, 0,  0],
                [0, 0, 0, 1, 0, 0, 0,  0],
                [0, 0, 0, 0, 1, 0, 0,  0],
                [0, 0, 0, 0, 0, 1, 0,  0],
                [0, 0, 0, 0, 0, 0, 1,  0],
                [0, 0, 0, 0, 0, 0, 0, -1]
            ])
            """
            Set the Unitary Matrix/Operator for the Controlled-Controlled-Pauli-Z Gate/Operation.
            """

            self.qiskit_quantum_circuit.unitary(controlled_controlled_pauli_z_unitary_matrix_operator,
                                                [self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_control_index_1][control_qubit_index_1],
                                                 self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_control_index_2][control_qubit_index_2],
                                                 self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_target_index][target_qubit_index]],
                                                label="ccz")
            """
            Apply the Controlled-Controlled-Pauli-Z Gate/Operation to the given indexes of
            controls and target IBM Qiskit's Quantum Registers and their respective qubits.
            """

    def apply_toffolli(self,
                       qiskit_quantum_register_control_index_1: int,
                       qiskit_quantum_register_control_index_2: int,
                       qiskit_quantum_register_target_index: int,
                       control_qubit_index_1: int, control_qubit_index_2: int,
                       target_qubit_index: int) -> None:
        """
        Apply the Controlled-Controlled-Pauli-X (Toffolli) Gate/Operation to
        given indexes of a control IBM Qiskit's Quantum Register and the respective qubit on it, as also,
        two target IBM Qiskit's Quantum Registers and the respective qubits on them.

        :param qiskit_quantum_register_control_index_1: the index of the 1st control IBM Qiskit's Quantum Register.
        :param qiskit_quantum_register_control_index_2: the index of the 2nd control IBM Qiskit's Quantum Register.
        :param qiskit_quantum_register_target_index: the index of the target IBM Qiskit's Quantum Register.
        :param control_qubit_index_1: the index of a qubit inside the 1st control IBM Qiskit's Quantum Register.
        :param control_qubit_index_2: the index of a qubit inside the 2nd control IBM Qiskit's Quantum Register.
        :param target_qubit_index: the index of a qubit inside the target IBM Qiskit's Quantum Register.
        """

        self.apply_controlled_controlled_pauli_x(qiskit_quantum_register_control_index_1,
                                                 qiskit_quantum_register_control_index_2,
                                                 qiskit_quantum_register_target_index,
                                                 control_qubit_index_1, control_qubit_index_2,
                                                 target_qubit_index)
        """
        Apply the equivalent Controlled-Controlled-X (Toffolli) Gate/Operation to the given indexes of
        controls and target IBM Qiskit's Quantum Registers and their respective qubits.
        """

    def apply_controlled_pauli_x_pauli_x(self,
                                         qiskit_quantum_register_control_index: int,
                                         qiskit_quantum_register_target_index_1: int,
                                         qiskit_quantum_register_target_index_2: int,
                                         control_qubit_index: int,
                                         target_qubit_index_1: int, target_qubit_index_2: int) -> None:
        """
        Apply the Controlled-Pauli-X-Pauli-X Gate/Operation to
        given indexes of a control IBM Qiskit's Quantum Register and the respective qubit on it, as also,
        two target IBM Qiskit's Quantum Registers and the respective qubits on them.

        :param qiskit_quantum_register_control_index: the index of the control IBM Qiskit's Quantum Register.
        :param qiskit_quantum_register_target_index_1: the index of the 1st target IBM Qiskit's Quantum Register.
        :param qiskit_quantum_register_target_index_2: the index of the 2nd target IBM Qiskit's Quantum Register.
        :param control_qubit_index: the index of a qubit inside the control IBM Qiskit's Quantum Register.
        :param target_qubit_index_1: the index of a qubit inside the 1st target IBM Qiskit's Quantum Register.
        :param target_qubit_index_2: the index of a qubit inside the 2nd target IBM Qiskit's Quantum Register.
        """

        is_possible_to_apply_operation_control = \
            self.check_if_is_possible_to_apply_operation(qiskit_quantum_register_control_index,
                                                         control_qubit_index, True)
        """
        Check if it is possible to apply the pretended operation for
        the control IBM Qiskit's Quantum Register and the respective control qubit.
        """

        is_possible_to_apply_operation_target_1 = \
            self.check_if_is_possible_to_apply_operation(qiskit_quantum_register_target_index_1,
                                                         target_qubit_index_1, True)
        """
        Check if it is possible to apply the pretended operation for
        the 1st target IBM Qiskit's Quantum Register and the respective target qubit.
        """

        is_possible_to_apply_operation_target_2 = \
            self.check_if_is_possible_to_apply_operation(qiskit_quantum_register_target_index_2,
                                                         target_qubit_index_2, True)
        """
        Check if it is possible to apply the pretended operation for
        the 2nd target IBM Qiskit's Quantum Register and the respective target qubit.
        """

        if is_possible_to_apply_operation_control and \
                is_possible_to_apply_operation_target_1 and is_possible_to_apply_operation_target_2:
            """
            It is possible to apply the pretended operation for both
            the control and targets IBM Qiskit's Quantum Registers and their respective qubits.
            """

            controlled_pauli_x_pauli_x_unitary_matrix_operator = Operator([
                [1, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1],
                [0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 1, 0],
                [0, 1, 0, 0, 0, 0, 0, 0]
            ])
            """
            Set the Unitary Matrix/Operator for the Controlled-Pauli-X-Pauli-X Gate/Operation.
            """

            self.qiskit_quantum_circuit.unitary(controlled_pauli_x_pauli_x_unitary_matrix_operator,
                                                [self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_control_index][control_qubit_index],
                                                 self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_target_index_1][target_qubit_index_1],
                                                 self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_target_index_2][target_qubit_index_2]],
                                                label="cxx")
            """
            Apply the Controlled-Pauli-X-Pauli-X Gate/Operation to the given indexes of
            controls and target IBM Qiskit's Quantum Registers and their respective qubits.
            """

    def apply_controlled_pauli_y_pauli_y(self,
                                         qiskit_quantum_register_control_index: int,
                                         qiskit_quantum_register_target_index_1: int,
                                         qiskit_quantum_register_target_index_2: int,
                                         control_qubit_index: int,
                                         target_qubit_index_1: int, target_qubit_index_2: int) -> None:
        """
        Apply the Controlled-Pauli-Y-Pauli-Y Gate/Operation to
        given indexes of a control IBM Qiskit's Quantum Register and the respective qubit on it, as also,
        two target IBM Qiskit's Quantum Registers and the respective qubits on them.

        :param qiskit_quantum_register_control_index: the index of the control IBM Qiskit's Quantum Register.
        :param qiskit_quantum_register_target_index_1: the index of the 1st target IBM Qiskit's Quantum Register.
        :param qiskit_quantum_register_target_index_2: the index of the 2nd target IBM Qiskit's Quantum Register.
        :param control_qubit_index: the index of a qubit inside the control IBM Qiskit's Quantum Register.
        :param target_qubit_index_1: the index of a qubit inside the 1st target IBM Qiskit's Quantum Register.
        :param target_qubit_index_2: the index of a qubit inside the 2nd target IBM Qiskit's Quantum Register.
        """

        is_possible_to_apply_operation_control = \
            self.check_if_is_possible_to_apply_operation(qiskit_quantum_register_control_index,
                                                         control_qubit_index, True)
        """
        Check if it is possible to apply the pretended operation for
        the control IBM Qiskit's Quantum Register and the respective control qubit.
        """

        is_possible_to_apply_operation_target_1 = \
            self.check_if_is_possible_to_apply_operation(qiskit_quantum_register_target_index_1,
                                                         target_qubit_index_1, True)
        """
        Check if it is possible to apply the pretended operation for
        the 1st target IBM Qiskit's Quantum Register and the respective target qubit.
        """

        is_possible_to_apply_operation_target_2 = \
            self.check_if_is_possible_to_apply_operation(qiskit_quantum_register_target_index_2,
                                                         target_qubit_index_2, True)
        """
        Check if it is possible to apply the pretended operation for
        the 2nd target IBM Qiskit's Quantum Register and the respective target qubit.
        """

        if is_possible_to_apply_operation_control and \
                is_possible_to_apply_operation_target_1 and is_possible_to_apply_operation_target_2:
            """
            It is possible to apply the pretended operation for both
            the control and targets IBM Qiskit's Quantum Registers and their respective qubits.
            """

            controlled_pauli_y_pauli_y_unitary_matrix_operator = Operator([
                [1,  0, 0, 0, 0, 0, 0,  0],
                [0,  0, 0, 0, 0, 0, 0, -1],
                [0,  0, 1, 0, 0, 0, 0,  0],
                [0,  0, 0, 0, 0, 1, 0,  0],
                [0,  0, 0, 0, 1, 0, 0,  0],
                [0,  0, 0, 1, 0, 0, 0,  0],
                [0,  0, 0, 0, 0, 0, 1,  0],
                [0, -1, 0, 0, 0, 0, 0,  0]
            ])
            """
            Set the Unitary Matrix/Operator for the Controlled-Pauli-Y-Pauli-Y Gate/Operation.
            """

            self.qiskit_quantum_circuit.unitary(controlled_pauli_y_pauli_y_unitary_matrix_operator,
                                                [self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_control_index][control_qubit_index],
                                                 self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_target_index_1][target_qubit_index_1],
                                                 self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_target_index_2][target_qubit_index_2]],
                                                label="cyy")
            """
            Apply the Controlled-Pauli-Y-Pauli-Y Gate/Operation to the given indexes of
            controls and target IBM Qiskit's Quantum Registers and their respective qubits.
            """

    def apply_controlled_pauli_z_pauli_z(self,
                                         qiskit_quantum_register_control_index: int,
                                         qiskit_quantum_register_target_index_1: int,
                                         qiskit_quantum_register_target_index_2: int,
                                         control_qubit_index: int,
                                         target_qubit_index_1: int, target_qubit_index_2: int) -> None:
        """
        Apply the Controlled-Pauli-Z-Pauli-Z Gate/Operation to
        given indexes of a control IBM Qiskit's Quantum Register and the respective qubit on it, as also,
        two target IBM Qiskit's Quantum Registers and the respective qubits on them.

        :param qiskit_quantum_register_control_index: the index of the control IBM Qiskit's Quantum Register.
        :param qiskit_quantum_register_target_index_1: the index of the 1st target IBM Qiskit's Quantum Register.
        :param qiskit_quantum_register_target_index_2: the index of the 2nd target IBM Qiskit's Quantum Register.
        :param control_qubit_index: the index of a qubit inside the control IBM Qiskit's Quantum Register.
        :param target_qubit_index_1: the index of a qubit inside the 1st target IBM Qiskit's Quantum Register.
        :param target_qubit_index_2: the index of a qubit inside the 2nd target IBM Qiskit's Quantum Register.
        """

        is_possible_to_apply_operation_control = \
            self.check_if_is_possible_to_apply_operation(qiskit_quantum_register_control_index,
                                                         control_qubit_index, True)
        """
        Check if it is possible to apply the pretended operation for
        the control IBM Qiskit's Quantum Register and the respective control qubit.
        """

        is_possible_to_apply_operation_target_1 = \
            self.check_if_is_possible_to_apply_operation(qiskit_quantum_register_target_index_1,
                                                         target_qubit_index_1, True)
        """
        Check if it is possible to apply the pretended operation for
        the 1st target IBM Qiskit's Quantum Register and the respective target qubit.
        """

        is_possible_to_apply_operation_target_2 = \
            self.check_if_is_possible_to_apply_operation(qiskit_quantum_register_target_index_2,
                                                         target_qubit_index_2, True)
        """
        Check if it is possible to apply the pretended operation for
        the 2nd target IBM Qiskit's Quantum Register and the respective target qubit.
        """

        if is_possible_to_apply_operation_control and \
                is_possible_to_apply_operation_target_1 and is_possible_to_apply_operation_target_2:
            """
            It is possible to apply the pretended operation for both
            the control and targets IBM Qiskit's Quantum Registers and their respective qubits.
            """

            controlled_pauli_z_pauli_z_unitary_matrix_operator = Operator([
                [1, 0, 0,  0, 0,  0, 0, 0],
                [0, 1, 0,  0, 0,  0, 0, 1],
                [0, 0, 1,  0, 0,  0, 0, 0],
                [0, 0, 0, -1, 0,  0, 0, 0],
                [0, 0, 0,  0, 1,  0, 0, 0],
                [0, 0, 0,  0, 0, -1, 0, 0],
                [0, 0, 0,  0, 0,  0, 1, 0],
                [0, 0, 0,  0, 0,  0, 0, 1]
            ])
            """
            Set the Unitary Matrix/Operator for the Controlled-Pauli-Z-Pauli-Z Gate/Operation.
            """

            self.qiskit_quantum_circuit.unitary(controlled_pauli_z_pauli_z_unitary_matrix_operator,
                                                [self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_control_index][control_qubit_index],
                                                 self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_target_index_1][target_qubit_index_1],
                                                 self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_target_index_2][target_qubit_index_2]],
                                                label="czz")
            """
            Apply the Controlled-Pauli-Z-Pauli-Z Gate/Operation to the given indexes of
            controls and target IBM Qiskit's Quantum Registers and their respective qubits.
            """

    def apply_ising_coupling_rxx_radians(self,
                                         theta_radians: float,
                                         qiskit_quantum_register_index_1: int,
                                         qiskit_quantum_register_index_2: int,
                                         qubit_index_1: int, qubit_index_2: int) -> None:
        """
        Apply the Ising Coupling R_(xx)(theta_radians) (Rotation_(xx)(theta_radians)) Gate/Operation to
        given indexes of IBM Qiskit's Quantum Registers and their respective qubits on them.

        :param theta_radians: the theta angle in radians,
                              for the Ising Coupling R_(xx)(theta_radians) (R_(xx)(theta_radians)) Gate/Operation.
        :param qiskit_quantum_register_index_1: the index of the 1st IBM Qiskit's Quantum Register.
        :param qiskit_quantum_register_index_2: the index of the 2nd IBM Qiskit's Quantum Register.
        :param qubit_index_1: the index of a qubit inside the 1st IBM Qiskit's Quantum Register.
        :param qubit_index_2: the index of a qubit inside the 2nd IBM Qiskit's Quantum Register.
        """

        is_possible_to_apply_operation_1 = \
            self.check_if_is_possible_to_apply_operation(qiskit_quantum_register_index_1,
                                                         qubit_index_1, True)
        """
        Check if it is possible to apply the pretended operation for
        the 1st IBM Qiskit's Quantum Register and the respective qubit.
        """

        is_possible_to_apply_operation_2 = \
            self.check_if_is_possible_to_apply_operation(qiskit_quantum_register_index_2,
                                                         qubit_index_2, True)
        """
        Check if it is possible to apply the pretended operation for
        the 2nd IBM Qiskit's Quantum Register and the respective qubit.
        """

        if is_possible_to_apply_operation_1 and is_possible_to_apply_operation_2:
            """
            It is possible to apply the pretended operation for both
            the IBM Qiskit's Quantum Registers and their respective qubits.
            """

            self.qiskit_quantum_circuit.rxx(theta_radians,
                                            self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_index_1][qubit_index_1],
                                            self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_index_2][qubit_index_2])
            """
            Apply the Ising Coupling R_(xx)(theta_radians) (Rotation_(xx)(theta_radians)) Gate/Operation to
            the given indexes of IBM Qiskit's Quantum Registers and their respective qubits.
            """

    def apply_ising_coupling_rxx_degrees(self,
                                         theta_degrees: float,
                                         qiskit_quantum_register_index_1: int,
                                         qiskit_quantum_register_index_2: int,
                                         qubit_index_1: int, qubit_index_2: int) -> None:
        """
        Apply the Ising Coupling R_(xx)(theta_degrees) (Rotation_(xx)(theta_degrees)) Gate/Operation to
        given indexes of IBM Qiskit's Quantum Registers and their respective qubits on them.

        :param theta_degrees: the theta angle in degrees,
                              for the Ising Coupling R_(xx)(theta_degrees) (R_(xx)(theta_degrees)) Gate/Operation.
        :param qiskit_quantum_register_index_1: the index of the 1st IBM Qiskit's Quantum Register.
        :param qiskit_quantum_register_index_2: the index of the 2nd IBM Qiskit's Quantum Register.
        :param qubit_index_1: the index of a qubit inside the 1st IBM Qiskit's Quantum Register.
        :param qubit_index_2: the index of a qubit inside the 2nd IBM Qiskit's Quantum Register.
        """

        theta_radians = radians(theta_degrees)
        """
        Convert the theta angle in degrees to radians.
        """

        self.apply_ising_coupling_rxx_radians(theta_radians,
                                              qiskit_quantum_register_index_1,
                                              qiskit_quantum_register_index_2,
                                              qubit_index_1, qubit_index_2)
        """
        Apply the Ising Coupling R_(xx)(theta_radians) (Rotation_(xx)(theta_radians)) Gate/Operation to
        the given indexes of IBM Qiskit's Quantum Registers and their respective qubits.
        """

    def apply_ising_coupling_ryy_radians(self,
                                         theta_radians: float,
                                         qiskit_quantum_register_index_1: int,
                                         qiskit_quantum_register_index_2: int,
                                         qubit_index_1: int, qubit_index_2: int) -> None:
        """
        Apply the Ising Coupling R_(yy)(theta_radians) (Rotation_(yy)(theta_radians)) Gate/Operation to
        given indexes of IBM Qiskit's Quantum Registers and their respective qubits on them.

        :param theta_radians: the theta angle in radians,
                              for the Ising Coupling R_(yy)(theta_radians) (R_(yy)(theta_radians)) Gate/Operation.
        :param qiskit_quantum_register_index_1: the index of the 1st IBM Qiskit's Quantum Register.
        :param qiskit_quantum_register_index_2: the index of the 2nd IBM Qiskit's Quantum Register.
        :param qubit_index_1: the index of a qubit inside the 1st IBM Qiskit's Quantum Register.
        :param qubit_index_2: the index of a qubit inside the 2nd IBM Qiskit's Quantum Register.
        """

        is_possible_to_apply_operation_1 = \
            self.check_if_is_possible_to_apply_operation(qiskit_quantum_register_index_1,
                                                         qubit_index_1, True)
        """
        Check if it is possible to apply the pretended operation for
        the 1st IBM Qiskit's Quantum Register and the respective qubit.
        """

        is_possible_to_apply_operation_2 = \
            self.check_if_is_possible_to_apply_operation(qiskit_quantum_register_index_2,
                                                         qubit_index_2, True)
        """
        Check if it is possible to apply the pretended operation for
        the 2nd IBM Qiskit's Quantum Register and the respective qubit.
        """

        if is_possible_to_apply_operation_1 and is_possible_to_apply_operation_2:
            """
            It is possible to apply the pretended operation for both
            the IBM Qiskit's Quantum Registers and their respective qubits.
            """

            self.qiskit_quantum_circuit.ryy(theta_radians,
                                            self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_index_1][qubit_index_1],
                                            self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_index_2][qubit_index_2])
            """
            Apply the Ising Coupling R_(yy)(theta_radians) (Rotation_(yy)(theta_radians)) Gate/Operation to
            the given indexes of IBM Qiskit's Quantum Registers and their respective qubits.
            """

    def apply_ising_coupling_ryy_degrees(self,
                                         theta_degrees: float,
                                         qiskit_quantum_register_index_1: int,
                                         qiskit_quantum_register_index_2: int,
                                         qubit_index_1: int, qubit_index_2: int) -> None:
        """
        Apply the Ising Coupling R_(yy)(theta_degrees) (Rotation_(yy)(theta_degrees)) Gate/Operation to
        given indexes of IBM Qiskit's Quantum Registers and their respective qubits on them.

        :param theta_degrees: the theta angle in degrees,
                              for the Ising Coupling R_(yy)(theta_degrees) (R_(yy)(theta_degrees)) Gate/Operation.
        :param qiskit_quantum_register_index_1: the index of the 1st IBM Qiskit's Quantum Register.
        :param qiskit_quantum_register_index_2: the index of the 2nd IBM Qiskit's Quantum Register.
        :param qubit_index_1: the index of a qubit inside the 1st IBM Qiskit's Quantum Register.
        :param qubit_index_2: the index of a qubit inside the 2nd IBM Qiskit's Quantum Register.
        """

        theta_radians = radians(theta_degrees)
        """
        Convert the theta angle in degrees to radians.
        """

        self.apply_ising_coupling_ryy_radians(theta_radians,
                                              qiskit_quantum_register_index_1,
                                              qiskit_quantum_register_index_2,
                                              qubit_index_1, qubit_index_2)
        """
        Apply the Ising Coupling R_(yy)(theta_radians) (Rotation_(yy)(theta_radians)) Gate/Operation to
        the given indexes of IBM Qiskit's Quantum Registers and their respective qubits.
        """

    def apply_ising_coupling_rzz_radians(self,
                                         theta_radians: float,
                                         qiskit_quantum_register_index_1: int,
                                         qiskit_quantum_register_index_2: int,
                                         qubit_index_1: int, qubit_index_2: int) -> None:
        """
        Apply the Ising Coupling R_(zz)(theta_radians) (Rotation_(zz)(theta_radians)) Gate/Operation to
        given indexes of IBM Qiskit's Quantum Registers and their respective qubits on them.

        :param theta_radians: the theta angle in radians,
                              for the Ising Coupling R_(zz)(theta_radians) (R_(zz)(theta_radians)) Gate/Operation.
        :param qiskit_quantum_register_index_1: the index of the 1st IBM Qiskit's Quantum Register.
        :param qiskit_quantum_register_index_2: the index of the 2nd IBM Qiskit's Quantum Register.
        :param qubit_index_1: the index of a qubit inside the 1st IBM Qiskit's Quantum Register.
        :param qubit_index_2: the index of a qubit inside the 2nd IBM Qiskit's Quantum Register.
        """

        is_possible_to_apply_operation_1 = \
            self.check_if_is_possible_to_apply_operation(qiskit_quantum_register_index_1,
                                                         qubit_index_1, True)
        """
        Check if it is possible to apply the pretended operation for
        the 1st IBM Qiskit's Quantum Register and the respective qubit.
        """

        is_possible_to_apply_operation_2 = \
            self.check_if_is_possible_to_apply_operation(qiskit_quantum_register_index_2,
                                                         qubit_index_2, True)
        """
        Check if it is possible to apply the pretended operation for
        the 2nd IBM Qiskit's Quantum Register and the respective qubit.
        """

        if is_possible_to_apply_operation_1 and is_possible_to_apply_operation_2:
            """
            It is possible to apply the pretended operation for both
            the IBM Qiskit's Quantum Registers and their respective qubits.
            """

            self.qiskit_quantum_circuit.rzz(theta_radians,
                                            self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_index_1][qubit_index_1],
                                            self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_index_2][qubit_index_2])
            """
            Apply the Ising Coupling R_(zz)(theta_radians) (Rotation_(zz)(theta_radians)) Gate/Operation to
            the given indexes of IBM Qiskit's Quantum Registers and their respective qubits.
            """

    def apply_ising_coupling_rzz_degrees(self,
                                         theta_degrees: float,
                                         qiskit_quantum_register_index_1: int,
                                         qiskit_quantum_register_index_2: int,
                                         qubit_index_1: int, qubit_index_2: int) -> None:
        """
        Apply the Ising Coupling R_(zz)(theta_degrees) (Rotation_(zz)(theta_degrees)) Gate/Operation to
        given indexes of IBM Qiskit's Quantum Registers and their respective qubits on them.

        :param theta_degrees: the theta angle in degrees,
                              for the Ising Coupling R_(zz)(theta_degrees) (R_(zz)(theta_degrees)) Gate/Operation.
        :param qiskit_quantum_register_index_1: the index of the 1st IBM Qiskit's Quantum Register.
        :param qiskit_quantum_register_index_2: the index of the 2nd IBM Qiskit's Quantum Register.
        :param qubit_index_1: the index of a qubit inside the 1st IBM Qiskit's Quantum Register.
        :param qubit_index_2: the index of a qubit inside the 2nd IBM Qiskit's Quantum Register.
        """

        theta_radians = radians(theta_degrees)
        """
        Convert the theta angle in degrees to radians.
        """

        self.apply_ising_coupling_rzz_radians(theta_radians,
                                              qiskit_quantum_register_index_1,
                                              qiskit_quantum_register_index_2,
                                              qubit_index_1, qubit_index_2)
        """
        Apply the Ising Coupling R_(zz)(theta_radians) (Rotation_(zz)(theta_radians)) Gate/Operation to
        the given indexes of IBM Qiskit's Quantum Registers and their respective qubits.
        """

    def apply_rzx_radians(self,
                          theta_radians: float,
                          qiskit_quantum_register_index_1: int,
                          qiskit_quantum_register_index_2: int,
                          qubit_index_1: int, qubit_index_2: int) -> None:
        """
        Apply the R_(zx)(theta_radians) (Rotation_(zx)(theta_radians)) Gate/Operation to
        given indexes of IBM Qiskit's Quantum Registers and their respective qubits on them.

        :param theta_radians: the theta angle in radians,
                              for the R_(zx)(theta_radians) (R_(zx)(theta_radians)) Gate/Operation.
        :param qiskit_quantum_register_index_1: the index of the 1st IBM Qiskit's Quantum Register.
        :param qiskit_quantum_register_index_2: the index of the 2nd IBM Qiskit's Quantum Register.
        :param qubit_index_1: the index of a qubit inside the 1st IBM Qiskit's Quantum Register.
        :param qubit_index_2: the index of a qubit inside the 2nd IBM Qiskit's Quantum Register.
        """

        is_possible_to_apply_operation_1 = \
            self.check_if_is_possible_to_apply_operation(qiskit_quantum_register_index_1,
                                                         qubit_index_1, True)
        """
        Check if it is possible to apply the pretended operation for
        the 1st IBM Qiskit's Quantum Register and the respective qubit.
        """

        is_possible_to_apply_operation_2 = \
            self.check_if_is_possible_to_apply_operation(qiskit_quantum_register_index_2,
                                                         qubit_index_2, True)
        """
        Check if it is possible to apply the pretended operation for
        the 2nd IBM Qiskit's Quantum Register and the respective qubit.
        """

        if is_possible_to_apply_operation_1 and is_possible_to_apply_operation_2:
            """
            It is possible to apply the pretended operation for both
            the IBM Qiskit's Quantum Registers and their respective qubits.
            """

            self.qiskit_quantum_circuit.rzx(theta_radians,
                                            self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_index_1][qubit_index_1],
                                            self.qiskit_quantum_circuit.qregs[qiskit_quantum_register_index_2][qubit_index_2])
            """
            Apply the R_(zx)(theta_radians) (Rotation_(zx)(theta_radians)) Gate/Operation to
            the given indexes of IBM Qiskit's Quantum Registers and their respective qubits.
            """

    def apply_rzx_degrees(self,
                          theta_degrees: float,
                          qiskit_quantum_register_index_1: int,
                          qiskit_quantum_register_index_2: int,
                          qubit_index_1: int, qubit_index_2: int) -> None:
        """
        Apply the R_(zx)(theta_degrees) (Rotation_(zx)(theta_degrees)) Gate/Operation to
        given indexes of IBM Qiskit's Quantum Registers and their respective qubits on them.

        :param theta_degrees: the theta angle in degrees,
                              for the R_(zx)(theta_degrees) (R_(zx)(theta_degrees)) Gate/Operation.
        :param qiskit_quantum_register_index_1: the index of the 1st IBM Qiskit's Quantum Register.
        :param qiskit_quantum_register_index_2: the index of the 2nd IBM Qiskit's Quantum Register.
        :param qubit_index_1: the index of a qubit inside the 1st IBM Qiskit's Quantum Register.
        :param qubit_index_2: the index of a qubit inside the 2nd IBM Qiskit's Quantum Register.
        """

        theta_radians = radians(theta_degrees)
        """
        Convert the theta angle in degrees to radians.
        """

        self.apply_rzx_radians(theta_radians,
                               qiskit_quantum_register_index_1,
                               qiskit_quantum_register_index_2,
                               qubit_index_1, qubit_index_2)
        """
        Apply the R_(zx)(theta_radians) (Rotation_(zx)(theta_radians)) Gate/Operation to
        the given indexes of IBM Qiskit's Quantum Registers and their respective qubits.
        """

    @staticmethod
    def create_global_molmer_sorensen_radians_qiskrypt_quantum_circuit(num_qubits: int,
                                                                       thetas_radians: list,
                                                                       name="qu_circ_gms") -> QiskryptQuantumCircuit:
        """
        Create a Qiskrypt's Quantum Circuit based on
        the Global Mølmer-Sørensen(thetas_radians) (GMS(thetas_radians)) Gate/Operation for a given number of qubits,
        based on a list of theta angles in radians to build the respective Unitary Matrix/Operator.

        :param num_qubits: the number of qubits for the Qiskrypt's Quantum Circuit.
        :param thetas_radians: the list of theta angles in radians to build the respective Unitary Matrix/Operator.
        :param name: the name for the Qiskrypt's Quantum Circuit.
        """

        if len(thetas_radians) == (num_qubits**2):
            """
            If the number of elements in the list of theta angles in radians is equal to
            the squared number of qubits.
            """

            thetas_radians_unitary_matrix_operator = zeros((num_qubits, num_qubits))
            """
            Create the Unitary Matrix/Operator for the theta angle in radians.
            """

            for row_unitary_matrix_operator in range(num_qubits):
                """
                For each row of the Unitary Matrix/Operator with
                the theta angles in radians.
                """

                for column_unitary_matrix_operator in range(num_qubits):
                    """
                    For each column of the Unitary Matrix/Operator with
                    the theta angles in radians.
                    """

                    theta_radians = thetas_radians[((row_unitary_matrix_operator * num_qubits) + num_qubits)]
                    """
                    Retrieve the current theta angle in radians from the list of them.
                    """

                    thetas_radians_unitary_matrix_operator[row_unitary_matrix_operator][column_unitary_matrix_operator] = theta_radians
                    """
                    Assign the current theta angle in radians to
                    the current element of the Unitary Matrix/Operator.
                    """

            global_molmer_sorensen_radians_qiskit_quantum_circuit = GMS(num_qubits, thetas_radians_unitary_matrix_operator)
            """
            Create the Qiskit's Quantum Circuit based on
            the Global Mølmer-Sørensen(thetas_radians) (GMS(thetas_radians)) Gate/Operation.
            """

            global_molmer_sorensen_radians_qiskrypt_quantum_circuit = \
                QiskryptQuantumCircuit(name, qiskit_quantum_circuit=global_molmer_sorensen_radians_qiskit_quantum_circuit)
            """
            Create the Qiskrypt's Quantum Circuit for
            the Global Mølmer-Sørensen(thetas_radians) (GMS(thetas_radians)) Gate/Operation.
            """

            """
            Return the Qiskrypt's Quantum Circuit for
            the Global Mølmer-Sørensen(thetas_radians) (GMS(thetas_radians)) Gate/Operation.
            """
            return global_molmer_sorensen_radians_qiskrypt_quantum_circuit
        else:
            """
            If the number of elements in the list of theta angles in radians is not equal to
            the squared number of qubits.
            """

            QiskryptQuantumCircuit.raise_list_do_not_represent_a_square_unitary_matrix_operator_error()
            """
            Raise a List Do Not Represent a Square Unitary Matrix Operator Error for the Qiskrypt's Quantum Circuit.
            """

    @staticmethod
    def create_global_molmer_sorensen_degrees_qiskrypt_quantum_circuit(num_qubits: int,
                                                                       thetas_degrees: list,
                                                                       name="qu_circ_gms") -> QiskryptQuantumCircuit:
        """
        Create a Qiskrypt's Quantum Circuit based on
        the Global Mølmer-Sørensen(theta_degrees) (GMS(theta_degrees)) Gate/Operation for a given number of qubits,
        based on a list of theta angles in degrees to build the respective Unitary Matrix/Operator.

        :param num_qubits: the number of qubits for the Qiskrypt's Quantum Circuit.
        :param thetas_degrees: the list of theta angles in degrees to build the respective Unitary Matrix/Operator.
        :param name: the name for the Qiskrypt's Quantum Circuit.
        """

        if len(thetas_degrees) == (num_qubits**2):
            """
            If the number of elements in the list of theta angles in degrees is equal to
            the squared number of qubits.
            """

            thetas_radians = []
            """
            Create a new list of theta angles in radians.
            """

            num_thetas_degrees = len(thetas_degrees)
            """
            Retrieve the number of theta angles in degrees.
            """

            for theta_degree_index in range(num_thetas_degrees):
                """
                For each index of a theta angle in degrees. 
                """

                theta_degrees = thetas_degrees[theta_degree_index]
                """
                Retrieve the current theta angle in degrees.
                """

                theta_radians = radians(theta_degrees)
                """
                Convert the current theta angle in degrees to radians.
                """

                thetas_radians.append(theta_radians)
                """
                Append the current theta angle converted in radians to the respective list.
                """

            thetas_radians_unitary_matrix_operator = zeros((num_qubits, num_qubits))
            """
            Create the Unitary Matrix/Operator for the theta angle in radians.
            """

            for row_unitary_matrix_operator in range(num_qubits):
                """
                For each row of the Unitary Matrix/Operator with
                the theta angles in radians.
                """

                for column_unitary_matrix_operator in range(num_qubits):
                    """
                    For each column of the Unitary Matrix/Operator with
                    the theta angles in radians.
                    """

                    theta_radians = thetas_radians[((row_unitary_matrix_operator * num_qubits) + num_qubits)]
                    """
                    Retrieve the current theta angle in radians from the list of them.
                    """

                    thetas_radians_unitary_matrix_operator[row_unitary_matrix_operator][column_unitary_matrix_operator] = theta_radians
                    """
                    Assign the current theta angle in radians to
                    the current element of the Unitary Matrix/Operator.
                    """

            global_molmer_sorensen_radians_qiskit_quantum_circuit = GMS(num_qubits, thetas_radians_unitary_matrix_operator)
            """
            Create the Qiskit's Quantum Circuit based on
            the Global Mølmer-Sørensen(thetas_radians) (GMS(thetas_radians)) Gate/Operation.
            """

            global_molmer_sorensen_radians_qiskrypt_quantum_circuit = \
                QiskryptQuantumCircuit(name, qiskit_quantum_circuit=global_molmer_sorensen_radians_qiskit_quantum_circuit)
            """
            Create the Qiskrypt's Quantum Circuit for
            the Global Mølmer-Sørensen(thetas_radians) (GMS(thetas_radians)) Gate/Operation.
            """

            """
            Return the Qiskrypt's Quantum Circuit for
            the Global Mølmer-Sørensen(thetas_radians) (GMS(thetas_radians)) Gate/Operation.
            """
            return global_molmer_sorensen_radians_qiskrypt_quantum_circuit
        else:
            """
            If the number of elements in the list of theta angles in degrees is not equal to
            the squared number of qubits.
            """

            QiskryptQuantumCircuit.raise_list_do_not_represent_a_square_unitary_matrix_operator_error()
            """
            Raise a List Do Not Represent a Square Unitary Matrix Operator Error for the Qiskrypt's Quantum Circuit.
            """

    @staticmethod
    def check_if_is_a_qiskrypt_semi_quantum_register(qiskrypt_register: object) -> bool:
        """
        Return a True boolean flag if a given Qiskrypt's Register is Semi-Quantum.
        Or a False boolean flag, otherwise.

        :param qiskrypt_register: a given Qiskrypt's Register.

        :return is_a_qiskrypt_semi_quantum_register: a True boolean flag if a given Qiskrypt's Register is Semi-Quantum.
        Or a False boolean flag, otherwise.
        """

        is_a_qiskrypt_semi_quantum_register = \
            (isinstance(qiskrypt_register, QiskryptSemiQuantumRegister) or
             isinstance(qiskrypt_register, QiskryptAncillaSemiQuantumRegister))
        """
        Retrieve the boolean flag, regarding if a given Qiskrypt's Register is Semi-Quantum or not.
        """

        """
        Return the boolean flag, regarding if a given Qiskrypt's Register is Semi-Quantum or not.
        """
        return is_a_qiskrypt_semi_quantum_register

    @staticmethod
    def raise_unsupported_type_registers_error() -> None:
        """
        Return/Raise an Unsupported Type of Registers Error for the Qiskrypt's Quantum Circuit.

        :raise unsupported_type_registers_error: an Unsupported Type of Registers Error for the Qiskrypt's Quantum Circuit.
        """

        unsupported_type_registers_error = \
            QiskryptQuantumCircuitUnsupportedTypeRegistersError()
        """
        Retrieve the Unsupported Type of Registers Error for the Qiskrypt's Quantum Circuit.
        """

        """
        Raise the Unsupported Type of Registers Error for the Qiskrypt's Quantum Circuit.
        """
        raise unsupported_type_registers_error

    @staticmethod
    def raise_invalid_qiskit_quantum_register_index_given_error() -> None:
        """
        Return/Raise an Invalid IBM Qiskit's Quantum Register Index Given Error.

        :raise invalid_qiskit_quantum_register_index_given_error: an Invalid IBM Qiskit's Quantum Register
                                                                  Index Given Error.
        """

        invalid_qiskit_quantum_register_index_given_error = \
            QiskryptQuantumCircuitInvalidQiskitQuantumRegisterIndexGivenError()
        """
        Retrieve the Invalid IBM Qiskit' Quantum Register Index Given Error for the Qiskrypt's Quantum Circuit.
        """

        """
        Raise the Invalid IBM Qiskit's Quantum Register Index Given Error for the Qiskrypt's Quantum Circuit.
        """
        raise invalid_qiskit_quantum_register_index_given_error

    @staticmethod
    def raise_invalid_qubit_index_given_error() -> None:
        """
        Return/Raise an Invalid Qubit Index Given Error.

        :raise invalid_qubit_index_given_error: an Invalid Qubit Index Given Error.
        """

        invalid_qubit_index_given_error = QiskryptQuantumCircuitInvalidQubitIndexGivenError()
        """
        Retrieve the Invalid Qubit Index Given Error for the Qiskrypt's Quantum Circuit.
        """

        """
        Raise the Invalid Qubit Index Given Error for the Qiskrypt's Quantum Circuit.
        """
        raise invalid_qubit_index_given_error

    @staticmethod
    def raise_unsupported_operation_for_semi_quantum_register_error() -> None:
        """
        Return/Raise an Unsupported Operation for Semi-Quantum Register Error.

        :raise unsupported_operation_for_semi_quantum_register_error: an Unsupported Operation for
                                                                      Semi-Quantum Register Error.
        """

        unsupported_operation_for_semi_quantum_register_error = \
            QiskryptSemiQuantumRegisterUnsupportedOperationError()
        """
        Retrieve the Unsupported Operation for Semi-Quantum Register Error.
        """

        """
        Raise the Unsupported Operation for Semi-Quantum Register Error.
        """
        raise unsupported_operation_for_semi_quantum_register_error

    @staticmethod
    def raise_unsupported_operation_for_ancilla_semi_quantum_register_error() -> None:
        """
        Return/Raise an Unsupported Operation for Ancilla Semi-Quantum Register Error.

        :raise unsupported_operation_for_ancilla_semi_quantum_register_error: an Unsupported Operation for
                                                                              Ancilla Semi-Quantum Register Error.
        """

        unsupported_operation_for_ancilla_semi_quantum_register_error = \
            QiskryptSemiQuantumRegisterUnsupportedOperationError()
        """
        Retrieve the Unsupported Operation for Ancilla Semi-Quantum Register Error.
        """

        """
        Raise the Unsupported Operation for Ancilla Semi-Quantum Register Error.
        """
        raise unsupported_operation_for_ancilla_semi_quantum_register_error

    @staticmethod
    def raise_invalid_qiskit_classical_register_index_given_error() -> None:
        """
        Return/Raise an Invalid IBM Qiskit's Classical Register Index Given Error.

        :raise invalid_qiskit_classical_register_index_given_error: an Invalid IBM Qiskit's Classical Register
                                                                    Index Given Error.
        """

        invalid_qiskit_classical_register_index_given_error = \
            QiskryptQuantumCircuitInvalidQiskitClassicalRegisterIndexGivenError()
        """
        Retrieve the Invalid IBM Qiskit' Classical Register Index Given Error for the Qiskrypt's Quantum Circuit.
        """

        """
        Raise the Invalid IBM Qiskit's Classical Register Index Given Error for the Qiskrypt's Quantum Circuit.
        """
        raise invalid_qiskit_classical_register_index_given_error

    @staticmethod
    def raise_invalid_bit_index_given_error() -> None:
        """
        Return/Raise an Invalid Bit Index Given Error.

        :raise invalid_bit_index_given_error: an Invalid Bit Index Given Error.
        """

        invalid_bit_index_given_error = QiskryptQuantumCircuitInvalidBitIndexGivenError()
        """
        Retrieve the Invalid Bit Index Given Error for the Qiskrypt's Quantum Circuit.
        """

        """
        Raise the Invalid Bit Index Given Error for the Qiskrypt's Quantum Circuit.
        """
        raise invalid_bit_index_given_error

    @staticmethod
    def raise_register_not_found_error() -> None:
        """
        Return/Raise a Register Not Found Error.

        :raise invalid_bit_index_given_error: an Invalid Bit Index Given Error.
        """

        register_not_found_error = QiskryptQuantumCircuitRegisterNotFoundError()
        """
        Retrieve the Register Not Found Error for the Qiskrypt's Quantum Circuit.
        """

        """
        Raise the Register Not Found Error for the Qiskrypt's Quantum Circuit.
        """
        raise register_not_found_error

    @staticmethod
    def raise_num_quantum_registers_and_num_classical_registers_are_not_equal_for_operation_or_measurement_error() -> None:
        """
        Return/Raise a Number of Quantum Registers and Number of Classical Registers are Not Equal for Operation or Measurement Error.

        :raise num_quantum_registers_and_num_classical_registers_are_not_equal_for_operation_or_measurement_error: a Number of Quantum Registers and
                                                                                                                   Number of Classical Registers are
                                                                                                                   Not Equal for Operation or Measurement Error.
        """

        num_quantum_registers_and_num_classical_registers_are_not_equal_for_operation_or_measurement_error = \
            QiskryptQuantumCircuitNumQuantumRegistersAndNumClassicalRegistersAreNotEqualForOperationOrMeasurementError()
        """
        Retrieve the Number of Quantum Registers and Number of Classical Registers are Not Equal for
        Operation or Measurement Error for the Qiskrypt's Quantum Circuit.
        """

        """
        Raise the Number of Quantum Registers and Number of Classical Registers are Not Equal for
        Operation or Measurement Error for the Qiskrypt's Quantum Circuit.
        """
        raise num_quantum_registers_and_num_classical_registers_are_not_equal_for_operation_or_measurement_error

    @staticmethod
    def raise_num_qubits_and_num_bits_are_not_equal_for_operation_or_measurement_error() -> None:
        """
        Return/Raise a Number of Qubits and Number of Bits are Not Equal for Operation or Measurement Error.

        :raise num_qubits_and_num_bits_are_not_equal_for_operation_or_measurement_error: a Number of Qubits and
                                                                                         Number of Bits are Not Equal for
                                                                                         Operation or Measurement Error.
        """

        num_qubits_and_num_bits_are_not_equal_for_operation_or_measurement_error = \
            QiskryptQuantumCircuitNumQubitsAndNumBitsAreNotEqualForOperationOrMeasurementError()
        """
        Retrieve the Number of Qubits and Number of Bits are Not Equal for
        Operation or Measurement Error for the Qiskrypt's Quantum Circuit.
        """

        """
        Raise the Number of Qubits and Number of Bits are Not Equal for
        Operation or Measurement Error for the Qiskrypt's Quantum Circuit.
        """
        raise num_qubits_and_num_bits_are_not_equal_for_operation_or_measurement_error

    @staticmethod
    def raise_list_do_not_represent_a_square_unitary_matrix_operator_error() -> None:
        """
        Return/Raise a List Do Not Represent a Square Unitary Matrix Operator Error.

        :raise list_do_not_represent_a_square_unitary_matrix_operator_error: a List Do Not Represent
                                                                             a Square Unitary Matrix Operator Error.
        """

        list_do_not_represent_a_square_unitary_matrix_operator_error = \
            QiskryptQuantumCircuitListDoNotRepresentASquareUnitaryMatrixOperatorError()
        """
        Retrieve the List Do Not Represent a Square Unitary Matrix Operator Error for
        the Qiskrypt's Quantum Circuit.
        """

        """
        Raise the List Do Not Represent a Square Unitary Matrix Operator Error for
        the Qiskrypt's Quantum Circuit.
        """
        raise list_do_not_represent_a_square_unitary_matrix_operator_error
