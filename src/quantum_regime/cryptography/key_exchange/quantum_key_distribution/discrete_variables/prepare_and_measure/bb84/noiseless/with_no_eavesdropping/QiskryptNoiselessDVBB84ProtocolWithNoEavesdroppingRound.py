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

from src.classical_regime.utils.geographic.QiskryptGeocoding \
    import QiskryptGeocoding
"""
Import Qiskrypt's Geocoding.
"""

from src.quantum_regime.cryptography.key_exchange.quantum_key_distribution.discrete_variables \
    .prepare_and_measure.bb84.common.QiskryptDVBB84ProtocolRound \
    import QiskryptDVBB84ProtocolRound
"""
Import the Qiskrypt's DV (Discrete Variables) BB84 Protocol Round.
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

from src.quantum_regime.networking_and_communications.channels.classical \
    .noiseless.QiskryptNoiselessClassicalCommunicationChannel \
    import QiskryptNoiselessClassicalCommunicationChannel
"""
Import the Qiskrypt's Noiseless Classical Communication Channel.
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

from src.quantum_regime.circuit.QiskryptQuantumCircuit \
    import QiskryptQuantumCircuit
"""
Import the Qiskrypt's Quantum Circuit.
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


class QiskryptNoiselessDVBB84ProtocolWithNoEavesdroppingRound \
            (QiskryptDVBB84ProtocolRound):
    """
    Object class for the Qiskrypt's Noiseless DV (Discrete Variables)
    BB84 Protocol with No Eavesdropping Round.
    """

    def __init__(self, quantum_key_exchange_protocol_round_number,
                 quantum_key_exchange_protocol_round_type,
                 quantum_key_exchange_protocol_round_quantum_circuit):
        """


        :param quantum_key_exchange_protocol_round_number:
        :param quantum_key_exchange_protocol_round_type:
        :param quantum_key_exchange_protocol_round_quantum_circuit:
        """

        super().__init__(quantum_key_exchange_protocol_round_number,
                         quantum_key_exchange_protocol_round_type,
                         quantum_key_exchange_protocol_round_quantum_circuit)
        """
        
        """

    def get_quantum_key_exchange_protocol_round_number(self) -> int:
        """
        Return the number of the Qiskrypt's Quantum Key Distribution (QKD) Round.

        :return super().get_quantum_key_exchange_protocol_round_number(): the number of the Qiskrypt's
                                                                          Quantum Key Distribution Round.
        """

        """
        Return the number of the Qiskrypt's Quantum Key Exchange Protocol Round.
        """
        return super().get_quantum_key_exchange_protocol_round_number()

    def get_quantum_key_exchange_protocol_round_type(self) -> str:
        """
        Return the type of the Qiskrypt's Quantum Key Exchange Protocol Round.

        :return super().get_quantum_key_exchange_protocol_round_type(): the type of the Qiskrypt's
                                                                        Quantum Key Exchange Protocol Round.
        """

        """
        Return the type of the Qiskrypt's Quantum Key Exchange Protocol Round.
        """
        return super().get_quantum_key_exchange_protocol_round_type()

    def get_quantum_key_exchange_protocol_round_quantum_circuit(self) -> QiskryptQuantumCircuit:
        """
        Return the Qiskrypt's Quantum Circuit of the Qiskrypt's Quantum Key Exchange Protocol Round.

        :return super().get_quantum_key_exchange_protocol_round_quantum_circuit(): the Qiskrypt's Quantum Circuit of
                                                                                   the Qiskrypt's Quantum Key Exchange
                                                                                   Protocol Round.
        """

        """
        Return the Qiskrypt's Quantum Circuit of the Qiskrypt's Quantum Key Exchange Protocol Round.
        """
        return super().get_quantum_key_exchange_protocol_round_quantum_circuit()

    @staticmethod
    def create_base_quantum_circuit_of_quantum_transmission_for_noiseless_dv_bb84_protocol_with_no_eavesdropping\
            (entities_list: list, distances_in_kms_list: list):
        """


        :param entities_list:
        :param distances_in_kms_list:

        :return:
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
            with Discrete Variables (DVs) for Noiseless Scenarios and no Eavesdropping.
            """

            for current_num_party in range(QUANTUM_KEY_DISTRIBUTION_NUM_PARTIES):
                """
                For each respective party for the Qiskrypt's BB84 Protocol Round
                with Discrete Variables (DVs) for Noiseless Scenarios and no Eavesdropping.
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
                the Qiskrypt's Noiseless DV (Discrete Variables) BB84 Protocol with no Eavesdropping.
                """

                sender_party_clients_list = [party_clients_list[0]]
                """
                Create the list for the sender Qiskrypt's Party Clients.
                """

                receiver_party_clients_list = [party_clients_list[1]]
                """
                Create the list for the receiver Qiskrypt's Party Clients.
                """

                communication_session.start(sender_party_clients_list, link, receiver_party_clients_list, 300)
                """
                Start the Qiskrypt's Communication Session for
                the Qiskrypt's Noiseless DV (Discrete Variables) BB84 Protocol with no Eavesdropping.
                """

                base_quantum_circuit_of_quantum_transmission_for_noiseless_dv_bb84_protocol_with_no_eavesdropping = \
                    communication_session.generate_base_quantum_circuit()
                """
                Generate the base Qiskrypt's Quantum Circuit for each round of the Qiskrypt's Communication Session,
                from the Qiskrypt's Registers retrieved of the sender and receiver Qiskrypt's Party Clients,
                and respective associated Qiskrypt's Link connecting them for
                the Qiskrypt's Noiseless DV (Discrete Variables) BB84 Protocol with no Eavesdropping.
                """

                """
                Return the base Qiskrypt's Quantum Circuit for each round of the Qiskrypt's Communication Session,
                from the Qiskrypt's Registers retrieved of the sender and receiver Qiskrypt's Party Clients,
                and respective associated Qiskrypt's Link connecting them for
                the Qiskrypt's Noiseless DV (Discrete Variables) BB84 Protocol with no Eavesdropping.
                """
                return base_quantum_circuit_of_quantum_transmission_for_noiseless_dv_bb84_protocol_with_no_eavesdropping

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
