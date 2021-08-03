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

from src.entanglements.bipartite.QiskryptBellState \
    import QiskryptBellState
"""
Import the Qiskrypt's Bell State.
"""


"""
Import required Constants and Enumerations.
"""

from src.entanglements.QiskryptQuantumEntanglement \
    import POSSIBLE_CONFIGURATIONS_BELL_STATES
"""
Import the available configurations for Bell States for
the Qiskrypt's Quantum Entanglement. 
"""


class QiskryptBellStateTests(TestCase):
    """
    Object Class of the Unitary Tests for the Qiskrypt's Bell State.
    """

    def test_no_1_prepare_qiskrypt_epr_pair_bell_state_phi_plus(self):
        """
        Test Case #1:

        - Initialise the Qiskrypt's Bell State and prepare it, as an Entangled Quantum State.

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Bell State is initialised and configured;
        2) The Qiskrypt's Bell State is prepared, without measuring it,
           on the Computational Basis;

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

        qiskrypt_quantum_circuit = \
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

        qiskrypt_bell_state = \
            QiskryptBellState("bell_state_epr_pair_1", qiskrypt_quantum_circuit, POSSIBLE_CONFIGURATIONS_BELL_STATES[0])
        """
        Create a Qiskrypt's Bell State, for a generation of a Bell's State with the configuration,
        |ϕ^+⟩ = 1/sqrt(2) x (|00⟩ + |11⟩) (also known as, EPR Pair).
        """

        qiskrypt_bell_state.configure(0, 0, 0, 1)
        """
        Configure the Qiskrypt's Bell State, regarding its control IBM Qiskit's Quantum Register
        and control qubit, as well, its target IBM Qiskit's Quantum Register and target qubit.
        """

        qiskrypt_bell_state.prepare_bipartite_entanglement(is_to_measure_at_computational_basis=False,
                                                           qiskit_classical_register_control_index=None,
                                                           qiskit_classical_register_target_index=None,
                                                           control_bit_index=None, target_bit_index=None)
        """
        Prepare the Bipartite Quantum Entanglement,
        for the specified Qiskrypt's Bell State, as a quantum entangled state,
        without measure it, on the Computational Basis.
        """

        qiskit_state_vector_backend = Aer.get_backend("statevector_simulator")
        """
        Getting the Aer Simulator Backend for the State Vector Representation
        (i.e., the quantum state represented as its state vector).
        """

        final_quantum_state_vector_state = \
            execute(qiskrypt_bell_state.qiskrypt_quantum_circuit.qiskit_quantum_circuit,
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
        represented by its state vector describing the given qubit,
        after be prepared a Bell's State with the configuration,
        |ϕ^+⟩ = 1/sqrt(2) x (|00⟩ + |11⟩) (also known as, EPR Pair).
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)
