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

from numpy import arccos, sqrt
"""
Import the Arc-Cosine and Squared Roots functions from Python's NumPy.
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

    def prepare_multipartite_entanglement_at_computational_basis(self, is_to_measure_at_computational_basis=False,
                                                                 qiskit_classical_registers_indexes=None,
                                                                 bits_indexes=None) -> None:
        """
        Prepare the Multipartite Quantum Entanglement,
        for the specified Qiskrypt's W State, as a Quantum Entangled State,
        or even, apply also the measurement of that Quantum Entangled State, on the Computational Basis,
        to allow the extraction of its final classical outcome/result.

        :param is_to_measure_at_computational_basis: the boolean flag to keep the information about
                                                     if it will be performed a measurement of
                                                     the Qiskrypt's W State on the Computational Basis.
        :param qiskit_classical_registers_indexes: the indexes of the IBM Qiskit's Classical Registers,
                                                   where it belongs the bits to store the final classical outcomes/results,
                                                   after be performed a measurement on the qubits inside
                                                   the IBM Qiskit's Quantum Registers.
        :param bits_indexes: the indexes of the bits inside the IBM Qiskit's Classical Registers,
                             where it will be stored the final classical outcomes/results,
                             after be performed a measurement on the qubits inside
                             the IBM Qiskit's Quantum Registers.
        """

        self.qiskrypt_quantum_circuit \
            .apply_barriers_set_qubits_in_set_qiskit_quantum_registers(self.qiskit_quantum_registers_indexes,
                                                                       self.qubits_indexes)
        """
        Apply barriers to the IBM Qiskit's Quantum Registers and the respective qubits.
        """

        num_quantum_registers = len(self.qiskit_quantum_registers_indexes)
        """
        Retrieve the number of the IBM Qiskit's Quantum Registers for the Qiskrypt's W State.
        """

        num_qubits = len(self.qubits_indexes)
        """
        Retrieve the number of qubits for the Qiskrypt's W State.
        """

        self.qiskrypt_quantum_circuit.apply_pauli_x(self.qiskit_quantum_registers_indexes[(num_quantum_registers - 1)],
                                                    self.qubits_indexes[(num_qubits - 1)])
        """
        Apply the Pauli-X Gate/Operation to the given indexes of
        the last IBM Qiskit's Quantum Register and the respective qubit on it.
        """

        for qiskit_quantum_register_index, qubit_index in \
                zip(range((num_quantum_registers - 1)), range((num_qubits - 1))):
            """
            For each pair of indexes for an IBM Qiskit's Quantum Register and a qubit. 
            """

            quantum_register_operator_index = (num_quantum_registers - qiskit_quantum_register_index)
            """
            Compute the operator index for the IBM Qiskit's Quantum Register.
            """

            qubit_operator_index = (num_qubits - qubit_index)
            """
            Compute the operator index for the qubit inside the IBM Qiskit's Quantum Register.
            """

            theta_radians = arccos(sqrt(1. / qubit_operator_index))
            """
            Compute the theta angle, in radians, from the Arc-Cosine function of
            the Square Root of the inverse of the operator index for the qubit inside
            the IBM Qiskit's Quantum Register.
            """

            self.qiskrypt_quantum_circuit.apply_ry_radians(-theta_radians,
                                                           self.qiskit_quantum_registers_indexes[(qiskit_quantum_register_index - 2)],
                                                           self.qubits_indexes[(qubit_operator_index - 2)])
            """
            Apply the Rotation-Y (R_y(-theta_radians)) Gate/Operation, with the symmetric theta angle in radians,
            to the given indexes of the current operator index for the IBM Qiskit's Quantum Register and
            the current operator index for the qubit on it.
            """

            self.qiskrypt_quantum_circuit\
                .apply_controlled_pauli_z(self.qiskit_quantum_registers_indexes[(quantum_register_operator_index - 1)],
                                          self.qiskit_quantum_registers_indexes[(quantum_register_operator_index - 2)],
                                          self.qubits_indexes[(qubit_operator_index - 1)],
                                          self.qubits_indexes[(qubit_operator_index - 2)])
            """
            Apply the Controlled-Pauli-Z (Controlled-Phase-Flip/Controlled-Phase-Shifter) Gate/Operation to
            the given indexes of the control IBM Qiskit's Quantum Register and the respective qubit on it, as also,
            of the current target IBM Qiskit's Quantum Register and the current respective qubit on it.
            """

            self.qiskrypt_quantum_circuit\
                .apply_ry_radians(theta_radians,
                                  self.qiskit_quantum_registers_indexes[(qiskit_quantum_register_index - 2)],
                                  self.qubits_indexes[(qubit_operator_index - 2)])
            """
            Apply again the Rotation-Y (R_y(theta_radians)) Gate/Operation, with the regular theta angle in radians,
            to the given indexes of the current operator index for the IBM Qiskit's Quantum Register and
            the current operator index for the qubit on it.
            """

        for qiskit_quantum_register_index, qubit_index in \
                zip(range((num_quantum_registers - 1)), range((num_qubits - 1))):
            """
            For each pair of indexes for an IBM Qiskit's Quantum Register and a qubit. 
            """

            quantum_register_operator_index = (num_quantum_registers - qiskit_quantum_register_index)
            """
            Compute the operator index for the IBM Qiskit's Quantum Register.
            """

            qubit_operator_index = (num_qubits - qubit_index)
            """
            Compute the operator index for the qubit inside the IBM Qiskit's Quantum Register.
            """

            self.qiskrypt_quantum_circuit\
                .apply_controlled_pauli_x(self.qiskit_quantum_registers_indexes[(quantum_register_operator_index - 2)],
                                          self.qiskit_quantum_registers_indexes[(quantum_register_operator_index - 1)],
                                          self.qubits_indexes[(qubit_operator_index - 2)],
                                          self.qubits_indexes[(qubit_operator_index - 1)])
            """
            Apply the Controlled-Pauli-X (Controlled-NOT) Gate/Operation to
            the given indexes of the control IBM Qiskit's Quantum Register and the respective qubit on it, as also,
            of the current target IBM Qiskit's Quantum Register and the current respective qubit on it.
            """

        self.qiskrypt_quantum_circuit \
            .apply_barriers_set_qubits_in_set_qiskit_quantum_registers(self.qiskit_quantum_registers_indexes,
                                                                       self.qubits_indexes)
        """
        Apply barriers to the IBM Qiskit's Quantum Registers and the respective qubits.
        """

        if is_to_measure_at_computational_basis:
            """
            If the boolean flag to keep the information about
            if it will be performed a measurement of
            the Qiskrypt's W State on the Computational Basis, is True.
            """

            if self.qiskrypt_quantum_circuit.get_total_num_bits() >= len(bits_indexes):
                """
                If the number of bits of the given Qiskrypt's Quantum Circuit is greater or equal than
                the number of the bits inside the IBM Qiskit's Classical Register.
                """

                self.qiskrypt_quantum_circuit\
                    .measure_set_qubits_in_set_qiskit_quantum_registers(self.qiskit_quantum_registers_indexes,
                                                                        qiskit_classical_registers_indexes,
                                                                        self.qubits_indexes,
                                                                        bits_indexes)
                """
                Measure the qubits in the IBM Qiskit's Quantum Registers into
                the respective bits in the IBM Qiskit's Classical Registers,
                inside the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit.
                """

            else:
                """
                If the number of bits of the given Qiskrypt's Quantum Circuit is lower than
                the number of the bits inside the IBM Qiskit's Classical Register.
                """

                # TODO - Throw Exception

    def prepare_multipartite_entanglement_at_w_state_basis(self, is_to_measure_at_w_state_basis=False,
                                                           qiskit_classical_registers_indexes=None,
                                                           bits_indexes=None) -> None:
        """
        Prepare the Multipartite Quantum Entanglement,
        for the specified Qiskrypt's W State, as a Quantum Entangled State,
        or even, apply also the measurement of that Quantum Entangled State, on the W State Basis,
        to allow the extraction of its final classical outcome/result.

        :param is_to_measure_at_w_state_basis: the boolean flag to keep the information about
                                               if it will be performed a measurement of
                                               the Qiskrypt's W State on the W State Basis.
        :param qiskit_classical_registers_indexes: the indexes of the IBM Qiskit's Classical Registers,
                                                   where it belongs the bits to store the final classical outcomes/results,
                                                   after be performed a measurement on the qubits inside
                                                   the IBM Qiskit's Quantum Registers.
        :param bits_indexes: the indexes of the bits inside the IBM Qiskit's Classical Registers,
                             where it will be stored the final classical outcomes/results,
                             after be performed a measurement on the qubits inside
                             the IBM Qiskit's Quantum Registers.
        """

        self.qiskrypt_quantum_circuit \
            .apply_barriers_set_qubits_in_set_qiskit_quantum_registers(self.qiskit_quantum_registers_indexes,
                                                                       self.qubits_indexes)
        """
        Apply barriers to the IBM Qiskit's Quantum Registers and the respective qubits.
        """

        num_quantum_registers = len(self.qiskit_quantum_registers_indexes)
        """
        Retrieve the number of the IBM Qiskit's Quantum Registers for the Qiskrypt's W State.
        """

        num_qubits = len(self.qubits_indexes)
        """
        Retrieve the number of qubits for the Qiskrypt's W State.
        """

        for qiskit_quantum_register_index, qubit_index in \
                zip(range((num_quantum_registers - 1)), range((num_qubits - 1))):
            """
            For each pair of indexes for an IBM Qiskit's Quantum Register and a qubit. 
            """

            self.qiskrypt_quantum_circuit\
                .apply_controlled_pauli_x(self.qiskit_quantum_registers_indexes[qiskit_quantum_register_index],
                                          self.qiskit_quantum_registers_indexes[(qiskit_quantum_register_index + 1)],
                                          self.qubits_indexes[qubit_index],
                                          self.qubits_indexes[(qubit_index + 1)])
            """
            Apply the Controlled-Pauli-X (Controlled-NOT) Gate/Operation to
            the given indexes of the control IBM Qiskit's Quantum Register and the respective qubit on it, as also,
            of the current target IBM Qiskit's Quantum Register and the current respective qubit on it.
            """

        for qiskit_quantum_register_index, qubit_index in \
                zip(range((num_quantum_registers - 1)), range((num_qubits - 1))):
            """
            For each pair of indexes for an IBM Qiskit's Quantum Register and a qubit. 
            """

            theta_radians = arccos(sqrt(1. / (qubit_index + 2)))
            """
            Compute the theta angle, in radians, from the Arc-Cosine function of
            the Square Root of the inverse of the index of the qubit inside
            the IBM Qiskit's Quantum Register.
            """

            self.qiskrypt_quantum_circuit\
                .apply_ry_radians(-theta_radians,
                                  self.qiskit_quantum_registers_indexes[(qiskit_quantum_register_index + 1)],
                                  self.qubits_indexes[qubit_index])
            """
            Apply the Rotation-Y (R_y(-theta_radians)) Gate/Operation, with the symmetric theta angle in radians,
            to the given indexes of the current index for the IBM Qiskit's Quantum Register and
            of the current index for the qubit on it.
            """

            self.qiskrypt_quantum_circuit\
                .apply_controlled_pauli_z(self.qiskit_quantum_registers_indexes[(qiskit_quantum_register_index + 1)],
                                          self.qiskit_quantum_registers_indexes[qiskit_quantum_register_index],
                                          self.qubits_indexes[(qubit_index + 1)],
                                          self.qubits_indexes[qubit_index])
            """
            Apply the Controlled-Pauli-Z (Controlled-Phase-Flip/Controlled-Phase-Shifter) Gate/Operation to
            the given indexes of the control IBM Qiskit's Quantum Register and the respective qubit on it, as also,
            of the current target IBM Qiskit's Quantum Register and the current respective qubit on it.
            """

            self.qiskrypt_quantum_circuit\
                .apply_ry_radians(theta_radians,
                                  self.qiskit_quantum_registers_indexes[(qiskit_quantum_register_index + 1)],
                                  self.qubits_indexes[qubit_index])
            """
            Apply the Rotation-Y (R_y(-theta_radians)) Gate/Operation, with the symmetric theta angle in radians,
            to the given indexes of the current index for the IBM Qiskit's Quantum Register and
            of the current index for the qubit on it.
            """

        self.qiskrypt_quantum_circuit.apply_pauli_x(self.qiskit_quantum_registers_indexes[(num_quantum_registers - 1)],
                                                    self.qubits_indexes[(num_qubits - 1)])
        """
        Apply the Pauli-X Gate/Operation to the given indexes of
        the last IBM Qiskit's Quantum Register and the respective qubit on it.
        """

        if is_to_measure_at_w_state_basis:
            """
            If the boolean flag to keep the information about
            if it will be performed a measurement of
            the Qiskrypt's W State on the W State Basis, is True.
            """

            if self.qiskrypt_quantum_circuit.get_total_num_bits() >= len(bits_indexes):
                """
                If the number of bits of the given Qiskrypt's Quantum Circuit is greater or equal than
                the number of the bits inside the IBM Qiskit's Classical Register.
                """

                self.qiskrypt_quantum_circuit\
                    .measure_set_qubits_in_set_qiskit_quantum_registers(self.qiskit_quantum_registers_indexes,
                                                                        qiskit_classical_registers_indexes,
                                                                        self.qubits_indexes,
                                                                        bits_indexes)
                """
                Measure the qubits in the IBM Qiskit's Quantum Registers into
                the respective bits in the IBM Qiskit's Classical Registers,
                inside the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit.
                """

            else:
                """
                If the number of bits of the given Qiskrypt's Quantum Circuit is lower than
                the number of the bits inside the IBM Qiskit's Classical Register.
                """

                # TODO - Throw Exception
