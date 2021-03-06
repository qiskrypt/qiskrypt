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

from src.quantum_regime.cryptography.key_exchange.QiskryptQuantumKeyExchangeProtocol \
    import QiskryptQuantumKeyExchangeProtocol
"""
Import the Qiskrypt's Quantum Key Exchange Protocol.
"""

from src.quantum_regime.networking_and_communications.sessions.QiskryptCommunicationSession \
    import QiskryptCommunicationSession
"""
Import the Qiskrypt's Communication Session.
"""

from src.quantum_regime.cryptography.QiskryptQuantumCryptographicPrimitive \
    import POSSIBLE_QUANTUM_CRYPTOGRAPHIC_PRIMITIVE_CARDINALITIES
"""
Import the available Quantum Cryptographic Primitive cardinalities for
the Qiskrypt's Quantum Cryptographic Primitives.
"""

from src.quantum_regime.cryptography.QiskryptQuantumCryptographicPrimitive \
    import POSSIBLE_QUANTUM_CRYPTOGRAPHIC_PRIMITIVE_CONTEXTS
"""
Import the available Quantum Cryptographic Primitive contexts for
the Qiskrypt's Quantum Cryptographic Primitives.
"""

from src.quantum_regime.cryptography.key_exchange.QiskryptQuantumKeyExchangeProtocol \
    import POSSIBLE_QUANTUM_KEY_EXCHANGE_PROTOCOL_TYPES
"""
Import the available Quantum Key Exchange Protocol types for
the Qiskrypt's Quantum Key Exchange Protocols.
"""


"""
Definition of Constants and Enumerations.
"""

POSSIBLE_SEMI_QUANTUM_CONFERENCE_KEY_AGREEMENT_TYPES = ["PREPARE-AND-MEASURE (PM)",
                                                        "ENTANGLEMENT-BASED (EB)"]
"""
The available Semi-Quantum Conference Key Agreement (SQCKA) types for
the Qiskrypt's Semi-Quantum Conference Agreement (SQCKA).
"""

SEMI_QUANTUM_CONFERENCE_KEY_AGREEMENT_DEFAULT_PARTIES_NAMES = ["ALICE", "BOB"]
"""
The default parties' names for
the Qiskrypt's Semi-Quantum Conference Agreement (SQCKA).
"""

SEMI_QUANTUM_CONFERENCE_KEY_AGREEMENT_DEFAULT_EAVESDROPPER_NAME = ["EVE"]
"""
The default eavesdropper's names for
the Qiskrypt's Semi-Quantum Conference Agreement (SQCKA).
"""

MINIMUM_SEMI_QUANTUM_CONFERENCE_KEY_AGREEMENT_NUM_PARTIES = 2
"""
The minimum number of parties for
the Qiskrypt's Semi-Quantum Conference Key Agreement (SQCKA).
"""

DEFAULT_SEMI_QUANTUM_CONFERENCE_KEY_AGREEMENT_NUM_PARTIES = 3
"""
The default number of parties for
the Qiskrypt's Semi-Quantum Conference Key Agreement (SQCKA).
"""


