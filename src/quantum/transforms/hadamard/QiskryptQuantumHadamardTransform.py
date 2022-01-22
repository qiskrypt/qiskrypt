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

from src.quantum.common.utils.QiskryptLibraryParameters import QISKIT_QASM_SIMULATOR_MAX_NUM_QUBITS
"""
Import the maximum number of Qubits for
the QASM (Quantum Assembly) Simulator of the IBM's Qiskit.
"""

from src.quantum.circuit.QiskryptQuantumCircuit import QiskryptQuantumCircuit
"""
Import the Qiskrypt's Quantum Circuit.
"""

from src.quantum.circuit.exception.QiskryptQuantumCircuitException \
    import QiskryptQuantumCircuitInvalidOrNoneGivenError
"""
Import the Invalid or None Quantum Circuit Given Error for
the Qiskrypt's Quantum Circuit.
"""

from src.quantum.circuit.exception.QiskryptQuantumCircuitException \
    import QiskryptQuantumCircuitNotAnInstanceOfError
"""
Import the Not An Instance Of Quantum Circuit Error for
the Qiskrypt's Quantum Circuit.
"""

from src.quantum.transforms.hadamard.exception.QiskryptQuantumHadamardTransformException \
    import QiskryptQuantumHadamardTransformNumberOfQubitsAndNumberOfQuantumRegistersNotEqualError
"""
Import the Number Of Qubits And Number Of Quantum Registers Not Equal Error for
the Qiskrypt's Quantum Hadamard Transform.
"""

from src.quantum.transforms.hadamard.exception.QiskryptQuantumHadamardTransformException \
    import QiskryptQuantumHadamardTransformNumberOfQubitsGreaterThanMaximumForQASMError
"""
Import the Number of Qubits Greater Than Maximum for QASM (Quantum Assembly) Error for
the Qiskrypt's Quantum Hadamard Transform.
"""


