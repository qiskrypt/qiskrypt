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
Import the Square Root and N-Dimensional Full functions from Python's NumPy.
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

from src.circuit.QiskryptQuantumCircuit import QiskryptQuantumCircuit
"""
Import the Qiskrypt's Quantum Circuit.
"""

from src.true_random.transforms.QiskryptQuantumHadamardTransform \
    import QiskryptQuantumHadamardTransform
"""
Import the Qiskrypt's Quantum Hadamard Transform.
"""


class QiskryptQuantumHadamardTransformTests(TestCase):
    """
    Object Class of the Unitary Tests for the Qiskrypt's Quantum Hadamard Transform.
    """

    def test_no_1_qiskrypt_quantum_hadamard_transform_1_qubit(self):
        """
        Test Case #1:

        - Setup the Qiskrypt's Quantum Hadamard Transform, given a Qiskrypt's Quantum Circuit,
          and apply the Transform to the respective indexes of IBM Qiskit's Quantum Registers and qubits,
          for 1 qubit involved.

        Description of the Steps for the Unitary Test:
        1) The required arguments for the Qiskrypt's Quantum Hadamard Transform are passed to it,
           i.e., a custom name for it, the associated Qiskrypt's Quantum Circuit,
           and two lists of indexes of IBM Qiskit's Quantum Registers and qubits;
        2) The Hadamard Transform it is applied to the respective indexes of
           IBM Qiskit's Quantum Registers and qubits defined previously
           (i.e., 1 IBM Qiskit's Quantum Register and 1 qubit);

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        num_qubits = 1
        """
        Set the number of qubits for the Qiskrypt's Quantum Register.
        """

        qiskrypt_quantum_register_quantum_hadamard_transform_1_qubit = \
            QiskryptQuantumRegister("qu_reg_hadamard_transform_1", num_qubits)
        """
        Create a Qiskrypt's Quantum Register with 1 qubit.
        """

        qiskrypt_quantum_circuit_quantum_hadamard_transform_1_qubit = \
            QiskryptQuantumCircuit("qu_circ_hadamard_transform_1",
                                   qiskrypt_quantum_registers=[qiskrypt_quantum_register_quantum_hadamard_transform_1_qubit],
                                   qiskrypt_fully_quantum_registers=None,
                                   qiskrypt_semi_quantum_registers=None,
                                   qiskrypt_ancilla_quantum_registers=None,
                                   qiskrypt_ancilla_fully_quantum_registers=None,
                                   qiskrypt_ancilla_semi_quantum_registers=None,
                                   qiskrypt_classical_registers=None,
                                   global_phase=0, qiskit_quantum_circuit=None)
        """
        Create a Qiskrypt's Quantum Circuit with
        the previously created Qiskrypt's Quantum Register.
        """

        qiskrypt_quantum_hadamard_transform = \
            QiskryptQuantumHadamardTransform("hadamard_transform_1",
                                             qiskrypt_quantum_circuit_quantum_hadamard_transform_1_qubit,
                                             ([0] * num_qubits), [*range(num_qubits)])
        """
        Create the Qiskrypt's Quantum Hadamard Transform, for 1 Qiskrypt's Quantum Register and 1 qubit.
        """

        qiskrypt_quantum_hadamard_transform.apply_transform()
        """
        Apply the Quantum Hadamard Transform to the Qiskrypt's Quantum Registers and qubits involved.
        """

        qiskit_state_vector_backend = Aer.get_backend("statevector_simulator")
        """
        Getting the Aer Simulator Backend for the State Vector Representation
        (i.e., the quantum state represented as its state vector).
        """

        final_quantum_state_vector_state = \
            execute(qiskrypt_quantum_circuit_quantum_hadamard_transform_1_qubit.qiskit_quantum_circuit,
                    qiskit_state_vector_backend).result().get_statevector()
        """
        Execute the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit
        and store the resulted quantum state represented in a final state vector.
        """

        num_possible_outcomes = (2 ** num_qubits)
        """
        Compute the number of possible outcomes (i.e., 2^(num_qubits)).
        """

        quantum_hadamard_transform_1_qubit_array_expected_amplitudes = \
            full((num_possible_outcomes,),
                 (1 / sqrt(num_possible_outcomes)) * (1. + 0.j))
        """
        Create and fill an array with the expected values/amplitudes for
        the Qiskrypt's Quantum Hadamard Transform.
        """

        assert_allclose(final_quantum_state_vector_state,
                        quantum_hadamard_transform_1_qubit_array_expected_amplitudes,
                        rtol=1e-7, atol=1e-7)
        """
        Perform the Assertion of all close values in the values of the quantum state,
        represented by its state vector describing the given qubit,
        after be applied the Qiskrypt's Quantum Hadamard Transform.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_2_qiskrypt_quantum_hadamard_transform_2_qubits(self):
        """
        Test Case #2:

        - Setup the Qiskrypt's Quantum Hadamard Transform, given a Qiskrypt's Quantum Circuit,
          and apply the Transform to the respective indexes of IBM Qiskit's Quantum Registers and qubits,
          for 2 qubits involved.

        Description of the Steps for the Unitary Test:
        1) The required arguments for the Qiskrypt's Quantum Hadamard Transform are passed to it,
           i.e., a custom name for it, the associated Qiskrypt's Quantum Circuit,
           and two lists of indexes of IBM Qiskit's Quantum Registers and qubits;
        2) The Hadamard Transform it is applied to the respective indexes of
           IBM Qiskit's Quantum Registers and qubits defined previously
           (i.e., 2 IBM Qiskit's Quantum Registers and 2 qubits);

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        num_qubits = 2
        """
        Set the number of qubits for the Qiskrypt's Quantum Register.
        """

        qiskrypt_quantum_register_quantum_hadamard_transform_2_qubits = \
            QiskryptQuantumRegister("qu_reg_hadamard_transform_2", num_qubits)
        """
        Create a Qiskrypt's Quantum Register with 2 qubits.
        """

        qiskrypt_quantum_circuit_quantum_hadamard_transform_2_qubits = \
            QiskryptQuantumCircuit("qu_circ_hadamard_transform_2",
                                   qiskrypt_quantum_registers=[qiskrypt_quantum_register_quantum_hadamard_transform_2_qubits],
                                   qiskrypt_fully_quantum_registers=None,
                                   qiskrypt_semi_quantum_registers=None,
                                   qiskrypt_ancilla_quantum_registers=None,
                                   qiskrypt_ancilla_fully_quantum_registers=None,
                                   qiskrypt_ancilla_semi_quantum_registers=None,
                                   qiskrypt_classical_registers=None,
                                   global_phase=0, qiskit_quantum_circuit=None)
        """
        Create a Qiskrypt's Quantum Circuit with
        the previously created Qiskrypt's Quantum Register.
        """

        qiskrypt_quantum_hadamard_transform = \
            QiskryptQuantumHadamardTransform("hadamard_transform_2",
                                             qiskrypt_quantum_circuit_quantum_hadamard_transform_2_qubits,
                                             ([0] * num_qubits), [*range(num_qubits)])
        """
        Create the Qiskrypt's Quantum Hadamard Transform, for 2 Qiskrypt's Quantum Registers and 2 qubits.
        """

        qiskrypt_quantum_hadamard_transform.apply_transform()
        """
        Apply the Quantum Hadamard Transform to the Qiskrypt's Quantum Registers and qubits involved.
        """

        qiskit_state_vector_backend = Aer.get_backend("statevector_simulator")
        """
        Getting the Aer Simulator Backend for the State Vector Representation
        (i.e., the quantum state represented as its state vector).
        """

        final_quantum_state_vector_state = \
            execute(qiskrypt_quantum_circuit_quantum_hadamard_transform_2_qubits.qiskit_quantum_circuit,
                    qiskit_state_vector_backend).result().get_statevector()
        """
        Execute the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit
        and store the resulted quantum state represented in a final state vector.
        """

        num_possible_outcomes = (2 ** num_qubits)
        """
        Compute the number of possible outcomes (i.e., 2^(num_qubits)).
        """

        quantum_hadamard_transform_2_qubits_array_expected_amplitudes = \
            full((num_possible_outcomes,),
                 (1 / sqrt(num_possible_outcomes)) * (1. + 0.j))
        """
        Create and fill an array with the expected values/amplitudes for
        the Qiskrypt's Quantum Hadamard Transform.
        """

        assert_allclose(final_quantum_state_vector_state,
                        quantum_hadamard_transform_2_qubits_array_expected_amplitudes,
                        rtol=1e-7, atol=1e-7)
        """
        Perform the Assertion of all close values in the values of the quantum state,
        represented by its state vector describing the given qubit,
        after be applied the Qiskrypt's Quantum Hadamard Transform.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_3_qiskrypt_quantum_hadamard_transform_4_qubits(self):
        """
        Test Case #3:

        - Setup the Qiskrypt's Quantum Hadamard Transform, given a Qiskrypt's Quantum Circuit,
          and apply the Transform to the respective indexes of IBM Qiskit's Quantum Registers and qubits,
          for 4 qubits involved.

        Description of the Steps for the Unitary Test:
        1) The required arguments for the Qiskrypt's Quantum Hadamard Transform are passed to it,
           i.e., a custom name for it, the associated Qiskrypt's Quantum Circuit,
           and two lists of indexes of IBM Qiskit's Quantum Registers and qubits;
        2) The Hadamard Transform it is applied to the respective indexes of
           IBM Qiskit's Quantum Registers and qubits defined previously
           (i.e., 4 IBM Qiskit's Quantum Registers and 4 qubits);

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        num_qubits = 4
        """
        Set the number of qubits for the Qiskrypt's Quantum Register.
        """

        qiskrypt_quantum_register_quantum_hadamard_transform_4_qubits = \
            QiskryptQuantumRegister("qu_reg_hadamard_transform_3", num_qubits)
        """
        Create a Qiskrypt's Quantum Register with 4 qubits.
        """

        qiskrypt_quantum_circuit_quantum_hadamard_transform_4_qubits = \
            QiskryptQuantumCircuit("qu_circ_hadamard_transform_3",
                                   qiskrypt_quantum_registers=[qiskrypt_quantum_register_quantum_hadamard_transform_4_qubits],
                                   qiskrypt_fully_quantum_registers=None,
                                   qiskrypt_semi_quantum_registers=None,
                                   qiskrypt_ancilla_quantum_registers=None,
                                   qiskrypt_ancilla_fully_quantum_registers=None,
                                   qiskrypt_ancilla_semi_quantum_registers=None,
                                   qiskrypt_classical_registers=None,
                                   global_phase=0, qiskit_quantum_circuit=None)
        """
        Create a Qiskrypt's Quantum Circuit with
        the previously created Qiskrypt's Quantum Register.
        """

        qiskrypt_quantum_hadamard_transform = \
            QiskryptQuantumHadamardTransform("hadamard_transform_3",
                                             qiskrypt_quantum_circuit_quantum_hadamard_transform_4_qubits,
                                             ([0] * num_qubits), [*range(num_qubits)])
        """
        Create the Qiskrypt's Quantum Hadamard Transform, for 1 Qiskrypt's Quantum Register and 4 qubits.
        """

        qiskrypt_quantum_hadamard_transform.apply_transform()
        """
        Apply the Quantum Hadamard Transform to the Qiskrypt's Quantum Registers and qubits involved.
        """

        qiskit_state_vector_backend = Aer.get_backend("statevector_simulator")
        """
        Getting the Aer Simulator Backend for the State Vector Representation
        (i.e., the quantum state represented as its state vector).
        """

        final_quantum_state_vector_state = \
            execute(qiskrypt_quantum_circuit_quantum_hadamard_transform_4_qubits.qiskit_quantum_circuit,
                    qiskit_state_vector_backend).result().get_statevector()
        """
        Execute the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit
        and store the resulted quantum state represented in a final state vector.
        """

        num_possible_outcomes = (2 ** num_qubits)
        """
        Compute the number of possible outcomes (i.e., 2^(num_qubits)).
        """

        quantum_hadamard_transform_4_qubits_array_expected_amplitudes = \
            full((num_possible_outcomes,),
                 (1 / sqrt(num_possible_outcomes)) * (1. + 0.j))
        """
        Create and fill an array with the expected values/amplitudes for
        the Qiskrypt's Quantum Hadamard Transform.
        """

        assert_allclose(final_quantum_state_vector_state,
                        quantum_hadamard_transform_4_qubits_array_expected_amplitudes,
                        rtol=1e-7, atol=1e-7)
        """
        Perform the Assertion of all close values in the values of the quantum state,
        represented by its state vector describing the given qubit,
        after be applied the Qiskrypt's Quantum Hadamard Transform.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_4_qiskrypt_quantum_hadamard_transform_8_qubits(self):
        """
        Test Case #4:

        - Setup the Qiskrypt's Quantum Hadamard Transform, given a Qiskrypt's Quantum Circuit,
          and apply the Transform to the respective indexes of IBM Qiskit's Quantum Registers and qubits,
          for 8 qubits involved.

        Description of the Steps for the Unitary Test:
        1) The required arguments for the Qiskrypt's Quantum Hadamard Transform are passed to it,
           i.e., a custom name for it, the associated Qiskrypt's Quantum Circuit,
           and two lists of indexes of IBM Qiskit's Quantum Registers and qubits;
        2) The Hadamard Transform it is applied to the respective indexes of
           IBM Qiskit's Quantum Registers and qubits defined previously
           (i.e., 8 IBM Qiskit's Quantum Registers and 8 qubits);

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        num_qubits = 8
        """
        Set the number of qubits for the Qiskrypt's Quantum Register.
        """

        qiskrypt_quantum_register_quantum_hadamard_transform_8_qubits = \
            QiskryptQuantumRegister("qu_reg_hadamard_transform_4", num_qubits)
        """
        Create a Qiskrypt's Quantum Register with 8 qubits.
        """

        qiskrypt_quantum_circuit_quantum_hadamard_transform_8_qubits = \
            QiskryptQuantumCircuit("qu_circ_hadamard_transform_4",
                                   qiskrypt_quantum_registers=[qiskrypt_quantum_register_quantum_hadamard_transform_8_qubits],
                                   qiskrypt_fully_quantum_registers=None,
                                   qiskrypt_semi_quantum_registers=None,
                                   qiskrypt_ancilla_quantum_registers=None,
                                   qiskrypt_ancilla_fully_quantum_registers=None,
                                   qiskrypt_ancilla_semi_quantum_registers=None,
                                   qiskrypt_classical_registers=None,
                                   global_phase=0, qiskit_quantum_circuit=None)
        """
        Create a Qiskrypt's Quantum Circuit with
        the previously created Qiskrypt's Quantum Register.
        """

        qiskrypt_quantum_hadamard_transform = \
            QiskryptQuantumHadamardTransform("hadamard_transform_4",
                                             qiskrypt_quantum_circuit_quantum_hadamard_transform_8_qubits,
                                             ([0] * num_qubits), [*range(num_qubits)])
        """
        Create the Qiskrypt's Quantum Hadamard Transform, for 1 Qiskrypt's Quantum Register and 8 qubits.
        """

        qiskrypt_quantum_hadamard_transform.apply_transform()
        """
        Apply the Quantum Hadamard Transform to the Qiskrypt's Quantum Registers and qubits involved.
        """

        qiskit_state_vector_backend = Aer.get_backend("statevector_simulator")
        """
        Getting the Aer Simulator Backend for the State Vector Representation
        (i.e., the quantum state represented as its state vector).
        """

        final_quantum_state_vector_state = \
            execute(qiskrypt_quantum_circuit_quantum_hadamard_transform_8_qubits.qiskit_quantum_circuit,
                    qiskit_state_vector_backend).result().get_statevector()
        """
        Execute the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit
        and store the resulted quantum state represented in a final state vector.
        """

        num_possible_outcomes = (2 ** num_qubits)
        """
        Compute the number of possible outcomes (i.e., 2^(num_qubits)).
        """

        quantum_hadamard_transform_8_qubits_array_expected_amplitudes = \
            full((num_possible_outcomes,),
                 (1 / sqrt(num_possible_outcomes)) * (1. + 0.j))
        """
        Create and fill an array with the expected values/amplitudes for
        the Qiskrypt's Quantum Hadamard Transform.
        """

        assert_allclose(final_quantum_state_vector_state,
                        quantum_hadamard_transform_8_qubits_array_expected_amplitudes,
                        rtol=1e-7, atol=1e-7)
        """
        Perform the Assertion of all close values in the values of the quantum state,
        represented by its state vector describing the given qubit,
        after be applied the Qiskrypt's Quantum Hadamard Transform.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_5_qiskrypt_quantum_hadamard_transform_16_qubits(self):
        """
        Test Case #5:

        - Setup the Qiskrypt's Quantum Hadamard Transform, given a Qiskrypt's Quantum Circuit,
          and apply the Transform to the respective indexes of IBM Qiskit's Quantum Registers and qubits,
          for 16 qubits involved.

        Description of the Steps for the Unitary Test:
        1) The required arguments for the Qiskrypt's Quantum Hadamard Transform are passed to it,
           i.e., a custom name for it, the associated Qiskrypt's Quantum Circuit,
           and two lists of indexes of IBM Qiskit's Quantum Registers and qubits;
        2) The Hadamard Transform it is applied to the respective indexes of
           IBM Qiskit's Quantum Registers and qubits defined previously
           (i.e., 16 IBM Qiskit's Quantum Registers and 16 qubits);

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        num_qubits = 16
        """
        Set the number of qubits for the Qiskrypt's Quantum Register.
        """

        qiskrypt_quantum_register_quantum_hadamard_transform_16_qubits = \
            QiskryptQuantumRegister("qu_reg_hadamard_transform_5", num_qubits)
        """
        Create a Qiskrypt's Quantum Register with 16 qubits.
        """

        qiskrypt_quantum_circuit_quantum_hadamard_transform_16_qubits = \
            QiskryptQuantumCircuit("qu_circ_hadamard_transform_5",
                                   qiskrypt_quantum_registers=[qiskrypt_quantum_register_quantum_hadamard_transform_16_qubits],
                                   qiskrypt_fully_quantum_registers=None,
                                   qiskrypt_semi_quantum_registers=None,
                                   qiskrypt_ancilla_quantum_registers=None,
                                   qiskrypt_ancilla_fully_quantum_registers=None,
                                   qiskrypt_ancilla_semi_quantum_registers=None,
                                   qiskrypt_classical_registers=None,
                                   global_phase=0, qiskit_quantum_circuit=None)
        """
        Create a Qiskrypt's Quantum Circuit with
        the previously created Qiskrypt's Quantum Register.
        """

        qiskrypt_quantum_hadamard_transform = \
            QiskryptQuantumHadamardTransform("hadamard_transform_5",
                                             qiskrypt_quantum_circuit_quantum_hadamard_transform_16_qubits,
                                             ([0] * num_qubits), [*range(num_qubits)])
        """
        Create the Qiskrypt's Quantum Hadamard Transform, for 1 Qiskrypt's Quantum Register and 16 qubits.
        """

        qiskrypt_quantum_hadamard_transform.apply_transform()
        """
        Apply the Quantum Hadamard Transform to the Qiskrypt's Quantum Registers and qubits involved.
        """

        qiskit_state_vector_backend = Aer.get_backend("statevector_simulator")
        """
        Getting the Aer Simulator Backend for the State Vector Representation
        (i.e., the quantum state represented as its state vector).
        """

        final_quantum_state_vector_state = \
            execute(qiskrypt_quantum_circuit_quantum_hadamard_transform_16_qubits.qiskit_quantum_circuit,
                    qiskit_state_vector_backend).result().get_statevector()
        """
        Execute the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit
        and store the resulted quantum state represented in a final state vector.
        """

        num_possible_outcomes = (2 ** num_qubits)
        """
        Compute the number of possible outcomes (i.e., 2^(num_qubits)).
        """

        quantum_hadamard_transform_16_qubits_array_expected_amplitudes = \
            full((num_possible_outcomes,),
                 (1 / sqrt(num_possible_outcomes)) * (1. + 0.j))
        """
        Create and fill an array with the expected values/amplitudes for
        the Qiskrypt's Quantum Hadamard Transform.
        """

        assert_allclose(final_quantum_state_vector_state,
                        quantum_hadamard_transform_16_qubits_array_expected_amplitudes,
                        rtol=1e-7, atol=1e-7)
        """
        Perform the Assertion of all close values in the values of the quantum state,
        represented by its state vector describing the given qubit,
        after be applied the Qiskrypt's Quantum Hadamard Transform.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_6_qiskrypt_quantum_hadamard_transform_20_qubits(self):
        """
        Test Case #6:

        - Setup the Qiskrypt's Quantum Hadamard Transform, given a Qiskrypt's Quantum Circuit,
          and apply the Transform to the respective indexes of IBM Qiskit's Quantum Registers and qubits,
          for 20 qubits involved.

        Description of the Steps for the Unitary Test:
        1) The required arguments for the Qiskrypt's Quantum Hadamard Transform are passed to it,
           i.e., a custom name for it, the associated Qiskrypt's Quantum Circuit,
           and two lists of indexes of IBM Qiskit's Quantum Registers and qubits;
        2) The Hadamard Transform it is applied to the respective indexes of
           IBM Qiskit's Quantum Registers and qubits defined previously
           (i.e., 20 IBM Qiskit's Quantum Registers and 20 qubits);

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        num_qubits = 20
        """
        Set the number of qubits for the Qiskrypt's Quantum Register.
        """

        qiskrypt_quantum_register_quantum_hadamard_transform_20_qubits = \
            QiskryptQuantumRegister("qu_reg_hadamard_transform_6", num_qubits)
        """
        Create a Qiskrypt's Quantum Register with 20 qubits.
        """

        qiskrypt_quantum_circuit_quantum_hadamard_transform_20_qubits = \
            QiskryptQuantumCircuit("qu_circ_hadamard_transform_6",
                                   qiskrypt_quantum_registers=[qiskrypt_quantum_register_quantum_hadamard_transform_20_qubits],
                                   qiskrypt_fully_quantum_registers=None,
                                   qiskrypt_semi_quantum_registers=None,
                                   qiskrypt_ancilla_quantum_registers=None,
                                   qiskrypt_ancilla_fully_quantum_registers=None,
                                   qiskrypt_ancilla_semi_quantum_registers=None,
                                   qiskrypt_classical_registers=None,
                                   global_phase=0, qiskit_quantum_circuit=None)
        """
        Create a Qiskrypt's Quantum Circuit with
        the previously created Qiskrypt's Quantum Register.
        """

        qiskrypt_quantum_hadamard_transform = \
            QiskryptQuantumHadamardTransform("hadamard_transform_4",
                                             qiskrypt_quantum_circuit_quantum_hadamard_transform_20_qubits,
                                             ([0] * num_qubits), [*range(num_qubits)])
        """
        Create the Qiskrypt's Quantum Hadamard Transform, for 1 Qiskrypt's Quantum Register and 20 qubits.
        """

        qiskrypt_quantum_hadamard_transform.apply_transform()
        """
        Apply the Quantum Hadamard Transform to the Qiskrypt's Quantum Registers and qubits involved.
        """

        qiskit_state_vector_backend = Aer.get_backend("statevector_simulator")
        """
        Getting the Aer Simulator Backend for the State Vector Representation
        (i.e., the quantum state represented as its state vector).
        """

        final_quantum_state_vector_state = \
            execute(qiskrypt_quantum_circuit_quantum_hadamard_transform_20_qubits.qiskit_quantum_circuit,
                    qiskit_state_vector_backend).result().get_statevector()
        """
        Execute the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit
        and store the resulted quantum state represented in a final state vector.
        """

        num_possible_outcomes = (2 ** num_qubits)
        """
        Compute the number of possible outcomes (i.e., 2^(num_qubits)).
        """

        quantum_hadamard_transform_20_qubits_array_expected_amplitudes = \
            full((num_possible_outcomes,),
                 (1 / sqrt(num_possible_outcomes)) * (1. + 0.j))
        """
        Create and fill an array with the expected values/amplitudes for
        the Qiskrypt's Quantum Hadamard Transform.
        """

        assert_allclose(final_quantum_state_vector_state,
                        quantum_hadamard_transform_20_qubits_array_expected_amplitudes,
                        rtol=1e-7, atol=1e-7)
        """
        Perform the Assertion of all close values in the values of the quantum state,
        represented by its state vector describing the given qubit,
        after be applied the Qiskrypt's Quantum Hadamard Transform.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)


if __name__ == "__main__":
    """
    The Main Method for the Unitary Test.
    """

    qiskrypt_quantum_hadamard_transform_test_cases = \
        TestLoader().loadTestsFromTestCase(QiskryptQuantumHadamardTransformTests)
    """
    Load the Test Cases from the Unitary Tests for the Qiskrypt's Quantum Hadamard Transform.
    """

    qiskrypt_quantum_hadamard_transform_test_suite = \
        TestSuite([qiskrypt_quantum_hadamard_transform_test_cases])
    """
    Load the Test Suite with all the Test Cases for the Qiskrypt's Quantum Hadamard Transform.
    """