class QiskryptSemiQuantumConferenceKeyAgreement(QiskryptQuantumKeyExchangeProtocol):
    """
    Object class for the Qiskrypt's Semi-Quantum Conference Key Agreement (SQCKA).
    """

    def __init__(self, primitive_name: str, primitive_signal_variable_type: str,
                 primitive_properties: list, primitive_scenario: str,
                 num_rounds_for_quantum_transmission_phase: int,
                 semi_quantum_conference_key_agreement_type: str,
                 semi_quantum_conference_key_agreement_num_parties: int, verbose=True):
        """
        Constructor of the Qiskrypt's Semi-Quantum Conference Key Agreement (SQCKA).

        :param primitive_name: the name of the Qiskrypt's Semi-Quantum Conference Key Agreement (SQCKA).
        :param primitive_signal_variable_type: the signal variable of the Qiskrypt's Quantum Cryptographic Primitive.
        :param primitive_properties: the list of properties of the Qiskrypt's Quantum Cryptographic Primitive.
        :param primitive_scenario: the scenario of the Qiskrypt's Quantum Cryptographic Primitive.
        :param num_rounds_for_quantum_transmission_phase: the number of rounds for the Quantum Transmission Phase in
                                                          the Qiskrypt's Quantum Key Exchange Protocol.
        :param semi_quantum_conference_key_agreement_type: the type of the Qiskrypt's
                                                           Semi-Quantum Conference Key Agreement (SQCKA).
        :param semi_quantum_conference_key_agreement_num_parties: the number of parties of the Qiskrypt's
                                                                  Semi-Quantum Conference Key Agreement (SQCKA).
        :param verbose: the boolean flag to show the runtime information about
                        the Qiskrypt's Quantum Cryptographic Primitive.
        """

        if semi_quantum_conference_key_agreement_type in POSSIBLE_SEMI_QUANTUM_CONFERENCE_KEY_AGREEMENT_TYPES:
            """
            If the given type of the Qiskrypt's Semi-Quantum Conference Key Agreement (SQCKA) is valid.
            """

            super().__init__(primitive_name, POSSIBLE_QUANTUM_CRYPTOGRAPHIC_PRIMITIVE_CARDINALITIES[1],
                             primitive_signal_variable_type, POSSIBLE_QUANTUM_CRYPTOGRAPHIC_PRIMITIVE_CONTEXTS[1],
                             primitive_properties, primitive_scenario,
                             POSSIBLE_QUANTUM_KEY_EXCHANGE_PROTOCOL_TYPES[3],
                             num_rounds_for_quantum_transmission_phase, verbose)
            """
            Call of the constructor of the super-class Qiskrypt's Quantum Key Exchange Protocol.
            """

            self.semi_quantum_conference_key_agreement_type = \
                semi_quantum_conference_key_agreement_type
            """
            Set the type of the Qiskrypt's Semi-Quantum Conference Key Agreement (SQCKA).
            """

            if semi_quantum_conference_key_agreement_num_parties >= \
                    MINIMUM_SEMI_QUANTUM_CONFERENCE_KEY_AGREEMENT_NUM_PARTIES:
                """
                If the number of parties for the Qiskrypt's Semi-Quantum Conference Key Agreement (SQCKA) is valid.
                """

                self.semi_quantum_conference_key_agreement_num_parties = \
                    semi_quantum_conference_key_agreement_num_parties
                """
                Set the number of parties of the Qiskrypt's Semi-Quantum Conference Key Agreement (SQCKA).
                """

            self.quantum_transmission_phase_rounds_not_discarded_from_key_sifting = list()
            """
            Create the list of the rounds for the Quantum Transmission Phase of
            the Qiskrypt's Semi-Quantum Conference Key Agreement (SQCKA) not discarded from
            the Key Sifting, initially, as an empty list.
            """

            self.quantum_transmission_phase_rounds_not_discarded_from_parameter_estimation = list()
            """
            Create the list of the rounds for the Quantum Transmission Phase of
            the Qiskrypt's Semi-Quantum Conference Key Agreement (SQCKA) not discarded from
            the Parameter Estimation, initially, as an empty list.
            """

        else:
            """
            If the given type of the Qiskrypt's Semi-Quantum Conference Key Agreement (SQCKA) is not valid.
            """

            # TODO Throw - Exception

    def get_primitive_name(self) -> str:
        """
        Return the name of the Qiskrypt's Quantum Cryptographic Primitive.

        :return super().get_primitive_name(): the name of the Qiskrypt's
                                              Quantum Cryptographic Primitive.
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

        :return super().get_primitive_signal_variable_type(): the signal variable type of
                                                              the Qiskrypt's Quantum Cryptographic Primitive.
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

        :return super().get_primitive_scenario(): the scenario of the Qiskrypt's
                                                  Quantum Cryptographic Primitive.
        """

        """
        Return the scenario of the Qiskrypt's Quantum Cryptographic Primitive.
        """
        return super().get_primitive_scenario()

    def get_primitive_type(self) -> str:
        """
        Return the type of the Qiskrypt's Quantum Cryptographic Primitive.

        :return super().get_primitive_type(): the type of the Qiskrypt's
                                              Quantum Cryptographic Primitive.
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

        :return super().get_protocol_type(): the type of the Qiskrypt's Quantum Key Exchange Protocol.
        """

        """
        Return the type of the Qiskrypt's Quantum Key Exchange Protocol.
        """
        return super().get_protocol_type()

    def get_num_rounds_for_quantum_transmission_phase(self) -> int:
        """
        Return the number of rounds for the Quantum Transmission Phase in
        the Qiskrypt's Quantum Key Exchange Protocol.

        :return super().get_num_rounds_for_quantum_transmission_phase(): the number of rounds for
                                                                         the Quantum Transmission Phase in
                                                                         the Qiskrypt's Quantum Key Exchange Protocol.
        """

        """
        Return the number of rounds for the Quantum Transmission Phase in
        the Qiskrypt's Quantum Key Exchange Protocol.
        """
        return super().get_num_rounds_for_quantum_transmission_phase()

    def get_communication_session(self) -> QiskryptCommunicationSession:
        """
        Return the Qiskrypt's Communication Session for
        the Qiskrypt's Quantum Key Exchange Protocol.

        :return super().get_communication_session(): the Qiskrypt's Communication Session for
                                                     the Qiskrypt's Quantum Key Exchange Protocol.
        """

        """
        Return the Qiskrypt's Communication Session for
        the Qiskrypt's Quantum Key Exchange Protocol.
        """
        return super().get_communication_session()

    def set_communication_session(self, communication_session: QiskryptCommunicationSession) -> None:
        """
        Set the Qiskrypt's Communication Session for
        the Qiskrypt's Quantum Key Exchange Protocol.

        :param communication_session: the Qiskrypt's Communication Session for
                                      the Qiskrypt's Quantum Key Exchange Protocol.
        """

        super().set_communication_session(communication_session)
        """
        Set the Qiskrypt's Communication Session for
        the Qiskrypt's Quantum Key Exchange Protocol.
        """

    def is_configured(self) -> bool:
        """
        Return the boolean flag to determine if
        the Qiskrypt's Key Exchange Protocol is configured.

        :return super().is_configured(): the boolean flag to determine if
                                         the Qiskrypt's Key Exchange Protocol is configured.
        """

        """
        Return the boolean flag to determine if the Qiskrypt's Key Exchange Protocol
        is configured.
        """
        return super().is_configured()

    def set_as_configured(self):
        """
        Set the boolean flag to determine if the Qiskrypt's Key Exchange Protocol
        is configured, as True, if it is not yet defined as True.
        """

        super().set_as_configured()
        """
        Set the boolean flag to determine if the Qiskrypt's Key Exchange Protocol
        is configured, as True.
        """

    def get_quantum_transmission_phase_rounds(self) -> list:
        """
        Return the list of the rounds for the Quantum Transmission Phase of
        the Qiskrypt's Quantum Key Exchange Protocol.

        :return super().get_quantum_transmission_phase_rounds: the list of the rounds for
                                                               the Quantum Transmission Phase of
                                                               the Qiskrypt's Quantum Key Exchange Protocol.
        """

        """
        Return the list of the rounds for the Quantum Transmission Phase of
        the Qiskrypt's Quantum Key Exchange Protocol.
        """
        return super().get_quantum_transmission_phase_rounds()

    def get_quantum_transmission_phase_rounds_not_discarded_from_key_sifting(self) -> list:
        """
        Return the list of the rounds for the Quantum Transmission Phase of
        the Qiskrypt's Semi-Quantum Conference Key Agreement (SQCKA) not discarded from the Key Sifting.

        :return self.quantum_transmission_phase_rounds_not_discarded_from_key_sifting:
                the list of the rounds for the Quantum Transmission Phase of
                the Qiskrypt's Semi-Quantum Conference Key Agreement (SQCKA) not discarded from the Key Sifting.
        """

        if super().is_configured():
            """
            If the Qiskrypt's Key Exchange Protocol is already configured.
            """

            """
            Return the list of the rounds for the Quantum Transmission Phase of
            the Qiskrypt's Semi-Quantum Conference Key Agreement (SQCKA) not discarded from the Key Sifting.
            """
            return self.quantum_transmission_phase_rounds_not_discarded_from_key_sifting

        else:
            """
            If the Qiskrypt's Key Exchange Protocol is not configured yet.
            """

            # TODO Throw - Exception

    def get_quantum_transmission_phase_rounds_not_discarded_from_parameter_estimation(self) -> list:
        """
        Return the list of the rounds for the Quantum Transmission Phase of
        the Qiskrypt's Semi-Quantum Conference Key Agreement (SQCKA) not discarded from
        the Parameter Estimation.

        :return self.quantum_transmission_phase_rounds_not_discarded_from_parameter_estimation:
                the list of the rounds for the Quantum Transmission Phase of
                the Qiskrypt's Semi-Quantum Conference Key Agreement (SQCKA) not discarded from
                the Parameter Estimation.
        """

        if super().is_configured():
            """
            If the Qiskrypt's Key Exchange Protocol is already configured.
            """

            """
            Return the list of the rounds for the Quantum Transmission Phase of
            the Qiskrypt's Semi-Quantum Conference Key Agreement (SQCKA) not discarded from
            the Parameter Estimation.
            """
            return self.quantum_transmission_phase_rounds_not_discarded_from_parameter_estimation

        else:
            """
            If the Qiskrypt's Key Exchange Protocol is not configured yet.
            """

            # TODO Throw - Exception

    def get_semi_quantum_conference_key_agreement_type(self) -> str:
        """
        Return the type of the Qiskrypt's Semi-Quantum Conference Key Agreement (SQCKA).

        :return self.semi_quantum_conference_key_agreement_type: the type of the Qiskrypt's
                                                                 Semi-Quantum Conference Key Agreement (SQCKA).
        """

        """
        Return the type of the Qiskrypt's Semi-Quantum Conference Key Agreement (SQCKA).
        """
        return self.semi_quantum_conference_key_agreement_type

    def get_semi_quantum_conference_key_agreement_num_parties(self) -> int:
        """
        Return the number of the parties of the Qiskrypt's Semi-Quantum Conference Key Agreement (SQCKA).

        :return self.semi_quantum_conference_key_agreement_num_parties: the number of the parties of the Qiskrypt's
                                                                        Semi-Quantum Conference Key Agreement (SQCKA).
        """

        """
        Return the number of the parties of the Qiskrypt's Semi-Quantum Conference Key Agreement (SQCKA).
        """
        return self.semi_quantum_conference_key_agreement_num_parties

    def start_quantum_transmission_phase(self):
        """
        Start the Quantum Transmission Phase of the
        Qiskrypt's Quantum Key Exchange Protocol.
        """

        self.prepare_quantum_states()
        """
        Prepare the Quantum States for the Quantum Transmission Phase of
        the Semi-Quantum Conference Key Agreement (SQCKA).
        """

        self.transmit_quantum_states()
        """
        Transmit the Quantum States for the Quantum Transmission Phase of
        the Semi-Quantum Conference Key Agreement (SQCKA).
        """

        self.measure_quantum_states()
        """
        Measure the Quantum States for the Quantum Transmission Phase of
        the Semi-Quantum Conference Key Agreement (SQCKA).
        """

    def start_classical_post_processing_phase(self):
        """
        Start the Classical Post-Processing Phase of the
        Qiskrypt's Quantum Key Exchange Protocol.
        """

        self.sift_raw_key()
        """
        Sift the Raw Key for the Classical Post-Processing Phase of
        the Semi-Quantum Conference Key Agreement (SQCKA).
        """

        self.estimate_parameters()
        """
        Estimate the Parameters for the Classical Post-Processing Phase of
        the Semi-Quantum Conference Key Agreement (SQCKA).
        """

        self.reconcile_information()
        """
        Reconcile the Information for the Classical Post-Processing Phase of
        the Semi-Quantum Conference Key Agreement (SQCKA).
        """

        self.amplify_privacy()
        """
        Amplify the Privacy for the Classical Post-Processing Phase of
        the Semi-Quantum Conference Key Agreement (SQCKA).
        """

    def run(self) -> None:
        """
        Run the Qiskrypt's Quantum Key Exchange Protocol.
        """

        """
        Run the Qiskrypt's Quantum Key Exchange Protocol.
        """
        super().run()

    def prepare_quantum_states(self):
        """
        Prepare the Quantum States for the
        Qiskrypt's Semi-Quantum Conference Key Agreement (SQCKA).
        """

        """
        Raise a Not Implemented Error since this abstract method
        should be implemented in its sub-classes.
        """
        # TODO Throw - Exception

    def transmit_quantum_states(self):
        """
        Transmit the Quantum States for the
        Qiskrypt's Semi-Quantum Conference Key Agreement (SQCKA).
        """

        """
        Raise a Not Implemented Error since this abstract method
        should be implemented in its sub-classes.
        """
        # TODO Throw - Exception

    def measure_quantum_states(self):
        """
        Measure the Quantum States for the
        Qiskrypt's Semi-Quantum Conference Key Agreement (SQCKA).
        """

        """
        Raise a Not Implemented Error since this abstract method
        should be implemented in its sub-classes.
        """
        # TODO Throw - Exception

    def sift_raw_key(self):
        """
        Sift the Secret Key for the
        Qiskrypt's Semi-Quantum Conference Key Agreement (SQCKA).
        """

        """
        Raise a Not Implemented Error since this abstract method
        should be implemented in its sub-classes.
        """
        # TODO Throw - Exception

    def estimate_parameters(self):
        """
        Estimate the Parameters for the
        Qiskrypt's Semi-Quantum Conference Key Agreement (SQCKA).
        """

        """
        Raise a Not Implemented Error since this abstract method
        should be implemented in its sub-classes.
        """
        # TODO Throw - Exception

    def reconcile_information(self):
        """
        Reconcile the Information for the
        Qiskrypt's Semi-Quantum Conference Key Agreement (SQCKA).
        """

        """
        Raise a Not Implemented Error since this abstract method
        should be implemented in its sub-classes.
        """
        # TODO Throw - Exception

    def amplify_privacy(self):
        """
        Amplify the Privacy for the
        Qiskrypt's Semi-Quantum Conference Key Agreement (SQCKA).
        """

        """
        Raise a Not Implemented Error since this abstract method
        should be implemented in its sub-classes.
        """
        # TODO Throw - Exception
