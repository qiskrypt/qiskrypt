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

from logging import basicConfig as logging_basic_configuration
"""
Import the Basic Configuration for the logger of messages.
"""

from logging import getLogger as get_logger
"""
Import the function to retrieve the logger with the specified given name.
"""

from logging import WARNING
"""
Import the 'WARNING' severity level for the logger of messages.
"""

from logging import INFO
"""
Import the 'INFO' severity level for the logger of messages.
"""

from logging import info as logger_info_message
"""
Import the logger of 'INFO' messages.
"""

from hashlib import sha256 as sha_256
"""
Import the SHA-256 (Secure-Hash Algorithm for 256 bits) from
the Python's HashLib.
"""

from copy import deepcopy as deep_copy
"""
Import the Deep Copy method from
the Copy module from the Python's Library.
"""

from qiskit import Aer as aer
"""
Import Aer Simulator from IBM's Qiskit.
"""

from qiskit import execute
"""
Import the execute function from IBM's Qiskit.
"""

from src.classical_regime.common.QiskryptClassicalUtilities \
    import QiskryptClassicalUtilities
"""
Import the Qiskrypt's Classical Utilities.
"""

from src.classical_regime.utils.geographic.QiskryptGeocoding \
    import QiskryptGeocoding
"""
Import Qiskrypt's Geocoding.
"""

from src.classical_regime.utils.geographic.QiskryptGeographicAddressEnumeration \
    import QiskryptGeographicAddressEnumeration
"""
Import the Qiskrypt's Geographic Address Enumeration.
"""

from src.quantum_regime.cryptography.key_exchange.semi_quantum_conference_key_agreement.dv \
    .entanglement_based.bkmps22.common.QiskryptDVBKMPS22Protocol \
    import QiskryptDVBKMPS22Protocol
"""
Import the Qiskrypt's DV (Discrete Variables) BKMPS22 Protocol.
"""

from src.quantum_regime.cryptography.key_exchange \
    .semi_quantum_conference_key_agreement.dv.entanglement_based.bkmps22.noiseless \
    .with_no_eavesdropping.QiskryptNoiselessDVBKMPS22ProtocolWithNoEavesdroppingQuantumTransmissionPhaseRound \
    import QiskryptNoiselessDVBKMPS22ProtocolWithNoEavesdroppingQuantumTransmissionPhaseRound
"""
Import the Qiskrypt's DV (Discrete Variables) BKMPS22 Protocol
with No Eavesdropping Quantum Transmission Phase Round.
"""

from src.quantum_regime.cryptography.common.keys \
    .symmetric.secret.types.QiskryptSecretRawKey \
    import QiskryptSecretRawKey
"""
Import the Qiskrypt's Secret Raw Key.
"""

from src.quantum_regime.cryptography.common.keys \
    .symmetric.secret.types.QiskryptSecretSiftedKey \
    import QiskryptSecretSiftedKey
"""
Import the Qiskrypt's Secret Sifted Key.
"""

from src.quantum_regime.cryptography.common.keys \
    .symmetric.secret.types.QiskryptSecretReconciledKey \
    import QiskryptSecretReconciledKey
"""
Import the Qiskrypt's Secret Reconciled Key.
"""

from src.quantum_regime.cryptography.common.keys \
    .symmetric.secret.types.QiskryptSecretSecureKey \
    import QiskryptSecretSecureKey
"""
Import the Qiskrypt's Secret Secure Key.
"""

from src.quantum_regime.networking_and_communications.essentials.QiskryptEntity \
    import QiskryptEntity
"""
Import the Qiskrypt's Entity.
"""

from src.quantum_regime.networking_and_communications.essentials.QiskryptParty \
    import QiskryptParty
"""
Import the Qiskrypt's Party.
"""

from src.quantum_regime.networking_and_communications.endpoints \
    .ground_station.quantum.fully_quantum.QiskryptFullyQuantumGroundStationEndpoint \
    import QiskryptFullyQuantumGroundStationEndpoint
"""
Import the Qiskrypt's Fully-Quantum Ground Station Endpoint.
"""

from src.quantum_regime.networking_and_communications.endpoints \
    .ground_station.quantum.semi_quantum.QiskryptSemiQuantumGroundStationEndpoint \
    import QiskryptSemiQuantumGroundStationEndpoint
"""
Import the Qiskrypt's Semi-Quantum Ground Station Endpoint.
"""

from src.quantum_regime.networking_and_communications.endpoints \
    .ground_station.classical.QiskryptClassicalGroundStationEndpoint \
    import QiskryptClassicalGroundStationEndpoint
"""
Import the Qiskrypt's Classical Ground Station Endpoint.
"""

from src.quantum_regime.networking_and_communications.clients.types.QiskryptPartyClient \
    import QiskryptPartyClient
"""
Import the Qiskrypt's Party Client.
"""

from src.quantum_regime.circuit.registers.quantum.fully_quantum.QiskryptFullyQuantumRegister \
    import QiskryptFullyQuantumRegister
"""
Import the Qiskrypt's Fully-Quantum Register.
"""

from src.quantum_regime.circuit.registers.quantum.semi_quantum.QiskryptSemiQuantumRegister \
    import QiskryptSemiQuantumRegister
"""
Import the Qiskrypt's Semi-Quantum Register.
"""

from src.quantum_regime.circuit.registers.classical.QiskryptClassicalRegister \
    import QiskryptClassicalRegister
"""
Import the Qiskrypt's Classical Register.
"""

from src.quantum_regime.circuit.QiskryptQuantumCircuit \
    import QiskryptQuantumCircuit
"""
Import the Qiskrypt's Quantum Circuit.
"""

from src.quantum_regime.networking_and_communications.mediums.types.QiskryptFiberOpticMedium \
    import QiskryptFiberOpticMedium
"""
Import the Qiskrypt's Fiber Optic Medium.
"""

from src.quantum_regime.networking_and_communications.channels.quantum \
    .discrete_variables.noiseless.types.QiskryptUnicastNoiselessDVQuantumCommunicationChannel \
    import QiskryptUnicastNoiselessDVQuantumCommunicationChannel
"""
Import the Qiskrypt's Unicast Noiseless DV (Discrete Variables) Quantum Communication Channel.
"""

from src.quantum_regime.networking_and_communications.links.QiskryptLink \
    import QiskryptLink
"""
Import the Qiskrypt's Link.
"""

from src.quantum_regime.networking_and_communications \
    .sessions.QiskryptCommunicationSession \
    import QiskryptCommunicationSession
"""
Import the Qiskrypt's Communication Session.
"""

from src.quantum_regime.true_random.coin_tossing.QiskryptQuantumCoinTossing \
    import QiskryptQuantumCoinTossing
"""
Import the Qiskrypt's Quantum Coin Tossing.
"""

from src.quantum_regime.true_random.random_generator \
    .numeric.QiskryptQuantumRandomNumericGenerator \
    import QiskryptQuantumRandomNumericGenerator
"""
Import the Qiskrypt's Quantum Random Numeric Generator.
"""

from src.quantum_regime.networking_and_communications.clients.QiskryptClient \
    import POSSIBLE_CLIENT_ROLES
"""
Import the available roles for the Qiskrypt's Client.
"""

from src.quantum_regime.networking_and_communications \
    .channels.QiskryptCommunicationChannel \
    import POSSIBLE_COMMUNICATION_CHANNEL_DIRECTIONS
"""
Import the available Communication Channel directions for
the Qiskrypt's Communication Channel.
"""

from src.quantum_regime.cryptography.QiskryptQuantumCryptographicPrimitive \
    import POSSIBLE_QUANTUM_CRYPTOGRAPHIC_PRIMITIVE_SCENARIOS
"""
Import the available Quantum Cryptographic Primitive scenarios for
the Qiskrypt's Quantum Cryptographic Primitives.
"""

from src.quantum_regime.cryptography.key_exchange \
    .semi_quantum_conference_key_agreement.QiskryptSemiQuantumConferenceKeyAgreement \
    import MINIMUM_SEMI_QUANTUM_CONFERENCE_KEY_AGREEMENT_NUM_PARTIES
"""
Import the minimum number of parties for
the Qiskrypt's Semi-Quantum Conference Key Agreement (SQCKA).
"""

from src.quantum_regime.cryptography.key_exchange \
    .semi_quantum_conference_key_agreement.QiskryptSemiQuantumConferenceKeyAgreement \
    import DEFAULT_SEMI_QUANTUM_CONFERENCE_KEY_AGREEMENT_NUM_PARTIES
"""
Import the default number of parties for
the Qiskrypt's Semi-Quantum Conference Key Agreement (SQCKA).
"""

from src.quantum_regime.cryptography.key_exchange \
    .semi_quantum_conference_key_agreement.QiskryptSemiQuantumConferenceKeyAgreement \
    import SEMI_QUANTUM_CONFERENCE_KEY_AGREEMENT_DEFAULT_PARTIES_NAMES
"""
Import the default parties' names for
the Qiskrypt's Semi-Quantum Conference Key Agreement (SQCKA).
"""

from src.quantum_regime.cryptography.key_exchange.semi_quantum_conference_key_agreement \
    .dv.entanglement_based.bkmps22.common.QiskryptDVBKMPS22Protocol \
    import DV_BKMPS22_PROTOCOL_DEFAULT_NUM_ROUNDS_FOR_QUANTUM_TRANSMISSION_PHASE
"""
Import the default number of rounds for the Quantum Transmission Phase of
the Qiskrypt's DV (Discrete Variable) BKMPS22 Protocol.
"""

from src.quantum_regime.cryptography.key_exchange.semi_quantum_conference_key_agreement \
    .dv.entanglement_based.bkmps22.common.QiskryptDVBKMPS22Protocol \
    import DV_BKMPS22_PROTOCOL_DEFAULT_FACTOR_FOR_NUM_ROUNDS_OF_PARAMETER_ESTIMATION_SAMPLE
"""
Import the default factor for the number of rounds for the Parameter Estimation Sample of
the Qiskrypt's DV (Discrete Variable) BKMPS22 Protocol.
"""

from src.quantum_regime.cryptography.key_exchange.semi_quantum_conference_key_agreement \
    .dv.entanglement_based.bkmps22.common.QiskryptDVBKMPS22ProtocolRound \
    import POSSIBLE_DV_BKMPS22_PROTOCOL_ROUND_TYPES_QUANTUM_TRANSMISSION_PHASE
"""
Import the available DV (Discrete Variables) BKMPS22 Protocol Round types for
the Qiskrypt's DV (Discrete Variables) BKMPS22 Protocol.
"""

from src.quantum_regime.cryptography.common.keys.QiskryptKey \
    import POSSIBLE_KEY_PRIVACY_LEVELS
"""
Import the available privacy levels of keys for the Qiskrypt's Key.
"""

from src.quantum_regime.cryptography.common.keys.QiskryptKey \
    import POSSIBLE_KEY_TYPES
"""
Import the available types of keys for the Qiskrypt's Key.
"""

from src.quantum_regime.true_random \
    .random_generator.numeric.QiskryptQuantumRandomNumericGenerator \
    import DATA_TYPES
"""
Import the Data Types for all the numbers that can be possibly generated
from the Qiskrypt's Quantum Random Numeric Generator.
"""

from src.classical_regime.common.QiskryptClassicalUtilities \
    import BINARY_FORMAT_START_OFFSET
"""
Import the offset for the start of the Python's binary format.
"""


