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

from src.circuit.registers.quantum.QiskryptQuantumRegister \
    import QiskryptQuantumRegister
"""
Import the Qiskrypt's Quantum Register.
"""

from src.circuit.QiskryptQuantumCircuit \
    import QiskryptQuantumCircuit
"""
Import the Qiskrypt's Quantum Circuit.
"""

from src.transforms.pauli.x.QiskryptQuantumPauliXTransform \
    import QiskryptQuantumPauliXTransform
"""
Import the Qiskrypt's Quantum Pauli-X Transform.
"""

from src.entanglements.multipartite.QiskryptWState \
    import QiskryptWState
"""
Import the Qiskrypt's W State.
"""


class QiskryptWStateTests(TestCase):
    """
    Object Class of the Unitary Tests for the Qiskrypt's W State.
    """

    def test_no_1_prepare_computational_basis_qiskrypt_w_state_3_qubits(self):
        """
        Test Case #1:

        - Initialise the Qiskrypt's W State and prepare it, as an Entangled Quantum State,
          in the Computational Basis.

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's W State is initialised and configured, for 3 qubits;
        2) The Qiskrypt's W State with the configuration,
           |W_3⟩ = 1/sqrt(3) x (|001⟩ + |010⟩ + |100⟩),
           is prepared, without measuring it, on the Computational Basis;

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

        qiskrypt_quantum_circuit_w_state_3_qubits_1 = \
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

        qiskrypt_w_state_3_qubits_1 = \
            QiskryptWState("w_state_3_qubits_1",
                            qiskrypt_quantum_circuit_w_state_3_qubits_1)
        """
        Create a Qiskrypt's W State, for a generation of a W State with 3 qubits,
        with the configuration, |W_3⟩ = 1/sqrt(3) x (|001⟩ + |010⟩ + |100⟩).
        """

        qiskrypt_w_state_3_qubits_1.configure([0, 0, 0],
                                              [0, 1, 2])
        """
        Configure the Qiskrypt's W State, regarding its IBM Qiskit's Quantum Registers and qubits.
        """

        qiskrypt_w_state_3_qubits_1 \
            .prepare_multipartite_entanglement_at_computational_basis(is_to_measure_at_computational_basis=False,
                                                                      qiskit_classical_registers_indexes=None,
                                                                      bits_indexes=None)
        """
        Prepare the Multipartite Quantum Entanglement,
        for the specified Qiskrypt's W State, as a Quantum Entangled State,
        without measure it, on the Computational Basis.
        """

        qiskit_state_vector_backend = Aer.get_backend("statevector_simulator")
        """
        Getting the Aer Simulator Backend for the State Vector Representation
        (i.e., the quantum state represented as its state vector).
        """

        final_quantum_state_vector_state = \
            execute(qiskrypt_w_state_3_qubits_1.qiskrypt_quantum_circuit.qiskit_quantum_circuit,
                    qiskit_state_vector_backend).result().get_statevector()
        """
        Execute the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit
        and store the resulted quantum state represented in a final state vector.
        """

        num_possible_outcomes = (2 ** quantum_register_num_qubits)
        """
        Compute the number of possible outcomes (i.e., 2^(quantum_register_num_qubits)).
        """

        w_state_3_qubits_array_expected_amplitudes = \
            full((num_possible_outcomes,), (0. + 0.j))
        """
        Create and fill an array with the zeros for the expected values of
        the Qiskrypt's W State, with 3 qubits.
        """

        for qubit_index in range(quantum_register_num_qubits):
            """
            For each index of the current qubit for
            the IBM Qiskit's Quantum Register defined previously.
            """

            current_index_expected_amplitude = (2 ** qubit_index)
            """
            Compute the index for the expected amplitude,
            regarding the index of the current qubit for
            the IBM Qiskit's Quantum Register defined previously.
            """

            w_state_3_qubits_array_expected_amplitudes[current_index_expected_amplitude] = \
                ((1. / sqrt(quantum_register_num_qubits)) * (1. + 0.j))
            """
            Fill the current computed position of the expected values of
            the Qiskrypt's W State, with ((1. / sqrt(3)) * (1. + 0.j)).
            """

        assert_allclose(final_quantum_state_vector_state,
                        w_state_3_qubits_array_expected_amplitudes,
                        rtol=1e-7, atol=1e-7)
        """
        Perform the Assertion of all close values in the values of the quantum state,
        represented by its state vector describing the given qubits,
        after be prepared a W State with the configuration,
        |W_3⟩ = (1. / sqrt(3)) x (|001⟩ + |010⟩ + |100⟩).
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)


if __name__ == "__main__":
    """
    The Main Method for the Unitary Test.
    """

    qiskrypt_w_state_test_cases = \
        TestLoader().loadTestsFromTestCase(QiskryptWStateTests)
    """
    Load the Test Cases from the Unitary Tests for the Qiskrypt's W State.
    """

    qiskrypt_w_state_test_suite = \
        TestSuite([qiskrypt_w_state_test_cases])
    """
    Load the Test Suite with all the Test Cases for the Qiskrypt's W State.
    """
