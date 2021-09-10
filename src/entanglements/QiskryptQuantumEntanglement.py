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
- Prof. Antonio Ravara (NOVA School of Science and Technology, NOVA University of Lisbon, Portugal).

"""

"""
Import required Libraries and Packages.
"""

from src.circuit.QiskryptQuantumCircuit \
    import QiskryptQuantumCircuit
"""
Import the Qiskrypt's Quantum Circuit.
"""

"""
Definition of Constants and Enumerations.
"""

POSSIBLE_QUANTUM_ENTANGLEMENT_CARDINALITIES = ["BIPARTITE", "MULTIPARTITE"]
"""
The available Quantum Entanglement cardinalities for
the Qiskrypt's Quantum Entanglement.
"""

POSSIBLE_QUANTUM_ENTANGLEMENT_TYPES = ["BELL_STATE", "GHZ_STATE", "W_STATE", "GHZ_LIKE",
                                       "DICKE_STATE", "RESOURCE_STATE", "WERNER_STATE"]
"""
The available Quantum Entanglement types for
the Qiskrypt's Quantum Entanglement.
"""

POSSIBLE_CONFIGURATIONS_BELL_STATES = ["EPR_PAIR_STATE", "BELL_STATE_PHI_PLUS", "BELL_STATE_PHI_MINUS",
                                       "BELL_STATE_PSI_PLUS", "BELL_STATE_PSI_MINUS"]
"""
The available configurations for Bell States for
the Qiskrypt's Quantum Entanglement.
"""

POSSIBLE_CONFIGURATIONS_RESOURCE_STATES = ["GRAPH_STATE", "CLUSTER_STATE"]
"""
The available configurations for Resource States for
the Qiskrypt's Quantum Entanglement.
"""


class QiskryptQuantumEntanglement:
    """
    Object class for the Qiskrypt's Quantum Entanglement.
    """

    def __init__(self, name: str, quantum_entanglement_cardinality: str, quantum_entanglement_type: str,
                 qiskrypt_quantum_circuit: QiskryptQuantumCircuit, bell_state_sub_type=None):
        """
        Constructor of the Qiskrypt's Quantum Entanglement.

        :param name: the name of the Qiskrypt's Quantum Entanglement.
        :param quantum_entanglement_cardinality: the cardinality of the Qiskrypt's Quantum Entanglement.
        :param quantum_entanglement_type: the type of the Qiskrypt's Quantum Entanglement.
        :param qiskrypt_quantum_circuit: the Qiskrypt's Quantum Circuit,
                                         from which it will be configured
                                         the Qiskrypt's Quantum Entanglement.
        :param bell_state_sub_type: the sub-type of the Qiskrypt's Quantum Entanglement,
                                    for the case of be a Bell State.
        """

        if quantum_entanglement_cardinality in POSSIBLE_QUANTUM_ENTANGLEMENT_CARDINALITIES:
            """
            If the given cardinality of the Qiskrypt's Quantum Entanglement is valid.
            """

            if quantum_entanglement_type in POSSIBLE_QUANTUM_ENTANGLEMENT_TYPES:
                """
                If the given type of the Qiskrypt's Quantum Entanglement is valid.
                """

                self.name = name
                """
                Se the name of the name of the Qiskrypt's Quantum Entanglement.
                """

                self.quantum_entanglement_cardinality = quantum_entanglement_cardinality
                """
                Set the cardinality of the Qiskrypt's Quantum Entanglement.
                """

                self.quantum_entanglement_type = quantum_entanglement_type
                """
                Set the type of the Qiskrypt's Quantum Entanglement.
                """

                self.qiskrypt_quantum_circuit = qiskrypt_quantum_circuit
                """
                Set the Qiskrypt's Quantum Circuit,
                from which it will be configured the Qiskrypt's Quantum Entanglement.
                """

                if quantum_entanglement_type == POSSIBLE_QUANTUM_ENTANGLEMENT_TYPES[0]:
                    """
                    If the Qiskrypt's Quantum Entanglement is a valid Bell State.
                    """

                    if bell_state_sub_type in POSSIBLE_CONFIGURATIONS_BELL_STATES:
                        """
                        If the sub-type of the Qiskrypt's Quantum Entanglement,
                        for the case of be a Bell State, is valid.
                        """

                        self.bell_state_sub_type = bell_state_sub_type
                        """
                        Set the sub-type of the Qiskrypt's Quantum Entanglement,
                        for the case of be a Bell State, as the given sub-type.
                        """

                    else:
                        """
                        If the sub-type of the Qiskrypt's Quantum Entanglement,
                        for the case of be a Bell State, is valid.
                        """

                        # TODO - Throw Exception

                else:
                    """
                    If the Qiskrypt's Quantum Entanglement is not a valid Bell State.
                    """

                    self.bell_state_sub_type = None
                    """
                    Set the sub-type of the Qiskrypt's Quantum Entanglement,
                    for the case of be a Bell State, as None.
                    """

            else:
                """
                If the given type of the Qiskrypt's Quantum Entanglement is not valid.
                """

                # TODO Throw - Exception

        else:
            """
            If the given cardinality of the Qiskrypt's Quantum Entanglement is not valid.
            """

            # TODO Throw - Exception

    def get_name(self):
        """
        Return the name of the Qiskrypt's Quantum Entanglement.

        :return self.name: the name of the Qiskrypt's Quantum Entanglement.
        """

        """
        Return the name of the Qiskrypt's Quantum Entanglement.
        """
        return self.name

    def get_quantum_entanglement_cardinality(self):
        """
        Return the cardinality of the Qiskrypt's Quantum Entanglement.

        :return self.quantum_entanglement_cardinality: the cardinality of
                                                       the Qiskrypt's Quantum Entanglement.
        """

        """
        Return the cardinality of the Qiskrypt's Quantum Entanglement.
        """
        return self.quantum_entanglement_cardinality

    def get_quantum_entanglement_type(self):
        """
        Return the type of the Qiskrypt's Quantum Entanglement.

        :return self.quantum_entanglement_type: the type of the Qiskrypt's Quantum Entanglement.
        """

        """
        Return the type of the Qiskrypt's Quantum Entanglement.
        """
        return self.quantum_entanglement_type

    def get_qiskrypt_quantum_circuit(self):
        """
        Return the Qiskrypt's Quantum Circuit,
        from which it will be configured the Qiskrypt's Quantum Entanglement.

        :return self.qiskrypt_quantum_circuit: the Qiskrypt's Quantum Circuit,
                                               from which it will be configured
                                               the Qiskrypt's Quantum Entanglement.
        """

        """
        Return the Qiskrypt's Quantum Circuit,
        from which it will be configured the Qiskrypt's Quantum Entanglement.
        """
        return self.qiskrypt_quantum_circuit

    def get_bell_state_sub_type(self):
        """
        Return the sub-type of the Qiskrypt's Quantum Entanglement,
        for the case of be a Bell State.

        :return self.bell_state_sub_type: the sub-type of the Qiskrypt's Quantum Entanglement,
                                          for the case of be a Bell State.
        """

        """
        Return the sub-type of the Qiskrypt's Quantum Entanglement,
        for the case of be a Bell State.
        """
        return self.bell_state_sub_type