class QiskryptNoiselessDVBKMPS22ProtocolWithNoEavesdropping \
            (QiskryptDVBKMPS22Protocol):
    """
    Object class for the Qiskrypt's Noiseless DV (Discrete Variables)
    BKMPS22 Protocol with No Eavesdropping.
    """

    def __init__(self, sender_name=SEMI_QUANTUM_CONFERENCE_KEY_AGREEMENT_DEFAULT_PARTIES_NAMES[0].lower(),
                 receivers_names=None,
                 sender_address=QiskryptGeographicAddressEnumeration
                 .NOVA_SCHOOL_OF_SCIENCE_AND_TECHNOLOGY_PORTUGAL.value,
                 receivers_addresses=None,
                 num_rounds_for_quantum_transmission_phase=DV_BKMPS22_PROTOCOL_DEFAULT_NUM_ROUNDS_FOR_QUANTUM_TRANSMISSION_PHASE,
                 verbose=True):
        """
        Constructor of the Qiskrypt's Noiseless DV (Discrete Variables)
        BKMPS22 Protocol with No Eavesdropping.

        :param sender_name: the name of the sender in the Qiskrypt's Noiseless DV (Discrete Variables)
                            BKMPS22 Protocol with No Eavesdropping.
        :param receivers_names: the names of the receivers in the Qiskrypt's Noiseless DV (Discrete Variables)
                                BKMPS22 Protocol with No Eavesdropping.
        :param sender_address: the address of the sender in the Qiskrypt's Noiseless DV (Discrete Variables)
                               BKMPS22 Protocol with No Eavesdropping.
        :param receivers_addresses: the addresses of the receivers in the Qiskrypt's Noiseless DV (Discrete Variables)
                                    BKMPS22 Protocol with No Eavesdropping.
        :param num_rounds_for_quantum_transmission_phase: the number of rounds for
                                                          the Quantum Transmission Phase in
                                                          the Qiskrypt's Quantum Key Exchange Protocol.
        :param verbose: the boolean flag to show the runtime information about
                        the Qiskrypt's Quantum Cryptographic Primitive.

        """

        super().__init__(POSSIBLE_QUANTUM_CRYPTOGRAPHIC_PRIMITIVE_SCENARIOS[0],
                         num_rounds_for_quantum_transmission_phase, verbose)
        """
        Call of the constructor of the super-class Qiskrypt's DV (Discrete Variable) BKMPS22 Protocol.
        """

        self.sender_name = sender_name
        """
        Set the name of the sender in the Qiskrypt's Noiseless DV (Discrete Variables)
        BKMPS22 Protocol with No Eavesdropping.
        """

        if receivers_names is None:
            """
            If no list of the names of the receivers in the Qiskrypt's Noiseless DV (Discrete Variables)
            BKMPS22 Protocol with No Eavesdropping is given.
            """

            self.receivers_names = \
                self.create_default_receivers_names(
                    num_receivers=DEFAULT_SEMI_QUANTUM_CONFERENCE_KEY_AGREEMENT_NUM_PARTIES
                )
            """
            Set the names of the receivers in the Qiskrypt's Noiseless DV (Discrete Variables)
            BKMPS22 Protocol with No Eavesdropping.
            """

        else:
            """
            If some list of the names of the receivers in the Qiskrypt's Noiseless DV (Discrete Variables)
            BKMPS22 Protocol with No Eavesdropping is given.
            """

            if len(receivers_names) >= (MINIMUM_SEMI_QUANTUM_CONFERENCE_KEY_AGREEMENT_NUM_PARTIES - 1):
                """
                If the size of the given list of the names of the receivers in the Qiskrypt's
                Noiseless DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping is greater or equal to
                the minimum number of parties for the Qiskrypt's Semi-Quantum Conference Key Agreement (SQCKA).
                """

                self.receivers_names = receivers_names
                """
                Set the names of the receivers in the Qiskrypt's
                Noiseless DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
                """

            else:
                """
                If the size of the given list of the names of the receivers in the Qiskrypt's
                Noiseless DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping is lower than
                the minimum number of parties for the Qiskrypt's Semi-Quantum Conference Key Agreement (SQCKA).
                """

                # TODO - Throw Exception

        self.sender_address = sender_address
        """
        Set the address of the sender in the Qiskrypt's Noiseless DV (Discrete Variables)
        BKMPS22 Protocol with No Eavesdropping.
        """

        if receivers_addresses is None:
            """
            If no list of the addresses of the receivers in the Qiskrypt's Noiseless DV (Discrete Variables)
            BKMPS22 Protocol with No Eavesdropping is given.
            """

        else:
            """
            If some list of the addresses of the receivers in the Qiskrypt's Noiseless DV (Discrete Variables)
            BKMPS22 Protocol with No Eavesdropping is given.
            """

        self.receivers_addresses = receivers_addresses
        """
        Set the addresses of the receiver in the Qiskrypt's Noiseless DV (Discrete Variables)
        BKMPS22 Protocol with No Eavesdropping.
        """

        if self.is_verbose():
            """
            If the boolean flag to show the runtime information about
            the Qiskrypt's Quantum Cryptographic Primitive, is set as True.
            """

            logging_basic_configuration(level=INFO)
            """
            Start the Basic Configuration for the logger of messages,
            with the 'INFO' severity level.
            """

            get_logger("qiskit").setLevel(level=WARNING)
            """
            Set the 'WARNING' severity level for the logger of the IBM Qiskit.
            """

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

    def start_quantum_transmission_phase(self):
        """
        Start the Quantum Transmission Phase of the
        Qiskrypt's Quantum Key Exchange Protocol.
        """

        QiskryptClassicalUtilities.waiting_animation()
        """
        Call the waiting animation from the Qiskrypt's Classical Utilities.
        """

        logger_info_message(" 2) Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol\n"
                            "              starts its Quantum Transmission Phase...")
        """
        Log an 'INFO' message for the Qiskrypt's Noiseless DV (Discrete Variables)
        starts its Quantum Transmission Phase.
        """

        super().start_quantum_transmission_phase()
        """
        Start the Quantum Transmission Phase of the
        Qiskrypt's Quantum Key Exchange Protocol.
        """

        logger_info_message(" 2) Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol\n"
                            "              finishes its Quantum Transmission Phase...")
        """
        Log an 'INFO' message for the Qiskrypt's Noiseless DV (Discrete Variables)
        finishes its Quantum Transmission Phase.
        """

    def start_classical_post_processing_phase(self):
        """
        Start the Classical Post-Processing Phase of the
        Qiskrypt's Quantum Key Exchange Protocol.
        """

        QiskryptClassicalUtilities.waiting_animation()
        """
        Call the waiting animation from the Qiskrypt's Classical Utilities.
        """

        logger_info_message(" 3) Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol\n"
                            "              starts its Classical Post-Processing Phase...")
        """
        Log an 'INFO' message for the Qiskrypt's Noiseless DV (Discrete Variables)
        starts its Classical Post-Processing Phase.
        """

        super().start_classical_post_processing_phase()
        """
        Start the Classical Post-Processing Phase of the
        Qiskrypt's Quantum Key Exchange Protocol.
        """

        logger_info_message(" 3) Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol\n"
                            "              finishes its Classical Post-Processing Phase...")
        """
        Log an 'INFO' message for the Qiskrypt's Noiseless DV (Discrete Variables)
        finishes its Classical Post-Processing Phase.
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

        NOTES:
        - For the DV (Discrete Variables) BKMPS22 Protocol, the preparation of
          the photons being transmitted is based on the secret bits generated and random bases
          generated by the sender, which are described in the following table:

           __________________________________________________________________________________
          | Secret Bit | Random Basis  | Polarization |            Quantum State             |
          |     for    |    for the    |   for the    |         resulting from the           |
          |  Sender's  |  Preparation  | Preparation  |       Preparation of Photons         |
          |   Raw Key  |  of Photons   | of Photons   |                                      |
          |____________|_______________|______________|______________________________________|
          |     0      |    Z-Basis    |       0º     |            |0⟩  (or |H⟩)             |
          |____________|_______________|______________|______________________________________|
          |     0      |    X-Basis    |      45º     |    |+⟩ = 1 / sqrt(2) x (|0⟩ + |1⟩)   |
          |            |               |              | (or, |D⟩ = 1 / sqrt(2) x (|H⟩ + |V⟩) |
          |____________|_______________|______________|______________________________________|
          |     1      |    Z-Basis    |      90º     |            |1⟩  (or |V⟩)             |
          |____________|_______________|______________|______________________________________|
          |     1      |    X-Basis    |     135º     |    |-⟩ = 1 / sqrt(2) x (|0⟩ - |1⟩)   |
          |            |               |              | (or, |A⟩ = 1 / sqrt(2) x (|H⟩ - |V⟩) |
          |____________|_______________|______________|______________________________________|

        """

        if self.is_configured():
            """
            If the Qiskrypt's Key Exchange Protocol is already configured.
            """

            logger_info_message(
                "    2.1) Starting the preparation of the outgoing photons for\n"
                "                   the Quantum Transmission Phase of the Qiskrypt's Noiseless\n"
                "                   DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping..."
            )
            """
            Log an 'INFO' message for the start of the procedure of the preparation of
            the outgoing photons for the Quantum Transmission Phase of the Qiskrypt's Noiseless
            DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
            """

            sender_party_client = \
                self.get_communication_session().get_sender_party_clients()[0]
            """
            Retrieve the sender Qiskrypt's Party Client of
            the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
            """

            receiver_party_client = \
                self.get_communication_session().get_receiver_party_clients()[0]
            """
            Retrieve the receiver Qiskrypt's Party Client of
            the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
            """

            if isinstance(sender_party_client, QiskryptPartyClient) and \
                    isinstance(receiver_party_client, QiskryptPartyClient):
                """
                If the sender and receiver Qiskrypt's Party Clients of
                the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol
                with No Eavesdropping are really Qiskrypt's Party Clients.
                """

                sender_raw_key_secret_bits = "0b"
                """
                Initialise the binary string for the bits used to build
                the Qiskrypt's Secret Raw Key of the sender Qiskrypt's Party Client.
                """

                num_rounds_for_quantum_transmission_phase = \
                    self.get_num_rounds_for_quantum_transmission_phase()
                """
                Retrieve the number of rounds for the Quantum Transmission Phase in
                the Qiskrypt's Quantum Key Exchange Protocol.
                """

                quantum_transmission_phase_rounds = \
                    self.get_quantum_transmission_phase_rounds()
                """
                Retrieve the list for the Quantum Transmission Phase of 
                the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
                """

                for current_num_round_for_quantum_transmission_phase in \
                        range(num_rounds_for_quantum_transmission_phase):
                    """
                    For each round of the Quantum Transmission Phase of 
                    the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
                    """

                    logger_info_message(
                        "    2.1.{}) {} preparing the photon of the round no. {} for\n"
                        "                     the Quantum Transmission Phase of the Qiskrypt's Noiseless\n"
                        "                     DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping..."
                        .format((current_num_round_for_quantum_transmission_phase + 1),
                                sender_party_client.get_party().get_name().upper(),
                                (current_num_round_for_quantum_transmission_phase + 1)))
                    """
                    Log an 'INFO' message for the preparation of the current photon for
                    the Quantum Transmission Phase of the Qiskrypt's Noiseless
                    DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
                    """

                    current_round_for_quantum_transmission_phase = \
                        quantum_transmission_phase_rounds[current_num_round_for_quantum_transmission_phase]
                    """
                    Retrieve the current round of the Quantum Transmission Phase of 
                    the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
                    """

                    if isinstance(current_round_for_quantum_transmission_phase,
                                  QiskryptNoiselessDVBKMPS22ProtocolWithNoEavesdroppingQuantumTransmissionPhaseRound):
                        """
                        If the current round of the Quantum Transmission Phase of 
                        the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping is
                        really a Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol
                        with No Eavesdropping Quantum Transmission Phase Round.
                        """

                        current_round_quantum_circuit_for_quantum_transmission_phase = \
                            current_round_for_quantum_transmission_phase.get_round_quantum_circuit()
                        """
                        Retrieve the Qiskrypt's Quantum Circuit for the current round of
                        the Quantum Transmission Phase of the Qiskrypt's Noiseless
                        DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
                        """

                        if isinstance(current_round_quantum_circuit_for_quantum_transmission_phase,
                                      QiskryptQuantumCircuit):
                            """
                            If the Qiskrypt's Quantum Circuit for the current round of
                            the Quantum Transmission Phase of the Qiskrypt's Noiseless DV (Discrete Variables)
                            BKMPS22 Protocol with No Eavesdropping is really a Qiskrypt's Quantum Circuit.
                            """

                            current_secret_bit_sender = \
                                current_round_quantum_circuit_for_quantum_transmission_phase \
                                .get_qiskrypt_classical_register(0).get_bit(0)
                            """
                            Retrieve the Secret Bit from the sender's Qiskrypt's Classical Register from
                            the Qiskrypt's Quantum Circuit for the current round of the Quantum Transmission Phase of 
                            the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
                            """

                            current_round_type_for_quantum_transmission_phase = \
                                current_round_for_quantum_transmission_phase \
                                .get_quantum_key_exchange_protocol_round_type()
                            """
                            Retrieve the type of the current round of the Quantum Transmission Phase of 
                            the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
                            """

                            sender_raw_key_secret_bits += str(current_secret_bit_sender)
                            """
                            Append the current secret bit to the binary string for the bits used to
                            build the Qiskrypt's Secret Raw Key of the sender Qiskrypt's Party Client,
                            according to the randomly chosen value for it.
                            """

                            if current_secret_bit_sender == 0:
                                """
                                If the Secret Bit from the sender's Qiskrypt's Classical Register from
                                the Qiskrypt's Quantum Circuit for the photon of the current round of
                                the Quantum Transmission Phase of the Qiskrypt's Noiseless DV (Discrete Variables)
                                BKMPS22 Protocol with No Eavesdropping is equal to zero (0), which will correspond to
                                a photon polarization of 0 or 45 degrees (also known as Horizontal or 
                                Diagonal polarizations, respectively).
                                """

                                if current_round_type_for_quantum_transmission_phase == \
                                        POSSIBLE_DV_BKMPS22_PROTOCOL_ROUND_TYPES_QUANTUM_TRANSMISSION_PHASE[0]:
                                    """
                                    If the current round of the Quantum Transmission Phase of 
                                    the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol
                                    with No Eavesdropping is a 'Z-BASIS ROUND', the sender will prepare
                                    the photon with a polarization of 0 degrees (also known as Horizontal
                                    polarization) corresponding to the Quantum State |0⟩ (or, |H⟩ in
                                    the notation of Jones Calculus), equivalent to the classical bit 0.
                                    """

                                    if not current_round_for_quantum_transmission_phase \
                                            .is_round_operation_sender_choice_made():
                                        """
                                        If the operation choice made by the sender in 
                                        the Qiskrypt's DV (Discrete Variables) BKMPS22 Protocol Round is not set yet.
                                        """

                                        current_round_for_quantum_transmission_phase \
                                            .set_round_operation_sender_choice(
                                                POSSIBLE_DV_BKMPS22_PROTOCOL_ROUND_TYPES_QUANTUM_TRANSMISSION_PHASE[0]
                                                .split(" ")[0]
                                            )
                                        """
                                        Set the operation choice made by the sender in
                                        the Qiskrypt's DV (Discrete Variables) BKMPS22 Protocol Round as 'Z-BASIS'.
                                        """

                                        current_round_quantum_circuit_for_quantum_transmission_phase \
                                            .apply_pauli_i(0, 0)
                                        """
                                        Apply the Pauli-I (Idle) Gate/Operation to the qubit in
                                        the Qiskrypt's Quantum Register of the sender's Qiskrypt's Party Client of
                                        the Qiskrypt's Quantum Circuit for the current round of
                                        the Quantum Transmission Phase of the Qiskrypt's Noiseless
                                        DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
                                        """

                                        current_round_quantum_circuit_for_quantum_transmission_phase \
                                            .prepare_and_measure_single_qubit_in_qiskit_quantum_register_in_z_basis \
                                            (0, 0, 0, 0, False)
                                        """
                                        Prepare the qubit in the sender's Qiskrypt's Quantum Register of
                                        the Qiskrypt's Quantum Circuit of the current round of
                                        the Quantum Transmission Phase of the Qiskrypt's Noiseless
                                        DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping in
                                        the Z-Basis (Standard Computational Basis), without measuring it.
                                        """

                                    else:
                                        """
                                        If the basis choice made by the sender in
                                        the Qiskrypt's DV (Discrete Variables) BKMPS22 Protocol Round is already set.
                                        """

                                        # TODO Throw - Exception

                                elif current_round_type_for_quantum_transmission_phase == \
                                        POSSIBLE_DV_BKMPS22_PROTOCOL_ROUND_TYPES_QUANTUM_TRANSMISSION_PHASE[1]:
                                    """
                                    If the current round of the Quantum Transmission Phase of 
                                    the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol
                                    with No Eavesdropping is a 'X-BASIS ROUND', the sender will prepare
                                    the photon with a polarization of 45 degrees (also known as Diagonal
                                    polarization) corresponding to the Quantum State |+⟩ = 1 / sqrt(2) x (|0⟩ + |1⟩)
                                    (or, |D⟩ = 1 / sqrt(2) x (|H⟩ + |V⟩) in the notation of Jones Calculus),
                                    equivalent to a quantum superposition of states representing
                                    the classical bits 0 and 1, in phase.
                                    """

                                    if not current_round_for_quantum_transmission_phase \
                                            .is_round_operation_sender_choice_made():
                                        """
                                        If the operation choice made by the sender in
                                        the Qiskrypt's DV (Discrete Variables) BKMPS22 Protocol Round is not set yet.
                                        """

                                        current_round_for_quantum_transmission_phase \
                                            .set_round_operation_sender_choice(
                                                POSSIBLE_DV_BKMPS22_PROTOCOL_ROUND_TYPES_QUANTUM_TRANSMISSION_PHASE[1]
                                                .split(" ")[0]
                                            )
                                        """
                                        Set the operation choice made by the sender in
                                        the Qiskrypt's DV (Discrete Variables) BKMPS22 Protocol Round as 'X-BASIS'.
                                        """

                                        current_round_quantum_circuit_for_quantum_transmission_phase \
                                            .apply_pauli_i(0, 0)
                                        """
                                        Apply the Pauli-I (Idle) Gate/Operation to the qubit in
                                        the Qiskrypt's Quantum Register of the sender's Qiskrypt's Party Client of
                                        the Qiskrypt's Quantum Circuit for the current round of
                                        the Quantum Transmission Phase of the Qiskrypt's Noiseless
                                        DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
                                        """

                                        current_round_quantum_circuit_for_quantum_transmission_phase \
                                            .prepare_and_measure_single_qubit_in_qiskit_quantum_register_in_x_basis \
                                            (0, 0, 0, 0, False)
                                        """
                                        Prepare the qubit in the Qiskrypt's Quantum Register of
                                        the sender's Qiskrypt's Party Client regarding
                                        the Qiskrypt's Quantum Circuit of the current round of
                                        the Quantum Transmission Phase of the Qiskrypt's Noiseless
                                        DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping in
                                        the X-Basis (Hadamard Basis), without measuring it.
                                        """

                                    else:
                                        """
                                        If the basis choice made by the sender in
                                        the Qiskrypt's DV (Discrete Variables) BKMPS22 Protocol Round is already set.
                                        """

                                        # TODO Throw - Exception

                            elif current_secret_bit_sender == 1:
                                """
                                If the Secret Bit from the sender's Qiskrypt's Classical Register from
                                the Qiskrypt's Quantum Circuit for the current round of
                                the Quantum Transmission Phase of the Qiskrypt's Noiseless
                                DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping is
                                equal to one (1), which will correspond to a photon polarization of
                                90 or 135 degrees (also known as Vertical or Anti-Diagonal
                                polarizations, respectively).
                                """

                                if current_round_type_for_quantum_transmission_phase == \
                                        POSSIBLE_DV_BKMPS22_PROTOCOL_ROUND_TYPES_QUANTUM_TRANSMISSION_PHASE[0]:
                                    """
                                    If the current round of the Quantum Transmission Phase of 
                                    the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol
                                    with No Eavesdropping is a 'Z-BASIS ROUND', the sender will prepare
                                    the photon with a polarization of 90 degrees (also known as Horizontal
                                    polarization) corresponding to the Quantum State |1⟩ (or, |V⟩ in
                                    the notation of Jones Calculus), equivalent to the classical bit 1.
                                    """

                                    if not current_round_for_quantum_transmission_phase \
                                            .is_round_operation_sender_choice_made():
                                        """
                                        If the operation choice made by the sender in
                                        the Qiskrypt's DV (Discrete Variables) BKMPS22 Protocol Round is not set yet.
                                        """

                                        current_round_for_quantum_transmission_phase \
                                            .set_round_operation_sender_choice(
                                                POSSIBLE_DV_BKMPS22_PROTOCOL_ROUND_TYPES_QUANTUM_TRANSMISSION_PHASE[0]
                                                .split(" ")[0]
                                            )
                                        """
                                        Set the basis choice made by the sender in
                                        the Qiskrypt's DV (Discrete Variables) BKMPS22 Protocol Round as 'Z-BASIS'.
                                        """

                                        current_round_quantum_circuit_for_quantum_transmission_phase \
                                            .apply_pauli_x(0, 0)
                                        """
                                        Apply the Pauli-X (NOT/Bit Flip) Gate/Operation to the qubit in
                                        the Qiskrypt's Quantum Register of the sender's Qiskrypt's Party Client of
                                        the Qiskrypt's Quantum Circuit for the current round of
                                        the Quantum Transmission Phase of the Qiskrypt's Noiseless
                                        DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
                                        """

                                        current_round_quantum_circuit_for_quantum_transmission_phase \
                                            .prepare_and_measure_single_qubit_in_qiskit_quantum_register_in_z_basis \
                                            (0, 0, 0, 0, False)
                                        """
                                        Prepare the qubit in the sender's Qiskrypt's Quantum Register of
                                        the Qiskrypt's Quantum Circuit of the current round of
                                        the Quantum Transmission Phase of the Qiskrypt's Noiseless
                                        DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping in
                                        the Z-Basis (Standard Computational Basis), without measuring it.
                                        """

                                    else:
                                        """
                                        If the basis choice made by the sender in
                                        the Qiskrypt's DV (Discrete Variables) BKMPS22 Protocol Round is already set.
                                        """

                                        # TODO Throw - Exception

                                elif current_round_type_for_quantum_transmission_phase == \
                                        POSSIBLE_DV_BKMPS22_PROTOCOL_ROUND_TYPES_QUANTUM_TRANSMISSION_PHASE[1]:
                                    """
                                    If the current round of the Quantum Transmission Phase of 
                                    the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol
                                    with No Eavesdropping is a 'X-BASIS ROUND', the sender will prepare
                                    the photon with a polarization of 135 degrees (also known as Diagonal
                                    polarization) corresponding to the Quantum State |-⟩ = 1 / sqrt(2) x (|0⟩ - |1⟩)
                                    (or, |A⟩ = 1 / sqrt(2) x (|H⟩ - |V⟩) in the notation of Jones Calculus),
                                    equivalent to a quantum superposition of states representing
                                    the classical bits 0 and 1, in anti-phase.
                                    """

                                    if not current_round_for_quantum_transmission_phase \
                                            .is_round_operation_sender_choice_made():
                                        """
                                        If the operation choice made by the sender in
                                        the Qiskrypt's DV (Discrete Variables) BKMPS22 Protocol Round is not set yet.
                                        """

                                        current_round_for_quantum_transmission_phase \
                                            .set_round_operation_sender_choice(
                                                POSSIBLE_DV_BKMPS22_PROTOCOL_ROUND_TYPES_QUANTUM_TRANSMISSION_PHASE[1]
                                                .split(" ")[0]
                                            )
                                        """
                                        Set the operation choice made by the sender in
                                        the Qiskrypt's DV (Discrete Variables) BKMPS22 Protocol Round as 'X-BASIS'.
                                        """

                                        current_round_quantum_circuit_for_quantum_transmission_phase \
                                            .apply_pauli_x(0, 0)
                                        """
                                        Apply the Pauli-X (NOT/Bit Flip) Gate/Operation to the qubit in
                                        the Qiskrypt's Quantum Register of the sender's Qiskrypt's Party Client of
                                        the Qiskrypt's Quantum Circuit for the current round of
                                        the Quantum Transmission Phase of the Qiskrypt's Noiseless
                                        DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
                                        """

                                        current_round_quantum_circuit_for_quantum_transmission_phase \
                                            .prepare_and_measure_single_qubit_in_qiskit_quantum_register_in_x_basis \
                                            (0, 0, 0, 0, False)
                                        """
                                        Prepare the qubit in the sender's Qiskrypt's Quantum Register of
                                        the Qiskrypt's Quantum Circuit of the current round of
                                        the Quantum Transmission Phase of the Qiskrypt's Noiseless
                                        DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping in
                                        the X-Basis (Hadamard Basis), without measuring it.
                                        """

                                    else:
                                        """
                                        If the basis choice made by the sender in
                                        the Qiskrypt's DV (Discrete Variables) BKMPS22 Protocol Round is already set.
                                        """

                                        # TODO Throw - Exception

                        else:
                            """
                            If the Qiskrypt's Quantum Circuit for the current round of
                            the Quantum Transmission Phase of the Qiskrypt's Noiseless
                            DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping is
                            not a Qiskrypt's Quantum Circuit.
                            """

                            # TODO Throw - Exception

                    else:
                        """
                        If the current round of the Quantum Transmission Phase of 
                        the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping is
                        not a Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol
                        with No Eavesdropping Quantum Transmission Phase Round.
                        """

                        # TODO Throw - Exception

                    sender_party_client_uuid = sender_party_client.get_uuid()
                    """
                    Retrieve the UUID (Universally Unique IDentifier) of the sender Qiskrypt's Client.
                    """

                    sender_secret_raw_key = QiskryptSecretRawKey(sender_raw_key_secret_bits,
                                                                 sender_party_client_uuid)
                    """
                    Create a Qiskrypt's Secret Raw Key for the sender Qiskrypt's Client.
                    """

                    sender_secret_raw_key_privacy_level = \
                        sender_secret_raw_key.get_key_privacy_level()
                    """
                    Retrieve the privacy level of the Qiskrypt's Key for the sender Qiskrypt's Client.
                    """

                    sender_secret_raw_key_type = \
                        sender_secret_raw_key.get_key_type()
                    """
                    Retrieve the type of the Qiskrypt's Key for the sender Qiskrypt's Client.
                    """

                    sender_party_name = sender_party_client.get_party().get_name()
                    """
                    Retrieve the name of the sender Qiskrypt's Party.
                    """

                    sender_party_num = sender_party_client.get_party().get_num()
                    """
                    Retrieve the number of the sender Qiskrypt's Party.                
                    """

                    receiver_party_name = receiver_party_client.get_party().get_name()
                    """
                    Retrieve the name of the receiver Qiskrypt's Party.
                    """

                    receiver_party_num = receiver_party_client.get_party().get_num()
                    """
                    Retrieve the number of the receiver Qiskrypt's Party.                
                    """

                    sender_secret_raw_key_id = \
                        "{} {} ({}_{} ; {}_{})".format(sender_secret_raw_key_privacy_level.lower(),
                                                       sender_secret_raw_key_type.lower(),
                                                       sender_party_name.lower(), sender_party_num,
                                                       receiver_party_name.lower(), receiver_party_num)
                    """
                    Set up the identifier of the Qiskrypt's Secret Raw Key for
                    the sender Qiskrypt's Client.
                    """

                    sender_party_client.add_item(sender_secret_raw_key_id, sender_secret_raw_key)
                    """
                    Add a new item to keep the Qiskrypt's Secret Raw Key for
                    the sender Qiskrypt's Client.
                    """

                    logger_info_message(
                        "    2.2) Finishing the preparation of the outgoing photons for\n"
                        "                   the Quantum Transmission Phase of the Qiskrypt's Noiseless\n"
                        "                   DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping..."
                    )
                    """
                    Log an 'INFO' message for the finish of the procedure of the preparation of
                    the outgoing photons for the Quantum Transmission Phase of the Qiskrypt's Noiseless
                    DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
                    """

            else:
                """
                If the sender and/or receiver Qiskrypt's Party Clients of
                the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol
                with No Eavesdropping are not Qiskrypt's Party Clients.
                """

                # TODO Throw - Exception

        else:
            """
            If the Qiskrypt's Key Exchange Protocol is not configured.
            """

            # TODO Throw - Exception

    def transmit_quantum_states(self):
        """
        Transmit the Quantum States for the
        Qiskrypt's Semi-Quantum Conference Key Agreement (SQCKA).
        """

        if self.is_configured():
            """
            If the Qiskrypt's Key Exchange Protocol is already configured.
            """

            logger_info_message(
                "    2.3) Starting the transmission of the photons for\n"
                "                   the Quantum Transmission Phase of the Qiskrypt's Noiseless\n"
                "                   DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping..."
            )
            """
            Log an 'INFO' message for the start of the procedure of the transmission of
            the photons for the Quantum Transmission Phase of the Qiskrypt's Noiseless
            DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
            """

            num_rounds_for_quantum_transmission_phase = \
                self.get_num_rounds_for_quantum_transmission_phase()
            """
            Retrieve the number of rounds for the Quantum Transmission Phase in
            the Qiskrypt's Quantum Key Exchange Protocol.
            """

            quantum_transmission_phase_rounds = \
                self.get_quantum_transmission_phase_rounds()
            """
            Retrieve the list for the Quantum Transmission Phase of 
            the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
            """

            for current_num_round_for_quantum_transmission_phase in \
                    range(num_rounds_for_quantum_transmission_phase):
                """
                For each round of the Quantum Transmission Phase of 
                the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
                """

                logger_info_message(
                    "    2.3.{}) Transmitting the photon of the round no. {} for\n"
                    "                     the Quantum Transmission Phase of the Qiskrypt's Noiseless\n"
                    "                     DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping..."
                    .format((current_num_round_for_quantum_transmission_phase + 1),
                            (current_num_round_for_quantum_transmission_phase + 1))
                )
                """
                Log an 'INFO' message for the preparation of the current photon for
                the Quantum Transmission Phase of the Qiskrypt's Noiseless
                DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
                """

                current_round_for_quantum_transmission_phase = \
                    quantum_transmission_phase_rounds[current_num_round_for_quantum_transmission_phase]
                """
                Retrieve the current round of the Quantum Transmission Phase of 
                the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
                """

                if isinstance(current_round_for_quantum_transmission_phase,
                              QiskryptNoiselessDVBKMPS22ProtocolWithNoEavesdroppingQuantumTransmissionPhaseRound):
                    """
                    If the current round of the Quantum Transmission Phase of 
                    the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping is
                    really a Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol
                    with No Eavesdropping Quantum Transmission Phase Round.
                    """

                    current_round_quantum_circuit_for_quantum_transmission_phase = \
                        current_round_for_quantum_transmission_phase.get_round_quantum_circuit()
                    """
                    Retrieve the Qiskrypt's Quantum Circuit for the current round of the Quantum Transmission Phase of 
                    the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
                    """

                    if isinstance(current_round_quantum_circuit_for_quantum_transmission_phase,
                                  QiskryptQuantumCircuit):
                        """
                        If the Qiskrypt's Quantum Circuit for the current round of the Quantum Transmission Phase of 
                        the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping is
                        really a Qiskrypt's Quantum Circuit.
                        """

                        current_round_quantum_circuit_for_quantum_transmission_phase.apply_swap(0, 1, 0, 0)
                        """
                        Apply the SWAP Gate/Operation between the qubits in
                        the Qiskrypt's Quantum Registers of the sender Qiskrypt's Party Client
                        and Qiskrypt's Link, respectively, of the Qiskrypt's Quantum Circuit for
                        the current round of the Quantum Transmission Phase of the Qiskrypt's Noiseless
                        DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
                        """

                        current_round_quantum_circuit_for_quantum_transmission_phase.apply_swap(1, 2, 0, 0)
                        """
                        Apply the SWAP Gate/Operation between the qubits in
                        the Qiskrypt's Quantum Registers of the Qiskrypt's Link
                        and receiver Qiskrypt's Party Client respectively,
                        of the Qiskrypt's Quantum Circuit for the current round of
                        the Quantum Transmission Phase of the Qiskrypt's Noiseless
                        DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
                        """

                    else:
                        """
                        If the Qiskrypt's Quantum Circuit for the current round of the Quantum Transmission Phase of 
                        the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping is
                        not a Qiskrypt's Quantum Circuit.
                        """

                        # TODO Throw - Exception

                else:
                    """
                    If the current round of the Quantum Transmission Phase of 
                    the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping is
                    not a Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol
                    with No Eavesdropping Quantum Transmission Phase Round.
                    """

                    # TODO Throw - Exception

            logger_info_message(
                "    2.4) Finishing the transmission of the photons for\n"
                "                   the Quantum Transmission Phase of the Qiskrypt's Noiseless\n"
                "                   DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping..."
            )
            """
            Log an 'INFO' message for the finish of the procedure of the transmission of
            the photons for the Quantum Transmission Phase of the Qiskrypt's Noiseless
            DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
            """

        else:
            """
            If the Qiskrypt's Key Exchange Protocol is not configured.
            """

            # TODO Throw - Exception

    def measure_quantum_states(self):
        """
        Measure the Quantum States for the
        Qiskrypt's Semi-Quantum Conference Key Agreement (SQCKA).

        NOTES:
        - For the DV (Discrete Variables) BKMPS22 Protocol, the measurements of
          the incoming photons is based on the random bases chosen by the receiver,
          resulting in several cases, which are described in the following table:

           _____________________________________________________________________________________________________
          | Random Basis  | Polarization | Random Basis  | Polarization |            Quantum State             |
          |    for the    |    for the   |    for the    |    for the   |       measured by the receiver       |
          |  Measurement  |  Measurement |  Preparation  |  Preparation |     and expected outcome bits for    |
          |  of Photons   |  of Photons  |  of Photons   |  of Photons  |         the respective case          |
          |_______________|______________|_______________|______________|______________________________________|
          |    Z-Basis    |      0º      |    Z-Basis    |   0º or 90º  |     |0⟩ or |1⟩  (or |H⟩ or |V⟩)      |
          |               |              |               |              |  (the outcome bit is expected to be  |
          |               |              |               |              |  ALWAYS correct and will be used to  |
          |               |              |               |              |    compose the secret sifted key)    |
          |               |              |_______________|______________|______________________________________|
          |               |              |    X-Basis    |  45º or 135º |     |+⟩ or |-⟩  (or |D⟩ or |A⟩)      |
          |               |              |               |              |   (the outcome bit is expected to    |
          |               |              |               |              |    be correct only in HALF times     |
          |               |              |               |              |      and will be discarded from      |
          |               |              |               |              |       the secret sifted key)         |
          |_______________|______________|_______________|______________|______________________________________|
          |    X-Basis    |     45º      |    Z-Basis    |   0º or 90º  |     |+⟩ or |-⟩  (or |D⟩ or |A⟩)      |
          |               |              |               |              |   (the outcome bit is expected to    |
          |               |              |               |              |    be correct only in HALF times     |
          |               |              |               |              |      and will be discarded from      |
          |               |              |               |              |       the secret sifted key)         |
          |               |              |_______________|______________|______________________________________|
          |               |              |    X-Basis    |  45º or 135º |     |0⟩ or |1⟩  (or |H⟩ or |V⟩)      |
          |               |              |               |              |  (the outcome bit is expected to be  |
          |               |              |               |              |  ALWAYS correct and will be used to  |
          |               |              |               |              |    compose the secret sifted key)    |
          |_______________|______________|_______________|______________|______________________________________|

        """

        if self.is_configured():
            """
            If the Qiskrypt's Key Exchange Protocol is already configured.
            """

            logger_info_message(
                "    2.5) Starting the measurement of the incoming photons for\n"
                "                   the Quantum Transmission Phase of the Qiskrypt's Noiseless\n"
                "                   DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping..."
            )
            """
            Log an 'INFO' message for the start of the procedure of the measurement of
            the incoming photons for the Quantum Transmission Phase of the Qiskrypt's Noiseless
            DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
            """

            receiver_party_client = \
                self.get_communication_session().get_receiver_party_clients()[0]
            """
            Retrieve the receiver Qiskrypt's Party Client from the Qiskrypt's Communication Session of
            the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
            """

            sender_party_client = \
                self.get_communication_session().get_sender_party_clients()[0]
            """
            Retrieve the sender Qiskrypt's Party Client from the Qiskrypt's Communication Session of
            the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
            """

            if isinstance(receiver_party_client, QiskryptPartyClient) and \
                    isinstance(sender_party_client, QiskryptPartyClient):
                """
                If the receiver and sender Qiskrypt's Party Clients of
                the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol
                with No Eavesdropping are really Qiskrypt's Party Clients.
                """

                receiver_raw_key_secret_bits = "0b"
                """
                Initialise the binary string for the bits used to build
                the Qiskrypt's Secret Raw Key of the receiver Qiskrypt's Party Client.
                """

                num_rounds_for_quantum_transmission_phase = \
                    self.get_num_rounds_for_quantum_transmission_phase()
                """
                Retrieve the number of rounds for the Quantum Transmission Phase in
                the Qiskrypt's Quantum Key Exchange Protocol.
                """

                quantum_transmission_phase_rounds = \
                    self.get_quantum_transmission_phase_rounds()
                """
                Retrieve the list for the Quantum Transmission Phase of 
                the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
                """

                for current_num_round_for_quantum_transmission_phase in \
                        range(num_rounds_for_quantum_transmission_phase):
                    """
                    For each round of the Quantum Transmission Phase of 
                    the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
                    """

                    logger_info_message(
                        "    2.5.{}) {} measuring the photon of the round no. {} for\n"
                        "                     the Quantum Transmission Phase of the Qiskrypt's Noiseless\n"
                        "                     DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping..."
                        .format((current_num_round_for_quantum_transmission_phase + 1),
                                receiver_party_client.get_party().get_name().upper(),
                                (current_num_round_for_quantum_transmission_phase + 1))
                    )
                    """
                    Log an 'INFO' message for the measurement of the current photon for
                    the Quantum Transmission Phase of the Qiskrypt's Noiseless
                    DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
                    """

                    current_round_for_quantum_transmission_phase = \
                        quantum_transmission_phase_rounds[current_num_round_for_quantum_transmission_phase]
                    """
                    Retrieve the current round of the Quantum Transmission Phase of 
                    the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
                    """

                    if isinstance(current_round_for_quantum_transmission_phase,
                                  QiskryptNoiselessDVBKMPS22ProtocolWithNoEavesdroppingQuantumTransmissionPhaseRound):
                        """
                        If the current round of the Quantum Transmission Phase of 
                        the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol
                        with No Eavesdropping is really a Qiskrypt's Noiseless DV (Discrete Variables)
                        BKMPS22 Protocol with No Eavesdropping Quantum Transmission Phase Round.
                        """

                        current_round_quantum_circuit_for_quantum_transmission_phase = \
                            current_round_for_quantum_transmission_phase.get_round_quantum_circuit()
                        """
                        Retrieve the Qiskrypt's Quantum Circuit for the current round of
                        the Quantum Transmission Phase of the Qiskrypt's Noiseless
                        DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
                        """

                        if isinstance(current_round_quantum_circuit_for_quantum_transmission_phase,
                                      QiskryptQuantumCircuit):
                            """
                            If the Qiskrypt's Quantum Circuit for the current round of
                            the Quantum Transmission Phase of the Qiskrypt's Noiseless DV (Discrete Variables)
                            BKMPS22 Protocol with No Eavesdropping is really a Qiskrypt's Quantum Circuit.
                            """

                            quantum_coin_tossing_receiver_random_basis = \
                                QiskryptQuantumCoinTossing("qu_coin_toss_receiver_random_basis")
                            """
                            Create a Qiskrypt's Quantum Coin Tossing for the choice of
                            Random Basis for the receiver.
                            """

                            quantum_coin_tossing_receiver_random_basis.initialise_qiskrypt_quantum_circuit()
                            """
                            Initialise the Qiskrypt's Quantum Circuit for
                            the Qiskrypt's Quantum Coin Tossing for the choice of
                            Random Basis for the receiver.
                            """

                            quantum_coin_tossing_receiver_random_basis.toss_coin()
                            """
                            Toss the Coin related to the Qiskrypt's Quantum Coin Tossing
                            for the choice of Random Basis for the receiver.
                            """

                            receiver_random_basis_bit = \
                                quantum_coin_tossing_receiver_random_basis \
                                .get_coin_tossing_outcome_bit_as_int_base_2()
                            """
                            Retrieve the classical bit from the Qiskrypt's Coin Tossing,
                            for the choice of Random Basis for the receiver through
                            the execution of the respective Qiskrypt's Quantum Circuit,
                            in an integer base-2 format (i.e., an integer representation of a bit).
                            """

                            if not current_round_for_quantum_transmission_phase \
                                    .is_round_operation_receiver_choice_made():
                                """
                                If the operation choice made by the receiver in
                                the Qiskrypt's DV (Discrete Variables) BKMPS22 Protocol Round is not set yet.
                                """

                                if receiver_random_basis_bit == 0:
                                    """
                                    If the classical bit from the Qiskrypt's Coin Tossing,
                                    for the choice of Random Basis for the receiver through
                                    the execution of the respective Qiskrypt's Quantum Circuit,
                                    in an integer base-2 format (i.e., an integer representation of a bit)
                                    is zero (0), the receiver will choose the 'Z-Basis' to measure
                                    the qubit in the current round of the Quantum Transmission Phase of 
                                    the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol
                                    with No Eavesdropping.
                                    """

                                    current_round_for_quantum_transmission_phase \
                                        .set_round_operation_receiver_choice(
                                            POSSIBLE_DV_BKMPS22_PROTOCOL_ROUND_TYPES_QUANTUM_TRANSMISSION_PHASE[0]
                                            .split(" ")[0]
                                        )
                                    """
                                    Set the operation choice made by the sender in
                                    the Qiskrypt's DV (Discrete Variables) BKMPS22 Protocol Round as 'Z-BASIS'.
                                    """

                                    current_round_for_quantum_transmission_phase.get_round_quantum_circuit() \
                                        .prepare_and_measure_single_qubit_in_qiskit_quantum_register_in_z_basis \
                                        (2, 1, 0, 0, True)
                                    """
                                    Prepare the qubit in the receiver's Qiskrypt's Quantum Register of
                                    the Qiskrypt's Quantum Circuit of the current round of
                                    the Quantum Transmission Phase of the Qiskrypt's Noiseless
                                    DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping in
                                    the Z-Basis (Standard Computational Basis), and then measuring it.
                                    """

                                elif receiver_random_basis_bit == 1:
                                    """
                                    If the classical bit from the Qiskrypt's Coin Tossing,
                                    for the choice of Random Basis for the receiver through
                                    the execution of the respective Qiskrypt's Quantum Circuit,
                                    in an integer base-2 format (i.e., an integer representation of a bit)
                                    is one (1), the receiver will choose the 'X-Basis' to measure
                                    the qubit in the current round of the Quantum Transmission Phase of 
                                    the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol
                                    with No Eavesdropping.
                                    """

                                    current_round_for_quantum_transmission_phase \
                                        .set_round_operation_receiver_choice(
                                            POSSIBLE_DV_BKMPS22_PROTOCOL_ROUND_TYPES_QUANTUM_TRANSMISSION_PHASE[1]
                                            .split(" ")[0]
                                        )
                                    """
                                    Set the operation choice made by the sender in
                                    the Qiskrypt's DV (Discrete Variables) BKMPS22 Protocol Round as 'X-BASIS'.
                                    """

                                    current_round_for_quantum_transmission_phase.get_round_quantum_circuit() \
                                        .prepare_and_measure_single_qubit_in_qiskit_quantum_register_in_x_basis \
                                        (2, 1, 0, 0, True)
                                    """
                                    Prepare the qubit in the receiver's Qiskrypt's Quantum Register of
                                    the Qiskrypt's Quantum Circuit of the current round of
                                    the Quantum Transmission Phase of the Qiskrypt's Noiseless
                                    DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping in
                                    the X-Basis (Hadamard Basis), and then measuring it.
                                    """

                                qiskit_qasm_backend = aer.get_backend("qasm_simulator")
                                """
                                Getting the Aer Simulator Backend for the QASM (Quantum Assembly) Simulation
                                (i.e., the classical simulation of an IBM Qiskit's Quantum Circuit).
                                """

                                final_results_frequency_counting = \
                                    execute(current_round_for_quantum_transmission_phase
                                            .get_round_quantum_circuit().get_qiskit_quantum_circuit(),
                                            qiskit_qasm_backend, shots=1).result().get_counts()
                                """
                                Execute the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit
                                and store the resulted measurement of its final quantum state.
                                """

                                measurement_outcome_secret_bit = \
                                    bin(int(final_results_frequency_counting
                                            .most_frequent()[::-1].split(" ")[1], base=2))
                                """
                                Set the secret bit outcome for the round of
                                the Quantum Transmission Phase of the Qiskrypt's Noiseless
                                DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping,
                                from the measurement of the qubit in the receiver
                                Qiskrypt's Quantum Register into the bit of the receiver
                                Qiskrypt's Classical Register of the respective
                                Qiskrypt's Quantum Circuit, as the resulted outcome from
                                the measurement of the IBM Qiskit's Quantum Circuit,
                                in an binary format (i.e., the Python's representation for a bit).
                                """

                                current_round_for_quantum_transmission_phase.get_round_quantum_circuit() \
                                    .get_qiskrypt_classical_register(1) \
                                    .update_bit(0, int(measurement_outcome_secret_bit[BINARY_FORMAT_START_OFFSET:]))
                                """
                                Update the bit in the receiver Qiskrypt's Classical Register of
                                the respective Qiskrypt's Quantum Circuit for the round of
                                the Quantum Transmission Phase of the Qiskrypt's Noiseless
                                DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
                                """

                                receiver_raw_key_secret_bits += \
                                    str(measurement_outcome_secret_bit[BINARY_FORMAT_START_OFFSET:])
                                """
                                Append the current secret bit to the binary string for
                                the bits used to build the Qiskrypt's Secret Raw Key of
                                the receiver Qiskrypt's Party Client, according to
                                the randomly chosen measurement for it.
                                """

                            else:
                                """
                                If the basis choice made by the receiver in
                                the Qiskrypt's DV (Discrete Variables) BKMPS22 Protocol Round is already set.
                                """

                                # TODO Throw - Exception

                        else:
                            """
                            If the Qiskrypt's Quantum Circuit for the current round of
                            the Quantum Transmission Phase of the Qiskrypt's Noiseless
                            DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping is
                            not a Qiskrypt's Quantum Circuit.
                            """

                            # TODO Throw - Exception

                    else:
                        """
                        If the current round of the Quantum Transmission Phase of 
                        the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol
                        with No Eavesdropping is not a Qiskrypt's Noiseless
                        DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping
                        Quantum Transmission Phase Round.
                        """

                        # TODO Throw - Exception

                    receiver_party_client_uuid = receiver_party_client.get_uuid()
                    """
                    Retrieve the UUID (Universally Unique IDentifier) of the receiver Qiskrypt's Client.
                    """

                    receiver_secret_raw_key = QiskryptSecretRawKey(receiver_raw_key_secret_bits,
                                                                   receiver_party_client_uuid)
                    """
                    Create a Qiskrypt's Secret Raw Key for the receiver Qiskrypt's Client.
                    """

                    receiver_secret_raw_key_privacy_level = \
                        receiver_secret_raw_key.get_key_privacy_level()
                    """
                    Retrieve the privacy level of the Qiskrypt's Key for the receiver Qiskrypt's Client.
                    """

                    receiver_secret_raw_key_type = \
                        receiver_secret_raw_key.get_key_type()
                    """
                    Retrieve the type of the Qiskrypt's Key for the receiver Qiskrypt's Client.
                    """

                    receiver_party_name = receiver_party_client.get_party().get_name()
                    """
                    Retrieve the name of the receiver Qiskrypt's Party.
                    """

                    receiver_party_num = receiver_party_client.get_party().get_num()
                    """
                    Retrieve the number of the receiver Qiskrypt's Party.                
                    """

                    sender_party_name = sender_party_client.get_party().get_name()
                    """
                    Retrieve the name of the sender Qiskrypt's Party.
                    """

                    sender_party_num = sender_party_client.get_party().get_num()
                    """
                    Retrieve the number of the sender Qiskrypt's Party.                
                    """

                    receiver_secret_raw_key_id = \
                        "{} {} ({}_{} ; {}_{})".format(receiver_secret_raw_key_privacy_level.lower(),
                                                       receiver_secret_raw_key_type.lower(),
                                                       receiver_party_name.lower(), receiver_party_num,
                                                       sender_party_name.lower(), sender_party_num)
                    """
                    Set up the identifier of the Qiskrypt's Secret Raw Key for
                    the receiver Qiskrypt's Client.
                    """

                    receiver_party_client.add_item(receiver_secret_raw_key_id, receiver_secret_raw_key)
                    """
                    Add a new item to keep the Qiskrypt's Secret Raw Key for
                    the receiver Qiskrypt's Client.
                    """

                    logger_info_message(
                        "    2.6) Finishing the measurement of the incoming photons for\n"
                        "                   the Quantum Transmission Phase of the Qiskrypt's Noiseless\n"
                        "                   DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping..."
                    )
                    """
                    Log an 'INFO' message for the finish of the procedure of the measurement of
                    the incoming photons for the Quantum Transmission Phase of the Qiskrypt's Noiseless
                    DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
                    """

                    sender_party_name = sender_party_client.get_party().get_name()
                    """
                    Retrieve the name of the sender Qiskrypt's Party.
                    """

                    sender_party_num = sender_party_client.get_party().get_num()
                    """
                    Retrieve the number of the sender Qiskrypt's Party.                
                    """

                    receiver_party_name = receiver_party_client.get_party().get_name()
                    """
                    Retrieve the name of the receiver Qiskrypt's Party.
                    """

                    receiver_party_num = receiver_party_client.get_party().get_num()
                    """
                    Retrieve the number of the receiver Qiskrypt's Party.                
                    """

                    sender_secret_raw_key_id = \
                        "{} {} ({}_{} ; {}_{})".format(POSSIBLE_KEY_PRIVACY_LEVELS[0].lower(),
                                                       POSSIBLE_KEY_TYPES[0].lower(),
                                                       sender_party_name.lower(), sender_party_num,
                                                       receiver_party_name.lower(), receiver_party_num)
                    """
                    Set up the identifier of the Qiskrypt's Secret Raw Key for
                    the sender Qiskrypt's Client.
                    """

                    receiver_secret_raw_key_id = \
                        "{} {} ({}_{} ; {}_{})".format(POSSIBLE_KEY_PRIVACY_LEVELS[0].lower(),
                                                       POSSIBLE_KEY_TYPES[0].lower(),
                                                       receiver_party_name.lower(), receiver_party_num,
                                                       sender_party_name.lower(), sender_party_num)
                    """
                    Set up the identifier of the Qiskrypt's Secret Raw Key for
                    the receiver Qiskrypt's Client.
                    """

                    sender_secret_raw_key = \
                        sender_party_client.get_item_value_by_key(sender_secret_raw_key_id)
                    """
                    Retrieve the Qiskrypt's Secret Raw Key for
                    the sender Qiskrypt's Client. 
                    """

                    receiver_secret_raw_key = \
                        receiver_party_client.get_item_value_by_key(receiver_secret_raw_key_id)
                    """
                    Retrieve the Qiskrypt's Secret Raw Key for
                    the receiver Qiskrypt's Client. 
                    """

                    logger_info_message(
                        "    2.7) Retrieving the information about the Qiskrypt's Secret Raw Keys obtained after\n"
                        "                   the Quantum Transmission Phase of the Qiskrypt's Noiseless\n"
                        "                   DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping:"
                    )
                    """
                    Log an 'INFO' message for the retrieval of the information about
                    the Qiskrypt's Secret Raw Keys obtained after the Quantum Transmission Phase of
                    the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol
                    with No Eavesdropping.
                    """

                    if isinstance(sender_secret_raw_key, QiskryptSecretRawKey) and \
                            isinstance(receiver_secret_raw_key, QiskryptSecretRawKey):
                        """
                        If both sender's and receiver's Qiskrypt's Secret Raw Keys are
                        really Qiskrypt's Secret Raw Keys.
                        """

                        logger_info_message(
                            "    2.7.1) Secret Raw Key #1 -> {}: {}"
                            .format(sender_secret_raw_key_id,
                                    sender_secret_raw_key.get_bits()[BINARY_FORMAT_START_OFFSET:])
                        )
                        """
                        Log an 'INFO' message for the sender's Qiskrypt's Secret Raw Key.
                        """

                        logger_info_message(
                            "    2.7.2) Secret Raw Key #2 -> {}: {}"
                            .format(receiver_secret_raw_key_id,
                                    receiver_secret_raw_key.get_bits()[BINARY_FORMAT_START_OFFSET:])
                        )
                        """
                        Log an 'INFO' message for the receiver's Qiskrypt's Secret Raw Key.
                        """

            else:
                """
                If the sender and/or receiver Qiskrypt's Party Clients of
                the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol
                with No Eavesdropping are not Qiskrypt's Party Clients.
                """

                # TODO Throw - Exception

        else:
            """
            If the Qiskrypt's Key Exchange Protocol is not configured.
            """

            # TODO Throw - Exception

    def sift_raw_key(self):
        """
        Sift the Secret Key for the
        Qiskrypt's Semi-Quantum Conference Key Agreement (SQCKA).

        NOTES:
        - For the DV (Discrete Variables) BKMPS22 Protocol, the rounds of Quantum Transmission Phase,
          on which the sender and receiver Qiskrypt's Party Clients choose the same basis,
          are kept and will be used to compose their Qiskrypt's Secret Sifted Keys,
          since it is expected that correspond to correlated outcome bits.
        - On the other hand, the rounds of Quantum Transmission Phase,
          on which the sender and receiver Qiskrypt's Party Clients choose different bases,
          are discarded, since it is not guaranteed that correspond to correlated outcome bits.
        """

        if self.is_configured():
            """
            If the Qiskrypt's Key Exchange Protocol is already configured.
            """

            logger_info_message(
                "    3.1) Starting the Key Sifting procedure for\n"
                "                   the Classical Post-Processing Phase of the Qiskrypt's Noiseless\n"
                "                   DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping..."
            )
            """
            Log an 'INFO' message for the start of the procedure of the Key Sifting of
            the Qiskrypt's Secret Raw Key for the Classical Post-Processing Phase of the Qiskrypt's Noiseless
            DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
            """

            sender_basis_choices = ""
            """
            Initialise the string for the basis choices made by the sender Qiskrypt's Party Client
            during the rounds of the Quantum Transmission Phase.
            """

            sender_sifted_key_secret_bits = "0b"
            """
            Initialise the binary string for the bits used to build
            the Qiskrypt's Secret Sifted Key of the sender Qiskrypt's Party Client.
            """

            receiver_sifted_key_secret_bits = "0b"
            """
            Initialise the binary string for the bits used to build
            the Qiskrypt's Secret Sifted Key of the receiver Qiskrypt's Party Client.
            """

            receiver_basis_choices = ""
            """
            Initialise the string for the basis choices made by the receiver Qiskrypt's Party Client
            during the rounds of the Quantum Transmission Phase.
            """

            num_rounds_for_quantum_transmission_phase = \
                self.get_num_rounds_for_quantum_transmission_phase()
            """
            Retrieve the number of rounds for the Quantum Transmission Phase in
            the Qiskrypt's Quantum Key Exchange Protocol.
            """

            quantum_transmission_phase_rounds = \
                self.get_quantum_transmission_phase_rounds()
            """
            Retrieve the list for the Quantum Transmission Phase of 
            the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
            """

            # TODO - Improve later for a more realistic exchange of bases using classical communications

            for current_num_round_for_quantum_transmission_phase in \
                    range(num_rounds_for_quantum_transmission_phase):
                """
                For each round of the Quantum Transmission Phase of 
                the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
                """

                current_round_for_quantum_transmission_phase = \
                    quantum_transmission_phase_rounds[current_num_round_for_quantum_transmission_phase]
                """
                Retrieve the current round of the Quantum Transmission Phase of 
                the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
                """

                if isinstance(current_round_for_quantum_transmission_phase,
                              QiskryptNoiselessDVBKMPS22ProtocolWithNoEavesdroppingQuantumTransmissionPhaseRound):
                    """
                    If the current round of the Quantum Transmission Phase of 
                    the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping is
                    really a Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol
                    with No Eavesdropping Quantum Transmission Phase Round.
                    """

                    if not current_round_for_quantum_transmission_phase.is_round_discarded():
                        """
                        If the current round of the Quantum Transmission Phase of
                        the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping,
                        is not a discarded round.
                        """

                        round_basis_sender_choice = \
                            current_round_for_quantum_transmission_phase.get_round_operation_sender_choice()
                        """
                        Retrieve the basis choice made by the sender for the current round of
                        the Quantum Transmission Phase of the Qiskrypt's Noiseless DV (Discrete Variables)
                        BKMPS22 Protocol with No Eavesdropping.
                        """

                        round_basis_receiver_choice = \
                            current_round_for_quantum_transmission_phase.get_round_operation_receiver_choice()
                        """
                        Retrieve the basis choice made by the receiver for the current round of
                        the Quantum Transmission Phase of the Qiskrypt's Noiseless DV (Discrete Variables)
                        BKMPS22 Protocol with No Eavesdropping.
                        """

                        if round_basis_sender_choice == \
                                POSSIBLE_DV_BKMPS22_PROTOCOL_ROUND_TYPES_QUANTUM_TRANSMISSION_PHASE[0].split(" ")[0]:
                            """
                            If the basis choice made by the sender for the current round of
                            the Quantum Transmission Phase of the Qiskrypt's Noiseless DV (Discrete Variables)
                            BKMPS22 Protocol with No Eavesdropping is the 'Z-Basis'.
                            """

                            sender_basis_choices += \
                                POSSIBLE_DV_BKMPS22_PROTOCOL_ROUND_TYPES_QUANTUM_TRANSMISSION_PHASE[0] \
                                .split(" ")[0].split("-")[0]
                            """
                            Append the basis choice made by the sender for the current round of
                            the Quantum Transmission Phase of the Qiskrypt's Noiseless DV (Discrete Variables)
                            BKMPS22 Protocol with No Eavesdropping if it is the 'Z-Basis'.
                            """

                        elif round_basis_sender_choice == \
                                POSSIBLE_DV_BKMPS22_PROTOCOL_ROUND_TYPES_QUANTUM_TRANSMISSION_PHASE[1].split(" ")[0]:
                            """
                            If the basis choice made by the sender for the current round of
                            the Quantum Transmission Phase of the Qiskrypt's Noiseless DV (Discrete Variables)
                            BKMPS22 Protocol with No Eavesdropping is the 'X-Basis'.
                            """

                            sender_basis_choices += \
                                POSSIBLE_DV_BKMPS22_PROTOCOL_ROUND_TYPES_QUANTUM_TRANSMISSION_PHASE[1] \
                                .split(" ")[0].split("-")[0]
                            """
                            Append the basis choice made by the sender for the current round of
                            the Quantum Transmission Phase of the Qiskrypt's Noiseless DV (Discrete Variables)
                            BKMPS22 Protocol with No Eavesdropping if it is the 'X-Basis'.
                            """

                        if round_basis_receiver_choice == \
                                POSSIBLE_DV_BKMPS22_PROTOCOL_ROUND_TYPES_QUANTUM_TRANSMISSION_PHASE[0].split(" ")[0]:
                            """
                            If the basis choice made by the receiver for the current round of
                            the Quantum Transmission Phase of the Qiskrypt's Noiseless DV (Discrete Variables)
                            BKMPS22 Protocol with No Eavesdropping is the 'Z-Basis'.
                            """

                            receiver_basis_choices += \
                                POSSIBLE_DV_BKMPS22_PROTOCOL_ROUND_TYPES_QUANTUM_TRANSMISSION_PHASE[0] \
                                .split(" ")[0].split("-")[0]
                            """
                            Append the basis choice made by the receiver for the current round of
                            the Quantum Transmission Phase of the Qiskrypt's Noiseless DV (Discrete Variables)
                            BKMPS22 Protocol with No Eavesdropping if it is the 'Z-Basis'.
                            """

                        elif round_basis_receiver_choice == \
                                POSSIBLE_DV_BKMPS22_PROTOCOL_ROUND_TYPES_QUANTUM_TRANSMISSION_PHASE[1].split(" ")[0]:
                            """
                            If the basis choice made by the receiver for the current round of
                            the Quantum Transmission Phase of the Qiskrypt's Noiseless DV (Discrete Variables)
                            BKMPS22 Protocol with No Eavesdropping is the 'X-Basis'.
                            """

                            receiver_basis_choices += \
                                POSSIBLE_DV_BKMPS22_PROTOCOL_ROUND_TYPES_QUANTUM_TRANSMISSION_PHASE[1] \
                                .split(" ")[0].split("-")[0]
                            """
                            Append the basis choice made by the receiver for the current round of
                            the Quantum Transmission Phase of the Qiskrypt's Noiseless DV (Discrete Variables)
                            BKMPS22 Protocol with No Eavesdropping if it is the 'X-Basis'.
                            """

                        if round_basis_sender_choice == round_basis_receiver_choice:
                            """
                            If the bases choices made by the sender and the receiver for the current round of
                            the Quantum Transmission Phase of the Qiskrypt's Noiseless DV (Discrete Variables)
                            BKMPS22 Protocol with No Eavesdropping are equal, the respective round will be used for
                            the Qiskrypt's Secret Sifted Key.
                            """

                            sender_secret_bit = \
                                current_round_for_quantum_transmission_phase \
                                .get_round_quantum_circuit().get_qiskrypt_classical_register(0).get_bit(0)
                            """
                            Retrieve the secret bit in the sender Qiskrypt's Classical Register of
                            the Qiskrypt's Quantum Circuit for the current round of the Quantum Transmission Phase of
                            the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
                            """

                            sender_sifted_key_secret_bits += str(sender_secret_bit)
                            """
                            Append the secret bit in the sender Qiskrypt's Classical Register of
                            the Qiskrypt's Quantum Circuit for the current round of the Quantum Transmission Phase of
                            the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping
                            to the binary string to be used to build the Qiskrypt's Secret Sifted Key for
                            the sender Qiskrypt's Client Party.
                            """

                            receiver_secret_bit = \
                                current_round_for_quantum_transmission_phase \
                                .get_round_quantum_circuit().get_qiskrypt_classical_register(1).get_bit(0)
                            """
                            Retrieve the secret bit in the receiver Qiskrypt's Classical Register of
                            the Qiskrypt's Quantum Circuit for the current round of the Quantum Transmission Phase of
                            the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
                            """

                            receiver_sifted_key_secret_bits += str(receiver_secret_bit)
                            """
                            Append the secret bit in the receiver Qiskrypt's Classical Register of
                            the Qiskrypt's Quantum Circuit for the current round of the Quantum Transmission Phase of
                            the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping
                            to the binary string to be used to build the Qiskrypt's Secret Sifted Key for
                            the receiver Qiskrypt's Client Party.
                            """

                            self.quantum_transmission_phase_rounds_not_discarded_from_key_sifting \
                                .append(current_round_for_quantum_transmission_phase)
                            """
                            Append the current round to the list of the rounds for
                            the Quantum Transmission Phase of the Qiskrypt's Noiseless DV (Discrete Variables)
                            BKMPS22 Protocol with No Eavesdropping not discarded from the Key Sifting.
                            """

                        else:
                            """
                            If the bases choices made by the sender and the receiver for the current round of
                            the Quantum Transmission Phase of the Qiskrypt's Noiseless DV (Discrete Variables)
                            BKMPS22 Protocol with No Eavesdropping are different, the respective round will be discarded.
                            """

                            current_round_for_quantum_transmission_phase.set_round_discarded_from_key_sifting()
                            """
                            Set the current round of the Quantum Transmission Phase of
                            the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping,
                            as a discarded round from the Key Sifting.
                            """

                    else:
                        """
                        If the current round of the Quantum Transmission Phase of
                        the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping,
                        is already a discarded round, which is not supposed yet before the Key Sifting.
                        """

                        # TODO Throw - Exception

            sender_party_client = \
                self.get_communication_session().get_sender_party_clients()[0]
            """
            Retrieve the sender Qiskrypt's Party Client from the Qiskrypt's Communication Session of
            the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
            """

            receiver_party_client = \
                self.get_communication_session().get_receiver_party_clients()[0]
            """
            Retrieve the receiver Qiskrypt's Party Client from the Qiskrypt's Communication Session of
            the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
            """

            if isinstance(sender_party_client, QiskryptPartyClient) and \
                    isinstance(receiver_party_client, QiskryptPartyClient):
                """
                If the sender and receiver Qiskrypt's Party Clients of
                the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol
                with No Eavesdropping are really Qiskrypt's Party Clients.
                """

                sender_party_name = sender_party_client.get_party().get_name()
                """
                Retrieve the name of the sender Qiskrypt's Party.
                """

                sender_party_num = sender_party_client.get_party().get_num()
                """
                Retrieve the number of the sender Qiskrypt's Party.                
                """

                receiver_party_name = receiver_party_client.get_party().get_name()
                """
                Retrieve the name of the receiver Qiskrypt's Party.
                """

                receiver_party_num = receiver_party_client.get_party().get_num()
                """
                Retrieve the number of the receiver Qiskrypt's Party.                
                """

                sender_party_client_uuid = sender_party_client.get_uuid()
                """
                Retrieve the UUID (Universally Unique IDentifier) of the sender Qiskrypt's Client.
                """

                sender_secret_sifted_key = QiskryptSecretSiftedKey(sender_sifted_key_secret_bits,
                                                                   sender_party_client_uuid)
                """
                Create a Qiskrypt's Secret Sifted Key for the sender Qiskrypt's Client.
                """

                receiver_party_client_uuid = receiver_party_client.get_uuid()
                """
                Retrieve the UUID (Universally Unique IDentifier) of the receiver Qiskrypt's Client.
                """

                receiver_secret_sifted_key = QiskryptSecretSiftedKey(receiver_sifted_key_secret_bits,
                                                                     receiver_party_client_uuid)
                """
                Create a Qiskrypt's Secret Sifted Key for the receiver Qiskrypt's Client.
                """

                sender_secret_sifted_key_privacy_level = \
                    sender_secret_sifted_key.get_key_privacy_level()
                """
                Retrieve the privacy level of the Qiskrypt's Key for the sender Qiskrypt's Client.
                """

                sender_secret_sifted_key_type = \
                    sender_secret_sifted_key.get_key_type()
                """
                Retrieve the type of the Qiskrypt's Key for the sender Qiskrypt's Client.
                """

                receiver_secret_sifted_key_privacy_level = \
                    receiver_secret_sifted_key.get_key_privacy_level()
                """
                Retrieve the privacy level of the Qiskrypt's Key for the receiver Qiskrypt's Client.
                """

                receiver_secret_sifted_key_type = \
                    receiver_secret_sifted_key.get_key_type()
                """
                Retrieve the type of the Qiskrypt's Key for the receiver Qiskrypt's Client.
                """

                sender_secret_sifted_key_id = \
                    "{} {} ({}_{} ; {}_{})".format(sender_secret_sifted_key_privacy_level.lower(),
                                                   sender_secret_sifted_key_type.lower(),
                                                   sender_party_name.lower(), sender_party_num,
                                                   receiver_party_name.lower(), receiver_party_num)
                """
                Set up the identifier of the Qiskrypt's Secret Sifted Key for
                the sender Qiskrypt's Client.
                """

                sender_party_client.add_item(sender_secret_sifted_key_id, sender_secret_sifted_key)
                """
                Add a new item to keep the Qiskrypt's Secret Sifted Key for
                the sender Qiskrypt's Client.
                """

                receiver_secret_sifted_key_id = \
                    "{} {} ({}_{} ; {}_{})".format(receiver_secret_sifted_key_privacy_level.lower(),
                                                   receiver_secret_sifted_key_type.lower(),
                                                   receiver_party_name.lower(), receiver_party_num,
                                                   sender_party_name.lower(), sender_party_num)
                """
                Set up the identifier of the Qiskrypt's Secret Sifted Key for
                the receiver Qiskrypt's Client.
                """

                receiver_party_client.add_item(receiver_secret_sifted_key_id, receiver_secret_sifted_key)
                """
                Add a new item to keep the Qiskrypt's Secret Sifted Key for
                the receiver Qiskrypt's Client.
                """

            else:
                """
                If the sender and/or receiver Qiskrypt's Party Clients of
                the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol
                with No Eavesdropping are not Qiskrypt's Party Clients.
                """

                # TODO Throw - Exception

            logger_info_message(
                "    3.2) Finishing the Key Sifting procedure for\n"
                "                   the Classical Post-Processing Phase of the Qiskrypt's Noiseless\n"
                "                   DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping..."
            )
            """
            Log an 'INFO' message for the finish of the procedure of the Key Sifting of
            the Qiskrypt's Secret Raw Key for the Classical Post-Processing Phase of the Qiskrypt's Noiseless
            DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
            """

            logger_info_message(
                "    3.3) Retrieving the information about the Qiskrypt's Secret Reconciled Keys obtained after\n"
                "                   the Key Sifting procedure of the Classical Post-Processing Phase\n"
                "                   of the Qiskrypt's Noiseless DV (Discrete Variables)\n"
                "                   BKMPS22 Protocol with No Eavesdropping:"
            )
            """
            Log an 'INFO' message for the retrieval of the information about
            the Qiskrypt's Secret Reconciled Keys obtained after the Key Sifting procedure
            of the Classical Post-Processing Phase of the Qiskrypt's Noiseless DV (Discrete Variables)
            BKMPS22 Protocol with No Eavesdropping.
            """

            sender_party_client = \
                self.get_communication_session().get_sender_party_clients()[0]
            """
            Retrieve the sender Qiskrypt's Party Client from the Qiskrypt's Communication Session of
            the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
            """

            receiver_party_client = \
                self.get_communication_session().get_receiver_party_clients()[0]
            """
            Retrieve the receiver Qiskrypt's Party Client from the Qiskrypt's Communication Session of
            the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
            """

            if isinstance(sender_party_client, QiskryptPartyClient) and \
                    isinstance(receiver_party_client, QiskryptPartyClient):
                """
                If the sender and receiver Qiskrypt's Party Clients of
                the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol
                with No Eavesdropping are really Qiskrypt's Party Clients.
                """

                sender_party_name = sender_party_client.get_party().get_name()
                """
                Retrieve the name of the sender Qiskrypt's Party.
                """

                sender_party_num = sender_party_client.get_party().get_num()
                """
                Retrieve the number of the sender Qiskrypt's Party.                
                """

                receiver_party_name = receiver_party_client.get_party().get_name()
                """
                Retrieve the name of the receiver Qiskrypt's Party.
                """

                receiver_party_num = receiver_party_client.get_party().get_num()
                """
                Retrieve the number of the receiver Qiskrypt's Party.                
                """

                sender_secret_sifted_key_id = \
                    "{} {} ({}_{} ; {}_{})".format(POSSIBLE_KEY_PRIVACY_LEVELS[0].lower(),
                                                   POSSIBLE_KEY_TYPES[1].lower(),
                                                   sender_party_name.lower(), sender_party_num,
                                                   receiver_party_name.lower(), receiver_party_num)
                """
                Set up the identifier of the Qiskrypt's Secret Sifted Key for
                the sender Qiskrypt's Client.
                """

                receiver_secret_sifted_key_id = \
                    "{} {} ({}_{} ; {}_{})".format(POSSIBLE_KEY_PRIVACY_LEVELS[0].lower(),
                                                   POSSIBLE_KEY_TYPES[1].lower(),
                                                   receiver_party_name.lower(), receiver_party_num,
                                                   sender_party_name.lower(), sender_party_num)
                """
                Set up the identifier of the Qiskrypt's Secret Sifted Key for
                the receiver Qiskrypt's Client.
                """

                sender_secret_sifted_key = \
                    sender_party_client.get_item_value_by_key(sender_secret_sifted_key_id)
                """
                Retrieve the Qiskrypt's Secret Sifted Key for
                the sender Qiskrypt's Client. 
                """

                receiver_secret_sifted_key = \
                    receiver_party_client.get_item_value_by_key(receiver_secret_sifted_key_id)
                """
                Retrieve the Qiskrypt's Secret Sifted Key for
                the receiver Qiskrypt's Client. 
                """

                logger_info_message(
                    "    3.3.1) Basis Choices #1: {}"
                    .format(sender_basis_choices)
                )
                """
                Log an 'INFO' message for the sender's basis choices.
                """

                logger_info_message(
                    "    3.3.2) Basis Choices #2: {}"
                    .format(receiver_basis_choices)
                )
                """
                Log an 'INFO' message for the receiver's basis choices.
                """

                bases_kept_and_discarded = ""
                """
                Initialise the string to keep the information about the basis choices,
                which will be kept and discarded.
                """

                num_sender_basis_choices = len(sender_basis_choices)
                """
                Retrieve the number of basis choices made by the sender Qiskrypt's Party Client.
                """

                num_receiver_basis_choices = len(receiver_basis_choices)
                """
                Retrieve the number of basis choices made by the receiver Qiskrypt's Party Client.
                """

                if num_sender_basis_choices == num_receiver_basis_choices:
                    """
                    If the number of basis choices made by both the sender and receiver
                    Qiskrypt's Party Clients are equal.
                    """

                    for current_sender_basis_choice, current_receiver_basis_choice in \
                            zip(range(num_sender_basis_choices), range(num_receiver_basis_choices)):
                        """
                        For each pair of basis choices made by both the sender and receiver
                        Qiskrypt's Party Clients.
                        """

                        if sender_basis_choices[current_sender_basis_choice] == \
                                receiver_basis_choices[current_receiver_basis_choice]:
                            """
                            If the basis choices made by both the sender and receiver
                            Qiskrypt's Party Clients, during the same round, are the same.
                            """

                            bases_kept_and_discarded += "✓"
                            """
                            Append the 'kept' symbol to the string to keep
                            the information about the basis choices, which will be kept and discarded.
                            """

                        else:
                            """
                            If the basis choices made by both the sender and receiver
                            Qiskrypt's Party Clients, during the same round, are different.
                            """

                            bases_kept_and_discarded += "✗"
                            """
                            Append the 'discarded' symbol to the string to keep
                            the information about the basis choices, which will be kept and discarded.
                            """

                else:
                    """
                    If the number of basis choices made by both the sender and receiver
                    Qiskrypt's Party Clients are not equal.
                    """

                    # TODO Throw - Exception

                logger_info_message(
                    "    3.3.3) Sifting of Bases: {}".format(bases_kept_and_discarded)
                )
                """
                Log an 'INFO' message for the basis choices kept and discarded.
                """

                if isinstance(sender_secret_sifted_key, QiskryptSecretSiftedKey) and \
                        isinstance(receiver_secret_sifted_key, QiskryptSecretSiftedKey):
                    """
                    If the Qiskrypt's Secret Sifted Keys of the sender and the receiver
                    Qiskrypt's Party Clients of the Qiskrypt's Noiseless DV (Discrete Variables)
                    BKMPS22 Protocol with No Eavesdropping are really Qiskrypt's Secret Sifted Keys.
                    """

                    logger_info_message(
                        "    3.3.4) Secret Sifted Key #1 -> {}: {}"
                        .format(sender_secret_sifted_key_id,
                                sender_secret_sifted_key.get_bits()[BINARY_FORMAT_START_OFFSET:])
                    )
                    """
                    Log an 'INFO' message for the sender's Qiskrypt's Secret Sifted Key.
                    """

                    logger_info_message(
                        "    3.3.5) Secret Sifted Key #2 -> {}: {}"
                        .format(receiver_secret_sifted_key_id,
                                receiver_secret_sifted_key.get_bits()[BINARY_FORMAT_START_OFFSET:])
                    )
                    """
                    Log an 'INFO' message for the receiver's Qiskrypt's Secret Sifted Key.
                    """

                else:
                    """
                    If the Qiskrypt's Secret Sifted Keys of the sender and/or the receiver
                    Qiskrypt's Party Clients of the Qiskrypt's Noiseless DV (Discrete Variables)
                    BKMPS22 Protocol with No Eavesdropping are not Qiskrypt's Secret Sifted Keys.
                    """

                    # TODO Throw - Exception

            else:
                """
                If the sender and/or receiver Qiskrypt's Party Clients of
                the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol
                with No Eavesdropping are not Qiskrypt's Party Clients.
                """

                # TODO Throw - Exception

        else:
            """
            If the Qiskrypt's Key Exchange Protocol is not configured.
            """

            # TODO Throw - Exception

    def estimate_parameters(self):
        """
        Estimate the Parameters for the
        Qiskrypt's Semi-Quantum Conference Key Agreement (SQCKA).
        """

        if self.is_configured():
            """
            If the Qiskrypt's Key Exchange Protocol is already configured.
            """

            logger_info_message(
                "    3.4) Starting the Parameter Estimation procedure for\n"
                "                   the Classical Post-Processing Phase of the Qiskrypt's Noiseless\n"
                "                   DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping..."
            )
            """
            Log an 'INFO' message for the start of the procedure of the Parameter Estimation of
            the Qiskrypt's Secret Sifted Key for the Classical Post-Processing Phase of the Qiskrypt's Noiseless
            DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
            """

            sender_party_client = \
                self.get_communication_session().get_sender_party_clients()[0]
            """
            Retrieve the sender Qiskrypt's Party Client from the Qiskrypt's Communication Session of
            the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
            """

            receiver_party_client = \
                self.get_communication_session().get_receiver_party_clients()[0]
            """
            Retrieve the receiver Qiskrypt's Party Client from the Qiskrypt's Communication Session of
            the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
            """

            if isinstance(sender_party_client, QiskryptPartyClient) and \
                    isinstance(receiver_party_client, QiskryptPartyClient):
                """
                If the sender and receiver Qiskrypt's Party Clients of
                the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol
                with No Eavesdropping are really Qiskrypt's Party Clients.
                """

                sender_party_name = sender_party_client.get_party().get_name()
                """
                Retrieve the name of the sender Qiskrypt's Party.
                """

                sender_party_num = sender_party_client.get_party().get_num()
                """
                Retrieve the number of the sender Qiskrypt's Party.                
                """

                receiver_party_name = receiver_party_client.get_party().get_name()
                """
                Retrieve the name of the receiver Qiskrypt's Party.
                """

                receiver_party_num = receiver_party_client.get_party().get_num()
                """
                Retrieve the number of the receiver Qiskrypt's Party.                
                """

                sender_secret_sifted_key_id = \
                    "{} {} ({}_{} ; {}_{})".format(POSSIBLE_KEY_PRIVACY_LEVELS[0].lower(),
                                                   POSSIBLE_KEY_TYPES[1].lower(),
                                                   sender_party_name.lower(), sender_party_num,
                                                   receiver_party_name.lower(), receiver_party_num)
                """
                Set up the identifier of the Qiskrypt's Secret Sifted Key for
                the sender Qiskrypt's Client.
                """

                receiver_secret_sifted_key_id = \
                    "{} {} ({}_{} ; {}_{})".format(POSSIBLE_KEY_PRIVACY_LEVELS[0].lower(),
                                                   POSSIBLE_KEY_TYPES[1].lower(),
                                                   receiver_party_name.lower(), receiver_party_num,
                                                   sender_party_name.lower(), sender_party_num)
                """
                Set up the identifier of the Qiskrypt's Secret Sifted Key for
                the receiver Qiskrypt's Client.
                """

                sender_secret_sifted_key = \
                    sender_party_client.get_item_value_by_key(sender_secret_sifted_key_id)
                """
                Retrieve the Qiskrypt's Secret Sifted Key for
                the sender Qiskrypt's Client. 
                """

                receiver_secret_sifted_key = \
                    receiver_party_client.get_item_value_by_key(receiver_secret_sifted_key_id)
                """
                Retrieve the Qiskrypt's Secret Sifted Key for
                the receiver Qiskrypt's Client. 
                """

                if isinstance(sender_secret_sifted_key, QiskryptSecretSiftedKey) and \
                        isinstance(receiver_secret_sifted_key, QiskryptSecretSiftedKey):
                    """
                    If the Qiskrypt's Secret Sifted Keys of the sender and the receiver
                    Qiskrypt's Party Clients of the Qiskrypt's Noiseless DV (Discrete Variables)
                    BKMPS22 Protocol with No Eavesdropping are really Qiskrypt's Secret Sifted Keys.
                    """

                    sender_secret_sifted_key_length = \
                        (len(sender_secret_sifted_key.get_bits()) - BINARY_FORMAT_START_OFFSET)
                    """
                    Retrieve the length of the Qiskrypt's Secret Sifted Keys of the sender
                    Qiskrypt's Party Clients of the Qiskrypt's Noiseless DV (Discrete Variables)
                    BKMPS22 Protocol with No Eavesdropping.
                    """

                    receiver_secret_sifted_key_length = \
                        (len(receiver_secret_sifted_key.get_bits()) - BINARY_FORMAT_START_OFFSET)
                    """
                    Retrieve the length of the Qiskrypt's Secret Sifted Keys of the receiver
                    Qiskrypt's Party Clients of the Qiskrypt's Noiseless DV (Discrete Variables)
                    BKMPS22 Protocol with No Eavesdropping.
                    """

                    if sender_secret_sifted_key_length == receiver_secret_sifted_key_length:
                        """
                        If the Qiskrypt's Secret Sifted Keys of the sender and the receiver
                        Qiskrypt's Party Clients of the Qiskrypt's Noiseless DV (Discrete Variables)
                        BKMPS22 Protocol with No Eavesdropping really have the same length.
                        """

                        secret_sifted_key_length = sender_secret_sifted_key_length
                        """
                        Retrieve the length of the Qiskrypt's Secret Sifted Keys.
                        """

                        num_rounds_parameter_estimation_sample = \
                            int((DV_BKMPS22_PROTOCOL_DEFAULT_FACTOR_FOR_NUM_ROUNDS_OF_PARAMETER_ESTIMATION_SAMPLE *
                                 secret_sifted_key_length))
                        """
                        Compute the number of rounds for the parameter estimation sample for
                        the Qiskrypt's Party Clients of the Qiskrypt's Noiseless DV (Discrete Variables)
                        BKMPS22 Protocol with No Eavesdropping.
                        """

                        rounds_parameter_estimation_sample_indexes = set()
                        """
                        Initialise the list of rounds for the parameter estimation sample for
                        the Qiskrypt's Party Clients of the Qiskrypt's Noiseless DV (Discrete Variables)
                        BKMPS22 Protocol with No Eavesdropping, initially, as an empty set.
                        """

                        quantum_random_numeric_generator_parameter_estimation_sample = \
                            QiskryptQuantumRandomNumericGenerator("qu_rng_parameter_estimation_sample",
                                                                  DATA_TYPES[1], ranged=True)
                        """
                        Create the Qiskrypt's Quantum Random Numeric Generator to
                        generate random integer number to choose the rounds for
                        the parameter estimation sample for the Qiskrypt's Party Clients of
                        the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol
                        with No Eavesdropping.
                        """

                        quantum_random_numeric_generator_parameter_estimation_sample \
                            .initiate(min_range=0, max_range=(secret_sifted_key_length - 1))
                        """
                        Initiate the Qiskrypt's Quantum Random Numeric Generator to
                        generate random integer number to choose the rounds for
                        the parameter estimation sample for the Qiskrypt's Party Clients of
                        the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol
                        with No Eavesdropping, rescaled between the range intervals inside
                        the length of the Qiskrypt's Secret Sifted Key.
                        """

                        current_num_rounds_parameter_estimation_sample = 0
                        """
                        Initialise the current number of rounds for the Parameter Estimation sample for
                        the Qiskrypt's Party Clients of the Qiskrypt's Noiseless DV (Discrete Variables)
                        BKMPS22 Protocol with No Eavesdropping, initially, as zero (0).
                        """

                        while current_num_rounds_parameter_estimation_sample < \
                                num_rounds_parameter_estimation_sample:
                            """
                            While the current number of rounds for the Parameter Estimation sample for
                            the Qiskrypt's Party Clients of the Qiskrypt's Noiseless DV (Discrete Variables)
                            BKMPS22 Protocol with No Eavesdropping, is not the pretended yet to the respective set.
                            """

                            random_num_round_parameter_estimation_sample = \
                                int(float(str(quantum_random_numeric_generator_parameter_estimation_sample
                                              .generate_number())))
                            """
                            Generate and retrieve the random integer number to choose a round for
                            the Parameter Estimation sample for the Qiskrypt's Party Clients of
                            the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol
                            with No Eavesdropping.
                            """

                            if 0 <= random_num_round_parameter_estimation_sample < \
                                    receiver_secret_sifted_key_length:
                                """
                                If the random integer number to choose a round for
                                the Parameter Estimation sample for the Qiskrypt's Party Clients of
                                the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol
                                with No Eavesdropping is inside the valid and acceptable range.
                                """

                                rounds_parameter_estimation_sample_indexes \
                                    .add(random_num_round_parameter_estimation_sample)
                                """
                                Add the random integer number to choose a rounds for
                                the parameter estimation sample for the Qiskrypt's Party Clients of
                                the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol
                                with No Eavesdropping to the respective set of rounds for it.
                                """

                            current_num_rounds_parameter_estimation_sample = \
                                len(rounds_parameter_estimation_sample_indexes)
                            """
                            Update the current number of rounds for the Parameter Estimation sample for
                            the Qiskrypt's Party Clients of the Qiskrypt's Noiseless DV (Discrete Variables)
                            BKMPS22 Protocol with No Eavesdropping, from the respective set of rounds for it.
                            """

                        quantum_transmission_phase_rounds_not_discarded_from_key_sifting = \
                            self.get_quantum_transmission_phase_rounds_not_discarded_from_key_sifting()
                        """
                        Retrieve the list of the rounds for the Quantum Transmission Phase of
                        the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol
                        with No Eavesdropping not discarded from the Key Sifting.
                        """

                        z_basis_quantum_bits_errors = 0
                        """
                        Initialise the errors counter for the Parameter Estimation rounds,
                        where was used the Z-Basis (Standard Computational Basis) by
                        both the sender and receiver Qiskrypt's Party Clients of the
                        Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
                        """

                        z_basis_quantum_bits_total = 0
                        """
                        Initialise the total counter for the Parameter Estimation rounds,
                        where was used the Z-Basis (Standard Computational Basis) by
                        both the sender and receiver Qiskrypt's Party Clients of the
                        Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
                        """

                        x_basis_quantum_bits_errors = 0
                        """
                        Initialise the errors counter for the Parameter Estimation rounds,
                        where was used the X-Basis (Hadamard Basis) by both the sender and receiver
                        Qiskrypt's Party Clients of the Qiskrypt's Noiseless DV (Discrete Variables)
                        BKMPS22 Protocol with No Eavesdropping.
                        """

                        x_basis_quantum_bits_total = 0
                        """
                        Initialise the total counter for the Parameter Estimation rounds,
                        where was used the X-Basis (Hadamard Basis) by both the sender and receiver
                        Qiskrypt's Party Clients of the Qiskrypt's Noiseless DV (Discrete Variables)
                        BKMPS22 Protocol with No Eavesdropping.
                        """

                        for current_sample_index in rounds_parameter_estimation_sample_indexes:
                            """
                            For each round for the Parameter Estimation sample for
                            the Qiskrypt's Party Clients of the Qiskrypt's Noiseless DV (Discrete Variables)
                            BKMPS22 Protocol with No Eavesdropping, from the respective set of rounds for it.
                            """

                            current_parameter_estimation_round = \
                                quantum_transmission_phase_rounds_not_discarded_from_key_sifting[current_sample_index]
                            """
                            Retrieve the current round for the Parameter Estimation sample for
                            the Qiskrypt's Party Clients of the Qiskrypt's Noiseless DV (Discrete Variables)
                            BKMPS22 Protocol with No Eavesdropping, from the respective set of rounds for it.
                            """

                            if isinstance(
                                    current_parameter_estimation_round,
                                    QiskryptNoiselessDVBKMPS22ProtocolWithNoEavesdroppingQuantumTransmissionPhaseRound
                            ):
                                """
                                If the current round for the Parameter Estimation sample for
                                the Qiskrypt's Party Clients of the Qiskrypt's Noiseless DV (Discrete Variables)
                                BKMPS22 Protocol with No Eavesdropping is really a Qiskrypt's Noiseless
                                DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping
                                Quantum Transmission Phase Round.
                                """

                                current_parameter_estimation_round \
                                    .set_round_discarded_from_parameter_estimation()
                                """
                                Set the current round for the Parameter Estimation sample for
                                the Qiskrypt's Party Clients of the Qiskrypt's Noiseless DV (Discrete Variables)
                                BKMPS22 Protocol with No Eavesdropping is really a Qiskrypt's Noiseless
                                DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping
                                Quantum Transmission Phase Round, as discarded.
                                """

                                current_parameter_estimation_round_basis_sender_choice = \
                                    current_parameter_estimation_round.get_round_operation_sender_choice()
                                """
                                Retrieve the basis choice made by the sender in
                                the current round for the Parameter Estimation sample for
                                the Qiskrypt's Party Clients of the Qiskrypt's Noiseless DV (Discrete Variables)
                                BKMPS22 Protocol with No Eavesdropping is really a Qiskrypt's Noiseless
                                DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping
                                Quantum Transmission Phase Round.
                                """

                                current_parameter_estimation_round_basis_receiver_choice = \
                                    current_parameter_estimation_round.get_round_operation_receiver_choice()
                                """
                                Retrieve the basis choice made by the receiver in
                                the current round for the Parameter Estimation sample for
                                the Qiskrypt's Party Clients of the Qiskrypt's Noiseless DV (Discrete Variables)
                                BKMPS22 Protocol with No Eavesdropping is really a Qiskrypt's Noiseless
                                DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping
                                Quantum Transmission Phase Round.
                                """

                                if current_parameter_estimation_round_basis_sender_choice == \
                                        current_parameter_estimation_round_basis_receiver_choice:
                                    """
                                    If basis choices made by both the sender and receiver in
                                    the current round for the Parameter Estimation sample for
                                    the Qiskrypt's Party Clients of the Qiskrypt's Noiseless DV (Discrete Variables)
                                    BKMPS22 Protocol with No Eavesdropping is really a Qiskrypt's Noiseless
                                    DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping
                                    Quantum Transmission Phase Round are the same.

                                    NOTE:
                                    - This case should ALWAYS happen in this phase of
                                      the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol
                                      with No Eavesdropping.
                                    """

                                    current_parameter_estimation_round_type = \
                                        current_parameter_estimation_round.get_round_type()
                                    """
                                    Retrieve the type of the current round for the
                                    Parameter Estimation sample for the Qiskrypt's Party Clients of
                                    the Qiskrypt's Noiseless DV (Discrete Variables)
                                    BKMPS22 Protocol with No Eavesdropping.
                                    """

                                    current_parameter_estimation_round_sender_secret_bit = \
                                        current_parameter_estimation_round.get_round_quantum_circuit() \
                                        .get_qiskrypt_classical_register(0).get_bit(0)
                                    """
                                    Retrieve the secret bit from the current round for
                                    the Parameter Estimation sample of the sender
                                    Qiskrypt's Party Client of the Qiskrypt's Noiseless
                                    DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
                                    """

                                    current_parameter_estimation_round_receiver_secret_bit = \
                                        current_parameter_estimation_round.get_round_quantum_circuit() \
                                        .get_qiskrypt_classical_register(1).get_bit(0)
                                    """
                                    Retrieve the secret bit from the current round for
                                    the Parameter Estimation sample of the receiver
                                    Qiskrypt's Party Client of the Qiskrypt's Noiseless
                                    DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
                                    """

                                    if current_parameter_estimation_round_type == \
                                            POSSIBLE_DV_BKMPS22_PROTOCOL_ROUND_TYPES_QUANTUM_TRANSMISSION_PHASE[0]:
                                        """
                                        If the current round for the Parameter Estimation sample for
                                        the Qiskrypt's Party Clients of the Qiskrypt's Noiseless
                                        DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping
                                        is a 'Z-BASIS ROUND'.
                                        """

                                        z_basis_quantum_bits_total += 1
                                        """
                                        Increment the total counter for the Parameter Estimation rounds,
                                        where was used the Z-Basis (Standard Computational Basis)
                                        by both the sender and receiver Qiskrypt's Party Clients of
                                        the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol
                                        with No Eavesdropping.
                                        """

                                        if current_parameter_estimation_round_sender_secret_bit != \
                                                current_parameter_estimation_round_receiver_secret_bit:
                                            """
                                            If there is an error in secret bits from the current
                                            Z-Basis (Standard Computational Basis) Round for
                                            the Parameter Estimation sample of the sender and receiver
                                            Qiskrypt's Party Clients of the Qiskrypt's Noiseless
                                            DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
                                            """

                                            z_basis_quantum_bits_errors += 1
                                            """
                                            Increment the errors counter for the Parameter Estimation rounds,
                                            where was used the Z-Basis (Standard Computational Basis)
                                            by both the sender and receiver Qiskrypt's Party Clients of
                                            the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol
                                            with No Eavesdropping.
                                            """

                                    elif current_parameter_estimation_round_type == \
                                            POSSIBLE_DV_BKMPS22_PROTOCOL_ROUND_TYPES_QUANTUM_TRANSMISSION_PHASE[1]:
                                        """
                                        If the current round for the Parameter Estimation sample for
                                        the Qiskrypt's Party Clients of the Qiskrypt's Noiseless
                                        DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping
                                        is a 'X-BASIS ROUND'.  
                                        """

                                        x_basis_quantum_bits_total += 1
                                        """
                                        Increment the total counter for the Parameter Estimation rounds,
                                        where was used the X-Basis (Hadamard Basis)
                                        by both the sender and receiver Qiskrypt's Party Clients of
                                        the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol
                                        with No Eavesdropping.
                                        """

                                        if current_parameter_estimation_round_sender_secret_bit != \
                                                current_parameter_estimation_round_receiver_secret_bit:
                                            """
                                            If there is an error in secret bits from the current
                                            X-Basis (Hadamard Basis) Round for
                                            the Parameter Estimation sample of the sender and receiver
                                            Qiskrypt's Party Clients of the Qiskrypt's Noiseless
                                            DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
                                            """

                                            x_basis_quantum_bits_errors += 1
                                            """
                                            Increment the errors counter for the Parameter Estimation rounds,
                                            where was used the X-Basis (Hadamard Basis)
                                            by both the sender and receiver Qiskrypt's Party Clients of
                                            the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol
                                            with No Eavesdropping.
                                            """

                                else:
                                    """
                                    If basis choices made by both the sender and receiver in
                                    the current round for the Parameter Estimation sample for
                                    the Qiskrypt's Party Clients of the Qiskrypt's Noiseless DV (Discrete Variables)
                                    BKMPS22 Protocol with No Eavesdropping is really a Qiskrypt's Noiseless
                                    DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping
                                    Quantum Transmission Phase Round are not the same.

                                    NOTE:
                                    - This case should NEVER happen in this phase of
                                      the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol
                                      with No Eavesdropping.
                                    """

                                    # TODO Throw - Exception

                        if z_basis_quantum_bits_total > 0:
                            """
                            If there are some 'Z-Basis' round chosen for the Parameter Estimation
                            in the Qiskrypt's Noiseless DV (Discrete Variables)
                            BKMPS22 Protocol with No Eavesdropping.
                            """

                            self.update_quantum_bit_error_rate_z_basis(
                                (z_basis_quantum_bits_errors / z_basis_quantum_bits_total)
                            )
                            """
                            Update the QBER (Quantum Bit Error Rate) for the Parameter Estimation rounds,
                            where was used the Z-Basis (Standard Computational Basis) by both
                            the sender and receiver Qiskrypt's Party Clients of the Qiskrypt's
                            Noiseless DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
                            """

                        elif z_basis_quantum_bits_total == 0:
                            """
                            If there are no Z-Basis (Standard Computational Basis) round chosen for
                            the Parameter Estimation in the Qiskrypt's Noiseless
                            DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
                            """

                            self.update_quantum_bit_error_rate_z_basis(0.0)
                            """
                            Update the QBER (Quantum Bit Error Rate) for the Parameter Estimation rounds,
                            where was used the Z-Basis (Standard Computational Basis) by both
                            the sender and receiver Qiskrypt's Party Clients of the Qiskrypt's
                            Noiseless DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
                            """

                        if x_basis_quantum_bits_total > 0:
                            """
                            If there are some X-Basis (Hadamard Basis) round chosen for
                            the Parameter Estimation in the Qiskrypt's Noiseless
                            DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
                            """

                            self.update_quantum_bit_error_rate_x_basis(
                                (x_basis_quantum_bits_errors / x_basis_quantum_bits_total)
                            )
                            """
                            Update the QBER (Quantum Bit Error Rate) for the Parameter Estimation rounds,
                            where was used the X-Basis (Hadamard Basis) by both the sender and receiver
                            Qiskrypt's Party Clients of the Qiskrypt's Noiseless DV (Discrete Variables)
                            BKMPS22 Protocol with No Eavesdropping.
                            """

                        elif x_basis_quantum_bits_total == 0:
                            """
                            If there are no X-Basis (Hadamard Basis) round chosen for
                            the Parameter Estimation in the Qiskrypt's Noiseless
                            DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
                            """

                            self.update_quantum_bit_error_rate_x_basis(0.0)
                            """
                            Update the QBER (Quantum Bit Error Rate) for the Parameter Estimation rounds,
                            where was used the X-Basis (Hadamard Basis) by both the sender and receiver
                            Qiskrypt's Party Clients of the Qiskrypt's Noiseless DV (Discrete Variables)
                            BKMPS22 Protocol with No Eavesdropping.
                            """

                        logger_info_message(
                            "    3.4.1) QBER (Quantum Bit Error Rate) for\n"
                            "                     the Z-Basis (Standard Computational Basis): {}"
                            .format(self.get_quantum_bit_error_rate_z_basis())
                        )
                        """
                        Log an 'INFO' message for the QBER (Quantum Bit Error Rater) for the Z-Basis
                        (Standard Computational Basis) obtained from the procedure of
                        the Parameter Estimation performed on the Qiskrypt's Secret Sifted Key
                        for the Classical Post-Processing Phase of the Qiskrypt's Noiseless
                        DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
                        """

                        logger_info_message(
                            "    3.4.2) QBER (Quantum Bit Error Rate) for\n"
                            "                     the X-Basis (Hadamard Basis): {}"
                            .format(self.get_quantum_bit_error_rate_x_basis())
                        )
                        """
                        Log an 'INFO' message for the QBER (Quantum Bit Error Rater) for the X-Basis
                        (Hadamard Basis) obtained from the procedure of
                        the Parameter Estimation performed on the Qiskrypt's Secret Sifted Key
                        for the Classical Post-Processing Phase of the Qiskrypt's Noiseless
                        DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
                        """

                        logger_info_message(
                            "    3.4.3) Global QBER (Quantum Bit Error Rate): {}"
                            .format(self.get_global_quantum_bit_error_rate())
                        )
                        """
                        Log an 'INFO' message for the global QBER (Quantum Bit Error Rate)
                        obtained from the procedure of the Parameter Estimation performed on
                        the Qiskrypt's Secret Sifted Key for the Classical Post-Processing Phase of
                        the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
                        """

                    else:
                        """
                        If the Qiskrypt's Secret Sifted Keys of the sender and the receiver
                        Qiskrypt's Party Clients of the Qiskrypt's Noiseless DV (Discrete Variables)
                        BKMPS22 Protocol with No Eavesdropping does not have the same length.
                        """

                        # TODO Throw - Exception

                else:
                    """
                    If the Qiskrypt's Secret Sifted Keys of the sender and/or the receiver
                    Qiskrypt's Party Clients of the Qiskrypt's Noiseless DV (Discrete Variables)
                    BKMPS22 Protocol with No Eavesdropping are not Qiskrypt's Secret Sifted Keys.
                    """

                    # TODO Throw - Exception

            else:
                """
                If the sender and/or receiver Qiskrypt's Party Clients of
                the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol
                with No Eavesdropping are not Qiskrypt's Party Clients.
                """

                # TODO Throw - Exception

            logger_info_message(
                "    3.5) Finishing the Parameter Estimation procedure for\n"
                "                   the Classical Post-Processing Phase of the Qiskrypt's Noiseless\n"
                "                   DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping..."
            )
            """
            Log an 'INFO' message for the finish of the procedure of the Parameter Estimation of
            the Qiskrypt's Secret Sifted Key for the Classical Post-Processing Phase of
            the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
            """

        else:
            """
            If the Qiskrypt's Key Exchange Protocol is not configured.
            """

            # TODO Throw - Exception

    def reconcile_information(self):
        """
        Reconcile the Information for the
        Qiskrypt's Semi-Quantum Conference Key Agreement (SQCKA).
        """

        if self.is_configured():
            """
            If the Qiskrypt's Key Exchange Protocol is already configured.
            """

            logger_info_message(
                "    3.6) Starting the Error Reconciliation procedure for\n"
                "                   the Classical Post-Processing Phase of the Qiskrypt's Noiseless\n"
                "                   DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping..."
            )
            """
            Log an 'INFO' message for the start of the procedure of the Error Reconciliation of
            the remaining not discarded bits of the Qiskrypt's Secure Sifted Key for
            the Classical Post-Processing Phase of the Qiskrypt's Noiseless
            DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
            """

            if self.get_global_quantum_bit_error_rate() > 0:
                """
                If the global QBER (Quantum Bit Error Rate) of the rounds estimated during
                the Parameter Estimation of the Qiskrypt's DV (Discrete Variables) BKMPS22 Protocol
                is greater than zero (0).

                NOTE:
                - In this case, the global QBER (Quantum Bit Error Rate) should always be equal to zero (0),
                  since there is no noise in the Quantum Communications and no action of a possible eavesdropper.
                - This case it is only checked to keep the coherence of the behavior of the protocol,
                  and it is not even necessary to apply an Error Correction Code to the remaining bits of
                  the Qiskrypt's Secret Sifted Key which were not discarded after
                  the Parameter Estimation procedure.
                """

                # TODO Throw - Exception

            logger_info_message(
                "    3.7) Finishing the Error Reconciliation procedure for\n"
                "                   the Classical Post-Processing Phase of the Qiskrypt's Noiseless\n"
                "                   DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping..."
            )
            """
            Log an 'INFO' message for the finish of the procedure of the Error Reconciliation of
            the remaining not discarded bits of the Qiskrypt's Secure Sifted Key for
            the Classical Post-Processing Phase of the Qiskrypt's Noiseless
            DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
            """

            logger_info_message(
                "    3.8) Retrieving the information about the Qiskrypt's Secret Reconciled Keys\n"
                "                   obtained after the Information Reconciliation procedure of\n"
                "                   the Classical Post-Processing Phase of the Qiskrypt's Noiseless\n"
                "                   DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping:"
            )
            """
            Log an 'INFO' message for the retrieval of the information about
            the Qiskrypt's Secret Reconciled Keys obtained after the Information Reconciliation procedure
            of the Classical Post-Processing Phase of the Qiskrypt's Noiseless DV (Discrete Variables)
            BKMPS22 Protocol with No Eavesdropping.
            """

            sender_reconciled_key_secret_bits = "0b"
            """
            Initialise the binary string for the bits used to build
            the Qiskrypt's Secret Reconciled Key of the sender Qiskrypt's Party Client.
            """

            receiver_reconciled_key_secret_bits = "0b"
            """
            Initialise the binary string for the bits used to build
            the Qiskrypt's Secret Reconciled Key of the receiver Qiskrypt's Party Client.
            """

            num_rounds_for_quantum_transmission_phase = \
                self.get_num_rounds_for_quantum_transmission_phase()
            """
            Retrieve the number of rounds for the Quantum Transmission Phase in
            the Qiskrypt's Quantum Key Exchange Protocol.
            """

            quantum_transmission_phase_rounds = \
                self.get_quantum_transmission_phase_rounds()
            """
            Retrieve the list for the Quantum Transmission Phase of 
            the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
            """

            for current_num_round_for_quantum_transmission_phase in \
                    range(num_rounds_for_quantum_transmission_phase):
                """
                For each round of the Quantum Transmission Phase of 
                the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
                """

                current_round_for_quantum_transmission_phase = \
                    quantum_transmission_phase_rounds[current_num_round_for_quantum_transmission_phase]
                """
                Retrieve the current round of the Quantum Transmission Phase of 
                the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
                """

                if isinstance(current_round_for_quantum_transmission_phase,
                              QiskryptNoiselessDVBKMPS22ProtocolWithNoEavesdroppingQuantumTransmissionPhaseRound):
                    """
                    If the current round of the Quantum Transmission Phase of 
                    the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping is
                    really a Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol
                    with No Eavesdropping Quantum Transmission Phase Round.
                    """

                    if not current_round_for_quantum_transmission_phase.is_round_discarded():
                        """
                        If the current round of the Quantum Transmission Phase of
                        the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping,
                        is not a discarded round.
                        """

                        sender_secret_bit = \
                            current_round_for_quantum_transmission_phase \
                            .get_round_quantum_circuit().get_qiskrypt_classical_register(0).get_bit(0)
                        """
                        Retrieve the secret bit in the sender Qiskrypt's Classical Register of
                        the Qiskrypt's Quantum Circuit for the current round of the Quantum Transmission Phase of
                        the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
                        """

                        sender_reconciled_key_secret_bits += str(sender_secret_bit)
                        """
                        Append the secret bit in the sender Qiskrypt's Classical Register of
                        the Qiskrypt's Quantum Circuit for the current round of the Quantum Transmission Phase of
                        the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping
                        to the binary string to be used to build the Qiskrypt's Secret Reconciled Key for
                        the sender Qiskrypt's Client Party.
                        """

                        receiver_secret_bit = \
                            current_round_for_quantum_transmission_phase \
                            .get_round_quantum_circuit().get_qiskrypt_classical_register(1).get_bit(0)
                        """
                        Retrieve the secret bit in the receiver Qiskrypt's Classical Register of
                        the Qiskrypt's Quantum Circuit for the current round of the Quantum Transmission Phase of
                        the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
                        """

                        receiver_reconciled_key_secret_bits += str(receiver_secret_bit)
                        """
                        Append the secret bit in the receiver Qiskrypt's Classical Register of
                        the Qiskrypt's Quantum Circuit for the current round of the Quantum Transmission Phase of
                        the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping
                        to the binary string to be used to build the Qiskrypt's Secret Reconciled Key for
                        the receiver Qiskrypt's Client Party.
                        """

            sender_party_client = \
                self.get_communication_session().get_sender_party_clients()[0]
            """
            Retrieve the sender Qiskrypt's Party Client from the Qiskrypt's Communication Session of
            the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
            """

            receiver_party_client = \
                self.get_communication_session().get_receiver_party_clients()[0]
            """
            Retrieve the receiver Qiskrypt's Party Client from the Qiskrypt's Communication Session of
            the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
            """

            if isinstance(sender_party_client, QiskryptPartyClient) and \
                    isinstance(receiver_party_client, QiskryptPartyClient):
                """
                If the sender and receiver Qiskrypt's Party Clients of
                the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol
                with No Eavesdropping are really Qiskrypt's Party Clients.
                """

                sender_party_name = sender_party_client.get_party().get_name()
                """
                Retrieve the name of the sender Qiskrypt's Party.
                """

                sender_party_num = sender_party_client.get_party().get_num()
                """
                Retrieve the number of the sender Qiskrypt's Party.                
                """

                receiver_party_name = receiver_party_client.get_party().get_name()
                """
                Retrieve the name of the receiver Qiskrypt's Party.
                """

                receiver_party_num = receiver_party_client.get_party().get_num()
                """
                Retrieve the number of the receiver Qiskrypt's Party.                
                """

                sender_party_client_uuid = sender_party_client.get_uuid()
                """
                Retrieve the UUID (Universally Unique IDentifier) of the sender Qiskrypt's Client.
                """

                sender_secret_reconciled_key = QiskryptSecretReconciledKey(sender_reconciled_key_secret_bits,
                                                                           sender_party_client_uuid)
                """
                Create a Qiskrypt's Secret Reconciled Key for the sender Qiskrypt's Client.
                """

                receiver_party_client_uuid = receiver_party_client.get_uuid()
                """
                Retrieve the UUID (Universally Unique IDentifier) of the receiver Qiskrypt's Client.
                """

                receiver_secret_reconciled_key = QiskryptSecretReconciledKey(receiver_reconciled_key_secret_bits,
                                                                             receiver_party_client_uuid)
                """
                Create a Qiskrypt's Secret Reconciled Key for the receiver Qiskrypt's Client.
                """

                sender_secret_reconciled_key_privacy_level = \
                    sender_secret_reconciled_key.get_key_privacy_level()
                """
                Retrieve the privacy level of the Qiskrypt's Key for the sender Qiskrypt's Client.
                """

                sender_secret_reconciled_key_type = \
                    sender_secret_reconciled_key.get_key_type()
                """
                Retrieve the type of the Qiskrypt's Key for the sender Qiskrypt's Client.
                """

                receiver_secret_reconciled_key_privacy_level = \
                    receiver_secret_reconciled_key.get_key_privacy_level()
                """
                Retrieve the privacy level of the Qiskrypt's Key for the receiver Qiskrypt's Client.
                """

                receiver_secret_reconciled_key_type = \
                    receiver_secret_reconciled_key.get_key_type()
                """
                Retrieve the type of the Qiskrypt's Key for the receiver Qiskrypt's Client.
                """

                sender_secret_reconciled_key_id = \
                    "{} {} ({}_{} ; {}_{})".format(sender_secret_reconciled_key_privacy_level.lower(),
                                                   sender_secret_reconciled_key_type.lower(),
                                                   sender_party_name.lower(), sender_party_num,
                                                   receiver_party_name.lower(), receiver_party_num)
                """
                Set up the identifier of the Qiskrypt's Secret Reconciled Key for
                the sender Qiskrypt's Client.
                """

                sender_party_client.add_item(sender_secret_reconciled_key_id, sender_secret_reconciled_key)
                """
                Add a new item to keep the Qiskrypt's Secret Reconciled Key for
                the sender Qiskrypt's Client.
                """

                receiver_secret_reconciled_key_id = \
                    "{} {} ({}_{} ; {}_{})".format(receiver_secret_reconciled_key_privacy_level.lower(),
                                                   receiver_secret_reconciled_key_type.lower(),
                                                   receiver_party_name.lower(), receiver_party_num,
                                                   sender_party_name.lower(), sender_party_num)
                """
                Set up the identifier of the Qiskrypt's Secret Reconciled Key for
                the receiver Qiskrypt's Client.
                """

                receiver_party_client.add_item(receiver_secret_reconciled_key_id, receiver_secret_reconciled_key)
                """
                Add a new item to keep the Qiskrypt's Secret Reconciled Key for
                the receiver Qiskrypt's Client.
                """

                sender_secret_reconciled_key = \
                    sender_party_client.get_item_value_by_key(sender_secret_reconciled_key_id)
                """
                Retrieve the Qiskrypt's Secret Reconciled Key for
                the sender Qiskrypt's Client. 
                """

                receiver_secret_reconciled_key = \
                    receiver_party_client.get_item_value_by_key(receiver_secret_reconciled_key_id)
                """
                Retrieve the Qiskrypt's Secret Reconciled Key for
                the receiver Qiskrypt's Client. 
                """

                if isinstance(sender_secret_reconciled_key, QiskryptSecretReconciledKey) and \
                        isinstance(receiver_secret_reconciled_key, QiskryptSecretReconciledKey):
                    """
                    If both sender's and receiver's Qiskrypt's Secret Reconciled Keys are
                    really Qiskrypt's Secret Reconciled Keys.
                    """

                    logger_info_message(
                        "    3.8.1) Secret Reconciled Key #1 -> {}: {}"
                        .format(sender_secret_reconciled_key_id,
                                sender_secret_reconciled_key.get_bits()[BINARY_FORMAT_START_OFFSET:])
                    )
                    """
                    Log an 'INFO' message for the sender's Qiskrypt's Secret Reconciled Key.
                    """

                    logger_info_message(
                        "    3.8.2) Secret Reconciled Key #2 -> {}: {}"
                        .format(receiver_secret_reconciled_key_id,
                                receiver_secret_reconciled_key.get_bits()[BINARY_FORMAT_START_OFFSET:])
                    )
                    """
                    Log an 'INFO' message for the receiver's Qiskrypt's Secret Reconciled Key.
                    """

                else:
                    """
                    If the sender's and/or receiver's Qiskrypt's Secret Reconciled Keys are
                    not Qiskrypt's Secret Reconciled Keys.
                    """

                    # TODO Throw - Exception

            else:
                """
                If the sender and/or receiver Qiskrypt's Party Clients of
                the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol
                with No Eavesdropping are not Qiskrypt's Party Clients.
                """

                # TODO Throw - Exception

        else:
            """
            If the Qiskrypt's Key Exchange Protocol is not configured.
            """

            # TODO Throw - Exception

    def amplify_privacy(self):
        """
        Amplify the Privacy for the
        Qiskrypt's Semi-Quantum Conference Key Agreement (SQCKA).
        """

        if self.is_configured():
            """
            If the Qiskrypt's Key Exchange Protocol is already configured.
            """

            logger_info_message(
                "    3.9) Starting the Privacy Amplification procedure for\n"
                "                   the Classical Post-Processing Phase of the Qiskrypt's Noiseless\n"
                "                   DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping..."
            )
            """
            Log an 'INFO' message for the start of the procedure of the Privacy Amplification of
            the bits of the error-free Qiskrypt's Secure Reconciled Key for
            the Classical Post-Processing Phase of the Qiskrypt's Noiseless
            DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
            """

            sender_party_client = \
                self.get_communication_session().get_sender_party_clients()[0]
            """
            Retrieve the sender Qiskrypt's Party Client from the Qiskrypt's Communication Session of
            the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
            """

            receiver_party_client = \
                self.get_communication_session().get_receiver_party_clients()[0]
            """
            Retrieve the receiver Qiskrypt's Party Client from the Qiskrypt's Communication Session of
            the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
            """

            if isinstance(sender_party_client, QiskryptPartyClient) and \
                    isinstance(receiver_party_client, QiskryptPartyClient):
                """
                If the sender and receiver Qiskrypt's Party Clients of
                the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol
                with No Eavesdropping are really Qiskrypt's Party Clients.
                """

                sender_party_name = sender_party_client.get_party().get_name()
                """
                Retrieve the name of the sender Qiskrypt's Party.
                """

                sender_party_num = sender_party_client.get_party().get_num()
                """
                Retrieve the number of the sender Qiskrypt's Party.                
                """

                receiver_party_name = receiver_party_client.get_party().get_name()
                """
                Retrieve the name of the receiver Qiskrypt's Party.
                """

                receiver_party_num = receiver_party_client.get_party().get_num()
                """
                Retrieve the number of the receiver Qiskrypt's Party.                
                """

                sender_secret_reconciled_key_id = \
                    "{} {} ({}_{} ; {}_{})".format(POSSIBLE_KEY_PRIVACY_LEVELS[0].lower(),
                                                   POSSIBLE_KEY_TYPES[2].lower(),
                                                   sender_party_name.lower(), sender_party_num,
                                                   receiver_party_name.lower(), receiver_party_num)
                """
                Set up the identifier of the Qiskrypt's Secret Reconciled Key for
                the sender Qiskrypt's Client.
                """

                receiver_secret_reconciled_key_id = \
                    "{} {} ({}_{} ; {}_{})".format(POSSIBLE_KEY_PRIVACY_LEVELS[0].lower(),
                                                   POSSIBLE_KEY_TYPES[2].lower(),
                                                   receiver_party_name.lower(), receiver_party_num,
                                                   sender_party_name.lower(), sender_party_num)
                """
                Set up the identifier of the Qiskrypt's Secret Reconciled Key for
                the receiver Qiskrypt's Client.
                """

                sender_secret_reconciled_key = \
                    sender_party_client.get_item_value_by_key(sender_secret_reconciled_key_id)
                """
                Retrieve the Qiskrypt's Secret Reconciled Key for
                the sender Qiskrypt's Client. 
                """

                receiver_secret_reconciled_key = \
                    receiver_party_client.get_item_value_by_key(receiver_secret_reconciled_key_id)
                """
                Retrieve the Qiskrypt's Secret Reconciled Key for
                the receiver Qiskrypt's Client. 
                """

                if isinstance(sender_secret_reconciled_key, QiskryptSecretReconciledKey) and \
                        isinstance(receiver_secret_reconciled_key, QiskryptSecretReconciledKey):
                    """
                    If the Qiskrypt's Secret Reconciled Keys of the sender and the receiver
                    Qiskrypt's Party Clients of the Qiskrypt's Noiseless DV (Discrete Variables)
                    BKMPS22 Protocol with No Eavesdropping are really Qiskrypt's Secret Reconciled Keys.
                    """

                    sender_sha_256_instance = sha_256()
                    """
                    Initialise the SHA-256 (Secure-Hash Algorithm for 256 bits) for
                    the sender Qiskrypt's Client.
                    """

                    receiver_sha_256_instance = sha_256()
                    """
                    Initialise the SHA-256 (Secure-Hash Algorithm for 256 bits) for
                    the receiver Qiskrypt's Client.
                    """

                    sender_secret_reconciled_key_bytes = \
                        QiskryptClassicalUtilities.convert_binary_string_to_bytes(
                            sender_secret_reconciled_key.get_bits()
                        )
                    """
                    Convert the bits Qiskrypt's Secret Reconciled Key of
                    the sender Qiskrypt's Party Client to bytes.
                    """

                    receiver_secret_reconciled_key_bytes = \
                        QiskryptClassicalUtilities.convert_binary_string_to_bytes(
                            receiver_secret_reconciled_key.get_bits()
                        )
                    """
                    Convert the bits Qiskrypt's Secret Reconciled Key of
                    the receiver Qiskrypt's Party Client to bytes.
                    """

                    sender_sha_256_instance.update(sender_secret_reconciled_key_bytes)
                    """
                    Update the SHA-256 (Secure-Hash Algorithm for 256 bits) for
                    the sender Qiskrypt's Client with its respective Qiskrypt's Secret Reconciled Key. 
                    """

                    receiver_sha_256_instance.update(receiver_secret_reconciled_key_bytes)
                    """
                    Update the SHA-256 (Secure-Hash Algorithm for 256 bits) for
                    the receiver Qiskrypt's Client with its respective Qiskrypt's Secret Reconciled Key. 
                    """

                    sender_sha_256_digest = sender_sha_256_instance.digest()
                    """
                    Digest the data in bytes of the Qiskrypt's Secret Reconciled Key of
                    the sender Qiskrypt's Client from the SHA-256 (Secure-Hash Algorithm for 256 bits).
                    """

                    receiver_sha_256_digest = receiver_sha_256_instance.digest()
                    """
                    Digest the data in bytes of the Qiskrypt's Secret Reconciled Key of
                    the receiver Qiskrypt's Client from the SHA-256 (Secure-Hash Algorithm for 256 bits).
                    """

                    sender_secure_key_secret_bits = "{:08b}".format(int(sender_sha_256_digest.hex(), 16))
                    """
                    Convert digested data in bytes of the Qiskrypt's Secret Reconciled Key of
                    the sender Qiskrypt's Client from the SHA-256 (Secure-Hash Algorithm for 256 bits) to bits.
                    """

                    receiver_secure_key_secret_bits = "{:08b}".format(int(receiver_sha_256_digest.hex(), 16))
                    """
                    Convert digested data in bytes of the Qiskrypt's Secret Reconciled Key of
                    the receiver Qiskrypt's Client from the SHA-256 (Secure-Hash Algorithm for 256 bits) to bits.
                    """

                    sender_party_client_uuid = sender_party_client.get_uuid()
                    """
                    Retrieve the UUID (Universally Unique IDentifier) of the sender Qiskrypt's Client.
                    """

                    sender_secret_secure_key = QiskryptSecretSecureKey(sender_secure_key_secret_bits,
                                                                       sender_party_client_uuid)
                    """
                    Create a Qiskrypt's Secret Secure Key for the sender Qiskrypt's Client.
                    """

                    receiver_party_client_uuid = receiver_party_client.get_uuid()
                    """
                    Retrieve the UUID (Universally Unique IDentifier) of the receiver Qiskrypt's Client.
                    """

                    receiver_secret_secure_key = QiskryptSecretSecureKey(receiver_secure_key_secret_bits,
                                                                         receiver_party_client_uuid)
                    """
                    Create a Qiskrypt's Secret Secure Key for the receiver Qiskrypt's Client.
                    """

                    sender_secret_secure_key_privacy_level = \
                        sender_secret_secure_key.get_key_privacy_level()
                    """
                    Retrieve the privacy level of the Qiskrypt's Key for the sender Qiskrypt's Client.
                    """

                    sender_secret_secure_key_type = \
                        sender_secret_secure_key.get_key_type()
                    """
                    Retrieve the type of the Qiskrypt's Key for the sender Qiskrypt's Client.
                    """

                    receiver_secret_secure_key_privacy_level = \
                        receiver_secret_secure_key.get_key_privacy_level()
                    """
                    Retrieve the privacy level of the Qiskrypt's Key for the receiver Qiskrypt's Client.
                    """

                    receiver_secret_secure_key_type = \
                        receiver_secret_secure_key.get_key_type()
                    """
                    Retrieve the type of the Qiskrypt's Key for the receiver Qiskrypt's Client.
                    """

                    sender_secret_secure_key_id = \
                        "{} {} ({}_{} ; {}_{})".format(sender_secret_secure_key_privacy_level.lower(),
                                                       sender_secret_secure_key_type.lower(),
                                                       sender_party_name.lower(), sender_party_num,
                                                       receiver_party_name.lower(), receiver_party_num)
                    """
                    Set up the identifier of the Qiskrypt's Secret Secure Key for
                    the sender Qiskrypt's Client.
                    """

                    sender_party_client.add_item(sender_secret_secure_key_id, sender_secret_secure_key)
                    """
                    Add a new item to keep the Qiskrypt's Secret Secure Key for
                    the sender Qiskrypt's Client.
                    """

                    receiver_secret_secure_key_id = \
                        "{} {} ({}_{} ; {}_{})".format(receiver_secret_secure_key_privacy_level.lower(),
                                                       receiver_secret_secure_key_type.lower(),
                                                       receiver_party_name.lower(), receiver_party_num,
                                                       sender_party_name.lower(), sender_party_num)
                    """
                    Set up the identifier of the Qiskrypt's Secret Secure Key for
                    the receiver Qiskrypt's Client.
                    """

                    receiver_party_client.add_item(receiver_secret_secure_key_id, receiver_secret_secure_key)
                    """
                    Add a new item to keep the Qiskrypt's Secret Secure Key for
                    the receiver Qiskrypt's Client.
                    """

                else:
                    """
                    If the Qiskrypt's Secret Reconciled Keys of the sender and/or the receiver
                    Qiskrypt's Party Clients of the Qiskrypt's Noiseless DV (Discrete Variables)
                    BKMPS22 Protocol with No Eavesdropping are not Qiskrypt's Secret Reconciled Keys.
                    """

                    # TODO Throw - Exception

            else:
                """
                If the sender and/or receiver Qiskrypt's Party Clients of
                the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol
                with No Eavesdropping are not Qiskrypt's Party Clients.
                """

                # TODO Throw - Exception

            logger_info_message(
                "    3.10) Finishing the Privacy Amplification procedure for\n"
                "                    the Classical Post-Processing Phase of the Qiskrypt's Noiseless\n"
                "                    DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping..."
            )
            """
            Log an 'INFO' message for the finish of the procedure of the Privacy Amplification of
            the bits of the error-free Qiskrypt's Secure Reconciled Key for
            the Classical Post-Processing Phase of the Qiskrypt's Noiseless
            DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
            """

            logger_info_message(
                "    3.11) Retrieving the information about the Qiskrypt's Secret Secure Keys\n"
                "                    obtained after the Privacy Amplification procedure of\n"
                "                    the Classical Post-Processing Phase of the Qiskrypt's Noiseless\n"
                "                    DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping:"
            )
            """
            Log an 'INFO' message for the retrieval of the information about
            the Qiskrypt's Secret Secure Keys obtained after the Privacy Amplification procedure
            of the Classical Post-Processing Phase of the Qiskrypt's Noiseless DV (Discrete Variables)
            BKMPS22 Protocol with No Eavesdropping.
            """

            sender_party_client = \
                self.get_communication_session().get_sender_party_clients()[0]
            """
            Retrieve the sender Qiskrypt's Party Client from the Qiskrypt's Communication Session of
            the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
            """

            receiver_party_client = \
                self.get_communication_session().get_receiver_party_clients()[0]
            """
            Retrieve the receiver Qiskrypt's Party Client from the Qiskrypt's Communication Session of
            the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
            """

            if isinstance(sender_party_client, QiskryptPartyClient) and \
                    isinstance(receiver_party_client, QiskryptPartyClient):
                """
                If the sender and receiver Qiskrypt's Party Clients of
                the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol
                with No Eavesdropping are really Qiskrypt's Party Clients.
                """

                sender_party_name = sender_party_client.get_party().get_name()
                """
                Retrieve the name of the sender Qiskrypt's Party.
                """

                sender_party_num = sender_party_client.get_party().get_num()
                """
                Retrieve the number of the sender Qiskrypt's Party.                
                """

                receiver_party_name = receiver_party_client.get_party().get_name()
                """
                Retrieve the name of the receiver Qiskrypt's Party.
                """

                receiver_party_num = receiver_party_client.get_party().get_num()
                """
                Retrieve the number of the receiver Qiskrypt's Party.                
                """

                sender_secret_secure_key_id = \
                    "{} {} ({}_{} ; {}_{})".format(POSSIBLE_KEY_PRIVACY_LEVELS[0].lower(),
                                                   POSSIBLE_KEY_TYPES[3].lower(),
                                                   sender_party_name.lower(), sender_party_num,
                                                   receiver_party_name.lower(), receiver_party_num)
                """
                Set up the identifier of the Qiskrypt's Secret Secure Key for
                the sender Qiskrypt's Client.
                """

                receiver_secret_secure_key_id = \
                    "{} {} ({}_{} ; {}_{})".format(POSSIBLE_KEY_PRIVACY_LEVELS[0].lower(),
                                                   POSSIBLE_KEY_TYPES[3].lower(),
                                                   receiver_party_name.lower(), receiver_party_num,
                                                   sender_party_name.lower(), sender_party_num)
                """
                Set up the identifier of the Qiskrypt's Secret Secure Key for
                the receiver Qiskrypt's Client.
                """

                sender_secret_secure_key = \
                    sender_party_client.get_item_value_by_key(sender_secret_secure_key_id)
                """
                Retrieve the Qiskrypt's Secret Secure Key for
                the sender Qiskrypt's Client. 
                """

                receiver_secret_secure_key = \
                    receiver_party_client.get_item_value_by_key(receiver_secret_secure_key_id)
                """
                Retrieve the Qiskrypt's Secret Secure Key for
                the receiver Qiskrypt's Client. 
                """

                if isinstance(sender_secret_secure_key, QiskryptSecretSecureKey) and \
                        isinstance(receiver_secret_secure_key, QiskryptSecretSecureKey):
                    """
                    If both sender's and receiver's Qiskrypt's Secret Secure Keys are
                    really Qiskrypt's Secret Secure Keys.
                    """

                    logger_info_message(
                        "    3.11.1) Secret Secure Key #1 -> {}: {}"
                        .format(sender_secret_secure_key_id,
                                sender_secret_secure_key.get_bits()[BINARY_FORMAT_START_OFFSET:])
                    )
                    """
                    Log an 'INFO' message for the sender's Qiskrypt's Secret Secure Key.
                    """

                    logger_info_message(
                        "    3.11.2) Secret Secure Key #2 -> {}: {}"
                        .format(receiver_secret_secure_key_id,
                                receiver_secret_secure_key.get_bits()[BINARY_FORMAT_START_OFFSET:])
                    )
                    """
                    Log an 'INFO' message for the receiver's Qiskrypt's Secret Secure Key.
                    """

                    if sender_secret_secure_key.get_bits() == receiver_secret_secure_key.get_bits():
                        """
                        If the two Qiskrypt's Secret Secure Keys are equal,
                        the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol
                        with no Eavesdropping executed with success. 
                        """

                        logger_info_message("    3.12) Execution of the Quantum Key Exchange was SUCCESSFUL!\n"
                                            "                    The Qiskrypt's Secret Secure Keys agreed between\n"
                                            "                    the two parties at the end of the protocol are equal!")
                        """
                        Log an 'INFO' message reporting that the execution of
                        the Qiskrypt's Quantum Key Exchange was SUCCESSFUL!
                        """

                    else:
                        """
                        If the two Qiskrypt's Secret Secure Keys are different,
                        the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol
                        with no Eavesdropping did not execute with success. 
                        """

                        logger_info_message("3.12) Execution of the Quantum Key Exchange was NOT SUCCESSFUL!\n"
                                            "       The Secure Keys agreed at the end of the protocol\n"
                                            "       are different!")
                        """
                        Log an 'INFO' message reporting that the execution of
                        the Qiskrypt's Quantum Key Exchange was NOT SUCCESSFUL!
                        """

                else:
                    """
                    If the sender's and/or receiver's Qiskrypt's Secret Secure Keys are
                    not Qiskrypt's Secret Secure Keys.
                    """

                    # TODO Throw - Exception

            else:
                """
                If the sender and/or receiver Qiskrypt's Party Clients of
                the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol
                with No Eavesdropping are not Qiskrypt's Party Clients.
                """

                # TODO Throw - Exception

        else:
            """
            If the Qiskrypt's Key Exchange Protocol is not configured.
            """

            # TODO Throw - Exception

    def is_configured(self) -> bool:
        """
        Return the boolean flag to determine if the Qiskrypt's Key Exchange Protocol
        is configured.

        :return self.configured: the boolean flag to determine if the Qiskrypt's Key Exchange Protocol
                                 is configured.
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

        if not super().is_configured():
            """
            If the boolean flag to determine if the Qiskrypt's Key Exchange Protocol
            is configured, as False.
            """

            super().set_as_configured()
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

    def get_semi_quantum_conference_key_agreement_type(self) -> str:
        """
        Return the type of the Qiskrypt's Semi-Quantum Conference Key Agreement (SQCKA).

        :return self.quantum_key_distribution_type: the type of the Qiskrypt's
                                                    Semi-Quantum Conference Key Agreement (SQCKA).
        """

        """
        Return the type of the Qiskrypt's Semi-Quantum Conference Key Agreement (SQCKA).
        """
        return self.semi_quantum_conference_key_agreement_type

    def get_sender_name(self) -> str:
        """
        Return the name of the sender in the Qiskrypt's Noiseless DV (Discrete Variables)
        BKMPS22 Protocol with No Eavesdropping.

        :return self.sender_name: the name of the sender in the Qiskrypt's Noiseless DV (Discrete Variables)
                                  BKMPS22 Protocol with No Eavesdropping.
        """

        """
        Return the name of the sender in the Qiskrypt's Noiseless DV (Discrete Variables)
        BKMPS22 Protocol with No Eavesdropping.
        """
        return self.sender_name

    def get_receivers_names(self) -> str:
        """
        Return the names of the receivers in the Qiskrypt's Noiseless DV (Discrete Variables)
        BKMPS22 Protocol with No Eavesdropping.

        :return self.receivers_names: the names of the receivers in the Qiskrypt's Noiseless DV (Discrete Variables)
                                      BKMPS22 Protocol with No Eavesdropping.
        """

        """
        Return the names of the receivers in the Qiskrypt's Noiseless DV (Discrete Variables)
        BKMPS22 Protocol with No Eavesdropping.
        """
        return self.receivers_names

    def get_sender_address(self) -> str:
        """
        Return the address of the sender in the Qiskrypt's Noiseless DV (Discrete Variables)
        BKMPS22 Protocol with No Eavesdropping.

        :return self.sender_address: the address of the sender in the Qiskrypt's Noiseless DV (Discrete Variables)
                                     BKMPS22 Protocol with No Eavesdropping.
        """

        """
        Return the address of the sender in the Qiskrypt's Noiseless DV (Discrete Variables)
        BKMPS22 Protocol with No Eavesdropping.
        """
        return self.sender_address

    def get_receivers_addresses(self) -> list:
        """
        Return the addresses of the receivers in the Qiskrypt's Noiseless DV (Discrete Variables)
        BKMPS22 Protocol with No Eavesdropping.

        :return self.receivers_addresses: the addresses of the receivers in the Qiskrypt's
                                          Noiseless DV (Discrete Variables)
                                          BKMPS22 Protocol with No Eavesdropping.
        """

        """
        Return the address of the receiver in the Qiskrypt's Noiseless DV (Discrete Variables)
        BKMPS22 Protocol with No Eavesdropping.
        """
        return self.receivers_addresses

    def get_quantum_transmission_phase_rounds(self) -> list:
        """
        Return the list of the rounds for the Quantum Transmission Phase of
        the Qiskrypt's Quantum Key Exchange Protocol.

        :return super().get_quantum_transmission_phase_rounds(): the list of the rounds for
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

        :return super().get_quantum_transmission_phase_rounds_not_discarded_from_key_sifting():
                the list of the rounds for the Quantum Transmission Phase of
                the Qiskrypt's Semi-Quantum Conference Key Agreement (SQCKA) not discarded from the Key Sifting.
        """

        """
        Return the list of the rounds for the Quantum Transmission Phase of
        the Qiskrypt's Semi-Quantum Conference Key Agreement (SQCKA) not discarded from the Key Sifting.
        """
        return super().get_quantum_transmission_phase_rounds_not_discarded_from_key_sifting()

    def get_quantum_transmission_phase_rounds_not_discarded_from_parameter_estimation(self) -> list:
        """
        Return the list of the rounds for the Quantum Transmission Phase of
        the Qiskrypt's Semi-Quantum Conference Key Agreement (SQCKA) not discarded
        from the Parameter Estimation.

        :return super().get_quantum_transmission_phase_rounds_not_discarded_from_parameter_estimation():
                the list of the rounds for the Quantum Transmission Phase of
                the Qiskrypt's Semi-Quantum Conference Key Agreement (SQCKA) not discarded
                from the Parameter Estimation.
        """

        """
        Return the list of the rounds for the Quantum Transmission Phase of
        the Qiskrypt's Semi-Quantum Conference Key Agreement (SQCKA) not discarded
        from the Parameter Estimation.
        """
        return super().get_quantum_transmission_phase_rounds_not_discarded_from_parameter_estimation()

    def get_quantum_bit_error_rate_z_basis(self) -> float:
        """
        Return the QBER (Quantum Bit Error Rate) of the Z-Basis (Standard Computational Basis) Rounds
        estimated during the Parameter Estimation of the Qiskrypt's DV (Discrete Variables) BKMPS22 Protocol.

        :return super().get_quantum_bit_error_rate_z_basis(): the QBER (Quantum Bit Error Rate) of
                                                              the Z-Basis (Standard Computational Basis) Rounds
                                                              estimated during the Parameter Estimation of
                                                              the Qiskrypt's DV (Discrete Variables) BKMPS22 Protocol.
        """

        """
        Return the QBER (Quantum Bit Error Rate) of the Z-Basis (Standard Computational Basis) Rounds
        estimated during the Parameter Estimation of the Qiskrypt's DV (Discrete Variables) BKMPS22 Protocol.
        """
        return super().get_quantum_bit_error_rate_z_basis()

    def get_quantum_bit_error_rate_x_basis(self) -> float:
        """
        Return the QBER (Quantum Bit Error Rate) of the X-Basis (Hadamard Basis) Rounds
        estimated during the Parameter Estimation of the Qiskrypt's DV (Discrete Variables) BKMPS22 Protocol.

        :return self.quantum_bit_error_rates[1]: the QBER (Quantum Bit Error Rate) of
                                                 the X-Basis (Hadamard Basis) Rounds
                                                 estimated during the Parameter Estimation of
                                                 the Qiskrypt's DV (Discrete Variables) BKMPS22 Protocol.
        """

        """
        Return the QBER (Quantum Bit Error Rate) of the X-Basis (Hadamard Basis) Rounds
        estimated during the Parameter Estimation of the Qiskrypt's DV (Discrete Variables) BKMPS22 Protocol.
        """
        return super().get_quantum_bit_error_rate_x_basis()

    def get_global_quantum_bit_error_rate(self) -> float:
        """
        Return the global QBER (Quantum Bit Error Rate) of the rounds estimated during
        the Parameter Estimation of the Qiskrypt's DV (Discrete Variables) BKMPS22 Protocol.

        :return super().get_global_quantum_bit_error_rate(): the global QBER (Quantum Bit Error Rate) of
                                                             the rounds estimated during the Parameter Estimation of
                                                             the Qiskrypt's DV (Discrete Variables) BKMPS22 Protocol.
        """

        """
        Return the global QBER (Quantum Bit Error Rate) of the rounds estimated during
        the Parameter Estimation of the Qiskrypt's DV (Discrete Variables) BKMPS22 Protocol.
        """
        return super().get_global_quantum_bit_error_rate()

    def update_quantum_bit_error_rate_z_basis(self, quantum_bit_error_rate_z_basis: float) -> None:
        """
        Update the QBER (Quantum Bit Error Rate) of the Z-Basis (Standard Computational Basis) Rounds
        estimated during the Parameter Estimation of the Qiskrypt's DV (Discrete Variables) BKMPS22 Protocol.

        :param quantum_bit_error_rate_z_basis: the QBER (Quantum Bit Error Rate) of
                                               the Z-Basis (Standard Computational Basis) Rounds
                                               estimated during the Parameter Estimation of
                                               the Qiskrypt's DV (Discrete Variables) BKMPS22 Protocol.
        """

        """
        Update the QBER (Quantum Bit Error Rate) of the Z-Basis (Standard Computational Basis) Rounds
        estimated during the Parameter Estimation of the Qiskrypt's DV (Discrete Variables) BKMPS22 Protocol.
        """
        super().update_quantum_bit_error_rate_z_basis(quantum_bit_error_rate_z_basis)

    def update_quantum_bit_error_rate_x_basis(self, quantum_bit_error_rate_x_basis: float) -> None:
        """
        Update the QBER (Quantum Bit Error Rate) of the X-Basis (Hadamard Basis) Rounds
        estimated during the Parameter Estimation of the Qiskrypt's DV (Discrete Variables) BKMPS22 Protocol.

        :param quantum_bit_error_rate_x_basis: the QBER (Quantum Bit Error Rate) of
                                               the X-Basis (Hadamard Basis) Rounds
                                               estimated during the Parameter Estimation of
                                               the Qiskrypt's DV (Discrete Variables) BKMPS22 Protocol.
        """

        """
        Update the QBER (Quantum Bit Error Rate) of the X-Basis (Hadamard Basis) Rounds
        estimated during the Parameter Estimation of the Qiskrypt's DV (Discrete Variables) BKMPS22 Protocol.
        """
        super().update_quantum_bit_error_rate_x_basis(quantum_bit_error_rate_x_basis)

    def configure(self) -> None:
        """
        Configure the Qiskrypt's Noiseless DV (Discrete Variables)
        BKMPS22 Protocol with No Eavesdropping.
        """

        if not self.is_configured():
            """
            If the Qiskrypt's Key Exchange Protocol is not configured yet.
            """

            QiskryptClassicalUtilities.waiting_animation()
            """
            Call the waiting animation from the Qiskrypt's Classical Utilities.
            """

            logger_info_message(" 1) Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol\n"
                                "              starts being configured...")
            """
            Log an 'INFO' message for the Qiskrypt's Noiseless DV (Discrete Variables) starts being configured.
            """

            logger_info_message("    1.1) Starting the creation of the Qiskrypt's Entities and\n"
                                "                   respective distances for the Qiskrypt's Noiseless\n"
                                "                   DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping...")
            """
            Log an 'INFO' message for the start of the procedure of the creation of
            the Qiskrypt's Entities and respective distances for the Qiskrypt's Noiseless
            DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
            """

            entities_and_distances_in_kms_list = \
                QiskryptNoiselessDVBKMPS22ProtocolWithNoEavesdropping \
                .create_entities_and_distances_in_kms([self.get_sender_name(), self.get_receivers_names()],
                                                      [self.get_sender_address(), self.get_receivers_addresses()])
            """
            Create the list of two Qiskrypt's Entities and respective distances
            in KMs (Kilometers) between them for the Qiskrypt's Noiseless DV (Discrete Variables)
            BKMPS22 Protocol with No Eavesdropping.
            """

            logger_info_message("    1.2) Finishing the creation of the Qiskrypt's Entities and\n"
                                "                   respective distances for the Qiskrypt's Noiseless\n"
                                "                   DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping...")
            """
            Log an 'INFO' message for the finish of the procedure of the creation of
            the Qiskrypt's Entities and respective distances for the Qiskrypt's Noiseless
            DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
            """

            entities = entities_and_distances_in_kms_list[0]
            """
            Retrieve the list of two Qiskrypt's Entities for
            the Qiskrypt's Noiseless DV (Discrete Variables)
            BKMPS22 Protocol with No Eavesdropping.
            """

            distances_in_kms = entities_and_distances_in_kms_list[1]
            """
            Retrieve the list of respective distances in KMs (Kilometers) between
            the two Qiskrypt's Entities for the Qiskrypt's Noiseless DV (Discrete Variables)
            BKMPS22 Protocol with No Eavesdropping.
            """

            logger_info_message("    1.3) Starting the creation of the template of\n"
                                "                   the Qiskrypt's Quantum Circuit for each round of\n"
                                "                   the Qiskrypt's Communication Session,\n"
                                "                   from the Qiskrypt's Registers retrieved of\n"
                                "                   the sender and receiver Qiskrypt's Party Clients,\n"
                                "                   and respective associated Qiskrypt's Link connecting them\n"
                                "                   for the Qiskrypt's Noiseless DV (Discrete Variables)\n"
                                "                   BKMPS22 Protocol with No Eavesdropping...")
            """
            Log an 'INFO' message for the start of the procedure of the creation of
            the template of the Qiskrypt's Quantum Circuit for each round of
            the Qiskrypt's Communication Session, from the Qiskrypt's Registers retrieved of
            the sender and receiver Qiskrypt's Party Clients, and respective associated
            Qiskrypt's Link connecting them for the Qiskrypt's Noiseless DV (Discrete Variables)
            BKMPS22 Protocol with No Eavesdropping.
            """

            template_quantum_circuit_of_quantum_transmission_phase, communication_session = \
                QiskryptNoiselessDVBKMPS22ProtocolWithNoEavesdropping \
                .create_template_quantum_circuit_and_communication_session_of_quantum_transmission_phase \
                (entities, distances_in_kms, verbose=self.is_verbose())
            """
            Create the template of the Qiskrypt's Quantum Circuit for each round of
            the Qiskrypt's Communication Session, from the Qiskrypt's Registers retrieved of
            the sender and receiver Qiskrypt's Party Clients, and respective associated
            Qiskrypt's Link connecting them for the Qiskrypt's Noiseless DV (Discrete Variables)
            BKMPS22 Protocol with No Eavesdropping.
            """

            logger_info_message("    1.4) Finishing the creation of the template of\n"
                                "                   the Qiskrypt's Quantum Circuit for each round of\n"
                                "                   the Qiskrypt's Communication Session,\n"
                                "                   from the Qiskrypt's Registers retrieved of\n"
                                "                   the sender and receiver Qiskrypt's Party Clients,\n"
                                "                   and respective associated Qiskrypt's Link connecting them\n"
                                "                   for the Qiskrypt's Noiseless DV (Discrete Variables)\n"
                                "                   BKMPS22 Protocol with No Eavesdropping...")
            """
            Log an 'INFO' message for the finish of the procedure of the creation of
            the template of the Qiskrypt's Quantum Circuit for each round of
            the Qiskrypt's Communication Session, from the Qiskrypt's Registers retrieved of
            the sender and receiver Qiskrypt's Party Clients, and respective associated
            Qiskrypt's Link connecting them for the Qiskrypt's Noiseless DV (Discrete Variables)
            BKMPS22 Protocol with No Eavesdropping.
            """

            self.set_communication_session(communication_session)
            """
            Set the Qiskrypt's Communication Session for
            the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
            """

            logger_info_message("    1.5) Starting the creation of the secret bits for\n"
                                "                   the sender's Qiskrypt's Secure Raw Key and for each round of\n"
                                "                   the Quantum Transmission Phase of the Qiskrypt's Noiseless\n"
                                "                   DV (Discrete Variables) BKMPS22 Protocol with\n"
                                "                   No Eavesdropping in the sender's side...")
            """
            Log an 'INFO' message for the start of the procedure of
            the creation of the secret bits for the sender's Qiskrypt's Secure Raw Key
            and for each round of the Qiskrypt's Noiseless DV (Discrete Variables)
            BKMPS22 Protocol with No Eavesdropping in the sender's side.
            """

            for current_num_round_for_quantum_transmission_phase in \
                    range(self.get_num_rounds_for_quantum_transmission_phase()):
                """
                For each round of the Quantum Transmission Phase in
                the Qiskrypt's Quantum Key Exchange Protocol.
                """

                quantum_coin_tossing_sender_secret_bit = \
                    QiskryptQuantumCoinTossing("qu_coin_toss_sender_secret_bit")
                """
                Create a Qiskrypt's Quantum Coin Tossing for the choice of Secret Bit for the sender.
                """

                quantum_coin_tossing_sender_secret_bit.initialise_qiskrypt_quantum_circuit()
                """
                Initialise the Qiskrypt's Quantum Circuit for
                the Qiskrypt's Quantum Coin Tossing for the choice of Secret Bit for the sender.
                """

                quantum_coin_tossing_sender_secret_bit.toss_coin()
                """
                Toss the Coin related to the Qiskrypt's Quantum Coin Tossing
                for the choice of Secret Bit for the sender.
                """

                sender_secret_bit = \
                    quantum_coin_tossing_sender_secret_bit.get_coin_tossing_outcome_bit_as_int_base_2()
                """
                Retrieve the classical secret bit from the Qiskrypt's Coin Tossing,
                for the choice of Secret Bit for the sender through
                the execution of the respective Qiskrypt's Quantum Circuit,
                in an integer base-2 format (i.e., an integer representation of a bit).
                """

                quantum_coin_tossing_sender_random_basis = \
                    QiskryptQuantumCoinTossing("qu_coin_toss_sender_random_basis")
                """
                Create a Qiskrypt's Quantum Coin Tossing for the choice of Random Basis for the sender.
                """

                quantum_coin_tossing_sender_random_basis.initialise_qiskrypt_quantum_circuit()
                """
                Initialise the Qiskrypt's Quantum Circuit for
                the Qiskrypt's Quantum Coin Tossing for the choice of Random Basis for the sender.
                """

                quantum_coin_tossing_sender_random_basis.toss_coin()
                """
                Toss the Coin related to the Qiskrypt's Quantum Coin Tossing
                for the choice of Random Basis for the sender.
                """

                sender_random_basis_bit = \
                    quantum_coin_tossing_sender_random_basis.get_coin_tossing_outcome_bit_as_int_base_2()
                """
                Retrieve the classical bit from the Qiskrypt's Coin Tossing,
                for the choice of Random Basis for the sender through
                the execution of the respective Qiskrypt's Quantum Circuit,
                in an integer base-2 format (i.e., an integer representation of a bit).
                """

                current_round_type_for_quantum_transmission_phase = None
                """
                Initialise the type of the current round of Quantum Transmission Phase of
                the Qiskrypt's Qiskrypt's DV (Discrete Variables) BKMPS22 Protocol.
                """

                if sender_random_basis_bit == 0:
                    """
                    If the classical bit from the Qiskrypt's Coin Tossing,
                    for the choice of Random Basis for the sender is zero (0).
                    """

                    current_round_type_for_quantum_transmission_phase = \
                        POSSIBLE_DV_BKMPS22_PROTOCOL_ROUND_TYPES_QUANTUM_TRANSMISSION_PHASE[0]
                    """
                    Set the type of the current round of Quantum Transmission Phase of
                    the Qiskrypt's Qiskrypt's DV (Discrete Variables) BKMPS22 Protocol,
                    as a 'Z-BASIS ROUND'.
                    """

                elif sender_random_basis_bit == 1:
                    """
                    If the classical bit from the Qiskrypt's Coin Tossing,
                    for the choice of Random Basis for the sender is one (1).
                    """

                    current_round_type_for_quantum_transmission_phase = \
                        POSSIBLE_DV_BKMPS22_PROTOCOL_ROUND_TYPES_QUANTUM_TRANSMISSION_PHASE[1]
                    """
                    Set the type of the current round of Quantum Transmission Phase of
                    the Qiskrypt's Qiskrypt's DV (Discrete Variables) BKMPS22 Protocol,
                    as a 'X-BASIS ROUND'.
                    """

                current_round_quantum_circuit = \
                    deep_copy(template_quantum_circuit_of_quantum_transmission_phase)
                """
                Create the Qiskrypt's Quantum Circuit from the a deep copy of
                the template of the Qiskrypt's Quantum Circuit for each round of
                the Qiskrypt's Communication Session, from the Qiskrypt's Registers retrieved of
                the sender and receiver Qiskrypt's Party Clients, and respective associated
                Qiskrypt's Link connecting them for the Qiskrypt's Noiseless DV (Discrete Variables)
                BKMPS22 Protocol with No Eavesdropping.
                """

                if sender_secret_bit == 0:
                    """
                    If the classical bit from the Qiskrypt's Coin Tossing,
                    for the choice of Secret Bit for the sender is zero (0).
                    """

                    current_round_quantum_circuit.get_qiskrypt_classical_register(0).buffer_bit(0)
                    """
                    Buffer the Secret Bit in the Qiskrypt's Classical Register of
                    the Qiskrypt's Quantum Circuit for the current round of Quantum Transmission Phase of
                    the Qiskrypt's Qiskrypt's DV (Discrete Variables) BKMPS22 Protocol. 
                    """

                elif sender_secret_bit == 1:
                    """
                    If the classical bit from the Qiskrypt's Coin Tossing,
                    for the choice of Secret Bit for the sender is one (1).
                    """

                    current_round_quantum_circuit.get_qiskrypt_classical_register(0).invert_bit(0)
                    """
                    Invert the Secret Bit in the Qiskrypt's Classical Register of
                    the Qiskrypt's Quantum Circuit for the current round of Quantum Transmission Phase of
                    the Qiskrypt's Qiskrypt's DV (Discrete Variables) BKMPS22 Protocol. 
                    """

                current_round_for_quantum_transmission_phase = \
                    QiskryptNoiselessDVBKMPS22ProtocolWithNoEavesdroppingQuantumTransmissionPhaseRound \
                    ((current_num_round_for_quantum_transmission_phase + 1),
                     current_round_type_for_quantum_transmission_phase,
                     current_round_quantum_circuit)
                """
                Create the current Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol
                with No Eavesdropping Quantum Transmission Phase Round of the current round.
                """

                self.quantum_transmission_phase_rounds \
                    .append(current_round_for_quantum_transmission_phase)
                """
                Append the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol
                with No Eavesdropping Quantum Transmission Phase Round of the current round to
                the list of the rounds for the Quantum Transmission Phase of
                the Qiskrypt's Noiseless DV (Discrete Variables)
                BKMPS22 Protocol with No Eavesdropping.
                """

            logger_info_message("    1.6) Finishing the creation of the secret bits for\n"
                                "                   the sender's Qiskrypt's Secure Raw Key and for each round of\n"
                                "                   the Quantum Transmission Phase of the Qiskrypt's Noiseless\n"
                                "                   DV (Discrete Variables) BKMPS22 Protocol with\n"
                                "                   No Eavesdropping in the sender's side...")
            """
            Log an 'INFO' message for the finish of the procedure of
            the creation of the secret bits for the sender's Qiskrypt's Secure Raw Key
            and for each round of the Qiskrypt's Noiseless DV (Discrete Variables)
            BKMPS22 Protocol with No Eavesdropping in the sender's side.
            """

            self.set_as_configured()
            """
            Set the Qiskrypt's Key Exchange Protocol as configured.
            """

            logger_info_message(" 1) Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol\n"
                                "              is finally configured!")
            """
            Log an 'INFO' message for the Qiskrypt's Noiseless DV (Discrete Variables) is finally configured.
            """

        else:
            """
            If the Qiskrypt's Key Exchange Protocol is already configured.
            """

            # TODO Throw - Exception

    @staticmethod
    def create_entities_and_distances_in_kms(names: list, addresses: list) -> list:
        """
        Create and return the list of two Qiskrypt's Entities
        and respective distances in KMs (Kilometers) between them for
        the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.

        NOTE:
        - The both lists of names and addresses should be in the order: [sender, receiver].

        :param names: the list of names for the Qiskrypt's Entities.
        :param addresses: the list of distances in KMs (Kilometers) between the Qiskrypt's Entities.

        :return [entities, distances_in_kms]: the list of two Qiskrypt's Entities
                                              and respective distance in KMs (Kilometers) between them.
        """

        qiskrypt_geocoding = QiskryptGeocoding()
        """
        Create a Qiskrypt's Geocoding object.
        """

        qiskrypt_geocoding.initialise_with_default_geocoder_service()
        """
        Initialise the Qiskrypt's Geocoding object with the default Geocoder service.
        """

        num_names = len(names)
        """
        Retrieve the number of names.
        """

        num_addresses = len(addresses)
        """
        Retrieve the number of addresses.
        """

        if num_names == num_addresses >= MINIMUM_SEMI_QUANTUM_CONFERENCE_KEY_AGREEMENT_NUM_PARTIES:
            """
            If the number of names is equal to the number of addresses,
            and are both greater or equal to 2.
            """

            entities = list()
            """
            Create an empty list for the two Qiskrypt's Entities to be added to
            the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
            """

            distances_in_kms = list()
            """
            Create an empty list for the distance between the two Qiskrypt's Entities to be added to
            the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
            """

            for current_name_index, current_address_index in \
                    zip(range(num_names), range(num_addresses)):
                """
                For each pair of indexes of the list of names and addresses.
                """

                current_name = names[current_name_index]
                """
                Retrieve the current name.
                """

                current_address = addresses[current_address_index]
                """
                Retrieve the current location address.
                """

                if isinstance(current_name, str) and \
                        isinstance(current_address, str):
                    """
                    If both current name and address are strings.
                    """

                    current_location_address = qiskrypt_geocoding \
                        .get_location_address_from_address(current_address)
                    """
                    Retrieve the current location address.
                    """

                    current_longitude = \
                        float(qiskrypt_geocoding.get_location_longitude_from_address(current_location_address))
                    """
                    Retrieve the current longitude.
                    """

                    current_latitude = \
                        float(qiskrypt_geocoding.get_location_latitude_from_address(current_location_address))
                    """
                    Retrieve the current latitude.
                    """

                    current_altitude_in_kms = \
                        qiskrypt_geocoding.get_location_altitude_in_kms_from_address_using_open_elevation(
                            current_location_address
                        )
                    """
                    Retrieve the current altitude in KMs (Kilometers).
                    """

                    current_entity = \
                        QiskryptEntity(current_name, current_location_address,
                                       current_longitude, current_latitude, current_altitude_in_kms)
                    """
                    Create the current Qiskrypt's Entity.
                    """

                    entities.append(current_entity)
                    """
                    Append the current Qiskrypt's Entity to the list of two Qiskrypt's Entities for
                    the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
                    """

                else:
                    """
                    If some current name and/or location address are not strings.
                    """

                    # TODO Throw - Exception

            for current_num_receiver_entity in range( (num_addresses - 1) ):
                """
                For each number of Qiskrypt's Entity (receiver) for
                the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
                """

                location_address_1 = entities[0].get_location_address()
                """
                Retrieve the location address of the 1st Qiskrypt's Entity (sender) for
                the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
                """

                location_address_2 = entities[(current_num_receiver_entity + 1)].get_location_address()
                """
                Retrieve the location address of the 2nd Qiskrypt's Entity (receiver) for
                the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
                """

                distance_in_kms = qiskrypt_geocoding \
                    .compute_distance_between_locations_from_addresses_in_kms_using_osmr(location_address_1,
                                                                                         location_address_2)
                """
                Compute the distance in KMs (Kilometers) between
                the 1st Qiskrypt's Entity (sender) and 2nd Qiskrypt's Entity (receiver) for
                the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
                """

                altitude_in_kms_1 = entities[0].get_altitude_in_kms()
                """
                Retrieve the altitude in KMs (Kilometers) of the 1st Qiskrypt's Entity (sender) for
                the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
                """

                altitude_in_kms_2 = entities[1].get_altitude_in_kms()
                """
                Retrieve the altitude in KMs (Kilometers) of the 2nd Qiskrypt's Entity (receiver) for
                the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
                """

                altitude_in_kms_difference = abs((altitude_in_kms_1 - altitude_in_kms_2))
                """
                Compute the difference between the altitudes in KMs (Kilometers) between
                the 1st Qiskrypt's Entity (sender) and 2nd Qiskrypt's Entity (receiver) for
                the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
                """

                distance_in_kms += altitude_in_kms_difference
                """
                Sum the difference between the altitudes in KMs (Kilometers) between
                the 1st Qiskrypt's Entity (sender) and 2nd Qiskrypt's Entity (receiver) to
                the distance in KMs (Kilometers) between them for
                the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
                """

                distances_in_kms.append( (2 * distance_in_kms) )
                """
                Append the distance in KMs (Kilometers) between
                the 1st Qiskrypt's Entity (sender) and 2nd Qiskrypt's Entity (receiver) to
                the list of distances in KMs (Kilometers) for
                the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping
                (i.e., the double of the distance for going forward and backward medium).
                """

            """
            Return the list of two Qiskrypt's Entities
            and respective distance in KMs (Kilometers) between them for
            the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
            """
            return [entities, distances_in_kms]

        else:
            """
            If the number of names is not equal to the number of location addresses.
            """

            # TODO Throw - Exception

    @staticmethod
    def create_template_quantum_circuit_and_communication_session_of_quantum_transmission_phase \
            (entities_list: list, distances_in_kms_list: list, verbose=True):
        """
        Create and return the template of the Qiskrypt's Quantum Circuit for each round of
        the Qiskrypt's Communication Session, from the Qiskrypt's Registers retrieved of
        the sender and receiver Qiskrypt's Party Clients, and respective associated
        Qiskrypt's Link connecting them for the Qiskrypt's Noiseless DV (Discrete Variables)
        BKMPS22 Protocol with No Eavesdropping.

        :param entities_list: the list of Qiskrypt's Entities.
        :param distances_in_kms_list: the list of distances between Qiskrypt's Entities.
        :param verbose: the boolean flag to show the runtime information about
                        the Qiskrypt's Quantum Cryptographic Primitive.

        :return template_quantum_circuit_of_quantum_transmission_phase, communication_session:
                the template of the Qiskrypt's Quantum Circuit for each round of
                the Qiskrypt's Communication Session, from the Qiskrypt's Registers retrieved of
                the sender and receiver Qiskrypt's Party Clients, and respective associated
                Qiskrypt's Link connecting them, as well as the Qiskrypt's Communication Session itself,
                for the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
        """

        if verbose:
            """
            If the boolean flag to show the runtime information about
            the Qiskrypt's Quantum Cryptographic Primitive, is set as True.
            """

            logging_basic_configuration(level=WARNING)
            """
            Start the Basic Configuration for the logger of messages,
            with the 'WARNING' severity level.
            """

        num_entities = len(entities_list)
        """
        Retrieve the number of Qiskrypt's Entities,
        from the given list of Qiskrypt's Entities.
        """

        num_distances_in_kms = len(distances_in_kms_list)
        """
        Retrieve the number of distances in KMs (Kilometers),
        from the given list of distances in KMs (Kilometers).
        """

        if num_entities >= MINIMUM_SEMI_QUANTUM_CONFERENCE_KEY_AGREEMENT_NUM_PARTIES:
            """
            If the number of given Qiskrypt's Entities is greater or equal to
            the number of parties for a Semi-Quantum Conference Key Agreement (SQCKA).
            """

            party_clients_list = []
            """
            Create an empty list for the Qiskrypt's Party Clients for the Qiskrypt's BKMPS22 Protocol Round
            with Discrete Variables (DVs) for Noiseless Scenarios and No Eavesdropping.
            """

            for current_num_party in range(num_entities):
                """
                For each respective party for the Qiskrypt's BKMPS22 Protocol Round
                with Discrete Variables (DVs) for Noiseless Scenarios and No Eavesdropping.
                """

                current_entity = entities_list[current_num_party]
                """
                Retrieve the current Qiskrypt's Entity.
                """

                if isinstance(current_entity, QiskryptEntity):
                    """
                    If the current Qiskrypt's Entity is really a Qiskrypt's Entity.
                    """

                    current_entity_name = current_entity.get_name()
                    """
                    Retrieve the name of the current Qiskrypt's Entity.
                    """

                    current_entity_longitude = str(current_entity.get_longitude())
                    """
                    Retrieve the longitude of the current Qiskrypt's Entity.
                    """

                    current_entity_latitude = str(current_entity.get_latitude())
                    """
                    Retrieve the latitude of the current Qiskrypt's Entity.
                    """

                    current_entity_altitude_in_kms = str(current_entity.get_altitude_in_kms())
                    """
                    Retrieve the altitude in KMs (Kilometers) of the current Qiskrypt's Entity.
                    """

                    current_party = QiskryptParty(current_num_party, current_entity_name)
                    """
                    Create the Qiskrypt's Party for
                    the current Qiskrypt's Party Client. 
                    """

                    if current_num_party == 0:
                        """
                        If the current party for the Qiskrypt's BKMPS22 Protocol Round
                        with Discrete Variables (DVs) for Noiseless Scenarios and No Eavesdropping is the first one.
                        """

                        current_fully_quantum_ground_station_endpoint = \
                            QiskryptFullyQuantumGroundStationEndpoint(current_num_party,
                                                                      current_entity_name,
                                                                      current_entity_longitude,
                                                                      current_entity_latitude,
                                                                      current_entity_altitude_in_kms)
                        """
                        Create the Qiskrypt's Fully-Quantum Ground Station Endpoint for
                        the current Qiskrypt's Party Client. 
                        """

                        current_classical_ground_station_endpoint = \
                            QiskryptClassicalGroundStationEndpoint(current_num_party,
                                                                   current_entity_name,
                                                                   current_entity_longitude,
                                                                   current_entity_latitude,
                                                                   current_entity_altitude_in_kms)
                        """
                        Create the Qiskrypt's Classical Ground Station Endpoint for
                        the current Qiskrypt's Party Client. 
                        """

                        current_endpoints_list = [current_fully_quantum_ground_station_endpoint,
                                                  current_classical_ground_station_endpoint]
                        """
                        Create a list of Qiskrypt's Endpoints for the current Qiskrypt's Party Client.
                        """

                        current_party_client = QiskryptPartyClient()
                        """
                        Create the current Qiskrypt's Party Client.
                        """

                        current_party_client.connect(current_party, current_endpoints_list)
                        """
                        Establish a connection between the Qiskrypt's Party and
                        the respective Qiskrypt's Fully-Quantum and Classical Ground Stations created for
                        the current Qiskrypt's Party Client.
                        """

                        current_fully_quantum_register = \
                            QiskryptFullyQuantumRegister(name="{}-qu-reg".format(current_entity_name),
                                                         num_qubits=num_entities, qiskit_quantum_register=None)
                        """
                        Create the Qiskrypt's Fully-Quantum Register for the current Qiskrypt's Party Client.
                        """

                        current_party_client.add_fully_quantum_register(current_fully_quantum_register, 0)
                        """
                        Add the Qiskrypt's Fully-Quantum Register to the current Qiskrypt's Party Client.
                        """

                        current_classical_register = \
                            QiskryptClassicalRegister(name="{}-cl-reg".format(current_entity_name),
                                                      num_bits=1, qiskit_classical_register=None)
                        """
                        Create the Qiskrypt's Classical Register for the current Qiskrypt's Party Client.
                        """

                        current_party_client.add_classical_register(current_classical_register, 1)
                        """
                        Add the Qiskrypt's Classical Register to the current Qiskrypt's Party Client.
                        """

                        party_clients_list.append(current_party_client)
                        """
                        Append the current Qiskrypt's Party Client to
                        the list of Qiskrypt's Party Clients.
                        """

                    else:
                        """
                        If the current party for the Qiskrypt's BKMPS22 Protocol Round
                        with Discrete Variables (DVs) for Noiseless Scenarios and
                        No Eavesdropping is not the first one.
                        """

                        current_semi_quantum_ground_station_endpoint = \
                            QiskryptSemiQuantumGroundStationEndpoint(current_num_party,
                                                                     current_entity_name,
                                                                     current_entity_longitude,
                                                                     current_entity_latitude,
                                                                     current_entity_altitude_in_kms)
                        """
                        Create the Qiskrypt's Semi-Quantum Ground Station Endpoint for
                        the current Qiskrypt's Party Client. 
                        """

                        current_classical_ground_station_endpoint = \
                            QiskryptClassicalGroundStationEndpoint(current_num_party,
                                                                   current_entity_name,
                                                                   current_entity_longitude,
                                                                   current_entity_latitude,
                                                                   current_entity_altitude_in_kms)
                        """
                        Create the Qiskrypt's Classical Ground Station Endpoint for
                        the current Qiskrypt's Party Client. 
                        """

                        current_endpoints_list = [current_semi_quantum_ground_station_endpoint,
                                                  current_classical_ground_station_endpoint]
                        """
                        Create a list of Qiskrypt's Endpoints for the current Qiskrypt's Party Client.
                        """

                        current_party_client = QiskryptPartyClient()
                        """
                        Create the current Qiskrypt's Party Client.
                        """

                        current_party_client.connect(current_party, current_endpoints_list)
                        """
                        Establish a connection between the Qiskrypt's Party and
                        the respective Qiskrypt's Semi-Quantum and Classical Ground Stations created for
                        the current Qiskrypt's Party Client.
                        """

                        current_semi_quantum_register = \
                            QiskryptSemiQuantumRegister(name="{}-qu-reg".format(current_entity_name),
                                                        num_qubits=1, qiskit_quantum_register=None)
                        """
                        Create the Qiskrypt's Semi-Quantum Register for the current Qiskrypt's Party Client.
                        """

                        current_party_client.add_semi_quantum_register(current_semi_quantum_register, 0)
                        """
                        Add the Qiskrypt's Semi-Quantum Register to the current Qiskrypt's Party Client.
                        """

                        current_classical_register = \
                            QiskryptClassicalRegister(name="{}-cl-reg".format(current_entity_name),
                                                      num_bits=1, qiskit_classical_register=None)
                        """
                        Create the Qiskrypt's Classical Register for the current Qiskrypt's Party Client.
                        """

                        current_party_client.add_classical_register(current_classical_register, 1)
                        """
                        Add the Qiskrypt's Classical Register to the current Qiskrypt's Party Client.
                        """

                        party_clients_list.append(current_party_client)
                        """
                        Append the current Qiskrypt's Party Client to
                        the list of Qiskrypt's Party Clients.
                        """

                else:
                    """
                    If the current Qiskrypt's Entity is not a Qiskrypt's Entity.
                    """

                    # TODO Throw - Exception

            if num_distances_in_kms == (num_entities - 1):
                """
                If the number of given distances in KMs (Kilometers) is equal to
                the number of parties for a Semi-Quantum Conference Key Agreement (SQCKA) minus one.
                """

                fiber_optic_medium = QiskryptFiberOpticMedium(0, "fib_op", distances_in_kms_list[0])
                """
                Create a Qiskrypt's Fiber Optic Medium.
                """

                fiber_optic_mediums_list = [fiber_optic_medium]
                """
                Create a list of Qiskrypt's Fiber Optic Mediums.
                """

                directions_list = [POSSIBLE_COMMUNICATION_CHANNEL_DIRECTIONS[0],
                                   POSSIBLE_COMMUNICATION_CHANNEL_DIRECTIONS[6]]
                """
                Create a list of directions for the Quantum Communication Channel.
                """

                quantum_communication_channel = \
                    QiskryptUnicastNoiselessDVQuantumCommunicationChannel(0, "dv_qu_ch", directions_list)
                """
                Create a Qiskrypt's Unicast Noiseless DV (Discrete Variable) Quantum Communication Channel.
                """

                quantum_communication_channel.set_installed(True)
                """
                Install the Quantum Communication Channel.
                """

                quantum_register = QiskryptFullyQuantumRegister(name="dv_qu_ch_{}".format(0),
                                                                num_qubits=1, qiskit_quantum_register=None)
                """
                Create a Qiskrypt's Quantum Register for the Qiskrypt's Link.

                NOTE:
                - It is assumed any Qiskrypt's Quantum Register for the Qiskrypt's Link to be a
                  Qiskrypt's Fully-Quantum Register.
                """

                quantum_registers_list = [quantum_register]
                """
                Create the list of Qiskrypt's Quantum Registers for the Qiskrypt's Link.
                """

                link = QiskryptLink((num_entities - 1))
                """
                Create the Qiskrypt's Link.
                """

                link.establish(fiber_optic_mediums_list, quantum_communication_channel)
                """
                Establish a Qiskrypt's Link from a list of Qiskrypt's Mediums
                and a Qiskrypt's Communication Channel.
                """

                link.set_quantum_registers(quantum_registers_list)
                """
                Set the list of Qiskrypt's Quantum Registers to be
                the Qiskrypt's Registers of the Qiskrypt's Link, if it is possible
                """

                communication_session = \
                    QiskryptCommunicationSession("noiseless_dv_BKMPS22_protocol_with_no_eavesdropping_session")
                """
                Create the Qiskrypt's Communication Session for
                the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
                """

                party_clients_list[0].add_role(POSSIBLE_CLIENT_ROLES[0])
                """
                Add the role of 'sender' to the sender Qiskrypt's Party Client.
                """

                sender_party_clients_list = [party_clients_list[0]]
                """
                Create the list for the sender Qiskrypt's Party Clients.
                """

                party_clients_list[1].add_role(POSSIBLE_CLIENT_ROLES[1])
                """
                Add the role of 'receiver' to the receiver Qiskrypt's Party Client.
                """

                receiver_party_clients_list = [party_clients_list[1]]
                """
                Create the list for the receiver Qiskrypt's Party Clients.
                """

                communication_session.start(sender_party_clients_list, link, receiver_party_clients_list,
                                            timeout_in_secs=300)
                """
                Start the Qiskrypt's Communication Session for
                the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
                """

                template_quantum_circuit_of_quantum_transmission_phase = \
                    communication_session.generate_base_quantum_circuit()
                """
                Generate the template of the Qiskrypt's Quantum Circuit for each round of
                the Qiskrypt's Communication Session, from the Qiskrypt's Registers retrieved of
                the sender and receiver Qiskrypt's Party Clients, and respective associated
                Qiskrypt's Link connecting them for the Qiskrypt's Noiseless DV (Discrete Variables)
                BKMPS22 Protocol with No Eavesdropping.
                """

                if verbose:
                    """
                    If the boolean flag to show the runtime information about
                    the Qiskrypt's Quantum Cryptographic Primitive, is set as True.
                    """

                    logging_basic_configuration(level=INFO)
                    """
                    Start the Basic Configuration for the logger of messages,
                    with the 'INFO' severity level.
                    """

                """
                Return the template of the Qiskrypt's Quantum Circuit for each round of
                the Qiskrypt's Communication Session, from the Qiskrypt's Registers retrieved of
                the sender and receiver Qiskrypt's Party Clients, and respective associated
                Qiskrypt's Link connecting them, as well as the Qiskrypt's Communication Session itself,
                for the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol with No Eavesdropping.
                """
                return template_quantum_circuit_of_quantum_transmission_phase, communication_session

            else:
                """
                If the number of given distances in KMs (Kilometers) is not equal to
                the number of parties for a Semi-Quantum Conference Key Agreement (SQCKA) minus one.
                """

                # TODO Throw - Exception

        else:
            """
            If the number of given Qiskrypt's Entities is lower than
            the number of parties for a Semi-Quantum Conference Key Agreement (SQCKA).
            """

            # TODO Throw - Exception

    @staticmethod
    def create_default_receivers_names(num_receivers: int):
        """
        Create and return the list of the names of the receivers for
        the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol.

        :param num_receivers: the number of the receivers for the Qiskrypt's
                              Noiseless DV (Discrete Variables) BKMPS22 Protocol.

        :return receivers_names: the list of the names of the receivers for the Qiskrypt's
                                 Noiseless DV (Discrete Variables) BKMPS22 Protocol.
        """

        if num_receivers >= 1:
            """
            If the number of the receivers for the Qiskrypt's
            Noiseless DV (Discrete Variables) BKMPS22 Protocol is valid.
            """

            receivers_names = \
                [SEMI_QUANTUM_CONFERENCE_KEY_AGREEMENT_DEFAULT_PARTIES_NAMES[1].lower()] * num_receivers
            """
            Initialise the list of the names of the receivers for the Qiskrypt's
            Noiseless DV (Discrete Variables) BKMPS22 Protocol.
            """

            for current_num_receiver in range(num_receivers):
                """
                For each number of receiver of the Qiskrypt's
                Noiseless DV (Discrete Variables) BKMPS22 Protocol.
                """

                receivers_names[current_num_receiver] += "_{}".format( (current_num_receiver + 1) )
                """
                Redefine the list of the names of the receivers for the Qiskrypt's
                Noiseless DV (Discrete Variables) BKMPS22 Protocol.
                """

            """
            Return the list of the names of the receivers for the Qiskrypt's
            Noiseless DV (Discrete Variables) BKMPS22 Protocol.
            """
            return receivers_names

        else:
            """
            If the number of the receivers for the Qiskrypt's
            Noiseless DV (Discrete Variables) BKMPS22 Protocol is not valid.
            """

            # TODO - Throw Exception

    @staticmethod
    def create_default_receivers_addresses(num_receivers: int):
        """
        Create and return the list of the addresses of the receivers for
        the Qiskrypt's Noiseless DV (Discrete Variables) BKMPS22 Protocol.

        :param num_receivers: the number of the receivers for the Qiskrypt's
                              Noiseless DV (Discrete Variables) BKMPS22 Protocol.

        :return receivers_addresses: the list of the addresses of the receivers for the Qiskrypt's
                                     Noiseless DV (Discrete Variables) BKMPS22 Protocol.
        """

        if num_receivers >= 1:
            """
            If the number of the receivers for the Qiskrypt's
            Noiseless DV (Discrete Variables) BKMPS22 Protocol is valid.
            """

            default_receivers_addresses_list = \
                [
                    QiskryptGeographicAddressEnumeration.INSTITUTO_SUPERIOR_TECNICO_PORTUGAL,
                    QiskryptGeographicAddressEnumeration.FACULTY_SCIENCES_OF_UNIVERSITY_OF_LISBON_PORTUGAL,
                    QiskryptGeographicAddressEnumeration.ISCTE_INSTITUTO_UNIVERSITARIO_DE_LISBOA_PORTUGAL,
                    QiskryptGeographicAddressEnumeration.ISEL_INSTITUTO_SUPERIOR_DE_ENGENHARIA_DE_LISBOA_PORTUGAL,
                    QiskryptGeographicAddressEnumeration.FACULTY_ENGINEERING_OF_UNIVERSITY_OF_PORTO_PORTUGAL,
                    QiskryptGeographicAddressEnumeration.FACULTY_SCIENCES_OF_UNIVERSITY_OF_PORTO_PORTUGAL,
                    QiskryptGeographicAddressEnumeration.ISEP_INSTITUTO_SUPERIOR_DE_ENGENHARIA_DO_PORTO_PORTUGAL
                ]
            """
            Initialise the list of default addresses of the receivers for the Qiskrypt's
            Noiseless DV (Discrete Variables) BKMPS22 Protocol.
            """

            num_default_receivers_addresses = len(default_receivers_addresses_list)
            """
            Retrieve the number of default addresses of the receivers for the Qiskrypt's
            Noiseless DV (Discrete Variables) BKMPS22 Protocol.
            """

            if num_receivers <= num_default_receivers_addresses:
                """
                If the number of the receivers for the Qiskrypt's
                Noiseless DV (Discrete Variables) BKMPS22 Protocol
                is lower or equal to the number of default addresses of
                the receivers for the Qiskrypt's Noiseless
                DV (Discrete Variables) BKMPS22 Protocol. 
                """

                receivers_addresses = list()
                """
                Initialise the list of the addresses of the receivers for the Qiskrypt's
                Noiseless DV (Discrete Variables) BKMPS22 Protocol.
                """

                for current_num_receiver in range(num_receivers):
                    """
                    For each number of receiver of the Qiskrypt's
                    Noiseless DV (Discrete Variables) BKMPS22 Protocol.
                    """

                    receivers_addresses.append(default_receivers_addresses_list[current_num_receiver])
                    """
                    Redefine the list of the names of the receivers for the Qiskrypt's
                    Noiseless DV (Discrete Variables) BKMPS22 Protocol.
                    """

            else:
                """
                If the number of the receivers for the Qiskrypt's
                Noiseless DV (Discrete Variables) BKMPS22 Protocol
                is higher than the number of default addresses of
                the receivers for the Qiskrypt's Noiseless
                DV (Discrete Variables) BKMPS22 Protocol. 
                """

                # TODO - Throw Exception

        else:
            """
            If the number of the receivers for the Qiskrypt's
            Noiseless DV (Discrete Variables) BKMPS22 Protocol is not valid.
            """

            # TODO - Throw Exception
