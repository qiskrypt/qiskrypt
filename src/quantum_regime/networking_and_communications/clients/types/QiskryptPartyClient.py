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

from src.quantum_regime.networking_and_communications.endpoints.QiskryptEndpoint \
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

from src.quantum_regime.networking_and_communications.endpoints.QiskryptEndpoint \
    import POSSIBLE_ENDPOINT_CONTEXTS
"""
Import the available Endpoint contexts for the Qiskrypt's Endpoints.
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

        self.endpoints = list()
        """
        Set the list of Qiskrypt's Endpoints for the Qiskrypt's Party Client, initially, as an empty list.
        """

        self.roles = list()
        """
        Set the list of roles for the Qiskrypt's Party Client, initially, as an empty list.
        """

        self.items = dict()
        """
        Set the dictionary of items of the Qiskrypt's Party Client, initially, as an empty dictionary.
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

    def get_ancilla_quantum_registers(self) -> list:
        """
        Return the list of the Qiskrypt's Ancilla Quantum Registers of the Qiskrypt's Client.

        :return ancilla_quantum_registers: the list of the Qiskrypt's Ancilla Quantum Registers of
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

        ancilla_quantum_registers = list()
        """
        Create the list of the Qiskrypt's Ancilla Quantum Registers of
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

            if isinstance(current_register, QiskryptAncillaQuantumRegister):
                """
                If the current Qiskrypt's Register of the Qiskrypt's Client
                is really a Qiskrypt's Ancilla Quantum Register.
                """

                ancilla_quantum_registers.append(current_register)
                """
                Append the current Qiskrypt's Register of the Qiskrypt's Client
                to the list of Qiskrypt's Ancilla Quantum Registers.
                """

        """
        Return the list of the Qiskrypt's Ancilla Quantum Registers of
        the Qiskrypt's Client.
        """
        return ancilla_quantum_registers

    def get_num_ancilla_quantum_registers(self) -> int:
        """
        Return the number of Qiskrypt's Ancilla Quantum Registers in
        the list of Qiskrypt's Registers of the Qiskrypt's Client.

        :return len(self.get_ancilla_quantum_registers()): the number of Qiskrypt's Ancilla Quantum Registers in
                                                           the list of Qiskrypt's Registers of
                                                           the Qiskrypt's Client.
        """

        """
        Return the number of Qiskrypt's Ancilla Quantum Registers in
        the list of Qiskrypt's Registers of the Qiskrypt's Client.
        """
        return len(self.get_quantum_registers())

    def get_ancilla_fully_quantum_registers(self) -> list:
        """
        Return the list of the Qiskrypt's Ancilla Fully-Quantum Registers of the Qiskrypt's Client.

        :return ancilla_fully_quantum_registers: the list of the Qiskrypt's Ancilla Fully-Quantum
                                                 Registers of the Qiskrypt's Client.
        """

        registers = super().get_registers()
        """
        Retrieve the list of the Qiskrypt's Registers of the Qiskrypt's Client.
        """

        num_registers = super().get_num_registers()
        """
        Retrieve number of the Qiskrypt's Registers of the Qiskrypt's Client.
        """

        ancilla_fully_quantum_registers = list()
        """
        Create the list of the Qiskrypt's Ancilla Fully-Quantum Registers of
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

            if isinstance(current_register, QiskryptAncillaFullyQuantumRegister):
                """
                If the current Qiskrypt's Register of the Qiskrypt's Client
                is really a Qiskrypt's Ancilla Fully-Quantum Register.
                """

                ancilla_fully_quantum_registers.append(current_register)
                """
                Append the current Qiskrypt's Register of the Qiskrypt's Client
                to the list of Qiskrypt's Ancilla Fully-Quantum Registers.
                """

        """
        Return the list of the Qiskrypt's Ancilla Fully-Quantum Registers of
        the Qiskrypt's Client.
        """
        return ancilla_fully_quantum_registers

    def get_num_ancilla_fully_quantum_registers(self) -> int:
        """
        Return the number of Qiskrypt's Ancilla Fully-Quantum Registers in
        the list of Qiskrypt's Registers of the Qiskrypt's Client.

        :return len(self.get_ancilla_fully_quantum_registers()): the number of Qiskrypt's Ancilla Fully-Quantum
                                                                 Registers in the list of Qiskrypt's Registers of
                                                                 the Qiskrypt's Client.
        """

        """
        Return the number of Qiskrypt's Ancilla Fully-Quantum Registers in
        the list of Qiskrypt's Registers of the Qiskrypt's Client.
        """
        return len(self.get_ancilla_fully_quantum_registers())

    def get_ancilla_semi_quantum_registers(self) -> list:
        """
        Return the list of the Qiskrypt's Ancilla Semi-Quantum Registers of the Qiskrypt's Client.

        :return ancilla_semi_quantum_registers: the list of the Qiskrypt's Ancilla Semi-Quantum
                                                Registers of the Qiskrypt's Client.
        """

        registers = super().get_registers()
        """
        Retrieve the list of the Qiskrypt's Registers of the Qiskrypt's Client.
        """

        num_registers = super().get_num_registers()
        """
        Retrieve number of the Qiskrypt's Registers of the Qiskrypt's Client.
        """

        ancilla_semi_quantum_registers = list()
        """
        Create the list of the Qiskrypt's Ancilla Semi-Quantum Registers of
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

            if isinstance(current_register, QiskryptAncillaSemiQuantumRegister):
                """
                If the current Qiskrypt's Register of the Qiskrypt's Client
                is really a Qiskrypt's Ancilla Semi-Quantum Register.
                """

                ancilla_semi_quantum_registers.append(current_register)
                """
                Append the current Qiskrypt's Register of the Qiskrypt's Client
                to the list of Qiskrypt's Ancilla Semi-Quantum Registers.
                """

        """
        Return the list of the Qiskrypt's Ancilla Semi-Quantum Registers of
        the Qiskrypt's Client.
        """
        return ancilla_semi_quantum_registers

    def get_num_ancilla_semi_quantum_registers(self) -> int:
        """
        Return the number of Qiskrypt's Ancilla Semi-Quantum Registers in
        the list of Qiskrypt's Registers of the Qiskrypt's Client.

        :return len(self.get_ancilla_semi_quantum_registers()): the number of Qiskrypt's Ancilla Semi-Quantum
                                                                Registers in the list of Qiskrypt's Registers of
                                                                the Qiskrypt's Client.
        """

        """
        Return the number of Qiskrypt's Ancilla Semi-Quantum Registers in
        the list of Qiskrypt's Registers of the Qiskrypt's Client.
        """
        return len(self.get_ancilla_semi_quantum_registers())

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

    def get_endpoints(self) -> list:
        """
        Return the list of Qiskrypt's Endpoints of the Qiskrypt's Party Client.

        :return self.endpoints: the list of the Qiskrypt's Endpoints of the Qiskrypt's Party Client.
        """

        if super().is_connected():
            """
            If the Qiskrypt's Client is already connected.
            """

            """
            Return the list of the Qiskrypt's Endpoints of the Qiskrypt's Party Client.
            """
            return self.endpoints

        else:
            """
            If the Qiskrypt's Party Client is not connected yet.
            """

            # TODO Throw - Exception

    def get_num_endpoints(self) -> int:
        """
        Return the number of Qiskrypt's Endpoints of the Qiskrypt's Party Client.

        :return len(self.get_endpoints()): the number of Qiskrypt's Endpoints of
                                           the Qiskrypt's Party Client.
        """

        """
        Return the number of Qiskrypt's Endpoints of the Qiskrypt's Party Client.
        """
        return len(self.get_endpoints())

    def get_endpoint_by_index(self, endpoint_index: int) -> QiskryptEndpoint:
        """
        Return a certain Qiskrypt's Endpoint from the list of Qiskrypt's Endpoints of
        the Qiskrypt's Party Client, given the corresponding index.

        :param endpoint_index: the index of a certain Qiskrypt's Endpoint of
                               the Qiskrypt's Party Client.

        :return endpoint: the Qiskrypt's Endpoint from the list of Qiskrypt's Endpoints,
                          given the corresponding index.
        """

        if endpoint_index < self.get_num_endpoints():
            """
            If the given Qiskrypt's Endpoint's index is valid.
            """

            endpoints = self.get_endpoints()
            """
            Retrieve the list of Qiskrypt's Endpoints of the Qiskrypt's Party Client.
            """

            """
            Retrieve the Qiskrypt's Endpoint from the list of Qiskrypt's Endpoints,
            given the corresponding index.
            """
            endpoint = endpoints[endpoint_index]

            """
            Return the Qiskrypt's Endpoint from the list of Qiskrypt's Endpoints,
            given the corresponding index.
            """
            return endpoint

        else:
            """
            If the given Qiskrypt's Endpoint's index is not valid.
            """

            # TODO Throw - Exception

    def get_endpoint_by_name(self, endpoint_name: str):
        """
        Return a certain Qiskrypt's Endpoint from the list of Qiskrypt's Endpoints of
        the Qiskrypt's Party Client, given the corresponding name.

        :param endpoint_name: the name of a certain Qiskrypt's Endpoint of
                              the Qiskrypt's Party Client.

        :return endpoint: the Qiskrypt's Endpoint from the list of Qiskrypt's Endpoints,
                          given the corresponding name.
        """

        endpoints = self.get_endpoints()
        """
        Retrieve the list of Qiskrypt's Endpoints of the Qiskrypt's Party Client.
        """

        num_endpoints = self.get_num_endpoints()
        """
        Retrieve the number of Qiskrypt's Endpoints of the Qiskrypt's Party Client.
        """

        for current_endpoint_index in range(num_endpoints):
            """
            For each Qiskrypt's Endpoint's index.
            """

            current_endpoint = endpoints[current_endpoint_index]
            """
            Retrieve the current Qiskrypt's Endpoint.
            """

            if isinstance(current_endpoint, QiskryptEndpoint):
                """
                If the current Qiskrypt's Endpoint is really a Qiskrypt's Endpoint.
                """

                if current_endpoint.get_name() == endpoint_name:
                    """
                    If the current Qiskrypt's Endpoint has the given name,
                    the pretended Qiskrypt's Endpoint was found.
                    """

                    """
                    Return the Qiskrypt's Endpoint from the list of Qiskrypt's Endpoints,
                    given the corresponding name.
                    """
                    return current_endpoint

        """
        If no Qiskrypt's Endpoint with the given corresponding name was found in
        the list of Qiskrypt's Endpoints, return None.
        """
        return None

    def add_role(self, new_role: str) -> None:
        """
        Add a new role to the list of the roles of the Qiskrypt's Party Client.

        :param new_role: the new role to be added to the list of the roles of the Qiskrypt's Party Client.
        """

        if super().is_connected():
            """
            If the Qiskrypt's Client is already connected.
            """

            """
            Add the new role to the list of the roles of the Qiskrypt's Party Client.
            """
            self.roles.append(new_role)

        else:
            """
            If the Qiskrypt's Party Client is not connected yet.
            """

            # TODO Throw - Exception

    def remove_role(self, role: str) -> None:
        """
        Remove a role from the list of the roles of the Qiskrypt's Party Client.

        :param role: the role to be removed from the list of the roles of the Qiskrypt's Party Client.
        """

        if super().is_connected():
            """
            If the Qiskrypt's Client is already connected.
            """

            """
            Remove the role from the list of the roles of the Qiskrypt's Party Client.
            """
            self.roles.remove(role)

        else:
            """
            If the Qiskrypt's Party Client is not connected yet.
            """

            # TODO Throw - Exception

    def get_roles(self) -> list:
        """
        Return the list of the roles of the Qiskrypt's Party Client.

        :return self.roles: the list of the roles of the Qiskrypt's Party Client.
        """

        if super().is_connected():
            """
            If the Qiskrypt's Client is already connected.
            """

            """
            Return the list of the roles of the Qiskrypt's Party Client.
            """
            return self.roles

        else:
            """
            If the Qiskrypt's Party Client is not connected yet.
            """

            # TODO Throw - Exception

    def get_num_roles(self) -> int:
        """
        Return the number of the roles of the Qiskrypt's Party Client.

        :return len(self.get_roles()): the number of the roles points of
                                       the Qiskrypt's Party Client.
        """

        """
        Return the number of the roles of the Qiskrypt's Party Client.
        """
        return len(self.get_roles())

    def get_role_by_index(self, role_index: int) -> str:
        """
        Return a certain role from the list of the roles of
        the Qiskrypt's Party Client, given the corresponding index.

        :param role_index: the index of a certain role of the Qiskrypt's Party Client.

        :return role: the role from the list of the roles of the Qiskrypt's Party Client,
                      given the corresponding index.
        """

        if role_index < self.get_num_roles():
            """
            If the given role's index is valid.
            """

            roles = self.get_roles()
            """
            Retrieve the list of the roles of the Qiskrypt's Party Client.
            """

            """
            Retrieve the role from the list of the roles of the Qiskrypt's Party Client,
            given the corresponding index.
            """
            role = roles[role_index]

            """
            Return the role from the list of the roles of the Qiskrypt's Party Client,
            given the corresponding index.
            """
            return role

        else:
            """
            If the given role's index is not valid.
            """

            # TODO Throw - Exception

    def get_role_by_name(self, role_name: str):
        """
        Return a certain role from the list of the roles of
        the Qiskrypt's Party Client, given the corresponding name.

        :param role_name: the name of a certain role of the Qiskrypt's Party Client.

        :return role: the role from the list of the roles of the Qiskrypt's Party Client,
                      given the corresponding name.
        """

        roles = self.get_roles()
        """
        Retrieve the list of the roles of the Qiskrypt's Party Client.
        """

        num_roles = self.get_num_roles()
        """
        Retrieve the number of the roles of the Qiskrypt's Party Client.
        """

        for current_role_index in range(num_roles):
            """
            For each role's index.
            """

            current_role = roles[current_role_index]
            """
            Retrieve the current role.
            """

            if isinstance(current_role, str):
                """
                If the current role is really a string.
                """

                if current_role == role_name:
                    """
                    If the current role is equal to the given name,
                    the pretended role was found.
                    """

                    """
                    Return the role from the list of the roles of the Qiskrypt's Party Client,
                    given the corresponding name.
                    """
                    return current_role

        """
        If no role with the given corresponding name was found in
        the list of the roles of the Qiskrypt's Party Client, return None.
        """
        return None

    def add_item(self, new_item_key: object, new_item_value: object) -> None:
        """
        Add a new item to the dictionary of the items of the Qiskrypt's Party Client,
        with the corresponding given key and value.

        :param new_item_key: the key of the new item to be added to
                             the dictionary of the items of the Qiskrypt's Party Client.
        :param new_item_value: the value of the new item to be added to
                               the dictionary of the items of the Qiskrypt's Party Client.
        """

        if super().is_connected():
            """
            If the Qiskrypt's Client is already connected.
            """

            """
            Add the new item to the dictionary of the items of the Qiskrypt's Party Client,
            with the corresponding given key and value.
            """
            self.items[new_item_key] = new_item_value

        else:
            """
            If the Qiskrypt's Party Client is not connected yet.
            """

            # TODO Throw - Exception

    def remove_item(self, item_key: str) -> None:
        """
        Remove an item from the dictionary of the roles of the Qiskrypt's Party Client,
        with the corresponding given key.

        :param item_key: the role to be removed from the list of the roles of the Qiskrypt's Party Client.
        """

        if super().is_connected():
            """
            If the Qiskrypt's Client is already connected.
            """

            """
            Remove the item from the list of the roles of the Qiskrypt's Party Client,
            with the corresponding given key.
            """
            self.items.pop(item_key)

        else:
            """
            If the Qiskrypt's Party Client is not connected yet.
            """

            # TODO Throw - Exception

    def get_items(self) -> dict:
        """
        Return the dictionary of items of the Qiskrypt's Party Client.

        :return self.items: the dictionary of items of the Qiskrypt's Party Client.
        """

        if super().is_connected():
            """
            If the Qiskrypt's Client is already connected.
            """

            """
            Return the dictionary of items of the Qiskrypt's Party Client.
            """
            return self.items

        else:
            """
            If the Qiskrypt's Party Client is not connected yet.
            """

            # TODO Throw - Exception

    def get_num_items(self) -> int:
        """
        Return the number of items of the Qiskrypt's Party Client.

        :return len(self.get_items()): the number of items of
                                       the Qiskrypt's Party Client.
        """

        """
        Return the number of items of the Qiskrypt's Party Client.
        """
        return len(self.get_items())

    def get_items_keys(self) -> list:
        """
        Return the list of keys of items of the Qiskrypt's Party Client.

        :return list(self.get_items().keys()): the list of keys of items of
                                               the Qiskrypt's Party Client.
        """

        """
        Return the list of keys of the dictionary of items of
        the Qiskrypt's Party Client.
        """
        return list(self.get_items().keys())

    def get_items_values(self) -> list:
        """
        Return the list of values of items of the Qiskrypt's Party Client.

        :return list(self.get_items().values()): the list of values of items of
                                                 the Qiskrypt's Party Client.
        """

        """
        Return the list of values of the dictionary of items of
        the Qiskrypt's Party Client.
        """
        return list(self.get_items().values())

    def get_item_key_by_index(self, item_index: int) -> object:
        """
        Return a certain item key from the dictionary of items of
        the Qiskrypt's Party Client, given the corresponding index.

        :param item_index: the index of a certain item key from
                           the dictionary of items of the Qiskrypt's Party Client.

        :return item_key: the key of the item in the dictionary of items of
                          the Qiskrypt's Party Client, given the corresponding index.
        """

        if item_index < self.get_num_items():
            """
            If the given item's index is valid.
            """

            items_keys = self.get_items_keys()
            """
            Retrieve the list of keys of the dictionary of items in
            the dictionary of items of the Qiskrypt's Party Client.
            """

            """
            Retrieve the key of the item in the dictionary of items of
            the Qiskrypt's Party Client, given the corresponding index.
            """
            item_key = items_keys[item_index]

            """
            Return the key of the item in the dictionary of items of
            the Qiskrypt's Party Client, given the corresponding index.
            """
            return item_key

        else:
            """
            If the given item's index is not valid.
            """

            # TODO Throw - Exception

    def get_item_value_by_index(self, item_index: int) -> object:
        """
        Return a certain item value from the dictionary of items of
        the Qiskrypt's Party Client, given the corresponding index.

        :param item_index: the index of a certain item value from
                           the dictionary of items of the Qiskrypt's Party Client.

        :return item_value: the value of the item in the dictionary of items of
                            the Qiskrypt's Party Client, given the corresponding index.
        """

        if item_index < self.get_num_items():
            """
            If the given item's index is valid.
            """

            items_values = self.get_items_values()
            """
            Retrieve the list of values of the dictionary of items in
            the dictionary of items of the Qiskrypt's Party Client.
            """

            """
            Retrieve the value of the item in the dictionary of items of
            the Qiskrypt's Party Client, given the corresponding index.
            """
            item_value = items_values[item_index]

            """
            Return the value of the item in the dictionary of items of
            the Qiskrypt's Party Client, given the corresponding index.
            """
            return item_value

        else:
            """
            If the given item's index is not valid.
            """

            # TODO Throw - Exception

    def get_item_value_by_key(self, item_key: object) -> object:
        """
        Return a certain item value from the dictionary of items of
        the Qiskrypt's Party Client, given the corresponding key.

        :param item_key: the key of a certain item value from
                         the dictionary of items of the Qiskrypt's Party Client.

        :return item_value: the value of the item in the dictionary of items of
                            the Qiskrypt's Party Client, given the corresponding key.
        """

        """
        Retrieve the value of the item in the dictionary of items of
        the Qiskrypt's Party Client, given the corresponding key.
        """
        item_value = self.get_items()[item_key]

        """
        Return the value of the item in the dictionary of items of
        the Qiskrypt's Party Client, given the corresponding key.
        """
        return item_value

    def connect(self, party: QiskryptParty, endpoints: list):
        """
        Connect a Qiskrypt's Party and a list of Qiskrypt's Endpoints, to the Qiskrypt's Party Client.

        :param party: the Qiskrypt's Party to be connected to the Qiskrypt's Party Client.
        :param endpoints: the list of Qiskrypt's Endpoints to be connected to the Qiskrypt's Party Client.
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

            num_endpoints = len(endpoints)
            """
            Retrieve the number of Qiskrypt's Endpoints to be connected
            for the Qiskrypt's Party Client.
            """

            endpoints_station_type = None
            """
            Initialise a local variable to keep the station type of
            the Qiskrypt's Endpoints, initially, as None.
            """

            endpoints_longitude = None
            """
            Initialise a local variable to keep the longitude of
            the Qiskrypt's Endpoints, initially, as None.
            """

            endpoints_latitude = None
            """
            Initialise a local variable to keep the latitude of
            the Qiskrypt's Endpoints, initially, as None.
            """

            endpoints_altitude_in_kms = None
            """
            Initialise a local variable to keep the altitude in KMs (Kilometers) of
            the Qiskrypt's Endpoints, initially, as None.
            """

            for current_endpoint_index in range(num_endpoints):
                """
                For each possibly Qiskrypt's Endpoint's index.
                """

                current_endpoint = endpoints[current_endpoint_index]
                """
                Retrieve the current Qiskrypt's Endpoint.
                """

                if isinstance(current_endpoint, QiskryptEndpoint):
                    """
                    If the current Qiskrypt's Endpoint is really a Qiskrypt's Endpoint.
                    """

                    if current_endpoint_index == 0:
                        """
                        If the current Qiskrypt's Endpoint is the first one to be treated.
                        """

                        endpoints_station_type = current_endpoint.get_station_type()
                        """
                        Keep the station type of the first Qiskrypt's Endpoint
                        to compare with the remaining ones to be added, in order to ensure
                        that all the information is completely coherent.
                        """

                        endpoints_longitude = current_endpoint.get_longitude()
                        """
                        Keep the longitude of the first Qiskrypt's Endpoint
                        to compare with the remaining ones to be added, in order to ensure
                        that all the information is completely coherent.
                        """

                        endpoints_latitude = current_endpoint.get_latitude()
                        """
                        Keep the latitude of the first Qiskrypt's Endpoint
                        to compare with the remaining ones to be added, in order to ensure
                        that all the information is completely coherent.
                        """

                        endpoints_altitude_in_kms = current_endpoint.get_altitude_in_kms()
                        """
                        Keep the altitude in KMs (Kilometers) of the first Qiskrypt's Endpoint
                        to compare with the remaining ones to be added, in order to ensure
                        that all the information is completely coherent.
                        """

                    else:
                        """
                        If the current Qiskrypt's Endpoint is not the first one to be treated.
                        """

                        boolean_validation_station_type = \
                            (endpoints_station_type == current_endpoint.get_station_type())
                        """
                        Retrieve the boolean validation to keep information about
                        if the station type of the current Qiskrypt's Endpoint is correct. 
                        """

                        boolean_validation_longitude = \
                            (endpoints_longitude == current_endpoint.get_longitude())
                        """
                        Retrieve the boolean validation to keep information about
                        if the longitude of the current Qiskrypt's Endpoint is correct.
                        """

                        boolean_validation_latitude = \
                            (endpoints_latitude == current_endpoint.get_latitude())
                        """
                        Retrieve the boolean validation to keep information about
                        if the latitude of the current Qiskrypt's Endpoint is correct.
                        """

                        boolean_validation_altitude_in_kms = \
                            (endpoints_altitude_in_kms == current_endpoint.get_altitude_in_kms())
                        """
                        Retrieve the boolean validation to keep information about
                        if the altitude in KMs (Kilometers) of the current Qiskrypt's Endpoint is correct.
                        """

                        if (boolean_validation_station_type and boolean_validation_longitude
                                and boolean_validation_latitude and boolean_validation_altitude_in_kms):
                            """
                            If all the boolean validations to keep information about
                            the correctness of the current Qiskrypt's Endpoint hold.
                            """

                            self.endpoints.append(current_endpoint)
                            """
                            Append the current Qiskrypt's Endpoint to the list of
                            Qiskrypt's Endpoints of the Qiskrypt's Party Client.
                            """

                        else:
                            """
                            If some of the boolean validations to keep information about
                            the correctness of the current Qiskrypt's Endpoint hold.
                            """

                            # TODO Throw - Exception

                else:
                    """
                    If the current Qiskrypt's Endpoint is not a Qiskrypt's Endpoint.
                    """

                    # TODO Throw - Exception

            self.endpoints = endpoints
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

    def add_quantum_register_to_endpoint(self, quantum_register: QiskryptQuantumRegister,
                                         endpoint_index=None, endpoint_name=None):
        """
        Adds a given Qiskrypt's Quantum Register to
        the list of Qiskrypt's Registers of the Qiskrypt's Party Client,
        regarding the given index or name of a Qiskrypt's Endpoint.

        :param quantum_register: the Qiskrypt's Quantum Register to be added
                                 to the list of Qiskrypt's Registers of
                                 the Qiskrypt's Party Client.
        :param endpoint_index: the index of the Qiskrypt's Endpoint related to
                               the Qiskrypt's Quantum Register to be added
                               to the list of Qiskrypt's Registers of
                               the Qiskrypt's Party Client.
        :param endpoint_name: the name of the Qiskrypt's Endpoint related to
                              the Qiskrypt's Quantum Register to be added
                              to the list of Qiskrypt's Registers of
                              the Qiskrypt's Party Client.
        """

        if (endpoint_index is not None) or (endpoint_name is not None):
            """
            If the given index or name of the Qiskrypt's Endpoint related to
            the Qiskrypt's Quantum Register to be added to the list of
            Qiskrypt's Registers of the Qiskrypt's Party Client is not None.
            """

            endpoint = None
            """
            Initialise the local variable to keep the Qiskrypt's Endpoint related to
            the Qiskrypt's Quantum Register to be added to the list of
            Qiskrypt's Registers of the Qiskrypt's Party Client, initially, as None.
            """

            if endpoint_index is not None:
                """
                If the given index of the Qiskrypt's Endpoint related to
                the Qiskrypt's Quantum Register to be added to the list of
                Qiskrypt's Registers of the Qiskrypt's Party Client is not None.
                """

                """
                Retrieve the Qiskrypt's Endpoint from the list of Qiskrypt's Endpoints of
                the Qiskrypt's Party Client, given the corresponding index.
                """
                endpoint = self.get_endpoint_by_index(endpoint_index)

            elif endpoint_name is not None:
                """
                If the given name of the Qiskrypt's Endpoint related to
                the Qiskrypt's Quantum Register to be added to the list of
                Qiskrypt's Registers of the Qiskrypt's Party Client is not None.
                """

                """
                Retrieve the Qiskrypt's Endpoint from the list of Qiskrypt's Endpoints of
                the Qiskrypt's Party Client, given the corresponding name.
                """
                endpoint = self.get_endpoint_by_name(endpoint_name)

            if endpoint is not None:
                """
                If the retrieved Qiskrypt's Endpoint from the list of Qiskrypt's Endpoints of
                the Qiskrypt's Party Client, given the corresponding index or name, is valid.
                """

                if (endpoint.get_context() == POSSIBLE_ENDPOINT_CONTEXTS[0]) and \
                        (isinstance(endpoint, QiskryptQuantumGroundStationEndpoint)):
                    """
                    If the retrieved Qiskrypt's Endpoint of the Qiskrypt's Party Client 
                    is a Qiskrypt's Quantum Ground Station Endpoint
                    and belongs to a Quantum Context.
                    """

                    super().get_registers().append(quantum_register)
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

            else:
                """
                If the retrieved Qiskrypt's Endpoint from the list of Qiskrypt's Endpoints of
                the Qiskrypt's Party Client, given the corresponding index or name, is not valid.
                """

                # TODO Throw - Exception

        else:
            """
            If the given index and name of the Qiskrypt's Endpoint related to
            the Qiskrypt's Quantum Register to be added to the list of
            Qiskrypt's Registers of the Qiskrypt's Party Client are both None.
            """

            # TODO Throw - Exception

    def remove_quantum_register_by_name_from_endpoint(self, quantum_register_name: str,
                                                      endpoint_index=None, endpoint_name=None):
        """
        Removes a Qiskrypt's Quantum Register from
        the list of Qiskrypt's Registers of the Qiskrypt's Party Client,
        given its name, regarding the given index or name of a Qiskrypt's Endpoint.

        :param quantum_register_name: the name of a Qiskrypt's Quantum Register to be removed
                                      from the list of Qiskrypt's Registers of
                                      the Qiskrypt's Party Client.
        :param endpoint_index: the index of the Qiskrypt's Endpoint related to
                               the Qiskrypt's Quantum Register to be removed
                               from the list of Qiskrypt's Registers of
                               the Qiskrypt's Party Client.
        :param endpoint_name: the name of the Qiskrypt's Endpoint related to
                              the Qiskrypt's Quantum Register to be removed
                              from the list of Qiskrypt's Registers of
                              the Qiskrypt's Party Client.
        """

        if (endpoint_index is not None) or (endpoint_name is not None):
            """
            If the given index or name of the Qiskrypt's Endpoint related to
            the Qiskrypt's Quantum Register to be removed from the list of
            Qiskrypt's Registers of the Qiskrypt's Party Client is not None.
            """

            endpoint = None
            """
            Initialise the local variable to keep the Qiskrypt's Endpoint related to
            the Qiskrypt's Quantum Register to be removed from the list of
            Qiskrypt's Registers of the Qiskrypt's Party Client, initially, as None.
            """

            if endpoint_index is not None:
                """
                If the given index of the Qiskrypt's Endpoint related to
                the Qiskrypt's Quantum Register to be removed from the list of
                Qiskrypt's Registers of the Qiskrypt's Party Client is not None.
                """

                """
                Retrieve the Qiskrypt's Endpoint from the list of Qiskrypt's Endpoints of
                the Qiskrypt's Party Client, given the corresponding index.
                """
                endpoint = self.get_endpoint_by_index(endpoint_index)

            elif endpoint_name is not None:
                """
                If the given name of the Qiskrypt's Endpoint related to
                the Qiskrypt's Quantum Register to be removed from the list of
                Qiskrypt's Registers of the Qiskrypt's Party Client is not None.
                """

                """
                Retrieve the Qiskrypt's Endpoint from the list of Qiskrypt's Endpoints of
                the Qiskrypt's Party Client, given the corresponding name.
                """
                endpoint = self.get_endpoint_by_name(endpoint_name)

            if (endpoint.get_context() == POSSIBLE_ENDPOINT_CONTEXTS[0]) and \
               (isinstance(endpoint, QiskryptQuantumGroundStationEndpoint)):
                """
                If the Qiskrypt's Endpoint of the Qiskrypt's Party Client 
                is a Qiskrypt's Quantum Ground Station Endpoint
                and belongs to a Quantum Context.
                """

                for current_register_index in range(super().get_num_registers()):
                    """
                    For each Qiskrypt's Register in the list of
                    Qiskrypt's Registers of the Qiskrypt's Party Client. 
                    """

                    current_register = super().get_registers()[current_register_index]
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

                            super().get_registers().remove(current_register)
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

        else:
            """
            If the given index and name of the Qiskrypt's Endpoint related to
            the Qiskrypt's Quantum Register to be removed from the list of
            Qiskrypt's Registers of the Qiskrypt's Party Client are both None.
            """

            # TODO Throw - Exception

    def remove_quantum_register_by_index(self, quantum_register_index: int,
                                         endpoint_index=None, endpoint_name=None):
        """
        Removes a Qiskrypt's Quantum Register from
        the list of Qiskrypt's Registers of the Qiskrypt's Party Client,
        given its index, regarding the given index or name of a Qiskrypt's Endpoint.

        :param quantum_register_index: the index of a Qiskrypt's Quantum Register to be removed
                                       from the list of Qiskrypt's Registers of
                                       the Qiskrypt's Party Client.
        :param endpoint_index: the index of the Qiskrypt's Endpoint related to
                               the Qiskrypt's Quantum Register to be removed
                               from the list of Qiskrypt's Registers of
                               the Qiskrypt's Party Client.
        :param endpoint_name: the name of the Qiskrypt's Endpoint related to
                              the Qiskrypt's Quantum Register to be removed
                              from the list of Qiskrypt's Registers of
                              the Qiskrypt's Party Client.
        """

        if (endpoint_index is not None) or (endpoint_name is not None):
            """
            If the given index or name of the Qiskrypt's Endpoint related to
            the Qiskrypt's Quantum Register to be removed from the list of
            Qiskrypt's Registers of the Qiskrypt's Party Client is not None.
            """

            endpoint = None
            """
            Initialise the local variable to keep the Qiskrypt's Endpoint related to
            the Qiskrypt's Quantum Register to be removed from the list of
            Qiskrypt's Registers of the Qiskrypt's Party Client, initially, as None.
            """

            if endpoint_index is not None:
                """
                If the given index of the Qiskrypt's Endpoint related to
                the Qiskrypt's Quantum Register to be removed from the list of
                Qiskrypt's Registers of the Qiskrypt's Party Client is not None.
                """

                """
                Retrieve the Qiskrypt's Endpoint from the list of Qiskrypt's Endpoints of
                the Qiskrypt's Party Client, given the corresponding index.
                """
                endpoint = self.get_endpoint_by_index(endpoint_index)

            elif endpoint_name is not None:
                """
                If the given name of the Qiskrypt's Endpoint related to
                the Qiskrypt's Quantum Register to be removed from the list of
                Qiskrypt's Registers of the Qiskrypt's Party Client is not None.
                """

                """
                Retrieve the Qiskrypt's Endpoint from the list of Qiskrypt's Endpoints of
                the Qiskrypt's Party Client, given the corresponding name.
                """
                endpoint = self.get_endpoint_by_name(endpoint_name)

            if (endpoint.get_context() == POSSIBLE_ENDPOINT_CONTEXTS[0]) and \
               (isinstance(endpoint, QiskryptQuantumGroundStationEndpoint)):
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

                    current_register = super().get_registers()[quantum_register_index]
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

                        super().get_registers().remove(current_register)
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

        else:
            """
            If the given index and name of the Qiskrypt's Endpoint related to
            the Qiskrypt's Quantum Register to be removed from the list of
            Qiskrypt's Registers of the Qiskrypt's Party Client are both None.
            """

            # TODO Throw - Exception

    def add_ancilla_quantum_register(self, ancilla_quantum_register: QiskryptAncillaQuantumRegister,
                                     endpoint_index=None, endpoint_name=None):
        """
        Adds a given Qiskrypt's Ancilla Quantum Register to
        the list of Qiskrypt's Registers of the Qiskrypt's Party Client,
        regarding the given index or name of a Qiskrypt's Endpoint.

        :param ancilla_quantum_register: the Qiskrypt's Ancilla Quantum Register to be added
                                         to the list of Qiskrypt's Registers of
                                         the Qiskrypt's Party Client.
        :param endpoint_index: the index of the Qiskrypt's Endpoint related to
                               the Qiskrypt's Ancilla Quantum Register to be added
                               to the list of Qiskrypt's Registers of
                               the Qiskrypt's Party Client.
        :param endpoint_name: the name of the Qiskrypt's Endpoint related to
                              the Qiskrypt's Ancilla Quantum Register to be added
                              to the list of Qiskrypt's Registers of
                              the Qiskrypt's Party Client.
        """

        if (endpoint_index is not None) or (endpoint_name is not None):
            """
            If the given index or name of the Qiskrypt's Endpoint related to
            the Qiskrypt's Ancilla Quantum Register to be added to the list of
            Qiskrypt's Registers of the Qiskrypt's Party Client is not None.
            """

            endpoint = None
            """
            Initialise the local variable to keep the Qiskrypt's Endpoint related to
            the Qiskrypt's Ancilla Quantum Register to be added to the list of
            Qiskrypt's Registers of the Qiskrypt's Party Client, initially, as None.
            """

            if endpoint_index is not None:
                """
                If the given index of the Qiskrypt's Endpoint related to
                the Qiskrypt's Ancilla Quantum Register to be added to the list of
                Qiskrypt's Registers of the Qiskrypt's Party Client is not None.
                """

                """
                Retrieve the Qiskrypt's Endpoint from the list of Qiskrypt's Endpoints of
                the Qiskrypt's Party Client, given the corresponding index.
                """
                endpoint = self.get_endpoint_by_index(endpoint_index)

            elif endpoint_name is not None:
                """
                If the given name of the Qiskrypt's Endpoint related to
                the Qiskrypt's Ancilla Quantum Register to be added to the list of
                Qiskrypt's Registers of the Qiskrypt's Party Client is not None.
                """

                """
                Retrieve the Qiskrypt's Endpoint from the list of Qiskrypt's Endpoints of
                the Qiskrypt's Party Client, given the corresponding name.
                """
                endpoint = self.get_endpoint_by_name(endpoint_name)

            if (endpoint.get_context() == POSSIBLE_ENDPOINT_CONTEXTS[0]) and \
               (isinstance(endpoint, QiskryptQuantumGroundStationEndpoint)):
                """
                If the Qiskrypt's Endpoint of the Qiskrypt's Party Client 
                is a Qiskrypt's Quantum Ground Station Endpoint
                and belongs to a Quantum Context.
                """

                super().get_registers().append(ancilla_quantum_register)
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

        else:
            """
            If the given index and name of the Qiskrypt's Endpoint related to
            the Qiskrypt's Ancilla Quantum Register to be added to the list of
            Qiskrypt's Registers of the Qiskrypt's Party Client are both None.
            """

            # TODO Throw - Exception

    def remove_ancilla_quantum_register_by_name(self, ancilla_quantum_register_name: str,
                                                endpoint_index=None, endpoint_name=None):
        """
        Removes a Qiskrypt's Ancilla Quantum Register from
        the list of Qiskrypt's Registers of the Qiskrypt's Party Client,
        given its name, regarding the given index or name of a Qiskrypt's Endpoint.

        :param ancilla_quantum_register_name: the name of a Qiskrypt's Ancilla Quantum Register to be removed
                                              from the list of Qiskrypt's Registers of
                                              the Qiskrypt's Party Client.
        :param endpoint_index: the index of the Qiskrypt's Endpoint related to
                               the Qiskrypt's Ancilla Quantum Register to be removed
                               from the list of Qiskrypt's Registers of
                               the Qiskrypt's Party Client.
        :param endpoint_name: the name of the Qiskrypt's Endpoint related to
                              the Qiskrypt's Ancilla Quantum Register to be removed
                              from the list of Qiskrypt's Registers of
                              the Qiskrypt's Party Client.
        """

        if (endpoint_index is not None) or (endpoint_name is not None):
            """
            If the given index or name of the Qiskrypt's Endpoint related to
            the Qiskrypt's Ancilla Quantum Register to be removed from the list of
            Qiskrypt's Registers of the Qiskrypt's Party Client is not None.
            """

            endpoint = None
            """
            Initialise the local variable to keep the Qiskrypt's Endpoint related to
            the Qiskrypt's Ancilla Quantum Register to be removed from the list of
            Qiskrypt's Registers of the Qiskrypt's Party Client, initially, as None.
            """

            if endpoint_index is not None:
                """
                If the given index of the Qiskrypt's Endpoint related to
                the Qiskrypt's Ancilla Quantum Register to be removed from the list of
                Qiskrypt's Registers of the Qiskrypt's Party Client is not None.
                """

                """
                Retrieve the Qiskrypt's Endpoint from the list of Qiskrypt's Endpoints of
                the Qiskrypt's Party Client, given the corresponding index.
                """
                endpoint = self.get_endpoint_by_index(endpoint_index)

            elif endpoint_name is not None:
                """
                If the given name of the Qiskrypt's Endpoint related to
                the Qiskrypt's Ancilla Quantum Register to be removed from the list of
                Qiskrypt's Registers of the Qiskrypt's Party Client is not None.
                """

                """
                Retrieve the Qiskrypt's Endpoint from the list of Qiskrypt's Endpoints of
                the Qiskrypt's Party Client, given the corresponding name.
                """
                endpoint = self.get_endpoint_by_name(endpoint_name)

            if (endpoint.get_context() == POSSIBLE_ENDPOINT_CONTEXTS[0]) and \
               (isinstance(endpoint, QiskryptQuantumGroundStationEndpoint)):
                """
                If the Qiskrypt's Endpoint of the Qiskrypt's Party Client 
                is a Qiskrypt's Quantum Ground Station Endpoint
                and belongs to a Quantum Context.
                """

                for current_register_index in range(super().get_num_registers()):
                    """
                    For each Qiskrypt's Register in the list of
                    Qiskrypt's Registers of the Qiskrypt's Party Client. 
                    """

                    current_register = super().get_registers()[current_register_index]
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

                            super().get_registers().remove(current_register)
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

        else:
            """
            If the given index and name of the Qiskrypt's Endpoint related to
            the Qiskrypt's Ancilla Quantum Register to be removed from the list of
            Qiskrypt's Registers of the Qiskrypt's Party Client are both None.
            """

            # TODO Throw - Exception

    def remove_ancilla_quantum_register_by_index(self, ancilla_quantum_register_index: int,
                                                 endpoint_index=None, endpoint_name=None):
        """
        Removes a Qiskrypt's Ancilla Quantum Register from
        the list of Qiskrypt's Registers of the Qiskrypt's Party Client,
        given its index, regarding the given index or name of a Qiskrypt's Endpoint.

        :param ancilla_quantum_register_index: the index of a Qiskrypt's Ancilla Quantum Register to be removed
                                               from the list of Qiskrypt's Registers of
                                               the Qiskrypt's Party Client.
        :param endpoint_index: the index of the Qiskrypt's Endpoint related to
                               the Qiskrypt's Quantum Register to be removed
                               from the list of Qiskrypt's Registers of
                               the Qiskrypt's Party Client.
        :param endpoint_name: the name of the Qiskrypt's Endpoint related to
                              the Qiskrypt's Quantum Register to be removed
                              from the list of Qiskrypt's Registers of
                              the Qiskrypt's Party Client.
        """

        if (endpoint_index is not None) or (endpoint_name is not None):
            """
            If the given index or name of the Qiskrypt's Endpoint related to
            the Qiskrypt's Ancilla Quantum Register to be removed from the list of
            Qiskrypt's Registers of the Qiskrypt's Party Client is not None.
            """

            endpoint = None
            """
            Initialise the local variable to keep the Qiskrypt's Endpoint related to
            the Qiskrypt's Ancilla Quantum Register to be removed from the list of
            Qiskrypt's Registers of the Qiskrypt's Party Client, initially, as None.
            """

            if endpoint_index is not None:
                """
                If the given index of the Qiskrypt's Endpoint related to
                the Qiskrypt's Ancilla Quantum Register to be removed from the list of
                Qiskrypt's Registers of the Qiskrypt's Party Client is not None.
                """

                """
                Retrieve the Qiskrypt's Endpoint from the list of Qiskrypt's Endpoints of
                the Qiskrypt's Party Client, given the corresponding index.
                """
                endpoint = self.get_endpoint_by_index(endpoint_index)

            elif endpoint_name is not None:
                """
                If the given name of the Qiskrypt's Endpoint related to
                the Qiskrypt's Ancilla Quantum Register to be removed from the list of
                Qiskrypt's Registers of the Qiskrypt's Party Client is not None.
                """

                """
                Retrieve the Qiskrypt's Endpoint from the list of Qiskrypt's Endpoints of
                the Qiskrypt's Party Client, given the corresponding name.
                """
                endpoint = self.get_endpoint_by_name(endpoint_name)

            if (endpoint.get_context() == POSSIBLE_ENDPOINT_CONTEXTS[0]) and \
               (isinstance(endpoint, QiskryptQuantumGroundStationEndpoint)):
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

                    current_register = super().get_registers()[ancilla_quantum_register_index]
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

                        super().get_registers().remove(current_register)
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

        else:
            """
            If the given index and name of the Qiskrypt's Endpoint related to
            the Qiskrypt's Ancilla Quantum Register to be removed from the list of
            Qiskrypt's Registers of the Qiskrypt's Party Client are both None.
            """

            # TODO Throw - Exception

    def add_fully_quantum_register(self, fully_quantum_register: QiskryptFullyQuantumRegister,
                                   endpoint_index=None, endpoint_name=None):
        """
        Adds a given Qiskrypt's Fully-Quantum Register to
        the list of Qiskrypt's Registers of the Qiskrypt's Party Client,
        given its index, regarding the given index or name of a Qiskrypt's Endpoint.

        :param fully_quantum_register: the Qiskrypt's Fully-Quantum Register to be added
                                       to the list of Qiskrypt's Registers of
                                       the Qiskrypt's Party Client.
        :param endpoint_index: the index of the Qiskrypt's Endpoint related to
                               the Qiskrypt's Fully-Quantum Register to be added
                               to the list of Qiskrypt's Registers of
                               the Qiskrypt's Party Client.
        :param endpoint_name: the name of the Qiskrypt's Endpoint related to
                              the Qiskrypt's Fully-Quantum Register to be added
                              to the list of Qiskrypt's Registers of
                              the Qiskrypt's Party Client.
        """

        if (endpoint_index is not None) or (endpoint_name is not None):
            """
            If the given index or name of the Qiskrypt's Endpoint related to
            the Qiskrypt's Fully-Quantum Register to be added to the list of
            Qiskrypt's Registers of the Qiskrypt's Party Client is not None.
            """

            endpoint = None
            """
            Initialise the local variable to keep the Qiskrypt's Endpoint related to
            the Qiskrypt's Fully-Quantum Register to be added to the list of
            Qiskrypt's Registers of the Qiskrypt's Party Client, initially, as None.
            """

            if endpoint_index is not None:
                """
                If the given index of the Qiskrypt's Endpoint related to
                the Qiskrypt's Fully-Quantum Register to be added to the list of
                Qiskrypt's Registers of the Qiskrypt's Party Client is not None.
                """

                """
                Retrieve the Qiskrypt's Endpoint from the list of Qiskrypt's Endpoints of
                the Qiskrypt's Party Client, given the corresponding index.
                """
                endpoint = self.get_endpoint_by_index(endpoint_index)

            elif endpoint_name is not None:
                """
                If the given name of the Qiskrypt's Endpoint related to
                the Qiskrypt's Fully-Quantum Register to be added to the list of
                Qiskrypt's Registers of the Qiskrypt's Party Client is not None.
                """

                """
                Retrieve the Qiskrypt's Endpoint from the list of Qiskrypt's Endpoints of
                the Qiskrypt's Party Client, given the corresponding name.
                """
                endpoint = self.get_endpoint_by_name(endpoint_name)

            if (endpoint.get_context() == POSSIBLE_ENDPOINT_CONTEXTS[1]) and \
               (isinstance(endpoint, QiskryptFullyQuantumGroundStationEndpoint)):
                """
                If the Qiskrypt's Endpoint of the Qiskrypt's Party Client 
                is a Qiskrypt's Fully-Quantum Ground Station Endpoint
                and belongs to a Fully-Quantum Context.
                """

                super().get_registers().append(fully_quantum_register)
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

        else:
            """
            If the given index and name of the Qiskrypt's Endpoint related to
            the Qiskrypt's Fully-Quantum Register to be added to the list of
            Qiskrypt's Registers of the Qiskrypt's Party Client are both None.
            """

            # TODO Throw - Exception

    def remove_fully_quantum_register_by_name(self, fully_quantum_register_name: str,
                                              endpoint_index=None, endpoint_name=None):
        """
        Removes a Qiskrypt's Fully-Quantum Register from
        the list of Qiskrypt's Registers of the Qiskrypt's Party Client,
        given its name, regarding the given index or name of a Qiskrypt's Endpoint.

        :param fully_quantum_register_name: the name of a Qiskrypt's Fully-Quantum Register to be removed
                                            from the list of Qiskrypt's Registers of
                                            the Qiskrypt's Party Client.
        :param endpoint_index: the index of the Qiskrypt's Endpoint related to
                               the Qiskrypt's Fully-Quantum Register to be removed
                               from the list of Qiskrypt's Registers of
                               the Qiskrypt's Party Client.
        :param endpoint_name: the name of the Qiskrypt's Endpoint related to
                              the Qiskrypt's Fully-Quantum Register to be removed
                              from the list of Qiskrypt's Registers of
                              the Qiskrypt's Party Client.
        """

        if (endpoint_index is not None) or (endpoint_name is not None):
            """
            If the given index or name of the Qiskrypt's Endpoint related to
            the Qiskrypt's Fully-Quantum Register to be removed from the list of
            Qiskrypt's Registers of the Qiskrypt's Party Client is not None.
            """

            endpoint = None
            """
            Initialise the local variable to keep the Qiskrypt's Endpoint related to
            the Qiskrypt's Fully-Quantum Register to be removed from the list of
            Qiskrypt's Registers of the Qiskrypt's Party Client, initially, as None.
            """

            if endpoint_index is not None:
                """
                If the given index of the Qiskrypt's Endpoint related to
                the Qiskrypt's Fully-Quantum Register to be removed from the list of
                Qiskrypt's Registers of the Qiskrypt's Party Client is not None.
                """

                """
                Retrieve the Qiskrypt's Endpoint from the list of Qiskrypt's Endpoints of
                the Qiskrypt's Party Client, given the corresponding index.
                """
                endpoint = self.get_endpoint_by_index(endpoint_index)

            elif endpoint_name is not None:
                """
                If the given name of the Qiskrypt's Endpoint related to
                the Qiskrypt's Fully-Quantum Register to be removed from the list of
                Qiskrypt's Registers of the Qiskrypt's Party Client is not None.
                """

                """
                Retrieve the Qiskrypt's Endpoint from the list of Qiskrypt's Endpoints of
                the Qiskrypt's Party Client, given the corresponding name.
                """
                endpoint = self.get_endpoint_by_name(endpoint_name)

            if (endpoint.get_context() == POSSIBLE_ENDPOINT_CONTEXTS[1]) and \
               (isinstance(endpoint, QiskryptFullyQuantumGroundStationEndpoint)):
                """
                If the Qiskrypt's Endpoint of the Qiskrypt's Party Client 
                is a Qiskrypt's Fully-Quantum Ground Station Endpoint
                and belongs to a Fully-Quantum Context.
                """

                for current_register_index in range(super().get_num_registers()):
                    """
                    For each Qiskrypt's Register in the list of
                    Qiskrypt's Registers of the Qiskrypt's Party Client. 
                    """

                    current_register = super().get_registers()[current_register_index]
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

                            super().get_registers().remove(current_register)
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

        else:
            """
            If the given index and name of the Qiskrypt's Endpoint related to
            the Qiskrypt's Fully-Quantum Register to be removed from the list of
            Qiskrypt's Registers of the Qiskrypt's Party Client are both None.
            """

            # TODO Throw - Exception

    def remove_fully_quantum_register_by_index(self, fully_quantum_register_index: int,
                                               endpoint_index=None, endpoint_name=None):
        """
        Removes a Qiskrypt's Fully-Quantum Register from
        the list of Qiskrypt's Registers of the Qiskrypt's Party Client,
        given its index, regarding the given index or name of a Qiskrypt's Endpoint.

        :param fully_quantum_register_index: the index of a Qiskrypt's Fully-Quantum Register to be removed
                                             from the list of Qiskrypt's Registers of
                                             the Qiskrypt's Party Client.
        :param endpoint_index: the index of the Qiskrypt's Endpoint related to
                               the Qiskrypt's Fully-Quantum Register to be removed
                               from the list of Qiskrypt's Registers of
                               the Qiskrypt's Party Client.
        :param endpoint_name: the name of the Qiskrypt's Endpoint related to
                              the Qiskrypt's Fully-Quantum Register to be removed
                              from the list of Qiskrypt's Registers of
                              the Qiskrypt's Party Client.
        """

        if (endpoint_index is not None) or (endpoint_name is not None):
            """
            If the given index or name of the Qiskrypt's Endpoint related to
            the Qiskrypt's Fully-Quantum Register to be removed from the list of
            Qiskrypt's Registers of the Qiskrypt's Party Client is not None.
            """

            endpoint = None
            """
            Initialise the local variable to keep the Qiskrypt's Endpoint related to
            the Qiskrypt's Fully-Quantum Register to be removed from the list of
            Qiskrypt's Registers of the Qiskrypt's Party Client, initially, as None.
            """

            if endpoint_index is not None:
                """
                If the given index of the Qiskrypt's Endpoint related to
                the Qiskrypt's Fully-Quantum Register to be removed from the list of
                Qiskrypt's Registers of the Qiskrypt's Party Client is not None.
                """

                """
                Retrieve the Qiskrypt's Endpoint from the list of Qiskrypt's Endpoints of
                the Qiskrypt's Party Client, given the corresponding index.
                """
                endpoint = self.get_endpoint_by_index(endpoint_index)

            elif endpoint_name is not None:
                """
                If the given name of the Qiskrypt's Endpoint related to
                the Qiskrypt's Fully-Quantum Register to be removed from the list of
                Qiskrypt's Registers of the Qiskrypt's Party Client is not None.
                """

                """
                Retrieve the Qiskrypt's Endpoint from the list of Qiskrypt's Endpoints of
                the Qiskrypt's Party Client, given the corresponding name.
                """
                endpoint = self.get_endpoint_by_name(endpoint_name)

            if (endpoint.get_context() == POSSIBLE_ENDPOINT_CONTEXTS[1]) and \
               (isinstance(endpoint, QiskryptFullyQuantumGroundStationEndpoint)):
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

                    current_register = super().get_registers()[fully_quantum_register_index]
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

                        super().get_registers().remove(current_register)
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

        else:
            """
            If the given index and name of the Qiskrypt's Endpoint related to
            the Qiskrypt's Fully-Quantum Register to be removed from the list of
            Qiskrypt's Registers of the Qiskrypt's Party Client are both None.
            """

            # TODO Throw - Exception

    def add_ancilla_fully_quantum_register(self, ancilla_fully_quantum_register: QiskryptAncillaFullyQuantumRegister,
                                           endpoint_index=None, endpoint_name=None):
        """
        Adds a given Qiskrypt's Ancilla Fully-Quantum Register to
        the list of Qiskrypt's Registers of the Qiskrypt's Party Client,
        regarding the given index or name of a Qiskrypt's Endpoint.

        :param ancilla_fully_quantum_register: the Qiskrypt's Ancilla Fully-Quantum Register to be added
                                               to the list of Qiskrypt's Registers of
                                               the Qiskrypt's Party Client.
        :param endpoint_index: the index of the Qiskrypt's Endpoint related to
                               the Qiskrypt's Ancilla Fully-Quantum Register to be added
                               to the list of Qiskrypt's Registers of
                               the Qiskrypt's Party Client.
        :param endpoint_name: the name of the Qiskrypt's Endpoint related to
                              the Qiskrypt's Ancilla Fully-Quantum Register to be added
                              to the list of Qiskrypt's Registers of
                              the Qiskrypt's Party Client.
        """

        if (endpoint_index is not None) or (endpoint_name is not None):
            """
            If the given index or name of the Qiskrypt's Endpoint related to
            the Qiskrypt's Ancilla Fully-Quantum Register to be added to the list of
            Qiskrypt's Registers of the Qiskrypt's Party Client is not None.
            """

            endpoint = None
            """
            Initialise the local variable to keep the Qiskrypt's Endpoint related to
            the Qiskrypt's Ancilla Fully-Quantum Register to be added to the list of
            Qiskrypt's Registers of the Qiskrypt's Party Client, initially, as None.
            """

            if endpoint_index is not None:
                """
                If the given index of the Qiskrypt's Endpoint related to
                the Qiskrypt's Ancilla Fully-Quantum Register to be added to the list of
                Qiskrypt's Registers of the Qiskrypt's Party Client is not None.
                """

                """
                Retrieve the Qiskrypt's Endpoint from the list of Qiskrypt's Endpoints of
                the Qiskrypt's Party Client, given the corresponding index.
                """
                endpoint = self.get_endpoint_by_index(endpoint_index)

            elif endpoint_name is not None:
                """
                If the given name of the Qiskrypt's Endpoint related to
                the Qiskrypt's Ancilla Fully-Quantum Register to be added to the list of
                Qiskrypt's Registers of the Qiskrypt's Party Client is not None.
                """

                """
                Retrieve the Qiskrypt's Endpoint from the list of Qiskrypt's Endpoints of
                the Qiskrypt's Party Client, given the corresponding name.
                """
                endpoint = self.get_endpoint_by_name(endpoint_name)

            if (endpoint.get_context() == POSSIBLE_ENDPOINT_CONTEXTS[1]) and \
               (isinstance(endpoint, QiskryptFullyQuantumGroundStationEndpoint)):
                """
                If the Qiskrypt's Endpoint of the Qiskrypt's Party Client 
                is a Qiskrypt's Fully-Quantum Ground Station Endpoint
                and belongs to a Fully-Quantum Context.
                """

                super().get_registers().append(ancilla_fully_quantum_register)
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

        else:
            """
            If the given index and name of the Qiskrypt's Endpoint related to
            the Qiskrypt's Ancilla Fully-Quantum Register to be added to the list of
            Qiskrypt's Registers of the Qiskrypt's Party Client are both None.
            """

            # TODO Throw - Exception

    def remove_ancilla_fully_quantum_register_by_name(self, ancilla_fully_quantum_register_name: str,
                                                      endpoint_index=None, endpoint_name=None):
        """
        Removes a Qiskrypt's Ancilla Fully-Quantum Register from
        the list of Qiskrypt's Registers of the Qiskrypt's Party Client,
        given its name, regarding the given index or name of a Qiskrypt's Endpoint.

        :param ancilla_fully_quantum_register_name: the name of a Qiskrypt's Ancilla Fully-Quantum Register
                                                    to be removed from the list of Qiskrypt's Registers of
                                                    the Qiskrypt's Party Client.
        :param endpoint_index: the index of the Qiskrypt's Endpoint related to
                               the Qiskrypt's Ancilla Fully-Quantum Register to be removed
                               from the list of Qiskrypt's Registers of
                               the Qiskrypt's Party Client.
        :param endpoint_name: the name of the Qiskrypt's Endpoint related to
                              the Qiskrypt's Ancilla Fully-Quantum Register to be removed
                              from the list of Qiskrypt's Registers of
                              the Qiskrypt's Party Client.
        """

        if (endpoint_index is not None) or (endpoint_name is not None):
            """
            If the given index or name of the Qiskrypt's Endpoint related to
            the Qiskrypt's Ancilla Fully-Quantum Register to be removed from the list of
            Qiskrypt's Registers of the Qiskrypt's Party Client is not None.
            """

            endpoint = None
            """
            Initialise the local variable to keep the Qiskrypt's Endpoint related to
            the Qiskrypt's Ancilla Fully-Quantum Register to be removed from the list of
            Qiskrypt's Registers of the Qiskrypt's Party Client, initially, as None.
            """

            if endpoint_index is not None:
                """
                If the given index of the Qiskrypt's Endpoint related to
                the Qiskrypt's Ancilla Fully-Quantum Register to be removed from the list of
                Qiskrypt's Registers of the Qiskrypt's Party Client is not None.
                """

                """
                Retrieve the Qiskrypt's Endpoint from the list of Qiskrypt's Endpoints of
                the Qiskrypt's Party Client, given the corresponding index.
                """
                endpoint = self.get_endpoint_by_index(endpoint_index)

            elif endpoint_name is not None:
                """
                If the given name of the Qiskrypt's Endpoint related to
                the Qiskrypt's Ancilla Fully-Quantum Register to be removed from the list of
                Qiskrypt's Registers of the Qiskrypt's Party Client is not None.
                """

                """
                Retrieve the Qiskrypt's Endpoint from the list of Qiskrypt's Endpoints of
                the Qiskrypt's Party Client, given the corresponding name.
                """
                endpoint = self.get_endpoint_by_name(endpoint_name)

            if (endpoint.get_context() == POSSIBLE_ENDPOINT_CONTEXTS[1]) and \
               (isinstance(endpoint, QiskryptFullyQuantumGroundStationEndpoint)):
                """
                If the Qiskrypt's Endpoint of the Qiskrypt's Party Client 
                is a Qiskrypt's Fully-Quantum Ground Station Endpoint
                and belongs to a Fully-Quantum Context.
                """

                for current_register_index in range(super().get_num_registers()):
                    """
                    For each Qiskrypt's Register in the list of
                    Qiskrypt's Registers of the Qiskrypt's Party Client. 
                    """

                    current_register = super().get_registers()[current_register_index]
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

                            super().get_registers().remove(current_register)
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

        else:
            """
            If the given index and name of the Qiskrypt's Endpoint related to
            the Qiskrypt's Ancilla Fully-Quantum Register to be removed from the list of
            Qiskrypt's Registers of the Qiskrypt's Party Client are both None.
            """

            # TODO Throw - Exception

    def remove_ancilla_fully_quantum_register_by_index(self, ancilla_fully_quantum_register_index: int,
                                                       endpoint_index=None, endpoint_name=None):
        """
        Removes a Qiskrypt's Ancilla Fully-Quantum Register from
        the list of Qiskrypt's Registers of the Qiskrypt's Party Client,
        given its index, regarding the given index or name of a Qiskrypt's Endpoint.

        :param ancilla_fully_quantum_register_index: the index of a Qiskrypt's Ancilla Fully-Quantum Register
                                                     to be removed from the list of Qiskrypt's Registers of
                                                     the Qiskrypt's Party Client.
        :param endpoint_index: the index of the Qiskrypt's Endpoint related to
                               the Qiskrypt's Ancilla Fully-Quantum Register to be removed
                               from the list of Qiskrypt's Registers of
                               the Qiskrypt's Party Client.
        :param endpoint_name: the name of the Qiskrypt's Endpoint related to
                              the Qiskrypt's Ancilla Fully-Quantum Register to be removed
                              from the list of Qiskrypt's Registers of
                              the Qiskrypt's Party Client.
        """

        if (endpoint_index is not None) or (endpoint_name is not None):
            """
            If the given index or name of the Qiskrypt's Endpoint related to
            the Qiskrypt's Ancilla Fully-Quantum Register to be removed from the list of
            Qiskrypt's Registers of the Qiskrypt's Party Client is not None.
            """

            endpoint = None
            """
            Initialise the local variable to keep the Qiskrypt's Endpoint related to
            the Qiskrypt's Ancilla Fully-Quantum Register to be removed from the list of
            Qiskrypt's Registers of the Qiskrypt's Party Client, initially, as None.
            """

            if endpoint_index is not None:
                """
                If the given index of the Qiskrypt's Endpoint related to
                the Qiskrypt's Ancilla Fully-Quantum Register to be removed from the list of
                Qiskrypt's Registers of the Qiskrypt's Party Client is not None.
                """

                """
                Retrieve the Qiskrypt's Endpoint from the list of Qiskrypt's Endpoints of
                the Qiskrypt's Party Client, given the corresponding index.
                """
                endpoint = self.get_endpoint_by_index(endpoint_index)

            elif endpoint_name is not None:
                """
                If the given name of the Qiskrypt's Endpoint related to
                the Qiskrypt's Ancilla Fully-Quantum Register to be removed from the list of
                Qiskrypt's Registers of the Qiskrypt's Party Client is not None.
                """

                """
                Retrieve the Qiskrypt's Endpoint from the list of Qiskrypt's Endpoints of
                the Qiskrypt's Party Client, given the corresponding name.
                """
                endpoint = self.get_endpoint_by_name(endpoint_name)

            if (endpoint.get_context() == POSSIBLE_ENDPOINT_CONTEXTS[1]) and \
               (isinstance(endpoint, QiskryptFullyQuantumGroundStationEndpoint)):
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

                    current_register = super().get_registers()[ancilla_fully_quantum_register_index]
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

                        super().get_registers().remove(current_register)
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

        else:
            """
            If the given index and name of the Qiskrypt's Endpoint related to
            the Qiskrypt's Ancilla Fully-Quantum Register to be removed from the list of
            Qiskrypt's Registers of the Qiskrypt's Party Client are both None.
            """

            # TODO Throw - Exception

    def add_semi_quantum_register(self, semi_quantum_register: QiskryptSemiQuantumRegister,
                                  endpoint_index=None, endpoint_name=None):
        """
        Adds a given Qiskrypt's Semi-Quantum Register to
        the list of Qiskrypt's Registers of the Qiskrypt's Party Client,
        given its index, regarding the given index or name of a Qiskrypt's Endpoint.

        :param semi_quantum_register: the Qiskrypt's Semi-Quantum Register to be added
                                      to the list of Qiskrypt's Registers of
                                      the Qiskrypt's Party Client.
        :param endpoint_index: the index of the Qiskrypt's Endpoint related to
                               the Qiskrypt's Semi-Quantum Register to be added
                               to the list of Qiskrypt's Registers of
                               the Qiskrypt's Party Client.
        :param endpoint_name: the name of the Qiskrypt's Endpoint related to
                              the Qiskrypt's Semi-Quantum Register to be added
                              to the list of Qiskrypt's Registers of
                              the Qiskrypt's Party Client.
        """

        if (endpoint_index is not None) or (endpoint_name is not None):
            """
            If the given index or name of the Qiskrypt's Endpoint related to
            the Qiskrypt's Semi-Quantum Register to be added to the list of
            Qiskrypt's Registers of the Qiskrypt's Party Client is not None.
            """

            endpoint = None
            """
            Initialise the local variable to keep the Qiskrypt's Endpoint related to
            the Qiskrypt's Semi-Quantum Register to be added to the list of
            Qiskrypt's Registers of the Qiskrypt's Party Client, initially, as None.
            """

            if endpoint_index is not None:
                """
                If the given index of the Qiskrypt's Endpoint related to
                the Qiskrypt's Semi-Quantum Register to be added to the list of
                Qiskrypt's Registers of the Qiskrypt's Party Client is not None.
                """

                """
                Retrieve the Qiskrypt's Endpoint from the list of Qiskrypt's Endpoints of
                the Qiskrypt's Party Client, given the corresponding index.
                """
                endpoint = self.get_endpoint_by_index(endpoint_index)

            elif endpoint_name is not None:
                """
                If the given name of the Qiskrypt's Endpoint related to
                the Qiskrypt's Semi-Quantum Register to be added to the list of
                Qiskrypt's Registers of the Qiskrypt's Party Client is not None.
                """

                """
                Retrieve the Qiskrypt's Endpoint from the list of Qiskrypt's Endpoints of
                the Qiskrypt's Party Client, given the corresponding name.
                """
                endpoint = self.get_endpoint_by_name(endpoint_name)

            if (endpoint.get_context() == POSSIBLE_ENDPOINT_CONTEXTS[2]) and \
               (isinstance(endpoint, QiskryptSemiQuantumGroundStationEndpoint)):
                """
                If the Qiskrypt's Endpoint of the Qiskrypt's Party Client 
                is a Qiskrypt's Semi-Quantum Ground Station Endpoint
                and belongs to a Semi-Quantum Context.
                """

                super().get_registers().append(semi_quantum_register)
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

        else:
            """
            If the given index and name of the Qiskrypt's Endpoint related to
            the Qiskrypt's Semi-Quantum Register to be added to the list of
            Qiskrypt's Registers of the Qiskrypt's Party Client are both None.
            """

            # TODO Throw - Exception

    def remove_semi_quantum_register_by_name(self, semi_quantum_register_name: str,
                                             endpoint_index=None, endpoint_name=None):
        """
        Removes a Qiskrypt's Semi-Quantum Register from
        the list of Qiskrypt's Registers of the Qiskrypt's Party Client,
        given its name, regarding the given index or name of a Qiskrypt's Endpoint.

        :param semi_quantum_register_name: the name of a Qiskrypt's Semi-Quantum Register
                                           to be removed from the list of Qiskrypt's Registers of
                                           the Qiskrypt's Party Client.
        :param endpoint_index: the index of the Qiskrypt's Endpoint related to
                               the Qiskrypt's Semi-Quantum Register to be removed
                               from the list of Qiskrypt's Registers of
                               the Qiskrypt's Party Client.
        :param endpoint_name: the name of the Qiskrypt's Endpoint related to
                              the Qiskrypt's Semi-Quantum Register to be removed
                              from the list of Qiskrypt's Registers of
                              the Qiskrypt's Party Client.
        """

        if (endpoint_index is not None) or (endpoint_name is not None):
            """
            If the given index or name of the Qiskrypt's Endpoint related to
            the Qiskrypt's Semi-Quantum Register to be removed from the list of
            Qiskrypt's Registers of the Qiskrypt's Party Client is not None.
            """

            endpoint = None
            """
            Initialise the local variable to keep the Qiskrypt's Endpoint related to
            the Qiskrypt's Semi-Quantum Register to be removed from the list of
            Qiskrypt's Registers of the Qiskrypt's Party Client, initially, as None.
            """

            if endpoint_index is not None:
                """
                If the given index of the Qiskrypt's Endpoint related to
                the Qiskrypt's Semi-Quantum Register to be removed from the list of
                Qiskrypt's Registers of the Qiskrypt's Party Client is not None.
                """

                """
                Retrieve the Qiskrypt's Endpoint from the list of Qiskrypt's Endpoints of
                the Qiskrypt's Party Client, given the corresponding index.
                """
                endpoint = self.get_endpoint_by_index(endpoint_index)

            elif endpoint_name is not None:
                """
                If the given name of the Qiskrypt's Endpoint related to
                the Qiskrypt's Semi-Quantum Register to be removed from the list of
                Qiskrypt's Registers of the Qiskrypt's Party Client is not None.
                """

                """
                Retrieve the Qiskrypt's Endpoint from the list of Qiskrypt's Endpoints of
                the Qiskrypt's Party Client, given the corresponding name.
                """
                endpoint = self.get_endpoint_by_name(endpoint_name)

            if (endpoint.get_context() == POSSIBLE_ENDPOINT_CONTEXTS[2]) and \
               (isinstance(endpoint, QiskryptSemiQuantumGroundStationEndpoint)):
                """
                If the Qiskrypt's Endpoint of the Qiskrypt's Party Client 
                is a Qiskrypt's Semi-Quantum Ground Station Endpoint
                and belongs to a Semi-Quantum Context.
                """

                for current_register_index in range(super().get_num_registers()):
                    """
                    For each Qiskrypt's Register in the list of
                    Qiskrypt's Registers of the Qiskrypt's Party Client. 
                    """

                    current_register = super().get_registers()[current_register_index]
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

                            super().get_registers().remove(current_register)
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

        else:
            """
            If the given index and name of the Qiskrypt's Endpoint related to
            the Qiskrypt's Semi-Quantum Register to be removed from the list of
            Qiskrypt's Registers of the Qiskrypt's Party Client are both None.
            """

            # TODO Throw - Exception

    def remove_semi_quantum_register_by_index(self, semi_quantum_register_index: int,
                                              endpoint_index=None, endpoint_name=None):
        """
        Removes a Qiskrypt's Semi-Quantum Register from
        the list of Qiskrypt's Registers of the Qiskrypt's Party Client,
        given its index, regarding the given index or name of a Qiskrypt's Endpoint.

        :param semi_quantum_register_index: the index of a Qiskrypt's Semi-Quantum Register
                                            to be removed from the list of Qiskrypt's Registers of
                                            the Qiskrypt's Party Client.
        :param endpoint_index: the index of the Qiskrypt's Endpoint related to
                               the Qiskrypt's Semi-Quantum Register to be removed
                               from the list of Qiskrypt's Registers of
                               the Qiskrypt's Party Client.
        :param endpoint_name: the name of the Qiskrypt's Endpoint related to
                              the Qiskrypt's Semi-Quantum Register to be removed
                              from the list of Qiskrypt's Registers of
                              the Qiskrypt's Party Client.
        """

        if (endpoint_index is not None) or (endpoint_name is not None):
            """
            If the given index or name of the Qiskrypt's Endpoint related to
            the Qiskrypt's Quantum Register to be removed from the list of
            Qiskrypt's Registers of the Qiskrypt's Party Client is not None.
            """

            endpoint = None
            """
            Initialise the local variable to keep the Qiskrypt's Endpoint related to
            the Qiskrypt's Quantum Register to be removed from the list of
            Qiskrypt's Registers of the Qiskrypt's Party Client, initially, as None.
            """

            if endpoint_index is not None:
                """
                If the given index of the Qiskrypt's Endpoint related to
                the Qiskrypt's Quantum Register to be removed from the list of
                Qiskrypt's Registers of the Qiskrypt's Party Client is not None.
                """

                """
                Retrieve the Qiskrypt's Endpoint from the list of Qiskrypt's Endpoints of
                the Qiskrypt's Party Client, given the corresponding index.
                """
                endpoint = self.get_endpoint_by_index(endpoint_index)

            elif endpoint_name is not None:
                """
                If the given name of the Qiskrypt's Endpoint related to
                the Qiskrypt's Quantum Register to be removed from the list of
                Qiskrypt's Registers of the Qiskrypt's Party Client is not None.
                """

                """
                Retrieve the Qiskrypt's Endpoint from the list of Qiskrypt's Endpoints of
                the Qiskrypt's Party Client, given the corresponding name.
                """
                endpoint = self.get_endpoint_by_name(endpoint_name)

            if (endpoint.get_context() == POSSIBLE_ENDPOINT_CONTEXTS[2]) and \
               (isinstance(endpoint, QiskryptSemiQuantumGroundStationEndpoint)):
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

                    current_register = super().get_registers()[semi_quantum_register_index]
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

                        super().get_registers().remove(current_register)
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

        else:
            """
            If the given index and name of the Qiskrypt's Endpoint related to
            the Qiskrypt's Semi-Quantum Register to be removed from the list of
            Qiskrypt's Registers of the Qiskrypt's Party Client are both None.
            """

            # TODO Throw - Exception

    def add_ancilla_semi_quantum_register(self, ancilla_semi_quantum_register: QiskryptAncillaSemiQuantumRegister,
                                          endpoint_index=None, endpoint_name=None):
        """
        Adds a given Qiskrypt's Ancilla Semi-Quantum Register to
        the list of Qiskrypt's Registers of the Qiskrypt's Party Client,
        regarding the given index or name of a Qiskrypt's Endpoint.

        :param ancilla_semi_quantum_register: the Qiskrypt's Ancilla Semi-Quantum Register to be added
                                              to the list of Qiskrypt's Registers of
                                              the Qiskrypt's Party Client.
        :param endpoint_index: the index of the Qiskrypt's Endpoint related to
                               the Qiskrypt's Ancilla Semi-Quantum Register to be added
                               to the list of Qiskrypt's Registers of
                               the Qiskrypt's Party Client.
        :param endpoint_name: the name of the Qiskrypt's Endpoint related to
                              the Qiskrypt's Ancilla Semi-Quantum Register to be added
                              to the list of Qiskrypt's Registers of
                              the Qiskrypt's Party Client.
        """

        if (endpoint_index is not None) or (endpoint_name is not None):
            """
            If the given index or name of the Qiskrypt's Endpoint related to
            the Qiskrypt's Ancilla Semi-Quantum Register to be added to the list of
            Qiskrypt's Registers of the Qiskrypt's Party Client is not None.
            """

            endpoint = None
            """
            Initialise the local variable to keep the Qiskrypt's Endpoint related to
            the Qiskrypt's Ancilla Semi-Quantum Register to be added to the list of
            Qiskrypt's Registers of the Qiskrypt's Party Client, initially, as None.
            """

            if endpoint_index is not None:
                """
                If the given index of the Qiskrypt's Endpoint related to
                the Qiskrypt's Ancilla Semi-Quantum Register to be added to the list of
                Qiskrypt's Registers of the Qiskrypt's Party Client is not None.
                """

                """
                Retrieve the Qiskrypt's Endpoint from the list of Qiskrypt's Endpoints of
                the Qiskrypt's Party Client, given the corresponding index.
                """
                endpoint = self.get_endpoint_by_index(endpoint_index)

            elif endpoint_name is not None:
                """
                If the given name of the Qiskrypt's Endpoint related to
                the Qiskrypt's Ancilla Semi-Quantum Register to be added to the list of
                Qiskrypt's Registers of the Qiskrypt's Party Client is not None.
                """

                """
                Retrieve the Qiskrypt's Endpoint from the list of Qiskrypt's Endpoints of
                the Qiskrypt's Party Client, given the corresponding name.
                """
                endpoint = self.get_endpoint_by_name(endpoint_name)

            if (endpoint.get_context() == POSSIBLE_ENDPOINT_CONTEXTS[2]) and \
               (isinstance(endpoint, QiskryptSemiQuantumGroundStationEndpoint)):
                """
                If the Qiskrypt's Endpoint of the Qiskrypt's Party Client 
                is a Qiskrypt's Semi-Quantum Ground Station Endpoint
                and belongs to a Semi-Quantum Context.
                """

                super().get_registers().append(ancilla_semi_quantum_register)
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

        else:
            """
            If the given index and name of the Qiskrypt's Endpoint related to
            the Qiskrypt's Ancilla Semi-Quantum Register to be added to the list of
            Qiskrypt's Registers of the Qiskrypt's Party Client are both None.
            """

            # TODO Throw - Exception

    def remove_ancilla_semi_quantum_register_by_name(self, ancilla_semi_quantum_register_name: str,
                                                     endpoint_index=None, endpoint_name=None):
        """
        Removes a Qiskrypt's Ancilla Semi-Quantum Register from
        the list of Qiskrypt's Registers of the Qiskrypt's Party Client,
        given its name, regarding the given index or name of a Qiskrypt's Endpoint.

        :param ancilla_semi_quantum_register_name: the name of a Qiskrypt's Ancilla Semi-Quantum Register
                                                   to be removed from the list of Qiskrypt's Registers of
                                                   the Qiskrypt's Party Client.
        :param endpoint_index: the index of the Qiskrypt's Endpoint related to
                               the Qiskrypt's Ancilla Semi-Quantum Register to be removed
                               from the list of Qiskrypt's Registers of
                               the Qiskrypt's Party Client.
        :param endpoint_name: the name of the Qiskrypt's Endpoint related to
                              the Qiskrypt's Ancilla Semi-Quantum Register to be removed
                              from the list of Qiskrypt's Registers of
                              the Qiskrypt's Party Client.
        """

        if (endpoint_index is not None) or (endpoint_name is not None):
            """
            If the given index or name of the Qiskrypt's Endpoint related to
            the Qiskrypt's Ancilla Semi-Quantum Register to be removed from the list of
            Qiskrypt's Registers of the Qiskrypt's Party Client is not None.
            """

            endpoint = None
            """
            Initialise the local variable to keep the Qiskrypt's Endpoint related to
            the Qiskrypt's Ancilla Semi-Quantum Register to be removed from the list of
            Qiskrypt's Registers of the Qiskrypt's Party Client, initially, as None.
            """

            if endpoint_index is not None:
                """
                If the given index of the Qiskrypt's Endpoint related to
                the Qiskrypt's Ancilla Semi-Quantum Register to be removed from the list of
                Qiskrypt's Registers of the Qiskrypt's Party Client is not None.
                """

                """
                Retrieve the Qiskrypt's Endpoint from the list of Qiskrypt's Endpoints of
                the Qiskrypt's Party Client, given the corresponding index.
                """
                endpoint = self.get_endpoint_by_index(endpoint_index)

            elif endpoint_name is not None:
                """
                If the given name of the Qiskrypt's Endpoint related to
                the Qiskrypt's Ancilla Semi-Quantum Register to be removed from the list of
                Qiskrypt's Registers of the Qiskrypt's Party Client is not None.
                """

                """
                Retrieve the Qiskrypt's Endpoint from the list of Qiskrypt's Endpoints of
                the Qiskrypt's Party Client, given the corresponding name.
                """
                endpoint = self.get_endpoint_by_name(endpoint_name)

            if (endpoint.get_context() == POSSIBLE_ENDPOINT_CONTEXTS[2]) and \
               (isinstance(endpoint, QiskryptSemiQuantumGroundStationEndpoint)):
                """
                If the Qiskrypt's Endpoint of the Qiskrypt's Party Client 
                is a Qiskrypt's Semi-Quantum Ground Station Endpoint
                and belongs to a Semi-Quantum Context.
                """

                for current_register_index in range(super().get_num_registers()):
                    """
                    For each Qiskrypt's Register in the list of
                    Qiskrypt's Registers of the Qiskrypt's Party Client. 
                    """

                    current_register = super().get_registers()[current_register_index]
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

                            super().get_registers().remove(current_register)
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

        else:
            """
            If the given index and name of the Qiskrypt's Endpoint related to
            the Qiskrypt's Ancilla Semi-Quantum Register to be removed from the list of
            Qiskrypt's Registers of the Qiskrypt's Party Client are both None.
            """

            # TODO Throw - Exception

    def remove_ancilla_semi_quantum_register_by_index(self, ancilla_semi_quantum_register_index: int,
                                                      endpoint_index=None, endpoint_name=None):
        """
        Removes a Qiskrypt's Ancilla Semi-Quantum Register from
        the list of Qiskrypt's Registers of the Qiskrypt's Party Client,
        given its index, regarding the given index or name of a Qiskrypt's Endpoint.

        :param ancilla_semi_quantum_register_index: the index of a Qiskrypt's Ancilla Semi-Quantum Register
                                                    to be removed from the list of Qiskrypt's Registers of
                                                    the Qiskrypt's Party Client.
        :param endpoint_index: the index of the Qiskrypt's Endpoint related to
                               the Qiskrypt's Ancilla Semi-Quantum Register to be removed
                               from the list of Qiskrypt's Registers of
                               the Qiskrypt's Party Client.
        :param endpoint_name: the name of the Qiskrypt's Endpoint related to
                              the Qiskrypt's Ancilla Semi-Quantum Register to be removed
                              from the list of Qiskrypt's Registers of
                              the Qiskrypt's Party Client.
        """

        if (endpoint_index is not None) or (endpoint_name is not None):
            """
            If the given index or name of the Qiskrypt's Endpoint related to
            the Qiskrypt's Ancilla Semi-Quantum Register to be removed from the list of
            Qiskrypt's Registers of the Qiskrypt's Party Client is not None.
            """

            endpoint = None
            """
            Initialise the local variable to keep the Qiskrypt's Endpoint related to
            the Qiskrypt's Ancilla Semi-Quantum Register to be removed from the list of
            Qiskrypt's Registers of the Qiskrypt's Party Client, initially, as None.
            """

            if endpoint_index is not None:
                """
                If the given index of the Qiskrypt's Endpoint related to
                the Qiskrypt's Ancilla Semi-Quantum Register to be removed from the list of
                Qiskrypt's Registers of the Qiskrypt's Party Client is not None.
                """

                """
                Retrieve the Qiskrypt's Endpoint from the list of Qiskrypt's Endpoints of
                the Qiskrypt's Party Client, given the corresponding index.
                """
                endpoint = self.get_endpoint_by_index(endpoint_index)

            elif endpoint_name is not None:
                """
                If the given name of the Qiskrypt's Endpoint related to
                the Qiskrypt's Ancilla Semi-Quantum Register to be removed from the list of
                Qiskrypt's Registers of the Qiskrypt's Party Client is not None.
                """

                """
                Retrieve the Qiskrypt's Endpoint from the list of Qiskrypt's Endpoints of
                the Qiskrypt's Party Client, given the corresponding name.
                """
                endpoint = self.get_endpoint_by_name(endpoint_name)

            if (endpoint.get_context() == POSSIBLE_ENDPOINT_CONTEXTS[2]) and \
               (isinstance(endpoint, QiskryptSemiQuantumGroundStationEndpoint)):
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

                    current_register = super().get_registers()[ancilla_semi_quantum_register_index]
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

                        super().get_registers().remove(current_register)
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

        else:
            """
            If the given index and name of the Qiskrypt's Endpoint related to
            the Qiskrypt's Ancilla Semi-Quantum Register to be removed from the list of
            Qiskrypt's Registers of the Qiskrypt's Party Client are both None.
            """

            # TODO Throw - Exception

    def add_classical_register(self, classical_register: QiskryptClassicalRegister,
                               endpoint_index=None, endpoint_name=None):
        """
        Adds a given Qiskrypt's Classical Register to
        the list of Qiskrypt's Registers of the Qiskrypt's Party Client,
        regarding the given index or name of a Qiskrypt's Endpoint.

        :param classical_register: the Qiskrypt's Classical Register to be added
                                   to the list of Qiskrypt's Registers of
                                   the Qiskrypt's Party Client.
        :param endpoint_index: the index of the Qiskrypt's Endpoint related to
                               the Qiskrypt's Classical Register to be added
                               to the list of Qiskrypt's Registers of
                               the Qiskrypt's Party Client.
        :param endpoint_name: the name of the Qiskrypt's Endpoint related to
                              the Qiskrypt's Classical Register to be added
                              to the list of Qiskrypt's Registers of
                              the Qiskrypt's Party Client.
        """

        if (endpoint_index is not None) or (endpoint_name is not None):
            """
            If the given index or name of the Qiskrypt's Endpoint related to
            the Qiskrypt's Classical Register to be added to the list of
            Qiskrypt's Registers of the Qiskrypt's Party Client is not None.
            """

            endpoint = None
            """
            Initialise the local variable to keep the Qiskrypt's Endpoint related to
            the Qiskrypt's Classical Register to be added to the list of
            Qiskrypt's Registers of the Qiskrypt's Party Client, initially, as None.
            """

            if endpoint_index is not None:
                """
                If the given index of the Qiskrypt's Endpoint related to
                the Qiskrypt's Classical Register to be added to the list of
                Qiskrypt's Registers of the Qiskrypt's Party Client is not None.
                """

                """
                Retrieve the Qiskrypt's Endpoint from the list of Qiskrypt's Endpoints of
                the Qiskrypt's Party Client, given the corresponding index.
                """
                endpoint = self.get_endpoint_by_index(endpoint_index)

            elif endpoint_name is not None:
                """
                If the given name of the Qiskrypt's Endpoint related to
                the Qiskrypt's Classical Register to be added to the list of
                Qiskrypt's Registers of the Qiskrypt's Party Client is not None.
                """

                """
                Retrieve the Qiskrypt's Endpoint from the list of Qiskrypt's Endpoints of
                the Qiskrypt's Party Client, given the corresponding name.
                """
                endpoint = self.get_endpoint_by_name(endpoint_name)

            if (endpoint.get_context() == POSSIBLE_ENDPOINT_CONTEXTS[3]) and \
               (isinstance(endpoint, QiskryptClassicalGroundStationEndpoint)):
                """
                If the Qiskrypt's Endpoint of the Qiskrypt's Party Client 
                is a Qiskrypt's Classical Ground Station Endpoint
                and belongs to a Classical Context.
                """

                super().get_registers().append(classical_register)
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

        else:
            """
            If the given index and name of the Qiskrypt's Endpoint related to
            the Qiskrypt's Classical Register to be added to the list of
            Qiskrypt's Registers of the Qiskrypt's Party Client are both None.
            """

            # TODO Throw - Exception

    def remove_classical_register_by_name(self, classical_register_name: str,
                                          endpoint_index=None, endpoint_name=None):
        """
        Removes a Qiskrypt's Classical Register from
        the list of Qiskrypt's Registers of the Qiskrypt's Party Client,
        given its name, regarding the given index or name of a Qiskrypt's Endpoint.

        :param classical_register_name: the name of a Qiskrypt's Classical Register
                                        to be removed from the list of Qiskrypt's Registers of
                                        the Qiskrypt's Party Client.
        :param endpoint_index: the index of the Qiskrypt's Endpoint related to
                               the Qiskrypt's Classical Register to be added
                               to the list of Qiskrypt's Registers of
                               the Qiskrypt's Party Client.
        :param endpoint_name: the name of the Qiskrypt's Endpoint related to
                              the Qiskrypt's Classical Register to be added
                              to the list of Qiskrypt's Registers of
                              the Qiskrypt's Party Client.
        """

        if (endpoint_index is not None) or (endpoint_name is not None):
            """
            If the given index or name of the Qiskrypt's Endpoint related to
            the Qiskrypt's Classical Register to be added to the list of
            Qiskrypt's Registers of the Qiskrypt's Party Client is not None.
            """

            endpoint = None
            """
            Initialise the local variable to keep the Qiskrypt's Endpoint related to
            the Qiskrypt's Classical Register to be added to the list of
            Qiskrypt's Registers of the Qiskrypt's Party Client, initially, as None.
            """

            if endpoint_index is not None:
                """
                If the given index of the Qiskrypt's Endpoint related to
                the Qiskrypt's Classical Register to be added to the list of
                Qiskrypt's Registers of the Qiskrypt's Party Client is not None.
                """

                """
                Retrieve the Qiskrypt's Endpoint from the list of Qiskrypt's Endpoints of
                the Qiskrypt's Party Client, given the corresponding index.
                """
                endpoint = self.get_endpoint_by_index(endpoint_index)

            elif endpoint_name is not None:
                """
                If the given name of the Qiskrypt's Endpoint related to
                the Qiskrypt's Classical Register to be added to the list of
                Qiskrypt's Registers of the Qiskrypt's Party Client is not None.
                """

                """
                Retrieve the Qiskrypt's Endpoint from the list of Qiskrypt's Endpoints of
                the Qiskrypt's Party Client, given the corresponding name.
                """
                endpoint = self.get_endpoint_by_name(endpoint_name)

            if (endpoint.get_context() == POSSIBLE_ENDPOINT_CONTEXTS[3]) and \
               (isinstance(endpoint, QiskryptClassicalGroundStationEndpoint)):
                """
                If the Qiskrypt's Endpoint of the Qiskrypt's Party Client 
                is a Qiskrypt's Classical Ground Station Endpoint
                and belongs to a Classical Context.
                """

                for current_register_index in range(super().get_num_registers()):
                    """
                    For each Qiskrypt's Register in the list of
                    Qiskrypt's Registers of the Qiskrypt's Party Client. 
                    """

                    current_register = super().get_registers()[current_register_index]
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

                            super().get_registers().remove(current_register)
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

        else:
            """
            If the given index and name of the Qiskrypt's Endpoint related to
            the Qiskrypt's Classical Register to be added to the list of
            Qiskrypt's Registers of the Qiskrypt's Party Client are both None.
            """

            # TODO Throw - Exception

    def remove_classical_register_by_index(self, classical_register_index: int,
                                           endpoint_index=None, endpoint_name=None):
        """
        Removes a Qiskrypt's Classical Register from
        the list of Qiskrypt's Registers of the Qiskrypt's Party Client,
        given its index, regarding the given index or name of a Qiskrypt's Endpoint.

        :param classical_register_index: the index of a Qiskrypt's Ancilla Semi-Quantum Register
                                         to be removed from the list of Qiskrypt's Registers of
                                         the Qiskrypt's Party Client.
        :param endpoint_index: the index of the Qiskrypt's Endpoint related to
                               the Qiskrypt's Classical Register to be removed
                               from the list of Qiskrypt's Registers of
                               the Qiskrypt's Party Client.
        :param endpoint_name: the name of the Qiskrypt's Endpoint related to
                              the Qiskrypt's Classical Register to be removed
                              from the list of Qiskrypt's Registers of
                              the Qiskrypt's Party Client.
        """

        if (endpoint_index is not None) or (endpoint_name is not None):
            """
            If the given index or name of the Qiskrypt's Endpoint related to
            the Qiskrypt's Classical Register to be removed from the list of
            Qiskrypt's Registers of the Qiskrypt's Party Client is not None.
            """

            endpoint = None
            """
            Initialise the local variable to keep the Qiskrypt's Endpoint related to
            the Qiskrypt's Classical Register to be removed from the list of
            Qiskrypt's Registers of the Qiskrypt's Party Client, initially, as None.
            """

            if endpoint_index is not None:
                """
                If the given index of the Qiskrypt's Endpoint related to
                the Qiskrypt's Classical Register to be removed from the list of
                Qiskrypt's Registers of the Qiskrypt's Party Client is not None.
                """

                """
                Retrieve the Qiskrypt's Endpoint from the list of Qiskrypt's Endpoints of
                the Qiskrypt's Party Client, given the corresponding index.
                """
                endpoint = self.get_endpoint_by_index(endpoint_index)

            elif endpoint_name is not None:
                """
                If the given name of the Qiskrypt's Endpoint related to
                the Qiskrypt's Classical Register to be removed from the list of
                Qiskrypt's Registers of the Qiskrypt's Party Client is not None.
                """

                """
                Retrieve the Qiskrypt's Endpoint from the list of Qiskrypt's Endpoints of
                the Qiskrypt's Party Client, given the corresponding name.
                """
                endpoint = self.get_endpoint_by_name(endpoint_name)

            if (endpoint.get_context() == POSSIBLE_ENDPOINT_CONTEXTS[3]) and \
               (isinstance(endpoint, QiskryptClassicalGroundStationEndpoint)):
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

                    current_register = super().get_registers()[classical_register_index]
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

                        super().get_registers().remove(current_register)
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

        else:
            """
            If the given index and name of the Qiskrypt's Endpoint related to
            the Qiskrypt's Classical Register to be removed from the list of
            Qiskrypt's Registers of the Qiskrypt's Party Client are both None.
            """

            # TODO Throw - Exception
