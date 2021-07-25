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
from src.circuit.QiskryptQuantumCircuit import QiskryptQuantumCircuit

"""
Import required Libraries and Packages.
"""

from numba import jit, prange
"""
Import NoPython mode of Just-In-Time and Parallel Range from Numba.
"""

from src.circuit.exception.QiskryptQuantumCircuitException \
    import QiskryptQuantumCircuitInvalidOrNoneGivenError
"""
Import the Invalid or None Quantum Circuit Given Error for
the Qiskrypt's Quantum Circuit.
"""

from src.circuit.exception.QiskryptQuantumCircuitException \
    import QiskryptQuantumCircuitNotAnInstanceOfError
"""
Import the Not An Instance Of Quantum Circuit Error for
the Qiskrypt's Quantum Circuit.
"""

"""
Constants.
"""

USE_NUMBA_PARALLEL = True
"""
The boolean flag to specify the parallelization parameter of Numba.
"""


class QiskryptQuantumHadamardTransform:

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

    @jit(nopython=False, forceobj=True, parallel=USE_NUMBA_PARALLEL)
    def apply_transform(self) -> None:
        """

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
