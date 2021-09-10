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

from src.transforms.hadamard.QiskryptQuantumHadamardTransform \
    import QiskryptQuantumHadamardTransform
"""
Import the Qiskrypt's Quantum Hadamard Transform.
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


class QiskryptGraphState(QiskryptResourceState):
    """
    Object class for the Qiskrypt's Graph State.
    """

    def __init__(self, name: str, qiskrypt_quantum_circuit: QiskryptQuantumCircuit):
        """
        Constructor of the Qiskrypt's Graph State.

        :param name: the name of the Qiskrypt's Graph State.
        :param qiskrypt_quantum_circuit: the name of the Qiskrypt's Graph State.
        """

        if qiskrypt_quantum_circuit.get_total_num_qubits() >= 1 and \
                qiskrypt_quantum_circuit.get_total_num_bits() >= 1:
            """
            If the number of qubits and bits of the given Qiskrypt's Quantum Circuit is greater or equal than 1.
            """

            super().__init__(name, qiskrypt_quantum_circuit, POSSIBLE_CONFIGURATIONS_RESOURCE_STATES[0])
            """
            Calls the constructor of the super-class Qiskrypt's Resource State.
            """

            self.qiskit_quantum_registers_indexes = None
            """
            Set the indexes of the IBM Qiskit's Quantum Registers, associated to the Graph State itself,
            as the given indexes for it, as None.
            """

            self.qubits_vertices_indexes = None
            """
            Set the indexes of the qubits inside the IBM Qiskit's Quantum Register,
            representing the vertices of the Graph State, as the given indexes for it, as None.
            """

            self.qubits_pairs_edges_indexes = None
            """
            Set the the pairs of indexes of the qubits inside the IBM Qiskit's Quantum Registers,
            as well, the IBM Qiskit's Quantum Registers themselves,
            representing the edges of the Graph State, as the given indexes for it, as None.
            """

        else:
            """
            If the number of qubits and bits of
            the given Qiskrypt's Quantum Circuit is strictly lower than 1.
            """

            # TODO - Throw Exception

    def get_name(self) -> str:
        """
        Return the name of the Qiskrypt's Graph State.

        :return super().get_name(): the name of the Qiskrypt's Graph State.
        """

        """
        Return the name of the Qiskrypt's Graph State.
        """
        return super().get_name()

    def get_quantum_entanglement_cardinality(self) -> str:
        """
        Return the cardinality of the Qiskrypt's Graph State.

        :return super().get_quantum_entanglement_cardinality(): the cardinality of the Qiskrypt's Graph State.
        """

        """
        Return the cardinality of the Qiskrypt's Graph State.
        """
        return super().get_quantum_entanglement_cardinality()

    def get_quantum_entanglement_type(self) -> str:
        """
        Return the type of the Qiskrypt's Graph State.

        :return super().get_quantum_entanglement_type(): the type of the Qiskrypt's Graph State.
        """

        """
        Return the type of the Qiskrypt's Graph State.
        """
        return super().get_quantum_entanglement_type()

    def get_qiskrypt_quantum_circuit(self) -> QiskryptQuantumCircuit:
        """
        Return the Qiskrypt's Quantum Circuit,
        from which it will be configured the Qiskrypt's Graph State.

        :return super().get_qiskrypt_quantum_circuit(): the Qiskrypt's Quantum Circuit,
                                                        from which it will be configured
                                                        the Qiskrypt's Graph State.
        """

        """
        Return the Qiskrypt's Quantum Circuit,
        from which it will be configured the Qiskrypt's Graph State.
        """
        return super().get_qiskrypt_quantum_circuit()

    def get_resource_type(self) -> str:
        """
        Return the resource type of the Qiskrypt's Graph State.

        :return self.resource_type: the resource type of the Qiskrypt's Graph State.
        """

        """
        Return the resource type of the Qiskrypt's Graph State.
        """
        return self.resource_type

    def get_qiskit_quantum_registers_indexes(self) -> list:
        """
        Return the indexes of the IBM Qiskit's Quantum Registers, associated to the Graph State itself.

        :return self.qiskit_quantum_registers_indexes: the indexes of the IBM Qiskit's Quantum Registers,
                                                       associated to the Graph State itself.
        """

        """
        Return the indexes of the IBM Qiskit's Quantum Registers, associated to the Graph State itself.
        """
        return self.qiskit_quantum_registers_indexes

    def get_qubits_vertices_indexes(self) -> list:
        """
        Return the indexes of the qubits inside the IBM Qiskit's Quantum Register,
        representing the vertices of the Graph State.

        :return self.qubits_vertices_indexes: the indexes of the qubits inside
                                              the IBM Qiskit's Quantum Register,
                                              representing the vertices of the Graph State.
        """

        """
        Return the indexes of the qubits inside the IBM Qiskit's Quantum Register,
        representing the vertices of the Graph State.
        """
        return self.qubits_vertices_indexes

    def get_qubits_pairs_edges_indexes(self) -> list:
        """
        Return the pairs of indexes of the qubits inside the IBM Qiskit's Quantum Registers,
        as well, the IBM Qiskit's Quantum Registers themselves, representing the edges of the Graph State.

        :return self.qubits_pairs_edges_indexes: the pairs of indexes of the qubits inside
                                                 the IBM Qiskit's Quantum Registers,
                                                 as well, the IBM Qiskit's Quantum Registers themselves,
                                                 representing the edges of the Graph State.
        """

        """
        Return the pairs of indexes of the qubits inside the IBM Qiskit's Quantum Registers,
        as well, the IBM Qiskit's Quantum Registers themselves, representing the edges of the Graph State.
        """
        return self.qubits_pairs_edges_indexes

    def configure(self, qiskit_quantum_registers_indexes: list,
                  qubits_vertices_indexes: list, qubits_pairs_edges_indexes: list) -> None:
        """
        Configure the Qiskrypt's Graph State,
        regarding its IBM Qiskit's Quantum Registers, qubits representing the vertices of the Graph State,
        as well, a dictionary with the pairs of qubits inside IBM Qiskit's Quantum Registers, as also,
        the respective IBM Qiskit's Quantum Registers themselves, representing the edges of the Graph State.

        :param qiskit_quantum_registers_indexes: the indexes of the IBM Qiskit's Quantum Registers,
                                                 associated to the Graph State itself.
        :param qubits_vertices_indexes: the indexes of the qubits inside the IBM Qiskit's Quantum Register,
                                        representing the vertices of the Graph State.
        :param qubits_pairs_edges_indexes: the pairs of indexes of the qubits inside the
                                           IBM Qiskit's Quantum Registers, as well, a dictionary with
                                           the pairs of qubits inside IBM Qiskit's Quantum Registers, as also,
                                           the respective IBM Qiskit's Quantum Registers themselves,
                                           representing the edges of the Graph State.
        """

        if self.are_qubits_pairs_edges_indexes_valid_for_graph_state(qiskit_quantum_registers_indexes,
                                                                     qubits_vertices_indexes,
                                                                     qubits_pairs_edges_indexes):
            """
            Check if all the pairs of indexes of the qubits inside the IBM Qiskit's Quantum Registers, as well,
            the IBM Qiskit's Quantum Registers themselves, representing the edges of the Graph State, are valid.
            """

            self.qiskit_quantum_registers_indexes = qiskit_quantum_registers_indexes
            """
            Set the indexes of the IBM Qiskit's Quantum Registers, associated to the Graph State itself,
            as the given indexes for it.
            """

            self.qubits_vertices_indexes = qubits_vertices_indexes
            """
            Set the indexes of the qubits inside the IBM Qiskit's Quantum Register,
            representing the vertices of the Graph State, as the given indexes for it.
            """

            self.qubits_pairs_edges_indexes = qubits_pairs_edges_indexes
            """
            Set the the pairs of indexes of the qubits inside the IBM Qiskit's Quantum Registers,
            as well, the IBM Qiskit's Quantum Registers themselves,
            representing the edges of the Graph State, as the given indexes for it.
            """

    def prepare_multipartite_entanglement_at_computational_basis(self, is_to_measure_at_computational_basis=False,
                                                                 qiskit_classical_registers_indexes=None,
                                                                 bits_vertices_indexes=None) -> None:
        """
        Prepare the Multipartite Quantum Entanglement,
        for the specified Qiskrypt's Graph State, as a Quantum Entangled State,
        or even, apply also the measurement of that Quantum Entangled State, on the Computational Basis,
        to allow the extraction of its final classical outcome/result.

        :param is_to_measure_at_computational_basis: the boolean flag to keep the information about
                                                     if it will be performed a measurement of
                                                     the Qiskrypt's Graph State on the Computational Basis.
        :param qiskit_classical_registers_indexes: the indexes of the IBM Qiskit's Classical Registers,
                                                   where it belongs the bits to store the final classical outcomes/results,
                                                   after be performed a measurement on the qubits inside
                                                   the IBM Qiskit's Quantum Registers,
                                                   associated to the Graph State itself.
        :param bits_vertices_indexes: the indexes of the bits inside the IBM Qiskit's Classical Registers,
                                      where it will be stored the final classical outcomes/results,
                                      after be performed a measurement on the qubits inside
                                      the IBM Qiskit's Quantum Registers,
                                      representing the vertices of the Graph State.
        """

        self.qiskrypt_quantum_circuit \
            .apply_barriers_set_qubits_in_set_qiskit_quantum_registers(self.qiskit_quantum_registers_indexes,
                                                                       self.qubits_vertices_indexes)
        """
        Apply barriers to the IBM Qiskit's Quantum Registers, associated to the Graph State itself and
        the respective qubits, representing the vertices of the Graph State.
        """

        qiskrypt_quantum_hadamard_transform_graph_state = \
            QiskryptQuantumHadamardTransform("hadamard_transform_graph_state",
                                             self.qiskrypt_quantum_circuit,
                                             self.qiskit_quantum_registers_indexes,
                                             self.qubits_vertices_indexes)
        """
        Create the Qiskrypt's Quantum Hadamard Transform, for the Qiskrypt's Quantum Register and qubits involved.
        """

        qiskrypt_quantum_hadamard_transform_graph_state.apply_transform()
        """
        Apply the Quantum Hadamard Transform to the Qiskrypt's Quantum Registers and qubits,
        involved on the Qiskrypt's Graph State.
        """

        self.qiskrypt_quantum_circuit = \
            qiskrypt_quantum_hadamard_transform_graph_state.get_qiskrypt_quantum_circuit()
        """
        Update the Qiskrypt's Quantum Circuit for the Graph State,
        from the previously created Qiskrypt's Quantum Hadamard Transform.
        """

        for qubits_pair_edge_indexes in self.qubits_pairs_edges_indexes:
            """
            For each edge pair of indexes of qubits,
            inside the respective IBM Qiskit's Quantum Registers.
            """

            qiskit_quantum_register_and_qubit_pair_control = qubits_pair_edge_indexes[0]
            """
            Retrieve the pair of the IBM Qiskit's Quantum Register and the respective qubit,
            for the 1st vertex of the current edge pair, to be the control IBM Qiskit's Quantum Register and
            the respective control qubit.
            """

            qiskit_quantum_register_and_qubit_pair_target = qubits_pair_edge_indexes[1]
            """
            Retrieve the pair of the IBM Qiskit's Quantum Register and the respective qubit,
            for the 2nd vertex of the current edge pair, to be the target IBM Qiskit's Quantum Register and
            the respective target qubit.
            """

            self.qiskrypt_quantum_circuit.apply_controlled_pauli_z(qiskit_quantum_register_and_qubit_pair_control[0],
                                                                   qiskit_quantum_register_and_qubit_pair_target[0],
                                                                   qiskit_quantum_register_and_qubit_pair_control[1],
                                                                   qiskit_quantum_register_and_qubit_pair_target[1])
            """
            Apply the Controlled-Pauli-Z (Controlled-Phase-Flip/Controlled-Phase-Shifter) Gate/Operation to
            the indexes of the control IBM Qiskit's Quantum Register and the respective qubit on it, as also,
            the current target IBM Qiskit's Quantum Register and the current respective qubit on it.
            """

        self.qiskrypt_quantum_circuit \
            .apply_barriers_set_qubits_in_set_qiskit_quantum_registers(self.qiskit_quantum_registers_indexes,
                                                                       self.qubits_vertices_indexes)
        """
        Apply barriers to the IBM Qiskit's Quantum Registers, associated to the Graph State itself and
        the respective qubits, representing the vertices of the Graph State.
        """

        if is_to_measure_at_computational_basis:
            """
            If the boolean flag to keep the information about
            if it will be performed a measurement of
            the Qiskrypt's Graph State on the Computational Basis, is True.
            """

            if self.qiskrypt_quantum_circuit.get_total_num_bits() >= len(bits_vertices_indexes):
                """
                If the number of bits of the given Qiskrypt's Quantum Circuit is greater or equal than
                the number of the bits inside the IBM Qiskit's Classical Registers,
                representing the vertices of the Graph State.
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
                representing the vertices of the Graph State.
                """

                # TODO - Throw Exception

    @staticmethod
    def are_qubits_pairs_edges_indexes_valid_for_graph_state(qiskit_quantum_registers_indexes: list,
                                                             qubits_vertices_indexes: list,
                                                             qubits_pairs_edges_indexes: list):
        """
        Return True, if all the pairs of indexes of the qubits inside the IBM Qiskit's Quantum Registers,
        as well, the IBM Qiskit's Quantum Registers themselves, representing the edges of the Graph State, are valid.

        :param qiskit_quantum_registers_indexes: the indexes of the IBM Qiskit's Quantum Registers,
                                                 associated to the Graph State itself.
        :param qubits_vertices_indexes: the indexes of the qubits inside the IBM Qiskit's Quantum Register,
                                        representing the vertices of the Graph State.
        :param qubits_pairs_edges_indexes: the pairs of indexes of the qubits inside the IBM Qiskit's Quantum Registers,
                                           as well, the IBM Qiskit's Quantum Registers themselves,
                                           representing the edges of the Graph State.

        :return True: all the pairs of indexes of the qubits inside the IBM Qiskit's Quantum Registers,
                      as well, the IBM Qiskit's Quantum Registers themselves,
                      representing the edges of the Graph State are valid.
        """

        qiskit_quantum_registers_and_qubit_vertices_indexes_pairs = \
            zip(qiskit_quantum_registers_indexes, qubits_vertices_indexes)
        """
        Zip the the indexes of the IBM Qiskit's Quantum Registers, associated to the Graph State itself,
        as well, the indexes of the qubits inside that IBM Qiskit's Quantum Register,
        representing the vertices of the Graph State, as a list of pairs.
        """

        for qubits_pair_edge_indexes in qubits_pairs_edges_indexes:
            """
            For each edge pair of indexes of qubits,
            inside the respective IBM Qiskit's Quantum Registers.
            """

            if not isinstance(qubits_pair_edge_indexes, tuple) \
                    or not len(qubits_pair_edge_indexes) == 2:
                """
                If the edge pair of indexes of qubits,
                inside the respective IBM Qiskit's Quantum Registers,
                is not an instance of a tuple or does not have the size of 2,
                the format for the current edge pair of indexes of qubits is wrong.
                """

                # TODO - Throw Exception

            else:
                """
                If the edge pair of indexes of qubits,
                inside the respective IBM Qiskit's Quantum Registers,
                is an instance of a tuple and does have the size of 2,
                the verification will proceed for the two pairs of
                qubits and IBM Qiskit's Quantum Registers of
                the current of edge pair of indexes of qubits.
                """

                for quantum_register_and_qubit_pair_vertex in qubits_pair_edge_indexes:
                    """
                    For each vertex pair of indexes of qubits,
                    inside the respective IBM Qiskit's Quantum Registers.
                    """

                    if not isinstance(quantum_register_and_qubit_pair_vertex, tuple) \
                            or not len(quantum_register_and_qubit_pair_vertex) == 2:
                        """
                        If the current vertex pair of indexes of qubits,
                        inside the respective IBM Qiskit's Quantum Registers,
                        is not an instance of a tuple or does not have the size of 2,
                        the format for the current vertex pair of indexes of
                        an IBM Qiskit's Quantum Register and a qubit is wrong.
                        """

                        # TODO - Throw Exception

                    if quantum_register_and_qubit_pair_vertex\
                           not in qiskit_quantum_registers_and_qubit_vertices_indexes_pairs:
                        """
                        If the current vertex pair of indexes of qubits,
                        inside the respective IBM Qiskit's Quantum Registers is not valid.
                        """

                        # TODO - Throw Exception

        """
        Return True, if all the pairs of indexes of the qubits inside the IBM Qiskit's Quantum Registers,
        as well, the IBM Qiskit's Quantum Registers themselves, representing the edges of the Graph State, are valid.
        """
        return True
