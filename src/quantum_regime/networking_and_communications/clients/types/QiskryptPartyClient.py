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

from uuid import UUID
"""
Import the general UUID (Universally Unique IDentifier).
"""

from src.quantum_regime.networking_and_communications.clients.QiskryptClient \
    import QiskryptClient
"""
Import the Qiskrypt's Client.
"""

from src.quantum_regime.networking_and_communications.essentials.QiskryptParty \
    import QiskryptParty
"""
Import the Qiskrypt's Party.
"""

from src.quantum_regime.networking_and_communications.endpoints \
    import QiskryptEndpoint
"""
Import the Qiskrypt's Endpoint.
"""

from src.quantum_regime.networking_and_communications.endpoints\
    .ground_station.quantum.QiskryptQuantumGroundStationEndpoint \
    import QiskryptQuantumGroundStationEndpoint
"""
Import the Qiskrypt's Quantum Ground Station Endpoint.
"""

from src.quantum_regime.networking_and_communications.endpoints\
    .ground_station.quantum.fully_quantum.QiskryptFullyQuantumGroundStationEndpoint \
    import QiskryptFullyQuantumGroundStationEndpoint
"""
Import the Qiskrypt's Fully-Quantum Ground Station Endpoint.
"""

from src.quantum_regime.networking_and_communications.endpoints\
    .ground_station.quantum.semi_quantum.QiskryptSemiQuantumGroundStationEndpoint \
    import QiskryptSemiQuantumGroundStationEndpoint
"""
Import the Qiskrypt's Semi-Quantum Ground Station Endpoint.
"""

from src.quantum_regime.networking_and_communications.endpoints\
    .ground_station.classical.QiskryptClassicalGroundStationEndpoint \
    import QiskryptClassicalGroundStationEndpoint
"""
Import the Qiskrypt's Classical Ground Station Endpoint.
"""

"""
Import the Qiskrypt's Satellite Station Endpoint.
"""

"""
Import the Qiskrypt's GEO (GEostationary Orbit) Satellite Station Endpoint.
"""

"""
Import the Qiskrypt's GEO (GEostationary Orbit) Quantum Satellite Station Endpoint.
"""

"""
Import the Qiskrypt's GEO (GEostationary Orbit) Fully-Quantum Satellite Station Endpoint.
"""

"""
Import the Qiskrypt's GEO (GEostationary Orbit) Semi-Quantum Satellite Station Endpoint.
"""

"""
Import the Qiskrypt's GEO (GEostationary Orbit) Classical Satellite Station Endpoint.
"""

"""
Import the Qiskrypt's HEO (High-Earth Orbit) Satellite Station Endpoint.
"""

"""
Import the Qiskrypt's HEO (High-Earth Orbit) Quantum Satellite Station Endpoint.
"""

"""
Import the Qiskrypt's HEO (High-Earth Orbit) Fully-Quantum Satellite Station Endpoint.
"""

"""
Import the Qiskrypt's HEO (High-Earth Orbit) Semi-Quantum Satellite Station Endpoint.
"""

"""
Import the Qiskrypt's HEO (High-Earth Orbit) Classical Satellite Station Endpoint.
"""

"""
Import the Qiskrypt's MEO (Medium-Earth Orbit) Satellite Station Endpoint.
"""

"""
Import the Qiskrypt's MEO (Medium-Earth Orbit) Quantum Satellite Station Endpoint.
"""

"""
Import the Qiskrypt's MEO (Medium-Earth Orbit) Fully-Quantum Satellite Station Endpoint.
"""

"""
Import the Qiskrypt's MEO (Medium-Earth Orbit) Semi-Quantum Satellite Station Endpoint.
"""

"""
Import the Qiskrypt's MEO (Medium-Earth Orbit) Classical Satellite Station Endpoint.
"""

"""
Import the Qiskrypt's LEO (Low-Earth Orbit) Satellite Station Endpoint.
"""

"""
Import the Qiskrypt's LEO (Low-Earth Orbit) Quantum Satellite Station Endpoint.
"""

"""
Import the Qiskrypt's LEO (Low-Earth Orbit) Fully-Quantum Satellite Station Endpoint.
"""

"""
Import the Qiskrypt's LEO (Low-Earth Orbit) Semi-Quantum Satellite Station Endpoint.
"""

"""
Import the Qiskrypt's LEO (Low-Earth Orbit) Classical Satellite Station Endpoint.
"""

from src.quantum_regime.networking_and_communications.endpoints.QiskryptEndpoint \
    import POSSIBLE_ENDPOINT_CONTEXTS
"""
Import the available Endpoint contexts for the Qiskrypt's Endpoints.
"""

from src.quantum_regime.circuit.registers.quantum.QiskryptQuantumRegister \
    import QiskryptQuantumRegister
"""
Import the Qiskrypt's Quantum Register.
"""

from src.quantum_regime.circuit.registers.quantum.QiskryptAncillaQuantumRegister \
    import QiskryptAncillaQuantumRegister
"""
Import the Qiskrypt's Ancilla Quantum Register.
"""

from src.quantum_regime.circuit.registers.quantum.fully_quantum.QiskryptFullyQuantumRegister \
    import QiskryptFullyQuantumRegister
"""
Import the Qiskrypt's Fully-Quantum Register.
"""

from src.quantum_regime.circuit.registers.quantum.fully_quantum.QiskryptAncillaFullyQuantumRegister \
    import QiskryptAncillaFullyQuantumRegister
"""
Import the Qiskrypt's Ancilla Fully-Quantum Register.
"""

from src.quantum_regime.circuit.registers.quantum.semi_quantum.QiskryptSemiQuantumRegister \
    import QiskryptSemiQuantumRegister
"""
Import the Qiskrypt's Semi-Quantum Register.
"""

from src.quantum_regime.circuit.registers.quantum.semi_quantum.QiskryptAncillaSemiQuantumRegister \
    import QiskryptAncillaSemiQuantumRegister
"""
Import the Qiskrypt's Ancilla Semi-Quantum Register.
"""

from src.quantum_regime.circuit.registers.classical.QiskryptClassicalRegister \
    import QiskryptClassicalRegister
"""
Import the Qiskrypt's Classical Register.
"""


"""
Definition of Constants and Enumerations.
"""

NUM_BYTES_FOR_UUID = 16
"""
The number of bytes to be used in an UUID (Universally Unique IDentifier)
for the Qiskrypt's Party Client.
"""


