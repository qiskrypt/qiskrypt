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

from src.quantum_regime.cryptography.QiskryptQuantumCryptographicPrimitive \
    import QiskryptQuantumCryptographicPrimitive
"""
Import the Qiskrypt's Quantum Cryptographic Primitive.
"""

from src.quantum_regime.networking_and_communications.sessions.QiskryptCommunicationSession \
    import QiskryptCommunicationSession
"""
Import the Qiskrypt's Communication Session.
"""

from src.quantum_regime.cryptography.QiskryptQuantumCryptographicPrimitive \
    import POSSIBLE_QUANTUM_CRYPTOGRAPHIC_PRIMITIVE_TYPES
"""
Import the available Quantum Cryptographic Primitive types for
the Qiskrypt's Quantum Cryptographic Primitives.
"""


"""
Definition of Constants and Enumerations.
"""

POSSIBLE_QUANTUM_KEY_EXCHANGE_PROTOCOL_TYPES = ["QUANTUM KEY DISTRIBUTION (QKD)",
                                                "SEMI-QUANTUM KEY DISTRIBUTION (SQKD)",
                                                "QUANTUM CONFERENCE KEY AGREEMENT (QCKA)",
                                                "SEMI-QUANTUM CONFERENCE KEY AGREEMENT (SQCKA)"]
"""
The available Quantum Key Exchange Protocol types for
the Qiskrypt's Quantum Key Exchange Protocol.
"""


