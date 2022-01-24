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

from src.quantum_regime.entanglements.QiskryptQuantumEntanglement \
    import QiskryptQuantumEntanglement
"""
Import the Qiskrypt's Quantum Entanglement.
"""

from src.quantum_regime.circuit.QiskryptQuantumCircuit \
    import QiskryptQuantumCircuit
"""
Import the Qiskrypt's Quantum Circuit.
"""

"""
Import of constants and enumerations.
"""

from src.quantum_regime.entanglements.QiskryptQuantumEntanglement \
    import POSSIBLE_QUANTUM_ENTANGLEMENT_CARDINALITIES
"""
Import the available Quantum Entanglement cardinalities for
the Qiskrypt's Quantum Entanglement.
"""

from src.quantum_regime.entanglements.QiskryptQuantumEntanglement \
    import POSSIBLE_QUANTUM_ENTANGLEMENT_TYPES
"""
Import the available Quantum Entanglement types for
the Qiskrypt's Quantum Entanglement.
"""

from src.quantum_regime.entanglements.QiskryptQuantumEntanglement \
    import POSSIBLE_CONFIGURATIONS_RESOURCE_STATES
"""
Import the available configurations for the types of
the Qiskrypt's Resource State.
"""


class QiskryptResourceState(QiskryptQuantumEntanglement):
    """
    Object class for the Qiskrypt's Resource State.
    """

    def __init__(self, name: str, qiskrypt_quantum_circuit: QiskryptQuantumCircuit, resource_type: str):
        """
        Constructor of the Qiskrypt's Resource State.

        :param name: the name of the Qiskrypt's Resource State.
        :param qiskrypt_quantum_circuit: the name of the Qiskrypt's Resource State.
        :param resource_type: the resource type (i.e., Graph or Cluster) for
                              the Qiskrypt's Resource State.
        """

        if qiskrypt_quantum_circuit.get_total_num_qubits() >= 3:
            """
            If the number of qubits of
            the given Qiskrypt's Quantum Circuit is greater or equal than 3.
            """

            if resource_type in POSSIBLE_CONFIGURATIONS_RESOURCE_STATES:
                """
                If the given resource type of the Qiskrypt's Resource State is valid.
                """

                super().__init__(name, POSSIBLE_QUANTUM_ENTANGLEMENT_CARDINALITIES[1],
                                 POSSIBLE_QUANTUM_ENTANGLEMENT_TYPES[5],
                                 qiskrypt_quantum_circuit)
                """
                Call of the constructor of the super-class Qiskrypt's Quantum Entanglement.
                """

                self.resource_type = resource_type
                """
                Set the resource type of the Qiskrypt's Resource State.
                """

        else:
            """
            If the number of qubits and bits of
            the given Qiskrypt's Quantum Circuit is strictly lower than 3.
            """

            # TODO - Throw Exception

    def get_name(self) -> str:
        """
        Return the name of the Qiskrypt's Resource State.

        :return super().get_name(): the name of the Qiskrypt's Resource State.
        """

        """
        Return the name of the Qiskrypt's Resource State.
        """
        return super().get_name()

    def get_quantum_entanglement_cardinality(self) -> str:
        """
        Return the cardinality of the Qiskrypt's Resource State.

        :return super().get_quantum_entanglement_cardinality(): the cardinality of
                                                                the Qiskrypt's Resource State.
        """

        """
        Return the cardinality of the Qiskrypt's Resource State.
        """
        return super().get_quantum_entanglement_cardinality()

    def get_quantum_entanglement_type(self) -> str:
        """
        Return the type of the Qiskrypt's Resource State.

        :return super().get_quantum_entanglement_type(): the type of the Qiskrypt's Resource State.
        """

        """
        Return the type of the Qiskrypt's Resource State.
        """
        return super().get_quantum_entanglement_type()

    def get_qiskrypt_quantum_circuit(self) -> QiskryptQuantumCircuit:
        """
        Return the Qiskrypt's Quantum Circuit,
        from which it will be configured the Qiskrypt's Resource State.

        :return super().get_qiskrypt_quantum_circuit(): the Qiskrypt's Quantum Circuit,
                                                        from which it will be configured
                                                        the Qiskrypt's Resource State.
        """

        """
        Return the Qiskrypt's Quantum Circuit,
        from which it will be configured the Qiskrypt's Resource State.
        """
        return super().get_qiskrypt_quantum_circuit()

    def get_resource_type(self) -> str:
        """
        Return the resource type of the Qiskrypt's Resource State.

        :return self.resource_type: the resource type of the Qiskrypt's Resource State.
        """

        """
        Return the resource type of the Qiskrypt's Resource State.
        """
        return self.resource_type