class QiskryptPartyClient(QiskryptClient):
    """
    Object class for the Qiskrypt's Party Client.
    """

    def __init__(self, uuid_version=0, uuid_bytes=None, uuid_node=None,
                 uuid_clock_sequence=None, uuid_name=None, uuid_namespace=None):
        """
        Constructor of the Qiskrypt's Party Client.

        :param uuid_version: the version of the UUID (Universally Unique IDentifier)
                             for the Qiskrypt's Party Client.
        :param uuid_bytes: the bytes to build the UUID (Universally Unique IDentifier)
                           for the Qiskrypt's Party Client.
        :param uuid_node: the node to build the UUID (Universally Unique IDentifier)
                          for the Qiskrypt's Party Client.
        :param uuid_clock_sequence: the clock sequence to build the UUID (Universally Unique IDentifier)
                          for the Qiskrypt's Party Client.
        :param uuid_name: the name to build the UUID (Universally Unique IDentifier)
                          for the Qiskrypt's Party Client.
        :param uuid_namespace: the namespace to build the UUID (Universally Unique IDentifier)
                               for the Qiskrypt's Party Client.
        """

        super().__init__(uuid_version, uuid_bytes, uuid_node,
                         uuid_clock_sequence, uuid_name, uuid_namespace)
        """
        Call of the constructor of the super-class Qiskrypt's Client.
        """

        self.party = None
        """
        Set the Qiskrypt's Party for the Qiskrypt's Party Client, initially, as None.
        """

        self.endpoint = None
        """
        Set the Qiskrypt's Endpoint for the Qiskrypt's Party Client, initially, as None.
        """

    def get_uuid(self) -> UUID:
        """
        Return the UUID (Universally Unique IDentifier) of
        the Qiskrypt's Client.

        :return super().get_uuid(): the UUID (Universally Unique IDentifier) of
                                    the Qiskrypt's Client.
        """

        """
        Return the UUID (Universally Unique IDentifier) of
        the Qiskrypt's Client.
        """
        return super().get_uuid()

    def is_connected(self) -> bool:
        """
        Return the boolean flag to keep the information about if
        the Qiskrypt's Client is connected or not.

        :return super().is_connected(): the boolean flag to keep the information about if
                                        the Qiskrypt's Client is connected or not.
        """

        """
        Return the boolean flag to keep the information about if
        the Qiskrypt's Client is connected or not.
        """
        return super().is_connected()

    def set_connected(self, connected: bool):
        """
        Set the boolean flag to keep the information about if
        the Qiskrypt's Client is connected or not, with a new boolean value.

        :param connected: the new boolean flag to keep the information about if
                          the Qiskrypt's Client is connected or not.
        """

        """
        Set the boolean flag to keep the information about if
        the Qiskrypt's Client is connected or not, with a new boolean value.
        """
        super().set_connected(connected)

    def get_registers(self) -> list:
        """
        Return the list of the Qiskrypt's Registers of the Qiskrypt's Client.

        :return super().get_registers(): the list of the Qiskrypt's Registers of the
                                         Qiskrypt's Client.
        """

        """
        Return the list of the Qiskrypt's Registers of the Qiskrypt's Client.
        """
        return super().get_registers()

    def get_num_registers(self) -> int:
        """
        Return the number of Qiskrypt's Registers in
        the list of Qiskrypt's Registers of the Qiskrypt's Client.

        :return super().get_num_registers(): the number of Qiskrypt's Registers in
                                             the list of Qiskrypt's Registers of
                                             the Qiskrypt's Client.
        """

        """
        Return the number of Qiskrypt's Registers in
        the list of Qiskrypt's Registers of the Qiskrypt's Client.
        """
        return super().get_num_registers()

    def get_quantum_registers(self) -> list:
        """
        Return the list of the Qiskrypt's Quantum Registers of the Qiskrypt's Client.

        :return quantum_registers: the list of the Qiskrypt's Quantum Registers of
                                   the Qiskrypt's Client.
        """

        registers = super().get_registers()
        """
        Retrieve the list of the Qiskrypt's Registers of the Qiskrypt's Client.
        """

        num_registers = super().get_num_registers()
        """
        Retrieve number of the Qiskrypt's Registers of the Qiskrypt's Client.
        """

        quantum_registers = list()
        """
        Create the list of the Qiskrypt's Quantum Registers of
        the Qiskrypt's Client, initially, as an empty list.
        """

        for current_register_index in range(num_registers):
            """
            For each Qiskrypt's Register's index of the Qiskrypt's Client.
            """

            current_register = registers[current_register_index]
            """
            Retrieve the current Qiskrypt's Register of the Qiskrypt's Client.
            """

            if isinstance(current_register, QiskryptQuantumRegister):
                """
                If the current Qiskrypt's Register of the Qiskrypt's Client
                is really a Qiskrypt's Quantum Register.
                """

                quantum_registers.append(current_register)
                """
                Append the current Qiskrypt's Register of the Qiskrypt's Client
                to the list of Qiskrypt's Quantum Registers.
                """

        """
        Return the list of the Qiskrypt's Quantum Registers of
        the Qiskrypt's Client.
        """
        return quantum_registers

    def get_num_quantum_registers(self) -> int:
        """
        Return the number of Qiskrypt's Quantum Registers in
        the list of Qiskrypt's Registers of the Qiskrypt's Client.

        :return len(self.get_quantum_registers()): the number of Qiskrypt's Quantum Registers in
                                                   the list of Qiskrypt's Registers of
                                                   the Qiskrypt's Client.
        """

        """
        Return the number of Qiskrypt's Quantum Registers in
        the list of Qiskrypt's Registers of the Qiskrypt's Client.
        """
        return len(self.get_quantum_registers())

    def get_fully_quantum_registers(self) -> list:
        """
        Return the list of the Qiskrypt's Fully-Quantum Registers of the Qiskrypt's Client.

        :return fully_quantum_registers: the list of the Qiskrypt's Fully-Quantum Registers of
                                         the Qiskrypt's Client.
        """

        registers = super().get_registers()
        """
        Retrieve the list of the Qiskrypt's Registers of the Qiskrypt's Client.
        """

        num_registers = super().get_num_registers()
        """
        Retrieve number of the Qiskrypt's Registers of the Qiskrypt's Client.
        """

        fully_quantum_registers = list()
        """
        Create the list of the Qiskrypt's Fully-Quantum Registers of
        the Qiskrypt's Client, initially, as an empty list.
        """

        for current_register_index in range(num_registers):
            """
            For each Qiskrypt's Register's index of the Qiskrypt's Client.
            """

            current_register = registers[current_register_index]
            """
            Retrieve the current Qiskrypt's Register of the Qiskrypt's Client.
            """

            if isinstance(current_register, QiskryptFullyQuantumRegister):
                """
                If the current Qiskrypt's Register of the Qiskrypt's Client
                is really a Qiskrypt's Fully-Quantum Register.
                """

                fully_quantum_registers.append(current_register)
                """
                Append the current Qiskrypt's Register of the Qiskrypt's Client
                to the list of Qiskrypt's Fully-Quantum Registers.
                """

        """
        Return the list of the Qiskrypt's Fully-Quantum Registers of
        the Qiskrypt's Client.
        """
        return fully_quantum_registers

    def get_num_fully_quantum_registers(self) -> int:
        """
        Return the number of Qiskrypt's Fully-Quantum Registers in
        the list of Qiskrypt's Registers of the Qiskrypt's Client.

        :return len(self.get_fully_quantum_registers()): the number of Qiskrypt's Fully-Quantum Registers in
                                                         the list of Qiskrypt's Registers of
                                                         the Qiskrypt's Client.
        """

        """
        Return the number of Qiskrypt's Fully-Quantum Registers in
        the list of Qiskrypt's Registers of the Qiskrypt's Client.
        """
        return len(self.get_fully_quantum_registers())

    def get_semi_quantum_registers(self) -> list:
        """
        Return the list of the Qiskrypt's Semi-Quantum Registers of the Qiskrypt's Client.

        :return semi_quantum_registers: the list of the Qiskrypt's Semi-Quantum Registers of
                                        the Qiskrypt's Client.
        """

        registers = super().get_registers()
        """
        Retrieve the list of the Qiskrypt's Registers of the Qiskrypt's Client.
        """

        num_registers = super().get_num_registers()
        """
        Retrieve number of the Qiskrypt's Registers of the Qiskrypt's Client.
        """

        semi_quantum_registers = list()
        """
        Create the list of the Qiskrypt's Semi-Quantum Registers of
        the Qiskrypt's Client, initially, as an empty list.
        """

        for current_register_index in range(num_registers):
            """
            For each Qiskrypt's Register's index of the Qiskrypt's Client.
            """

            current_register = registers[current_register_index]
            """
            Retrieve the current Qiskrypt's Register of the Qiskrypt's Client.
            """

            if isinstance(current_register, QiskryptSemiQuantumRegister):
                """
                If the current Qiskrypt's Register of the Qiskrypt's Client
                is really a Qiskrypt's Semi-Quantum Register.
                """

                semi_quantum_registers.append(current_register)
                """
                Append the current Qiskrypt's Register of the Qiskrypt's Client
                to the list of Qiskrypt's Semi-Quantum Registers.
                """

        """
        Return the list of the Qiskrypt's Semi-Quantum Registers of
        the Qiskrypt's Client.
        """
        return semi_quantum_registers

    def get_num_semi_quantum_registers(self) -> int:
        """
        Return the number of Qiskrypt's Semi-Quantum Registers in
        the list of Qiskrypt's Registers of the Qiskrypt's Client.

        :return len(self.get_semi_quantum_registers()): the number of Qiskrypt's Semi-Quantum Registers in
                                                        the list of Qiskrypt's Registers of
                                                        the Qiskrypt's Client.
        """

        """
        Return the number of Qiskrypt's Semi-Quantum Registers in
        the list of Qiskrypt's Registers of the Qiskrypt's Client.
        """
        return len(self.get_semi_quantum_registers())

    def get_classical_registers(self) -> list:
        """
        Return the list of the Qiskrypt's Classical Registers of the Qiskrypt's Client.

        :return classical_registers: the list of the Qiskrypt's Classical Registers of
                                     the Qiskrypt's Client.
        """

        registers = super().get_registers()
        """
        Retrieve the list of the Qiskrypt's Registers of the Qiskrypt's Client.
        """

        num_registers = super().get_num_registers()
        """
        Retrieve number of the Qiskrypt's Registers of the Qiskrypt's Client.
        """

        classical_registers = list()
        """
        Create the list of the Qiskrypt's Classical Registers of
        the Qiskrypt's Client, initially, as an empty list.
        """

        for current_register_index in range(num_registers):
            """
            For each Qiskrypt's Register's index of the Qiskrypt's Client.
            """

            current_register = registers[current_register_index]
            """
            Retrieve the current Qiskrypt's Register of the Qiskrypt's Client.
            """

            if isinstance(current_register, QiskryptClassicalRegister):
                """
                If the current Qiskrypt's Register of the Qiskrypt's Client
                is really a Qiskrypt's Classical Register.
                """

                classical_registers.append(current_register)
                """
                Append the current Qiskrypt's Register of the Qiskrypt's Client
                to the list of Qiskrypt's Classical Registers.
                """

        """
        Return the list of the Qiskrypt's Classical Registers of
        the Qiskrypt's Client.
        """
        return classical_registers

    def get_num_classical_registers(self) -> int:
        """
        Return the number of Qiskrypt's Classical Registers in
        the list of Qiskrypt's Registers of the Qiskrypt's Client.

        :return len(self.get_classical_registers()): the number of Qiskrypt's Classical Registers in
                                                     the list of Qiskrypt's Registers of
                                                     the Qiskrypt's Client.
        """

        """
        Return the number of Qiskrypt's Classical Registers in
        the list of Qiskrypt's Registers of the Qiskrypt's Client.
        """
        return len(self.get_classical_registers())

    def get_party(self) -> QiskryptParty:
        """
        Return the Qiskrypt's Party of the Qiskrypt's Party Client.

        :return self.party: the Qiskrypt's Party of the Qiskrypt's Party Client.
        """

        if super().is_connected():
            """
            If the Qiskrypt's Client is already connected.
            """

            """
            Return the Qiskrypt's Party of the Qiskrypt's Party Client.
            """
            return self.party

        else:
            """
            If the Qiskrypt's Party Client is not connected yet.
            """

            # TODO Throw - Exception

    def get_endpoint(self) -> QiskryptEndpoint:
        """
        Return the Qiskrypt's Endpoint of the Qiskrypt's Party Client.

        :return self.endpoint: the Qiskrypt's Endpoint of the Qiskrypt's Party Client.
        """

        if super().is_connected():
            """
            If the Qiskrypt's Client is already connected.
            """

            """
            Return the Qiskrypt's Endpoint of the Qiskrypt's Party Client.
            """
            return self.endpoint

        else:
            """
            If the Qiskrypt's Party Client is not connected yet.
            """

            # TODO Throw - Exception

    def connect(self, party: QiskryptParty, endpoint: QiskryptEndpoint):
        """
        Connect a Qiskrypt's Party and a Qiskrypt's Endpoint, to the Qiskrypt's Party Client.

        :param party: the Qiskrypt's Party to be connected to the Qiskrypt's Party Client.
        :param endpoint: the Qiskrypt's Endpoint to be connected to the Qiskrypt's Party Client.
        """

        if not super().is_connected():
            """
            If the Qiskrypt's Party Client is not connected yet
            to a Qiskrypt's Party and to a Qiskrypt's Endpoint.
            """

            self.party = party
            """
            Set the Qiskrypt's Party for the Qiskrypt's Party Client.
            """

            self.endpoint = endpoint
            """
            Set the Qiskrypt's Endpoint for the Qiskrypt's Party Client.
            """

            """
            Set the boolean flag to keep the information about if
            the Qiskrypt's Client is connected or not, as True.
            """
            super().set_connected(True)

        else:
            """
            If the Qiskrypt's Party Client is already connected
            to a Qiskrypt's Party and to a Qiskrypt's Endpoint.
            """

            # TODO Throw - Exception

    def add_quantum_register(self, quantum_register: QiskryptQuantumRegister):
        """
        Adds a given Qiskrypt's Quantum Register to
        the list of Qiskrypt's Registers of the Qiskrypt's Party Client.

        :param quantum_register: the Qiskrypt's Quantum Register to be added
                                 to the list of Qiskrypt's Registers of
                                 the Qiskrypt's Party Client.
        """

        if (self.get_endpoint().get_context() == POSSIBLE_ENDPOINT_CONTEXTS[0]) and \
                (isinstance(self.get_endpoint(), QiskryptQuantumGroundStationEndpoint)):
            """
            If the Qiskrypt's Endpoint of the Qiskrypt's Party Client 
            is a Qiskrypt's Quantum Ground Station Endpoint
            and belongs to a Quantum Context.
            """

            super().registers.append(quantum_register)
            """
            Adds the given Qiskrypt's Quantum Register to
            the list of Qiskrypt's Registers of the Qiskrypt's Party Client.
            """

        else:
            """
            If the Qiskrypt's Endpoint of the Qiskrypt's Party Client 
            is not a Qiskrypt's Quantum Ground Station Endpoint 
            and does not belong to a Quantum Context.
            """

            # TODO Throw - Exception

    def remove_quantum_register_by_name(self, quantum_register_name: str):
        """
        Removes a Qiskrypt's Quantum Register from
        the list of Qiskrypt's Registers of the Qiskrypt's Party Client,
        given its name.

        :param quantum_register_name: the name of a Qiskrypt's Quantum Register to be removed
                                      from the list of Qiskrypt's Registers of
                                      the Qiskrypt's Party Client.
        """

        if (self.get_endpoint().get_context() == POSSIBLE_ENDPOINT_CONTEXTS[0]) and \
           (isinstance(self.get_endpoint(), QiskryptQuantumGroundStationEndpoint)):
            """
            If the Qiskrypt's Endpoint of the Qiskrypt's Party Client 
            is a Qiskrypt's Quantum Ground Station Endpoint
            and belongs to a Quantum Context.
            """

            for current_register_index in range(len(super().registers)):
                """
                For each Qiskrypt's Register in the list of
                Qiskrypt's Registers of the Qiskrypt's Party Client. 
                """

                current_register = super().registers[current_register_index]
                """
                Retrieve the current Qiskrypt's Register in
                the list of Qiskrypt's Registers of the Qiskrypt's Party Client.
                """

                if current_register.get_name() == quantum_register_name:
                    """
                    If it was found a Qiskrypt's Register in
                    the list of Qiskrypt's Registers of the Qiskrypt's Party Client,
                    with the given name.
                    """

                    if isinstance(current_register, QiskryptQuantumRegister):
                        """
                        If the current Qiskrypt's Register in
                        the list of Qiskrypt's Registers of the Qiskrypt's Party Client
                        is a Qiskrypt's Quantum Register.
                        """

                        super().registers.remove(current_register)
                        """
                        Removes the current Qiskrypt's Register in
                        the list of Qiskrypt's Registers of the Qiskrypt's Party Client.
                        """

                    else:
                        """
                        If the current Qiskrypt's Register in
                        the list of Qiskrypt's Registers of the Qiskrypt's Party Client
                        is not a Qiskrypt's Quantum Register.
                        """

                        # TODO Throw - Exception

        else:
            """
            If the Qiskrypt's Endpoint of the Qiskrypt's Party Client 
            is not a Qiskrypt's Quantum Ground Station Endpoint 
            and does not belong to a Quantum Context.
            """

            # TODO Throw - Exception

    def remove_quantum_register_by_index(self, quantum_register_index: int):
        """
        Removes a Qiskrypt's Quantum Register from
        the list of Qiskrypt's Registers of the Qiskrypt's Party Client,
        given its index.

        :param quantum_register_index: the index of a Qiskrypt's Quantum Register to be removed
                                       from the list of Qiskrypt's Registers of
                                       the Qiskrypt's Party Client.
        """

        if (self.get_endpoint().get_context() == POSSIBLE_ENDPOINT_CONTEXTS[0]) and \
           (isinstance(self.get_endpoint(), QiskryptQuantumGroundStationEndpoint)):
            """
            If the Qiskrypt's Endpoint of the Qiskrypt's Party Client 
            is a Qiskrypt's Quantum Ground Station Endpoint
            and belongs to a Quantum Context.
            """

            if quantum_register_index < self.get_num_registers():
                """
                If the given index of a Qiskrypt's Quantum Register to be removed
                from the list of Qiskrypt's Registers of the Qiskrypt's Party Client is valid.
                """

                current_register = super().registers[quantum_register_index]
                """
                Retrieve the respective Qiskrypt's Register in
                the list of Qiskrypt's Registers of the Qiskrypt's Party Client.
                """

                if isinstance(current_register, QiskryptQuantumRegister):
                    """
                    If the current Qiskrypt's Register in
                    the list of Qiskrypt's Registers of the Qiskrypt's Party Client
                    is a Qiskrypt's Quantum Register.
                    """

                    super().registers.remove(current_register)
                    """
                    Removes the current Qiskrypt's Register in
                    the list of Qiskrypt's Registers of the Qiskrypt's Party Client.
                    """

                else:
                    """
                    If the current Qiskrypt's Register in
                    the list of Qiskrypt's Registers of the Qiskrypt's Party Client
                    is not a Qiskrypt's Quantum Register.
                    """

                    # TODO Throw - Exception

            else:
                """
                If the given index of a Qiskrypt's Quantum Register to be removed
                from the list of Qiskrypt's Registers of the Qiskrypt's Party Client is not valid.
                """

                # TODO Throw - Exception

        else:
            """
            If the Qiskrypt's Endpoint of the Qiskrypt's Party Client 
            is not a Qiskrypt's Quantum Ground Station Endpoint 
            and does not belong to a Quantum Context.
            """

            # TODO Throw - Exception

    def add_ancilla_quantum_register(self, ancilla_quantum_register: QiskryptAncillaQuantumRegister):
        """
        Adds a given Qiskrypt's Ancilla Quantum Register to
        the list of Qiskrypt's Registers of the Qiskrypt's Party Client.

        :param ancilla_quantum_register: the Qiskrypt's Ancilla Quantum Register to be added
                                         to the list of Qiskrypt's Registers of
                                         the Qiskrypt's Party Client.
        """

        if (self.get_endpoint().get_context() == POSSIBLE_ENDPOINT_CONTEXTS[0]) and \
           (isinstance(self.get_endpoint(), QiskryptQuantumGroundStationEndpoint)):
            """
            If the Qiskrypt's Endpoint of the Qiskrypt's Party Client 
            is a Qiskrypt's Quantum Ground Station Endpoint
            and belongs to a Quantum Context.
            """

            super().registers.append(ancilla_quantum_register)
            """
            Adds the given Qiskrypt's Ancilla Quantum Register to
            the list of Qiskrypt's Registers of the Qiskrypt's Party Client.
            """

        else:
            """
            If the Qiskrypt's Endpoint of the Qiskrypt's Party Client 
            is not a Qiskrypt's Quantum Ground Station Endpoint 
            and does not belong to a Quantum Context.
            """

            # TODO Throw - Exception

    def remove_ancilla_quantum_register_by_name(self, ancilla_quantum_register_name: str):
        """
        Removes a Qiskrypt's Ancilla Quantum Register from
        the list of Qiskrypt's Registers of the Qiskrypt's Party Client,
        given its name.

        :param ancilla_quantum_register_name: the name of a Qiskrypt's Ancilla Quantum Register to be removed
                                              from the list of Qiskrypt's Registers of
                                              the Qiskrypt's Party Client.
        """

        if (self.get_endpoint().get_context() == POSSIBLE_ENDPOINT_CONTEXTS[0]) and \
           (isinstance(self.get_endpoint(), QiskryptQuantumGroundStationEndpoint)):
            """
            If the Qiskrypt's Endpoint of the Qiskrypt's Party Client 
            is a Qiskrypt's Quantum Ground Station Endpoint
            and belongs to a Quantum Context.
            """

            for current_register_index in range(len(super().registers)):
                """
                For each Qiskrypt's Register in the list of
                Qiskrypt's Registers of the Qiskrypt's Party Client. 
                """

                current_register = super().registers[current_register_index]
                """
                Retrieve the current Qiskrypt's Register in
                the list of Qiskrypt's Registers of the Qiskrypt's Party Client.
                """

                if current_register.get_name() == ancilla_quantum_register_name:
                    """
                    If it was found a Qiskrypt's Register in
                    the list of Qiskrypt's Registers of the Qiskrypt's Party Client,
                    with the given name.
                    """

                    if isinstance(current_register, QiskryptAncillaQuantumRegister):
                        """
                        If the current Qiskrypt's Register in
                        the list of Qiskrypt's Registers of the Qiskrypt's Party Client
                        is a Qiskrypt's Ancilla Quantum Register.
                        """

                        super().registers.remove(current_register)
                        """
                        Removes the current Qiskrypt's Register in
                        the list of Qiskrypt's Registers of the Qiskrypt's Party Client.
                        """

                    else:
                        """
                        If the current Qiskrypt's Register in
                        the list of Qiskrypt's Registers of the Qiskrypt's Party Client
                        is not a Qiskrypt's Ancilla Quantum Register.
                        """

                        # TODO Throw - Exception

        else:
            """
            If the Qiskrypt's Endpoint of the Qiskrypt's Party Client 
            is not a Qiskrypt's Quantum Ground Station Endpoint 
            and does not belong to a Quantum Context.
            """

            # TODO Throw - Exception

    def remove_ancilla_quantum_register_by_index(self, ancilla_quantum_register_index: int):
        """
        Removes a Qiskrypt's Ancilla Quantum Register from
        the list of Qiskrypt's Registers of the Qiskrypt's Party Client,
        given its index.

        :param ancilla_quantum_register_index: the index of a Qiskrypt's Ancilla Quantum Register to be removed
                                               from the list of Qiskrypt's Registers of
                                               the Qiskrypt's Party Client.
        """

        if (self.get_endpoint().get_context() == POSSIBLE_ENDPOINT_CONTEXTS[0]) and \
           (isinstance(self.get_endpoint(), QiskryptQuantumGroundStationEndpoint)):
            """
            If the Qiskrypt's Endpoint of the Qiskrypt's Party Client 
            is a Qiskrypt's Quantum Ground Station Endpoint
            and belongs to a Quantum Context.
            """

            if ancilla_quantum_register_index < self.get_num_registers():
                """
                If the given index of a Qiskrypt's Ancilla Quantum Register to be removed
                from the list of Qiskrypt's Registers of the Qiskrypt's Party Client is valid.
                """

                current_register = super().registers[ancilla_quantum_register_index]
                """
                Retrieve the respective Qiskrypt's Register in
                the list of Qiskrypt's Registers of the Qiskrypt's Party Client.
                """

                if isinstance(current_register, QiskryptAncillaQuantumRegister):
                    """
                    If the current Qiskrypt's Register in
                    the list of Qiskrypt's Registers of the Qiskrypt's Party Client
                    is a Qiskrypt's Ancilla Quantum Register.
                    """

                    super().registers.remove(current_register)
                    """
                    Removes the current Qiskrypt's Register in
                    the list of Qiskrypt's Registers of the Qiskrypt's Party Client.
                    """

                else:
                    """
                    If the current Qiskrypt's Register in
                    the list of Qiskrypt's Registers of the Qiskrypt's Party Client
                    is not a Qiskrypt's Ancilla Quantum Register.
                    """

                    # TODO Throw - Exception

            else:
                """
                If the given index of a Qiskrypt's Ancilla Quantum Register to be removed
                from the list of Qiskrypt's Registers of the Qiskrypt's Party Client is not valid.
                """

                # TODO Throw - Exception

        else:
            """
            If the Qiskrypt's Endpoint of the Qiskrypt's Party Client 
            is not a Qiskrypt's Quantum Ground Station Endpoint 
            and does not belong to a Quantum Context.
            """

            # TODO Throw - Exception

    def add_fully_quantum_register(self, fully_quantum_register: QiskryptFullyQuantumRegister):
        """
        Adds a given Qiskrypt's Fully-Quantum Register to
        the list of Qiskrypt's Registers of the Qiskrypt's Party Client.

        :param fully_quantum_register: the Qiskrypt's Fully-Quantum Register to be added
                                       to the list of Qiskrypt's Registers of
                                       the Qiskrypt's Party Client.
        """

        if (self.get_endpoint().get_context() == POSSIBLE_ENDPOINT_CONTEXTS[1]) and \
           (isinstance(self.get_endpoint(), QiskryptFullyQuantumGroundStationEndpoint)):
            """
            If the Qiskrypt's Endpoint of the Qiskrypt's Party Client 
            is a Qiskrypt's Fully-Quantum Ground Station Endpoint
            and belongs to a Fully-Quantum Context.
            """

            super().registers.append(fully_quantum_register)
            """
            Adds the given Qiskrypt's Fully-Quantum Register to
            the list of Qiskrypt's Registers of the Qiskrypt's Party Client.
            """

        else:
            """
            If the Qiskrypt's Endpoint of the Qiskrypt's Party Client 
            is not a Qiskrypt's Fully-Quantum Ground Station Endpoint 
            and does not belong to a Fully-Quantum Context.
            """

            # TODO Throw - Exception

    def remove_fully_quantum_register_by_name(self, fully_quantum_register_name: str):
        """
        Removes a Qiskrypt's Fully-Quantum Register from
        the list of Qiskrypt's Registers of the Qiskrypt's Party Client,
        given its name.

        :param fully_quantum_register_name: the name of a Qiskrypt's Fully-Quantum Register to be removed
                                            from the list of Qiskrypt's Registers of
                                            the Qiskrypt's Party Client.
        """

        if (self.get_endpoint().get_context() == POSSIBLE_ENDPOINT_CONTEXTS[1]) and \
           (isinstance(self.get_endpoint(), QiskryptFullyQuantumGroundStationEndpoint)):
            """
            If the Qiskrypt's Endpoint of the Qiskrypt's Party Client 
            is a Qiskrypt's Fully-Quantum Ground Station Endpoint
            and belongs to a Fully-Quantum Context.
            """

            for current_register_index in range(len(super().registers)):
                """
                For each Qiskrypt's Register in the list of
                Qiskrypt's Registers of the Qiskrypt's Party Client. 
                """

                current_register = super().registers[current_register_index]
                """
                Retrieve the current Qiskrypt's Register in
                the list of Qiskrypt's Registers of the Qiskrypt's Party Client.
                """

                if current_register.get_name() == fully_quantum_register_name:
                    """
                    If it was found a Qiskrypt's Register in
                    the list of Qiskrypt's Registers of the Qiskrypt's Party Client,
                    with the given name.
                    """

                    if isinstance(current_register, QiskryptFullyQuantumRegister):
                        """
                        If the current Qiskrypt's Register in
                        the list of Qiskrypt's Registers of the Qiskrypt's Party Client
                        is a Qiskrypt's Fully-Quantum Register.
                        """

                        super().registers.remove(current_register)
                        """
                        Removes the current Qiskrypt's Register in
                        the list of Qiskrypt's Registers of the Qiskrypt's Party Client.
                        """

                    else:
                        """
                        If the current Qiskrypt's Register in
                        the list of Qiskrypt's Registers of the Qiskrypt's Party Client
                        is not a Qiskrypt's Fully-Quantum Register.
                        """

                        # TODO Throw - Exception

        else:
            """
            If the Qiskrypt's Endpoint of the Qiskrypt's Party Client 
            is not a Qiskrypt's Fully-Quantum Ground Station Endpoint 
            and does not belong to a Fully-Quantum Context.
            """

            # TODO Throw - Exception

    def remove_fully_quantum_register_by_index(self, fully_quantum_register_index: int):
        """
        Removes a Qiskrypt's Fully-Quantum Register from
        the list of Qiskrypt's Registers of the Qiskrypt's Party Client,
        given its index.

        :param fully_quantum_register_index: the index of a Qiskrypt's Fully-Quantum Register to be removed
                                             from the list of Qiskrypt's Registers of
                                             the Qiskrypt's Party Client.
        """

        if (self.get_endpoint().get_context() == POSSIBLE_ENDPOINT_CONTEXTS[1]) and \
           (isinstance(self.get_endpoint(), QiskryptFullyQuantumGroundStationEndpoint)):
            """
            If the Qiskrypt's Endpoint of the Qiskrypt's Party Client 
            is a Qiskrypt's Fully-Quantum Ground Station Endpoint
            and belongs to a Fully-Quantum Context.
            """

            if fully_quantum_register_index < self.get_num_registers():
                """
                If the given index of a Qiskrypt's Fully-Quantum Register to be removed
                from the list of Qiskrypt's Registers of the Qiskrypt's Party Client is valid.
                """

                current_register = super().registers[fully_quantum_register_index]
                """
                Retrieve the respective Qiskrypt's Register in
                the list of Qiskrypt's Registers of the Qiskrypt's Party Client.
                """

                if isinstance(current_register, QiskryptFullyQuantumRegister):
                    """
                    If the current Qiskrypt's Register in
                    the list of Qiskrypt's Registers of the Qiskrypt's Party Client
                    is a Qiskrypt's Fully-Quantum Register.
                    """

                    super().registers.remove(current_register)
                    """
                    Removes the current Qiskrypt's Register in
                    the list of Qiskrypt's Registers of the Qiskrypt's Party Client.
                    """

                else:
                    """
                    If the current Qiskrypt's Register in
                    the list of Qiskrypt's Registers of the Qiskrypt's Party Client
                    is not a Qiskrypt's Fully-Quantum Register.
                    """

                    # TODO Throw - Exception

            else:
                """
                If the given index of a Qiskrypt's Fully-Quantum Register to be removed
                from the list of Qiskrypt's Registers of the Qiskrypt's Party Client is not valid.
                """

                # TODO Throw - Exception

        else:
            """
            If the Qiskrypt's Endpoint of the Qiskrypt's Party Client 
            is not a Qiskrypt's Fully-Quantum Ground Station Endpoint 
            and does not belong to a Fully-Quantum Context.
            """

            # TODO Throw - Exception

    def add_ancilla_fully_quantum_register(self, ancilla_fully_quantum_register: QiskryptAncillaFullyQuantumRegister):
        """
        Adds a given Qiskrypt's Ancilla Fully-Quantum Register to
        the list of Qiskrypt's Registers of the Qiskrypt's Party Client.

        :param ancilla_fully_quantum_register: the Qiskrypt's Ancilla Fully-Quantum Register to be added
                                               to the list of Qiskrypt's Registers of
                                               the Qiskrypt's Party Client.
        """

        if (self.get_endpoint().get_context() == POSSIBLE_ENDPOINT_CONTEXTS[1]) and \
           (isinstance(self.get_endpoint(), QiskryptFullyQuantumGroundStationEndpoint)):
            """
            If the Qiskrypt's Endpoint of the Qiskrypt's Party Client 
            is a Qiskrypt's Fully-Quantum Ground Station Endpoint
            and belongs to a Fully-Quantum Context.
            """

            super().registers.append(ancilla_fully_quantum_register)
            """
            Adds the given Qiskrypt's Ancilla Fully-Quantum Register to
            the list of Qiskrypt's Registers of the Qiskrypt's Party Client.
            """

        else:
            """
            If the Qiskrypt's Endpoint of the Qiskrypt's Party Client 
            is not a Qiskrypt's Fully-Quantum Ground Station Endpoint 
            and does not belong to a Fully-Quantum Context.
            """

            # TODO Throw - Exception

    def remove_ancilla_fully_quantum_register_by_name(self, ancilla_fully_quantum_register_name: str):
        """
        Removes a Qiskrypt's Ancilla Fully-Quantum Register from
        the list of Qiskrypt's Registers of the Qiskrypt's Party Client,
        given its name.

        :param ancilla_fully_quantum_register_name: the name of a Qiskrypt's Ancilla Fully-Quantum Register
                                                    to be removed from the list of Qiskrypt's Registers of
                                                    the Qiskrypt's Party Client.
        """

        if (self.get_endpoint().get_context() == POSSIBLE_ENDPOINT_CONTEXTS[1]) and \
           (isinstance(self.get_endpoint(), QiskryptFullyQuantumGroundStationEndpoint)):
            """
            If the Qiskrypt's Endpoint of the Qiskrypt's Party Client 
            is a Qiskrypt's Fully-Quantum Ground Station Endpoint
            and belongs to a Fully-Quantum Context.
            """

            for current_register_index in range(len(super().registers)):
                """
                For each Qiskrypt's Register in the list of
                Qiskrypt's Registers of the Qiskrypt's Party Client. 
                """

                current_register = super().registers[current_register_index]
                """
                Retrieve the current Qiskrypt's Register in
                the list of Qiskrypt's Registers of the Qiskrypt's Party Client.
                """

                if current_register.get_name() == ancilla_fully_quantum_register_name:
                    """
                    If it was found a Qiskrypt's Register in
                    the list of Qiskrypt's Registers of the Qiskrypt's Party Client,
                    with the given name.
                    """

                    if isinstance(current_register, QiskryptAncillaFullyQuantumRegister):
                        """
                        If the current Qiskrypt's Register in
                        the list of Qiskrypt's Registers of the Qiskrypt's Party Client
                        is a Qiskrypt's Ancilla Fully-Quantum Register.
                        """

                        super().registers.remove(current_register)
                        """
                        Removes the current Qiskrypt's Register in
                        the list of Qiskrypt's Registers of the Qiskrypt's Party Client.
                        """

                    else:
                        """
                        If the current Qiskrypt's Register in
                        the list of Qiskrypt's Registers of the Qiskrypt's Party Client
                        is not a Qiskrypt's Ancilla Fully-Quantum Register.
                        """

                        # TODO Throw - Exception

        else:
            """
            If the Qiskrypt's Endpoint of the Qiskrypt's Party Client 
            is not a Qiskrypt's Fully-Quantum Ground Station Endpoint 
            and does not belong to a Fully-Quantum Context.
            """

            # TODO Throw - Exception

    def remove_ancilla_fully_quantum_register_by_index(self, ancilla_fully_quantum_register_index: int):
        """
        Removes a Qiskrypt's Ancilla Fully-Quantum Register from
        the list of Qiskrypt's Registers of the Qiskrypt's Party Client,
        given its index.

        :param ancilla_fully_quantum_register_index: the index of a Qiskrypt's Ancilla Fully-Quantum Register
                                                     to be removed from the list of Qiskrypt's Registers of
                                                     the Qiskrypt's Party Client.
        """

        if (self.get_endpoint().get_context() == POSSIBLE_ENDPOINT_CONTEXTS[1]) and \
           (isinstance(self.get_endpoint(), QiskryptFullyQuantumGroundStationEndpoint)):
            """
            If the Qiskrypt's Endpoint of the Qiskrypt's Party Client 
            is a Qiskrypt's Fully-Quantum Ground Station Endpoint
            and belongs to a Fully-Quantum Context.
            """

            if ancilla_fully_quantum_register_index < self.get_num_registers():
                """
                If the given index of a Qiskrypt's Ancilla Fully-Quantum Register to be removed
                from the list of Qiskrypt's Registers of the Qiskrypt's Party Client is valid.
                """

                current_register = super().registers[ancilla_fully_quantum_register_index]
                """
                Retrieve the respective Qiskrypt's Register in
                the list of Qiskrypt's Registers of the Qiskrypt's Party Client.
                """

                if isinstance(current_register, QiskryptAncillaFullyQuantumRegister):
                    """
                    If the current Qiskrypt's Register in
                    the list of Qiskrypt's Registers of the Qiskrypt's Party Client
                    is a Qiskrypt's Ancilla Fully-Quantum Register.
                    """

                    super().registers.remove(current_register)
                    """
                    Removes the current Qiskrypt's Register in
                    the list of Qiskrypt's Registers of the Qiskrypt's Party Client.
                    """

                else:
                    """
                    If the current Qiskrypt's Register in
                    the list of Qiskrypt's Registers of the Qiskrypt's Party Client
                    is not a Qiskrypt's Ancilla Fully-Quantum Register.
                    """

                    # TODO Throw - Exception

            else:
                """
                If the given index of a Qiskrypt's Ancilla Fully-Quantum Register to be removed
                from the list of Qiskrypt's Registers of the Qiskrypt's Party Client is not valid.
                """

                # TODO Throw - Exception

        else:
            """
            If the Qiskrypt's Endpoint of the Qiskrypt's Party Client 
            is not a Qiskrypt's Fully-Quantum Ground Station Endpoint 
            and does not belong to a Fully-Quantum Context.
            """

            # TODO Throw - Exception

    def add_semi_quantum_register(self, semi_quantum_register: QiskryptSemiQuantumRegister):
        """
        Adds a given Qiskrypt's Semi-Quantum Register to
        the list of Qiskrypt's Registers of the Qiskrypt's Party Client.

        :param semi_quantum_register: the Qiskrypt's Semi-Quantum Register to be added
                                      to the list of Qiskrypt's Registers of
                                      the Qiskrypt's Party Client.
        """

        if (self.get_endpoint().get_context() == POSSIBLE_ENDPOINT_CONTEXTS[2]) and \
           (isinstance(self.get_endpoint(), QiskryptSemiQuantumGroundStationEndpoint)):
            """
            If the Qiskrypt's Endpoint of the Qiskrypt's Party Client 
            is a Qiskrypt's Semi-Quantum Ground Station Endpoint
            and belongs to a Semi-Quantum Context.
            """

            super().registers.append(semi_quantum_register)
            """
            Adds the given Qiskrypt's Semi-Quantum Register to
            the list of Qiskrypt's Registers of the Qiskrypt's Party Client.
            """

        else:
            """
            If the Qiskrypt's Endpoint of the Qiskrypt's Party Client 
            is not a Qiskrypt's Semi-Quantum Ground Station Endpoint 
            and does not belong to a Semi-Quantum Context.
            """

            # TODO Throw - Exception

    def remove_semi_quantum_register_by_name(self, semi_quantum_register_name: str):
        """
        Removes a Qiskrypt's Semi-Quantum Register from
        the list of Qiskrypt's Registers of the Qiskrypt's Party Client,
        given its name.

        :param semi_quantum_register_name: the name of a Qiskrypt's Semi-Quantum Register
                                           to be removed from the list of Qiskrypt's Registers of
                                           the Qiskrypt's Party Client.
        """

        if (self.get_endpoint().get_context() == POSSIBLE_ENDPOINT_CONTEXTS[2]) and \
           (isinstance(self.get_endpoint(), QiskryptSemiQuantumGroundStationEndpoint)):
            """
            If the Qiskrypt's Endpoint of the Qiskrypt's Party Client 
            is a Qiskrypt's Semi-Quantum Ground Station Endpoint
            and belongs to a Semi-Quantum Context.
            """

            for current_register_index in range(len(super().registers)):
                """
                For each Qiskrypt's Register in the list of
                Qiskrypt's Registers of the Qiskrypt's Party Client. 
                """

                current_register = super().registers[current_register_index]
                """
                Retrieve the current Qiskrypt's Register in
                the list of Qiskrypt's Registers of the Qiskrypt's Party Client.
                """

                if current_register.get_name() == semi_quantum_register_name:
                    """
                    If it was found a Qiskrypt's Register in
                    the list of Qiskrypt's Registers of the Qiskrypt's Party Client,
                    with the given name.
                    """

                    if isinstance(current_register, QiskryptSemiQuantumRegister):
                        """
                        If the current Qiskrypt's Register in
                        the list of Qiskrypt's Registers of the Qiskrypt's Party Client
                        is a Qiskrypt's Semi-Quantum Register.
                        """

                        super().registers.remove(current_register)
                        """
                        Removes the current Qiskrypt's Register in
                        the list of Qiskrypt's Registers of the Qiskrypt's Party Client.
                        """

                    else:
                        """
                        If the current Qiskrypt's Register in
                        the list of Qiskrypt's Registers of the Qiskrypt's Party Client
                        is not a Qiskrypt's Semi-Quantum Register.
                        """

                        # TODO Throw - Exception

        else:
            """
            If the Qiskrypt's Endpoint of the Qiskrypt's Party Client 
            is not a Qiskrypt's Semi-Quantum Ground Station Endpoint 
            and does not belong to a Semi-Quantum Context.
            """

            # TODO Throw - Exception

    def remove_semi_quantum_register_by_index(self, semi_quantum_register_index: int):
        """
        Removes a Qiskrypt's Semi-Quantum Register from
        the list of Qiskrypt's Registers of the Qiskrypt's Party Client,
        given its index.

        :param semi_quantum_register_index: the index of a Qiskrypt's Semi-Quantum Register
                                            to be removed from the list of Qiskrypt's Registers of
                                            the Qiskrypt's Party Client.
        """

        if (self.get_endpoint().get_context() == POSSIBLE_ENDPOINT_CONTEXTS[2]) and \
           (isinstance(self.get_endpoint(), QiskryptSemiQuantumGroundStationEndpoint)):
            """
            If the Qiskrypt's Endpoint of the Qiskrypt's Party Client 
            is a Qiskrypt's Semi-Quantum Ground Station Endpoint
            and belongs to a Semi-Quantum Context.
            """

            if semi_quantum_register_index < self.get_num_registers():
                """
                If the given index of a Qiskrypt's Semi-Quantum Register to be removed
                from the list of Qiskrypt's Registers of the Qiskrypt's Party Client is valid.
                """

                current_register = super().registers[semi_quantum_register_index]
                """
                Retrieve the respective Qiskrypt's Register in
                the list of Qiskrypt's Registers of the Qiskrypt's Party Client.
                """

                if isinstance(current_register, QiskryptSemiQuantumRegister):
                    """
                    If the current Qiskrypt's Register in
                    the list of Qiskrypt's Registers of the Qiskrypt's Party Client
                    is a Qiskrypt's Semi-Quantum Register.
                    """

                    super().registers.remove(current_register)
                    """
                    Removes the current Qiskrypt's Register in
                    the list of Qiskrypt's Registers of the Qiskrypt's Party Client.
                    """

                else:
                    """
                    If the current Qiskrypt's Register in
                    the list of Qiskrypt's Registers of the Qiskrypt's Party Client
                    is not a Qiskrypt's Semi-Quantum Register.
                    """

                    # TODO Throw - Exception

            else:
                """
                If the given index of a Qiskrypt's Semi-Quantum Register to be removed
                from the list of Qiskrypt's Registers of the Qiskrypt's Party Client is not valid.
                """

                # TODO Throw - Exception

        else:
            """
            If the Qiskrypt's Endpoint of the Qiskrypt's Party Client 
            is not a Qiskrypt's Semi-Quantum Ground Station Endpoint 
            and does not belong to a Semi-Quantum Context.
            """

            # TODO Throw - Exception

    def add_ancilla_semi_quantum_register(self, ancilla_semi_quantum_register: QiskryptAncillaSemiQuantumRegister):
        """
        Adds a given Qiskrypt's Ancilla Semi-Quantum Register to
        the list of Qiskrypt's Registers of the Qiskrypt's Party Client.

        :param ancilla_semi_quantum_register: the Qiskrypt's Ancilla Semi-Quantum Register to be added
                                              to the list of Qiskrypt's Registers of
                                              the Qiskrypt's Party Client.
        """

        if (self.get_endpoint().get_context() == POSSIBLE_ENDPOINT_CONTEXTS[2]) and \
           (isinstance(self.get_endpoint(), QiskryptSemiQuantumGroundStationEndpoint)):
            """
            If the Qiskrypt's Endpoint of the Qiskrypt's Party Client 
            is a Qiskrypt's Semi-Quantum Ground Station Endpoint
            and belongs to a Semi-Quantum Context.
            """

            super().registers.append(ancilla_semi_quantum_register)
            """
            Adds the given Qiskrypt's Ancilla Semi-Quantum Register to
            the list of Qiskrypt's Registers of the Qiskrypt's Party Client.
            """

        else:
            """
            If the Qiskrypt's Endpoint of the Qiskrypt's Party Client 
            is not a Qiskrypt's Semi-Quantum Ground Station Endpoint 
            and does not belong to a Semi-Quantum Context.
            """

            # TODO Throw - Exception

    def remove_ancilla_semi_quantum_register_by_name(self, ancilla_semi_quantum_register_name: str):
        """
        Removes a Qiskrypt's Ancilla Semi-Quantum Register from
        the list of Qiskrypt's Registers of the Qiskrypt's Party Client,
        given its name.

        :param ancilla_semi_quantum_register_name: the name of a Qiskrypt's Ancilla Semi-Quantum Register
                                                   to be removed from the list of Qiskrypt's Registers of
                                                   the Qiskrypt's Party Client.
        """

        if (self.get_endpoint().get_context() == POSSIBLE_ENDPOINT_CONTEXTS[2]) and \
           (isinstance(self.get_endpoint(), QiskryptSemiQuantumGroundStationEndpoint)):
            """
            If the Qiskrypt's Endpoint of the Qiskrypt's Party Client 
            is a Qiskrypt's Semi-Quantum Ground Station Endpoint
            and belongs to a Semi-Quantum Context.
            """

            for current_register_index in range(len(super().registers)):
                """
                For each Qiskrypt's Register in the list of
                Qiskrypt's Registers of the Qiskrypt's Party Client. 
                """

                current_register = super().registers[current_register_index]
                """
                Retrieve the current Qiskrypt's Register in
                the list of Qiskrypt's Registers of the Qiskrypt's Party Client.
                """

                if current_register.get_name() == ancilla_semi_quantum_register_name:
                    """
                    If it was found a Qiskrypt's Register in
                    the list of Qiskrypt's Registers of the Qiskrypt's Party Client,
                    with the given name.
                    """

                    if isinstance(current_register, QiskryptAncillaSemiQuantumRegister):
                        """
                        If the current Qiskrypt's Register in
                        the list of Qiskrypt's Registers of the Qiskrypt's Party Client
                        is a Qiskrypt's Ancilla Semi-Quantum Register.
                        """

                        super().registers.remove(current_register)
                        """
                        Removes the current Qiskrypt's Register in
                        the list of Qiskrypt's Registers of the Qiskrypt's Party Client.
                        """

                    else:
                        """
                        If the current Qiskrypt's Register in
                        the list of Qiskrypt's Registers of the Qiskrypt's Party Client
                        is not a Qiskrypt's Ancilla Semi-Quantum Register.
                        """

                        # TODO Throw - Exception

        else:
            """
            If the Qiskrypt's Endpoint of the Qiskrypt's Party Client 
            is not a Qiskrypt's Semi-Quantum Ground Station Endpoint 
            and does not belong to a Semi-Quantum Context.
            """

            # TODO Throw - Exception

    def remove_ancilla_semi_quantum_register_by_index(self, ancilla_semi_quantum_register_index: int):
        """
        Removes a Qiskrypt's Ancilla Semi-Quantum Register from
        the list of Qiskrypt's Registers of the Qiskrypt's Party Client,
        given its index.

        :param ancilla_semi_quantum_register_index: the index of a Qiskrypt's Ancilla Semi-Quantum Register
                                                    to be removed from the list of Qiskrypt's Registers of
                                                    the Qiskrypt's Party Client.
        """

        if (self.get_endpoint().get_context() == POSSIBLE_ENDPOINT_CONTEXTS[2]) and \
           (isinstance(self.get_endpoint(), QiskryptSemiQuantumGroundStationEndpoint)):
            """
            If the Qiskrypt's Endpoint of the Qiskrypt's Party Client 
            is a Qiskrypt's Semi-Quantum Ground Station Endpoint
            and belongs to a Semi-Quantum Context.
            """

            if ancilla_semi_quantum_register_index < self.get_num_registers():
                """
                If the given index of a Qiskrypt's Ancilla Semi-Quantum Register to be removed
                from the list of Qiskrypt's Registers of the Qiskrypt's Party Client is valid.
                """

                current_register = super().registers[ancilla_semi_quantum_register_index]
                """
                Retrieve the respective Qiskrypt's Register in
                the list of Qiskrypt's Registers of the Qiskrypt's Party Client.
                """

                if isinstance(current_register, QiskryptAncillaSemiQuantumRegister):
                    """
                    If the current Qiskrypt's Register in
                    the list of Qiskrypt's Registers of the Qiskrypt's Party Client
                    is a Qiskrypt's Ancilla Semi-Quantum Register.
                    """

                    super().registers.remove(current_register)
                    """
                    Removes the current Qiskrypt's Register in
                    the list of Qiskrypt's Registers of the Qiskrypt's Party Client.
                    """

                else:
                    """
                    If the current Qiskrypt's Register in
                    the list of Qiskrypt's Registers of the Qiskrypt's Party Client
                    is not a Qiskrypt's Ancilla Semi-Quantum Register.
                    """

                    # TODO Throw - Exception

            else:
                """
                If the given index of a Qiskrypt's Ancilla Semi-Quantum Register to be removed
                from the list of Qiskrypt's Registers of the Qiskrypt's Party Client is not valid.
                """

                # TODO Throw - Exception

        else:
            """
            If the Qiskrypt's Endpoint of the Qiskrypt's Party Client 
            is not a Qiskrypt's Semi-Quantum Ground Station Endpoint 
            and does not belong to a Semi-Quantum Context.
            """

            # TODO Throw - Exception

    def add_classical_register(self, classical_register: QiskryptClassicalRegister):
        """
        Adds a given Qiskrypt's Classical Register to
        the list of Qiskrypt's Registers of the Qiskrypt's Party Client.

        :param classical_register: the Qiskrypt's Classical Register to be added
                                   to the list of Qiskrypt's Registers of
                                   the Qiskrypt's Party Client.
        """

        if (self.get_endpoint().get_context() == POSSIBLE_ENDPOINT_CONTEXTS[3]) and \
           (isinstance(self.get_endpoint(), QiskryptClassicalGroundStationEndpoint)):
            """
            If the Qiskrypt's Endpoint of the Qiskrypt's Party Client 
            is a Qiskrypt's Classical Ground Station Endpoint
            and belongs to a Classical Context.
            """

            super().registers.append(classical_register)
            """
            Adds the given Qiskrypt's Classical Register to
            the list of Qiskrypt's Registers of the Qiskrypt's Party Client.
            """

        else:
            """
            If the Qiskrypt's Endpoint of the Qiskrypt's Party Client 
            is not a Qiskrypt's Classical Ground Station Endpoint 
            and does not belong to a Classical Context.
            """

            # TODO Throw - Exception

    def remove_classical_register_by_name(self, classical_register_name: str):
        """
        Removes a Qiskrypt's Classical Register from
        the list of Qiskrypt's Registers of the Qiskrypt's Party Client,
        given its name.

        :param classical_register_name: the name of a Qiskrypt's Classical Register
                                        to be removed from the list of Qiskrypt's Registers of
                                        the Qiskrypt's Party Client.
        """

        if (self.get_endpoint().get_context() == POSSIBLE_ENDPOINT_CONTEXTS[3]) and \
           (isinstance(self.get_endpoint(), QiskryptClassicalGroundStationEndpoint)):
            """
            If the Qiskrypt's Endpoint of the Qiskrypt's Party Client 
            is a Qiskrypt's Classical Ground Station Endpoint
            and belongs to a Classical Context.
            """

            for current_register_index in range(len(super().registers)):
                """
                For each Qiskrypt's Register in the list of
                Qiskrypt's Registers of the Qiskrypt's Party Client. 
                """

                current_register = super().registers[current_register_index]
                """
                Retrieve the current Qiskrypt's Register in
                the list of Qiskrypt's Registers of the Qiskrypt's Party Client.
                """

                if current_register.get_name() == classical_register_name:
                    """
                    If it was found a Qiskrypt's Register in
                    the list of Qiskrypt's Registers of the Qiskrypt's Party Client,
                    with the given name.
                    """

                    if isinstance(current_register, QiskryptClassicalRegister):
                        """
                        If the current Qiskrypt's Register in
                        the list of Qiskrypt's Registers of the Qiskrypt's Party Client
                        is a Qiskrypt's Classical Register.
                        """

                        super().registers.remove(current_register)
                        """
                        Removes the current Qiskrypt's Register in
                        the list of Qiskrypt's Registers of the Qiskrypt's Party Client.
                        """

                    else:
                        """
                        If the current Qiskrypt's Register in
                        the list of Qiskrypt's Registers of the Qiskrypt's Party Client
                        is not a Qiskrypt's Classical Register.
                        """

                        # TODO Throw - Exception

        else:
            """
            If the Qiskrypt's Endpoint of the Qiskrypt's Party Client 
            is not a Qiskrypt's Classical Ground Station Endpoint 
            and does not belong to a Classical Context.
            """

            # TODO Throw - Exception

    def remove_classical_register_by_index(self, classical_register_index: int):
        """
        Removes a Qiskrypt's Classical Register from
        the list of Qiskrypt's Registers of the Qiskrypt's Party Client,
        given its index.

        :param classical_register_index: the index of a Qiskrypt's Ancilla Semi-Quantum Register
                                         to be removed from the list of Qiskrypt's Registers of
                                         the Qiskrypt's Party Client.
        """

        if (self.get_endpoint().get_context() == POSSIBLE_ENDPOINT_CONTEXTS[3]) and \
           (isinstance(self.get_endpoint(), QiskryptClassicalGroundStationEndpoint)):
            """
            If the Qiskrypt's Endpoint of the Qiskrypt's Party Client 
            is a Qiskrypt's Classical Ground Station Endpoint
            and belongs to a Classical Context.
            """

            if classical_register_index < self.get_num_registers():
                """
                If the given index of a Qiskrypt's Classical Register to be removed
                from the list of Qiskrypt's Registers of the Qiskrypt's Party Client is valid.
                """

                current_register = super().registers[classical_register_index]
                """
                Retrieve the respective Qiskrypt's Register in
                the list of Qiskrypt's Registers of the Qiskrypt's Party Client.
                """

                if isinstance(current_register, QiskryptClassicalRegister):
                    """
                    If the current Qiskrypt's Register in
                    the list of Qiskrypt's Registers of the Qiskrypt's Party Client
                    is a Qiskrypt's Classical Register.
                    """

                    super().registers.remove(current_register)
                    """
                    Removes the current Qiskrypt's Register in
                    the list of Qiskrypt's Registers of the Qiskrypt's Party Client.
                    """

                else:
                    """
                    If the current Qiskrypt's Register in
                    the list of Qiskrypt's Registers of the Qiskrypt's Party Client
                    is not a Qiskrypt's Classical Register.
                    """

                    # TODO Throw - Exception

            else:
                """
                If the given index of a Qiskrypt's Classical Register to be removed
                from the list of Qiskrypt's Registers of the Qiskrypt's Party Client is not valid.
                """

                # TODO Throw - Exception

        else:
            """
            If the Qiskrypt's Endpoint of the Qiskrypt's Party Client 
            is not a Qiskrypt's Classical Ground Station Endpoint 
            and does not belong to a Classical Context.
            """

            # TODO Throw - Exception