class QiskryptQuantumKeyExchangeProtocol(QiskryptQuantumCryptographicPrimitive):
    """
    Object class for the Qiskrypt's Quantum Key Exchange Protocol.
    """

    def __init__(self, primitive_name: str, primitive_cardinality: str, primitive_signal_variable_type: str,
                 primitive_context: str, primitive_properties: list,  primitive_scenario: str,
                 protocol_type: str, num_rounds_for_quantum_transmission_phase: int, verbose=True):
        """
        Constructor of the Qiskrypt's Quantum Cryptographic Primitive.

        :param primitive_name: the name of the Qiskrypt's Quantum Cryptographic Primitive.
        :param primitive_cardinality: the cardinality of the Qiskrypt's Quantum Cryptographic Primitive.
        :param primitive_signal_variable_type: the signal variable type of the Qiskrypt's
                                               Quantum Cryptographic Primitive.
        :param primitive_context: the context of the Qiskrypt's Quantum Cryptographic Primitive.
        :param primitive_properties: the list of properties of the Qiskrypt's Quantum Cryptographic Primitive.
        :param primitive_scenario: the scenario of the Qiskrypt's Quantum Cryptographic Primitive.
        :param protocol_type: the type of the Qiskrypt's Quantum Key Exchange Protocol.
        :param num_rounds_for_quantum_transmission_phase: the number of rounds for the Quantum Transmission in
                                                          the Qiskrypt's Quantum Key Exchange Protocol.
        :param verbose: the boolean flag to show the runtime information about
                        the Qiskrypt's Quantum Cryptographic Primitive.
        """

        if protocol_type in POSSIBLE_QUANTUM_KEY_EXCHANGE_PROTOCOL_TYPES:
            """
            If the given type of the Qiskrypt's Quantum Key Exchange Protocol is valid.
            """

            super().__init__(primitive_name, primitive_cardinality, primitive_signal_variable_type,
                             primitive_context, primitive_properties, primitive_scenario,
                             POSSIBLE_QUANTUM_CRYPTOGRAPHIC_PRIMITIVE_TYPES[1], verbose)
            """
            Call of the constructor of the super-class Qiskrypt's Quantum Cryptographic Primitive.
            """

            self.protocol_type = protocol_type
            """
            Set the scenario of the Qiskrypt's Quantum Key Exchange Protocol.
            """

            self.num_rounds_for_quantum_transmission_phase = \
                num_rounds_for_quantum_transmission_phase
            """
            Set the number of rounds for the Quantum Transmission Phase in
            the Qiskrypt's Quantum Key Exchange Protocol.
            """

            self.communication_session = None
            """
            Set the Qiskrypt's Communication Session for
            the Qiskrypt's Quantum Key Exchange Protocol, initially, as None.
            """

            self.configured = False
            """
            Set the boolean flag to determine if the Qiskrypt's Key Exchange Protocol
            is configured, initially as False.
            """

            self.quantum_transmission_phase_rounds = list()
            """
            Create the list of the rounds for the Quantum Transmission Phase of
            the Qiskrypt's Quantum Key Exchange Protocol, initially, as an empty list.
            """

        else:
            """
            If the given type of the Qiskrypt's Quantum Key Exchange Protocol is not valid.
            """

            # TODO Throw - Exception

    def get_primitive_name(self) -> str:
        """
        Return the name of the Qiskrypt's Quantum Cryptographic Primitive.

        :return super().get_primitive_name(): the name of the Qiskrypt's Quantum Cryptographic Primitive.
        """

        """
        Return the name of the Qiskrypt's Quantum Cryptographic Primitive.
        """
        return super().get_primitive_name()

    def get_primitive_cardinality(self) -> str:
        """
        Return the cardinality of the Qiskrypt's Quantum Cryptographic Primitive.

        :return super().get_primitive_cardinality(): the cardinality of the Qiskrypt's
                                                     Quantum Cryptographic Primitive.
        """

        """
        Return the cardinality of the Qiskrypt's Quantum Cryptographic Primitive.
        """
        return super().get_primitive_cardinality()

    def get_primitive_signal_variable_type(self) -> str:
        """
        Return the signal variable type of the Qiskrypt's Quantum Cryptographic Primitive.

        :return super().get_primitive_signal_variable_type(): the signal variable type of the
                                                              Qiskrypt's Quantum Cryptographic Primitive.
        """

        """
        Return the signal variable type of the Qiskrypt's Quantum Cryptographic Primitive.
        """
        return super().get_primitive_signal_variable_type()

    def get_primitive_context(self) -> str:
        """
        Return the context of the Qiskrypt's Quantum Cryptographic Primitive.

        :return super().get_primitive_context(): the context of the Qiskrypt's Quantum Cryptographic Primitive.
        """

        """
        Return the context of the Qiskrypt's Quantum Cryptographic Primitive.
        """
        return super().get_primitive_context()

    def get_primitive_properties(self) -> list:
        """
        Return the list of properties of the Qiskrypt's Quantum Cryptographic Primitive.

        :return super().get_primitive_properties(): the list of properties of the Qiskrypt's
                                                    Quantum Cryptographic Primitive.
        """

        """
        Return the list of properties of the Qiskrypt's Quantum Cryptographic Primitive.
        """
        return super().get_primitive_properties()

    def get_primitive_scenario(self) -> str:
        """
        Return the scenario of the Qiskrypt's Quantum Cryptographic Primitive.

        :return super().get_primitive_scenario(): the scenario of the Qiskrypt's Quantum Cryptographic Primitive.
        """

        """
        Return the scenario of the Qiskrypt's Quantum Cryptographic Primitive.
        """
        return super().get_primitive_scenario()

    def get_primitive_type(self) -> str:
        """
        Return the type of the Qiskrypt's Quantum Cryptographic Primitive.

        :return super().get_primitive_type(): the type of the Qiskrypt's Quantum Cryptographic Primitive.
        """

        """
        Return the type of the Qiskrypt's Quantum Cryptographic Primitive.
        """
        return super().get_primitive_type()

    def is_verbose(self) -> bool:
        """
        Return the boolean flag to show the runtime information about
        the Qiskrypt's Quantum Cryptographic Primitive.

        :return super().is_verbose(): the boolean flag to show the runtime information about
                                      the Qiskrypt's Quantum Cryptographic Primitive.
        """

        """
        Return the boolean flag to show the runtime information about
        the Qiskrypt's Quantum Cryptographic Primitive.
        """
        return super().is_verbose()

    def get_protocol_type(self) -> str:
        """
        Return the type of the Qiskrypt's Quantum Key Exchange Protocol.

        :return self.protocol_type: the type of the Qiskrypt's Quantum Key Exchange Protocol.
        """

        """
        Return the type of the Qiskrypt's Quantum Key Exchange Protocol.
        """
        return self.protocol_type

    def get_num_rounds_for_quantum_transmission_phase(self) -> int:
        """
        Return the number of rounds for the Quantum Transmission Phase in
        the Qiskrypt's Quantum Key Exchange Protocol.

        :return self.num_rounds_for_quantum_transmission_phase: the number of rounds for
                                                                the Quantum Transmission Phase in
                                                                the Qiskrypt's Quantum Key Exchange Protocol.
        """

        """
        Return the number of rounds for the Quantum Transmission Phase in
        the Qiskrypt's Quantum Key Exchange Protocol.
        """
        return self.num_rounds_for_quantum_transmission_phase

    def get_communication_session(self) -> QiskryptCommunicationSession:
        """
        Return the Qiskrypt's Communication Session for
        the Qiskrypt's Quantum Key Exchange Protocol.

        :return self.communication_session: the Qiskrypt's Communication Session for
                                            the Qiskrypt's Quantum Key Exchange Protocol.
        """

        """
        Return the Qiskrypt's Communication Session for
        the Qiskrypt's Quantum Key Exchange Protocol.
        """
        return self.communication_session

    def set_communication_session(self, communication_session: QiskryptCommunicationSession) -> None:
        """
        Set the Qiskrypt's Communication Session for
        the Qiskrypt's Quantum Key Exchange Protocol.

        :param communication_session: the Qiskrypt's Communication Session for
                                      the Qiskrypt's Quantum Key Exchange Protocol.
        """

        if not self.is_configured():
            """
            If the boolean flag to determine if the Qiskrypt's Key Exchange Protocol
            is configured, as False.
            """

            self.communication_session = communication_session
            """
            Set the Qiskrypt's Communication Session for
            the Qiskrypt's Quantum Key Exchange Protocol.
            """

        else:
            """
            If the boolean flag to determine if the Qiskrypt's Key Exchange Protocol
            is configured, as True.
            """

            # TODO Throw - Exception

    def is_configured(self) -> bool:
        """
        Return the boolean flag to determine if
        the Qiskrypt's Key Exchange Protocol is configured.

        :return self.configured: the boolean flag to determine if
                                 the Qiskrypt's Key Exchange Protocol is configured.
        """

        """
        Return the boolean flag to determine if the Qiskrypt's Key Exchange Protocol
        is configured.
        """
        return self.configured

    def set_as_configured(self) -> None:
        """
        Set the boolean flag to determine if the Qiskrypt's Key Exchange Protocol
        is configured, as True, if it is not yet defined as True.
        """

        if not self.is_configured():
            """
            If the boolean flag to determine if the Qiskrypt's Key Exchange Protocol
            is configured, as False.
            """

            self.configured = True
            """
            Set the boolean flag to determine if the Qiskrypt's Key Exchange Protocol
            is configured, as True.
            """

        else:
            """
            If the boolean flag to determine if the Qiskrypt's Key Exchange Protocol
            is configured, as True.
            """

            # TODO Throw - Exception

    def get_quantum_transmission_phase_rounds(self) -> list:
        """
        Return the list of the rounds for the Quantum Transmission Phase of
        the Qiskrypt's Quantum Key Exchange Protocol.

        :return self.quantum_transmission_phase_rounds: the list of the rounds for the Quantum Transmission Phase of
                                                        the Qiskrypt's Quantum Key Exchange Protocol.
        """

        if self.is_configured():
            """
            If the boolean flag to determine if the Qiskrypt's Key Exchange Protocol
            is configured, as True.
            """

            """
            Return the list of the rounds for the Quantum Transmission Phase of
            the Qiskrypt's Quantum Key Exchange Protocol.
            """
            return self.quantum_transmission_phase_rounds

        else:
            """
            If the boolean flag to determine if the Qiskrypt's Key Exchange Protocol
            is configured, as False.
            """

            # TODO Throw - Exception

    def start_quantum_transmission_phase(self) -> None:
        """
        Start the Quantum Transmission Phase of the
        Qiskrypt's Quantum Key Exchange Protocol.
        """

        """
        Raise a Not Implemented Error since this abstract method
        should be implemented in its sub-classes.
        """
        # TODO Throw - Exception

    def start_classical_post_processing_phase(self) -> None:
        """
        Start the Classical Post-Processing Phase of the
        Qiskrypt's Quantum Key Exchange Protocol.
        """

        """
        Raise a Not Implemented Error since this abstract method
        should be implemented in its sub-classes.
        """
        # TODO Throw - Exception

    def run(self) -> None:
        """
        Run the Qiskrypt's Quantum Key Exchange Protocol.
        """

        if self.is_configured():
            """
            If the Qiskrypt's Key Exchange Protocol is already configured.
            """

            self.start_quantum_transmission_phase()
            """
            Start the Quantum Transmission Phase of the
            Qiskrypt's Quantum Key Exchange Protocol.
            """

            self.start_classical_post_processing_phase()
            """
            Start the Classical Post-Processing Phase of the
            Qiskrypt's Quantum Key Exchange Protocol.
            """

        else:
            """
            If the Qiskrypt's Key Exchange Protocol is not configured yet.
            """

            # TODO Throw - Exception

    def configure(self) -> None:
        """
        Configure the Qiskrypt's Quantum Key Exchange Protocol.
        """

        """
        Raise a Not Implemented Error since this abstract method
        should be implemented in its sub-classes.
        """
        # TODO Throw - Exception
