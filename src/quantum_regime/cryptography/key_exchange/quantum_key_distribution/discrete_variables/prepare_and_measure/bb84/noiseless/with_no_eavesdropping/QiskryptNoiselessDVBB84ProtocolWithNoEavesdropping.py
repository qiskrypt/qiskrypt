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

from copy import deepcopy as deep_copy
"""
Import the Deep Copy method from
the Copy module from the Python's Library.
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

from src.quantum_regime.cryptography.key_exchange.quantum_key_distribution.discrete_variables \
    .prepare_and_measure.bb84.common.QiskryptDVBB84Protocol \
    import QiskryptDVBB84Protocol
"""
Import the Qiskrypt's DV (Discrete Variables) BB84 Protocol.
"""

from src.quantum_regime.cryptography.key_exchange\
    .quantum_key_distribution.discrete_variables.prepare_and_measure.bb84.noiseless\
    .with_no_eavesdropping.QiskryptNoiselessDVBB84ProtocolWithNoEavesdroppingQuantumTransmissionRound\
    import QiskryptNoiselessDVBB84ProtocolWithNoEavesdroppingQuantumTransmissionRound
"""
Import the Qiskrypt's DV (Discrete Variables) BB84 Protocol
with No Eavesdropping Quantum Transmission Round.
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

from src.quantum_regime.circuit.registers.quantum.QiskryptQuantumRegister \
    import QiskryptQuantumRegister
"""
Import the Qiskrypt's Quantum Register.
"""

from src.quantum_regime.circuit.registers.classical.QiskryptClassicalRegister \
    import QiskryptClassicalRegister
