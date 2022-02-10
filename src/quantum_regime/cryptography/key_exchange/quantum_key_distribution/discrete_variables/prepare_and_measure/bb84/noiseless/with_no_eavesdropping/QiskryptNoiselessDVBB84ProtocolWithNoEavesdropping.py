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

from qiskit import Aer, execute
"""
Import Aer Simulator and the Execute function from IBM's Qiskit.
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
    .with_no_eavesdropping.QiskryptNoiselessDVBB84ProtocolWithNoEavesdroppingQuantumTransmissionPhaseRound\
    import QiskryptNoiselessDVBB84ProtocolWithNoEavesdroppingQuantumTransmissionPhaseRound
"""
Import the Qiskrypt's DV (Discrete Variables) BB84 Protocol
with No Eavesdropping Quantum Transmission Phase Round.
"""

from src.quantum_regime.cryptography.common.keys.symmetric.secret.QiskryptSecretKey \
    import QiskryptSecretKey
"""
Import the Qiskrypt's Secret Key.
"""

from src.quantum_regime.cryptography.common.keys.symmetric.secret.types.QiskryptSecretRawKey \
    import QiskryptSecretRawKey
"""
Import the Qiskrypt's Secret Raw Key.
"""

from src.quantum_regime.cryptography.common.keys.symmetric.secret.types.QiskryptSecretSiftedKey \
    import QiskryptSecretSiftedKey
"""
Import the Qiskrypt's Secret Sifted Key.
"""

from src.quantum_regime.cryptography.common.keys.symmetric.secret.types.QiskryptSecretReconciledKey \
    import QiskryptSecretReconciledKey
"""
Import the Qiskrypt's Secret Reconciled Key.
"""

from src.quantum_regime.cryptography.common.keys.symmetric.secret.types.QiskryptSecretSecureKey \
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

from src.quantum_regime.networking_and_communications.clients.QiskryptClient \
    import POSSIBLE_CLIENT_ROLES
"""
Import the available roles for the Qiskrypt's Client.
"""

from src.quantum_regime.networking_and_communications.channels.QiskryptCommunicationChannel \
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

from src.quantum_regime.cryptography.key_exchange.quantum_key_distribution.QiskryptQuantumKeyDistribution \
    import QUANTUM_KEY_DISTRIBUTION_NUM_PARTIES
"""
Import the number of parties for
the Qiskrypt's Quantum Key Distribution (QKD). 
"""

from src.quantum_regime.cryptography.key_exchange.quantum_key_distribution.QiskryptQuantumKeyDistribution \
    import QUANTUM_KEY_DISTRIBUTION_DEFAULT_PARTIES_NAMES
"""
Import the default parties' names for
the Qiskrypt's Quantum Key Distribution (QKD).
"""

from src.quantum_regime.cryptography.key_exchange.quantum_key_distribution \
    .discrete_variables.prepare_and_measure.bb84.common.QiskryptDVBB84Protocol \
    import DV_BB84_PROTOCOL_NUM_ROUNDS_FOR_QUANTUM_TRANSMISSION_PHASE
"""
Import the default number of rounds for the Quantum Transmission Phase of
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
                 num_rounds_for_quantum_transmission_phase=DV_BB84_PROTOCOL_NUM_ROUNDS_FOR_QUANTUM_TRANSMISSION_PHASE):
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
        :param num_rounds_for_quantum_transmission_phase: the number of rounds for
                                                          the Quantum Transmission Phase in
                                                          the Qiskrypt's Quantum Key Exchange Protocol.
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

        self.quantum_transmission_phase_rounds = list()
        """
        Create the list for the rounds for the Quantum Transmission Phase of
        the Qiskrypt's Noiseless DV (Discrete Variables)
        BB84 Protocol with No Eavesdropping, initially, as empty.
        """

        super().__init__(POSSIBLE_QUANTUM_CRYPTOGRAPHIC_PRIMITIVE_SCENARIOS[0],
                         num_rounds_for_quantum_transmission_phase)
        """
        Call of the constructor of the super-class Qiskrypt's DV (Discrete Variable) BB84 Protocol.
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

    def prepare_quantum_states(self):
        """
        Prepare the Quantum States for the
        Qiskrypt's Quantum Key Distribution (QKD).

        NOTES:
        - For the DV (Discrete Variables) BB84 Protocol, the preparation of
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
            the Qiskrypt's Noiseless DV (Discrete Variables) BB84 Protocol with No Eavesdropping.
            """

            for current_num_round_for_quantum_transmission_phase in \
                    range(num_rounds_for_quantum_transmission_phase):
                """
                For each round of the Quantum Transmission Phase of 
                the Qiskrypt's Noiseless DV (Discrete Variables) BB84 Protocol with No Eavesdropping.
                """

                current_round_for_quantum_transmission_phase = \
                    quantum_transmission_phase_rounds[current_num_round_for_quantum_transmission_phase]
                """
                Retrieve the current round of the Quantum Transmission Phase of 
                the Qiskrypt's Noiseless DV (Discrete Variables) BB84 Protocol with No Eavesdropping.
                """

                if isinstance(current_round_for_quantum_transmission_phase,
                              QiskryptNoiselessDVBB84ProtocolWithNoEavesdroppingQuantumTransmissionPhaseRound):
                    """
                    If the current round of the Quantum Transmission Phase of 
                    the Qiskrypt's Noiseless DV (Discrete Variables) BB84 Protocol with No Eavesdropping is
                    really a Qiskrypt's Noiseless DV (Discrete Variables) BB84 Protocol
                    with No Eavesdropping Quantum Transmission Phase Round.
                    """

                    current_round_quantum_circuit_for_quantum_transmission_phase = \
                        current_round_for_quantum_transmission_phase\
                        .get_quantum_key_exchange_protocol_round_quantum_circuit()
                    """
                    Retrieve the Qiskrypt's Quantum Circuit for the current round of the Quantum Transmission Phase of 
                    the Qiskrypt's Noiseless DV (Discrete Variables) BB84 Protocol with No Eavesdropping.
                    """

                    if isinstance(current_round_quantum_circuit_for_quantum_transmission_phase,
                                  QiskryptQuantumCircuit):
                        """
                        If the Qiskrypt's Quantum Circuit for the current round of the Quantum Transmission Phase of 
                        the Qiskrypt's Noiseless DV (Discrete Variables) BB84 Protocol with No Eavesdropping is
                        really a Qiskrypt's Quantum Circuit.
                        """

                        current_secret_bit_sender = \
                            current_round_quantum_circuit_for_quantum_transmission_phase\
                            .get_qiskrypt_classical_register(0).get_bit(0)
                        """
                        Retrieve the Secret Bit from the sender's Qiskrypt's Classical Register from
                        the Qiskrypt's Quantum Circuit for the current round of the Quantum Transmission Phase of 
                        the Qiskrypt's Noiseless DV (Discrete Variables) BB84 Protocol with No Eavesdropping.
                        """

                        current_round_type_for_quantum_transmission_phase = \
                            current_round_for_quantum_transmission_phase\
                            .get_quantum_key_exchange_protocol_round_type()
                        """
                        Retrieve the type of the current round of the Quantum Transmission Phase of 
                        the Qiskrypt's Noiseless DV (Discrete Variables) BB84 Protocol with No Eavesdropping.
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
                            the Qiskrypt's Quantum Circuit for the current round of the Quantum Transmission Phase of 
                            the Qiskrypt's Noiseless DV (Discrete Variables) BB84 Protocol with No Eavesdropping is
                            equal to zero (0), which will correspond to a photon polarization of 0 or 45 degrees
                            (also known as Horizontal or Diagonal polarizations, respectively).
                            """

                            if current_round_type_for_quantum_transmission_phase == \
                                    POSSIBLE_DV_BB84_PROTOCOL_ROUND_TYPES[0]:
                                """
                                If the current round of the Quantum Transmission Phase of 
                                the Qiskrypt's Noiseless DV (Discrete Variables) BB84 Protocol with No Eavesdropping is
                                a 'Z-BASIS ROUND', the sender will prepare the photon with a polarization of 0 degrees
                                (also known as Horizontal polarization) corresponding to the Quantum State |0⟩
                                (or, |H⟩ in the notation of Jones Calculus), equivalent to the classical bit 0.
                                """

                                if not current_round_for_quantum_transmission_phase.is_round_basis_sender_choice_made():
                                    """
                                    If the basis choice made by the sender in the Qiskrypt's DV (Discrete Variables)
                                    BB84 Protocol Round is not set yet.
                                    """

                                    current_round_for_quantum_transmission_phase\
                                        .set_round_basis_sender_choice(
                                            POSSIBLE_DV_BB84_PROTOCOL_ROUND_TYPES[0].split(" ")[0]
                                        )
                                    """
                                    Set the basis choice made by the sender in
                                    the Qiskrypt's DV (Discrete Variables) BB84 Protocol Round as 'Z-BASIS'.
                                    """

                                    current_round_quantum_circuit_for_quantum_transmission_phase.apply_pauli_i(0, 0)
                                    """
                                    Apply the Pauli-I (Idle) Gate/Operation to the qubit in
                                    the Qiskrypt's Quantum Register of the sender's Qiskrypt's Party Client of
                                    the Qiskrypt's Quantum Circuit for the current round of
                                    the Quantum Transmission Phase of the Qiskrypt's Noiseless
                                    DV (Discrete Variables) BB84 Protocol with No Eavesdropping.
                                    """

                                    current_round_quantum_circuit_for_quantum_transmission_phase\
                                        .prepare_and_measure_single_qubit_in_qiskit_quantum_register_in_z_basis(0, 0,
                                                                                                                0, 0, False)
                                    """
                                    Prepare the qubit in the sender's Qiskrypt's Quantum Register of
                                    the Qiskrypt's Quantum Circuit of the current round of
                                    the Quantum Transmission Phase of the Qiskrypt's Noiseless
                                    DV (Discrete Variables) BB84 Protocol with No Eavesdropping in
                                    the Z-Basis (Standard Computational Basis), without measuring it.
                                    """

                                else:
                                    """
                                    If the basis choice made by the sender in the Qiskrypt's DV (Discrete Variables)
                                    BB84 Protocol Round is already set.
                                    """

                                    # TODO Throw - Exception

                            elif current_round_type_for_quantum_transmission_phase == \
                                    POSSIBLE_DV_BB84_PROTOCOL_ROUND_TYPES[1]:
                                """
                                If the current round of the Quantum Transmission Phase of 
                                the Qiskrypt's Noiseless DV (Discrete Variables) BB84 Protocol with No Eavesdropping is
                                a 'X-BASIS ROUND', the sender will prepare the photon with a polarization of 45 degrees
                                (also known as Diagonal polarization) corresponding to the Quantum State
                                |+⟩ = 1 / sqrt(2) x (|0⟩ + |1⟩) (or, |D⟩ = 1 / sqrt(2) x (|H⟩ + |V⟩) in
                                the notation of Jones Calculus), equivalent to a quantum superposition of states
                                representing the classical bits 0 and 1, in phase.
                                """

                                if not current_round_for_quantum_transmission_phase.is_round_basis_sender_choice_made():
                                    """
                                    If the basis choice made by the sender in the Qiskrypt's DV (Discrete Variables)
                                    BB84 Protocol Round is not set yet.
                                    """

                                    current_round_for_quantum_transmission_phase\
                                        .set_round_basis_sender_choice(
                                            POSSIBLE_DV_BB84_PROTOCOL_ROUND_TYPES[1].split(" ")[0]
                                        )
                                    """
                                    Set the basis choice made by the sender in
                                    the Qiskrypt's DV (Discrete Variables) BB84 Protocol Round as 'X-BASIS'.
                                    """

                                    current_round_quantum_circuit_for_quantum_transmission_phase.apply_pauli_i(0, 0)
                                    """
                                    Apply the Pauli-I (Idle) Gate/Operation to the qubit in
                                    the Qiskrypt's Quantum Register of the sender's Qiskrypt's Party Client of
                                    the Qiskrypt's Quantum Circuit for the current round of
                                    the Quantum Transmission Phase of the Qiskrypt's Noiseless
                                    DV (Discrete Variables) BB84 Protocol with No Eavesdropping.
                                    """

                                    current_round_quantum_circuit_for_quantum_transmission_phase\
                                        .prepare_and_measure_single_qubit_in_qiskit_quantum_register_in_x_basis(0, 0,
                                                                                                                0, 0, False)
                                    """
                                    Prepare the qubit in the Qiskrypt's Quantum Register of
                                    the sender's Qiskrypt's Party Client regarding
                                    the Qiskrypt's Quantum Circuit of the current round of
                                    the Quantum Transmission Phase of the Qiskrypt's Noiseless
                                    DV (Discrete Variables) BB84 Protocol with No Eavesdropping in
                                    the X-Basis (Hadamard Basis), without measuring it.
                                    """

                                else:
                                    """
                                    If the basis choice made by the sender in the Qiskrypt's DV (Discrete Variables)
                                    BB84 Protocol Round is already set.
                                    """

                                    # TODO Throw - Exception

                        elif current_secret_bit_sender == 1:
                            """
                            If the Secret Bit from the sender's Qiskrypt's Classical Register from
                            the Qiskrypt's Quantum Circuit for the current round of the Quantum Transmission Phase of 
                            the Qiskrypt's Noiseless DV (Discrete Variables) BB84 Protocol with No Eavesdropping is
                            equal to one (1), which will correspond to a photon polarization of 90 or 135 degrees
                            (also known as Vertical or Anti-Diagonal polarizations, respectively).
                            """

                            if current_round_type_for_quantum_transmission_phase == \
                                    POSSIBLE_DV_BB84_PROTOCOL_ROUND_TYPES[0]:
                                """
                                If the current round of the Quantum Transmission Phase of 
                                the Qiskrypt's Noiseless DV (Discrete Variables) BB84 Protocol with No Eavesdropping is
                                a 'Z-BASIS ROUND', the sender will prepare the photon with a polarization of 90 degrees
                                (also known as Horizontal polarization) corresponding to the Quantum State |1⟩
                                (or, |V⟩ in the notation of Jones Calculus), equivalent to the classical bit 1.
                                """

                                if not current_round_for_quantum_transmission_phase.is_round_basis_sender_choice_made():
                                    """
                                    If the basis choice made by the sender in the Qiskrypt's DV (Discrete Variables)
                                    BB84 Protocol Round is not set yet.
                                    """

                                    current_round_for_quantum_transmission_phase\
                                        .set_round_basis_sender_choice(
                                            POSSIBLE_DV_BB84_PROTOCOL_ROUND_TYPES[0].split(" ")[0]
                                        )
                                    """
                                    Set the basis choice made by the sender in
                                    the Qiskrypt's DV (Discrete Variables) BB84 Protocol Round as 'Z-BASIS'.
                                    """

                                    current_round_quantum_circuit_for_quantum_transmission_phase.apply_pauli_x(0, 0)
                                    """
                                    Apply the Pauli-X (NOT/Bit Flip) Gate/Operation to the qubit in
                                    the Qiskrypt's Quantum Register of the sender's Qiskrypt's Party Client of
                                    the Qiskrypt's Quantum Circuit for the current round of
                                    the Quantum Transmission Phase of the Qiskrypt's Noiseless
                                    DV (Discrete Variables) BB84 Protocol with No Eavesdropping.
                                    """

                                    current_round_quantum_circuit_for_quantum_transmission_phase\
                                        .prepare_and_measure_single_qubit_in_qiskit_quantum_register_in_z_basis(0, 0,
                                                                                                                0, 0, False)
                                    """
                                    Prepare the qubit in the sender's Qiskrypt's Quantum Register of
                                    the Qiskrypt's Quantum Circuit of the current round of
                                    the Quantum Transmission Phase of the Qiskrypt's Noiseless
                                    DV (Discrete Variables) BB84 Protocol with No Eavesdropping in
                                    the Z-Basis (Standard Computational Basis), without measuring it.
                                    """

                                else:
                                    """
                                    If the basis choice made by the sender in the Qiskrypt's DV (Discrete Variables)
                                    BB84 Protocol Round is already set.
                                    """

                                    # TODO Throw - Exception

                            elif current_round_type_for_quantum_transmission_phase == \
                                    POSSIBLE_DV_BB84_PROTOCOL_ROUND_TYPES[1]:
                                """
                                If the current round of the Quantum Transmission Phase of 
                                the Qiskrypt's Noiseless DV (Discrete Variables) BB84 Protocol with No Eavesdropping is
                                a 'X-BASIS ROUND', the sender will prepare the photon with a polarization of 135 degrees
                                (also known as Diagonal polarization) corresponding to the Quantum State
                                |-⟩ = 1 / sqrt(2) x (|0⟩ - |1⟩) (or, |A⟩ = 1 / sqrt(2) x (|H⟩ - |V⟩) in
                                the notation of Jones Calculus), equivalent to a quantum superposition of states
                                representing the classical bits 0 and 1, in anti-phase.
                                """

                                if not current_round_for_quantum_transmission_phase.is_round_basis_sender_choice_made():
                                    """
                                    If the basis choice made by the sender in the Qiskrypt's DV (Discrete Variables)
                                    BB84 Protocol Round is not set yet.
                                    """

                                    current_round_for_quantum_transmission_phase\
                                        .set_round_basis_sender_choice(
                                            POSSIBLE_DV_BB84_PROTOCOL_ROUND_TYPES[1].split(" ")[0]
                                        )
                                    """
                                    Set the basis choice made by the sender in
                                    the Qiskrypt's DV (Discrete Variables) BB84 Protocol Round as 'X-BASIS'.
                                    """

                                    current_round_quantum_circuit_for_quantum_transmission_phase.apply_pauli_x(0, 0)
                                    """
                                    Apply the Pauli-X (NOT/Bit Flip) Gate/Operation to the qubit in
                                    the Qiskrypt's Quantum Register of the sender's Qiskrypt's Party Client of
                                    the Qiskrypt's Quantum Circuit for the current round of
                                    the Quantum Transmission Phase of the Qiskrypt's Noiseless
                                    DV (Discrete Variables) BB84 Protocol with No Eavesdropping.
                                    """

                                    current_round_quantum_circuit_for_quantum_transmission_phase\
                                        .prepare_and_measure_single_qubit_in_qiskit_quantum_register_in_x_basis(0, 0,
                                                                                                                0, 0, False)
                                    """
                                    Prepare the qubit in the sender's Qiskrypt's Quantum Register of
                                    the Qiskrypt's Quantum Circuit of the current round of
                                    the Quantum Transmission Phase of the Qiskrypt's Noiseless
                                    DV (Discrete Variables) BB84 Protocol with No Eavesdropping in
                                    the X-Basis (Hadamard Basis), without measuring it.
                                    """

                                else:
                                    """
                                    If the basis choice made by the sender in the Qiskrypt's DV (Discrete Variables)
                                    BB84 Protocol Round is already set.
                                    """

                                    # TODO Throw - Exception

                    else:
                        """
                        If the Qiskrypt's Quantum Circuit for the current round of the Quantum Transmission Phase of 
                        the Qiskrypt's Noiseless DV (Discrete Variables) BB84 Protocol with No Eavesdropping is
                        not a Qiskrypt's Quantum Circuit.
                        """

                        # TODO Throw - Exception

                else:
                    """
                    If the current round of the Quantum Transmission Phase of 
                    the Qiskrypt's Noiseless DV (Discrete Variables) BB84 Protocol with No Eavesdropping is
                    not a Qiskrypt's Noiseless DV (Discrete Variables) BB84 Protocol
                    with No Eavesdropping Quantum Transmission Phase Round.
                    """

                    # TODO Throw - Exception

            sender_party_client = \
                self.get_communication_session().get_sender_party_clients()[0]
            """
            Retrieve the sender Qiskrypt's Party Client of
            the Qiskrypt's Noiseless DV (Discrete Variables) BB84 Protocol with No Eavesdropping.
            """

            receiver_party_client = \
                self.get_communication_session().get_receiver_party_clients()[0]
            """
            Retrieve the receiver Qiskrypt's Party Client of
            the Qiskrypt's Noiseless DV (Discrete Variables) BB84 Protocol with No Eavesdropping.
            """

            if isinstance(sender_party_client, QiskryptPartyClient) and\
                    isinstance(receiver_party_client, QiskryptPartyClient):
                """
                If the sender and receiver Qiskrypt's Party Clients of
                the Qiskrypt's Noiseless DV (Discrete Variables) BB84 Protocol with No Eavesdropping are
                really Qiskrypt's Party Clients.
                """

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

            else:
                """
                If the sender Qiskrypt's Party Client of
                the Qiskrypt's Noiseless DV (Discrete Variables) BB84 Protocol with No Eavesdropping is
                not a Qiskrypt's Party Client.
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
        Qiskrypt's Quantum Key Distribution (QKD).
        """

        if self.is_configured():
            """
            If the Qiskrypt's Key Exchange Protocol is already configured.
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
            the Qiskrypt's Noiseless DV (Discrete Variables) BB84 Protocol with No Eavesdropping.
            """

            for current_num_round_for_quantum_transmission_phase in \
                    range(num_rounds_for_quantum_transmission_phase):
                """
                For each round of the Quantum Transmission Phase of 
                the Qiskrypt's Noiseless DV (Discrete Variables) BB84 Protocol with No Eavesdropping.
                """

                current_round_for_quantum_transmission_phase = \
                    quantum_transmission_phase_rounds[current_num_round_for_quantum_transmission_phase]
                """
                Retrieve the current round of the Quantum Transmission Phase of 
                the Qiskrypt's Noiseless DV (Discrete Variables) BB84 Protocol with No Eavesdropping.
                """

                if isinstance(current_round_for_quantum_transmission_phase,
                              QiskryptNoiselessDVBB84ProtocolWithNoEavesdroppingQuantumTransmissionPhaseRound):
                    """
                    If the current round of the Quantum Transmission Phase of 
                    the Qiskrypt's Noiseless DV (Discrete Variables) BB84 Protocol with No Eavesdropping is
                    really a Qiskrypt's Noiseless DV (Discrete Variables) BB84 Protocol
                    with No Eavesdropping Quantum Transmission Phase Round.
                    """

                    current_round_quantum_circuit_for_quantum_transmission_phase = \
                        current_round_for_quantum_transmission_phase\
                        .get_quantum_key_exchange_protocol_round_quantum_circuit()
                    """
                    Retrieve the Qiskrypt's Quantum Circuit for the current round of the Quantum Transmission Phase of 
                    the Qiskrypt's Noiseless DV (Discrete Variables) BB84 Protocol with No Eavesdropping.
                    """

                    if isinstance(current_round_quantum_circuit_for_quantum_transmission_phase,
                                  QiskryptQuantumCircuit):
                        """
                        If the Qiskrypt's Quantum Circuit for the current round of the Quantum Transmission Phase of 
                        the Qiskrypt's Noiseless DV (Discrete Variables) BB84 Protocol with No Eavesdropping is
                        really a Qiskrypt's Quantum Circuit.
                        """

                        current_round_quantum_circuit_for_quantum_transmission_phase.apply_swap(0, 1, 0, 0)
                        """
                        Apply the SWAP Gate/Operation between the qubits in
                        the Qiskrypt's Quantum Registers of the sender Qiskrypt's Party Client
                        and Qiskrypt's Link, respectively, of the Qiskrypt's Quantum Circuit for
                        the current round of the Quantum Transmission Phase of the Qiskrypt's Noiseless
                        DV (Discrete Variables) BB84 Protocol with No Eavesdropping.
                        """

                        current_round_quantum_circuit_for_quantum_transmission_phase.apply_swap(1, 2, 0, 0)
                        """
                        Apply the SWAP Gate/Operation between the qubits in
                        the Qiskrypt's Quantum Registers of the Qiskrypt's Link
                        and receiver Qiskrypt's Party Client respectively,
                        of the Qiskrypt's Quantum Circuit for the current round of
                        the Quantum Transmission Phase of the Qiskrypt's Noiseless
                        DV (Discrete Variables) BB84 Protocol with No Eavesdropping.
                        """

                    else:
                        """
                        If the Qiskrypt's Quantum Circuit for the current round of the Quantum Transmission Phase of 
                        the Qiskrypt's Noiseless DV (Discrete Variables) BB84 Protocol with No Eavesdropping is
                        not a Qiskrypt's Quantum Circuit.
                        """

                        # TODO Throw - Exception

                else:
                    """
                    If the current round of the Quantum Transmission Phase of 
                    the Qiskrypt's Noiseless DV (Discrete Variables) BB84 Protocol with No Eavesdropping is
                    not a Qiskrypt's Noiseless DV (Discrete Variables) BB84 Protocol
                    with No Eavesdropping Quantum Transmission Phase Round.
                    """

                    # TODO Throw - Exception

        else:
            """
            If the Qiskrypt's Key Exchange Protocol is not configured.
            """

            # TODO Throw - Exception

    def measure_quantum_states(self):
        """
        Measure the Quantum States for the
        Qiskrypt's Quantum Key Distribution (QKD).
        """

        if self.is_configured():
            """
            If the Qiskrypt's Key Exchange Protocol is already configured.
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
            the Qiskrypt's Noiseless DV (Discrete Variables) BB84 Protocol with No Eavesdropping.
            """

            for current_num_round_for_quantum_transmission_phase in \
                    range(num_rounds_for_quantum_transmission_phase):
                """
                For each round of the Quantum Transmission Phase of 
                the Qiskrypt's Noiseless DV (Discrete Variables) BB84 Protocol with No Eavesdropping.
                """

                current_round_for_quantum_transmission_phase = \
                    quantum_transmission_phase_rounds[current_num_round_for_quantum_transmission_phase]
                """
                Retrieve the current round of the Quantum Transmission Phase of 
                the Qiskrypt's Noiseless DV (Discrete Variables) BB84 Protocol with No Eavesdropping.
                """

                if isinstance(current_round_for_quantum_transmission_phase,
                              QiskryptNoiselessDVBB84ProtocolWithNoEavesdroppingQuantumTransmissionPhaseRound):
                    """
                    If the current round of the Quantum Transmission Phase of 
                    the Qiskrypt's Noiseless DV (Discrete Variables) BB84 Protocol with No Eavesdropping is
                    really a Qiskrypt's Noiseless DV (Discrete Variables) BB84 Protocol
                    with No Eavesdropping Quantum Transmission Phase Round.
                    """

                    current_round_quantum_circuit_for_quantum_transmission_phase = \
                        current_round_for_quantum_transmission_phase\
                        .get_quantum_key_exchange_protocol_round_quantum_circuit()
                    """
                    Retrieve the Qiskrypt's Quantum Circuit for the current round of the Quantum Transmission Phase of 
                    the Qiskrypt's Noiseless DV (Discrete Variables) BB84 Protocol with No Eavesdropping.
                    """

                    if isinstance(current_round_quantum_circuit_for_quantum_transmission_phase,
                                  QiskryptQuantumCircuit):
                        """
                        If the Qiskrypt's Quantum Circuit for the current round of the Quantum Transmission Phase of 
                        the Qiskrypt's Noiseless DV (Discrete Variables) BB84 Protocol with No Eavesdropping is
                        really a Qiskrypt's Quantum Circuit.
                        """

                        quantum_coin_tossing_receiver_random_basis = \
                            QiskryptQuantumCoinTossing("qu_coin_toss_receiver_random_basis")
                        """
                        Create a Qiskrypt's Quantum Coin Tossing for the choice of Random Basis for the receiver.
                        """

                        quantum_coin_tossing_receiver_random_basis.initialise_qiskrypt_quantum_circuit()
                        """
                        Initialise the Qiskrypt's Quantum Circuit for
                        the Qiskrypt's Quantum Coin Tossing for the choice of Random Basis for the receiver.
                        """

                        quantum_coin_tossing_receiver_random_basis.toss_coin()
                        """
                        Toss the Coin related to the Qiskrypt's Quantum Coin Tossing
                        for the choice of Random Basis for the receiver.
                        """

                        receiver_random_basis_bit = \
                            quantum_coin_tossing_receiver_random_basis.get_coin_tossing_outcome_bit_as_int_base_2()
                        """
                        Retrieve the classical bit from the Qiskrypt's Coin Tossing,
                        for the choice of Random Basis for the receiver through
                        the execution of the respective Qiskrypt's Quantum Circuit,
                        in an integer base-2 format (i.e., an integer representation of a bit).
                        """

                        if not current_round_for_quantum_transmission_phase.is_round_basis_receiver_choice_made():
                            """
                            If the basis choice made by the receiver in
                            the Qiskrypt's DV (Discrete Variables) BB84 Protocol Round is not set yet.
                            """

                            if receiver_random_basis_bit == 0:
                                """
                                If the classical bit from the Qiskrypt's Coin Tossing,
                                for the choice of Random Basis for the receiver through
                                the execution of the respective Qiskrypt's Quantum Circuit,
                                in an integer base-2 format (i.e., an integer representation of a bit) is zero (0),
                                the receiver will choose the 'Z-Basis' to measure the qubit in
                                the current round of the Quantum Transmission Phase of 
                                the Qiskrypt's Noiseless DV (Discrete Variables) BB84 Protocol with No Eavesdropping.
                                """

                                current_round_for_quantum_transmission_phase \
                                    .set_round_basis_sender_choice(
                                        POSSIBLE_DV_BB84_PROTOCOL_ROUND_TYPES[0].split(" ")[0]
                                    )
                                """
                                Set the basis choice made by the sender in
                                the Qiskrypt's DV (Discrete Variables) BB84 Protocol Round as 'Z-BASIS'.
                                """

                                current_round_for_quantum_transmission_phase.get_round_quantum_circuit()\
                                    .prepare_and_measure_single_qubit_in_qiskit_quantum_register_in_z_basis\
                                    (2, 1, 0, 0, True)
                                """
                                Prepare the qubit in the receiver's Qiskrypt's Quantum Register of
                                the Qiskrypt's Quantum Circuit of the current round of
                                the Quantum Transmission Phase of the Qiskrypt's Noiseless
                                DV (Discrete Variables) BB84 Protocol with No Eavesdropping in
                                the Z-Basis (Standard Computational Basis), and then measuring it.
                                """

                            elif receiver_random_basis_bit == 1:
                                """
                                If the classical bit from the Qiskrypt's Coin Tossing,
                                for the choice of Random Basis for the receiver through
                                the execution of the respective Qiskrypt's Quantum Circuit,
                                in an integer base-2 format (i.e., an integer representation of a bit) is one (1),
                                the receiver will choose the 'X-Basis' to measure the qubit in
                                the current round of the Quantum Transmission Phase of 
                                the Qiskrypt's Noiseless DV (Discrete Variables) BB84 Protocol with No Eavesdropping.
                                """

                                current_round_for_quantum_transmission_phase \
                                    .set_round_basis_sender_choice(
                                        POSSIBLE_DV_BB84_PROTOCOL_ROUND_TYPES[1].split(" ")[0]
                                    )
                                """
                                Set the basis choice made by the sender in
                                the Qiskrypt's DV (Discrete Variables) BB84 Protocol Round as 'X-BASIS'.
                                """

                                current_round_for_quantum_transmission_phase.get_round_quantum_circuit()\
                                    .prepare_and_measure_single_qubit_in_qiskit_quantum_register_in_x_basis\
                                    (2, 1, 0, 0, True)
                                """
                                Prepare the qubit in the receiver's Qiskrypt's Quantum Register of
                                the Qiskrypt's Quantum Circuit of the current round of
                                the Quantum Transmission Phase of the Qiskrypt's Noiseless
                                DV (Discrete Variables) BB84 Protocol with No Eavesdropping in
                                the X-Basis (Hadamard Basis), and then measuring it.
                                """

                            qiskit_qasm_backend = Aer.get_backend("qasm_simulator")
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
                                bin(int(final_results_frequency_counting.most_frequent(), base=2))
                            """
                            Set the secret bit outcome for the round of the Quantum Transmission Phase of
                            the Qiskrypt's Noiseless DV (Discrete Variables) BB84 Protocol with No Eavesdropping,
                            from the measurement of the qubit in the receiver Qiskrypt's Quantum Register into
                            the bit of the receiver Qiskrypt's Classical Register of the respective
                            Qiskrypt's Quantum Circuit, as the resulted outcome from the measurement of
                            the IBM Qiskit's Quantum Circuit, in an binary format
                            (i.e., the Python's representation for a bit).
                            """

                            current_round_for_quantum_transmission_phase.get_round_quantum_circuit()\
                                .get_qiskrypt_classical_register(1)\
                                .update_bit(0, int(measurement_outcome_secret_bit))
                            """
                            Update the bit in the receiver Qiskrypt's Classical Register of the respective
                            Qiskrypt's Quantum Circuit for the round of the Quantum Transmission Phase of
                            the Qiskrypt's Noiseless DV (Discrete Variables) BB84 Protocol with No Eavesdropping.
                            """

                            receiver_raw_key_secret_bits += str(measurement_outcome_secret_bit)
                            """
                            Append the current secret bit to the binary string for the bits used to
                            build the Qiskrypt's Secret Raw Key of the receiver Qiskrypt's Party Client,
                            according to the randomly chosen measurement for it.
                            """

                        else:
                            """
                            If the basis choice made by the receiver in
                            the Qiskrypt's DV (Discrete Variables) BB84 Protocol Round is already set.
                            """

                            # TODO Throw - Exception

                    else:
                        """
                        If the Qiskrypt's Quantum Circuit for the current round of the Quantum Transmission Phase of 
                        the Qiskrypt's Noiseless DV (Discrete Variables) BB84 Protocol with No Eavesdropping is
                        not a Qiskrypt's Quantum Circuit.
                        """

                        # TODO Throw - Exception

                else:
                    """
                    If the current round of the Quantum Transmission Phase of 
                    the Qiskrypt's Noiseless DV (Discrete Variables) BB84 Protocol with No Eavesdropping is
                    not a Qiskrypt's Noiseless DV (Discrete Variables) BB84 Protocol
                    with No Eavesdropping Quantum Transmission Phase Round.
                    """

                    # TODO Throw - Exception

            receiver_party_client = \
                self.get_communication_session().get_sender_party_clients()[0]
            """
            Retrieve the receiver Qiskrypt's Party Client of
            the Qiskrypt's Noiseless DV (Discrete Variables) BB84 Protocol with No Eavesdropping.
            """

            sender_party_client = \
                self.get_communication_session().get_receiver_party_clients()[0]
            """
            Retrieve the sender Qiskrypt's Party Client of
            the Qiskrypt's Noiseless DV (Discrete Variables) BB84 Protocol with No Eavesdropping.
            """

            if isinstance(receiver_party_client, QiskryptPartyClient) and \
                    isinstance(sender_party_client, QiskryptPartyClient):
                """
                If the receiver and sender Qiskrypt's Party Clients of
                the Qiskrypt's Noiseless DV (Discrete Variables) BB84 Protocol with No Eavesdropping are
                really Qiskrypt's Party Clients.
                """

                receiver_party_client_uuid = sender_party_client.get_uuid()
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

        else:
            """
            If the Qiskrypt's Key Exchange Protocol is not configured.
            """

            # TODO Throw - Exception

    def sift_raw_key(self):
        """
        Sift the Secret Key for the
        Qiskrypt's Quantum Key Distribution (QKD).
        """

        if self.is_configured():
            """
            If the Qiskrypt's Key Exchange Protocol is already configured.
            """

            # TODO - To complete

        else:
            """
            If the Qiskrypt's Key Exchange Protocol is not configured.
            """

            # TODO Throw - Exception

    def estimate_parameters(self):
        """
        Estimate the Parameters for the
        Qiskrypt's Quantum Key Distribution (QKD).
        """

        if self.is_configured():
            """
            If the Qiskrypt's Key Exchange Protocol is already configured.
            """

            # TODO - To complete

        else:
            """
            If the Qiskrypt's Key Exchange Protocol is not configured.
            """

            # TODO Throw - Exception

    def reconcile_information(self):
        """
        Reconcile the Information for the
        Qiskrypt's Quantum Key Distribution (QKD).
        """

        if self.is_configured():
            """
            If the Qiskrypt's Key Exchange Protocol is already configured.
            """

            # TODO - To complete

        else:
            """
            If the Qiskrypt's Key Exchange Protocol is not configured.
            """

            # TODO Throw - Exception

    def amplify_privacy(self):
        """
        Amplify the Privacy for the
        Qiskrypt's Quantum Key Distribution (QKD).
        """

        if self.is_configured():
            """
            If the Qiskrypt's Key Exchange Protocol is already configured.
            """

            # TODO - To complete

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

    def get_quantum_transmission_phase_rounds(self) -> list:
        """
        Return the list for the Quantum Transmission Phase of
        the Qiskrypt's Noiseless DV (Discrete Variables) BB84 Protocol with No Eavesdropping.

        :return self.quantum_transmission_phase_rounds: the list for the Quantum Transmission Phase of
                                                        the Qiskrypt's Noiseless DV (Discrete Variables)
                                                        BB84 Protocol with No Eavesdropping.
        """

        if self.is_configured():
            """
            If the Qiskrypt's Key Exchange Protocol is already configured.
            """

            """
            Return the list for the Quantum Transmission Phase of
            the Qiskrypt's Noiseless DV (Discrete Variables) BB84 Protocol with No Eavesdropping.
            """
            return self.quantum_transmission_phase_rounds

        else:
            """
            If the Qiskrypt's Key Exchange Protocol is not configured yet.
            """

            # TODO Throw - Exception

    def configure(self) -> None:
        """
        Configure the Qiskrypt's Noiseless DV (Discrete Variables)
        BB84 Protocol with No Eavesdropping.
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

            template_quantum_circuit_of_quantum_transmission_phase, communication_session = \
                QiskryptNoiselessDVBB84ProtocolWithNoEavesdropping\
                .create_template_quantum_circuit_and_communication_session_of_quantum_transmission_phase\
                (entities, distances_in_kms)
            """
            Create the template of the Qiskrypt's Quantum Circuit for each round of
            the Qiskrypt's Communication Session, from the Qiskrypt's Registers retrieved of
            the sender and receiver Qiskrypt's Party Clients, and respective associated
            Qiskrypt's Link connecting them for the Qiskrypt's Noiseless DV (Discrete Variables)
            BB84 Protocol with No Eavesdropping.
            """

            self.set_communication_session(communication_session)
            """
            Set the Qiskrypt's Communication Session for
            the Qiskrypt's Noiseless DV (Discrete Variables) BB84 Protocol with No Eavesdropping.
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
                the Qiskrypt's Qiskrypt's DV (Discrete Variables) BB84 Protocol.
                """

                if sender_random_basis_bit == 0:
                    """
                    If the classical bit from the Qiskrypt's Coin Tossing,
                    for the choice of Random Basis for the sender is zero (0).
                    """

                    current_round_type_for_quantum_transmission_phase = \
                        POSSIBLE_DV_BB84_PROTOCOL_ROUND_TYPES[0]
                    """
                    Set the type of the current round of Quantum Transmission Phase of
                    the Qiskrypt's Qiskrypt's DV (Discrete Variables) BB84 Protocol,
                    as a 'Z-BASIS ROUND'.
                    """

                elif sender_random_basis_bit == 1:
                    """
                    If the classical bit from the Qiskrypt's Coin Tossing,
                    for the choice of Random Basis for the sender is one (1).
                    """

                    current_round_type_for_quantum_transmission_phase = \
                        POSSIBLE_DV_BB84_PROTOCOL_ROUND_TYPES[1]
                    """
                    Set the type of the current round of Quantum Transmission Phase of
                    the Qiskrypt's Qiskrypt's DV (Discrete Variables) BB84 Protocol,
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
                BB84 Protocol with No Eavesdropping.
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
                    the Qiskrypt's Qiskrypt's DV (Discrete Variables) BB84 Protocol. 
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
                    the Qiskrypt's Qiskrypt's DV (Discrete Variables) BB84 Protocol. 
                    """

                current_round_for_quantum_transmission_phase = \
                    QiskryptNoiselessDVBB84ProtocolWithNoEavesdroppingQuantumTransmissionPhaseRound\
                    (current_num_round_for_quantum_transmission_phase,
                     current_round_type_for_quantum_transmission_phase,
                     current_round_quantum_circuit)
                """
                Create the Qiskrypt's Noiseless DV (Discrete Variables) BB84 Protocol
                with No Eavesdropping Quantum Transmission Phase Round of the current round.
                """

                self.quantum_transmission_phase_rounds\
                    .append(current_round_for_quantum_transmission_phase)
                """
                Append the Qiskrypt's Noiseless DV (Discrete Variables) BB84 Protocol
                with No Eavesdropping Quantum Transmission Phase Round of the current round to
                the list for the rounds for the Quantum Transmission Phase of
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
    def create_template_quantum_circuit_and_communication_session_of_quantum_transmission_phase\
            (entities_list: list, distances_in_kms_list: list):
        """
        Create and return the template of the Qiskrypt's Quantum Circuit for each round of
        the Qiskrypt's Communication Session, from the Qiskrypt's Registers retrieved of
        the sender and receiver Qiskrypt's Party Clients, and respective associated
        Qiskrypt's Link connecting them for the Qiskrypt's Noiseless DV (Discrete Variables)
        BB84 Protocol with No Eavesdropping.

        :param entities_list: the list of Qiskrypt's Entities.
        :param distances_in_kms_list: the list of distances between Qiskrypt's Entities.

        :return template_quantum_circuit_of_quantum_transmission_phase, communication_session:
                the template of the Qiskrypt's Quantum Circuit for each round of
                the Qiskrypt's Communication Session, from the Qiskrypt's Registers retrieved of
                the sender and receiver Qiskrypt's Party Clients, and respective associated
                Qiskrypt's Link connecting them, as well as the Qiskrypt's Communication Session itself,
                for the Qiskrypt's Noiseless DV (Discrete Variables) BB84 Protocol with No Eavesdropping.
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
                the Qiskrypt's Noiseless DV (Discrete Variables) BB84 Protocol with No Eavesdropping.
                """

                template_quantum_circuit_of_quantum_transmission_phase = \
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
                Qiskrypt's Link connecting them, as well as the Qiskrypt's Communication Session itself,
                for the Qiskrypt's Noiseless DV (Discrete Variables) BB84 Protocol with No Eavesdropping.
                """
                return template_quantum_circuit_of_quantum_transmission_phase, communication_session

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
