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

from unittest import TestCase, TestLoader, TestSuite
"""
Import TestCase, TestLoader and TestSuite from Unittest.
"""

from numpy import array, sqrt
"""
Import the N-Dimensional Arrays and Square Root functions from Python's NumPy.
"""

from numpy.testing import assert_allclose
"""
Import the function for the assertion of all close values of an array,
allowing a small value of error of the Testing Module from Python's NumPy.
"""

from qiskit import Aer, execute
"""
Import Aer Simulator and the Execute function from IBM's Qiskit.
"""

from src.quantum.circuit.registers.quantum.QiskryptQuantumRegister \
    import QiskryptQuantumRegister
"""
Import the Qiskrypt's Quantum Register.
"""

from src.quantum.circuit \
    import QiskryptQuantumCircuit
"""
Import the Qiskrypt's Quantum Circuit.
"""

from src.quantum.entanglements.bipartite.QiskryptBellState \
    import QiskryptBellState
"""
Import the Qiskrypt's Bell State.
"""


"""
Import required Constants and Enumerations.
"""

from src.quantum.entanglements.QiskryptQuantumEntanglement \
    import POSSIBLE_CONFIGURATIONS_BELL_STATES
"""
Import the available configurations for Bell States for
the Qiskrypt's Quantum Entanglement. 
"""


