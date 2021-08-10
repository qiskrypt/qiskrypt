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

from src.entanglements.QiskryptQuantumEntanglement \
    import QiskryptQuantumEntanglement
"""
Import the Qiskrypt's Quantum Entanglement.
"""

from src.entanglements.QiskryptQuantumEntanglement \
    import POSSIBLE_QUANTUM_ENTANGLEMENT_CARDINALITIES
"""
Import the available Quantum Entanglement cardinalities for
the Qiskrypt's Quantum Entanglement.
"""

from src.entanglements.QiskryptQuantumEntanglement \
    import POSSIBLE_QUANTUM_ENTANGLEMENT_TYPES
"""
Import the available Quantum Entanglement types for
the Qiskrypt's Quantum Entanglement.
"""

from src.circuit.QiskryptQuantumCircuit \
    import QiskryptQuantumCircuit
"""
Import the Qiskrypt's Quantum Circuit.
"""


class QiskryptWState(QiskryptQuantumEntanglement):
    """
    Object class for the Qiskrypt's W State.
    """

    def __init__(self, name: str, qiskrypt_quantum_circuit: QiskryptQuantumCircuit):
        """
        Constructor of the Qiskrypt's W State.

        :param name: the name of the Qiskrypt's W State.
        :param qiskrypt_quantum_circuit: the name of the Qiskrypt's W State.
        """

        if qiskrypt_quantum_circuit.get_total_num_qubits() >= 3:
            """
            If the number of qubits of
            the given Qiskrypt's Quantum Circuit is greater or equal than 3.
            """

            super().__init__(name, POSSIBLE_QUANTUM_ENTANGLEMENT_CARDINALITIES[1],
                             POSSIBLE_QUANTUM_ENTANGLEMENT_TYPES[2],
                             qiskrypt_quantum_circuit)
            """
            Calls the constructor of the super-class Qiskrypt's Quantum Entanglement.
            """

            self.qiskit_quantum_registers_indexes = None
            """
            Set the index of the IBM Qiskit's Quantum Registers, as None.
            """

            self.qubits_indexes = None
            """
            Set the indexes of the qubits inside the IBM Qiskit's Quantum Registers, as None.
            """

        else:
            """
            If the number of qubits and bits of
            the given Qiskrypt's Quantum Circuit is strictly lower than 3.
            """

            # TODO - Throw Exception

    def get_name(self) -> str:
        """
        Return the name of the Qiskrypt's W State.

        :return super().get_name(): the name of the Qiskrypt's W State.
        """

        """
        Return the name of the Qiskrypt's W State.
        """
        return super().get_name()

    def get_quantum_entanglement_cardinality(self) -> str:
        """
        Return the cardinality of the Qiskrypt's W State.

        :return super().get_quantum_entanglement_cardinality(): the cardinality of
                                                                the Qiskrypt's W State.
        """

        """
        Return the cardinality of the Qiskrypt's W State.
        """
        return super().get_quantum_entanglement_cardinality()

    def get_quantum_entanglement_type(self) -> str:
        """
        Return the type of the Qiskrypt's W State.

        :return super().get_quantum_entanglement_type(): the type of the Qiskrypt's W State.
        """

        """
        Return the type of the Qiskrypt's W State.
        """
        return super().get_quantum_entanglement_type()

    def get_qiskrypt_quantum_circuit(self) -> QiskryptQuantumCircuit:
        """
        Return the Qiskrypt's Quantum Circuit,
        from which it will be configured the Qiskrypt's W State.

        :return super().get_qiskrypt_quantum_circuit(): the Qiskrypt's Quantum Circuit,
                                                        from which it will be configured
                                                        the Qiskrypt's W State.
        """

        """
        Return the Qiskrypt's Quantum Circuit,
        from which it will be configured the Qiskrypt's W State.
        """
        return super().get_qiskrypt_quantum_circuit()

    def get_qiskit_quantum_registers_indexes(self) -> int:
        """
        Return the indexes of the IBM Qiskit's Quantum Registers of the Qiskrypt's W State.

        :return self.qiskit_quantum_registers_indexes: the indexes of the
                                                       IBM Qiskit's Quantum Register of
                                                       the Qiskrypt's W State.
        """

        """
        Return the indexes of the IBM Qiskit's Quantum Registers of the Qiskrypt's W State.
        """
        return self.qiskit_quantum_registers_indexes

    def get_qubits_indexes(self) -> list:
        """
        Return the indexes of the qubits inside the IBM Qiskit's Quantum Registers of the Qiskrypt's W State.

        :return self.qubits_indexes: the indexes of the qubits inside
                                     the IBM Qiskit's Quantum Registers of
                                     the Qiskrypt's W State.
        """

        """
        Return the indexes of the qubits inside the IBM Qiskit's Quantum Registers of the Qiskrypt's W State.
        """
        return self.qubits_indexes

    def configure(self, qiskit_quantum_registers_indexes: list, qubits_indexes: list) -> None:
        """
        Configure the Qiskrypt's W State,
        regarding its IBM Qiskit's Quantum Registers and respective qubits.

        :param qiskit_quantum_registers_indexes: the indexes of the IBM Qiskit's Quantum Registers.
        :param qubits_indexes: the indexes of qubits inside the IBM Qiskit's Quantum Registers.
        """

        self.qiskit_quantum_registers_indexes = qiskit_quantum_registers_indexes
        """
        Set the indexes of the IBM Qiskit's Quantum Registers, as the given indexes for it.
        """

        self.qubits_indexes = qubits_indexes
        """
        Set the indexes of the qubits inside the IBM Qiskit's Quantum Registers,
        as the given indexes for it.
        """
