"""

Copyrights:\n
- © Qiskrypt, 2022 - All rights reserved.\n

Powered by:\n
- IBM
- IBM Quantum
- IBM Qiskit


Description:\n
- The Qiskrypt is a software suite of protocols of
  quantum_regime cryptography, quantum_regime communication and
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

from unittest import TestCase, TestLoader, TestSuite
"""
Import TestCase, TestLoader and TestSuite from Unittest.
"""

from numpy import sqrt, full
"""
Import the Square Root and Full functions from Python's NumPy.
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

from src.quantum_regime.circuit.registers.quantum.QiskryptQuantumRegister \
    import QiskryptQuantumRegister
"""
Import the Qiskrypt's Quantum Register.
"""

from src.quantum_regime.circuit.QiskryptQuantumCircuit \
    import QiskryptQuantumCircuit
"""
Import the Qiskrypt's Quantum Circuit.
"""

from src.quantum_regime.transforms.pauli.x.QiskryptQuantumPauliXTransform \
    import QiskryptQuantumPauliXTransform
"""
Import the Qiskrypt's Quantum Pauli-X Transform.
"""

from src.quantum_regime.entanglements.multipartite.resource.cluster.QiskryptClusterState \
    import QiskryptClusterState
"""
Import the Qiskrypt's Cluster State.
"""


