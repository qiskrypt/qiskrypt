"""

Copyrights:\n
- © Qiskrypt, 2022 - All rights reserved.\n

Powered by:\n
- IBM
- IBM Quantum
- IBM Qiskit


Description:\n
- The Qiskrypt is a software suite of protocols of
  quantum_regime cryptography, quantum_regime communication and
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

from src.quantum_regime.transforms.pauli.QiskryptQuantumPauliTransform \
    import QiskryptQuantumPauliTransform
"""
Import the Qiskrypt's Quantum Pauli Transform.
"""

from src.quantum_regime.circuit.QiskryptQuantumCircuit import QiskryptQuantumCircuit
"""
Import the Qiskrypt's Quantum Circuit.
"""


class QiskryptQuantumPauliYTransform(QiskryptQuantumPauliTransform):
    """
    Object class for the Qiskrypt's Quantum Pauli-Y Transform.
    """

    def __init__(self, name: str, qiskrypt_quantum_circuit: QiskryptQuantumCircuit,
                 qiskit_quantum_registers_indexes: list, qubits_indexes: list):
        """
        Constructor of the Qiskrypt's Quantum Pauli-Y Transform.

        :param name: the name for the Qiskrypt's Quantum Pauli-Y Transform.
        :param qiskrypt_quantum_circuit: the Qiskrypt's Quantum Circuit of the Qiskrypt's Quantum Pauli-Y Transform.
        :param qiskit_quantum_registers_indexes: the indexes of the IBM Qiskit's Quantum Registers,
                                                 involved in the Qiskrypt's Quantum Pauli-Y Transform.
        :param qubits_indexes: the indexes of the qubits in the IBM Qiskit's Quantum Registers,
                               to which will be applied the Pauli-Y Gates/Operations,
                               involved in the Qiskrypt's Quantum Pauli-Y Transform.
        """

        super().__init__(name, qiskrypt_quantum_circuit, qiskit_quantum_registers_indexes, qubits_indexes)
        """
        Calls the constructor of the super-class Qiskrypt's Quantum Pauli Transform.
        """

    def get_name(self) -> str:
        """
        Return the name for the Qiskrypt's Quantum Pauli Transform.

        :return super().get_name(): the name for the Qiskrypt's Quantum Pauli Transform.
        """

        """
        Return the name for the Qiskrypt's Quantum Pauli Transform.
        """
        return super().get_name()

    def get_qiskrypt_quantum_circuit(self) -> QiskryptQuantumCircuit:
        """
        Return the Qiskrypt's Quantum Circuit of the Qiskrypt's Quantum Pauli Transform.

        :return super().get_qiskrypt_quantum_circuit(): the Qiskrypt's Quantum Circuit of
                                                        the Qiskrypt's Quantum Pauli Transform.
        """

        """
        Return the Qiskrypt's Quantum Circuit of the Qiskrypt's Quantum Pauli Transform.
        """
        return super().get_qiskrypt_quantum_circuit()

    def get_qiskit_quantum_registers_indexes(self) -> list:
        """
        Return the indexes of the IBM Qiskit's Quantum Registers,
        involved in the Qiskrypt's Quantum Pauli Transform.

        :return super().get_qiskit_quantum_registers_indexes(): the indexes of the IBM Qiskit's Quantum Registers,
                                                                involved in the Qiskrypt's Quantum Pauli Transform.
        """

        """
        Return the indexes of the IBM Qiskit's Quantum Registers,
        involved in the Qiskrypt's Quantum Pauli Transform.
        """
        return super().get_qiskit_quantum_registers_indexes()

    def get_qubits_indexes(self) -> list:
        """
        Return the indexes of the qubits in the IBM Qiskit's Quantum Registers,
        to which will be applied the Pauli Gates/Operations,
        involved in the Qiskrypt's Quantum Pauli Transform.

        :return super().get_qubits_indexes(): the indexes of the qubits in the IBM Qiskit's Quantum Registers,
                                              to which will be applied the Pauli Gates/Operations,
                                              involved in the Qiskrypt's Quantum Pauli Transform.
        """

        """
        Return the indexes of the qubits in the IBM Qiskit's Quantum Registers,
        to which will be applied the Pauli Gates/Operations,
        involved in the Qiskrypt's Quantum Pauli Transform.
        """
        return super().get_qubits_indexes()

    def apply_transform(self) -> None:
        """
        Apply the Qiskrypt's Quantum Pauli-Y Transform,
        to the specified indexes of qubits in the also specified indexes of
        IBM Qiskit's Quantum Registers.
        """

        for qiskit_quantum_register_index, qubit_index \
            in zip(self.qiskit_quantum_registers_indexes, self.qubits_indexes):
            """
            For each pair of indexes of IBM Qiskit's Quantum Registers and qubits.
            """

            is_possible_to_apply_operation = self.qiskrypt_quantum_circuit\
                .check_if_is_possible_to_apply_operation(qiskit_quantum_register_index,
                                                         qubit_index, True)
            """
            Check if it is possible to apply a specific Operation,
            regarding the current IBM Qiskit's Quantum Register index and the current qubit index.
            """

            if is_possible_to_apply_operation:
                """
                If is really possible to apply a specific Operation,
                regarding the current IBM Qiskit's Quantum Register index and the current qubit index.
                """

                self.qiskrypt_quantum_circuit.apply_pauli_y(qiskit_quantum_register_index, qubit_index)
                """
                Apply the Pauli-Y Gate/Operation to
                the current pair of indexes of IBM Qiskit's Quantum Registers and qubits.
                """
