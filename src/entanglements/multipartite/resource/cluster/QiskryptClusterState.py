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

from src.entanglements.multipartite.resource.QiskryptResourceState \
    import QiskryptResourceState
"""
Import the Qiskrypt's Resource State.
"""

from src.circuit.QiskryptQuantumCircuit \
    import QiskryptQuantumCircuit
"""
Import the Qiskrypt's Quantum Circuit.
"""

"""
Import of constants and enumerations.
"""

from src.entanglements.QiskryptQuantumEntanglement \
    import POSSIBLE_CONFIGURATIONS_RESOURCE_STATES
"""
Import the available configurations for the types of
the Qiskrypt's Resource State.
"""


class QiskryptClusterState(QiskryptResourceState):
    """
    Object class for the Qiskrypt's Cluster State.
    """

    def __init__(self, name: str, qiskrypt_quantum_circuit: QiskryptQuantumCircuit):
        """
        Constructor of the Qiskrypt's Cluster State.

        :param name: the name of the Qiskrypt's Cluster State.
        :param qiskrypt_quantum_circuit: the name of the Qiskrypt's Cluster State.
        """

        if qiskrypt_quantum_circuit.get_total_num_qubits() >= 3:
            """
            If the number of qubits of the given Qiskrypt's Quantum Circuit is greater or equal than 3.
            """

            super().__init__(name, qiskrypt_quantum_circuit, POSSIBLE_CONFIGURATIONS_RESOURCE_STATES[1])
            """
            Calls the constructor of the super-class Qiskrypt's Resource State.
            """

    def get_name(self) -> str:
        """
        Return the name of the Qiskrypt's Cluster State.

        :return super().get_name(): the name of the Qiskrypt's Cluster State.
        """

        """
        Return the name of the Qiskrypt's Cluster State.
        """
        return super().get_name()

    def get_quantum_entanglement_cardinality(self) -> str:
        """
        Return the cardinality of the Qiskrypt's Cluster State.

        :return super().get_quantum_entanglement_cardinality(): the cardinality of the Qiskrypt's Cluster State.
        """

        """
        Return the cardinality of the Qiskrypt's Cluster State.
        """
        return super().get_quantum_entanglement_cardinality()

    def get_quantum_entanglement_type(self) -> str:
        """
        Return the type of the Qiskrypt's Cluster State.

        :return super().get_quantum_entanglement_type(): the type of the Qiskrypt's Cluster State.
        """

        """
        Return the type of the Qiskrypt's Cluster State.
        """
        return super().get_quantum_entanglement_type()

    def get_qiskrypt_quantum_circuit(self) -> QiskryptQuantumCircuit:
        """
        Return the Qiskrypt's Quantum Circuit,
        from which it will be configured the Qiskrypt's Cluster State.

        :return super().get_qiskrypt_quantum_circuit(): the Qiskrypt's Quantum Circuit,
                                                        from which it will be configured
                                                        the Qiskrypt's Cluster State.
        """

        """
        Return the Qiskrypt's Quantum Circuit,
        from which it will be configured the Qiskrypt's Cluster State.
        """
        return super().get_qiskrypt_quantum_circuit()

    def get_resource_type(self) -> str:
        """
        Return the resource type of the Qiskrypt's Cluster State.

        :return self.resource_type: the resource type of the Qiskrypt's Cluster State.
        """

        """
        Return the resource type of the Qiskrypt's Cluster State.
        """
        return self.resource_type
