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

from src.entanglements.QiskryptQuantumEntanglement \
    import POSSIBLE_CONFIGURATIONS_BELL_STATES
"""
Import the available configurations for Bell States for
the Qiskrypt's Quantum Entanglement.
"""

from src.circuit.QiskryptQuantumCircuit \
    import QiskryptQuantumCircuit
"""
Import the Qiskrypt's Quantum Circuit.
"""


class QiskryptBellState(QiskryptQuantumEntanglement):
    """
    Object class for the Qiskrypt's Bell State.
    """

    def __init__(self, name: str, qiskrypt_quantum_circuit: QiskryptQuantumCircuit, bell_state_sub_type: str):
        """
        Constructor of the Qiskrypt's Bell State.

        :param name: the name of the Qiskrypt's Bell State.
        :param qiskrypt_quantum_circuit: the name of the Qiskrypt's Bell State.
        :param bell_state_sub_type: the sub-type of the Qiskrypt's Bell State.
        """

        if bell_state_sub_type in POSSIBLE_CONFIGURATIONS_BELL_STATES:
            """
            If the Qiskrypt's Quantum Entanglement is a valid Bell State.
            """

            if (qiskrypt_quantum_circuit.get_total_num_qubits() >= 2) \
                and (qiskrypt_quantum_circuit.get_total_num_bits() >= 2):
                """
                If the number of qubits and bits of
                the given Qiskrypt's Quantum Circuit is greater or equal than 2.
                """

                super().__init__(name, POSSIBLE_QUANTUM_ENTANGLEMENT_CARDINALITIES[0],
                                 POSSIBLE_QUANTUM_ENTANGLEMENT_TYPES[0],
                                 qiskrypt_quantum_circuit, bell_state_sub_type)
                """
                Calls the constructor of the super-class Qiskrypt's Quantum Entanglement.
                """

                self.qiskit_quantum_register_control_index = None
                """
                Set the index of the control IBM Qiskit's Quantum Register, as None.
                """

                self.qiskit_quantum_register_target_index = None
                """
                Set the index of the target IBM Qiskit's Quantum Register, as None.
                """

                self.control_qubit_index = None
                """
                Set the index of a qubit inside the control IBM Qiskit's Quantum Register, as None.
                """

                self.target_qubit_index = None
                """
                Set the index of a qubit inside the target IBM Qiskit's Quantum Register, as None.
                """

            else:
                """
                If the number of qubits and bits of
                the given Qiskrypt's Quantum Circuit is strictly lower than 2.
                """

                # TODO - Throw Exception

        else:
            """
            If the Qiskrypt's Quantum Entanglement is not a valid Bell State.
            """

            # TODO - Throw Exception

    def get_name(self):
        """
        Return the name of the Qiskrypt's Bell State.

        :return super().get_name(): the name of the Qiskrypt's Bell State.
        """

        """
        Return the name of the Qiskrypt's Bell State.
        """
        return super().get_name()

    def get_quantum_entanglement_cardinality(self):
        """
        Return the cardinality of the Qiskrypt's Bell State.

        :return super().get_quantum_entanglement_cardinality(): the cardinality of
                                                                the Qiskrypt's Bell State.
        """

        """
        Return the cardinality of the Qiskrypt's Bell State.
        """
        return super().get_quantum_entanglement_cardinality()

    def get_quantum_entanglement_type(self):
        """
        Return the type of the Qiskrypt's Bell State.

        :return super().get_quantum_entanglement_type(): the type of the Qiskrypt's Bell State.
        """

        """
        Return the type of the Qiskrypt's Bell State.
        """
        return super().get_quantum_entanglement_type()

    def get_qiskrypt_quantum_circuit(self):
        """
        Return the Qiskrypt's Quantum Circuit,
        from which it will be configured the Qiskrypt's Bell State.

        :return super().get_qiskrypt_quantum_circuit(): the Qiskrypt's Quantum Circuit,
                                                        from which it will be configured
                                                        the Qiskrypt's Bell State.
        """

        """
        Return the Qiskrypt's Quantum Circuit,
        from which it will be configured the Qiskrypt's Bell State.
        """
        return super().get_qiskrypt_quantum_circuit()

    def get_bell_state_sub_type(self):
        """
        Return the sub-type of the Qiskrypt's Bell State.

        :return super().get_bell_state_sub_type(): the sub-type of the Qiskrypt's Bell State.
        """

        """
        Return the sub-type of the Qiskrypt's Bell State.
        """
        return super().get_bell_state_sub_type()

    def configure(self, qiskit_quantum_register_control_index: int,
                  qiskit_quantum_register_target_index: int,
                  control_qubit_index: int, target_qubit_index: int) -> None:
        """
        Configure the Qiskrypt's Bell State,
        regarding its control IBM Qiskit's Quantum Register and control qubit,
        as well, its target IBM Qiskit's Quantum Register and target qubit.

        :param qiskit_quantum_register_control_index: the index of the control IBM Qiskit's Quantum Register.
        :param qiskit_quantum_register_target_index: the index of the target IBM Qiskit's Quantum Register.
        :param control_qubit_index: the index of a qubit inside the control IBM Qiskit's Quantum Register.
        :param target_qubit_index: the index of a qubit inside the target IBM Qiskit's Quantum Register.
        """

        self.qiskit_quantum_register_control_index = qiskit_quantum_register_control_index
        """
        Set the index of the control IBM Qiskit's Quantum Register, as the given index for it.
        """

        self.qiskit_quantum_register_target_index = qiskit_quantum_register_target_index
        """
        Set the index of the target IBM Qiskit's Quantum Register, as the given index for it.
        """

        self.control_qubit_index = control_qubit_index
        """
        Set the index of a qubit inside the control IBM Qiskit's Quantum Register,
        as the given index for it.
        """

        self.target_qubit_index = target_qubit_index
        """
        Set the index of a qubit inside the target IBM Qiskit's Quantum Register,
        as the given index for it.
        """

    def prepare_bipartite_entanglement(self, is_to_measure_at_computational_basis=False,
                                       qiskit_classical_register_control_index=None,
                                       qiskit_classical_register_target_index=None,
                                       control_bit_index=None, target_bit_index=None) -> None:
        """
        Prepare the Bipartite Quantum Entanglement,
        for the specified Qiskrypt's Bell State, as a quantum entangled state,
        or even, apply also the measurement of that Quantum Entangled State, on the Computational Basis,
        to allow the extraction of its final classical outcome/result.

        :param is_to_measure_at_computational_basis: the boolean flag to keep the information about
                                                     if it will be performed a measurement of
                                                     the Qiskrypt's Bell State on the Computational Basis.
        :param qiskit_classical_register_control_index: the index of the control IBM Qiskit's Classical Register,
                                                        where it belongs the bit to store the final classical outcome/result,
                                                        after be performed a measurement on the qubit inside
                                                        the control IBM Qiskit's Quantum Register.
        :param qiskit_classical_register_target_index: the index of the target IBM Qiskit's Classical Register,
                                                       where it belongs the bit to store the final classical outcome/result,
                                                       after be performed a measurement on the qubit inside
                                                       the target IBM Qiskit's Quantum Register.
        :param control_bit_index: the index of a bit inside the control IBM Qiskit's Classical Register,
                                  where it will be stored the final classical outcome/result,
                                  after be performed a measurement on the qubit inside
                                  the control IBM Qiskit's Quantum Register.
        :param target_bit_index: the index of a bit inside the target IBM Qiskit's Classical Register,
                                 where it will be stored the final classical outcome/result,
                                 after be performed a measurement on the qubit inside
                                 the target IBM Qiskit's Quantum Register.
        """

        self.qiskrypt_quantum_circuit\
            .apply_barrier_to_single_qubit_in_qiskit_quantum_register(self.qiskit_quantum_register_control_index,
                                                                      self.control_qubit_index)
        """
        Apply a barrier to the control IBM Qiskit's Quantum Register and the respective control qubit.
        """

        self.qiskrypt_quantum_circuit\
            .apply_barrier_to_single_qubit_in_qiskit_quantum_register(self.qiskit_quantum_register_target_index,
                                                                      self.target_qubit_index)
        """
        Apply a barrier to the target IBM Qiskit's Quantum Register and the respective control qubit.
        """

        if (self.get_bell_state_sub_type() == POSSIBLE_CONFIGURATIONS_BELL_STATES[0]) \
            or (self.get_bell_state_sub_type() == POSSIBLE_CONFIGURATIONS_BELL_STATES[1]):
            """
            If the sub-type of the Qiskrypt's Bell State is, |ϕ^+⟩ = 1/sqrt(2) x (|00⟩ + |11⟩)
            (also known as, EPR Pair).
            """

            self.qiskrypt_quantum_circuit.apply_hadamard(self.qiskit_quantum_register_control_index,
                                                         self.control_qubit_index)
            """
            Apply the Hadamard Gate/Operation to the given indexes of
            the control IBM Qiskit's Quantum Register and the respective control qubit on it.
            """

            self.qiskrypt_quantum_circuit\
                .apply_controlled_pauli_x(self.qiskit_quantum_register_control_index,
                                          self.control_qubit_index,
                                          self.qiskit_quantum_register_target_index,
                                          self.target_qubit_index)
            """
            Apply the Controlled-Pauli-X (Controlled-NOT) Gate/Operation to given indexes of
            the control IBM Qiskit's Quantum Register and the respective qubit on it, as also,
            the target IBM Qiskit's Quantum Register and the respective qubit on it. 
            """

        elif self.get_bell_state_sub_type() == POSSIBLE_CONFIGURATIONS_BELL_STATES[2]:
            """
            If the sub-type of the Qiskrypt's Bell State is, |ϕ^-⟩ = 1/sqrt(2) x (|00⟩ - |11⟩).
            """

            self.qiskrypt_quantum_circuit.apply_hadamard(self.qiskit_quantum_register_control_index,
                                                         self.control_qubit_index)
            """
            Apply the Hadamard Gate/Operation to the given indexes of
            the control IBM Qiskit's Quantum Register and the respective control qubit on it.
            """

            self.qiskrypt_quantum_circuit.apply_pauli_z(self.qiskit_quantum_register_control_index,
                                                        self.control_qubit_index)
            """
            Apply the Pauli-Z (Phase Flip/Shift) Gate/Operation to the given indexes of
            the control IBM Qiskit's Quantum Register and the respective control qubit on it.
            """

            self.qiskrypt_quantum_circuit\
                .apply_controlled_pauli_x(self.qiskit_quantum_register_control_index,
                                          self.control_qubit_index,
                                          self.qiskit_quantum_register_target_index,
                                          self.target_qubit_index)
            """
            Apply the Controlled-Pauli-X (Controlled-NOT) Gate/Operation to given indexes of
            the control IBM Qiskit's Quantum Register and the respective qubit on it, as also,
            the target IBM Qiskit's Quantum Register and the respective qubit on it. 
            """

        elif self.get_bell_state_sub_type() == POSSIBLE_CONFIGURATIONS_BELL_STATES[3]:
            """
            If the sub-type of the Qiskrypt's Bell State is, |ψ^+⟩ = 1/sqrt(2) x (|01⟩ + |10⟩).
            """

            self.qiskrypt_quantum_circuit.apply_hadamard(self.qiskit_quantum_register_control_index,
                                                         self.control_qubit_index)
            """
            Apply the Hadamard Gate/Operation to the given indexes of
            the control IBM Qiskit's Quantum Register and the respective control qubit on it.
            """

            self.qiskrypt_quantum_circuit.apply_pauli_x(self.qiskit_quantum_register_target_index,
                                                        self.target_qubit_index)
            """
            Apply the Pauli-X (NOT/Bit Flip) Gate/Operation to the given indexes of
            the target IBM Qiskit's Quantum Register and the respective target qubit on it.
            """

            self.qiskrypt_quantum_circuit\
                .apply_controlled_pauli_x(self.qiskit_quantum_register_control_index,
                                          self.control_qubit_index,
                                          self.qiskit_quantum_register_target_index,
                                          self.target_qubit_index)
            """
            Apply the Controlled-Pauli-X (Controlled-NOT) Gate/Operation to given indexes of
            the control IBM Qiskit's Quantum Register and the respective qubit on it, as also,
            the target IBM Qiskit's Quantum Register and the respective qubit on it. 
            """

        elif self.get_bell_state_sub_type() == POSSIBLE_CONFIGURATIONS_BELL_STATES[4]:
            """
            If the sub-type of the Qiskrypt's Bell State is, |ψ^+⟩ = 1/sqrt(2) x (|01⟩ - |10⟩).
            """

            self.qiskrypt_quantum_circuit.apply_hadamard(self.qiskit_quantum_register_control_index,
                                                         self.control_qubit_index)
            """
            Apply the Hadamard Gate/Operation to the given indexes of
            the control IBM Qiskit's Quantum Register and the respective control qubit on it.
            """

            self.qiskrypt_quantum_circuit.apply_pauli_x(self.qiskit_quantum_register_target_index,
                                                        self.target_qubit_index)
            """
            Apply the Pauli-X (NOT/Bit Flip) Gate/Operation to the given indexes of
            the target IBM Qiskit's Quantum Register and the respective target qubit on it.
            """

            self.qiskrypt_quantum_circuit\
                .apply_controlled_pauli_x(self.qiskit_quantum_register_control_index,
                                          self.control_qubit_index,
                                          self.qiskit_quantum_register_target_index,
                                          self.target_qubit_index)
            """
            Apply the Controlled-Pauli-X (Controlled-NOT) Gate/Operation to given indexes of
            the control IBM Qiskit's Quantum Register and the respective qubit on it, as also,
            the target IBM Qiskit's Quantum Register and the respective qubit on it. 
            """

            self.qiskrypt_quantum_circuit.apply_pauli_z(self.qiskit_quantum_register_target_index,
                                                        self.target_qubit_index)
            """
            Apply the Pauli-Z (Phase Flip/Shift) Gate/Operation to the given indexes of
            the target IBM Qiskit's Quantum Register and the respective target qubit on it.
            """

        self.qiskrypt_quantum_circuit\
            .apply_barrier_to_single_qubit_in_qiskit_quantum_register(self.qiskit_quantum_register_control_index,
                                                                      self.control_qubit_index)
        """
        Apply a barrier to the control IBM Qiskit's Quantum Register and the respective control qubit.
        """

        self.qiskrypt_quantum_circuit\
            .apply_barrier_to_single_qubit_in_qiskit_quantum_register(self.qiskit_quantum_register_target_index,
                                                                      self.target_qubit_index)
        """
        Apply a barrier to the target IBM Qiskit's Quantum Register and the respective control qubit.
        """

        if is_to_measure_at_computational_basis:
            """
            If the boolean flag to keep the information about
            if it will be performed a measurement of
            the Qiskrypt's Bell State on the Computational Basis, is True.
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
                .measure_single_qubit_in_qiskit_quantum_register(self.qiskit_quantum_register_target_index,
                                                                 qiskit_classical_register_target_index,
                                                                 self.target_qubit_index, target_bit_index)
            """
            Measure the target qubit in the target IBM Qiskit's Quantum Register into
            the respective target bit in the target IBM Qiskit's Classical Register,
            inside the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit.
            """

    def measure_bipartite_entanglement_at_bell_state_basis(self, is_to_measure_at_bell_state_basis=False,
                                                           qiskit_classical_register_control_index=None,
                                                           qiskit_classical_register_target_index=None,
                                                           control_bit_index=None, target_bit_index=None) -> None:
        """
        Perform all the necessary Quantum Gates/Operations to prepare the Qiskrypt's Bell State,
        at the Bell State Basis, or even, apply also the measurements,
        to allow the extraction of its final classical outcome/result.

        :param is_to_measure_at_bell_state_basis: the boolean flag to keep the information about
                                                  if it will be performed a measurement of
                                                  the Qiskrypt's Bell State on the Bell State Basis.
        :param qiskit_classical_register_control_index: the index of the control IBM Qiskit's Classical Register,
                                                        where it belongs the bit to store the final classical outcome/result,
                                                        after be performed a measurement on the qubit inside
                                                        the control IBM Qiskit's Quantum Register.
        :param qiskit_classical_register_target_index: the index of the target IBM Qiskit's Classical Register,
                                                       where it belongs the bit to store the final classical outcome/result,
                                                       after be performed a measurement on the qubit inside
                                                       the target IBM Qiskit's Quantum Register.
        :param control_bit_index: the index of a bit inside the control IBM Qiskit's Classical Register,
                                  where it will be stored the final classical outcome/result,
                                  after be performed a measurement on the qubit inside
                                  the control IBM Qiskit's Quantum Register.
        :param target_bit_index: the index of a bit inside the target IBM Qiskit's Classical Register,
                                 where it will be stored the final classical outcome/result,
                                 after be performed a measurement on the qubit inside
                                 the target IBM Qiskit's Quantum Register.
        """

        self.qiskrypt_quantum_circuit \
            .apply_barrier_to_single_qubit_in_qiskit_quantum_register(self.qiskit_quantum_register_control_index,
                                                                      self.control_qubit_index)
        """
        Apply a barrier to the control IBM Qiskit's Quantum Register and the respective control qubit.
        """

        self.qiskrypt_quantum_circuit \
            .apply_barrier_to_single_qubit_in_qiskit_quantum_register(self.qiskit_quantum_register_target_index,
                                                                      self.target_qubit_index)
        """
        Apply a barrier to the target IBM Qiskit's Quantum Register and the respective control qubit.
        """

        if (self.get_bell_state_sub_type() == POSSIBLE_CONFIGURATIONS_BELL_STATES[0]) \
            or (self.get_bell_state_sub_type() == POSSIBLE_CONFIGURATIONS_BELL_STATES[1]):
            """
            If the sub-type of the Qiskrypt's Bell State is, |ϕ^+⟩ = 1/sqrt(2) x (|00⟩ + |11⟩)
            (also known as, EPR Pair).
            """

            self.qiskrypt_quantum_circuit\
                .apply_controlled_pauli_x(self.qiskit_quantum_register_control_index,
                                          self.control_qubit_index,
                                          self.qiskit_quantum_register_target_index,
                                          self.target_qubit_index)
            """
            Apply the Controlled-Pauli-X (Controlled-NOT) Gate/Operation to given indexes of
            the control IBM Qiskit's Quantum Register and the respective qubit on it, as also,
            the target IBM Qiskit's Quantum Register and the respective qubit on it. 
            """

            self.qiskrypt_quantum_circuit.apply_hadamard(self.qiskit_quantum_register_control_index,
                                                         self.control_qubit_index)
            """
            Apply the Hadamard Gate/Operation to the given indexes of
            the control IBM Qiskit's Quantum Register and the respective control qubit on it.
            """

        elif self.get_bell_state_sub_type() == POSSIBLE_CONFIGURATIONS_BELL_STATES[2]:
            """
            If the sub-type of the Qiskrypt's Bell State is, |ϕ^-⟩ = 1/sqrt(2) x (|00⟩ - |11⟩).
            """

            self.qiskrypt_quantum_circuit\
                .apply_controlled_pauli_x(self.qiskit_quantum_register_control_index,
                                          self.control_qubit_index,
                                          self.qiskit_quantum_register_target_index,
                                          self.target_qubit_index)
            """
            Apply the Controlled-Pauli-X (Controlled-NOT) Gate/Operation to given indexes of
            the control IBM Qiskit's Quantum Register and the respective qubit on it, as also,
            the target IBM Qiskit's Quantum Register and the respective qubit on it. 
            """

            self.qiskrypt_quantum_circuit.apply_pauli_z(self.qiskit_quantum_register_control_index,
                                                        self.control_qubit_index)
            """
            Apply the Pauli-Z (Phase Flip/Shift) Gate/Operation to the given indexes of
            the control IBM Qiskit's Quantum Register and the respective control qubit on it.
            """

            self.qiskrypt_quantum_circuit.apply_hadamard(self.qiskit_quantum_register_control_index,
                                                         self.control_qubit_index)
            """
            Apply the Hadamard Gate/Operation to the given indexes of
            the control IBM Qiskit's Quantum Register and the respective control qubit on it.
            """

        elif self.get_bell_state_sub_type() == POSSIBLE_CONFIGURATIONS_BELL_STATES[3]:
            """
            If the sub-type of the Qiskrypt's Bell State is, |ψ^+⟩ = 1/sqrt(2) x (|01⟩ + |10⟩).
            """

            self.qiskrypt_quantum_circuit\
                .apply_controlled_pauli_x(self.qiskit_quantum_register_control_index,
                                          self.control_qubit_index,
                                          self.qiskit_quantum_register_target_index,
                                          self.target_qubit_index)
            """
            Apply the Controlled-Pauli-X (Controlled-NOT) Gate/Operation to given indexes of
            the control IBM Qiskit's Quantum Register and the respective qubit on it, as also,
            the target IBM Qiskit's Quantum Register and the respective qubit on it. 
            """

            self.qiskrypt_quantum_circuit.apply_pauli_x(self.qiskit_quantum_register_target_index,
                                                        self.target_qubit_index)
            """
            Apply the Pauli-X (NOT/Bit Flip) Gate/Operation to the given indexes of
            the target IBM Qiskit's Quantum Register and the respective target qubit on it.
            """

            self.qiskrypt_quantum_circuit.apply_hadamard(self.qiskit_quantum_register_control_index,
                                                         self.control_qubit_index)
            """
            Apply the Hadamard Gate/Operation to the given indexes of
            the control IBM Qiskit's Quantum Register and the respective control qubit on it.
            """

        elif self.get_bell_state_sub_type() == POSSIBLE_CONFIGURATIONS_BELL_STATES[4]:
            """
            If the sub-type of the Qiskrypt's Bell State is, |ψ^+⟩ = 1/sqrt(2) x (|01⟩ - |10⟩).
            """

            self.qiskrypt_quantum_circuit.apply_pauli_z(self.qiskit_quantum_register_target_index,
                                                        self.target_qubit_index)
            """
            Apply the Pauli-Z (Phase Flip/Shift) Gate/Operation to the given indexes of
            the target IBM Qiskit's Quantum Register and the respective target qubit on it.
            """

            self.qiskrypt_quantum_circuit\
                .apply_controlled_pauli_x(self.qiskit_quantum_register_control_index,
                                          self.control_qubit_index,
                                          self.qiskit_quantum_register_target_index,
                                          self.target_qubit_index)
            """
            Apply the Controlled-Pauli-X (Controlled-NOT) Gate/Operation to given indexes of
            the control IBM Qiskit's Quantum Register and the respective qubit on it, as also,
            the target IBM Qiskit's Quantum Register and the respective qubit on it. 
            """

            self.qiskrypt_quantum_circuit.apply_pauli_x(self.qiskit_quantum_register_target_index,
                                                        self.target_qubit_index)
            """
            Apply the Pauli-X (NOT/Bit Flip) Gate/Operation to the given indexes of
            the target IBM Qiskit's Quantum Register and the respective target qubit on it.
            """

            self.qiskrypt_quantum_circuit.apply_hadamard(self.qiskit_quantum_register_control_index,
                                                         self.control_qubit_index)
            """
            Apply the Hadamard Gate/Operation to the given indexes of
            the control IBM Qiskit's Quantum Register and the respective control qubit on it.
            """

        if is_to_measure_at_bell_state_basis:
            """
            If the boolean flag to keep the information about
            if it will be performed a measurement of
            the Qiskrypt's Bell State on the Bell State Basis, is True.
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
                .measure_single_qubit_in_qiskit_quantum_register(self.qiskit_quantum_register_target_index,
                                                                 qiskit_classical_register_target_index,
                                                                 self.target_qubit_index, target_bit_index)
            """
            Measure the target qubit in the target IBM Qiskit's Quantum Register into
            the respective target bit in the target IBM Qiskit's Classical Register,
            inside the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit.
            """