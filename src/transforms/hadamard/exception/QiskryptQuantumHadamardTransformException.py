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
Definition of the custom Exception messages.
"""

MESSAGE_NUMBER_OF_QUBITS_AND_NUMBER_OF_QUANTUM_REGISTERS_NOT_EQUAL_EXCEPTION = "Number of Qubits And Number Of Quantum Registers " \
                                                                               "Not Equal Error (Quantum Hadamard Transform): " \
                                                                               "The number of qubits and the number of " \
                                                                               "Quantum Registers given are not equal!!!\n"
"""
The custom defined message for the Number of Qubits And Number Of Quantum Registers Not Equal Error for
the Qiskrypt's Quantum Hadamard Transform.
"""

MESSAGE_NUMBER_OF_QUBITS_GREATER_THAN_MAXIMUM_FOR_QASM_EXCEPTION = "Number Of Qubits Greater Than Maximum For " \
                                                                   "QASM Error (Quantum Hadamard Transform): " \
                                                                   "The number of qubits are greater than the maximum of " \
                                                                   "qubits allowed for QASM (Quantum Assembly) Simulator (i.e., 30 qubits)!!!\n"
"""
The custom defined message for the Number Of Qubits Greater Than Maximum For QASM Error for
the Qiskrypt's Quantum Hadamard Transform.
"""


class QiskryptQuantumHadamardTransformNumberOfQubitsAndNumberOfQuantumRegistersNotEqualError(Exception):
    """
    Object Class of the Number of Qubits And Number Of Quantum Registers Not Equal Error for
    the Qiskrypt's Quantum Hadamard Transform.
    """

    def __init__(self, message=MESSAGE_NUMBER_OF_QUBITS_AND_NUMBER_OF_QUANTUM_REGISTERS_NOT_EQUAL_EXCEPTION):
        """
        Constructor for the Number of Qubits And Number Of Quantum Registers Not Equal Error for
        the Qiskrypt's Quantum Hadamard Transform.

        :param message: the custom message for the Number of Qubits And Number Of Quantum Registers Not Equal Error
                        for the Qiskrypt's Quantum Hadamard Transform.
        """

        self.message = message
        """
        Set the custom message for the Number of Qubits And Number Of Quantum Registers Not Equal Error for
        the Qiskrypt's Quantum Hadamard Transform.
        """

        super().__init__(self.message)
        """
        Calls the constructor of the super-class Exception.
        """


class QiskryptQuantumHadamardTransformNumberOfQubitsGreaterThanMaximumForQASMError(Exception):
    """
    Object Class of the Number of Qubits Greater Than Maximum For QASM (Quantum Assembly) Error for
    the Qiskrypt's Quantum Hadamard Transform.
    """

    def __init__(self, message=MESSAGE_NUMBER_OF_QUBITS_GREATER_THAN_MAXIMUM_FOR_QASM_EXCEPTION):
        """
        Constructor for the Number of Qubits Greater Than Maximum For QASM (Quantum Assembly) Error for
        the Qiskrypt's Quantum Hadamard Transform.

        :param message: the custom message for the Number of Qubits Greater Than Maximum For QASM (Quantum Assembly) Error
                        for the Qiskrypt's Quantum Hadamard Transform.
        """

        self.message = message
        """
        Set the custom message for the Number of Qubits Greater Than Maximum For QASM (Quantum Assembly) Error for
        the Qiskrypt's Quantum Hadamard Transform.
        """

        super().__init__(self.message)
        """
        Calls the constructor of the super-class Exception.
        """
