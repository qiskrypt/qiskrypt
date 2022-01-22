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
Definition of the custom Exception messages.
"""

MESSAGE_UNSUPPORTED_TYPE_REGISTERS_EXCEPTION = "Unsupported Type for Registers Error: " \
                                               "The Qiskrypt's Quantum Circuit only supports Register(s) given as list...\n"
"""
The custom defined message for the Unsupported Type for Registers Error for
the Qiskrypt's Quantum Circuit.
"""

MESSAGE_INVALID_QISKIT_QUANTUM_REGISTER_INDEX_GIVEN_EXCEPTION = "Invalid IBM Qiskit's Quantum Register Index Given Error: " \
                                                                "The given index for the IBM Qiskit's Quantum Register is invalid!!!\n"
"""
The custom defined message for the Invalid IBM Qiskit's Quantum Register Index Given Error for
the Qiskrypt's Quantum Circuit.
"""

MESSAGE_INVALID_QUBIT_INDEX_GIVEN_EXCEPTION = "Invalid Qubit Index Given Error: " \
                                              "The given index for a qubit in an IBM Qiskit's Quantum Register is invalid!!!\n"
"""
The custom defined message for the Invalid Qubit Index Given Error for
the IBM Qiskit's Quantum Register.
"""

MESSAGE_INVALID_QISKIT_CLASSICAL_REGISTER_INDEX_GIVEN_EXCEPTION = "Invalid IBM Qiskit's Classical Register Index Given Error: " \
                                                                  "The given index for the IBM Qiskit's Classical Register is invalid!!!\n"
"""
The custom defined message for the Invalid IBM Qiskit's Classical Register Index Given Error for
the Qiskrypt's Quantum Circuit.
"""

MESSAGE_INVALID_BIT_INDEX_GIVEN_EXCEPTION = "Invalid Bit Index Given Error: " \
                                            "The given index for a bit in an IBM Qiskit's Classical Register is invalid!!!\n"
"""
The custom defined message for the Invalid Qubit Index Given Error for
the IBM Qiskit's Classical Register.
"""

MESSAGE_REGISTER_NOT_FOUND_EXCEPTION = "Register Not Found Error: " \
                                       "The supposed Qiskrypt's Register do not exist in the Qiskrypt's Quantum Circuit!!!\n"
"""
The custom defined message for the Register Not Found Error for
the Qiskrypt's Quantum Circuit.
"""

MESSAGE_NUM_QUANTUM_REGISTERS_AND_NUM_CLASSICAL_REGISTERS_ARE_NOT_EQUAL_EXCEPTION = "Number of Quantum Registers and Number of Classical Registers Are Not Equal Error: " \
                                                                                    "The number of IBM Qiskit's Quantum Registers and " \
                                                                                    "the number of IBM Qiskit's Classical Registers are not equal and must be, " \
                                                                                    "in order to complete the pretended operation/measurement!!!\n"
"""
The custom defined message for the Number of Quantum Registers and Number of Classical Registers Are Not Equal Error for
the Qiskrypt's Quantum Circuit.
"""

MESSAGE_NUM_QUBITS_AND_NUM_BITS_ARE_NOT_EQUAL_EXCEPTION = "Number of Qubits and Number of Bits Are Not Equal Error: " \
                                                          "The number of qubits and the number of bits are not equal and must be, " \
                                                          "in order to complete the pretended operation/measurement!!!\n"
"""
The custom defined message for the Number of Qubits and Number of Bits Are Not Equal Error for
the Qiskrypt's Quantum Circuit.
"""

MESSAGE_LIST_DO_NOT_REPRESENT_A_SQUARE_UNITARY_MATRIX_OPERATOR_EXCEPTION = "List Do Not Represent a Square Unitary Matrix Operator Error: " \
                                                                           "The given list of complex numbers/angles do not represent " \
                                                                           "a square unitary matrix/operator!!!\n"
"""
The custom defined message for the List Do Not Represent a Square Unitary Matrix Operator Error for
the Qiskrypt's Quantum Circuit.
"""

MESSAGE_INVALID_OR_NONE_QUANTUM_CIRCUIT_GIVEN_EXCEPTION = "Invalid or None Quantum Circuit Given Error: " \
                                                          "An invalid or none Qiskrypt's Quantum Circuit was given as argument!!!\n"
"""
The custom defined message for the Invalid or None Quantum Circuit Given Error for
the Qiskrypt's Quantum Circuit.
"""

MESSAGE_NOT_AN_INSTANCE_OF_QUANTUM_CIRCUIT_EXCEPTION = "Not An Instance Of Quantum Circuit Error: " \
                                                       "The Quantum Circuit given as argument is not a Qiskrypt's Quantum Circuit!!!\n"
"""
The custom defined message for the Not An Instance Of Quantum Circuit Error for
the Qiskrypt's Quantum Circuit.
"""

MESSAGE_QUANTUM_CIRCUIT_NOT_INITIALISED_YET_EXCEPTION = "Quantum Circuit Not Initialised Yet Error: " \
                                                        "The respective Qiskrypt's Quantum Circuit was not initialised yet!!!\n"
"""
The custom defined message for the Quantum Circuit Not Initialised Yet Error for
the Qiskrypt's Quantum Circuit.
"""

MESSAGE_QUANTUM_CIRCUIT_ALREADY_INITIALISED_EXCEPTION = "Quantum Circuit Already Initialised Error: " \
                                                        "The respective Qiskrypt's Quantum Circuit was already initialised!!!\n"
"""
The custom defined message for the Quantum Circuit Already Initialised Error for
the Qiskrypt's Quantum Circuit.
"""


class QiskryptQuantumCircuitUnsupportedTypeRegistersError(Exception):
    """
    Object Class of the Unsupported Type of Registers Error for
    the Qiskrypt's Quantum Circuit.
    """

    def __init__(self, message=MESSAGE_UNSUPPORTED_TYPE_REGISTERS_EXCEPTION):
        """
        Constructor for the Unsupported Type of Registers Error for
        the Qiskrypt's Quantum Circuit.

        :param message: the custom message for the Unsupported Type of Registers Error for
                        the Qiskrypt's Quantum Circuit.
        """

        self.message = message
        """
        Set the custom message for the Unsupported Type of Registers Error for
        the Qiskrypt's Quantum Circuit.
        """

        super().__init__(self.message)
        """
        Calls the constructor of the super-class Exception.
        """


class QiskryptQuantumCircuitInvalidQiskitQuantumRegisterIndexGivenError(Exception):
    """
    Object Class of the Invalid Qiskit Quantum Register Index Given Error for
    the Qiskrypt's Quantum Circuit.
    """

    def __init__(self, message=MESSAGE_INVALID_QISKIT_QUANTUM_REGISTER_INDEX_GIVEN_EXCEPTION):
        """
        Constructor for the Invalid Qiskit
        Quantum Register Index Given Error for the Qiskrypt's Quantum Circuit.

        :param message: the custom message for the Invalid Qiskit
                        Quantum Register Index Given Error for the Qiskrypt's Quantum Circuit.
        """

        self.message = message
        """
        Set the custom message for the Invalid Qiskit
        Quantum Register Index Given Error for the Qiskrypt's Quantum Circuit.
        """

        super().__init__(self.message)
        """
        Calls the constructor of the super-class Exception.
        """


class QiskryptQuantumCircuitInvalidQubitIndexGivenError(Exception):
    """
    Object Class of the Invalid Qubit Index Given Error for
    the Qiskrypt's Quantum Circuit.
    """

    def __init__(self, message=MESSAGE_INVALID_QUBIT_INDEX_GIVEN_EXCEPTION):
        """
        Constructor for the Invalid Qubit Index Given Error for
        the Qiskrypt's Quantum Circuit.

        :param message: the custom message for the Invalid Qubit Index Given Error for
                        the Qiskrypt's Quantum Circuit.
        """

        self.message = message
        """
        Set the custom message for the Invalid Qubit Index Given Error for
        the Qiskrypt's Quantum Circuit.
        """

        super().__init__(self.message)
        """
        Calls the constructor of the super-class Exception.
        """


class QiskryptQuantumCircuitInvalidQiskitClassicalRegisterIndexGivenError(Exception):
    """
    Object Class of the Invalid Qiskit Classical Register Index Given Error for
    the Qiskrypt's Quantum Circuit.
    """

    def __init__(self, message=MESSAGE_INVALID_QISKIT_CLASSICAL_REGISTER_INDEX_GIVEN_EXCEPTION):
        """
        Constructor for the Invalid Qiskit
        Classical Register Index Given Error for the Qiskrypt's Quantum Circuit.

        :param message: the custom message for the Invalid Qiskit
                        Classical Register Index Given Error for the Qiskrypt's Quantum Circuit.
        """

        self.message = message
        """
        Set the custom message for the Invalid Qiskit
        Classical Register Index Given Error for the Qiskrypt's Quantum Circuit.
        """

        super().__init__(self.message)
        """
        Calls the constructor of the super-class Exception.
        """


class QiskryptQuantumCircuitInvalidBitIndexGivenError(Exception):
    """
    Object Class of the Invalid Bit Index Given Error for
    the Qiskrypt's Quantum Circuit.
    """

    def __init__(self, message=MESSAGE_INVALID_BIT_INDEX_GIVEN_EXCEPTION):
        """
        Constructor for the Invalid Bit Index Given Error for
        the Qiskrypt's Quantum Circuit.

        :param message: the custom message for the Invalid Bit Index Given Error for
                        the Qiskrypt's Quantum Circuit.
        """

        self.message = message
        """
        Set the custom message for the Invalid Bit Index Given Error for
        the Qiskrypt's Quantum Circuit.
        """

        super().__init__(self.message)
        """
        Calls the constructor of the super-class Exception.
        """


class QiskryptQuantumCircuitRegisterNotFoundError(Exception):
    """
    Object Class of the Register Not Found Error for
    the Qiskrypt's Quantum Circuit.
    """

    def __init__(self, message=MESSAGE_REGISTER_NOT_FOUND_EXCEPTION):
        """
        Constructor for the Register Not Found Error for
        the Qiskrypt's Quantum Circuit.

        :param message: the custom message for the Register Not Found Error for
                        the Qiskrypt's Quantum Circuit.
        """

        self.message = message
        """
        Set the custom message for the Register Not Found Error for
        the Qiskrypt's Quantum Circuit.
        """

        super().__init__(self.message)
        """
        Calls the constructor of the super-class Exception.
        """


class QiskryptQuantumCircuitNumQuantumRegistersAndNumClassicalRegistersAreNotEqualForOperationOrMeasurementError(Exception):
    """
    Object Class of the Number of Quantum Registers and Number of Classical Registers
    Are Not Equal for Operation or Measurement Error for the Qiskrypt's Quantum Circuit.
    """

    def __init__(self, message=MESSAGE_NUM_QUANTUM_REGISTERS_AND_NUM_CLASSICAL_REGISTERS_ARE_NOT_EQUAL_EXCEPTION):
        """
        Constructor for the Number of Quantum Registers and Number of Classical Registers
        Are Not Equal for Operation or Measurement Error for the Qiskrypt's Quantum Circuit.

        :param message: the custom message for the Number of Quantum Registers and Number of Classical Registers
                        Are Not Equal for Operation or Measurement Error for the Qiskrypt's Quantum Circuit.
        """

        self.message = message
        """
        Set the custom message for the Number of Quantum Registers and Number of Classical Registers Are Not Equal for
        Operation or Measurement Error for the Qiskrypt's Quantum Circuit.
        """

        super().__init__(self.message)
        """
        Calls the constructor of the super-class Exception.
        """


class QiskryptQuantumCircuitNumQubitsAndNumBitsAreNotEqualForOperationOrMeasurementError(Exception):
    """
    Object Class of the Number of Qubits and Number of Bits Are Not Equal for Operation or Measurement Error for
    the Qiskrypt's Quantum Circuit.
    """

    def __init__(self, message=MESSAGE_NUM_QUBITS_AND_NUM_BITS_ARE_NOT_EQUAL_EXCEPTION):
        """
        Constructor for the Number of Qubits and Number of Bits Are Not Equal for
        Operation or Measurement Error for the Qiskrypt's Quantum Circuit.

        :param message: the custom message for the Number of Qubits and Number of Bits Are Not Equal for
                        Operation or Measurement Error for the Qiskrypt's Quantum Circuit.
        """

        self.message = message
        """
        Set the custom message for the Number of Qubits and Number of Bits Are Not Equal for
        Operation or Measurement Error for the Qiskrypt's Quantum Circuit.
        """

        super().__init__(self.message)
        """
        Calls the constructor of the super-class Exception.
        """


class QiskryptQuantumCircuitListDoNotRepresentASquareUnitaryMatrixOperatorError(Exception):
    """
    Object Class of the List Do Not Represent a Square Unitary Matrix Operator Error for
    the Qiskrypt's Quantum Circuit.
    """

    def __init__(self, message=MESSAGE_LIST_DO_NOT_REPRESENT_A_SQUARE_UNITARY_MATRIX_OPERATOR_EXCEPTION):
        """
        Constructor for the List Do Not Represent a Square Unitary Matrix Operator Error for
        the Qiskrypt's Quantum Circuit.

        :param message: the custom message for the List Do Not Represent a Square Unitary Matrix Operator Error for
                        the Qiskrypt's Quantum Circuit.
        """

        self.message = message
        """
        Set the custom message for the List Do Not Represent a Square Unitary Matrix Operator Error for
        the Qiskrypt's Quantum Circuit.
        """

        super().__init__(self.message)
        """
        Calls the constructor of the super-class Exception.
        """


class QiskryptQuantumCircuitInvalidOrNoneGivenError(Exception):
    """
    Object Class of the Invalid or None Quantum Circuit Given Error for the Qiskrypt's Quantum Circuit.
    """

    def __init__(self, message=MESSAGE_INVALID_OR_NONE_QUANTUM_CIRCUIT_GIVEN_EXCEPTION, primitive=""):
        """
        Constructor for the Invalid or Not Quantum Circuit Given Error for the Qiskrypt's Quantum Circuit.

        :param message: the custom message for the Invalid or Not Quantum Circuit Given Error for
                        the Qiskrypt's Quantum Circuit.
        :param primitive: the Qiskrypt's primitive for what the Invalid or None Quantum Circuit Given Error
                          is being returned/raised.
        """

        if primitive == "":
            """
            If there is no primitive, the message will not contain the respective header.
            """

            self.message = message
            """
            Set the custom message for the Invalid or Not Quantum Circuit Given Error for
            the Qiskrypt's Quantum Circuit, not considering any primitive.
            """

        else:
            """
            If there is any primitive, the message will contain the respective header.
            """

            self.message = f"{message} (related to: {primitive})"
            """
            Set the custom message for the Invalid or Not Quantum Circuit Given Error for
            the Qiskrypt's Quantum Circuit, considering the given primitive.
            """

        super().__init__(self.message)
        """
        Calls the constructor of the super-class Exception.
        """


class QiskryptQuantumCircuitNotAnInstanceOfError(Exception):
    """
    Object Class of the Not An Instance of Quantum Circuit Error for the Qiskrypt's Quantum Circuit.
    """

    def __init__(self, message=MESSAGE_NOT_AN_INSTANCE_OF_QUANTUM_CIRCUIT_EXCEPTION, primitive=""):
        """
        Constructor for the Not An Instance of Quantum Circuit Error for the Qiskrypt's Quantum Circuit.

        :param message: the custom message for the Not An Instance Of Quantum Circuit Error for
                        the Qiskrypt's Quantum Circuit.
        :param primitive: the Qiskrypt's primitive for what the Not An Instance Of Quantum Circuit Error
                          is being returned/raised.
        """

        if primitive == "":
            """
            If there is no primitive, the message will not contain the respective header.
            """

            self.message = message
            """
            Set the custom message for the Not An Instance Of Quantum Circuit Error for
            the Qiskrypt's Quantum Circuit, not considering any primitive.
            """

        else:
            """
            If there is any primitive, the message will contain the respective header.
            """

            self.message = f"{message} (related to: {primitive})"
            """
            Set the custom message for the Not An Instance Of Quantum Circuit Error for
            the Qiskrypt's Quantum Circuit, considering the given primitive.
            """

        super().__init__(self.message)
        """
        Calls the constructor of the super-class Exception.
        """


class QiskryptQuantumCircuitNotInitialisedYetError(Exception):
    """
    Object Class of the Quantum Circuit Not Initialised Yet Error for the Qiskrypt's Quantum Circuit.
    """

    def __init__(self, message=MESSAGE_QUANTUM_CIRCUIT_NOT_INITIALISED_YET_EXCEPTION, primitive=""):
        """
        Constructor for the Quantum Circuit Not Initialised Yet Error for the Qiskrypt's Quantum Circuit.

        :param message: the custom message for the Quantum Circuit Not Initialised Yet Error for
                        the Qiskrypt's Quantum Circuit.
        :param primitive: the Qiskrypt's primitive for what the Quantum Circuit Not Initialised Yet Error
                          is being returned/raised.
        """

        if primitive == "":
            """
            If there is no primitive, the message will not contain the respective header.
            """

            self.message = message
            """
            Set the custom message for the Quantum Circuit Not Initialised Yet Error for
            the Qiskrypt's Quantum Circuit, not considering any primitive.
            """

        else:
            """
            If there is any primitive, the message will contain the respective header.
            """

            self.message = f"{message} (related to: {primitive})"
            """
            Set the custom message for the Quantum Circuit Not Initialised Yet Error for
            the Qiskrypt's Quantum Circuit, considering the given primitive.
            """

        super().__init__(self.message)
        """
        Calls the constructor of the super-class Exception.
        """


class QiskryptQuantumCircuitAlreadyInitialisedError(Exception):
    """
    Object Class of the Quantum Circuit Already Initialised Error for the Qiskrypt's Quantum Circuit.
    """

    def __init__(self, message=MESSAGE_QUANTUM_CIRCUIT_ALREADY_INITIALISED_EXCEPTION, primitive=""):
        """
        Constructor for the Quantum Circuit Already Initialised Error for the Qiskrypt's Quantum Circuit.

        :param message: the custom message for the Quantum Circuit Already Initialised Error for
                        the Qiskrypt's Quantum Circuit.
        :param primitive: the Qiskrypt's primitive for what the Quantum Circuit Already Initialised Error
                          is being returned/raised.
        """

        if primitive == "":
            """
            If there is no primitive, the message will not contain the respective header.
            """

            self.message = message
            """
            Set the custom message for the Quantum Circuit Already Initialised Error for
            the Qiskrypt's Quantum Circuit, not considering any primitive.
            """

        else:
            """
            If there is any primitive, the message will contain the respective header.
            """

            self.message = f"{message} (related to: {primitive})"
            """
            Set the custom message for the Quantum Circuit Already Initialised Error for
            the Qiskrypt's Quantum Circuit, considering the given primitive.
            """

        super().__init__(self.message)
        """
        Calls the constructor of the super-class Exception.
        """
