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
- NOVA LINCS, Portugal.
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

from src.quantum_regime.entanglements.multipartite.resource.QiskryptResourceState \
    import QiskryptResourceState
"""
Import the Qiskrypt's Resource State.
"""

from src.quantum_regime.circuit.QiskryptQuantumCircuit \
    import QiskryptQuantumCircuit
"""
Import the Qiskrypt's Quantum Circuit.
"""

from src.quantum_regime.transforms.hadamard.QiskryptQuantumHadamardTransform \
    import QiskryptQuantumHadamardTransform
"""
Import the Qiskrypt's Quantum Hadamard Transform.
"""


"""
Import of constants and enumerations.
"""

from src.quantum_regime.entanglements.QiskryptQuantumEntanglement \
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

        if qiskrypt_quantum_circuit.get_total_num_qubits() >= 1:
            """
            If the number of qubits of
            the given Qiskrypt's Quantum Circuit is greater or equal than 1.
            """

            super().__init__(name, qiskrypt_quantum_circuit, POSSIBLE_CONFIGURATIONS_RESOURCE_STATES[1])
            """
            Call of the constructor of the super-class Qiskrypt's Resource State.
            """

            self.qiskit_quantum_registers_indexes = None
            """
            Set the indexes of the IBM Qiskit's Quantum Registers, associated to the Cluster State itself,
            as the given indexes for it, as None.
            """

            self.qubits_vertices_indexes = None
            """
            Set the indexes of the qubits inside the IBM Qiskit's Quantum Register,
            representing the vertices of the Cluster State, as the given indexes for it, as None.
            """

        else:
            """
            If the number of qubits of
            the given Qiskrypt's Quantum Circuit is strictly lower than 1.
            """

            # TODO - Throw Exception

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

    def configure(self, qiskit_quantum_registers_indexes: list,
                  qubits_vertices_indexes: list) -> None:
        """
        Configure the Qiskrypt's Cluster State,
        regarding its IBM Qiskit's Quantum Registers and
        the qubits representing the vertices of the Cluster State, being ordered.

        :param qiskit_quantum_registers_indexes: the indexes of the IBM Qiskit's Quantum Registers,
                                                 associated to the Cluster State itself.
        :param qubits_vertices_indexes: the indexes of the qubits inside the IBM Qiskit's Quantum Register,
                                        representing the vertices of the Cluster State.
        """

        self.qiskit_quantum_registers_indexes = qiskit_quantum_registers_indexes
        """
        Set the indexes of the IBM Qiskit's Quantum Registers, associated to the Cluster State itself,
        as the given indexes for it.
        """

        self.qubits_vertices_indexes = qubits_vertices_indexes
        """
        Set the indexes of the qubits inside the IBM Qiskit's Quantum Register,
        representing the vertices of the Cluster State, as the given indexes for it.
        """

    def prepare_multipartite_entanglement_at_computational_basis(self, is_to_measure_at_computational_basis=False,
                                                                 qiskit_classical_registers_indexes=None,
                                                                 bits_vertices_indexes=None) -> None:
        """
        Prepare the Multipartite Quantum Entanglement,
        for the specified Qiskrypt's Cluster State, as a Quantum Entangled State,
        or even, apply also the measurement of that Quantum Entangled State, on the Computational Basis,
        to allow the extraction of its final classical outcome/result.

        :param is_to_measure_at_computational_basis: the boolean flag to keep the information about
                                                     if it will be performed a measurement of
                                                     the Qiskrypt's Cluster State on the Computational Basis.
        :param qiskit_classical_registers_indexes: the indexes of the IBM Qiskit's Classical Registers,
                                                   where it belongs the bits to store the final classical outcomes/results,
                                                   after be performed a measurement on the qubits inside
                                                   the IBM Qiskit's Quantum Registers,
                                                   associated to the Cluster State itself.
        :param bits_vertices_indexes: the indexes of the bits inside the IBM Qiskit's Classical Registers,
                                      where it will be stored the final classical outcomes/results,
                                      after be performed a measurement on the qubits inside
                                      the IBM Qiskit's Quantum Registers,
                                      representing the vertices of the Cluster State.
        """

        self.qiskrypt_quantum_circuit \
            .apply_barriers_set_qubits_in_set_qiskit_quantum_registers(self.qiskit_quantum_registers_indexes,
                                                                       self.qubits_vertices_indexes)
        """
        Apply barriers to the IBM Qiskit's Quantum Registers, associated to the Cluster State itself and
        the respective qubits, representing the vertices of the Cluster State.
        """

        qiskrypt_quantum_hadamard_transform_cluster_state = \
            QiskryptQuantumHadamardTransform("hadamard_transform_cluster_state",
                                             self.qiskrypt_quantum_circuit,
                                             self.qiskit_quantum_registers_indexes,
                                             self.qubits_vertices_indexes)
        """
        Create the Qiskrypt's Quantum Hadamard Transform, for the Qiskrypt's Quantum Register and qubits involved.
        """

        qiskrypt_quantum_hadamard_transform_cluster_state.apply_transform()
        """
        Apply the Quantum Hadamard Transform to the Qiskrypt's Quantum Registers and qubits,
        involved on the Qiskrypt's Cluster State.
        """

        self.qiskrypt_quantum_circuit = \
            qiskrypt_quantum_hadamard_transform_cluster_state.get_qiskrypt_quantum_circuit()
        """
        Update the Qiskrypt's Quantum Circuit for the Cluster State,
        from the previously created Qiskrypt's Quantum Hadamard Transform.
        """

        num_quantum_registers = len(self.qiskit_quantum_registers_indexes)
        """
        Retrieve the number of the IBM Qiskit's Quantum Registers for the Qiskrypt's Cluster State.
        """

        num_qubits_vertices = len(self.qubits_vertices_indexes)
        """
        Retrieve the number of qubits for the Qiskrypt's Cluster State, representing its vertices.
        """

        for qiskit_quantum_register_index, qubit_vertex_index in \
                zip(range((num_quantum_registers - 1)), range((num_qubits_vertices - 1))):
            """
            For each pair of indexes for an IBM Qiskit's Quantum Register and a qubit,
            representing a vertex of the Qiskrypt's Cluster State. 
            """

            self.qiskrypt_quantum_circuit\
                .apply_controlled_pauli_z(self.qiskit_quantum_registers_indexes[qiskit_quantum_register_index],
                                          self.qiskit_quantum_registers_indexes[(qiskit_quantum_register_index + 1)],
                                          self.qubits_vertices_indexes[qubit_vertex_index],
                                          self.qubits_vertices_indexes[(qubit_vertex_index + 1)])
            """
            Apply the Controlled-Pauli-Z (Controlled-Phase-Flip/Controlled-Phase-Shifter) Gate/Operation to
            the indexes of the current IBM Qiskit's Quantum Register and the respective qubit on it, as also,
            of the next IBM Qiskit's Quantum Register and the current respective qubit on it.
            """

        self.qiskrypt_quantum_circuit \
            .apply_controlled_pauli_z(self.qiskit_quantum_registers_indexes[0],
                                      self.qiskit_quantum_registers_indexes[(num_quantum_registers - 1)],
                                      self.qubits_vertices_indexes[0],
                                      self.qubits_vertices_indexes[(num_qubits_vertices - 1)])
        """
        Apply the Controlled-Pauli-Z (Controlled-Phase-Flip/Controlled-Phase-Shifter) Gate/Operation to
        the indexes of the first IBM Qiskit's Quantum Register and the respective qubit on it, as also,
        of the last IBM Qiskit's Quantum Register and the current respective qubit on it.
        """

        self.qiskrypt_quantum_circuit \
            .apply_barriers_set_qubits_in_set_qiskit_quantum_registers(self.qiskit_quantum_registers_indexes,
                                                                       self.qubits_vertices_indexes)
        """
        Apply barriers to the IBM Qiskit's Quantum Registers, associated to the Cluster State itself and
        the respective qubits, representing the vertices of the Cluster State.
        """

        if is_to_measure_at_computational_basis:
            """
            If the boolean flag to keep the information about
            if it will be performed a measurement of
            the Qiskrypt's Cluster State on the Computational Basis, is True.
            """

            if self.qiskrypt_quantum_circuit.get_total_num_bits() >= len(bits_vertices_indexes):
                """
                If the number of bits of the given Qiskrypt's Quantum Circuit is greater or equal than
                the number of the bits inside the IBM Qiskit's Classical Registers,
                representing the vertices of the Cluster State.
                """

                self.qiskrypt_quantum_circuit\
                    .measure_set_qubits_in_set_qiskit_quantum_registers(self.qiskit_quantum_registers_indexes,
                                                                        qiskit_classical_registers_indexes,
                                                                        self.qubits_vertices_indexes,
                                                                        bits_vertices_indexes)
                """
                Measure the qubits in the IBM Qiskit's Quantum Registers into
                the respective bits in the IBM Qiskit's Classical Registers,
                inside the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit.
                """

            else:
                """
                If the number of bits of the given Qiskrypt's Quantum Circuit is lower than
                the number of the bits inside the IBM Qiskit's Classical Registers,
                representing the vertices of the Cluster State.
                """

                # TODO - Throw Exception

    def prepare_multipartite_entanglement_at_cluster_state_basis(self, is_to_measure_at_cluster_state_basis=False,
                                                                 qiskit_classical_registers_indexes=None,
                                                                 bits_vertices_indexes=None) -> None:
        """
        Prepare the Multipartite Quantum Entanglement,
        for the specified Qiskrypt's Cluster State, as a Quantum Entangled State,
        or even, apply also the measurement of that Quantum Entangled State, on the Cluster State Basis,
        to allow the extraction of its final classical outcome/result.

        :param is_to_measure_at_cluster_state_basis: the boolean flag to keep the information about
                                                     if it will be performed a measurement of
                                                     the Qiskrypt's Cluster State on the Cluster State Basis.
        :param qiskit_classical_registers_indexes: the indexes of the target IBM Qiskit's Classical Registers,
                                                   where it belongs the bits to store the final classical outcomes/results,
                                                   after be performed a measurement on the qubits inside
                                                   the target IBM Qiskit's Quantum Registers.
        :param bits_vertices_indexes: the indexes of the bits inside the target IBM Qiskit's Classical Registers,
                                      where it will be stored the final classical outcomes/results,
                                      after be performed a measurement on the qubits inside
                                      the target IBM Qiskit's Quantum Registers.
        """

        self.qiskrypt_quantum_circuit \
            .apply_barriers_set_qubits_in_set_qiskit_quantum_registers(self.qiskit_quantum_registers_indexes,
                                                                       self.qubits_vertices_indexes)
        """
        Apply barriers to the IBM Qiskit's Quantum Registers, associated to the Cluster State itself and
        the respective qubits, representing the vertices of the Cluster State.
        """

        num_quantum_registers = len(self.qiskit_quantum_registers_indexes)
        """
        Retrieve the number of the IBM Qiskit's Quantum Registers for the Qiskrypt's Cluster State.
        """

        num_qubits_vertices = len(self.qubits_vertices_indexes)
        """
        Retrieve the number of qubits for the Qiskrypt's Cluster State, representing its vertices.
        """

        self.qiskrypt_quantum_circuit \
            .apply_controlled_pauli_z(self.qiskit_quantum_registers_indexes[0],
                                      self.qiskit_quantum_registers_indexes[(num_quantum_registers - 1)],
                                      self.qubits_vertices_indexes[0],
                                      self.qubits_vertices_indexes[(num_qubits_vertices - 1)])
        """
        Apply the Controlled-Pauli-Z (Controlled-Phase-Flip/Controlled-Phase-Shifter) Gate/Operation to
        the indexes of the first IBM Qiskit's Quantum Register and the respective qubit on it, as also,
        of the last IBM Qiskit's Quantum Register and the current respective qubit on it.
        """

        qiskit_quantum_registers_indexes_reversed = self.qiskit_quantum_registers_indexes.copy()
        """
        Create a copy of the list of indexes of the IBM Qiskit's Quantum Registers, for its own reversal.
        """

        qubits_vertices_indexes_reversed = self.qubits_vertices_indexes.copy()
        """
        Create a copy of the list of indexes of the qubits,
        representing the vertices of the Cluster State, for its own reversal.
        """

        qiskit_quantum_registers_indexes_reversed.reverse()
        """
        Reverse the list of indexes of the IBM Qiskit's Quantum Registers.
        """

        qubits_vertices_indexes_reversed.reverse()
        """
        Reverse the list of indexes of the qubits, representing the vertices of the Cluster State.
        """

        for qiskit_quantum_register_index, qubit_vertex_index in \
                zip(range((num_quantum_registers - 1)), range((num_qubits_vertices - 1))):
            """
            For each pair of indexes for an IBM Qiskit's Quantum Register and a qubit,
            representing a vertex of the Qiskrypt's Cluster State. 
            """

            self.qiskrypt_quantum_circuit \
                .apply_controlled_pauli_z(qiskit_quantum_registers_indexes_reversed[(qiskit_quantum_register_index + 1)],
                                          qiskit_quantum_registers_indexes_reversed[qiskit_quantum_register_index],
                                          qubits_vertices_indexes_reversed[(qubit_vertex_index + 1)],
                                          qubits_vertices_indexes_reversed[qubit_vertex_index])
            """
            Apply the Controlled-Pauli-Z (Controlled-Phase-Flip/Controlled-Phase-Shifter) Gate/Operation to
            the indexes of the current IBM Qiskit's Quantum Register and the respective qubit on it, as also,
            of the next IBM Qiskit's Quantum Register and the current respective qubit on it.
            """

        qiskrypt_quantum_hadamard_transform_cluster_state = \
            QiskryptQuantumHadamardTransform("hadamard_transform_cluster_state",
                                             self.qiskrypt_quantum_circuit,
                                             self.qiskit_quantum_registers_indexes,
                                             self.qubits_vertices_indexes)
        """
        Create the Qiskrypt's Quantum Hadamard Transform, for the Qiskrypt's Quantum Register and qubits involved.
        """

        qiskrypt_quantum_hadamard_transform_cluster_state.apply_transform()
        """
        Apply the Quantum Hadamard Transform to the Qiskrypt's Quantum Registers and qubits,
        involved on the Qiskrypt's Cluster State.
        """

        self.qiskrypt_quantum_circuit = \
            qiskrypt_quantum_hadamard_transform_cluster_state.get_qiskrypt_quantum_circuit()
        """
        Update the Qiskrypt's Quantum Circuit for the Cluster State,
        from the previously created Qiskrypt's Quantum Hadamard Transform.
        """

        self.qiskrypt_quantum_circuit \
            .apply_barriers_set_qubits_in_set_qiskit_quantum_registers(self.qiskit_quantum_registers_indexes,
                                                                       self.qubits_vertices_indexes)
        """
        Apply barriers to the IBM Qiskit's Quantum Registers, associated to the Cluster State itself and
        the respective qubits, representing the vertices of the Cluster State.
        """

        if is_to_measure_at_cluster_state_basis:
            """
            If the boolean flag to keep the information about
            if it will be performed a measurement of
            the Qiskrypt's Cluster State on the Cluster State Basis, is True.
            """

            if self.qiskrypt_quantum_circuit.get_total_num_bits() >= len(bits_vertices_indexes):
                """
                If the number of bits of the given Qiskrypt's Quantum Circuit is greater or equal than
                the number of the bits inside the IBM Qiskit's Classical Registers,
                representing the vertices of the Cluster State.
                """

                self.qiskrypt_quantum_circuit \
                    .measure_set_qubits_in_set_qiskit_quantum_registers(self.qiskit_quantum_registers_indexes,
                                                                        qiskit_classical_registers_indexes,
                                                                        self.qubits_vertices_indexes,
                                                                        bits_vertices_indexes)
                """
                Measure the qubits in the IBM Qiskit's Quantum Registers into
                the respective bits in the IBM Qiskit's Classical Registers,
                inside the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit.
                """

            else:
                """
                If the number of bits of the given Qiskrypt's Quantum Circuit is lower than
                the number of the bits inside the IBM Qiskit's Classical Registers,
                representing the vertices of the Cluster State.
                """

                # TODO - Throw Exception
