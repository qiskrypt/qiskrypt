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
Definition of Constants and Enumerations.
"""

POSSIBLE_QUANTUM_CRYPTOGRAPHIC_PRIMITIVE_CARDINALITIES = ["BIPARTITE", "MULTIPARTITE"]
"""
The available Quantum Cryptographic Primitive cardinalities for
the Qiskrypt's Quantum Cryptographic Primitive.
"""

POSSIBLE_QUANTUM_CRYPTOGRAPHIC_PRIMITIVE_SIGNAL_VARIABLES = ["DISCRETE", "CONTINUOUS"]
"""
The available Quantum Cryptographic Primitive signal variables for
the Qiskrypt's Quantum Cryptographic Primitive.
"""

POSSIBLE_QUANTUM_CRYPTOGRAPHIC_PRIMITIVE_SCENARIOS = ["NOISELESS", "NOISY"]
"""
The available Quantum Cryptographic Primitive scenarios for
the Qiskrypt's Quantum Cryptographic Primitive.
"""

POSSIBLE_QUANTUM_CRYPTOGRAPHIC_PRIMITIVE_TYPES = ["CRYPTOCURRENCY", "KEY_EXCHANGE", "STEGANOGRAPHY"]
"""
The available Quantum Cryptographic Primitive types for
the Qiskrypt's Quantum Cryptographic Primitive.
"""


class QiskryptQuantumCryptographicPrimitive:
    """
    Object class for the Qiskrypt's Quantum Cryptographic Primitive.
    """

    def __init__(self, name: str,
                 quantum_cryptographic_primitive_cardinality: str,
                 quantum_cryptographic_primitive_signal_variable: str,
                 quantum_cryptographic_primitive_scenario: str,
                 quantum_cryptographic_primitive_type: str):
        """
        Constructor of the Qiskrypt's Quantum Cryptographic Primitive.

        :param name: the name of the Qiskrypt's Quantum Cryptographic Primitive.
        :param quantum_cryptographic_primitive_cardinality: the cardinality of the Qiskrypt's
                                                            Quantum Cryptographic Primitive.
        :param quantum_cryptographic_primitive_signal_variable: the signal variable of the Qiskrypt's
                                                                 Quantum Cryptographic Primitive.
        :param quantum_cryptographic_primitive_scenario: the scenario of the Qiskrypt's
                                                         Quantum Cryptographic Primitive.
        :param quantum_cryptographic_primitive_type: the type of the Qiskrypt's
                                                     Quantum Cryptographic Primitive.
        """

        if quantum_cryptographic_primitive_cardinality in \
                POSSIBLE_QUANTUM_CRYPTOGRAPHIC_PRIMITIVE_CARDINALITIES:
            """
            If the given cardinality of the Qiskrypt's Quantum Cryptographic Primitive is valid.
            """

            if quantum_cryptographic_primitive_signal_variable in \
                    POSSIBLE_QUANTUM_CRYPTOGRAPHIC_PRIMITIVE_SIGNAL_VARIABLES:
                """
                If the given signal variable of the Qiskrypt's Quantum Cryptographic Primitive is valid.
                """

                if quantum_cryptographic_primitive_scenario in \
                        POSSIBLE_QUANTUM_CRYPTOGRAPHIC_PRIMITIVE_SCENARIOS:
                    """
                    If the given scenario of the Qiskrypt's Quantum Cryptographic Primitive is valid.
                    """

                    if quantum_cryptographic_primitive_type in POSSIBLE_QUANTUM_CRYPTOGRAPHIC_PRIMITIVE_TYPES:
                        """
                        If the given type of the Qiskrypt's Quantum Cryptographic Primitive is valid.
                        """

                        self.name = name
                        """
                        Se the name of the name of the Qiskrypt's Quantum Cryptographic Primitive.
                        """

                        self.quantum_cryptographic_primitive_cardinality = quantum_cryptographic_primitive_cardinality
                        """
                        Set the cardinality of the Qiskrypt's Quantum Cryptographic Primitive.
                        """

                        self.quantum_cryptographic_primitive_signal_variable = quantum_cryptographic_primitive_signal_variable
                        """
                        Set the signal variable of the Qiskrypt's Quantum Cryptographic Primitive.
                        """

                        self.quantum_cryptographic_primitive_scenario = quantum_cryptographic_primitive_scenario
                        """
                        Set the scenario of the Qiskrypt's Quantum Cryptographic Primitive.
                        """

                        self.quantum_cryptographic_primitive_type = quantum_cryptographic_primitive_type
                        """
                        Set the type of the Qiskrypt's Quantum Cryptographic Primitive.
                        """

                    else:
                        """
                        If the given type of the Qiskrypt's Quantum Cryptographic Primitive is not valid.
                        """

                        # TODO Throw - Exception

                else:
                    """
                    If the given scenario of the Qiskrypt's Quantum Cryptographic Primitive is not valid.
                    """

                    # TODO Throw - Exception

            else:
                """
                If the given signal variable of the Qiskrypt's Quantum Cryptographic Primitive is not valid.
                """

                # TODO Throw - Exception

        else:
            """
            If the given cardinality of the Qiskrypt's Quantum Cryptographic Primitive is not valid.
            """

            # TODO Throw - Exception

    def get_name(self) -> str:
        """
        Return the name of the Qiskrypt's Quantum Cryptographic Primitive.

        :return self.name: the name of the Qiskrypt's Quantum Cryptographic Primitive.
        """

        """
        Return the name of the Qiskrypt's Quantum Cryptographic Primitive.
        """
        return self.name

    def get_quantum_cryptographic_primitive_cardinality(self) -> str:
        """
        Return the cardinality of the Qiskrypt's Quantum Cryptographic Primitive.

        :return self.quantum_cryptographic_primitive_cardinality: the cardinality of the Qiskrypt's
                                                                  Quantum Cryptographic Primitive.
        """

        """
        Return the cardinality of the Qiskrypt's Quantum Cryptographic Primitive.
        """
        return self.quantum_cryptographic_primitive_cardinality

    def get_quantum_cryptographic_primitive_signal_variable(self) -> str:
        """
        Return the signal variable of the Qiskrypt's Quantum Cryptographic Primitive.

        :return self.quantum_cryptographic_primitive_signal_variable: the signal variable of the Qiskrypt's
                                                                      Quantum Cryptographic Primitive.
        """

        """
        Return the signal variable of the Qiskrypt's Quantum Cryptographic Primitive.
        """
        return self.quantum_cryptographic_primitive_signal_variable

    def get_quantum_cryptographic_primitive_scenario(self) -> str:
        """
        Return the scenario of the Qiskrypt's Quantum Cryptographic Primitive.

        :return self.quantum_cryptographic_primitive_scenario: the scenario of the Qiskrypt's
                                                               Quantum Cryptographic Primitive.
        """

        """
        Return the scenario of the Qiskrypt's Quantum Cryptographic Primitive.
        """
        return self.quantum_cryptographic_primitive_scenario

    def get_quantum_cryptographic_primitive_type(self) -> str:
        """
        Return the type of the Qiskrypt's Quantum Cryptographic Primitive.

        :return self.quantum_cryptographic_primitive_type: the type of the Qiskrypt's
                                                           Quantum Cryptographic Primitive.
        """

        """
        Return the type of the Qiskrypt's Quantum Cryptographic Primitive.
        """
        return self.quantum_cryptographic_primitive_type