class QiskryptClusterStateTests(TestCase):
    """
    Object Class of the Unitary Tests for the Qiskrypt's Cluster State.
    """

    def test_no_1_prepare_computational_basis_qiskrypt_cluster_state_3_qubits(self):
        """
        Test Case #1:

        - Initialise the Qiskrypt's Cluster State and prepare it, as an Entangled Quantum State,
          in the Computational Basis.

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Cluster State is initialised and configured, for 3 qubits;
        2) The Qiskrypt's Cluster State is prepared, without measuring it, on the Computational Basis;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        quantum_register_name = "qu_reg"
        """
        Set the name of the Qiskrypt's Quantum Register.
        """

        quantum_register_num_qubits = 3
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

        qiskrypt_quantum_circuit_cluster_state_3_qubits_1 = \
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

        qiskrypt_cluster_state_3_qubits_1 = \
            QiskryptClusterState("cluster_state_3_qubits_1",
                                 qiskrypt_quantum_circuit_cluster_state_3_qubits_1)
        """
        Create a Qiskrypt's Cluster State, for a generation of a Cluster State with 3 qubits.
        """

        qiskrypt_cluster_state_3_qubits_1.configure([0, 0, 0],
                                                    [0, 1, 2])
        """
        Configure the Qiskrypt's Cluster State, regarding its IBM Qiskit's Quantum Registers and qubits.
        """

        qiskrypt_cluster_state_3_qubits_1 \
            .prepare_multipartite_entanglement_at_computational_basis(is_to_measure_at_computational_basis=False,
                                                                      qiskit_classical_registers_indexes=None,
                                                                      bits_vertices_indexes=None)
        """
        Prepare the Multipartite Quantum Entanglement,
        for the specified Qiskrypt's Cluster State, as a Quantum Entangled State,
        without measure it, on the Computational Basis.
        """

        qiskit_state_vector_backend = Aer.get_backend("statevector_simulator")
        """
        Getting the Aer Simulator Backend for the State Vector Representation
        (i.e., the quantum_regime state represented as its state vector).
        """

        final_quantum_state_vector_state = \
            execute(qiskrypt_cluster_state_3_qubits_1.qiskrypt_quantum_circuit.qiskit_quantum_circuit,
                    qiskit_state_vector_backend).result().get_statevector()
        """
        Execute the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit
        and store the resulted quantum_regime state represented in a final state vector.
        """

        num_possible_outcomes = (2 ** quantum_register_num_qubits)
        """
        Compute the number of possible outcomes (i.e., 2^(quantum_register_num_qubits)).
        """

        cluster_state_3_qubits_array_expected_amplitudes = \
            full((num_possible_outcomes,), (1 / sqrt(num_possible_outcomes)) * (1. + 0.j))
        """
        Create and fill an array with (1. / sqrt(8)) for the expected values of
        the Qiskrypt's Cluster State, with 3 qubits.
        """

        qubits_indexes_symmetric_phase = [3, 5, 6, 7]
        """
        Compute the list of indexes of IBM Qiskit's Quantum Registers and qubits,
        in a Quantum Superposition of States, expected to have symmetric phase.
        """

        for qubit_index_symmetric_phase in qubits_indexes_symmetric_phase:
            """
            For each index of the IBM Qiskit's Quantum Registers and qubits,
            in a Quantum Superposition of States, expected to have symmetric phase.
            """

            cluster_state_3_qubits_array_expected_amplitudes[qubit_index_symmetric_phase] *= -1.0
            """
            Fill the current position of the expected values of
            the Qiskrypt's Cluster State, with ((1. / sqrt(8)) * (1. + 0.j)).
            """

        assert_allclose(final_quantum_state_vector_state,
                        cluster_state_3_qubits_array_expected_amplitudes,
                        rtol=1e-7, atol=1e-7)
        """
        Perform the Assertion of all close values in the values of the quantum_regime state,
        represented by its state vector describing the given qubits, after be prepared a Cluster State.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_2_prepare_computational_basis_qiskrypt_cluster_state_4_qubits(self):
        """
        Test Case #2:

        - Initialise the Qiskrypt's Cluster State and prepare it, as an Entangled Quantum State,
          in the Computational Basis.

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Cluster State is initialised and configured, for 4 qubits;
        2) The Qiskrypt's Cluster State is prepared, without measuring it, on the Computational Basis;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        quantum_register_name = "qu_reg"
        """
        Set the name of the Qiskrypt's Quantum Register.
        """

        quantum_register_num_qubits = 4
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

        qiskrypt_quantum_circuit_cluster_state_4_qubits_2 = \
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

        qiskrypt_cluster_state_4_qubits_2 = \
            QiskryptClusterState("cluster_state_4_qubits_2",
                                 qiskrypt_quantum_circuit_cluster_state_4_qubits_2)
        """
        Create a Qiskrypt's Cluster State, for a generation of a Cluster State with 4 qubits.
        """

        qiskrypt_cluster_state_4_qubits_2.configure([0, 0, 0, 0],
                                                    [0, 1, 2, 3])
        """
        Configure the Qiskrypt's Cluster State, regarding its IBM Qiskit's Quantum Registers and qubits.
        """

        qiskrypt_cluster_state_4_qubits_2 \
            .prepare_multipartite_entanglement_at_computational_basis(is_to_measure_at_computational_basis=False,
                                                                      qiskit_classical_registers_indexes=None,
                                                                      bits_vertices_indexes=None)
        """
        Prepare the Multipartite Quantum Entanglement,
        for the specified Qiskrypt's Cluster State, as a Quantum Entangled State,
        without measure it, on the Computational Basis.
        """

        qiskit_state_vector_backend = Aer.get_backend("statevector_simulator")
        """
        Getting the Aer Simulator Backend for the State Vector Representation
        (i.e., the quantum_regime state represented as its state vector).
        """

        final_quantum_state_vector_state = \
            execute(qiskrypt_cluster_state_4_qubits_2.qiskrypt_quantum_circuit.qiskit_quantum_circuit,
                    qiskit_state_vector_backend).result().get_statevector()
        """
        Execute the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit
        and store the resulted quantum_regime state represented in a final state vector.
        """

        num_possible_outcomes = (2 ** quantum_register_num_qubits)
        """
        Compute the number of possible outcomes (i.e., 2^(quantum_register_num_qubits)).
        """

        cluster_state_4_qubits_array_expected_amplitudes = \
            full((num_possible_outcomes,), (1 / sqrt(num_possible_outcomes)) * (1. + 0.j))
        """
        Create and fill an array with (1. / sqrt(16)) for the expected values of
        the Qiskrypt's Cluster State, with 4 qubits.
        """

        qubits_indexes_symmetric_phase = [3, 6, 9, 12]
        """
        Compute the list of indexes of IBM Qiskit's Quantum Registers and qubits,
        in a Quantum Superposition of States, expected to have symmetric phase.
        """

        for qubit_index_symmetric_phase in qubits_indexes_symmetric_phase:
            """
            For each index of the IBM Qiskit's Quantum Registers and qubits,
            in a Quantum Superposition of States, expected to have symmetric phase.
            """

            cluster_state_4_qubits_array_expected_amplitudes[qubit_index_symmetric_phase] *= -1.0
            """
            Fill the current position of the expected values of
            the Qiskrypt's Cluster State, with ((1. / sqrt(16)) * (1. + 0.j)).
            """

        assert_allclose(final_quantum_state_vector_state,
                        cluster_state_4_qubits_array_expected_amplitudes,
                        rtol=1e-7, atol=1e-7)
        """
        Perform the Assertion of all close values in the values of the quantum_regime state,
        represented by its state vector describing the given qubits, after be prepared a Cluster State.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_3_prepare_computational_basis_qiskrypt_cluster_state_5_qubits(self):
        """
        Test Case #3:

        - Initialise the Qiskrypt's Cluster State and prepare it, as an Entangled Quantum State,
          in the Computational Basis.

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Cluster State is initialised and configured, for 5 qubits;
        2) The Qiskrypt's Cluster State is prepared, without measuring it, on the Computational Basis;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        quantum_register_name = "qu_reg"
        """
        Set the name of the Qiskrypt's Quantum Register.
        """

        quantum_register_num_qubits = 5
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

        qiskrypt_quantum_circuit_cluster_state_5_qubits_3 = \
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

        qiskrypt_cluster_state_5_qubits_3 = \
            QiskryptClusterState("cluster_state_5_qubits_3",
                                 qiskrypt_quantum_circuit_cluster_state_5_qubits_3)
        """
        Create a Qiskrypt's Cluster State, for a generation of a Cluster State with 5 qubits.
        """

        qiskrypt_cluster_state_5_qubits_3.configure([0, 0, 0, 0, 0],
                                                    [0, 1, 2, 3, 4])
        """
        Configure the Qiskrypt's Cluster State, regarding its IBM Qiskit's Quantum Registers and qubits.
        """

        qiskrypt_cluster_state_5_qubits_3 \
            .prepare_multipartite_entanglement_at_computational_basis(is_to_measure_at_computational_basis=False,
                                                                      qiskit_classical_registers_indexes=None,
                                                                      bits_vertices_indexes=None)
        """
        Prepare the Multipartite Quantum Entanglement,
        for the specified Qiskrypt's Cluster State, as a Quantum Entangled State,
        without measure it, on the Computational Basis.
        """

        qiskit_state_vector_backend = Aer.get_backend("statevector_simulator")
        """
        Getting the Aer Simulator Backend for the State Vector Representation
        (i.e., the quantum_regime state represented as its state vector).
        """

        final_quantum_state_vector_state = \
            execute(qiskrypt_cluster_state_5_qubits_3.qiskrypt_quantum_circuit.qiskit_quantum_circuit,
                    qiskit_state_vector_backend).result().get_statevector()
        """
        Execute the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit
        and store the resulted quantum_regime state represented in a final state vector.
        """

        num_possible_outcomes = (2 ** quantum_register_num_qubits)
        """
        Compute the number of possible outcomes (i.e., 2^(quantum_register_num_qubits)).
        """

        cluster_state_5_qubits_array_expected_amplitudes = \
            full((num_possible_outcomes,), (1 / sqrt(num_possible_outcomes)) * (1. + 0.j))
        """
        Create and fill an array with (1. / sqrt(32)) for the expected values of
        the Qiskrypt's Cluster State, with 5 qubits.
        """

        qubits_indexes_symmetric_phase = [3, 6, 11, 12, 13, 15, 17, 21,
                                          22, 23, 24, 26, 27, 29, 30, 31]
        """
        Compute the list of indexes of IBM Qiskit's Quantum Registers and qubits,
        in a Quantum Superposition of States, expected to have symmetric phase.
        """

        for qubit_index_symmetric_phase in qubits_indexes_symmetric_phase:
            """
            For each index of the IBM Qiskit's Quantum Registers and qubits,
            in a Quantum Superposition of States, expected to have symmetric phase.
            """

            cluster_state_5_qubits_array_expected_amplitudes[qubit_index_symmetric_phase] *= -1.0
            """
            Fill the current position of the expected values of
            the Qiskrypt's Cluster State, with ((1. / sqrt(32)) * (1. + 0.j)).
            """

        assert_allclose(final_quantum_state_vector_state,
                        cluster_state_5_qubits_array_expected_amplitudes,
                        rtol=1e-7, atol=1e-7)
        """
        Perform the Assertion of all close values in the values of the quantum_regime state,
        represented by its state vector describing the given qubits, after be prepared a Cluster State.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_4_prepare_computational_basis_qiskrypt_cluster_state_6_qubits(self):
        """
        Test Case #4:

        - Initialise the Qiskrypt's Cluster State and prepare it, as an Entangled Quantum State,
          in the Computational Basis.

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Cluster State is initialised and configured, for 6 qubits;
        2) The Qiskrypt's Cluster State is prepared, without measuring it, on the Computational Basis;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        quantum_register_name = "qu_reg"
        """
        Set the name of the Qiskrypt's Quantum Register.
        """

        quantum_register_num_qubits = 6
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

        qiskrypt_quantum_circuit_cluster_state_6_qubits_4 = \
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

        qiskrypt_cluster_state_6_qubits_4 = \
            QiskryptClusterState("cluster_state_6_qubits_4",
                                 qiskrypt_quantum_circuit_cluster_state_6_qubits_4)
        """
        Create a Qiskrypt's Cluster State, for a generation of a Cluster State with 6 qubits.
        """

        qiskrypt_cluster_state_6_qubits_4.configure([0, 0, 0, 0, 0, 0],
                                                    [0, 1, 2, 3, 4, 5])
        """
        Configure the Qiskrypt's Cluster State, regarding its IBM Qiskit's Quantum Registers and qubits.
        """

        qiskrypt_cluster_state_6_qubits_4 \
            .prepare_multipartite_entanglement_at_computational_basis(is_to_measure_at_computational_basis=False,
                                                                      qiskit_classical_registers_indexes=None,
                                                                      bits_vertices_indexes=None)
        """
        Prepare the Multipartite Quantum Entanglement,
        for the specified Qiskrypt's Cluster State, as a Quantum Entangled State,
        without measure it, on the Computational Basis.
        """

        qiskit_state_vector_backend = Aer.get_backend("statevector_simulator")
        """
        Getting the Aer Simulator Backend for the State Vector Representation
        (i.e., the quantum_regime state represented as its state vector).
        """

        final_quantum_state_vector_state = \
            execute(qiskrypt_cluster_state_6_qubits_4.qiskrypt_quantum_circuit.qiskit_quantum_circuit,
                    qiskit_state_vector_backend).result().get_statevector()
        """
        Execute the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit
        and store the resulted quantum_regime state represented in a final state vector.
        """

        num_possible_outcomes = (2 ** quantum_register_num_qubits)
        """
        Compute the number of possible outcomes (i.e., 2^(quantum_register_num_qubits)).
        """

        cluster_state_6_qubits_array_expected_amplitudes = \
            full((num_possible_outcomes,), (1 / sqrt(num_possible_outcomes)) * (1. + 0.j))
        """
        Create and fill an array with (1. / sqrt(64)) for the expected values of
        the Qiskrypt's Cluster State, with 6 qubits.
        """

        qubits_indexes_symmetric_phase = [3, 6, 11, 12, 13, 15, 19, 22, 24, 25, 26, 30,
                                          33, 37, 38, 39, 41, 44, 48, 50, 51, 52, 57, 60]
        """
        Compute the list of indexes of IBM Qiskit's Quantum Registers and qubits,
        in a Quantum Superposition of States, expected to have symmetric phase.
        """

        for qubit_index_symmetric_phase in qubits_indexes_symmetric_phase:
            """
            For each index of the IBM Qiskit's Quantum Registers and qubits,
            in a Quantum Superposition of States, expected to have symmetric phase.
            """

            cluster_state_6_qubits_array_expected_amplitudes[qubit_index_symmetric_phase] *= -1.0
            """
            Fill the current position of the expected values of
            the Qiskrypt's Cluster State, with ((1. / sqrt(64)) * (1. + 0.j)).
            """

        assert_allclose(final_quantum_state_vector_state,
                        cluster_state_6_qubits_array_expected_amplitudes,
                        rtol=1e-7, atol=1e-7)
        """
        Perform the Assertion of all close values in the values of the quantum_regime state,
        represented by its state vector describing the given qubits, after be prepared a Cluster State.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_5_prepare_cluster_state_basis_qiskrypt_cluster_state_3_qubits_000(self):
        """
        Test Case #5:

        - Initialise the Qiskrypt's Cluster State and prepare it, as an Entangled Quantum State,
          in the Cluster State Basis.

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Cluster State is initialised and configured, for 3 qubits;
        2) The Qiskrypt's Cluster State is prepared, without measuring it,
           on the Computational Basis;
        3) The Qiskrypt's Cluster State is prepared, without measuring it,
           on the Cluster State Basis;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        quantum_register_name = "qu_reg"
        """
        Set the name of the Qiskrypt's Quantum Register.
        """

        quantum_register_num_qubits = 3
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

        qiskrypt_quantum_circuit_cluster_state_3_qubits_000_5 = \
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

        qiskrypt_cluster_state_3_qubits_000_5 = \
            QiskryptClusterState("cluster_state_3_qubits_5",
                                 qiskrypt_quantum_circuit_cluster_state_3_qubits_000_5)
        """
        Create a Qiskrypt's Cluster State, for a generation of a Cluster State with 3 qubits.
        """

        qiskrypt_cluster_state_3_qubits_000_5.configure([0, 0, 0],
                                                        [0, 1, 2])
        """
        Configure the Qiskrypt's Cluster State, regarding its IBM Qiskit's Quantum Register and qubits.
        """

        qiskrypt_cluster_state_3_qubits_000_5 \
            .prepare_multipartite_entanglement_at_computational_basis(is_to_measure_at_computational_basis=False,
                                                                      qiskit_classical_registers_indexes=None,
                                                                      bits_vertices_indexes=None)
        """
        Prepare the Multipartite Quantum Entanglement,
        for the specified Qiskrypt's Cluster State, as a Quantum Entangled State,
        without measure it, on the Computational Basis.
        """

        qiskrypt_cluster_state_3_qubits_000_5 \
            .prepare_multipartite_entanglement_at_cluster_state_basis(is_to_measure_at_cluster_state_basis=False,
                                                                      qiskit_classical_registers_indexes=None,
                                                                      bits_vertices_indexes=None)
        """
        Prepare the Multipartite Quantum Entanglement,
        for the specified Qiskrypt's Cluster State, as a Quantum Entangled State,
        without measure it, on the Cluster State Basis.
        """

        qiskit_state_vector_backend = Aer.get_backend("statevector_simulator")
        """
        Getting the Aer Simulator Backend for the State Vector Representation
        (i.e., the quantum_regime state represented as its state vector).
        """

        final_quantum_state_vector_state = \
            execute(qiskrypt_cluster_state_3_qubits_000_5.qiskrypt_quantum_circuit.qiskit_quantum_circuit,
                    qiskit_state_vector_backend).result().get_statevector()
        """
        Execute the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit
        and store the resulted quantum_regime state represented in a final state vector.
        """

        num_possible_outcomes = (2 ** quantum_register_num_qubits)
        """
        Compute the number of possible outcomes (i.e., 2^(quantum_register_num_qubits)).
        """

        cluster_state_3_qubits_array_expected_amplitudes = \
            full((num_possible_outcomes,), (0. + 0.j))
        """
        Create and fill an array with the zeros for the expected values of
        the Qiskrypt's Cluster State, with 3 qubits.
        """

        cluster_state_3_qubits_array_expected_amplitudes[0] = (1. + 0.j)
        """
        Fill the first position of the expected values of
        the Qiskrypt's Cluster State, with (1. + 0.j).
        """

        assert_allclose(final_quantum_state_vector_state,
                        cluster_state_3_qubits_array_expected_amplitudes,
                        rtol=1e-7, atol=1e-7)
        """
        Perform the Assertion of all close values in the values of the quantum_regime state,
        represented by its state vector describing the given qubits,
        after be prepared a Cluster State with the configuration,
        |C_3⟩ = |000⟩, in Cluster State Basis.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_6_prepare_cluster_state_basis_qiskrypt_cluster_state_3_qubits_111(self):
        """
        Test Case #6:

        - Initialise the Qiskrypt's Cluster State and prepare it, as an Entangled Quantum State,
          in the Cluster State Basis.

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Quantum Pauli-X Transform is initialised and configured, for 3 qubits;
        2) The Qiskrypt's Cluster State is initialised and configured, for 3 qubits;
        3) The Qiskrypt's Cluster State is prepared, without measuring it,
           on the Computational Basis;
        4) The Qiskrypt's Cluster State is prepared, without measuring it,
           on the Cluster State Basis;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        quantum_register_name = "qu_reg"
        """
        Set the name of the Qiskrypt's Quantum Register.
        """

        quantum_register_num_qubits = 3
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

        qiskrypt_quantum_circuit_cluster_state_3_qubits_111_6 = \
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

        qiskrypt_quantum_pauli_x_transform_3_qubits_111_6 = \
            QiskryptQuantumPauliXTransform("pauli_x_transform_3_qubits_6",
                                           qiskrypt_quantum_circuit_cluster_state_3_qubits_111_6,
                                           ([0] * quantum_register_num_qubits),
                                           [*range(quantum_register_num_qubits)])
        """
        Create the Qiskrypt's Quantum Pauli-X Transform, for 1 Qiskrypt's Quantum Register and 3 qubits.
        """

        qiskrypt_quantum_pauli_x_transform_3_qubits_111_6.apply_transform()
        """
        Apply the Quantum Pauli-X Transform to the Qiskrypt's Quantum Registers and qubits involved.
        """

        qiskrypt_quantum_circuit_cluster_state_3_qubits_111_6 = \
            qiskrypt_quantum_pauli_x_transform_3_qubits_111_6.get_qiskrypt_quantum_circuit()
        """
        Retrieve the Qiskrypt's Quantum Circuit from
        the previously created Qiskrypt's Quantum Pauli-X Transform, for 3 qubits.
        """

        qiskrypt_cluster_state_3_qubits_111_6 = \
            QiskryptClusterState("cluster_state_3_qubits_6",
                                 qiskrypt_quantum_circuit_cluster_state_3_qubits_111_6)
        """
        Create a Qiskrypt's Cluster State, for a generation of a Cluster State with 3 qubits.
        """

        qiskrypt_cluster_state_3_qubits_111_6.configure([0, 0, 0],
                                                        [0, 1, 2])
        """
        Configure the Qiskrypt's Cluster State, regarding its IBM Qiskit's Quantum Register and qubits.
        """

        qiskrypt_cluster_state_3_qubits_111_6 \
            .prepare_multipartite_entanglement_at_computational_basis(is_to_measure_at_computational_basis=False,
                                                                      qiskit_classical_registers_indexes=None,
                                                                      bits_vertices_indexes=None)
        """
        Prepare the Multipartite Quantum Entanglement,
        for the specified Qiskrypt's Cluster State, as a Quantum Entangled State,
        without measure it, on the Computational Basis.
        """

        qiskrypt_cluster_state_3_qubits_111_6 \
            .prepare_multipartite_entanglement_at_cluster_state_basis(is_to_measure_at_cluster_state_basis=False,
                                                                      qiskit_classical_registers_indexes=None,
                                                                      bits_vertices_indexes=None)
        """
        Prepare the Multipartite Quantum Entanglement,
        for the specified Qiskrypt's Cluster State, as a Quantum Entangled State,
        without measure it, on the Cluster State Basis.
        """

        qiskit_state_vector_backend = Aer.get_backend("statevector_simulator")
        """
        Getting the Aer Simulator Backend for the State Vector Representation
        (i.e., the quantum_regime state represented as its state vector).
        """

        final_quantum_state_vector_state = \
            execute(qiskrypt_cluster_state_3_qubits_111_6.qiskrypt_quantum_circuit.qiskit_quantum_circuit,
                    qiskit_state_vector_backend).result().get_statevector()
        """
        Execute the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit
        and store the resulted quantum_regime state represented in a final state vector.
        """

        num_possible_outcomes = (2 ** quantum_register_num_qubits)
        """
        Compute the number of possible outcomes (i.e., 2^(quantum_register_num_qubits)).
        """

        cluster_state_3_qubits_array_expected_amplitudes = \
            full((num_possible_outcomes,), (0. + 0.j))
        """
        Create and fill an array with the zeros for the expected values of
        the Qiskrypt's Cluster State, with 3 qubits.
        """

        cluster_state_3_qubits_array_expected_amplitudes[(num_possible_outcomes - 1)] = (1. + 0.j)
        """
        Fill the last position of the expected values of
        the Qiskrypt's Cluster State, with (1. + 0.j).
        """

        assert_allclose(final_quantum_state_vector_state,
                        cluster_state_3_qubits_array_expected_amplitudes,
                        rtol=1e-7, atol=1e-7)
        """
        Perform the Assertion of all close values in the values of the quantum_regime state,
        represented by its state vector describing the given qubits,
        after be prepared a Cluster State with the configuration,
        |C_3⟩ = |111⟩, in Cluster State Basis.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_7_prepare_cluster_state_basis_qiskrypt_cluster_state_4_qubits_0000(self):
        """
        Test Case #7:

        - Initialise the Qiskrypt's Cluster State and prepare it, as an Entangled Quantum State,
          in the Cluster State Basis.

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Cluster State is initialised and configured, for 4 qubits;
        2) The Qiskrypt's Cluster State is prepared, without measuring it,
           on the Computational Basis;
        3) The Qiskrypt's Cluster State is prepared, without measuring it,
           on the Cluster State Basis;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        quantum_register_name = "qu_reg"
        """
        Set the name of the Qiskrypt's Quantum Register.
        """

        quantum_register_num_qubits = 4
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

        qiskrypt_quantum_circuit_cluster_state_4_qubits_0000_7 = \
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

        qiskrypt_cluster_state_4_qubits_0000_7 = \
            QiskryptClusterState("cluster_state_4_qubits_7",
                                 qiskrypt_quantum_circuit_cluster_state_4_qubits_0000_7)
        """
        Create a Qiskrypt's Cluster State, for a generation of a Cluster State with 4 qubits.
        """

        qiskrypt_cluster_state_4_qubits_0000_7.configure([0, 0, 0, 0],
                                                         [0, 1, 2, 3])
        """
        Configure the Qiskrypt's Cluster State, regarding its IBM Qiskit's Quantum Register and qubits.
        """

        qiskrypt_cluster_state_4_qubits_0000_7 \
            .prepare_multipartite_entanglement_at_computational_basis(is_to_measure_at_computational_basis=False,
                                                                      qiskit_classical_registers_indexes=None,
                                                                      bits_vertices_indexes=None)
        """
        Prepare the Multipartite Quantum Entanglement,
        for the specified Qiskrypt's Cluster State, as a Quantum Entangled State,
        without measure it, on the Computational Basis.
        """

        qiskrypt_cluster_state_4_qubits_0000_7 \
            .prepare_multipartite_entanglement_at_cluster_state_basis(is_to_measure_at_cluster_state_basis=False,
                                                                      qiskit_classical_registers_indexes=None,
                                                                      bits_vertices_indexes=None)
        """
        Prepare the Multipartite Quantum Entanglement,
        for the specified Qiskrypt's Cluster State, as a Quantum Entangled State,
        without measure it, on the Cluster State Basis.
        """

        qiskit_state_vector_backend = Aer.get_backend("statevector_simulator")
        """
        Getting the Aer Simulator Backend for the State Vector Representation
        (i.e., the quantum_regime state represented as its state vector).
        """

        final_quantum_state_vector_state = \
            execute(qiskrypt_cluster_state_4_qubits_0000_7.qiskrypt_quantum_circuit.qiskit_quantum_circuit,
                    qiskit_state_vector_backend).result().get_statevector()
        """
        Execute the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit
        and store the resulted quantum_regime state represented in a final state vector.
        """

        num_possible_outcomes = (2 ** quantum_register_num_qubits)
        """
        Compute the number of possible outcomes (i.e., 2^(quantum_register_num_qubits)).
        """

        cluster_state_4_qubits_array_expected_amplitudes = \
            full((num_possible_outcomes,), (0. + 0.j))
        """
        Create and fill an array with the zeros for the expected values of
        the Qiskrypt's Cluster State, with 4 qubits.
        """

        cluster_state_4_qubits_array_expected_amplitudes[0] = (1. + 0.j)
        """
        Fill the first position of the expected values of
        the Qiskrypt's Cluster State, with (1. + 0.j).
        """

        assert_allclose(final_quantum_state_vector_state,
                        cluster_state_4_qubits_array_expected_amplitudes,
                        rtol=1e-7, atol=1e-7)
        """
        Perform the Assertion of all close values in the values of the quantum_regime state,
        represented by its state vector describing the given qubits,
        after be prepared a Cluster State with the configuration,
        |C_4⟩ = |0000⟩, in Cluster State Basis.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_8_prepare_cluster_state_basis_qiskrypt_cluster_state_4_qubits_1111(self):
        """
        Test Case #8:

        - Initialise the Qiskrypt's Cluster State and prepare it, as an Entangled Quantum State,
          in the Cluster State Basis.

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Quantum Pauli-X Transform is initialised and configured, for 4 qubits;
        2) The Qiskrypt's Cluster State is initialised and configured, for 4 qubits;
        3) The Qiskrypt's Cluster State is prepared, without measuring it,
           on the Computational Basis;
        4) The Qiskrypt's Cluster State is prepared, without measuring it,
           on the Cluster State Basis;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        quantum_register_name = "qu_reg"
        """
        Set the name of the Qiskrypt's Quantum Register.
        """

        quantum_register_num_qubits = 4
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

        qiskrypt_quantum_circuit_cluster_state_4_qubits_1111_8 = \
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

        qiskrypt_quantum_pauli_x_transform_4_qubits_1111_8 = \
            QiskryptQuantumPauliXTransform("pauli_x_transform_4_qubits_8",
                                           qiskrypt_quantum_circuit_cluster_state_4_qubits_1111_8,
                                           ([0] * quantum_register_num_qubits),
                                           [*range(quantum_register_num_qubits)])
        """
        Create the Qiskrypt's Quantum Pauli-X Transform, for 1 Qiskrypt's Quantum Register and 4 qubits.
        """

        qiskrypt_quantum_pauli_x_transform_4_qubits_1111_8.apply_transform()
        """
        Apply the Quantum Pauli-X Transform to the Qiskrypt's Quantum Registers and qubits involved.
        """

        qiskrypt_quantum_circuit_cluster_state_4_qubits_1111_8 = \
            qiskrypt_quantum_pauli_x_transform_4_qubits_1111_8.get_qiskrypt_quantum_circuit()
        """
        Retrieve the Qiskrypt's Quantum Circuit from
        the previously created Qiskrypt's Quantum Pauli-X Transform, for 4 qubits.
        """

        qiskrypt_cluster_state_4_qubits_1111_8 = \
            QiskryptClusterState("cluster_state_4_qubits_8",
                                 qiskrypt_quantum_circuit_cluster_state_4_qubits_1111_8)
        """
        Create a Qiskrypt's Cluster State, for a generation of a Cluster State with 4 qubits.
        """

        qiskrypt_cluster_state_4_qubits_1111_8.configure([0, 0, 0, 0],
                                                         [0, 1, 2, 3])
        """
        Configure the Qiskrypt's Cluster State, regarding its IBM Qiskit's Quantum Register and qubits.
        """

        qiskrypt_cluster_state_4_qubits_1111_8 \
            .prepare_multipartite_entanglement_at_computational_basis(is_to_measure_at_computational_basis=False,
                                                                      qiskit_classical_registers_indexes=None,
                                                                      bits_vertices_indexes=None)
        """
        Prepare the Multipartite Quantum Entanglement,
        for the specified Qiskrypt's Cluster State, as a Quantum Entangled State,
        without measure it, on the Computational Basis.
        """

        qiskrypt_cluster_state_4_qubits_1111_8 \
            .prepare_multipartite_entanglement_at_cluster_state_basis(is_to_measure_at_cluster_state_basis=False,
                                                                      qiskit_classical_registers_indexes=None,
                                                                      bits_vertices_indexes=None)
        """
        Prepare the Multipartite Quantum Entanglement,
        for the specified Qiskrypt's Cluster State, as a Quantum Entangled State,
        without measure it, on the Cluster State Basis.
        """

        qiskit_state_vector_backend = Aer.get_backend("statevector_simulator")
        """
        Getting the Aer Simulator Backend for the State Vector Representation
        (i.e., the quantum_regime state represented as its state vector).
        """

        final_quantum_state_vector_state = \
            execute(qiskrypt_cluster_state_4_qubits_1111_8.qiskrypt_quantum_circuit.qiskit_quantum_circuit,
                    qiskit_state_vector_backend).result().get_statevector()
        """
        Execute the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit
        and store the resulted quantum_regime state represented in a final state vector.
        """

        num_possible_outcomes = (2 ** quantum_register_num_qubits)
        """
        Compute the number of possible outcomes (i.e., 2^(quantum_register_num_qubits)).
        """

        cluster_state_4_qubits_array_expected_amplitudes = \
            full((num_possible_outcomes,), (0. + 0.j))
        """
        Create and fill an array with the zeros for the expected values of
        the Qiskrypt's Cluster State, with 4 qubits.
        """

        cluster_state_4_qubits_array_expected_amplitudes[(num_possible_outcomes - 1)] = (1. + 0.j)
        """
        Fill the last position of the expected values of
        the Qiskrypt's Cluster State, with (1. + 0.j).
        """

        assert_allclose(final_quantum_state_vector_state,
                        cluster_state_4_qubits_array_expected_amplitudes,
                        rtol=1e-7, atol=1e-7)
        """
        Perform the Assertion of all close values in the values of the quantum_regime state,
        represented by its state vector describing the given qubits,
        after be prepared a Cluster State with the configuration,
        |C_4⟩ = |1111⟩, in Cluster State Basis.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_9_prepare_cluster_state_basis_qiskrypt_cluster_state_5_qubits_00000(self):
        """
        Test Case #9:

        - Initialise the Qiskrypt's Cluster State and prepare it, as an Entangled Quantum State,
          in the Cluster State Basis.

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Cluster State is initialised and configured, for 5 qubits;
        2) The Qiskrypt's Cluster State is prepared, without measuring it,
           on the Computational Basis;
        3) The Qiskrypt's Cluster State is prepared, without measuring it,
           on the Cluster State Basis;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        quantum_register_name = "qu_reg"
        """
        Set the name of the Qiskrypt's Quantum Register.
        """

        quantum_register_num_qubits = 5
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

        qiskrypt_quantum_circuit_cluster_state_5_qubits_00000_9 = \
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

        qiskrypt_cluster_state_5_qubits_00000_9 = \
            QiskryptClusterState("cluster_state_5_qubits_9",
                                 qiskrypt_quantum_circuit_cluster_state_5_qubits_00000_9)
        """
        Create a Qiskrypt's Cluster State, for a generation of a Cluster State with 5 qubits.
        """

        qiskrypt_cluster_state_5_qubits_00000_9.configure([0, 0, 0, 0, 0],
                                                          [0, 1, 2, 3, 4])
        """
        Configure the Qiskrypt's Cluster State, regarding its IBM Qiskit's Quantum Register and qubits.
        """

        qiskrypt_cluster_state_5_qubits_00000_9 \
            .prepare_multipartite_entanglement_at_computational_basis(is_to_measure_at_computational_basis=False,
                                                                      qiskit_classical_registers_indexes=None,
                                                                      bits_vertices_indexes=None)
        """
        Prepare the Multipartite Quantum Entanglement,
        for the specified Qiskrypt's Cluster State, as a Quantum Entangled State,
        without measure it, on the Computational Basis.
        """

        qiskrypt_cluster_state_5_qubits_00000_9 \
            .prepare_multipartite_entanglement_at_cluster_state_basis(is_to_measure_at_cluster_state_basis=False,
                                                                      qiskit_classical_registers_indexes=None,
                                                                      bits_vertices_indexes=None)
        """
        Prepare the Multipartite Quantum Entanglement,
        for the specified Qiskrypt's Cluster State, as a Quantum Entangled State,
        without measure it, on the Cluster State Basis.
        """

        qiskit_state_vector_backend = Aer.get_backend("statevector_simulator")
        """
        Getting the Aer Simulator Backend for the State Vector Representation
        (i.e., the quantum_regime state represented as its state vector).
        """

        final_quantum_state_vector_state = \
            execute(qiskrypt_cluster_state_5_qubits_00000_9.qiskrypt_quantum_circuit.qiskit_quantum_circuit,
                    qiskit_state_vector_backend).result().get_statevector()
        """
        Execute the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit
        and store the resulted quantum_regime state represented in a final state vector.
        """

        num_possible_outcomes = (2 ** quantum_register_num_qubits)
        """
        Compute the number of possible outcomes (i.e., 2^(quantum_register_num_qubits)).
        """

        cluster_state_5_qubits_array_expected_amplitudes = \
            full((num_possible_outcomes,), (0. + 0.j))
        """
        Create and fill an array with the zeros for the expected values of
        the Qiskrypt's Cluster State, with 5 qubits.
        """

        cluster_state_5_qubits_array_expected_amplitudes[0] = (1. + 0.j)
        """
        Fill the first position of the expected values of
        the Qiskrypt's Cluster State, with (1. + 0.j).
        """

        assert_allclose(final_quantum_state_vector_state,
                        cluster_state_5_qubits_array_expected_amplitudes,
                        rtol=1e-7, atol=1e-7)
        """
        Perform the Assertion of all close values in the values of the quantum_regime state,
        represented by its state vector describing the given qubits,
        after be prepared a Cluster State with the configuration,
        |C_5⟩ = |00000⟩, in Cluster State Basis.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_10_prepare_cluster_state_basis_qiskrypt_cluster_state_5_qubits_11111(self):
        """
        Test Case #10:

        - Initialise the Qiskrypt's Cluster State and prepare it, as an Entangled Quantum State,
          in the Cluster State Basis.

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Quantum Pauli-X Transform is initialised and configured, for 5 qubits;
        2) The Qiskrypt's Cluster State is initialised and configured, for 5 qubits;
        3) The Qiskrypt's Cluster State is prepared, without measuring it,
           on the Computational Basis;
        4) The Qiskrypt's Cluster State is prepared, without measuring it,
           on the Cluster State Basis;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        quantum_register_name = "qu_reg"
        """
        Set the name of the Qiskrypt's Quantum Register.
        """

        quantum_register_num_qubits = 5
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

        qiskrypt_quantum_circuit_cluster_state_5_qubits_11111_10 = \
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

        qiskrypt_quantum_pauli_x_transform_5_qubits_11111_10 = \
            QiskryptQuantumPauliXTransform("pauli_x_transform_5_qubits_10",
                                           qiskrypt_quantum_circuit_cluster_state_5_qubits_11111_10,
                                           ([0] * quantum_register_num_qubits),
                                           [*range(quantum_register_num_qubits)])
        """
        Create the Qiskrypt's Quantum Pauli-X Transform, for 1 Qiskrypt's Quantum Register and 5 qubits.
        """

        qiskrypt_quantum_pauli_x_transform_5_qubits_11111_10.apply_transform()
        """
        Apply the Quantum Pauli-X Transform to the Qiskrypt's Quantum Registers and qubits involved.
        """

        qiskrypt_quantum_circuit_cluster_state_5_qubits_11111_10 = \
            qiskrypt_quantum_pauli_x_transform_5_qubits_11111_10.get_qiskrypt_quantum_circuit()
        """
        Retrieve the Qiskrypt's Quantum Circuit from
        the previously created Qiskrypt's Quantum Pauli-X Transform, for 5 qubits.
        """

        qiskrypt_cluster_state_5_qubits_11111_10 = \
            QiskryptClusterState("cluster_state_5_qubits_10",
                                 qiskrypt_quantum_circuit_cluster_state_5_qubits_11111_10)
        """
        Create a Qiskrypt's Cluster State, for a generation of a Cluster State with 5 qubits.
        """

        qiskrypt_cluster_state_5_qubits_11111_10.configure([0, 0, 0, 0, 0],
                                                           [0, 1, 2, 3, 4])
        """
        Configure the Qiskrypt's Cluster State, regarding its IBM Qiskit's Quantum Register and qubits.
        """

        qiskrypt_cluster_state_5_qubits_11111_10 \
            .prepare_multipartite_entanglement_at_computational_basis(is_to_measure_at_computational_basis=False,
                                                                      qiskit_classical_registers_indexes=None,
                                                                      bits_vertices_indexes=None)
        """
        Prepare the Multipartite Quantum Entanglement,
        for the specified Qiskrypt's Cluster State, as a Quantum Entangled State,
        without measure it, on the Computational Basis.
        """

        qiskrypt_cluster_state_5_qubits_11111_10 \
            .prepare_multipartite_entanglement_at_cluster_state_basis(is_to_measure_at_cluster_state_basis=False,
                                                                      qiskit_classical_registers_indexes=None,
                                                                      bits_vertices_indexes=None)
        """
        Prepare the Multipartite Quantum Entanglement,
        for the specified Qiskrypt's Cluster State, as a Quantum Entangled State,
        without measure it, on the Cluster State Basis.
        """

        qiskit_state_vector_backend = Aer.get_backend("statevector_simulator")
        """
        Getting the Aer Simulator Backend for the State Vector Representation
        (i.e., the quantum_regime state represented as its state vector).
        """

        final_quantum_state_vector_state = \
            execute(qiskrypt_cluster_state_5_qubits_11111_10.qiskrypt_quantum_circuit.qiskit_quantum_circuit,
                    qiskit_state_vector_backend).result().get_statevector()
        """
        Execute the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit
        and store the resulted quantum_regime state represented in a final state vector.
        """

        num_possible_outcomes = (2 ** quantum_register_num_qubits)
        """
        Compute the number of possible outcomes (i.e., 2^(quantum_register_num_qubits)).
        """

        cluster_state_5_qubits_array_expected_amplitudes = \
            full((num_possible_outcomes,), (0. + 0.j))
        """
        Create and fill an array with the zeros for the expected values of
        the Qiskrypt's Cluster State, with 5 qubits.
        """

        cluster_state_5_qubits_array_expected_amplitudes[(num_possible_outcomes - 1)] = (1. + 0.j)
        """
        Fill the last position of the expected values of
        the Qiskrypt's Cluster State, with (1. + 0.j).
        """

        assert_allclose(final_quantum_state_vector_state,
                        cluster_state_5_qubits_array_expected_amplitudes,
                        rtol=1e-7, atol=1e-7)
        """
        Perform the Assertion of all close values in the values of the quantum_regime state,
        represented by its state vector describing the given qubits,
        after be prepared a Cluster State with the configuration,
        |C_5⟩ = |11111⟩, in Cluster State Basis.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_11_prepare_cluster_state_basis_qiskrypt_cluster_state_6_qubits_000000(self):
        """
        Test Case #11:

        - Initialise the Qiskrypt's Cluster State and prepare it, as an Entangled Quantum State,
          in the Cluster State Basis.

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Cluster State is initialised and configured, for 6 qubits;
        2) The Qiskrypt's Cluster State is prepared, without measuring it,
           on the Computational Basis;
        3) The Qiskrypt's Cluster State is prepared, without measuring it,
           on the Cluster State Basis;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        quantum_register_name = "qu_reg"
        """
        Set the name of the Qiskrypt's Quantum Register.
        """

        quantum_register_num_qubits = 6
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

        qiskrypt_quantum_circuit_cluster_state_6_qubits_000000_11 = \
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

        qiskrypt_cluster_state_6_qubits_000000_11 = \
            QiskryptClusterState("cluster_state_6_qubits_11",
                                 qiskrypt_quantum_circuit_cluster_state_6_qubits_000000_11)
        """
        Create a Qiskrypt's Cluster State, for a generation of a Cluster State with 6 qubits.
        """

        qiskrypt_cluster_state_6_qubits_000000_11.configure([0, 0, 0, 0, 0, 0],
                                                            [0, 1, 2, 3, 4, 5])
        """
        Configure the Qiskrypt's Cluster State, regarding its IBM Qiskit's Quantum Register and qubits.
        """

        qiskrypt_cluster_state_6_qubits_000000_11 \
            .prepare_multipartite_entanglement_at_computational_basis(is_to_measure_at_computational_basis=False,
                                                                      qiskit_classical_registers_indexes=None,
                                                                      bits_vertices_indexes=None)
        """
        Prepare the Multipartite Quantum Entanglement,
        for the specified Qiskrypt's Cluster State, as a Quantum Entangled State,
        without measure it, on the Computational Basis.
        """

        qiskrypt_cluster_state_6_qubits_000000_11 \
            .prepare_multipartite_entanglement_at_cluster_state_basis(is_to_measure_at_cluster_state_basis=False,
                                                                      qiskit_classical_registers_indexes=None,
                                                                      bits_vertices_indexes=None)
        """
        Prepare the Multipartite Quantum Entanglement,
        for the specified Qiskrypt's Cluster State, as a Quantum Entangled State,
        without measure it, on the Cluster State Basis.
        """

        qiskit_state_vector_backend = Aer.get_backend("statevector_simulator")
        """
        Getting the Aer Simulator Backend for the State Vector Representation
        (i.e., the quantum_regime state represented as its state vector).
        """

        final_quantum_state_vector_state = \
            execute(qiskrypt_cluster_state_6_qubits_000000_11.qiskrypt_quantum_circuit.qiskit_quantum_circuit,
                    qiskit_state_vector_backend).result().get_statevector()
        """
        Execute the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit
        and store the resulted quantum_regime state represented in a final state vector.
        """

        num_possible_outcomes = (2 ** quantum_register_num_qubits)
        """
        Compute the number of possible outcomes (i.e., 2^(quantum_register_num_qubits)).
        """

        cluster_state_6_qubits_array_expected_amplitudes = \
            full((num_possible_outcomes,), (0. + 0.j))
        """
        Create and fill an array with the zeros for the expected values of
        the Qiskrypt's Cluster State, with 6 qubits.
        """

        cluster_state_6_qubits_array_expected_amplitudes[0] = (1. + 0.j)
        """
        Fill the first position of the expected values of
        the Qiskrypt's Cluster State, with (1. + 0.j).
        """

        assert_allclose(final_quantum_state_vector_state,
                        cluster_state_6_qubits_array_expected_amplitudes,
                        rtol=1e-7, atol=1e-7)
        """
        Perform the Assertion of all close values in the values of the quantum_regime state,
        represented by its state vector describing the given qubits,
        after be prepared a Cluster State with the configuration,
        |C_6⟩ = |000000⟩, in Cluster State Basis.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_12_prepare_cluster_state_basis_qiskrypt_cluster_state_6_qubits_111111(self):
        """
        Test Case #12:

        - Initialise the Qiskrypt's Cluster State and prepare it, as an Entangled Quantum State,
          in the Cluster State Basis.

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Quantum Pauli-X Transform is initialised and configured, for 6 qubits;
        2) The Qiskrypt's Cluster State is initialised and configured, for 6 qubits;
        3) The Qiskrypt's Cluster State is prepared, without measuring it,
           on the Computational Basis;
        4) The Qiskrypt's Cluster State is prepared, without measuring it,
           on the Cluster State Basis;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        quantum_register_name = "qu_reg"
        """
        Set the name of the Qiskrypt's Quantum Register.
        """

        quantum_register_num_qubits = 6
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

        qiskrypt_quantum_circuit_cluster_state_6_qubits_111111_12 = \
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

        qiskrypt_quantum_pauli_x_transform_6_qubits_111111_12 = \
            QiskryptQuantumPauliXTransform("pauli_x_transform_6_qubits_12",
                                           qiskrypt_quantum_circuit_cluster_state_6_qubits_111111_12,
                                           ([0] * quantum_register_num_qubits),
                                           [*range(quantum_register_num_qubits)])
        """
        Create the Qiskrypt's Quantum Pauli-X Transform, for 1 Qiskrypt's Quantum Register and 6 qubits.
        """

        qiskrypt_quantum_pauli_x_transform_6_qubits_111111_12.apply_transform()
        """
        Apply the Quantum Pauli-X Transform to the Qiskrypt's Quantum Registers and qubits involved.
        """

        qiskrypt_quantum_circuit_cluster_state_6_qubits_111111_12 = \
            qiskrypt_quantum_pauli_x_transform_6_qubits_111111_12.get_qiskrypt_quantum_circuit()
        """
        Retrieve the Qiskrypt's Quantum Circuit from
        the previously created Qiskrypt's Quantum Pauli-X Transform, for 6 qubits.
        """

        qiskrypt_cluster_state_6_qubits_111111_12 = \
            QiskryptClusterState("cluster_state_6_qubits_12",
                                 qiskrypt_quantum_circuit_cluster_state_6_qubits_111111_12)
        """
        Create a Qiskrypt's Cluster State, for a generation of a Cluster State with 6 qubits.
        """

        qiskrypt_cluster_state_6_qubits_111111_12.configure([0, 0, 0, 0, 0, 0],
                                                            [0, 1, 2, 3, 4, 5])
        """
        Configure the Qiskrypt's Cluster State, regarding its IBM Qiskit's Quantum Register and qubits.
        """

        qiskrypt_cluster_state_6_qubits_111111_12 \
            .prepare_multipartite_entanglement_at_computational_basis(is_to_measure_at_computational_basis=False,
                                                                      qiskit_classical_registers_indexes=None,
                                                                      bits_vertices_indexes=None)
        """
        Prepare the Multipartite Quantum Entanglement,
        for the specified Qiskrypt's Cluster State, as a Quantum Entangled State,
        without measure it, on the Computational Basis.
        """

        qiskrypt_cluster_state_6_qubits_111111_12 \
            .prepare_multipartite_entanglement_at_cluster_state_basis(is_to_measure_at_cluster_state_basis=False,
                                                                      qiskit_classical_registers_indexes=None,
                                                                      bits_vertices_indexes=None)
        """
        Prepare the Multipartite Quantum Entanglement,
        for the specified Qiskrypt's Cluster State, as a Quantum Entangled State,
        without measure it, on the Cluster State Basis.
        """

        qiskit_state_vector_backend = Aer.get_backend("statevector_simulator")
        """
        Getting the Aer Simulator Backend for the State Vector Representation
        (i.e., the quantum_regime state represented as its state vector).
        """

        final_quantum_state_vector_state = \
            execute(qiskrypt_cluster_state_6_qubits_111111_12.qiskrypt_quantum_circuit.qiskit_quantum_circuit,
                    qiskit_state_vector_backend).result().get_statevector()
        """
        Execute the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit
        and store the resulted quantum_regime state represented in a final state vector.
        """

        num_possible_outcomes = (2 ** quantum_register_num_qubits)
        """
        Compute the number of possible outcomes (i.e., 2^(quantum_register_num_qubits)).
        """

        cluster_state_6_qubits_array_expected_amplitudes = \
            full((num_possible_outcomes,), (0. + 0.j))
        """
        Create and fill an array with the zeros for the expected values of
        the Qiskrypt's Cluster State, with 6 qubits.
        """

        cluster_state_6_qubits_array_expected_amplitudes[(num_possible_outcomes - 1)] = (1. + 0.j)
        """
        Fill the last position of the expected values of
        the Qiskrypt's Cluster State, with (1. + 0.j).
        """

        assert_allclose(final_quantum_state_vector_state,
                        cluster_state_6_qubits_array_expected_amplitudes,
                        rtol=1e-7, atol=1e-7)
        """
        Perform the Assertion of all close values in the values of the quantum_regime state,
        represented by its state vector describing the given qubits,
        after be prepared a Cluster State with the configuration,
        |C_6⟩ = |111111⟩, in Cluster State Basis.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)


if __name__ == "__main__":
    """
    The Main Method for the Unitary Test.
    """

    qiskrypt_cluster_state_test_cases = \
        TestLoader().loadTestsFromTestCase(QiskryptClusterStateTests)
    """
    Load the Test Cases from the Unitary Tests for the Qiskrypt's Cluster State.
    """

    qiskrypt_cluster_state_test_suite = \
        TestSuite([qiskrypt_cluster_state_test_cases])
    """
    Load the Test Suite with all the Test Cases for the Qiskrypt's Cluster State.
    """
