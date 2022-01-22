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

from src.quantum.entanglements.QiskryptQuantumEntanglement \
    import QiskryptQuantumEntanglement
"""
Import the Qiskrypt's Quantum Entanglement.
"""

from src.quantum.entanglements.QiskryptQuantumEntanglement \
    import POSSIBLE_QUANTUM_ENTANGLEMENT_CARDINALITIES
"""
Import the available Quantum Entanglement cardinalities for
the Qiskrypt's Quantum Entanglement.
"""

from src.quantum.entanglements.QiskryptQuantumEntanglement \
    import POSSIBLE_QUANTUM_ENTANGLEMENT_TYPES
"""
Import the available Quantum Entanglement types for
the Qiskrypt's Quantum Entanglement.
"""

from src.quantum.circuit.QiskryptQuantumCircuit \
    import QiskryptQuantumCircuit
"""
Import the Qiskrypt's Quantum Circuit.
"""


class QiskryptGHZState(QiskryptQuantumEntanglement):
    """
    Object class for the Qiskrypt's GHZ State.
    """

    def __init__(self, name: str, qiskrypt_quantum_circuit: QiskryptQuantumCircuit):
        """
        Constructor of the Qiskrypt's GHZ State.

        :param name: the name of the Qiskrypt's GHZ State.
        :param qiskrypt_quantum_circuit: the name of the Qiskrypt's GHZ State.
        """

        if qiskrypt_quantum_circuit.get_total_num_qubits() >= 3:
            """
            If the number of qubits of
            the given Qiskrypt's Quantum Circuit is greater or equal than 3.
            """

            super().__init__(name, POSSIBLE_QUANTUM_ENTANGLEMENT_CARDINALITIES[1],
                             POSSIBLE_QUANTUM_ENTANGLEMENT_TYPES[1],
                             qiskrypt_quantum_circuit)
            """
            Calls the constructor of the super-class Qiskrypt's Quantum Entanglement.
            """

            self.qiskit_quantum_register_control_index = None
            """
            Set the index of the control IBM Qiskit's Quantum Register, as None.
            """

            self.qiskit_quantum_registers_target_indexes = None
            """
            Set the indexes of the target IBM Qiskit's Quantum Registers, as None.
            """

            self.control_qubit_index = None
            """
            Set the index of a qubit inside the control IBM Qiskit's Quantum Register, as None.
            """

            self.target_qubits_indexes = None
            """
            Set the indexes of the qubits inside the target IBM Qiskit's Quantum Registers, as None.
            """

        else:
            """
            If the number of qubits and bits of
            the given Qiskrypt's Quantum Circuit is strictly lower than 3.
            """

            # TODO - Throw Exception

    def get_name(self) -> str:
        """
        Return the name of the Qiskrypt's GHZ State.

        :return super().get_name(): the name of the Qiskrypt's GHZ State.
        """

        """
        Return the name of the Qiskrypt's GHZ State.
        """
        return super().get_name()

    def get_quantum_entanglement_cardinality(self) -> str:
        """
        Return the cardinality of the Qiskrypt's GHZ State.

        :return super().get_quantum_entanglement_cardinality(): the cardinality of
                                                                the Qiskrypt's GHZ State.
        """

        """
        Return the cardinality of the Qiskrypt's GHZ State.
        """
        return super().get_quantum_entanglement_cardinality()

    def get_quantum_entanglement_type(self) -> str:
        """
        Return the type of the Qiskrypt's GHZ State.

        :return super().get_quantum_entanglement_type(): the type of the Qiskrypt's GHZ State.
        """

        """
        Return the type of the Qiskrypt's GHZ State.
        """
        return super().get_quantum_entanglement_type()

    def get_qiskrypt_quantum_circuit(self) -> QiskryptQuantumCircuit:
        """
        Return the Qiskrypt's Quantum Circuit,
        from which it will be configured the Qiskrypt's GHZ State.

        :return super().get_qiskrypt_quantum_circuit(): the Qiskrypt's Quantum Circuit,
                                                        from which it will be configured
                                                        the Qiskrypt's GHZ State.
        """

        """
        Return the Qiskrypt's Quantum Circuit,
        from which it will be configured the Qiskrypt's GHZ State.
        """
        return super().get_qiskrypt_quantum_circuit()

    def get_qiskit_quantum_register_control_index(self) -> int:
        """
        Return the index of the control IBM Qiskit's Quantum Register of the Qiskrypt's GHZ State.

        :return self.qiskit_quantum_register_control_index: the index of the control
                                                            IBM Qiskit's Quantum Register of
                                                            the Qiskrypt's GHZ State.
        """

        """
        Return the index of the control IBM Qiskit's Quantum Register of the Qiskrypt's GHZ State.
        """
        return self.qiskit_quantum_register_control_index

    def get_qiskit_quantum_registers_target_indexes(self) -> list:
        """
        Return the indexes of the target IBM Qiskit's Quantum Registers of the Qiskrypt's GHZ State.

        :return self.qiskit_quantum_registers_target_indexes: the indexes of the target
                                                           IBM Qiskit's Quantum Registers of
                                                           the Qiskrypt's GHZ State.
        """

        """
        Return the index of the target IBM Qiskit's Quantum Register of the Qiskrypt's GHZ State.
        """
        return self.qiskit_quantum_registers_target_indexes

    def get_control_qubit_index(self) -> int:
        """
        Return the index of a qubit inside the control IBM Qiskit's Quantum Register of the Qiskrypt's GHZ State.

        :return self.control_qubit_index: the index of a qubit inside
                                          the control IBM Qiskit's Quantum Register of
                                          the Qiskrypt's GHZ State.
        """

        """
        Return the index of a qubit inside the control IBM Qiskit's Quantum Register of the Qiskrypt's GHZ State.
        """
        return self.control_qubit_index

    def get_target_qubits_indexes(self) -> list:
        """
        Return the indexes of the qubits inside the target IBM Qiskit's Quantum Registers of the Qiskrypt's GHZ State.

        :return self.target_qubit_index: the indexes of the qubits inside
                                         the target IBM Qiskit's Quantum Registers of
                                         the Qiskrypt's GHZ State.
        """

        """
        Return the indexes of the qubits inside the target IBM Qiskit's Quantum Registers of the Qiskrypt's GHZ State.
        """
        return self.target_qubits_indexes

    def configure(self, qiskit_quantum_register_control_index: int,
                  qiskit_quantum_registers_target_indexes: list,
                  control_qubit_index: int, target_qubits_indexes: list) -> None:
        """
        Configure the Qiskrypt's GHZ State,
        regarding its control IBM Qiskit's Quantum Register and control qubit,
        as well, its target IBM Qiskit's Quantum Registers and target qubits.

        :param qiskit_quantum_register_control_index: the index of the control IBM Qiskit's Quantum Register.
        :param qiskit_quantum_registers_target_indexes: the indexes of the target IBM Qiskit's Quantum Registers.
        :param control_qubit_index: the index of a qubit inside the control IBM Qiskit's Quantum Register.
        :param target_qubits_indexes: the indexes of the qubits inside the target IBM Qiskit's Quantum Registers.
        """

        self.qiskit_quantum_register_control_index = qiskit_quantum_register_control_index
        """
        Set the index of the control IBM Qiskit's Quantum Register, as the given index for it.
        """

        self.qiskit_quantum_registers_target_indexes = qiskit_quantum_registers_target_indexes
        """
        Set the indexes of the target IBM Qiskit's Quantum Registers, as the given indexes for it.
        """

        self.control_qubit_index = control_qubit_index
        """
        Set the index of a qubit inside the control IBM Qiskit's Quantum Register,
        as the given index for it.
        """

        self.target_qubits_indexes = target_qubits_indexes
        """
        Set the indexes of the qubits inside the target IBM Qiskit's Quantum Registers,
        as the given indexes for it.
        """

    def prepare_multipartite_entanglement_at_computational_basis(self, is_to_measure_at_computational_basis=False,
                                                                 qiskit_classical_register_control_index=None,
                                                                 qiskit_classical_registers_target_indexes=None,
                                                                 control_bit_index=None, target_bits_indexes=None) -> None:
        """
        Prepare the Multipartite Quantum Entanglement,
        for the specified Qiskrypt's GHZ State, as a Quantum Entangled State,
        or even, apply also the measurement of that Quantum Entangled State, on the Computational Basis,
        to allow the extraction of its final classical outcome/result.

        :param is_to_measure_at_computational_basis: the boolean flag to keep the information about
                                                     if it will be performed a measurement of
                                                     the Qiskrypt's GHZ State on the Computational Basis.
        :param qiskit_classical_register_control_index: the index of the control IBM Qiskit's Classical Register,
                                                        where it belongs the bit to store the final classical outcome/result,
                                                        after be performed a measurement on the qubit inside
                                                        the control IBM Qiskit's Quantum Register.
        :param qiskit_classical_registers_target_indexes: the indexes of the target IBM Qiskit's Classical Registers,
                                                          where it belongs the bits to store the final classical outcomes/results,
                                                          after be performed a measurement on the qubits inside
                                                          the target IBM Qiskit's Quantum Registers.
        :param control_bit_index: the index of a bit inside the control IBM Qiskit's Classical Register,
                                  where it will be stored the final classical outcome/result,
                                  after be performed a measurement on the qubit inside
                                  the control IBM Qiskit's Quantum Register.
        :param target_bits_indexes: the indexes of the bits inside the target IBM Qiskit's Classical Registers,
                                    where it will be stored the final classical outcomes/results,
                                    after be performed a measurement on the qubits inside
                                    the target IBM Qiskit's Quantum Registers.
        """

        self.qiskrypt_quantum_circuit\
            .apply_barrier_to_single_qubit_in_qiskit_quantum_register(self.qiskit_quantum_register_control_index,
                                                                      self.control_qubit_index)
        """
        Apply a barrier to the control IBM Qiskit's Quantum Register and the respective control qubit.
        """

        self.qiskrypt_quantum_circuit \
            .apply_barriers_set_qubits_in_set_qiskit_quantum_registers(self.qiskit_quantum_registers_target_indexes,
                                                                       self.target_qubits_indexes)
        """
        Apply barriers to the target IBM Qiskit's Quantum Registers and the respective target qubits.
        """

        self.qiskrypt_quantum_circuit.apply_hadamard(self.qiskit_quantum_register_control_index,
                                                     self.control_qubit_index)
        """
        Apply the Hadamard Gate/Operation to the given indexes of
        the control IBM Qiskit's Quantum Register and the respective control qubit on it.
        """

        qiskit_quantum_registers_and_qubits_target_indexes = zip(self.qiskit_quantum_registers_target_indexes,
                                                                 self.target_qubits_indexes)
        """
        Zip the both lists of indexes for the target IBM Qiskit's Quantum Registers and
        the respective target qubits.
        """

        for qiskit_quantum_register_target_index, target_qubit_index in \
            qiskit_quantum_registers_and_qubits_target_indexes:
            """
            For each pair of target IBM Qiskit's Quantum Register and its respective target qubit.
            """

            self.qiskrypt_quantum_circuit.apply_controlled_pauli_x(self.qiskit_quantum_register_control_index,
                                                                   self.control_qubit_index,
                                                                   qiskit_quantum_register_target_index,
                                                                   target_qubit_index)
            """
            Apply the Controlled-Pauli-X (Controlled-NOT) Gate/Operation to the given indexes of
            the control IBM Qiskit's Quantum Register and the respective qubit on it, as also,
            of the current target IBM Qiskit's Quantum Register and the current respective qubit on it.
            """

        self.qiskrypt_quantum_circuit \
            .apply_barrier_to_single_qubit_in_qiskit_quantum_register(self.qiskit_quantum_register_control_index,
                                                                      self.control_qubit_index)
        """
        Apply a barrier to the control IBM Qiskit's Quantum Register and the respective control qubit.
        """

        self.qiskrypt_quantum_circuit \
            .apply_barriers_set_qubits_in_set_qiskit_quantum_registers(self.qiskit_quantum_registers_target_indexes,
                                                                       self.target_qubits_indexes)
        """
        Apply barriers to the target IBM Qiskit's Quantum Registers and the respective target qubits.
        """

        if is_to_measure_at_computational_basis:
            """
            If the boolean flag to keep the information about
            if it will be performed a measurement of
            the Qiskrypt's GHZ State on the Computational Basis, is True.
            """

            if self.qiskrypt_quantum_circuit.get_total_num_bits() >= (len(target_bits_indexes) + 1):
                """
                If the number of bits of the given Qiskrypt's Quantum Circuit is greater or equal than
                the number of the target bits inside the target IBM Qiskit's Classical Registers,
                plus one, for the control bit inside the control IBM Qiskit's Classical Register.
                """

                self.qiskrypt_quantum_circuit\
                    .measure_single_qubit_in_qiskit_quantum_register(self.qiskit_quantum_register_control_index,
                                                                     qiskit_classical_register_control_index,
                                                                     self.control_qubit_index, control_bit_index)
                """
                Measure the control qubit in the control IBM Qiskit's Quantum Register into
                the respective control bit in the control IBM Qiskit's Classical Register,
                inside the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit.
                """

                self.qiskrypt_quantum_circuit\
                    .measure_set_qubits_in_set_qiskit_quantum_registers(self.qiskit_quantum_registers_target_indexes,
                                                                        qiskit_classical_registers_target_indexes,
                                                                        self.target_qubits_indexes,
                                                                        target_bits_indexes)
                """
                Measure the target qubits in the target IBM Qiskit's Quantum Registers into
                the respective target bits in the target IBM Qiskit's Classical Registers,
                inside the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit.
                """

            else:
                """
                If the number of bits of the given Qiskrypt's Quantum Circuit is lower than
                the number of the target bits inside the target IBM Qiskit's Classical Registers,
                plus one, for the control bit inside the control IBM Qiskit's Classical Register.
                """

                # TODO - Throw Exception

    def prepare_multipartite_entanglement_at_ghz_state_basis(self, is_to_measure_at_ghz_state_basis=False,
                                                             qiskit_classical_register_control_index=None,
                                                             qiskit_classical_registers_target_indexes=None,
                                                             control_bit_index=None, target_bits_indexes=None) -> None:
        """
        Prepare the Multipartite Quantum Entanglement,
        for the specified Qiskrypt's GHZ State, as a Quantum Entangled State,
        or even, apply also the measurement of that Quantum Entangled State, on the GHZ State Basis,
        to allow the extraction of its final classical outcome/result.

        :param is_to_measure_at_ghz_state_basis: the boolean flag to keep the information about
                                                 if it will be performed a measurement of
                                                 the Qiskrypt's GHZ State on the GHZ State Basis.
        :param qiskit_classical_register_control_index: the index of the control IBM Qiskit's Classical Register,
                                                        where it belongs the bit to store the final classical outcome/result,
                                                        after be performed a measurement on the qubit inside
                                                        the control IBM Qiskit's Quantum Register.
        :param qiskit_classical_registers_target_indexes: the indexes of the target IBM Qiskit's Classical Registers,
                                                          where it belongs the bits to store the final classical outcomes/results,
                                                          after be performed a measurement on the qubits inside
                                                          the target IBM Qiskit's Quantum Registers.
        :param control_bit_index: the index of a bit inside the control IBM Qiskit's Classical Register,
                                  where it will be stored the final classical outcome/result,
                                  after be performed a measurement on the qubit inside
                                  the control IBM Qiskit's Quantum Register.
        :param target_bits_indexes: the indexes of the bits inside the target IBM Qiskit's Classical Registers,
                                    where it will be stored the final classical outcomes/results,
                                    after be performed a measurement on the qubits inside
                                    the target IBM Qiskit's Quantum Registers.
        """

        self.qiskrypt_quantum_circuit \
            .apply_barrier_to_single_qubit_in_qiskit_quantum_register(self.qiskit_quantum_register_control_index,
                                                                      self.control_qubit_index)
        """
        Apply a barrier to the control IBM Qiskit's Quantum Register and the respective control qubit.
        """

        self.qiskrypt_quantum_circuit \
            .apply_barriers_set_qubits_in_set_qiskit_quantum_registers(self.qiskit_quantum_registers_target_indexes,
                                                                       self.target_qubits_indexes)
        """
        Apply barriers to the target IBM Qiskit's Quantum Registers and the respective target qubits.
        """

        qiskit_quantum_registers_target_indexes_reversed = self.qiskit_quantum_registers_target_indexes.copy()
        """
        Create a copy of the list of indexes of the target IBM Qiskit's Quantum Registers, for its own reversal.
        """

        target_qubits_indexes_reversed = self.target_qubits_indexes.copy()
        """
        Create a copy of the list of indexes of the target qubits, for its own reversal.
        """

        qiskit_quantum_registers_target_indexes_reversed.reverse()
        """
        Reverse the list of indexes of the target IBM Qiskit's Quantum Registers.
        """

        target_qubits_indexes_reversed.reverse()
        """
        Reverse the list of indexes of the target qubits.
        """

        qiskit_quantum_registers_and_qubits_target_indexes_reversed = zip(self.qiskit_quantum_registers_target_indexes,
                                                                          self.target_qubits_indexes)
        """
        Zip the both lists of indexes for the reversed target IBM Qiskit's Quantum Registers and
        the respective reversed target qubits.
        """

        for qiskit_quantum_register_target_index_reversed, target_qubit_index_reversed in \
            qiskit_quantum_registers_and_qubits_target_indexes_reversed:
            """
            For each pair of reversed target IBM Qiskit's Quantum Register and
            its respective reversed target qubit.
            """

            self.qiskrypt_quantum_circuit.apply_controlled_pauli_x(self.qiskit_quantum_register_control_index,
                                                                   self.control_qubit_index,
                                                                   qiskit_quantum_register_target_index_reversed,
                                                                   target_qubit_index_reversed)
            """
            Apply the Controlled-Pauli-X (Controlled-NOT) Gate/Operation to the given indexes of
            the control IBM Qiskit's Quantum Register and the respective reversed qubit on it, as also,
            of the current reversed target IBM Qiskit's Quantum Register and
            the current respective reversed qubit on it.
            """

        self.qiskrypt_quantum_circuit.apply_hadamard(self.qiskit_quantum_register_control_index,
                                                     self.control_qubit_index)
        """
        Apply the Hadamard Gate/Operation to the given indexes of
        the control IBM Qiskit's Quantum Register and the respective control qubit on it.
        """

        self.qiskrypt_quantum_circuit \
            .apply_barrier_to_single_qubit_in_qiskit_quantum_register(self.qiskit_quantum_register_control_index,
                                                                      self.control_qubit_index)
        """
        Apply a barrier to the control IBM Qiskit's Quantum Register and the respective control qubit.
        """

        self.qiskrypt_quantum_circuit \
            .apply_barriers_set_qubits_in_set_qiskit_quantum_registers(self.qiskit_quantum_registers_target_indexes,
                                                                       self.target_qubits_indexes)
        """
        Apply barriers to the target IBM Qiskit's Quantum Registers and the respective target qubits.
        """

        if is_to_measure_at_ghz_state_basis:
            """
            If the boolean flag to keep the information about
            if it will be performed a measurement of
            the Qiskrypt's GHZ State on the GHZ State Basis, is True.
            """

            if self.qiskrypt_quantum_circuit.get_total_num_bits() >= (len(target_bits_indexes) + 1):
                """
                If the number of bits of the given Qiskrypt's Quantum Circuit is greater or equal than
                the number of the target bits inside the target IBM Qiskit's Classical Registers,
                plus one, for the control bit inside the control IBM Qiskit's Classical Register.
                """

                self.qiskrypt_quantum_circuit\
                    .measure_single_qubit_in_qiskit_quantum_register(self.qiskit_quantum_register_control_index,
                                                                     qiskit_classical_register_control_index,
                                                                     self.control_qubit_index, control_bit_index)
                """
                Measure the control qubit in the control IBM Qiskit's Quantum Register into
                the respective control bit in the control IBM Qiskit's Classical Register,
                inside the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit.
                """

                self.qiskrypt_quantum_circuit\
                    .measure_set_qubits_in_set_qiskit_quantum_registers(self.qiskit_quantum_registers_target_indexes,
                                                                        qiskit_classical_registers_target_indexes,
                                                                        self.target_qubits_indexes,
                                                                        target_bits_indexes)
                """
                Measure the target qubits in the target IBM Qiskit's Quantum Registers into
                the respective target bits in the target IBM Qiskit's Classical Registers,
                inside the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit.
                """

            else:
                """
                If the number of bits of the given Qiskrypt's Quantum Circuit is lower than
                the number of the target bits inside the target IBM Qiskit's Classical Registers,
                plus one, for the control bit inside the control IBM Qiskit's Classical Register.
                """

                # TODO - Throw Exception