"""
Import the Qiskrypt's Classical Register.
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

from src.quantum_regime.networking_and_communications.sessions.QiskryptCommunicationSession \
    import QiskryptCommunicationSession
"""
Import the Qiskrypt's Communication Session.
"""

from src.quantum_regime.true_random.coin_tossing.QiskryptQuantumCoinTossing \
    import QiskryptQuantumCoinTossing
"""
Import the Qiskrypt's Quantum Coin Tossing.
"""

from src.quantum_regime.cryptography.key_exchange.quantum_key_distribution.QiskryptQuantumKeyDistribution \
    import QUANTUM_KEY_DISTRIBUTION_DEFAULT_PARTIES_NAMES
"""
Import the default parties' names for the Qiskrypt's Quantum Key Distribution (QKD).
"""

from src.quantum_regime.cryptography.QiskryptQuantumCryptographicPrimitive \
    import POSSIBLE_QUANTUM_CRYPTOGRAPHIC_PRIMITIVE_SCENARIOS
"""
Import the available Quantum Cryptographic Primitive scenarios for
the Qiskrypt's Quantum Cryptographic Primitives.
"""

from src.quantum_regime.networking_and_communications.channels.QiskryptCommunicationChannel \
    import POSSIBLE_COMMUNICATION_CHANNEL_DIRECTIONS
"""
Import the available Communication Channel directions for the Qiskrypt's Communication Channel.
"""

from src.quantum_regime.cryptography.key_exchange.quantum_key_distribution.QiskryptQuantumKeyDistribution \
    import QUANTUM_KEY_DISTRIBUTION_NUM_PARTIES
"""
Import the number of parties for
the Qiskrypt's Quantum Key Distribution (QKD). 
"""

from src.quantum_regime.cryptography.key_exchange.quantum_key_distribution \
    .discrete_variables.prepare_and_measure.bb84.common.QiskryptDVBB84Protocol \
    import DV_BB84_PROTOCOL_NUM_ROUNDS_FOR_QUANTUM_TRANSMISSION
"""
Import the default number of rounds for the Quantum Transmission of
the Qiskrypt's DV (Discrete Variable) BB84 Protocol.
"""

from src.quantum_regime.cryptography.key_exchange.quantum_key_distribution\
    .discrete_variables.prepare_and_measure.bb84.common.QiskryptDVBB84ProtocolRound \
    import POSSIBLE_DV_BB84_PROTOCOL_ROUND_TYPES
"""
Import the available DV (Discrete Variables) BB84 Protocol Round types for
the Qiskrypt's DV (Discrete Variables) BB84 Protocol.
"""


class QiskryptNoiselessDVBB84ProtocolWithNoEavesdropping \
            (QiskryptDVBB84Protocol):
    """
    Object class for the Qiskrypt's Noiseless DV (Discrete Variables)
    BB84 Protocol with No Eavesdropping.
    """

    def __init__(self, sender_name=QUANTUM_KEY_DISTRIBUTION_DEFAULT_PARTIES_NAMES[0].lower(),
                 receiver_name=QUANTUM_KEY_DISTRIBUTION_DEFAULT_PARTIES_NAMES[1].lower(),
                 sender_address=QiskryptGeographicAddressEnumeration
                 .NOVA_SCHOOL_OF_SCIENCE_AND_TECHNOLOGY_PORTUGAL.value,
                 receiver_address=QiskryptGeographicAddressEnumeration
                 .INSTITUTO_SUPERIOR_TECNICO_PORTUGAL.value,
                 quantum_key_exchange_protocol_num_rounds_for_quantum_transmission=DV_BB84_PROTOCOL_NUM_ROUNDS_FOR_QUANTUM_TRANSMISSION):
        """
        Constructor of the Qiskrypt's Noiseless DV (Discrete Variables)
        BB84 Protocol with No Eavesdropping.

        :param sender_name: the name of the sender in the Qiskrypt's Noiseless DV (Discrete Variables)
                            BB84 Protocol with No Eavesdropping.
        :param receiver_name: the name of the receiver in the Qiskrypt's Noiseless DV (Discrete Variables)
                              BB84 Protocol with No Eavesdropping.
        :param sender_address: the address of the sender in the Qiskrypt's Noiseless DV (Discrete Variables)
                               BB84 Protocol with No Eavesdropping.
        :param receiver_address: the address of the receiver in the Qiskrypt's Noiseless DV (Discrete Variables)
                                 BB84 Protocol with No Eavesdropping.
        :param quantum_key_exchange_protocol_num_rounds_for_quantum_transmission: the number of rounds for
                                                                                  the Quantum Transmission in
                                                                                  the Qiskrypt's Quantum Key
                                                                                  Exchange Protocol.
        """

        self.sender_name = sender_name
        """
        Set the name of the sender in the Qiskrypt's Noiseless DV (Discrete Variables)
        BB84 Protocol with No Eavesdropping.
        """

        self.receiver_name = receiver_name
        """
        Set the name of the receiver in the Qiskrypt's Noiseless DV (Discrete Variables)
        BB84 Protocol with No Eavesdropping.
        """

        self.sender_address = sender_address
        """
        Set the address of the sender in the Qiskrypt's Noiseless DV (Discrete Variables)
        BB84 Protocol with No Eavesdropping.
        """

        self.receiver_address = receiver_address
        """
        Set the address of the receiver in the Qiskrypt's Noiseless DV (Discrete Variables)
        BB84 Protocol with No Eavesdropping.
        """

        self.quantum_transmission_rounds = list()
        """
        Create the list for the rounds for the Quantum Transmission of
        the Qiskrypt's Noiseless DV (Discrete Variables)
        BB84 Protocol with No Eavesdropping, initially, as empty.
        """

        super().__init__(POSSIBLE_QUANTUM_CRYPTOGRAPHIC_PRIMITIVE_SCENARIOS[0],
                         quantum_key_exchange_protocol_num_rounds_for_quantum_transmission)
        """
        Call of the constructor of the super-class Qiskrypt's DV (Discrete Variable) BB84 Protocol.
        """

    def get_name(self) -> str:
        """
        Return the name of the Qiskrypt's Quantum Cryptographic Primitive.

        :return super().get_name(): the name of the Qiskrypt's
                                    Quantum Cryptographic Primitive.
        """

        """
        Return the name of the Qiskrypt's Quantum Cryptographic Primitive.
        """
        return super().get_name()

    def get_quantum_cryptographic_primitive_cardinality(self) -> str:
        """
        Return the cardinality of the Qiskrypt's Quantum Cryptographic Primitive.

        :return super().get_quantum_cryptographic_primitive_cardinality(): the cardinality of the Qiskrypt's
                                                                           Quantum Cryptographic Primitive.
        """

        """
        Return the cardinality of the Qiskrypt's Quantum Cryptographic Primitive.
        """
        return super().get_quantum_cryptographic_primitive_cardinality()

    def get_quantum_cryptographic_primitive_signal_variable_type(self) -> str:
        """
        Return the signal variable type of the Qiskrypt's Quantum Cryptographic Primitive.

        :return super().get_quantum_cryptographic_primitive_signal_variable_type(): the signal variable type of the
                                                                                    Qiskrypt's Quantum Cryptographic
                                                                                    Primitive.
        """

        """
        Return the signal variable type of the Qiskrypt's Quantum Cryptographic Primitive.
        """
        return super().get_quantum_cryptographic_primitive_signal_variable_type()

    def get_quantum_cryptographic_primitive_context(self) -> str:
        """
        Return the context of the Qiskrypt's Quantum Cryptographic Primitive.

        :return super().get_quantum_cryptographic_primitive_context(): the context of the Qiskrypt's
                                                                       Quantum Cryptographic Primitive.
        """

        """
        Return the context of the Qiskrypt's Quantum Cryptographic Primitive.
        """
        return super().get_quantum_cryptographic_primitive_context()

    def get_quantum_cryptographic_primitive_properties(self) -> list:
        """
        Return the list of properties of the Qiskrypt's Quantum Cryptographic Primitive.

        :return super().get_quantum_cryptographic_primitive_properties(): the list of properties of the Qiskrypt's
                                                                          Quantum Cryptographic Primitive.
        """

        """
        Return the list of properties of the Qiskrypt's Quantum Cryptographic Primitive.
        """
        return super().get_quantum_cryptographic_primitive_properties()

    def get_quantum_cryptographic_primitive_scenario(self) -> str:
        """
        Return the scenario of the Qiskrypt's Quantum Cryptographic Primitive.

        :return super().get_quantum_cryptographic_primitive_scenario(): the scenario of the Qiskrypt's
                                                                        Quantum Cryptographic Primitive.
        """

        """
        Return the scenario of the Qiskrypt's Quantum Cryptographic Primitive.
        """
        return super().get_quantum_cryptographic_primitive_scenario()

    def get_quantum_cryptographic_primitive_type(self) -> str:
        """
        Return the type of the Qiskrypt's Quantum Cryptographic Primitive.

        :return super().get_quantum_cryptographic_primitive_type(): the type of the Qiskrypt's
                                                                    Quantum Cryptographic Primitive.
        """

        """
        Return the type of the Qiskrypt's Quantum Cryptographic Primitive.
        """
        return super().get_quantum_cryptographic_primitive_type()

    def get_quantum_key_exchange_protocol_type(self) -> str:
        """
        Return the type of the Qiskrypt's Quantum Key Exchange Protocol.

        :return self.quantum_key_exchange_protocol_type: the type of the Qiskrypt's
                                                         Quantum Key Exchange Protocol.
        """

        """
        Return the type of the Qiskrypt's Quantum Key Exchange Protocol.
        """
        return super().get_quantum_key_exchange_protocol_type()

    def get_quantum_key_exchange_protocol_num_rounds_for_quantum_transmission(self) -> int:
        """
        Return the number of rounds for the Quantum Transmission in
        the Qiskrypt's Quantum Key Exchange Protocol.

        :return super().get_quantum_key_exchange_protocol_num_rounds_for_quantum_transmission():
                the number of rounds for the Quantum Transmission in
                the Qiskrypt's Quantum Key Exchange Protocol.
        """

        """
        Return the number of rounds for the Quantum Transmission in
        the Qiskrypt's Quantum Key Exchange Protocol.
        """
        return super().get_quantum_key_exchange_protocol_num_rounds_for_quantum_transmission()

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

    def get_quantum_key_distribution_type(self) -> str:
        """
        Return the type of the Qiskrypt's Quantum Key Distribution (QKD).

        :return self.quantum_key_distribution_type: the type of the Qiskrypt's
                                                    Quantum Key Distribution (QKD).
        """

        """
        Return the type of the Qiskrypt's Quantum Key Distribution (QKD).
        """
        return self.quantum_key_distribution_type

    def get_sender_name(self) -> str:
        """
        Return the name of the sender in the Qiskrypt's Noiseless DV (Discrete Variables)
        BB84 Protocol with No Eavesdropping.

        :return self.sender_name: the name of the sender in the Qiskrypt's Noiseless DV (Discrete Variables)
                                  BB84 Protocol with No Eavesdropping.
        """

        """
        Return the name of the sender in the Qiskrypt's Noiseless DV (Discrete Variables)
        BB84 Protocol with No Eavesdropping.
        """
        return self.sender_name

    def get_receiver_name(self) -> str:
        """
        Return the name of the receiver in the Qiskrypt's Noiseless DV (Discrete Variables)
        BB84 Protocol with No Eavesdropping.

        :return self.receiver_name: the name of the receiver in the Qiskrypt's Noiseless DV (Discrete Variables)
                                    BB84 Protocol with No Eavesdropping.
        """

        """
        Return the name of the receiver in the Qiskrypt's Noiseless DV (Discrete Variables)
        BB84 Protocol with No Eavesdropping.
        """
        return self.receiver_name

    def get_sender_address(self) -> str:
        """
        Return the address of the sender in the Qiskrypt's Noiseless DV (Discrete Variables)
        BB84 Protocol with No Eavesdropping.

        :return self.sender_address: the address of the sender in the Qiskrypt's Noiseless DV (Discrete Variables)
                                     BB84 Protocol with No Eavesdropping.
        """

        """
        Return the address of the sender in the Qiskrypt's Noiseless DV (Discrete Variables)
        BB84 Protocol with No Eavesdropping.
        """
        return self.sender_address

    def get_receiver_address(self) -> str:
        """
        Return the address of the receiver in the Qiskrypt's Noiseless DV (Discrete Variables)
        BB84 Protocol with No Eavesdropping.

        :return self.receiver_address: the address of the receiver in the Qiskrypt's Noiseless DV (Discrete Variables)
                                       BB84 Protocol with No Eavesdropping.
        """

        """
        Return the address of the receiver in the Qiskrypt's Noiseless DV (Discrete Variables)
        BB84 Protocol with No Eavesdropping.
        """
        return self.receiver_address

    def get_quantum_transmission_rounds(self) -> list:
        """
        Return the list for the Quantum Transmission of
        the Qiskrypt's Noiseless DV (Discrete Variables) BB84 Protocol with No Eavesdropping.

        :return self.quantum_transmission_rounds: the list for the Quantum Transmission of
                                                  the Qiskrypt's Noiseless DV (Discrete Variables)
                                                  BB84 Protocol with No Eavesdropping.
        """

        if self.is_configured():
            """
            If the Qiskrypt's Key Exchange Protocol is already configured.
            """

            """
            Return the list for the Quantum Transmission of
            the Qiskrypt's Noiseless DV (Discrete Variables) BB84 Protocol with No Eavesdropping.
            """
            return self.quantum_transmission_rounds

        else:
            """
            If the Qiskrypt's Key Exchange Protocol is not configured yet.
            """

            # TODO Throw - Exception

    def configure(self) -> None:
        """


        :return:
        """

        if not self.is_configured():
            """
            If the Qiskrypt's Key Exchange Protocol is not configured yet.
            """

            entities_and_distances_in_kms_list =\
                QiskryptNoiselessDVBB84ProtocolWithNoEavesdropping\
                .create_entities_and_distances_in_kms([self.get_sender_name(), self.get_receiver_name()],
                                                      [self.get_sender_address(), self.get_receiver_address()])
            """
            Create the list of two Qiskrypt's Entities and respective distances
            in KMs (Kilometers) between them for the Qiskrypt's Noiseless DV (Discrete Variables)
            BB84 Protocol with No Eavesdropping.
            """

            entities = entities_and_distances_in_kms_list[0]
            """
            Retrieve the list of two Qiskrypt's Entities for
            the Qiskrypt's Noiseless DV (Discrete Variables)
            BB84 Protocol with No Eavesdropping.
            """

            distances_in_kms = entities_and_distances_in_kms_list[1]
            """
            Retrieve the list of respective distances in KMs (Kilometers) between
            the two Qiskrypt's Entities for the Qiskrypt's Noiseless DV (Discrete Variables)
            BB84 Protocol with No Eavesdropping.
            """

            template_quantum_circuit_of_quantum_transmission_for_noiseless_dv_bb84_protocol_with_no_eavesdropping = \
                QiskryptNoiselessDVBB84ProtocolWithNoEavesdropping\
                .create_template_quantum_circuit_of_quantum_transmission_for_noiseless_dv_bb84_protocol_with_no_eavesdropping\
                (entities, distances_in_kms)
            """
            Create the template of the Qiskrypt's Quantum Circuit for each round of
            the Qiskrypt's Communication Session, from the Qiskrypt's Registers retrieved of
            the sender and receiver Qiskrypt's Party Clients, and respective associated
            Qiskrypt's Link connecting them for the Qiskrypt's Noiseless DV (Discrete Variables)
            BB84 Protocol with No Eavesdropping.
            """

            for current_num_round_for_quantum_transmission in \
                    range(self.get_quantum_key_exchange_protocol_num_rounds_for_quantum_transmission()):
                """
                For each round for the Quantum Transmission in
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

                secret_bit = \
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

                random_basis_bit = \
                    quantum_coin_tossing_sender_random_basis.get_coin_tossing_outcome_bit_as_int_base_2()
                """
                Retrieve the classical bit from the Qiskrypt's Coin Tossing,
                for the choice of Random Basis for the sender through
                the execution of the respective Qiskrypt's Quantum Circuit,
                in an integer base-2 format (i.e., an integer representation of a bit).
                """

                current_round_type_for_quantum_transmission = None
                """
                Initialise the type of the current round for Quantum Transmission of
                the Qiskrypt's Qiskrypt's DV (Discrete Variables) BB84 Protocol.
                """

                if random_basis_bit == 0:
                    """
                    If the classical bit from the Qiskrypt's Coin Tossing,
                    for the choice of Random Basis for the sender is zero (0).
                    """

                    current_round_type_for_quantum_transmission = \
                        POSSIBLE_DV_BB84_PROTOCOL_ROUND_TYPES[0]
                    """
                    Set the type of the current round for Quantum Transmission of
                    the Qiskrypt's Qiskrypt's DV (Discrete Variables) BB84 Protocol,
                    as a 'Z-BASIS ROUND'.
                    """

                elif random_basis_bit == 1:
                    """
                    If the classical bit from the Qiskrypt's Coin Tossing,
                    for the choice of Random Basis for the sender is one (1).
                    """

                    current_round_type_for_quantum_transmission = \
                        POSSIBLE_DV_BB84_PROTOCOL_ROUND_TYPES[1]
                    """
                    Set the type of the current round for Quantum Transmission of
                    the Qiskrypt's Qiskrypt's DV (Discrete Variables) BB84 Protocol,
                    as a 'X-BASIS ROUND'.
                    """

                current_round_quantum_circuit = \
                    deep_copy(template_quantum_circuit_of_quantum_transmission_for_noiseless_dv_bb84_protocol_with_no_eavesdropping)
                """
                Create the Qiskrypt's Quantum Circuit from the a deep copy of
                the template of the Qiskrypt's Quantum Circuit for each round of
                the Qiskrypt's Communication Session, from the Qiskrypt's Registers retrieved of
                the sender and receiver Qiskrypt's Party Clients, and respective associated
                Qiskrypt's Link connecting them for the Qiskrypt's Noiseless DV (Discrete Variables)
                BB84 Protocol with No Eavesdropping.
                """

                if secret_bit == 0:
                    """
                    If the classical bit from the Qiskrypt's Coin Tossing,
                    for the choice of Secret Bit for the sender is zero (0).
                    """

                    current_round_quantum_circuit.get_qiskrypt_classical_register(0).buffer_bit(0)
                    """
                    Buffer the Secret Bit in the Qiskrypt's Classical Register of
                    the Qiskrypt's Quantum Circuit for the current round for Quantum Transmission of
                    the Qiskrypt's Qiskrypt's DV (Discrete Variables) BB84 Protocol. 
                    """

                elif secret_bit == 1:
                    """
                    If the classical bit from the Qiskrypt's Coin Tossing,
                    for the choice of Secret Bit for the sender is one (1).
                    """

                    current_round_quantum_circuit.get_qiskrypt_classical_register(0).invert_bit(0)
                    """
                    Invert the Secret Bit in the Qiskrypt's Classical Register of
                    the Qiskrypt's Quantum Circuit for the current round for Quantum Transmission of
                    the Qiskrypt's Qiskrypt's DV (Discrete Variables) BB84 Protocol. 
                    """

                current_round_for_quantum_transmission = \
                    QiskryptNoiselessDVBB84ProtocolWithNoEavesdroppingQuantumTransmissionRound\
                    (current_num_round_for_quantum_transmission,
                     current_round_type_for_quantum_transmission,
                     current_round_quantum_circuit)
                """
                Create the Qiskrypt's Noiseless DV (Discrete Variables) BB84 Protocol
                with No Eavesdropping Quantum Transmission Round for the current round.
                """

                self.quantum_transmission_rounds.append(current_round_for_quantum_transmission)
                """
                Append the Qiskrypt's Noiseless DV (Discrete Variables) BB84 Protocol
                with No Eavesdropping Quantum Transmission Round for the current round to
                the list for the rounds for the Quantum Transmission of
                the Qiskrypt's Noiseless DV (Discrete Variables)
                BB84 Protocol with No Eavesdropping
                """

            """
            Set the Qiskrypt's Key Exchange Protocol as configured.
            """
            self.set_as_configured()

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
        the Qiskrypt's Noiseless DV (Discrete Variables) BB84 Protocol with No Eavesdropping.

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

        if num_names == num_addresses == QUANTUM_KEY_DISTRIBUTION_NUM_PARTIES:
            """
            If the number of names is equal to the number of addresses,
            and are both equal to 2.
            """

            entities = list()
            """
            Create an empty list for the two Qiskrypt's Entities to be added to
            the Qiskrypt's Noiseless DV (Discrete Variables) BB84 Protocol with No Eavesdropping.
            """

            distances_in_kms = list()
            """
            Create an empty list for the distance between the two Qiskrypt's Entities to be added to
            the Qiskrypt's Noiseless DV (Discrete Variables) BB84 Protocol with No Eavesdropping.
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
                    the Qiskrypt's Noiseless DV (Discrete Variables) BB84 Protocol with No Eavesdropping.
                    """

                else:
                    """
                    If some current name and/or location address are not strings.
                    """

                    # TODO Throw - Exception

            location_address_1 = entities[0].get_location_address()
            """
            Retrieve the location address of the 1st Qiskrypt's Entity (sender) for
            the Qiskrypt's Noiseless DV (Discrete Variables) BB84 Protocol with No Eavesdropping.
            """

            location_address_2 = entities[1].get_location_address()
            """
            Retrieve the location address of the 2nd Qiskrypt's Entity (receiver) for
            the Qiskrypt's Noiseless DV (Discrete Variables) BB84 Protocol with No Eavesdropping.
            """

            distance_in_kms = qiskrypt_geocoding \
                .compute_distance_between_locations_from_addresses_in_kms_using_osmr(location_address_1,
                                                                                     location_address_2)
            """
            Compute the distance in KMs (Kilometers) between
            the 1st Qiskrypt's Entity (sender) and 2nd Qiskrypt's Entity (receiver) for
            the Qiskrypt's Noiseless DV (Discrete Variables) BB84 Protocol with No Eavesdropping.
            """

            altitude_in_kms_1 = entities[0].get_altitude_in_kms()
            """
            Retrieve the altitude in KMs (Kilometers) of the 1st Qiskrypt's Entity (sender) for
            the Qiskrypt's Noiseless DV (Discrete Variables) BB84 Protocol with No Eavesdropping.
            """

            altitude_in_kms_2 = entities[1].get_altitude_in_kms()
            """
            Retrieve the altitude in KMs (Kilometers) of the 2nd Qiskrypt's Entity (receiver) for
            the Qiskrypt's Noiseless DV (Discrete Variables) BB84 Protocol with No Eavesdropping.
            """

            altitude_in_kms_difference = abs((altitude_in_kms_1 - altitude_in_kms_2))
            """
            Compute the difference between the altitudes in KMs (Kilometers) between
            the 1st Qiskrypt's Entity (sender) and 2nd Qiskrypt's Entity (receiver) for
            the Qiskrypt's Noiseless DV (Discrete Variables) BB84 Protocol with No Eavesdropping.
            """

            distance_in_kms += altitude_in_kms_difference
            """
            Sum the difference between the altitudes in KMs (Kilometers) between
            the 1st Qiskrypt's Entity (sender) and 2nd Qiskrypt's Entity (receiver) to
            the distance in KMs (Kilometers) between them for
            the Qiskrypt's Noiseless DV (Discrete Variables) BB84 Protocol with No Eavesdropping.
            """

            distances_in_kms.append(distance_in_kms)
            """
            Append the distance in KMs (Kilometers) between
            the 1st Qiskrypt's Entity (sender) and 2nd Qiskrypt's Entity (receiver) to
            the list of distances in KMs (Kilometers) for
            the Qiskrypt's Noiseless DV (Discrete Variables) BB84 Protocol with No Eavesdropping.
            """

            """
            Return the list of two Qiskrypt's Entities
            and respective distance in KMs (Kilometers) between them for
            the Qiskrypt's Noiseless DV (Discrete Variables) BB84 Protocol with No Eavesdropping.
            """
            return [entities, distances_in_kms]

        else:
            """
            If the number of names is not equal to the number of location addresses.
            """

            # TODO Throw - Exception

    @staticmethod
    def create_template_quantum_circuit_of_quantum_transmission_for_noiseless_dv_bb84_protocol_with_no_eavesdropping \
            (entities_list: list, distances_in_kms_list: list):
        """
        Create and return the template of the Qiskrypt's Quantum Circuit for each round of
        the Qiskrypt's Communication Session, from the Qiskrypt's Registers retrieved of
        the sender and receiver Qiskrypt's Party Clients, and respective associated
        Qiskrypt's Link connecting them for the Qiskrypt's Noiseless DV (Discrete Variables)
        BB84 Protocol with No Eavesdropping.

        :param entities_list: the list of Qiskrypt's Entities.
        :param distances_in_kms_list: the list of distances between Qiskrypt's Entities.

        :return template_quantum_circuit_of_quantum_transmission_for_noiseless_dv_bb84_protocol_with_no_eavesdropping:
                the template of the Qiskrypt's Quantum Circuit for each round of
                the Qiskrypt's Communication Session, from the Qiskrypt's Registers retrieved of
                the sender and receiver Qiskrypt's Party Clients, and respective associated
                Qiskrypt's Link connecting them for the Qiskrypt's Noiseless DV (Discrete Variables)
                BB84 Protocol with No Eavesdropping.
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

        if num_entities == QUANTUM_KEY_DISTRIBUTION_NUM_PARTIES:
            """
            If the number of given Qiskrypt's Entities is equal to
            the number of parties for a Quantum Key Distribution (QKD).
            """

            party_clients_list = []
            """
            Create an empty list for the Qiskrypt's Party Clients for the Qiskrypt's BB84 Protocol Round
            with Discrete Variables (DVs) for Noiseless Scenarios and No Eavesdropping.
            """

            for current_num_party in range(QUANTUM_KEY_DISTRIBUTION_NUM_PARTIES):
                """
                For each respective party for the Qiskrypt's BB84 Protocol Round
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
                                                     num_qubits=1, qiskit_quantum_register=None)
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
                    If the current Qiskrypt's Entity is not a Qiskrypt's Entity.
                    """

                    # TODO Throw - Exception

            if num_distances_in_kms == (QUANTUM_KEY_DISTRIBUTION_NUM_PARTIES - 1):
                """
                If the number of given distances in KMs (Kilometers) is equal to
                the number of parties for a Quantum Key Distribution (QKD) minus one.
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

                quantum_register = QiskryptQuantumRegister(name="dv_qu_ch_{}".format(0),
                                                           num_qubits=1, qiskit_quantum_register=None)
                """
                Create a Qiskrypt's Quantum Register for the Qiskrypt's Link.
                """

                quantum_registers_list = [quantum_register]
                """
                Create the list of Qiskrypt's Quantum Registers for the Qiskrypt's Link.
                """

                link = QiskryptLink(QUANTUM_KEY_DISTRIBUTION_NUM_PARTIES)
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
                    QiskryptCommunicationSession("noiseless_dv_bb84_protocol_with_no_eavesdropping_session")
                """
                Create the Qiskrypt's Communication Session for
                the Qiskrypt's Noiseless DV (Discrete Variables) BB84 Protocol with No Eavesdropping.
                """

                sender_party_clients_list = [party_clients_list[0]]
                """
                Create the list for the sender Qiskrypt's Party Clients.
                """

                receiver_party_clients_list = [party_clients_list[1]]
                """
                Create the list for the receiver Qiskrypt's Party Clients.
                """

                communication_session.start(sender_party_clients_list, link, receiver_party_clients_list,
                                            timeout_in_secs=300)
                """
                Start the Qiskrypt's Communication Session for
                the Qiskrypt's Noiseless DV (Discrete Variables) BB84 Protocol with No Eavesdropping.
                """

                template_quantum_circuit_of_quantum_transmission_for_noiseless_dv_bb84_protocol_with_no_eavesdropping = \
                    communication_session.generate_base_quantum_circuit()
                """
                Generate the template of the Qiskrypt's Quantum Circuit for each round of
                the Qiskrypt's Communication Session, from the Qiskrypt's Registers retrieved of
                the sender and receiver Qiskrypt's Party Clients, and respective associated
                Qiskrypt's Link connecting them for the Qiskrypt's Noiseless DV (Discrete Variables)
                BB84 Protocol with No Eavesdropping.
                """

                """
                Return the template of the Qiskrypt's Quantum Circuit for each round of
                the Qiskrypt's Communication Session, from the Qiskrypt's Registers retrieved of
                the sender and receiver Qiskrypt's Party Clients, and respective associated
                Qiskrypt's Link connecting them for the Qiskrypt's Noiseless DV (Discrete Variables)
                BB84 Protocol with No Eavesdropping.
                """
                return template_quantum_circuit_of_quantum_transmission_for_noiseless_dv_bb84_protocol_with_no_eavesdropping

            else:
                """
                If the number of given distances in KMs (Kilometers) is not equal to
                the number of parties for a Quantum Key Distribution (QKD) minus one.
                """

                # TODO Throw - Exception

        else:
            """
            If the number of given Qiskrypt's Entities is not equal to
            the number of parties for a Quantum Key Distribution (QKD).
            """

            # TODO Throw - Exception