class QiskryptBellStateTests(TestCase):
    """
    Object Class of the Unitary Tests for the Qiskrypt's Bell State.
    """

    def test_no_1_prepare_computational_basis_qiskrypt_bell_state_phi_plus_epr_pair(self):
        """
        Test Case #1:

        - Initialise the Qiskrypt's Bell State and prepare it, as an Entangled Quantum State,
          in the Computational Basis.

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Bell State is initialised and configured;
        2) The Qiskrypt's Bell State with the configuration,
           |ϕ^+⟩ = 1/sqrt(2) x (|00⟩ + |11⟩) (also known as, EPR Pair),
           is prepared, without measuring it, on the Computational Basis;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        quantum_register_name = "qu_reg"
        """
        Set the name of the Qiskrypt's Quantum Register.
        """

        quantum_register_num_qubits = 2
        """
        Set the number of qubits for the Qiskrypt's Quantum Register.
        """

        qiskrypt_quantum_register = \
            QiskryptQuantumRegister(name=quantum_register_name,
                                    num_qubits=quantum_register_num_qubits,
                                    qiskit_quantum_register=None)
        """
        Create a Qiskrypt's Quantum Register, given its name and number of qubits.
        """

        quantum_circuit_name = "qu_circ"
        """
        Set the name of the Qiskrypt's Quantum Circuit.
        """

        qiskrypt_quantum_circuit_bell_state_phi_plus_epr_pair_1 = \
            QiskryptQuantumCircuit(name=quantum_circuit_name,
                                   qiskrypt_quantum_registers=[qiskrypt_quantum_register],
                                   qiskrypt_fully_quantum_registers=None,
                                   qiskrypt_semi_quantum_registers=None,
                                   qiskrypt_ancilla_quantum_registers=None,
                                   qiskrypt_ancilla_fully_quantum_registers=None,
                                   qiskrypt_ancilla_semi_quantum_registers=None,
                                   qiskrypt_classical_registers=None,
                                   global_phase=0)
        """
        Create a Qiskrypt's Quantum Circuit, given its name,
        Qiskrypt's Quantum Registers, Qiskrypt's Fully-Quantum Registers,
        Qiskrypt's Semi-Quantum Registers,
        Qiskrypt's Ancilla Quantum Registers, Qiskrypt's Ancilla Fully-Quantum Registers,
        Qiskrypt's Ancilla Semi-Quantum Registers,
        Qiskrypt's Classical Registers and
        Global Phase.
        """

        qiskrypt_bell_state_phi_plus_epr_pair_1 = \
            QiskryptBellState("bell_state_phi_plus_epr_pair_1",
                              qiskrypt_quantum_circuit_bell_state_phi_plus_epr_pair_1,
                              POSSIBLE_CONFIGURATIONS_BELL_STATES[0])
        """
        Create a Qiskrypt's Bell State, for a generation of a Bell's State with the configuration,
        |ϕ^+⟩ = 1/sqrt(2) x (|00⟩ + |11⟩) (also known as, EPR Pair).
        """

        qiskrypt_bell_state_phi_plus_epr_pair_1.configure(0, 0, 0, 1)
        """
        Configure the Qiskrypt's Bell State, regarding its control IBM Qiskit's Quantum Register
        and control qubit, as well, its target IBM Qiskit's Quantum Register and target qubit.
        """

        qiskrypt_bell_state_phi_plus_epr_pair_1\
            .prepare_bipartite_entanglement_at_computational_basis(is_to_measure_at_computational_basis=False,
                                                                   qiskit_classical_register_control_index=None,
                                                                   qiskit_classical_register_target_index=None,
                                                                   control_bit_index=None, target_bit_index=None)
        """
        Prepare the Bipartite Quantum Entanglement,
        for the specified Qiskrypt's Bell State, as a Quantum Entangled State,
        without measure it, on the Computational Basis.
        """

        qiskit_state_vector_backend = Aer.get_backend("statevector_simulator")
        """
        Getting the Aer Simulator Backend for the State Vector Representation
        (i.e., the quantum state represented as its state vector).
        """

        final_quantum_state_vector_state = \
            execute(qiskrypt_bell_state_phi_plus_epr_pair_1.qiskrypt_quantum_circuit.qiskit_quantum_circuit,
                    qiskit_state_vector_backend).result().get_statevector()
        """
        Execute the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit
        and store the resulted quantum state represented in a final state vector.
        """

        assert_allclose(final_quantum_state_vector_state,
                        array([((1. / sqrt(2.)) + 0.j),
                               (0. + 0.j),
                               (0. + 0.j),
                               ((1. / sqrt(2.)) + 0.j)]),
                        rtol=1e-7, atol=1e-7)
        """
        Perform the Assertion of all close values in the values of the quantum state,
        represented by its state vector describing the given qubits,
        after be prepared a Bell's State with the configuration,
        |ϕ^+⟩ = 1/sqrt(2) x (|00⟩ + |11⟩) (also known as, EPR Pair).
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_2_prepare_computational_basis_qiskrypt_bell_state_phi_minus(self):
        """
        Test Case #2:

        - Initialise the Qiskrypt's Bell State and prepare it, as an Entangled Quantum State,
          in the Computational Basis.

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Bell State is initialised and configured;
        2) The Qiskrypt's Bell State with the configuration,
           |ϕ^-⟩ = 1/sqrt(2) x (|00⟩ - |11⟩),
           is prepared, without measuring it, on the Computational Basis;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        quantum_register_name = "qu_reg"
        """
        Set the name of the Qiskrypt's Quantum Register.
        """

        quantum_register_num_qubits = 2
        """
        Set the number of qubits for the Qiskrypt's Quantum Register.
        """

        qiskrypt_quantum_register = \
            QiskryptQuantumRegister(name=quantum_register_name,
                                    num_qubits=quantum_register_num_qubits,
                                    qiskit_quantum_register=None)
        """
        Create a Qiskrypt's Quantum Register, given its name and number of qubits.
        """

        quantum_circuit_name = "qu_circ"
        """
        Set the name of the Qiskrypt's Quantum Circuit.
        """

        qiskrypt_quantum_circuit_bell_state_phi_minus_2 = \
            QiskryptQuantumCircuit(name=quantum_circuit_name,
                                   qiskrypt_quantum_registers=[qiskrypt_quantum_register],
                                   qiskrypt_fully_quantum_registers=None,
                                   qiskrypt_semi_quantum_registers=None,
                                   qiskrypt_ancilla_quantum_registers=None,
                                   qiskrypt_ancilla_fully_quantum_registers=None,
                                   qiskrypt_ancilla_semi_quantum_registers=None,
                                   qiskrypt_classical_registers=None,
                                   global_phase=0)
        """
        Create a Qiskrypt's Quantum Circuit, given its name,
        Qiskrypt's Quantum Registers, Qiskrypt's Fully-Quantum Registers,
        Qiskrypt's Semi-Quantum Registers,
        Qiskrypt's Ancilla Quantum Registers, Qiskrypt's Ancilla Fully-Quantum Registers,
        Qiskrypt's Ancilla Semi-Quantum Registers,
        Qiskrypt's Classical Registers and
        Global Phase.
        """

        qiskrypt_bell_state_phi_minus_2 = \
            QiskryptBellState("bell_state_phi_minus_2",
                              qiskrypt_quantum_circuit_bell_state_phi_minus_2,
                              POSSIBLE_CONFIGURATIONS_BELL_STATES[2])
        """
        Create a Qiskrypt's Bell State, for a generation of a Bell's State with the configuration,
        |ϕ^-⟩ = 1/sqrt(2) x (|00⟩ - |11⟩).
        """

        qiskrypt_bell_state_phi_minus_2.configure(0, 0, 0, 1)
        """
        Configure the Qiskrypt's Bell State, regarding its control IBM Qiskit's Quantum Register
        and control qubit, as well, its target IBM Qiskit's Quantum Register and target qubit.
        """

        qiskrypt_bell_state_phi_minus_2\
            .prepare_bipartite_entanglement_at_computational_basis(is_to_measure_at_computational_basis=False,
                                                                   qiskit_classical_register_control_index=None,
                                                                   qiskit_classical_register_target_index=None,
                                                                   control_bit_index=None, target_bit_index=None)
        """
        Prepare the Bipartite Quantum Entanglement,
        for the specified Qiskrypt's Bell State, as a Quantum Entangled State,
        without measure it, on the Computational Basis.
        """

        qiskit_state_vector_backend = Aer.get_backend("statevector_simulator")
        """
        Getting the Aer Simulator Backend for the State Vector Representation
        (i.e., the quantum state represented as its state vector).
        """

        final_quantum_state_vector_state = \
            execute(qiskrypt_bell_state_phi_minus_2.qiskrypt_quantum_circuit.qiskit_quantum_circuit,
                    qiskit_state_vector_backend).result().get_statevector()
        """
        Execute the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit
        and store the resulted quantum state represented in a final state vector.
        """

        assert_allclose(final_quantum_state_vector_state,
                        array([((1. / sqrt(2.)) + 0.j),
                               (0. + 0.j),
                               (0. + 0.j),
                               -((1. / sqrt(2.)) + 0.j)]),
                        rtol=1e-7, atol=1e-7)
        """
        Perform the Assertion of all close values in the values of the quantum state,
        represented by its state vector describing the given qubits,
        after be prepared a Bell's State with the configuration,
        |ϕ^-⟩ = 1/sqrt(2) x (|00⟩ - |11⟩).
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_3_prepare_computational_basis_qiskrypt_bell_state_phi_plus_epr_pair(self):
        """
        Test Case #3:

        - Initialise the Qiskrypt's Bell State and prepare it, as an Entangled Quantum State,
          in the Computational Basis.

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Bell State is initialised and configured;
        2) The Qiskrypt's Bell State with the configuration,
           |ψ^+⟩ = 1/sqrt(2) x (|01⟩ + |10⟩),
           is prepared, without measuring it, on the Computational Basis;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        quantum_register_name = "qu_reg"
        """
        Set the name of the Qiskrypt's Quantum Register.
        """

        quantum_register_num_qubits = 2
        """
        Set the number of qubits for the Qiskrypt's Quantum Register.
        """

        qiskrypt_quantum_register = \
            QiskryptQuantumRegister(name=quantum_register_name,
                                    num_qubits=quantum_register_num_qubits,
                                    qiskit_quantum_register=None)
        """
        Create a Qiskrypt's Quantum Register, given its name and number of qubits.
        """

        quantum_circuit_name = "qu_circ"
        """
        Set the name of the Qiskrypt's Quantum Circuit.
        """

        qiskrypt_quantum_circuit_bell_state_psi_plus_3 = \
            QiskryptQuantumCircuit(name=quantum_circuit_name,
                                   qiskrypt_quantum_registers=[qiskrypt_quantum_register],
                                   qiskrypt_fully_quantum_registers=None,
                                   qiskrypt_semi_quantum_registers=None,
                                   qiskrypt_ancilla_quantum_registers=None,
                                   qiskrypt_ancilla_fully_quantum_registers=None,
                                   qiskrypt_ancilla_semi_quantum_registers=None,
                                   qiskrypt_classical_registers=None,
                                   global_phase=0)
        """
        Create a Qiskrypt's Quantum Circuit, given its name,
        Qiskrypt's Quantum Registers, Qiskrypt's Fully-Quantum Registers,
        Qiskrypt's Semi-Quantum Registers,
        Qiskrypt's Ancilla Quantum Registers, Qiskrypt's Ancilla Fully-Quantum Registers,
        Qiskrypt's Ancilla Semi-Quantum Registers,
        Qiskrypt's Classical Registers and
        Global Phase.
        """

        qiskrypt_bell_state_bell_state_psi_plus_3 = \
            QiskryptBellState("bell_state_psi_plus_3", qiskrypt_quantum_circuit_bell_state_psi_plus_3,
                              POSSIBLE_CONFIGURATIONS_BELL_STATES[3])
        """
        Create a Qiskrypt's Bell State, for a generation of a Bell's State with the configuration,
        |ψ^+⟩ = 1/sqrt(2) x (|01⟩ + |10⟩).
        """

        qiskrypt_bell_state_bell_state_psi_plus_3.configure(0, 0, 0, 1)
        """
        Configure the Qiskrypt's Bell State, regarding its control IBM Qiskit's Quantum Register
        and control qubit, as well, its target IBM Qiskit's Quantum Register and target qubit.
        """

        qiskrypt_bell_state_bell_state_psi_plus_3\
            .prepare_bipartite_entanglement_at_computational_basis(is_to_measure_at_computational_basis=False,
                                                                   qiskit_classical_register_control_index=None,
                                                                   qiskit_classical_register_target_index=None,
                                                                   control_bit_index=None, target_bit_index=None)
        """
        Prepare the Bipartite Quantum Entanglement,
        for the specified Qiskrypt's Bell State, as a Quantum Entangled State,
        without measure it, on the Computational Basis.
        """

        qiskit_state_vector_backend = Aer.get_backend("statevector_simulator")
        """
        Getting the Aer Simulator Backend for the State Vector Representation
        (i.e., the quantum state represented as its state vector).
        """

        final_quantum_state_vector_state = \
            execute(qiskrypt_bell_state_bell_state_psi_plus_3.qiskrypt_quantum_circuit.qiskit_quantum_circuit,
                    qiskit_state_vector_backend).result().get_statevector()
        """
        Execute the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit
        and store the resulted quantum state represented in a final state vector.
        """

        assert_allclose(final_quantum_state_vector_state,
                        array([(0. + 0.j),
                               ((1. / sqrt(2.)) + 0.j),
                               ((1. / sqrt(2.)) + 0.j),
                               (0. + 0.j)]),
                        rtol=1e-7, atol=1e-7)
        """
        Perform the Assertion of all close values in the values of the quantum state,
        represented by its state vector describing the given qubits,
        after be prepared a Bell's State with the configuration,
        |ψ^+⟩ = 1/sqrt(2) x (|01⟩ + |10⟩).
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_4_prepare_computational_basis_qiskrypt_bell_state_psi_minus(self):
        """
        Test Case #4:

        - Initialise the Qiskrypt's Bell State and prepare it, as an Entangled Quantum State,
          in the Computational Basis.

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Bell State is initialised and configured;
        2) The Qiskrypt's Bell State with the configuration,
           |ψ^-⟩ = 1/sqrt(2) x (|01⟩ - |10⟩),
           is prepared, without measuring it, on the Computational Basis;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        quantum_register_name = "qu_reg"
        """
        Set the name of the Qiskrypt's Quantum Register.
        """

        quantum_register_num_qubits = 2
        """
        Set the number of qubits for the Qiskrypt's Quantum Register.
        """

        qiskrypt_quantum_register = \
            QiskryptQuantumRegister(name=quantum_register_name,
                                    num_qubits=quantum_register_num_qubits,
                                    qiskit_quantum_register=None)
        """
        Create a Qiskrypt's Quantum Register, given its name and number of qubits.
        """

        quantum_circuit_name = "qu_circ"
        """
        Set the name of the Qiskrypt's Quantum Circuit.
        """

        qiskrypt_quantum_circuit_bell_state_psi_minus_4 = \
            QiskryptQuantumCircuit(name=quantum_circuit_name,
                                   qiskrypt_quantum_registers=[qiskrypt_quantum_register],
                                   qiskrypt_fully_quantum_registers=None,
                                   qiskrypt_semi_quantum_registers=None,
                                   qiskrypt_ancilla_quantum_registers=None,
                                   qiskrypt_ancilla_fully_quantum_registers=None,
                                   qiskrypt_ancilla_semi_quantum_registers=None,
                                   qiskrypt_classical_registers=None,
                                   global_phase=0)
        """
        Create a Qiskrypt's Quantum Circuit, given its name,
        Qiskrypt's Quantum Registers, Qiskrypt's Fully-Quantum Registers,
        Qiskrypt's Semi-Quantum Registers,
        Qiskrypt's Ancilla Quantum Registers, Qiskrypt's Ancilla Fully-Quantum Registers,
        Qiskrypt's Ancilla Semi-Quantum Registers,
        Qiskrypt's Classical Registers and
        Global Phase.
        """

        qiskrypt_bell_state_psi_minus_4 = \
            QiskryptBellState("bell_state_psi_minus_4", qiskrypt_quantum_circuit_bell_state_psi_minus_4,
                              POSSIBLE_CONFIGURATIONS_BELL_STATES[4])
        """
        Create a Qiskrypt's Bell State, for a generation of a Bell's State with the configuration,
        |ψ^-⟩ = 1/sqrt(2) x (|01⟩ - |10⟩).
        """

        qiskrypt_bell_state_psi_minus_4.configure(0, 0, 0, 1)
        """
        Configure the Qiskrypt's Bell State, regarding its control IBM Qiskit's Quantum Register
        and control qubit, as well, its target IBM Qiskit's Quantum Register and target qubit.
        """

        qiskrypt_bell_state_psi_minus_4\
            .prepare_bipartite_entanglement_at_computational_basis(is_to_measure_at_computational_basis=False,
                                                                   qiskit_classical_register_control_index=None,
                                                                   qiskit_classical_register_target_index=None,
                                                                   control_bit_index=None, target_bit_index=None)
        """
        Prepare the Bipartite Quantum Entanglement,
        for the specified Qiskrypt's Bell State, as a Quantum Entangled State,
        without measure it, on the Computational Basis.
        """

        qiskit_state_vector_backend = Aer.get_backend("statevector_simulator")
        """
        Getting the Aer Simulator Backend for the State Vector Representation
        (i.e., the quantum state represented as its state vector).
        """

        final_quantum_state_vector_state = \
            execute(qiskrypt_bell_state_psi_minus_4.qiskrypt_quantum_circuit.qiskit_quantum_circuit,
                    qiskit_state_vector_backend).result().get_statevector()
        """
        Execute the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit
        and store the resulted quantum state represented in a final state vector.
        """

        assert_allclose(final_quantum_state_vector_state,
                        array([(0. + 0.j),
                               ((1. / sqrt(2.)) + 0.j),
                               -((1. / sqrt(2.)) + 0.j),
                               (0. + 0.j)]),
                        rtol=1e-7, atol=1e-7)
        """
        Perform the Assertion of all close values in the values of the quantum state,
        represented by its state vector describing the given qubits,
        after be prepared a Bell's State with the configuration,
        |ψ^-⟩ = 1/sqrt(2) x (|01⟩ - |10⟩).
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_5_prepare_bell_state_basis_bell_state_phi_plus_epr_pair_00(self):
        """
        Test Case #5:

        - Initialise the Qiskrypt's Bell State, prepare it, as an Entangled Quantum State,
          in the Bell State Basis.

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Quantum Register is prepared on the quantum state, |00⟩;
        2) The Qiskrypt's Bell State is initialised and configured;
        3) The Qiskrypt's Bell State with the configuration,
           |ϕ^+⟩ = 1/sqrt(2) x (|00⟩ + |11⟩) (also known as, EPR Pair),
           is prepared, without measuring it, on the Computational Basis;
        4) The Qiskrypt's Bell State with the configuration,
           |ϕ^+⟩ = 1/sqrt(2) x (|00⟩ + |11⟩) (also known as, EPR Pair),
           is prepared, without measuring it, on the Bell State Basis,
           resulting on the initial quantum state, |00⟩;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        quantum_register_name = "qu_reg"
        """
        Set the name of the Qiskrypt's Quantum Register.
        """

        quantum_register_num_qubits = 2
        """
        Set the number of qubits for the Qiskrypt's Quantum Register.
        """

        qiskrypt_quantum_register = \
            QiskryptQuantumRegister(name=quantum_register_name,
                                    num_qubits=quantum_register_num_qubits,
                                    qiskit_quantum_register=None)
        """
        Create a Qiskrypt's Quantum Register, given its name and number of qubits.
        """

        quantum_circuit_name = "qu_circ"
        """
        Set the name of the Qiskrypt's Quantum Circuit.
        """

        qiskrypt_quantum_circuit_bell_state_phi_plus_epr_pair_5 = \
            QiskryptQuantumCircuit(name=quantum_circuit_name,
                                   qiskrypt_quantum_registers=[qiskrypt_quantum_register],
                                   qiskrypt_fully_quantum_registers=None,
                                   qiskrypt_semi_quantum_registers=None,
                                   qiskrypt_ancilla_quantum_registers=None,
                                   qiskrypt_ancilla_fully_quantum_registers=None,
                                   qiskrypt_ancilla_semi_quantum_registers=None,
                                   qiskrypt_classical_registers=None,
                                   global_phase=0)
        """
        Create a Qiskrypt's Quantum Circuit, given its name,
        Qiskrypt's Quantum Registers, Qiskrypt's Fully-Quantum Registers,
        Qiskrypt's Semi-Quantum Registers,
        Qiskrypt's Ancilla Quantum Registers, Qiskrypt's Ancilla Fully-Quantum Registers,
        Qiskrypt's Ancilla Semi-Quantum Registers,
        Qiskrypt's Classical Registers and
        Global Phase.
        """

        qiskrypt_bell_state_phi_plus_epr_pair_5 = \
            QiskryptBellState("bell_state_phi_plus_epr_pair_5",
                              qiskrypt_quantum_circuit_bell_state_phi_plus_epr_pair_5,
                              POSSIBLE_CONFIGURATIONS_BELL_STATES[0])
        """
        Create a Qiskrypt's Bell State, for a generation of a Bell's State with the configuration,
        |ϕ^+⟩ = 1/sqrt(2) x (|00⟩ + |11⟩) (also known as, EPR Pair).
        """

        qiskrypt_bell_state_phi_plus_epr_pair_5.configure(0, 0, 0, 1)
        """
        Configure the Qiskrypt's Bell State, regarding its control IBM Qiskit's Quantum Register
        and control qubit, as well, its target IBM Qiskit's Quantum Register and target qubit.
        """

        qiskrypt_bell_state_phi_plus_epr_pair_5\
            .prepare_bipartite_entanglement_at_computational_basis(is_to_measure_at_computational_basis=False,
                                                                   qiskit_classical_register_control_index=None,
                                                                   qiskit_classical_register_target_index=None,
                                                                   control_bit_index=None, target_bit_index=None)
        """
        Prepare the Bipartite Quantum Entanglement,
        for the specified Qiskrypt's Bell State, as a Quantum Entangled State,
        without measure it, on the Computational Basis.
        """

        qiskrypt_bell_state_phi_plus_epr_pair_5\
            .prepare_bipartite_entanglement_at_bell_state_basis(is_to_measure_at_bell_state_basis=False,
                                                                qiskit_classical_register_control_index=None,
                                                                qiskit_classical_register_target_index=None,
                                                                control_bit_index=None, target_bit_index=None)
        """
        Prepare the Bipartite Quantum Entanglement,
        for the specified Qiskrypt's Bell State, as a Quantum Entangled State,
        without measure it, on the Bell State Basis.
        """

        qiskit_state_vector_backend = Aer.get_backend("statevector_simulator")
        """
        Getting the Aer Simulator Backend for the State Vector Representation
        (i.e., the quantum state represented as its state vector).
        """

        final_quantum_state_vector_state = \
            execute(qiskrypt_bell_state_phi_plus_epr_pair_5.qiskrypt_quantum_circuit.qiskit_quantum_circuit,
                    qiskit_state_vector_backend).result().get_statevector()
        """
        Execute the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit
        and store the resulted quantum state represented in a final state vector.
        """

        assert_allclose(final_quantum_state_vector_state,
                        array([(1. + 0.j),
                               (0. + 0.j),
                               (0. + 0.j),
                               (0. + 0.j)]),
                        rtol=1e-7, atol=1e-7)
        """
        Perform the Assertion of all close values in the values of the quantum state,
        represented by its state vector describing the given qubits,
        after be initialised a quantum state as |00⟩,
        then prepared Bell's State with the configuration,
        |ϕ^+⟩ = 1/sqrt(2) x (|00⟩ + |11⟩) (also known as, EPR Pair),
        on the Computational Basis and then reverting it,
        by preparing it on the Bell State Basis.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_6_prepare_computational_basis_bell_state_phi_plus_epr_pair_01(self):
        """
        Test Case #6:

        - Initialise the Qiskrypt's Bell State, prepare it, as an Entangled Quantum State,
          in the Bell State Basis.

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Quantum Register is prepared on the quantum state, |01⟩;
        2) The Qiskrypt's Bell State is initialised and configured;
        3) The Qiskrypt's Bell State with the configuration,
           |ϕ^+⟩ = 1/sqrt(2) x (|00⟩ + |11⟩) (also known as, EPR Pair),
           is prepared, without measuring it, on the Computational Basis;
        4) The Qiskrypt's Bell State with the configuration,
           |ϕ^+⟩ = 1/sqrt(2) x (|00⟩ + |11⟩) (also known as, EPR Pair),
           is prepared, without measuring it, on the Bell State Basis,
           resulting on the initial quantum state, |01⟩;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        quantum_register_name = "qu_reg"
        """
        Set the name of the Qiskrypt's Quantum Register.
        """

        quantum_register_num_qubits = 2
        """
        Set the number of qubits for the Qiskrypt's Quantum Register.
        """

        qiskrypt_quantum_register = \
            QiskryptQuantumRegister(name=quantum_register_name,
                                    num_qubits=quantum_register_num_qubits,
                                    qiskit_quantum_register=None)
        """
        Create a Qiskrypt's Quantum Register, given its name and number of qubits.
        """

        quantum_circuit_name = "qu_circ"
        """
        Set the name of the Qiskrypt's Quantum Circuit.
        """

        qiskrypt_quantum_circuit_bell_state_phi_plus_epr_pair_6 = \
            QiskryptQuantumCircuit(name=quantum_circuit_name,
                                   qiskrypt_quantum_registers=[qiskrypt_quantum_register],
                                   qiskrypt_fully_quantum_registers=None,
                                   qiskrypt_semi_quantum_registers=None,
                                   qiskrypt_ancilla_quantum_registers=None,
                                   qiskrypt_ancilla_fully_quantum_registers=None,
                                   qiskrypt_ancilla_semi_quantum_registers=None,
                                   qiskrypt_classical_registers=None,
                                   global_phase=0)
        """
        Create a Qiskrypt's Quantum Circuit, given its name,
        Qiskrypt's Quantum Registers, Qiskrypt's Fully-Quantum Registers,
        Qiskrypt's Semi-Quantum Registers,
        Qiskrypt's Ancilla Quantum Registers, Qiskrypt's Ancilla Fully-Quantum Registers,
        Qiskrypt's Ancilla Semi-Quantum Registers,
        Qiskrypt's Classical Registers and
        Global Phase.
        """

        qiskrypt_quantum_circuit_bell_state_phi_plus_epr_pair_6 \
            .apply_pauli_x(0, 0)
        """
        Apply the Pauli-X (Bit Flip/NOT) Gate/Operation to the given index for
        the single qubit of the given IBM Qiskit's Quantum Register (|00⟩ ↦ |01⟩).
        """

        qiskrypt_bell_state_phi_plus_epr_pair_6 = \
            QiskryptBellState("bell_state_phi_plus_epr_pair_6",
                              qiskrypt_quantum_circuit_bell_state_phi_plus_epr_pair_6,
                              POSSIBLE_CONFIGURATIONS_BELL_STATES[0])
        """
        Create a Qiskrypt's Bell State, for a generation of a Bell's State with the configuration,
        |ϕ^+⟩ = 1/sqrt(2) x (|00⟩ + |11⟩) (also known as, EPR Pair).
        """

        qiskrypt_bell_state_phi_plus_epr_pair_6.configure(0, 0, 0, 1)
        """
        Configure the Qiskrypt's Bell State, regarding its control IBM Qiskit's Quantum Register
        and control qubit, as well, its target IBM Qiskit's Quantum Register and target qubit.
        """

        qiskrypt_bell_state_phi_plus_epr_pair_6\
            .prepare_bipartite_entanglement_at_computational_basis(is_to_measure_at_computational_basis=False,
                                                                   qiskit_classical_register_control_index=None,
                                                                   qiskit_classical_register_target_index=None,
                                                                   control_bit_index=None, target_bit_index=None)
        """
        Prepare the Bipartite Quantum Entanglement,
        for the specified Qiskrypt's Bell State, as a Quantum Entangled State,
        without measure it, on the Computational Basis.
        """

        qiskrypt_bell_state_phi_plus_epr_pair_6\
            .prepare_bipartite_entanglement_at_bell_state_basis(is_to_measure_at_bell_state_basis=False,
                                                                qiskit_classical_register_control_index=None,
                                                                qiskit_classical_register_target_index=None,
                                                                control_bit_index=None, target_bit_index=None)
        """
        Prepare the Bipartite Quantum Entanglement,
        for the specified Qiskrypt's Bell State, as a Quantum Entangled State,
        without measure it, on the Bell State Basis.
        """

        qiskit_state_vector_backend = Aer.get_backend("statevector_simulator")
        """
        Getting the Aer Simulator Backend for the State Vector Representation
        (i.e., the quantum state represented as its state vector).
        """

        final_quantum_state_vector_state = \
            execute(qiskrypt_bell_state_phi_plus_epr_pair_6.qiskrypt_quantum_circuit.qiskit_quantum_circuit,
                    qiskit_state_vector_backend).result().get_statevector()
        """
        Execute the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit
        and store the resulted quantum state represented in a final state vector.
        """

        assert_allclose(final_quantum_state_vector_state,
                        array([(0. + 0.j),
                               (1. + 0.j),
                               (0. + 0.j),
                               (0. + 0.j)]),
                        rtol=1e-7, atol=1e-7)
        """
        Perform the Assertion of all close values in the values of the quantum state,
        represented by its state vector describing the given qubits,
        after be initialised a quantum state as |01⟩,
        then prepared Bell's State with the configuration,
        |ϕ^+⟩ = 1/sqrt(2) x (|00⟩ + |11⟩) (also known as, EPR Pair),
        on the Computational Basis and then reverting it,
        by preparing it on the Bell State Basis.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_7_prepare_bell_state_basis_bell_state_phi_plus_epr_pair_10(self):
        """
        Test Case #7:

        - Initialise the Qiskrypt's Bell State, prepare it, as an Entangled Quantum State,
          in the Bell State Basis.

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Quantum Register is prepared on the quantum state, |10⟩;
        2) The Qiskrypt's Bell State is initialised and configured;
        3) The Qiskrypt's Bell State with the configuration,
           |ϕ^+⟩ = 1/sqrt(2) x (|00⟩ + |11⟩) (also known as, EPR Pair),
           is prepared, without measuring it, on the Computational Basis;
        4) The Qiskrypt's Bell State with the configuration,
           |ϕ^+⟩ = 1/sqrt(2) x (|00⟩ + |11⟩) (also known as, EPR Pair),
           is prepared, without measuring it, on the Bell State Basis,
           resulting on the initial quantum state, |10⟩;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        quantum_register_name = "qu_reg"
        """
        Set the name of the Qiskrypt's Quantum Register.
        """

        quantum_register_num_qubits = 2
        """
        Set the number of qubits for the Qiskrypt's Quantum Register.
        """

        qiskrypt_quantum_register = \
            QiskryptQuantumRegister(name=quantum_register_name,
                                    num_qubits=quantum_register_num_qubits,
                                    qiskit_quantum_register=None)
        """
        Create a Qiskrypt's Quantum Register, given its name and number of qubits.
        """

        quantum_circuit_name = "qu_circ"
        """
        Set the name of the Qiskrypt's Quantum Circuit.
        """

        qiskrypt_quantum_circuit_bell_state_phi_plus_epr_pair_7 = \
            QiskryptQuantumCircuit(name=quantum_circuit_name,
                                   qiskrypt_quantum_registers=[qiskrypt_quantum_register],
                                   qiskrypt_fully_quantum_registers=None,
                                   qiskrypt_semi_quantum_registers=None,
                                   qiskrypt_ancilla_quantum_registers=None,
                                   qiskrypt_ancilla_fully_quantum_registers=None,
                                   qiskrypt_ancilla_semi_quantum_registers=None,
                                   qiskrypt_classical_registers=None,
                                   global_phase=0)
        """
        Create a Qiskrypt's Quantum Circuit, given its name,
        Qiskrypt's Quantum Registers, Qiskrypt's Fully-Quantum Registers,
        Qiskrypt's Semi-Quantum Registers,
        Qiskrypt's Ancilla Quantum Registers, Qiskrypt's Ancilla Fully-Quantum Registers,
        Qiskrypt's Ancilla Semi-Quantum Registers,
        Qiskrypt's Classical Registers and
        Global Phase.
        """

        qiskrypt_quantum_circuit_bell_state_phi_plus_epr_pair_7 \
            .apply_pauli_x(0, 1)
        """
        Apply the Pauli-X (Bit Flip/NOT) Gate/Operation to the given index for
        the single qubit of the given IBM Qiskit's Quantum Register (|00⟩ ↦ |10⟩).
        """

        qiskrypt_bell_state_phi_plus_epr_pair_7 = \
            QiskryptBellState("bell_state_phi_plus_epr_pair_7",
                              qiskrypt_quantum_circuit_bell_state_phi_plus_epr_pair_7,
                              POSSIBLE_CONFIGURATIONS_BELL_STATES[0])
        """
        Create a Qiskrypt's Bell State, for a generation of a Bell's State with the configuration,
        |ϕ^+⟩ = 1/sqrt(2) x (|00⟩ + |11⟩) (also known as, EPR Pair).
        """

        qiskrypt_bell_state_phi_plus_epr_pair_7.configure(0, 0, 0, 1)
        """
        Configure the Qiskrypt's Bell State, regarding its control IBM Qiskit's Quantum Register
        and control qubit, as well, its target IBM Qiskit's Quantum Register and target qubit.
        """

        qiskrypt_bell_state_phi_plus_epr_pair_7\
            .prepare_bipartite_entanglement_at_computational_basis(is_to_measure_at_computational_basis=False,
                                                                   qiskit_classical_register_control_index=None,
                                                                   qiskit_classical_register_target_index=None,
                                                                   control_bit_index=None, target_bit_index=None)
        """
        Prepare the Bipartite Quantum Entanglement,
        for the specified Qiskrypt's Bell State, as a Quantum Entangled State,
        without measure it, on the Computational Basis.
        """

        qiskrypt_bell_state_phi_plus_epr_pair_7\
            .prepare_bipartite_entanglement_at_bell_state_basis(is_to_measure_at_bell_state_basis=False,
                                                                qiskit_classical_register_control_index=None,
                                                                qiskit_classical_register_target_index=None,
                                                                control_bit_index=None, target_bit_index=None)
        """
        Prepare the Bipartite Quantum Entanglement,
        for the specified Qiskrypt's Bell State, as a Quantum Entangled State,
        without measure it, on the Bell State Basis.
        """

        qiskit_state_vector_backend = Aer.get_backend("statevector_simulator")
        """
        Getting the Aer Simulator Backend for the State Vector Representation
        (i.e., the quantum state represented as its state vector).
        """

        final_quantum_state_vector_state = \
            execute(qiskrypt_bell_state_phi_plus_epr_pair_7.qiskrypt_quantum_circuit.qiskit_quantum_circuit,
                    qiskit_state_vector_backend).result().get_statevector()
        """
        Execute the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit
        and store the resulted quantum state represented in a final state vector.
        """

        assert_allclose(final_quantum_state_vector_state,
                        array([(0. + 0.j),
                               (0. + 0.j),
                               (1. + 0.j),
                               (0. + 0.j)]),
                        rtol=1e-7, atol=1e-7)
        """
        Perform the Assertion of all close values in the values of the quantum state,
        represented by its state vector describing the given qubits,
        after be initialised a quantum state as |10⟩,
        then prepared Bell's State with the configuration,
        |ϕ^+⟩ = 1/sqrt(2) x (|00⟩ + |11⟩) (also known as, EPR Pair),
        on the Computational Basis and then reverting it,
        by preparing it on the Bell State Basis.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_8_prepare_bell_state_basis_bell_state_phi_plus_epr_pair_11(self):
        """
        Test Case #8:

        - Initialise the Qiskrypt's Bell State, prepare it, as an Entangled Quantum State,
          and then, measure in the Bell State Basis.

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Quantum Register is prepared on the quantum state, |11⟩;
        2) The Qiskrypt's Bell State is initialised and configured;
        3) The Qiskrypt's Bell State with the configuration,
           |ϕ^+⟩ = 1/sqrt(2) x (|00⟩ + |11⟩) (also known as, EPR Pair),
           is prepared, without measuring it, on the Computational Basis;
        4) The Qiskrypt's Bell State with the configuration,
           |ϕ^+⟩ = 1/sqrt(2) x (|00⟩ + |11⟩) (also known as, EPR Pair),
           is prepared, without measuring it, on the Bell State Basis,
           resulting on the initial quantum state, |11⟩;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        quantum_register_name = "qu_reg"
        """
        Set the name of the Qiskrypt's Quantum Register.
        """

        quantum_register_num_qubits = 2
        """
        Set the number of qubits for the Qiskrypt's Quantum Register.
        """

        qiskrypt_quantum_register = \
            QiskryptQuantumRegister(name=quantum_register_name,
                                    num_qubits=quantum_register_num_qubits,
                                    qiskit_quantum_register=None)
        """
        Create a Qiskrypt's Quantum Register, given its name and number of qubits.
        """

        quantum_circuit_name = "qu_circ"
        """
        Set the name of the Qiskrypt's Quantum Circuit.
        """

        qiskrypt_quantum_circuit_bell_state_phi_plus_epr_pair_8 = \
            QiskryptQuantumCircuit(name=quantum_circuit_name,
                                   qiskrypt_quantum_registers=[qiskrypt_quantum_register],
                                   qiskrypt_fully_quantum_registers=None,
                                   qiskrypt_semi_quantum_registers=None,
                                   qiskrypt_ancilla_quantum_registers=None,
                                   qiskrypt_ancilla_fully_quantum_registers=None,
                                   qiskrypt_ancilla_semi_quantum_registers=None,
                                   qiskrypt_classical_registers=None,
                                   global_phase=0)
        """
        Create a Qiskrypt's Quantum Circuit, given its name,
        Qiskrypt's Quantum Registers, Qiskrypt's Fully-Quantum Registers,
        Qiskrypt's Semi-Quantum Registers,
        Qiskrypt's Ancilla Quantum Registers, Qiskrypt's Ancilla Fully-Quantum Registers,
        Qiskrypt's Ancilla Semi-Quantum Registers,
        Qiskrypt's Classical Registers and
        Global Phase.
        """

        qiskrypt_quantum_circuit_bell_state_phi_plus_epr_pair_8 \
            .apply_pauli_x(0, 0)
        """
        Apply the Pauli-X (Bit Flip/NOT) Gate/Operation to the given index for
        the single qubit of the given IBM Qiskit's Quantum Register (|00⟩ ↦ |01⟩).
        """

        qiskrypt_quantum_circuit_bell_state_phi_plus_epr_pair_8 \
            .apply_pauli_x(0, 1)
        """
        Apply the Pauli-X (Bit Flip/NOT) Gate/Operation to the given index for
        the single qubit of the given IBM Qiskit's Quantum Register (|01⟩ ↦ |11⟩).
        """

        qiskrypt_bell_state_phi_plus_epr_pair_8 = \
            QiskryptBellState("bell_state_phi_plus_epr_pair_8",
                              qiskrypt_quantum_circuit_bell_state_phi_plus_epr_pair_8,
                              POSSIBLE_CONFIGURATIONS_BELL_STATES[0])
        """
        Create a Qiskrypt's Bell State, for a generation of a Bell's State with the configuration,
        |ϕ^+⟩ = 1/sqrt(2) x (|00⟩ + |11⟩) (also known as, EPR Pair).
        """

        qiskrypt_bell_state_phi_plus_epr_pair_8.configure(0, 0, 0, 1)
        """
        Configure the Qiskrypt's Bell State, regarding its control IBM Qiskit's Quantum Register
        and control qubit, as well, its target IBM Qiskit's Quantum Register and target qubit.
        """

        qiskrypt_bell_state_phi_plus_epr_pair_8\
            .prepare_bipartite_entanglement_at_computational_basis(is_to_measure_at_computational_basis=False,
                                                                   qiskit_classical_register_control_index=None,
                                                                   qiskit_classical_register_target_index=None,
                                                                   control_bit_index=None, target_bit_index=None)
        """
        Prepare the Bipartite Quantum Entanglement,
        for the specified Qiskrypt's Bell State, as a Quantum Entangled State,
        without measure it, on the Computational Basis.
        """

        qiskrypt_bell_state_phi_plus_epr_pair_8\
            .prepare_bipartite_entanglement_at_bell_state_basis(is_to_measure_at_bell_state_basis=False,
                                                                qiskit_classical_register_control_index=None,
                                                                qiskit_classical_register_target_index=None,
                                                                control_bit_index=None, target_bit_index=None)
        """
        Prepare the Bipartite Quantum Entanglement,
        for the specified Qiskrypt's Bell State, as a Quantum Entangled State,
        without measure it, on the Bell State Basis.
        """

        qiskit_state_vector_backend = Aer.get_backend("statevector_simulator")
        """
        Getting the Aer Simulator Backend for the State Vector Representation
        (i.e., the quantum state represented as its state vector).
        """

        final_quantum_state_vector_state = \
            execute(qiskrypt_bell_state_phi_plus_epr_pair_8.qiskrypt_quantum_circuit.qiskit_quantum_circuit,
                    qiskit_state_vector_backend).result().get_statevector()
        """
        Execute the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit
        and store the resulted quantum state represented in a final state vector.
        """

        assert_allclose(final_quantum_state_vector_state,
                        array([(0. + 0.j),
                               (0. + 0.j),
                               (0. + 0.j),
                               (1. + 0.j)]),
                        rtol=1e-7, atol=1e-7)
        """
        Perform the Assertion of all close values in the values of the quantum state,
        represented by its state vector describing the given qubits,
        after be initialised a quantum state as |11⟩,
        then prepared Bell's State with the configuration,
        |ϕ^+⟩ = 1/sqrt(2) x (|00⟩ + |11⟩) (also known as, EPR Pair),
        on the Computational Basis and then reverting it,
        by preparing it on the Bell State Basis.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_9_prepare_bell_state_basis_bell_state_phi_minus_00(self):
        """
        Test Case #9:

        - Initialise the Qiskrypt's Bell State, prepare it, as an Entangled Quantum State,
          and then, measure in the Bell State Basis.

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Quantum Register is prepared on the quantum state, |00⟩;
        2) The Qiskrypt's Bell State is initialised and configured;
        3) The Qiskrypt's Bell State with the configuration,
           |ϕ^-⟩ = 1/sqrt(2) x (|00⟩ - |11⟩),
           is prepared, without measuring it, on the Computational Basis;
        4) The Qiskrypt's Bell State with the configuration,
           |ϕ^-⟩ = 1/sqrt(2) x (|00⟩ - |11⟩),
           is prepared, without measuring it, on the Bell State Basis,
           resulting on the initial quantum state, |00⟩;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        quantum_register_name = "qu_reg"
        """
        Set the name of the Qiskrypt's Quantum Register.
        """

        quantum_register_num_qubits = 2
        """
        Set the number of qubits for the Qiskrypt's Quantum Register.
        """

        qiskrypt_quantum_register = \
            QiskryptQuantumRegister(name=quantum_register_name,
                                    num_qubits=quantum_register_num_qubits,
                                    qiskit_quantum_register=None)
        """
        Create a Qiskrypt's Quantum Register, given its name and number of qubits.
        """

        quantum_circuit_name = "qu_circ"
        """
        Set the name of the Qiskrypt's Quantum Circuit.
        """

        qiskrypt_quantum_circuit_bell_state_phi_minus_9 = \
            QiskryptQuantumCircuit(name=quantum_circuit_name,
                                   qiskrypt_quantum_registers=[qiskrypt_quantum_register],
                                   qiskrypt_fully_quantum_registers=None,
                                   qiskrypt_semi_quantum_registers=None,
                                   qiskrypt_ancilla_quantum_registers=None,
                                   qiskrypt_ancilla_fully_quantum_registers=None,
                                   qiskrypt_ancilla_semi_quantum_registers=None,
                                   qiskrypt_classical_registers=None,
                                   global_phase=0)
        """
        Create a Qiskrypt's Quantum Circuit, given its name,
        Qiskrypt's Quantum Registers, Qiskrypt's Fully-Quantum Registers,
        Qiskrypt's Semi-Quantum Registers,
        Qiskrypt's Ancilla Quantum Registers, Qiskrypt's Ancilla Fully-Quantum Registers,
        Qiskrypt's Ancilla Semi-Quantum Registers,
        Qiskrypt's Classical Registers and
        Global Phase.
        """

        qiskrypt_bell_state_phi_minus_9 = \
            QiskryptBellState("bell_state_phi_minus_9",
                              qiskrypt_quantum_circuit_bell_state_phi_minus_9,
                              POSSIBLE_CONFIGURATIONS_BELL_STATES[2])
        """
        Create a Qiskrypt's Bell State, for a generation of a Bell's State with the configuration,
        |ϕ^+⟩ = 1/sqrt(2) x (|00⟩ - |11⟩).
        """

        qiskrypt_bell_state_phi_minus_9.configure(0, 0, 0, 1)
        """
        Configure the Qiskrypt's Bell State, regarding its control IBM Qiskit's Quantum Register
        and control qubit, as well, its target IBM Qiskit's Quantum Register and target qubit.
        """

        qiskrypt_bell_state_phi_minus_9\
            .prepare_bipartite_entanglement_at_computational_basis(is_to_measure_at_computational_basis=False,
                                                                   qiskit_classical_register_control_index=None,
                                                                   qiskit_classical_register_target_index=None,
                                                                   control_bit_index=None, target_bit_index=None)
        """
        Prepare the Bipartite Quantum Entanglement,
        for the specified Qiskrypt's Bell State, as a Quantum Entangled State,
        without measure it, on the Computational Basis.
        """

        qiskrypt_bell_state_phi_minus_9\
            .prepare_bipartite_entanglement_at_bell_state_basis(is_to_measure_at_bell_state_basis=False,
                                                                qiskit_classical_register_control_index=None,
                                                                qiskit_classical_register_target_index=None,
                                                                control_bit_index=None, target_bit_index=None)
        """
        Prepare the Bipartite Quantum Entanglement,
        for the specified Qiskrypt's Bell State, as a Quantum Entangled State,
        without measure it, on the Bell State Basis.
        """

        qiskit_state_vector_backend = Aer.get_backend("statevector_simulator")
        """
        Getting the Aer Simulator Backend for the State Vector Representation
        (i.e., the quantum state represented as its state vector).
        """

        final_quantum_state_vector_state = \
            execute(qiskrypt_bell_state_phi_minus_9.qiskrypt_quantum_circuit.qiskit_quantum_circuit,
                    qiskit_state_vector_backend).result().get_statevector()
        """
        Execute the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit
        and store the resulted quantum state represented in a final state vector.
        """

        assert_allclose(final_quantum_state_vector_state,
                        array([(1. + 0.j),
                               (0. + 0.j),
                               (0. + 0.j),
                               (0. + 0.j)]),
                        rtol=1e-7, atol=1e-7)
        """
        Perform the Assertion of all close values in the values of the quantum state,
        represented by its state vector describing the given qubits,
        after be initialised a quantum state as |00⟩,
        then prepared Bell's State with the configuration,
        |ϕ^+⟩ = 1/sqrt(2) x (|00⟩ - |11⟩),
        on the Computational Basis and then reverting it,
        by preparing it on the Bell State Basis.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_10_prepare_bell_state_basis_bell_state_phi_minus_01(self):
        """
        Test Case #10:

        - Initialise the Qiskrypt's Bell State, prepare it, as an Entangled Quantum State,
          and then, measure in the Bell State Basis.

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Quantum Register is prepared on the quantum state, |01⟩;
        2) The Qiskrypt's Bell State is initialised and configured;
        3) The Qiskrypt's Bell State with the configuration,
           |ϕ^-⟩ = 1/sqrt(2) x (|00⟩ - |11⟩),
           is prepared, without measuring it, on the Computational Basis;
        4) The Qiskrypt's Bell State with the configuration,
           |ϕ^-⟩ = 1/sqrt(2) x (|00⟩ - |11⟩),
           is prepared, without measuring it, on the Bell State Basis,
           resulting on the initial quantum state, |01⟩;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        quantum_register_name = "qu_reg"
        """
        Set the name of the Qiskrypt's Quantum Register.
        """

        quantum_register_num_qubits = 2
        """
        Set the number of qubits for the Qiskrypt's Quantum Register.
        """

        qiskrypt_quantum_register = \
            QiskryptQuantumRegister(name=quantum_register_name,
                                    num_qubits=quantum_register_num_qubits,
                                    qiskit_quantum_register=None)
        """
        Create a Qiskrypt's Quantum Register, given its name and number of qubits.
        """

        quantum_circuit_name = "qu_circ"
        """
        Set the name of the Qiskrypt's Quantum Circuit.
        """

        qiskrypt_quantum_circuit_bell_state_phi_minus_10 = \
            QiskryptQuantumCircuit(name=quantum_circuit_name,
                                   qiskrypt_quantum_registers=[qiskrypt_quantum_register],
                                   qiskrypt_fully_quantum_registers=None,
                                   qiskrypt_semi_quantum_registers=None,
                                   qiskrypt_ancilla_quantum_registers=None,
                                   qiskrypt_ancilla_fully_quantum_registers=None,
                                   qiskrypt_ancilla_semi_quantum_registers=None,
                                   qiskrypt_classical_registers=None,
                                   global_phase=0)
        """
        Create a Qiskrypt's Quantum Circuit, given its name,
        Qiskrypt's Quantum Registers, Qiskrypt's Fully-Quantum Registers,
        Qiskrypt's Semi-Quantum Registers,
        Qiskrypt's Ancilla Quantum Registers, Qiskrypt's Ancilla Fully-Quantum Registers,
        Qiskrypt's Ancilla Semi-Quantum Registers,
        Qiskrypt's Classical Registers and
        Global Phase.
        """

        qiskrypt_quantum_circuit_bell_state_phi_minus_10 \
            .apply_pauli_x(0, 0)
        """
        Apply the Pauli-X (Bit Flip/NOT) Gate/Operation to the given index for
        the single qubit of the given IBM Qiskit's Quantum Register (|00⟩ ↦ |01⟩).
        """

        qiskrypt_bell_state_phi_minus_10 = \
            QiskryptBellState("bell_state_phi_minus_10",
                              qiskrypt_quantum_circuit_bell_state_phi_minus_10,
                              POSSIBLE_CONFIGURATIONS_BELL_STATES[2])
        """
        Create a Qiskrypt's Bell State, for a generation of a Bell's State with the configuration,
        |ϕ^+⟩ = 1/sqrt(2) x (|00⟩ - |11⟩).
        """

        qiskrypt_bell_state_phi_minus_10.configure(0, 0, 0, 1)
        """
        Configure the Qiskrypt's Bell State, regarding its control IBM Qiskit's Quantum Register
        and control qubit, as well, its target IBM Qiskit's Quantum Register and target qubit.
        """

        qiskrypt_bell_state_phi_minus_10\
            .prepare_bipartite_entanglement_at_computational_basis(is_to_measure_at_computational_basis=False,
                                                                   qiskit_classical_register_control_index=None,
                                                                   qiskit_classical_register_target_index=None,
                                                                   control_bit_index=None, target_bit_index=None)
        """
        Prepare the Bipartite Quantum Entanglement,
        for the specified Qiskrypt's Bell State, as a Quantum Entangled State,
        without measure it, on the Computational Basis.
        """

        qiskrypt_bell_state_phi_minus_10\
            .prepare_bipartite_entanglement_at_bell_state_basis(is_to_measure_at_bell_state_basis=False,
                                                                qiskit_classical_register_control_index=None,
                                                                qiskit_classical_register_target_index=None,
                                                                control_bit_index=None, target_bit_index=None)
        """
        Prepare the Bipartite Quantum Entanglement,
        for the specified Qiskrypt's Bell State, as a Quantum Entangled State,
        without measure it, on the Bell State Basis.
        """

        qiskit_state_vector_backend = Aer.get_backend("statevector_simulator")
        """
        Getting the Aer Simulator Backend for the State Vector Representation
        (i.e., the quantum state represented as its state vector).
        """

        final_quantum_state_vector_state = \
            execute(qiskrypt_bell_state_phi_minus_10.qiskrypt_quantum_circuit.qiskit_quantum_circuit,
                    qiskit_state_vector_backend).result().get_statevector()
        """
        Execute the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit
        and store the resulted quantum state represented in a final state vector.
        """

        assert_allclose(final_quantum_state_vector_state,
                        array([(0. + 0.j),
                               (1. + 0.j),
                               (0. + 0.j),
                               (0. + 0.j)]),
                        rtol=1e-7, atol=1e-7)
        """
        Perform the Assertion of all close values in the values of the quantum state,
        represented by its state vector describing the given qubits,
        after be initialised a quantum state as |01⟩,
        then prepared Bell's State with the configuration,
        |ϕ^+⟩ = 1/sqrt(2) x (|00⟩ - |11⟩),
        on the Computational Basis and then reverting it,
        by preparing it on the Bell State Basis.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_11_prepare_bell_state_basis_bell_state_phi_minus_10(self):
        """
        Test Case #11:

        - Initialise the Qiskrypt's Bell State, prepare it, as an Entangled Quantum State,
          and then, measure in the Bell State Basis.

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Quantum Register is prepared on the quantum state, |10⟩;
        2) The Qiskrypt's Bell State is initialised and configured;
        3) The Qiskrypt's Bell State with the configuration,
           |ϕ^-⟩ = 1/sqrt(2) x (|00⟩ - |11⟩),
           is prepared, without measuring it, on the Computational Basis;
        4) The Qiskrypt's Bell State with the configuration,
           |ϕ^-⟩ = 1/sqrt(2) x (|00⟩ - |11⟩),
           is prepared, without measuring it, on the Bell State Basis,
           resulting on the initial quantum state, |10⟩;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        quantum_register_name = "qu_reg"
        """
        Set the name of the Qiskrypt's Quantum Register.
        """

        quantum_register_num_qubits = 2
        """
        Set the number of qubits for the Qiskrypt's Quantum Register.
        """

        qiskrypt_quantum_register = \
            QiskryptQuantumRegister(name=quantum_register_name,
                                    num_qubits=quantum_register_num_qubits,
                                    qiskit_quantum_register=None)
        """
        Create a Qiskrypt's Quantum Register, given its name and number of qubits.
        """

        quantum_circuit_name = "qu_circ"
        """
        Set the name of the Qiskrypt's Quantum Circuit.
        """

        qiskrypt_quantum_circuit_bell_state_phi_minus_11 = \
            QiskryptQuantumCircuit(name=quantum_circuit_name,
                                   qiskrypt_quantum_registers=[qiskrypt_quantum_register],
                                   qiskrypt_fully_quantum_registers=None,
                                   qiskrypt_semi_quantum_registers=None,
                                   qiskrypt_ancilla_quantum_registers=None,
                                   qiskrypt_ancilla_fully_quantum_registers=None,
                                   qiskrypt_ancilla_semi_quantum_registers=None,
                                   qiskrypt_classical_registers=None,
                                   global_phase=0)
        """
        Create a Qiskrypt's Quantum Circuit, given its name,
        Qiskrypt's Quantum Registers, Qiskrypt's Fully-Quantum Registers,
        Qiskrypt's Semi-Quantum Registers,
        Qiskrypt's Ancilla Quantum Registers, Qiskrypt's Ancilla Fully-Quantum Registers,
        Qiskrypt's Ancilla Semi-Quantum Registers,
        Qiskrypt's Classical Registers and
        Global Phase.
        """

        qiskrypt_quantum_circuit_bell_state_phi_minus_11 \
            .apply_pauli_x(0, 1)
        """
        Apply the Pauli-X (Bit Flip/NOT) Gate/Operation to the given index for
        the single qubit of the given IBM Qiskit's Quantum Register (|00⟩ ↦ |10⟩).
        """

        qiskrypt_bell_state_phi_minus_11 = \
            QiskryptBellState("bell_state_phi_minus_11",
                              qiskrypt_quantum_circuit_bell_state_phi_minus_11,
                              POSSIBLE_CONFIGURATIONS_BELL_STATES[2])
        """
        Create a Qiskrypt's Bell State, for a generation of a Bell's State with the configuration,
        |ϕ^+⟩ = 1/sqrt(2) x (|00⟩ - |11⟩).
        """

        qiskrypt_bell_state_phi_minus_11.configure(0, 0, 0, 1)
        """
        Configure the Qiskrypt's Bell State, regarding its control IBM Qiskit's Quantum Register
        and control qubit, as well, its target IBM Qiskit's Quantum Register and target qubit.
        """

        qiskrypt_bell_state_phi_minus_11\
            .prepare_bipartite_entanglement_at_computational_basis(is_to_measure_at_computational_basis=False,
                                                                   qiskit_classical_register_control_index=None,
                                                                   qiskit_classical_register_target_index=None,
                                                                   control_bit_index=None, target_bit_index=None)
        """
        Prepare the Bipartite Quantum Entanglement,
        for the specified Qiskrypt's Bell State, as a Quantum Entangled State,
        without measure it, on the Computational Basis.
        """

        qiskrypt_bell_state_phi_minus_11\
            .prepare_bipartite_entanglement_at_bell_state_basis(is_to_measure_at_bell_state_basis=False,
                                                                qiskit_classical_register_control_index=None,
                                                                qiskit_classical_register_target_index=None,
                                                                control_bit_index=None, target_bit_index=None)
        """
        Prepare the Bipartite Quantum Entanglement,
        for the specified Qiskrypt's Bell State, as a Quantum Entangled State,
        without measure it, on the Bell State Basis.
        """

        qiskit_state_vector_backend = Aer.get_backend("statevector_simulator")
        """
        Getting the Aer Simulator Backend for the State Vector Representation
        (i.e., the quantum state represented as its state vector).
        """

        final_quantum_state_vector_state = \
            execute(qiskrypt_bell_state_phi_minus_11.qiskrypt_quantum_circuit.qiskit_quantum_circuit,
                    qiskit_state_vector_backend).result().get_statevector()
        """
        Execute the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit
        and store the resulted quantum state represented in a final state vector.
        """

        assert_allclose(final_quantum_state_vector_state,
                        array([(0. + 0.j),
                               (0. + 0.j),
                               (1. + 0.j),
                               (0. + 0.j)]),
                        rtol=1e-7, atol=1e-7)
        """
        Perform the Assertion of all close values in the values of the quantum state,
        represented by its state vector describing the given qubits,
        after be initialised a quantum state as |10⟩,
        then prepared Bell's State with the configuration,
        |ϕ^+⟩ = 1/sqrt(2) x (|00⟩ - |11⟩),
        on the Computational Basis and then reverting it,
        by preparing it on the Bell State Basis.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_12_prepare_bell_state_basis_bell_state_phi_minus_11(self):
        """
        Test Case #12:

        - Initialise the Qiskrypt's Bell State, prepare it, as an Entangled Quantum State,
          and then, measure in the Bell State Basis.

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Quantum Register is prepared on the quantum state, |11⟩;
        2) The Qiskrypt's Bell State is initialised and configured;
        3) The Qiskrypt's Bell State with the configuration,
           |ϕ^-⟩ = 1/sqrt(2) x (|00⟩ - |11⟩),
           is prepared, without measuring it, on the Computational Basis;
        4) The Qiskrypt's Bell State with the configuration,
           |ϕ^-⟩ = 1/sqrt(2) x (|00⟩ - |11⟩),
           is prepared, without measuring it, on the Bell State Basis,
           resulting on the initial quantum state, |11⟩;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        quantum_register_name = "qu_reg"
        """
        Set the name of the Qiskrypt's Quantum Register.
        """

        quantum_register_num_qubits = 2
        """
        Set the number of qubits for the Qiskrypt's Quantum Register.
        """

        qiskrypt_quantum_register = \
            QiskryptQuantumRegister(name=quantum_register_name,
                                    num_qubits=quantum_register_num_qubits,
                                    qiskit_quantum_register=None)
        """
        Create a Qiskrypt's Quantum Register, given its name and number of qubits.
        """

        quantum_circuit_name = "qu_circ"
        """
        Set the name of the Qiskrypt's Quantum Circuit.
        """

        qiskrypt_quantum_circuit_bell_state_phi_minus_12 = \
            QiskryptQuantumCircuit(name=quantum_circuit_name,
                                   qiskrypt_quantum_registers=[qiskrypt_quantum_register],
                                   qiskrypt_fully_quantum_registers=None,
                                   qiskrypt_semi_quantum_registers=None,
                                   qiskrypt_ancilla_quantum_registers=None,
                                   qiskrypt_ancilla_fully_quantum_registers=None,
                                   qiskrypt_ancilla_semi_quantum_registers=None,
                                   qiskrypt_classical_registers=None,
                                   global_phase=0)
        """
        Create a Qiskrypt's Quantum Circuit, given its name,
        Qiskrypt's Quantum Registers, Qiskrypt's Fully-Quantum Registers,
        Qiskrypt's Semi-Quantum Registers,
        Qiskrypt's Ancilla Quantum Registers, Qiskrypt's Ancilla Fully-Quantum Registers,
        Qiskrypt's Ancilla Semi-Quantum Registers,
        Qiskrypt's Classical Registers and
        Global Phase.
        """

        qiskrypt_quantum_circuit_bell_state_phi_minus_12 \
            .apply_pauli_x(0, 0)
        """
        Apply the Pauli-X (Bit Flip/NOT) Gate/Operation to the given index for
        the single qubit of the given IBM Qiskit's Quantum Register (|00⟩ ↦ |01⟩).
        """

        qiskrypt_quantum_circuit_bell_state_phi_minus_12 \
            .apply_pauli_x(0, 1)
        """
        Apply the Pauli-X (Bit Flip/NOT) Gate/Operation to the given index for
        the single qubit of the given IBM Qiskit's Quantum Register (|01⟩ ↦ |11⟩).
        """

        qiskrypt_bell_state_phi_minus_12 = \
            QiskryptBellState("bell_state_phi_minus_12",
                              qiskrypt_quantum_circuit_bell_state_phi_minus_12,
                              POSSIBLE_CONFIGURATIONS_BELL_STATES[2])
        """
        Create a Qiskrypt's Bell State, for a generation of a Bell's State with the configuration,
        |ϕ^+⟩ = 1/sqrt(2) x (|00⟩ - |11⟩).
        """

        qiskrypt_bell_state_phi_minus_12.configure(0, 0, 0, 1)
        """
        Configure the Qiskrypt's Bell State, regarding its control IBM Qiskit's Quantum Register
        and control qubit, as well, its target IBM Qiskit's Quantum Register and target qubit.
        """

        qiskrypt_bell_state_phi_minus_12\
            .prepare_bipartite_entanglement_at_computational_basis(is_to_measure_at_computational_basis=False,
                                                                   qiskit_classical_register_control_index=None,
                                                                   qiskit_classical_register_target_index=None,
                                                                   control_bit_index=None, target_bit_index=None)
        """
        Prepare the Bipartite Quantum Entanglement,
        for the specified Qiskrypt's Bell State, as a Quantum Entangled State,
        without measure it, on the Computational Basis.
        """

        qiskrypt_bell_state_phi_minus_12\
            .prepare_bipartite_entanglement_at_bell_state_basis(is_to_measure_at_bell_state_basis=False,
                                                                qiskit_classical_register_control_index=None,
                                                                qiskit_classical_register_target_index=None,
                                                                control_bit_index=None, target_bit_index=None)
        """
        Prepare the Bipartite Quantum Entanglement,
        for the specified Qiskrypt's Bell State, as a Quantum Entangled State,
        without measure it, on the Bell State Basis.
        """

        qiskit_state_vector_backend = Aer.get_backend("statevector_simulator")
        """
        Getting the Aer Simulator Backend for the State Vector Representation
        (i.e., the quantum state represented as its state vector).
        """

        final_quantum_state_vector_state = \
            execute(qiskrypt_bell_state_phi_minus_12.qiskrypt_quantum_circuit.qiskit_quantum_circuit,
                    qiskit_state_vector_backend).result().get_statevector()
        """
        Execute the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit
        and store the resulted quantum state represented in a final state vector.
        """

        assert_allclose(final_quantum_state_vector_state,
                        array([(0. + 0.j),
                               (0. + 0.j),
                               (0. + 0.j),
                               (1. + 0.j)]),
                        rtol=1e-7, atol=1e-7)
        """
        Perform the Assertion of all close values in the values of the quantum state,
        represented by its state vector describing the given qubits,
        after be initialised a quantum state as |11⟩,
        then prepared Bell's State with the configuration,
        |ϕ^+⟩ = 1/sqrt(2) x (|00⟩ - |11⟩),
        on the Computational Basis and then reverting it,
        by preparing it on the Bell State Basis.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_13_prepare_bell_state_basis_bell_state_psi_plus_00(self):
        """
        Test Case #13:

        - Initialise the Qiskrypt's Bell State, prepare it, as an Entangled Quantum State,
          and then, measure in the Bell State Basis.

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Quantum Register is prepared on the quantum state, |00⟩;
        2) The Qiskrypt's Bell State is initialised and configured;
        3) The Qiskrypt's Bell State with the configuration,
           |ψ^+⟩ = 1/sqrt(2) x (|01⟩ + |10⟩),
           is prepared, without measuring it, on the Computational Basis;
        4) The Qiskrypt's Bell State with the configuration,
           |ψ^+⟩ = 1/sqrt(2) x (|01⟩ + |10⟩),
           is prepared, without measuring it, on the Bell State Basis,
           resulting on the initial quantum state, |00⟩;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        quantum_register_name = "qu_reg"
        """
        Set the name of the Qiskrypt's Quantum Register.
        """

        quantum_register_num_qubits = 2
        """
        Set the number of qubits for the Qiskrypt's Quantum Register.
        """

        qiskrypt_quantum_register = \
            QiskryptQuantumRegister(name=quantum_register_name,
                                    num_qubits=quantum_register_num_qubits,
                                    qiskit_quantum_register=None)
        """
        Create a Qiskrypt's Quantum Register, given its name and number of qubits.
        """

        quantum_circuit_name = "qu_circ"
        """
        Set the name of the Qiskrypt's Quantum Circuit.
        """

        qiskrypt_quantum_circuit_bell_state_psi_plus_13 = \
            QiskryptQuantumCircuit(name=quantum_circuit_name,
                                   qiskrypt_quantum_registers=[qiskrypt_quantum_register],
                                   qiskrypt_fully_quantum_registers=None,
                                   qiskrypt_semi_quantum_registers=None,
                                   qiskrypt_ancilla_quantum_registers=None,
                                   qiskrypt_ancilla_fully_quantum_registers=None,
                                   qiskrypt_ancilla_semi_quantum_registers=None,
                                   qiskrypt_classical_registers=None,
                                   global_phase=0)
        """
        Create a Qiskrypt's Quantum Circuit, given its name,
        Qiskrypt's Quantum Registers, Qiskrypt's Fully-Quantum Registers,
        Qiskrypt's Semi-Quantum Registers,
        Qiskrypt's Ancilla Quantum Registers, Qiskrypt's Ancilla Fully-Quantum Registers,
        Qiskrypt's Ancilla Semi-Quantum Registers,
        Qiskrypt's Classical Registers and
        Global Phase.
        """

        qiskrypt_bell_state_psi_plus_13 = \
            QiskryptBellState("bell_state_psi_plus_13",
                              qiskrypt_quantum_circuit_bell_state_psi_plus_13,
                              POSSIBLE_CONFIGURATIONS_BELL_STATES[3])
        """
        Create a Qiskrypt's Bell State, for a generation of a Bell's State with the configuration,
        |ψ^+⟩ = 1/sqrt(2) x (|01⟩ + |10⟩).
        """

        qiskrypt_bell_state_psi_plus_13.configure(0, 0, 0, 1)
        """
        Configure the Qiskrypt's Bell State, regarding its control IBM Qiskit's Quantum Register
        and control qubit, as well, its target IBM Qiskit's Quantum Register and target qubit.
        """

        qiskrypt_bell_state_psi_plus_13\
            .prepare_bipartite_entanglement_at_computational_basis(is_to_measure_at_computational_basis=False,
                                                                   qiskit_classical_register_control_index=None,
                                                                   qiskit_classical_register_target_index=None,
                                                                   control_bit_index=None, target_bit_index=None)
        """
        Prepare the Bipartite Quantum Entanglement,
        for the specified Qiskrypt's Bell State, as a Quantum Entangled State,
        without measure it, on the Computational Basis.
        """

        qiskrypt_bell_state_psi_plus_13\
            .prepare_bipartite_entanglement_at_bell_state_basis(is_to_measure_at_bell_state_basis=False,
                                                                qiskit_classical_register_control_index=None,
                                                                qiskit_classical_register_target_index=None,
                                                                control_bit_index=None, target_bit_index=None)
        """
        Prepare the Bipartite Quantum Entanglement,
        for the specified Qiskrypt's Bell State, as a Quantum Entangled State,
        without measure it, on the Bell State Basis.
        """

        qiskit_state_vector_backend = Aer.get_backend("statevector_simulator")
        """
        Getting the Aer Simulator Backend for the State Vector Representation
        (i.e., the quantum state represented as its state vector).
        """

        final_quantum_state_vector_state = \
            execute(qiskrypt_bell_state_psi_plus_13.qiskrypt_quantum_circuit.qiskit_quantum_circuit,
                    qiskit_state_vector_backend).result().get_statevector()
        """
        Execute the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit
        and store the resulted quantum state represented in a final state vector.
        """

        assert_allclose(final_quantum_state_vector_state,
                        array([(1. + 0.j),
                               (0. + 0.j),
                               (0. + 0.j),
                               (0. + 0.j)]),
                        rtol=1e-7, atol=1e-7)
        """
        Perform the Assertion of all close values in the values of the quantum state,
        represented by its state vector describing the given qubits,
        after be initialised a quantum state as |00⟩,
        then prepared Bell's State with the configuration,
        |ψ^+⟩ = 1/sqrt(2) x (|01⟩ + |10⟩),
        on the Computational Basis and then reverting it,
        by preparing it on the Bell State Basis.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_14_prepare_bell_state_basis_bell_state_psi_plus_01(self):
        """
        Test Case #14:

        - Initialise the Qiskrypt's Bell State, prepare it, as an Entangled Quantum State,
          and then, measure in the Bell State Basis.

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Quantum Register is prepared on the quantum state, |01⟩;
        2) The Qiskrypt's Bell State is initialised and configured;
        3) The Qiskrypt's Bell State with the configuration,
           |ψ^+⟩ = 1/sqrt(2) x (|01⟩ + |10⟩),
           is prepared, without measuring it, on the Computational Basis;
        4) The Qiskrypt's Bell State with the configuration,
           |ψ^+⟩ = 1/sqrt(2) x (|01⟩ + |10⟩),
           is prepared, without measuring it, on the Bell State Basis,
           resulting on the initial quantum state, |01⟩;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        quantum_register_name = "qu_reg"
        """
        Set the name of the Qiskrypt's Quantum Register.
        """

        quantum_register_num_qubits = 2
        """
        Set the number of qubits for the Qiskrypt's Quantum Register.
        """

        qiskrypt_quantum_register = \
            QiskryptQuantumRegister(name=quantum_register_name,
                                    num_qubits=quantum_register_num_qubits,
                                    qiskit_quantum_register=None)
        """
        Create a Qiskrypt's Quantum Register, given its name and number of qubits.
        """

        quantum_circuit_name = "qu_circ"
        """
        Set the name of the Qiskrypt's Quantum Circuit.
        """

        qiskrypt_quantum_circuit_bell_state_psi_plus_14 = \
            QiskryptQuantumCircuit(name=quantum_circuit_name,
                                   qiskrypt_quantum_registers=[qiskrypt_quantum_register],
                                   qiskrypt_fully_quantum_registers=None,
                                   qiskrypt_semi_quantum_registers=None,
                                   qiskrypt_ancilla_quantum_registers=None,
                                   qiskrypt_ancilla_fully_quantum_registers=None,
                                   qiskrypt_ancilla_semi_quantum_registers=None,
                                   qiskrypt_classical_registers=None,
                                   global_phase=0)
        """
        Create a Qiskrypt's Quantum Circuit, given its name,
        Qiskrypt's Quantum Registers, Qiskrypt's Fully-Quantum Registers,
        Qiskrypt's Semi-Quantum Registers,
        Qiskrypt's Ancilla Quantum Registers, Qiskrypt's Ancilla Fully-Quantum Registers,
        Qiskrypt's Ancilla Semi-Quantum Registers,
        Qiskrypt's Classical Registers and
        Global Phase.
        """

        qiskrypt_quantum_circuit_bell_state_psi_plus_14 \
            .apply_pauli_x(0, 0)
        """
        Apply the Pauli-X (Bit Flip/NOT) Gate/Operation to the given index for
        the single qubit of the given IBM Qiskit's Quantum Register (|00⟩ ↦ |01⟩).
        """

        qiskrypt_bell_state_psi_plus_14 = \
            QiskryptBellState("bell_state_psi_plus_14",
                              qiskrypt_quantum_circuit_bell_state_psi_plus_14,
                              POSSIBLE_CONFIGURATIONS_BELL_STATES[3])
        """
        Create a Qiskrypt's Bell State, for a generation of a Bell's State with the configuration,
        |ψ^+⟩ = 1/sqrt(2) x (|01⟩ + |10⟩).
        """

        qiskrypt_bell_state_psi_plus_14.configure(0, 0, 0, 1)
        """
        Configure the Qiskrypt's Bell State, regarding its control IBM Qiskit's Quantum Register
        and control qubit, as well, its target IBM Qiskit's Quantum Register and target qubit.
        """

        qiskrypt_bell_state_psi_plus_14\
            .prepare_bipartite_entanglement_at_computational_basis(is_to_measure_at_computational_basis=False,
                                                                   qiskit_classical_register_control_index=None,
                                                                   qiskit_classical_register_target_index=None,
                                                                   control_bit_index=None, target_bit_index=None)
        """
        Prepare the Bipartite Quantum Entanglement,
        for the specified Qiskrypt's Bell State, as a Quantum Entangled State,
        without measure it, on the Computational Basis.
        """

        qiskrypt_bell_state_psi_plus_14\
            .prepare_bipartite_entanglement_at_bell_state_basis(is_to_measure_at_bell_state_basis=False,
                                                                qiskit_classical_register_control_index=None,
                                                                qiskit_classical_register_target_index=None,
                                                                control_bit_index=None, target_bit_index=None)
        """
        Prepare the Bipartite Quantum Entanglement,
        for the specified Qiskrypt's Bell State, as a Quantum Entangled State,
        without measure it, on the Bell State Basis.
        """

        qiskit_state_vector_backend = Aer.get_backend("statevector_simulator")
        """
        Getting the Aer Simulator Backend for the State Vector Representation
        (i.e., the quantum state represented as its state vector).
        """

        final_quantum_state_vector_state = \
            execute(qiskrypt_bell_state_psi_plus_14.qiskrypt_quantum_circuit.qiskit_quantum_circuit,
                    qiskit_state_vector_backend).result().get_statevector()
        """
        Execute the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit
        and store the resulted quantum state represented in a final state vector.
        """

        assert_allclose(final_quantum_state_vector_state,
                        array([(0. + 0.j),
                               (1. + 0.j),
                               (0. + 0.j),
                               (0. + 0.j)]),
                        rtol=1e-7, atol=1e-7)
        """
        Perform the Assertion of all close values in the values of the quantum state,
        represented by its state vector describing the given qubits,
        after be initialised a quantum state as |01⟩,
        then prepared Bell's State with the configuration,
        |ψ^+⟩ = 1/sqrt(2) x (|01⟩ + |10⟩),
        on the Computational Basis and then reverting it,
        by preparing it on the Bell State Basis.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_15_prepare_bell_state_basis_bell_state_psi_plus_10(self):
        """
        Test Case #15:

        - Initialise the Qiskrypt's Bell State, prepare it, as an Entangled Quantum State,
          and then, measure in the Bell State Basis.

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Quantum Register is prepared on the quantum state, |10⟩;
        2) The Qiskrypt's Bell State is initialised and configured;
        3) The Qiskrypt's Bell State with the configuration,
           |ψ^+⟩ = 1/sqrt(2) x (|01⟩ + |10⟩),
           is prepared, without measuring it, on the Computational Basis;
        4) The Qiskrypt's Bell State with the configuration,
           |ψ^+⟩ = 1/sqrt(2) x (|01⟩ + |10⟩),
           is prepared, without measuring it, on the Bell State Basis,
           resulting on the initial quantum state, |10⟩;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        quantum_register_name = "qu_reg"
        """
        Set the name of the Qiskrypt's Quantum Register.
        """

        quantum_register_num_qubits = 2
        """
        Set the number of qubits for the Qiskrypt's Quantum Register.
        """

        qiskrypt_quantum_register = \
            QiskryptQuantumRegister(name=quantum_register_name,
                                    num_qubits=quantum_register_num_qubits,
                                    qiskit_quantum_register=None)
        """
        Create a Qiskrypt's Quantum Register, given its name and number of qubits.
        """

        quantum_circuit_name = "qu_circ"
        """
        Set the name of the Qiskrypt's Quantum Circuit.
        """

        qiskrypt_quantum_circuit_bell_state_psi_plus_15 = \
            QiskryptQuantumCircuit(name=quantum_circuit_name,
                                   qiskrypt_quantum_registers=[qiskrypt_quantum_register],
                                   qiskrypt_fully_quantum_registers=None,
                                   qiskrypt_semi_quantum_registers=None,
                                   qiskrypt_ancilla_quantum_registers=None,
                                   qiskrypt_ancilla_fully_quantum_registers=None,
                                   qiskrypt_ancilla_semi_quantum_registers=None,
                                   qiskrypt_classical_registers=None,
                                   global_phase=0)
        """
        Create a Qiskrypt's Quantum Circuit, given its name,
        Qiskrypt's Quantum Registers, Qiskrypt's Fully-Quantum Registers,
        Qiskrypt's Semi-Quantum Registers,
        Qiskrypt's Ancilla Quantum Registers, Qiskrypt's Ancilla Fully-Quantum Registers,
        Qiskrypt's Ancilla Semi-Quantum Registers,
        Qiskrypt's Classical Registers and
        Global Phase.
        """

        qiskrypt_quantum_circuit_bell_state_psi_plus_15 \
            .apply_pauli_x(0, 1)
        """
        Apply the Pauli-X (Bit Flip/NOT) Gate/Operation to the given index for
        the single qubit of the given IBM Qiskit's Quantum Register (|00⟩ ↦ |10⟩).
        """

        qiskrypt_bell_state_psi_plus_15 = \
            QiskryptBellState("bell_state_psi_plus_15",
                              qiskrypt_quantum_circuit_bell_state_psi_plus_15,
                              POSSIBLE_CONFIGURATIONS_BELL_STATES[3])
        """
        Create a Qiskrypt's Bell State, for a generation of a Bell's State with the configuration,
        |ψ^+⟩ = 1/sqrt(2) x (|01⟩ + |10⟩).
        """

        qiskrypt_bell_state_psi_plus_15.configure(0, 0, 0, 1)
        """
        Configure the Qiskrypt's Bell State, regarding its control IBM Qiskit's Quantum Register
        and control qubit, as well, its target IBM Qiskit's Quantum Register and target qubit.
        """

        qiskrypt_bell_state_psi_plus_15\
            .prepare_bipartite_entanglement_at_computational_basis(is_to_measure_at_computational_basis=False,
                                                                   qiskit_classical_register_control_index=None,
                                                                   qiskit_classical_register_target_index=None,
                                                                   control_bit_index=None, target_bit_index=None)
        """
        Prepare the Bipartite Quantum Entanglement,
        for the specified Qiskrypt's Bell State, as a Quantum Entangled State,
        without measure it, on the Computational Basis.
        """

        qiskrypt_bell_state_psi_plus_15\
            .prepare_bipartite_entanglement_at_bell_state_basis(is_to_measure_at_bell_state_basis=False,
                                                                qiskit_classical_register_control_index=None,
                                                                qiskit_classical_register_target_index=None,
                                                                control_bit_index=None, target_bit_index=None)
        """
        Prepare the Bipartite Quantum Entanglement,
        for the specified Qiskrypt's Bell State, as a Quantum Entangled State,
        without measure it, on the Bell State Basis.
        """

        qiskit_state_vector_backend = Aer.get_backend("statevector_simulator")
        """
        Getting the Aer Simulator Backend for the State Vector Representation
        (i.e., the quantum state represented as its state vector).
        """

        final_quantum_state_vector_state = \
            execute(qiskrypt_bell_state_psi_plus_15.qiskrypt_quantum_circuit.qiskit_quantum_circuit,
                    qiskit_state_vector_backend).result().get_statevector()
        """
        Execute the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit
        and store the resulted quantum state represented in a final state vector.
        """

        assert_allclose(final_quantum_state_vector_state,
                        array([(0. + 0.j),
                               (0. + 0.j),
                               (1. + 0.j),
                               (0. + 0.j)]),
                        rtol=1e-7, atol=1e-7)
        """
        Perform the Assertion of all close values in the values of the quantum state,
        represented by its state vector describing the given qubits,
        after be initialised a quantum state as |10⟩,
        then prepared Bell's State with the configuration,
        |ψ^+⟩ = 1/sqrt(2) x (|01⟩ + |10⟩),
        on the Computational Basis and then reverting it,
        by preparing it on the Bell State Basis.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_16_prepare_bell_state_basis_bell_state_psi_plus_11(self):
        """
        Test Case #16:

        - Initialise the Qiskrypt's Bell State, prepare it, as an Entangled Quantum State,
          and then, measure in the Bell State Basis.

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Quantum Register is prepared on the quantum state, |11⟩;
        2) The Qiskrypt's Bell State is initialised and configured;
        3) The Qiskrypt's Bell State with the configuration,
           |ψ^+⟩ = 1/sqrt(2) x (|01⟩ + |10⟩),
           is prepared, without measuring it, on the Computational Basis;
        4) The Qiskrypt's Bell State with the configuration,
           |ψ^+⟩ = 1/sqrt(2) x (|01⟩ + |10⟩),
           is prepared, without measuring it, on the Bell State Basis,
           resulting on the initial quantum state, |11⟩;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        quantum_register_name = "qu_reg"
        """
        Set the name of the Qiskrypt's Quantum Register.
        """

        quantum_register_num_qubits = 2
        """
        Set the number of qubits for the Qiskrypt's Quantum Register.
        """

        qiskrypt_quantum_register = \
            QiskryptQuantumRegister(name=quantum_register_name,
                                    num_qubits=quantum_register_num_qubits,
                                    qiskit_quantum_register=None)
        """
        Create a Qiskrypt's Quantum Register, given its name and number of qubits.
        """

        quantum_circuit_name = "qu_circ"
        """
        Set the name of the Qiskrypt's Quantum Circuit.
        """

        qiskrypt_quantum_circuit_bell_state_psi_plus_16 = \
            QiskryptQuantumCircuit(name=quantum_circuit_name,
                                   qiskrypt_quantum_registers=[qiskrypt_quantum_register],
                                   qiskrypt_fully_quantum_registers=None,
                                   qiskrypt_semi_quantum_registers=None,
                                   qiskrypt_ancilla_quantum_registers=None,
                                   qiskrypt_ancilla_fully_quantum_registers=None,
                                   qiskrypt_ancilla_semi_quantum_registers=None,
                                   qiskrypt_classical_registers=None,
                                   global_phase=0)
        """
        Create a Qiskrypt's Quantum Circuit, given its name,
        Qiskrypt's Quantum Registers, Qiskrypt's Fully-Quantum Registers,
        Qiskrypt's Semi-Quantum Registers,
        Qiskrypt's Ancilla Quantum Registers, Qiskrypt's Ancilla Fully-Quantum Registers,
        Qiskrypt's Ancilla Semi-Quantum Registers,
        Qiskrypt's Classical Registers and
        Global Phase.
        """

        qiskrypt_quantum_circuit_bell_state_psi_plus_16 \
            .apply_pauli_x(0, 0)
        """
        Apply the Pauli-X (Bit Flip/NOT) Gate/Operation to the given index for
        the single qubit of the given IBM Qiskit's Quantum Register (|00⟩ ↦ |01⟩).
        """

        qiskrypt_quantum_circuit_bell_state_psi_plus_16 \
            .apply_pauli_x(0, 1)
        """
        Apply the Pauli-X (Bit Flip/NOT) Gate/Operation to the given index for
        the single qubit of the given IBM Qiskit's Quantum Register (|01⟩ ↦ |11⟩).
        """

        qiskrypt_bell_state_psi_plus_16 = \
            QiskryptBellState("bell_state_psi_plus_16",
                              qiskrypt_quantum_circuit_bell_state_psi_plus_16,
                              POSSIBLE_CONFIGURATIONS_BELL_STATES[3])
        """
        Create a Qiskrypt's Bell State, for a generation of a Bell's State with the configuration,
        |ψ^+⟩ = 1/sqrt(2) x (|01⟩ + |10⟩).
        """

        qiskrypt_bell_state_psi_plus_16.configure(0, 0, 0, 1)
        """
        Configure the Qiskrypt's Bell State, regarding its control IBM Qiskit's Quantum Register
        and control qubit, as well, its target IBM Qiskit's Quantum Register and target qubit.
        """

        qiskrypt_bell_state_psi_plus_16\
            .prepare_bipartite_entanglement_at_computational_basis(is_to_measure_at_computational_basis=False,
                                                                   qiskit_classical_register_control_index=None,
                                                                   qiskit_classical_register_target_index=None,
                                                                   control_bit_index=None, target_bit_index=None)
        """
        Prepare the Bipartite Quantum Entanglement,
        for the specified Qiskrypt's Bell State, as a Quantum Entangled State,
        without measure it, on the Computational Basis.
        """

        qiskrypt_bell_state_psi_plus_16\
            .prepare_bipartite_entanglement_at_bell_state_basis(is_to_measure_at_bell_state_basis=False,
                                                                qiskit_classical_register_control_index=None,
                                                                qiskit_classical_register_target_index=None,
                                                                control_bit_index=None, target_bit_index=None)
        """
        Prepare the Bipartite Quantum Entanglement,
        for the specified Qiskrypt's Bell State, as a Quantum Entangled State,
        without measure it, on the Bell State Basis.
        """

        qiskit_state_vector_backend = Aer.get_backend("statevector_simulator")
        """
        Getting the Aer Simulator Backend for the State Vector Representation
        (i.e., the quantum state represented as its state vector).
        """

        final_quantum_state_vector_state = \
            execute(qiskrypt_bell_state_psi_plus_16.qiskrypt_quantum_circuit.qiskit_quantum_circuit,
                    qiskit_state_vector_backend).result().get_statevector()
        """
        Execute the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit
        and store the resulted quantum state represented in a final state vector.
        """

        assert_allclose(final_quantum_state_vector_state,
                        array([(0. + 0.j),
                               (0. + 0.j),
                               (0. + 0.j),
                               (1. + 0.j)]),
                        rtol=1e-7, atol=1e-7)
        """
        Perform the Assertion of all close values in the values of the quantum state,
        represented by its state vector describing the given qubits,
        after be initialised a quantum state as |11⟩,
        then prepared Bell's State with the configuration,
        |ψ^+⟩ = 1/sqrt(2) x (|01⟩ + |10⟩),
        on the Computational Basis and then reverting it,
        by preparing it on the Bell State Basis.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_17_prepare_bell_state_basis_bell_state_psi_minus_00(self):
        """
        Test Case #17:

        - Initialise the Qiskrypt's Bell State, prepare it, as an Entangled Quantum State,
          and then, measure in the Bell State Basis.

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Quantum Register is prepared on the quantum state, |00⟩;
        2) The Qiskrypt's Bell State is initialised and configured;
        3) The Qiskrypt's Bell State with the configuration,
           |ψ^-⟩ = 1/sqrt(2) x (|01⟩ - |10⟩),
           is prepared, without measuring it, on the Computational Basis;
        4) The Qiskrypt's Bell State with the configuration,
           |ψ^-⟩ = 1/sqrt(2) x (|01⟩ - |10⟩),
           is prepared, without measuring it, on the Bell State Basis,
           resulting on the initial quantum state, |00⟩;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        quantum_register_name = "qu_reg"
        """
        Set the name of the Qiskrypt's Quantum Register.
        """

        quantum_register_num_qubits = 2
        """
        Set the number of qubits for the Qiskrypt's Quantum Register.
        """

        qiskrypt_quantum_register = \
            QiskryptQuantumRegister(name=quantum_register_name,
                                    num_qubits=quantum_register_num_qubits,
                                    qiskit_quantum_register=None)
        """
        Create a Qiskrypt's Quantum Register, given its name and number of qubits.
        """

        quantum_circuit_name = "qu_circ"
        """
        Set the name of the Qiskrypt's Quantum Circuit.
        """

        qiskrypt_quantum_circuit_bell_state_psi_minus_17 = \
            QiskryptQuantumCircuit(name=quantum_circuit_name,
                                   qiskrypt_quantum_registers=[qiskrypt_quantum_register],
                                   qiskrypt_fully_quantum_registers=None,
                                   qiskrypt_semi_quantum_registers=None,
                                   qiskrypt_ancilla_quantum_registers=None,
                                   qiskrypt_ancilla_fully_quantum_registers=None,
                                   qiskrypt_ancilla_semi_quantum_registers=None,
                                   qiskrypt_classical_registers=None,
                                   global_phase=0)
        """
        Create a Qiskrypt's Quantum Circuit, given its name,
        Qiskrypt's Quantum Registers, Qiskrypt's Fully-Quantum Registers,
        Qiskrypt's Semi-Quantum Registers,
        Qiskrypt's Ancilla Quantum Registers, Qiskrypt's Ancilla Fully-Quantum Registers,
        Qiskrypt's Ancilla Semi-Quantum Registers,
        Qiskrypt's Classical Registers and
        Global Phase.
        """

        qiskrypt_bell_state_psi_minus_17 = \
            QiskryptBellState("bell_state_psi_minus_17",
                              qiskrypt_quantum_circuit_bell_state_psi_minus_17,
                              POSSIBLE_CONFIGURATIONS_BELL_STATES[4])
        """
        Create a Qiskrypt's Bell State, for a generation of a Bell's State with the configuration,
        |ψ^-⟩ = 1/sqrt(2) x (|01⟩ - |10⟩).
        """

        qiskrypt_bell_state_psi_minus_17.configure(0, 0, 0, 1)
        """
        Configure the Qiskrypt's Bell State, regarding its control IBM Qiskit's Quantum Register
        and control qubit, as well, its target IBM Qiskit's Quantum Register and target qubit.
        """

        qiskrypt_bell_state_psi_minus_17\
            .prepare_bipartite_entanglement_at_computational_basis(is_to_measure_at_computational_basis=False,
                                                                   qiskit_classical_register_control_index=None,
                                                                   qiskit_classical_register_target_index=None,
                                                                   control_bit_index=None, target_bit_index=None)
        """
        Prepare the Bipartite Quantum Entanglement,
        for the specified Qiskrypt's Bell State, as a Quantum Entangled State,
        without measure it, on the Computational Basis.
        """

        qiskrypt_bell_state_psi_minus_17\
            .prepare_bipartite_entanglement_at_bell_state_basis(is_to_measure_at_bell_state_basis=False,
                                                                qiskit_classical_register_control_index=None,
                                                                qiskit_classical_register_target_index=None,
                                                                control_bit_index=None, target_bit_index=None)
        """
        Prepare the Bipartite Quantum Entanglement,
        for the specified Qiskrypt's Bell State, as a Quantum Entangled State,
        without measure it, on the Bell State Basis.
        """

        qiskit_state_vector_backend = Aer.get_backend("statevector_simulator")
        """
        Getting the Aer Simulator Backend for the State Vector Representation
        (i.e., the quantum state represented as its state vector).
        """

        final_quantum_state_vector_state = \
            execute(qiskrypt_bell_state_psi_minus_17.qiskrypt_quantum_circuit.qiskit_quantum_circuit,
                    qiskit_state_vector_backend).result().get_statevector()
        """
        Execute the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit
        and store the resulted quantum state represented in a final state vector.
        """

        assert_allclose(final_quantum_state_vector_state,
                        array([(1. + 0.j),
                               (0. + 0.j),
                               (0. + 0.j),
                               (0. + 0.j)]),
                        rtol=1e-7, atol=1e-7)
        """
        Perform the Assertion of all close values in the values of the quantum state,
        represented by its state vector describing the given qubits,
        after be initialised a quantum state as |00⟩,
        then prepared Bell's State with the configuration,
        |ψ^-⟩ = 1/sqrt(2) x (|01⟩ - |10⟩),
        on the Computational Basis and then reverting it,
        by preparing it on the Bell State Basis.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_18_prepare_bell_state_basis_bell_state_psi_minus_01(self):
        """
        Test Case #18:

        - Initialise the Qiskrypt's Bell State, prepare it, as an Entangled Quantum State,
          and then, measure in the Bell State Basis.

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Quantum Register is prepared on the quantum state, |01⟩;
        2) The Qiskrypt's Bell State is initialised and configured;
        3) The Qiskrypt's Bell State with the configuration,
           |ψ^-⟩ = 1/sqrt(2) x (|01⟩ - |10⟩),
           is prepared, without measuring it, on the Computational Basis;
        4) The Qiskrypt's Bell State with the configuration,
           |ψ^-⟩ = 1/sqrt(2) x (|01⟩ - |10⟩),
           is prepared, without measuring it, on the Bell State Basis,
           resulting on the initial quantum state, |01⟩;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        quantum_register_name = "qu_reg"
        """
        Set the name of the Qiskrypt's Quantum Register.
        """

        quantum_register_num_qubits = 2
        """
        Set the number of qubits for the Qiskrypt's Quantum Register.
        """

        qiskrypt_quantum_register = \
            QiskryptQuantumRegister(name=quantum_register_name,
                                    num_qubits=quantum_register_num_qubits,
                                    qiskit_quantum_register=None)
        """
        Create a Qiskrypt's Quantum Register, given its name and number of qubits.
        """

        quantum_circuit_name = "qu_circ"
        """
        Set the name of the Qiskrypt's Quantum Circuit.
        """

        qiskrypt_quantum_circuit_bell_state_psi_minus_18 = \
            QiskryptQuantumCircuit(name=quantum_circuit_name,
                                   qiskrypt_quantum_registers=[qiskrypt_quantum_register],
                                   qiskrypt_fully_quantum_registers=None,
                                   qiskrypt_semi_quantum_registers=None,
                                   qiskrypt_ancilla_quantum_registers=None,
                                   qiskrypt_ancilla_fully_quantum_registers=None,
                                   qiskrypt_ancilla_semi_quantum_registers=None,
                                   qiskrypt_classical_registers=None,
                                   global_phase=0)
        """
        Create a Qiskrypt's Quantum Circuit, given its name,
        Qiskrypt's Quantum Registers, Qiskrypt's Fully-Quantum Registers,
        Qiskrypt's Semi-Quantum Registers,
        Qiskrypt's Ancilla Quantum Registers, Qiskrypt's Ancilla Fully-Quantum Registers,
        Qiskrypt's Ancilla Semi-Quantum Registers,
        Qiskrypt's Classical Registers and
        Global Phase.
        """

        qiskrypt_quantum_circuit_bell_state_psi_minus_18 \
            .apply_pauli_x(0, 0)
        """
        Apply the Pauli-X (Bit Flip/NOT) Gate/Operation to the given index for
        the single qubit of the given IBM Qiskit's Quantum Register (|00⟩ ↦ |01⟩).
        """

        qiskrypt_bell_state_psi_minus_18 = \
            QiskryptBellState("bell_state_psi_minus_18",
                              qiskrypt_quantum_circuit_bell_state_psi_minus_18,
                              POSSIBLE_CONFIGURATIONS_BELL_STATES[4])
        """
        Create a Qiskrypt's Bell State, for a generation of a Bell's State with the configuration,
        |ψ^-⟩ = 1/sqrt(2) x (|01⟩ - |10⟩).
        """

        qiskrypt_bell_state_psi_minus_18.configure(0, 0, 0, 1)
        """
        Configure the Qiskrypt's Bell State, regarding its control IBM Qiskit's Quantum Register
        and control qubit, as well, its target IBM Qiskit's Quantum Register and target qubit.
        """

        qiskrypt_bell_state_psi_minus_18\
            .prepare_bipartite_entanglement_at_computational_basis(is_to_measure_at_computational_basis=False,
                                                                   qiskit_classical_register_control_index=None,
                                                                   qiskit_classical_register_target_index=None,
                                                                   control_bit_index=None, target_bit_index=None)
        """
        Prepare the Bipartite Quantum Entanglement,
        for the specified Qiskrypt's Bell State, as a Quantum Entangled State,
        without measure it, on the Computational Basis.
        """

        qiskrypt_bell_state_psi_minus_18\
            .prepare_bipartite_entanglement_at_bell_state_basis(is_to_measure_at_bell_state_basis=False,
                                                                qiskit_classical_register_control_index=None,
                                                                qiskit_classical_register_target_index=None,
                                                                control_bit_index=None, target_bit_index=None)
        """
        Prepare the Bipartite Quantum Entanglement,
        for the specified Qiskrypt's Bell State, as a Quantum Entangled State,
        without measure it, on the Bell State Basis.
        """

        qiskit_state_vector_backend = Aer.get_backend("statevector_simulator")
        """
        Getting the Aer Simulator Backend for the State Vector Representation
        (i.e., the quantum state represented as its state vector).
        """

        final_quantum_state_vector_state = \
            execute(qiskrypt_bell_state_psi_minus_18.qiskrypt_quantum_circuit.qiskit_quantum_circuit,
                    qiskit_state_vector_backend).result().get_statevector()
        """
        Execute the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit
        and store the resulted quantum state represented in a final state vector.
        """

        assert_allclose(final_quantum_state_vector_state,
                        array([(0. + 0.j),
                               (1. + 0.j),
                               (0. + 0.j),
                               (0. + 0.j)]),
                        rtol=1e-7, atol=1e-7)
        """
        Perform the Assertion of all close values in the values of the quantum state,
        represented by its state vector describing the given qubits,
        after be initialised a quantum state as |01⟩,
        then prepared Bell's State with the configuration,
        |ψ^-⟩ = 1/sqrt(2) x (|01⟩ - |10⟩),
        on the Computational Basis and then reverting it,
        by preparing it on the Bell State Basis.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_19_prepare_bell_state_basis_bell_state_psi_minus_10(self):
        """
        Test Case #19:

        - Initialise the Qiskrypt's Bell State, prepare it, as an Entangled Quantum State,
          and then, measure in the Bell State Basis.

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Quantum Register is prepared on the quantum state, |10⟩;
        2) The Qiskrypt's Bell State is initialised and configured;
        3) The Qiskrypt's Bell State with the configuration,
           |ψ^-⟩ = 1/sqrt(2) x (|01⟩ - |10⟩),
           is prepared, without measuring it, on the Computational Basis;
        4) The Qiskrypt's Bell State with the configuration,
           |ψ^-⟩ = 1/sqrt(2) x (|01⟩ - |10⟩),
           is prepared, without measuring it, on the Bell State Basis,
           resulting on the initial quantum state, |10⟩;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        quantum_register_name = "qu_reg"
        """
        Set the name of the Qiskrypt's Quantum Register.
        """

        quantum_register_num_qubits = 2
        """
        Set the number of qubits for the Qiskrypt's Quantum Register.
        """

        qiskrypt_quantum_register = \
            QiskryptQuantumRegister(name=quantum_register_name,
                                    num_qubits=quantum_register_num_qubits,
                                    qiskit_quantum_register=None)
        """
        Create a Qiskrypt's Quantum Register, given its name and number of qubits.
        """

        quantum_circuit_name = "qu_circ"
        """
        Set the name of the Qiskrypt's Quantum Circuit.
        """

        qiskrypt_quantum_circuit_bell_state_psi_minus_19 = \
            QiskryptQuantumCircuit(name=quantum_circuit_name,
                                   qiskrypt_quantum_registers=[qiskrypt_quantum_register],
                                   qiskrypt_fully_quantum_registers=None,
                                   qiskrypt_semi_quantum_registers=None,
                                   qiskrypt_ancilla_quantum_registers=None,
                                   qiskrypt_ancilla_fully_quantum_registers=None,
                                   qiskrypt_ancilla_semi_quantum_registers=None,
                                   qiskrypt_classical_registers=None,
                                   global_phase=0)
        """
        Create a Qiskrypt's Quantum Circuit, given its name,
        Qiskrypt's Quantum Registers, Qiskrypt's Fully-Quantum Registers,
        Qiskrypt's Semi-Quantum Registers,
        Qiskrypt's Ancilla Quantum Registers, Qiskrypt's Ancilla Fully-Quantum Registers,
        Qiskrypt's Ancilla Semi-Quantum Registers,
        Qiskrypt's Classical Registers and
        Global Phase.
        """

        qiskrypt_quantum_circuit_bell_state_psi_minus_19 \
            .apply_pauli_x(0, 1)
        """
        Apply the Pauli-X (Bit Flip/NOT) Gate/Operation to the given index for
        the single qubit of the given IBM Qiskit's Quantum Register (|00⟩ ↦ |10⟩).
        """

        qiskrypt_bell_state_psi_minus_19 = \
            QiskryptBellState("bell_state_psi_minus_19",
                              qiskrypt_quantum_circuit_bell_state_psi_minus_19,
                              POSSIBLE_CONFIGURATIONS_BELL_STATES[4])
        """
        Create a Qiskrypt's Bell State, for a generation of a Bell's State with the configuration,
        |ψ^-⟩ = 1/sqrt(2) x (|01⟩ - |10⟩).
        """

        qiskrypt_bell_state_psi_minus_19.configure(0, 0, 0, 1)
        """
        Configure the Qiskrypt's Bell State, regarding its control IBM Qiskit's Quantum Register
        and control qubit, as well, its target IBM Qiskit's Quantum Register and target qubit.
        """

        qiskrypt_bell_state_psi_minus_19\
            .prepare_bipartite_entanglement_at_computational_basis(is_to_measure_at_computational_basis=False,
                                                                   qiskit_classical_register_control_index=None,
                                                                   qiskit_classical_register_target_index=None,
                                                                   control_bit_index=None, target_bit_index=None)
        """
        Prepare the Bipartite Quantum Entanglement,
        for the specified Qiskrypt's Bell State, as a Quantum Entangled State,
        without measure it, on the Computational Basis.
        """

        qiskrypt_bell_state_psi_minus_19\
            .prepare_bipartite_entanglement_at_bell_state_basis(is_to_measure_at_bell_state_basis=False,
                                                                qiskit_classical_register_control_index=None,
                                                                qiskit_classical_register_target_index=None,
                                                                control_bit_index=None, target_bit_index=None)
        """
        Prepare the Bipartite Quantum Entanglement,
        for the specified Qiskrypt's Bell State, as a Quantum Entangled State,
        without measure it, on the Bell State Basis.
        """

        qiskit_state_vector_backend = Aer.get_backend("statevector_simulator")
        """
        Getting the Aer Simulator Backend for the State Vector Representation
        (i.e., the quantum state represented as its state vector).
        """

        final_quantum_state_vector_state = \
            execute(qiskrypt_bell_state_psi_minus_19.qiskrypt_quantum_circuit.qiskit_quantum_circuit,
                    qiskit_state_vector_backend).result().get_statevector()
        """
        Execute the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit
        and store the resulted quantum state represented in a final state vector.
        """

        assert_allclose(final_quantum_state_vector_state,
                        array([(0. + 0.j),
                               (0. + 0.j),
                               (1. + 0.j),
                               (0. + 0.j)]),
                        rtol=1e-7, atol=1e-7)
        """
        Perform the Assertion of all close values in the values of the quantum state,
        represented by its state vector describing the given qubits,
        after be initialised a quantum state as |10⟩,
        then prepared Bell's State with the configuration,
        |ψ^-⟩ = 1/sqrt(2) x (|01⟩ - |10⟩),
        on the Computational Basis and then reverting it,
        by preparing it on the Bell State Basis.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_20_prepare_bell_state_basis_bell_state_psi_minus_11(self):
        """
        Test Case #20:

        - Initialise the Qiskrypt's Bell State, prepare it, as an Entangled Quantum State,
          and then, measure in the Bell State Basis.

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Quantum Register is prepared on the quantum state, |11⟩;
        2) The Qiskrypt's Bell State is initialised and configured;
        3) The Qiskrypt's Bell State with the configuration,
           |ψ^-⟩ = 1/sqrt(2) x (|01⟩ - |10⟩),
           is prepared, without measuring it, on the Computational Basis;
        4) The Qiskrypt's Bell State with the configuration,
           |ψ^-⟩ = 1/sqrt(2) x (|01⟩ - |10⟩),
           is prepared, without measuring it, on the Bell State Basis,
           resulting on the initial quantum state, |11⟩;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        quantum_register_name = "qu_reg"
        """
        Set the name of the Qiskrypt's Quantum Register.
        """

        quantum_register_num_qubits = 2
        """
        Set the number of qubits for the Qiskrypt's Quantum Register.
        """

        qiskrypt_quantum_register = \
            QiskryptQuantumRegister(name=quantum_register_name,
                                    num_qubits=quantum_register_num_qubits,
                                    qiskit_quantum_register=None)
        """
        Create a Qiskrypt's Quantum Register, given its name and number of qubits.
        """

        quantum_circuit_name = "qu_circ"
        """
        Set the name of the Qiskrypt's Quantum Circuit.
        """

        qiskrypt_quantum_circuit_bell_state_psi_minus_20 = \
            QiskryptQuantumCircuit(name=quantum_circuit_name,
                                   qiskrypt_quantum_registers=[qiskrypt_quantum_register],
                                   qiskrypt_fully_quantum_registers=None,
                                   qiskrypt_semi_quantum_registers=None,
                                   qiskrypt_ancilla_quantum_registers=None,
                                   qiskrypt_ancilla_fully_quantum_registers=None,
                                   qiskrypt_ancilla_semi_quantum_registers=None,
                                   qiskrypt_classical_registers=None,
                                   global_phase=0)
        """
        Create a Qiskrypt's Quantum Circuit, given its name,
        Qiskrypt's Quantum Registers, Qiskrypt's Fully-Quantum Registers,
        Qiskrypt's Semi-Quantum Registers,
        Qiskrypt's Ancilla Quantum Registers, Qiskrypt's Ancilla Fully-Quantum Registers,
        Qiskrypt's Ancilla Semi-Quantum Registers,
        Qiskrypt's Classical Registers and
        Global Phase.
        """

        qiskrypt_quantum_circuit_bell_state_psi_minus_20 \
            .apply_pauli_x(0, 0)
        """
        Apply the Pauli-X (Bit Flip/NOT) Gate/Operation to the given index for
        the single qubit of the given IBM Qiskit's Quantum Register (|00⟩ ↦ |01⟩).
        """

        qiskrypt_quantum_circuit_bell_state_psi_minus_20 \
            .apply_pauli_x(0, 1)
        """
        Apply the Pauli-X (Bit Flip/NOT) Gate/Operation to the given index for
        the single qubit of the given IBM Qiskit's Quantum Register (|01⟩ ↦ |11⟩).
        """

        qiskrypt_bell_state_psi_minus_20 = \
            QiskryptBellState("bell_state_psi_minus_20",
                              qiskrypt_quantum_circuit_bell_state_psi_minus_20,
                              POSSIBLE_CONFIGURATIONS_BELL_STATES[4])
        """
        Create a Qiskrypt's Bell State, for a generation of a Bell's State with the configuration,
        |ψ^-⟩ = 1/sqrt(2) x (|01⟩ - |10⟩).
        """

        qiskrypt_bell_state_psi_minus_20.configure(0, 0, 0, 1)
        """
        Configure the Qiskrypt's Bell State, regarding its control IBM Qiskit's Quantum Register
        and control qubit, as well, its target IBM Qiskit's Quantum Register and target qubit.
        """

        qiskrypt_bell_state_psi_minus_20\
            .prepare_bipartite_entanglement_at_computational_basis(is_to_measure_at_computational_basis=False,
                                                                   qiskit_classical_register_control_index=None,
                                                                   qiskit_classical_register_target_index=None,
                                                                   control_bit_index=None, target_bit_index=None)
        """
        Prepare the Bipartite Quantum Entanglement,
        for the specified Qiskrypt's Bell State, as a Quantum Entangled State,
        without measure it, on the Computational Basis.
        """

        qiskrypt_bell_state_psi_minus_20\
            .prepare_bipartite_entanglement_at_bell_state_basis(is_to_measure_at_bell_state_basis=False,
                                                                qiskit_classical_register_control_index=None,
                                                                qiskit_classical_register_target_index=None,
                                                                control_bit_index=None, target_bit_index=None)
        """
        Prepare the Bipartite Quantum Entanglement,
        for the specified Qiskrypt's Bell State, as a Quantum Entangled State,
        without measure it, on the Bell State Basis.
        """

        qiskit_state_vector_backend = Aer.get_backend("statevector_simulator")
        """
        Getting the Aer Simulator Backend for the State Vector Representation
        (i.e., the quantum state represented as its state vector).
        """

        final_quantum_state_vector_state = \
            execute(qiskrypt_bell_state_psi_minus_20.qiskrypt_quantum_circuit.qiskit_quantum_circuit,
                    qiskit_state_vector_backend).result().get_statevector()
        """
        Execute the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit
        and store the resulted quantum state represented in a final state vector.
        """

        assert_allclose(final_quantum_state_vector_state,
                        array([(0. + 0.j),
                               (0. + 0.j),
                               (0. + 0.j),
                               (1. + 0.j)]),
                        rtol=1e-7, atol=1e-7)
        """
        Perform the Assertion of all close values in the values of the quantum state,
        represented by its state vector describing the given qubits,
        after be initialised a quantum state as |11⟩,
        then prepared Bell's State with the configuration,
        |ψ^-⟩ = 1/sqrt(2) x (|01⟩ - |10⟩),
        on the Computational Basis and then reverting it,
        by preparing it on the Bell State Basis.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)


if __name__ == "__main__":
    """
    The Main Method for the Unitary Test.
    """

    qiskrypt_bell_states_test_cases = \
        TestLoader().loadTestsFromTestCase(QiskryptBellStateTests)
    """
    Load the Test Cases from the Unitary Tests for the Qiskrypt's Bell States.
    """

    qiskrypt_bell_states_test_suite = TestSuite([qiskrypt_bell_states_test_cases])
    """
    Load the Test Suite with all the Test Cases for the Qiskrypt's Bell States.
    """