class QiskryptQuantumHadamardTransform:
    """
    Object class for the Qiskrypt's Quantum Hadamard Transform.
    """

    def __init__(self, name: str, qiskrypt_quantum_circuit: QiskryptQuantumCircuit,
                 qiskit_quantum_registers_indexes: list, qubits_indexes: list):
        """
        Constructor of the Qiskrypt's Quantum Hadamard Transform.

        :param name: the name for the Qiskrypt's Quantum Hadamard Transform.
        :param qiskrypt_quantum_circuit: the Qiskrypt's Quantum Circuit of the Qiskrypt's Quantum Hadamard Transform.
        :param qiskit_quantum_registers_indexes: the indexes of the IBM Qiskit's Quantum Registers,
                                                 involved in the Qiskrypt's Quantum Hadamard Transform.
        :param qubits_indexes: the indexes of the qubits in the IBM Qiskit's Quantum Registers,
                               to which will be applied the Hadamard Gates/Operations,
                               involved in the Qiskrypt's Quantum Hadamard Transform.
        """

        if qiskrypt_quantum_circuit is not None:
            """
            If some Qiskrypt's Quantum Circuit is given.
            """

            if isinstance(qiskrypt_quantum_circuit, QiskryptQuantumCircuit):
                """
                If the Qiskrypt's Quantum Circuit given as argument,
                is really a Qiskrypt's Quantum Circuit.
                """

                num_qiskit_quantum_registers = len(qiskit_quantum_registers_indexes)
                """
                Retrieve the number of the IBM Qiskit's Quantum Registers
                to which will be applied the Quantum Hadamard Transform.
                """

                num_qubits = len(qiskit_quantum_registers_indexes)
                """
                Retrieve the number of the qubits
                to which will be applied the Quantum Hadamard Transform.
                """

                if num_qiskit_quantum_registers == num_qubits:
                    """
                    If the number of the IBM Qiskit's Quantum Registers
                    and the number of the qubits is the same.
                    """

                    if num_qubits <= QISKIT_QASM_SIMULATOR_MAX_NUM_QUBITS:
                        """
                        If the number of qubits given for the Qiskrypt's Quantum Hadamard Transform
                        is lower or equal to the maximum number of Qubits for
                        the QASM (Quantum Assembly) Simulator of the IBM's Qiskit.
                        """

                        for qiskit_quantum_register_index, qubit_index \
                            in zip(qiskit_quantum_registers_indexes, qubits_indexes):
                            """
                            For each pair of indexes of IBM Qiskit's Quantum Registers and qubits. 
                            """

                            qiskrypt_quantum_circuit.check_if_is_possible_to_apply_operation(qiskit_quantum_register_index, qubit_index,
                                                                                             is_operation_only_supported_for_fully_quantum_registers=True)
                            """
                            Check if it is possible to apply a specific Operation,
                            regarding the current IBM Qiskit's Quantum Register index and the current qubit index.
                            """

                        self.name = name
                        """
                        Set the name for the Qiskrypt's Quantum Hadamard Transform.
                        """

                        self.qiskrypt_quantum_circuit = qiskrypt_quantum_circuit
                        """
                        Set the Qiskrypt's Quantum Circuit of
                        the Qiskrypt's Quantum Hadamard Transform.
                        """

                        self.qiskit_quantum_registers_indexes = \
                            qiskit_quantum_registers_indexes
                        """
                        Set the indexes of the IBM Qiskit's Quantum Registers,
                        involved in the Qiskrypt's Quantum Hadamard Transform.
                        """

                        self.qubits_indexes = qubits_indexes
                        """
                        Set the indexes of the qubits in the IBM Qiskit's Quantum Registers,
                        to which will be applied the Hadamard Gates/Operations,
                        involved in the Qiskrypt's Quantum Hadamard Transform.
                        """

                    else:
                        """
                        If the number of qubits given for the Qiskrypt's Quantum Hadamard Transform
                        is greater than the maximum number of Qubits for
                        the QASM (Quantum Assembly) Simulator of the IBM's Qiskit.
                        """

                        self.raise_number_of_qubits_greater_than_maximum_for_qasm_error()
                        """
                        Return/Raise a Number of Qubits Greater Than Maximum for QASM (Quantum Assembly) Error for
                        the Qiskrypt's Quantum Hadamard Transform.
                        """

                else:
                    """
                    If the number of the IBM Qiskit's Quantum Registers
                    and the number of the qubits is not the same.
                    """

                    self.raise_number_of_qubits_and_number_of_quantum_registers_not_equal_error()
                    """
                    Return/Raise a Number Of Qubits And Number Of Quantum Registers Not Equal Error for
                    the Qiskrypt's Quantum Hadamard Transform.
                    """

            else:
                """
                If the Qiskrypt's Quantum Circuit given as argument,
                is really a Qiskrypt's Quantum Circuit.
                """

                self.raise_not_an_instance_of_quantum_circuit_error()
                """
                Return/Raise a Not An Instance Of Quantum Circuit Error for
                the Qiskrypt's Quantum Hadamard Transform.
                """

        else:
            """
            If none Qiskrypt's Quantum Circuit is given.
            """

            self.raise_invalid_or_none_quantum_circuit_given_error()
            """
            Return/Raise an Invalid or None Quantum Circuit Given Error for
            the Qiskrypt's Quantum Hadamard Transform.
            """

    def get_name(self) -> str:
        """
        Return the name for the Qiskrypt's Quantum Hadamard Transform.

        :return self.name: the name for the Qiskrypt's Quantum Hadamard Transform.
        """

        """
        Return the name for the Qiskrypt's Quantum Hadamard Transform.
        """
        return self.name

    def get_qiskrypt_quantum_circuit(self) -> QiskryptQuantumCircuit:
        """
        Return the Qiskrypt's Quantum Circuit of the Qiskrypt's Quantum Hadamard Transform.

        :return self.qiskrypt_quantum_circuit: the Qiskrypt's Quantum Circuit of
                                               the Qiskrypt's Quantum Hadamard Transform.
        """

        """
        Return the Qiskrypt's Quantum Circuit of the Qiskrypt's Quantum Hadamard Transform.
        """
        return self.qiskrypt_quantum_circuit

    def get_qiskit_quantum_registers_indexes(self) -> list:
        """
        Return the indexes of the IBM Qiskit's Quantum Registers,
        involved in the Qiskrypt's Quantum Hadamard Transform.

        :return self.qiskit_quantum_registers_indexes: the indexes of the IBM Qiskit's Quantum Registers,
                                                       involved in the Qiskrypt's Quantum Hadamard Transform.
        """

        """
        Return the indexes of the IBM Qiskit's Quantum Registers,
        involved in the Qiskrypt's Quantum Hadamard Transform.
        """
        return self.qiskit_quantum_registers_indexes

    def get_qubits_indexes(self) -> list:
        """
        Return the indexes of the qubits in the IBM Qiskit's Quantum Registers,
        to which will be applied the Hadamard Gates/Operations,
        involved in the Qiskrypt's Quantum Hadamard Transform.

        :return self.qubits_indexes: the indexes of the qubits in the IBM Qiskit's Quantum Registers,
                                     to which will be applied the Hadamard Gates/Operations,
                                     involved in the Qiskrypt's Quantum Hadamard Transform.
        """

        """
        Return the indexes of the qubits in the IBM Qiskit's Quantum Registers,
        to which will be applied the Hadamard Gates/Operations,
        involved in the Qiskrypt's Quantum Hadamard Transform.
        """
        return self.qubits_indexes

    def apply_transform(self) -> None:
        """
        Apply the Qiskrypt's Quantum Hadamard Transform,
        to the specified indexes of qubits in the also specified indexes of
        IBM Qiskit's Quantum Registers.
        """

        for qiskit_quantum_register_index, qubit_index \
            in zip(self.qiskit_quantum_registers_indexes, self.qubits_indexes):
            """
            For each pair of indexes of IBM Qiskit's Quantum Registers and qubits.
            """

            is_possible_to_apply_operation = self.qiskrypt_quantum_circuit\
                .check_if_is_possible_to_apply_operation(qiskit_quantum_register_index,
                                                         qubit_index, True)
            """
            Check if it is possible to apply a specific Operation,
            regarding the current IBM Qiskit's Quantum Register index and the current qubit index.
            """

            if is_possible_to_apply_operation:
                """
                If is really possible to apply a specific Operation,
                regarding the current IBM Qiskit's Quantum Register index and the current qubit index.
                """

                self.qiskrypt_quantum_circuit.apply_hadamard(qiskit_quantum_register_index, qubit_index)
                """
                Apply the Hadamard Gate/Operation to
                the current pair of indexes of IBM Qiskit's Quantum Registers and qubits.
                """

    @staticmethod
    def raise_invalid_or_none_quantum_circuit_given_error() -> None:
        """
        Return/Raise an Invalid or None Quantum Circuit Given Error for the Qiskrypt's Quantum Hadamard Transform.

        :raise invalid_or_none_quantum_circuit_given_error: an Invalid or None Quantum Circuit Given Error for
                                                            the Qiskrypt's Quantum Hadamard Transform.
        """

        invalid_or_none_quantum_circuit_given_error = \
            QiskryptQuantumCircuitInvalidOrNoneGivenError(primitive="Qiskrypt's Quantum Hadamard Transform")
        """
        Retrieve the Invalid or None Quantum Circuit Given Error for the Qiskrypt's Quantum Hadamard Transform.
        """

        """
        Raise the Invalid or None Quantum Circuit Given Error for the Qiskrypt's Quantum Hadamard Transform.
        """
        raise invalid_or_none_quantum_circuit_given_error

    @staticmethod
    def raise_not_an_instance_of_quantum_circuit_error() -> None:
        """
        Return/Raise a Not An Instance Of Quantum Circuit Error for the Qiskrypt's Quantum Hadamard Transform.

        :raise not_an_instance_of_quantum_circuit_error: a Not An Instance Of Quantum Circuit Error for
                                                         the Qiskrypt's Quantum Hadamard Transform.
        """

        not_an_instance_of_quantum_circuit_error = \
            QiskryptQuantumCircuitNotAnInstanceOfError(primitive="Qiskrypt's Quantum Hadamard Transform")
        """
        Retrieve the Not An Instance Of Quantum Circuit Error for the Qiskrypt's Quantum Coin Tossing.
        """

        """
        Raise the Not An Instance Of Quantum Circuit Error for the Qiskrypt's Quantum Coin Tossing.
        """
        raise not_an_instance_of_quantum_circuit_error

    @staticmethod
    def raise_number_of_qubits_and_number_of_quantum_registers_not_equal_error() -> None:
        """
        Return/Raise a Number Of Qubits And Number Of Quantum Registers Not Equal Error for
        the Qiskrypt's Quantum Hadamard Transform.

        :raise number_of_qubits_and_number_of_quantum_registers_not_equal_error: a Number Of Qubits And Number Of Quantum Registers Not Equal Error for
                                                                                 the Qiskrypt's Quantum Hadamard Transform.
        """

        number_of_qubits_and_number_of_quantum_registers_not_equal_error = \
            QiskryptQuantumHadamardTransformNumberOfQubitsAndNumberOfQuantumRegistersNotEqualError()
        """
        Retrieve the Number Of Qubits And Number Of Quantum Registers Not Equal Error for
        the Qiskrypt's Quantum Hadamard Transform.
        """

        """
        Raise the Number Of Qubits And Number Of Quantum Registers Not Equal Error for
        the Qiskrypt's Quantum Hadamard Transform.
        """
        raise number_of_qubits_and_number_of_quantum_registers_not_equal_error

    @staticmethod
    def raise_number_of_qubits_greater_than_maximum_for_qasm_error() -> None:
        """
        Return/Raise a Number of Qubits Greater Than Maximum For QASM (Quantum Assembly) Error for
        the Qiskrypt's Quantum Hadamard Transform.

        :raise number_of_qubits_greater_than_maximum_for_qasm_error: a Number of Qubits Greater Than Maximum For QASM (Quantum Assembly) Error for
                                                                     the Qiskrypt's Quantum Hadamard Transform.
        """

        number_of_qubits_greater_than_maximum_for_qasm_error = \
            QiskryptQuantumHadamardTransformNumberOfQubitsGreaterThanMaximumForQASMError()
        """
        Retrieve the Number of Qubits Greater Than Maximum For QASM (Quantum Assembly) Error for
        the Qiskrypt's Quantum Hadamard Transform.
        """

        """
        Raise the Number of Qubits Greater Than Maximum For QASM (Quantum Assembly) Error for
        the Qiskrypt's Quantum Hadamard Transform.
        """
        raise number_of_qubits_greater_than_maximum_for_qasm_error
