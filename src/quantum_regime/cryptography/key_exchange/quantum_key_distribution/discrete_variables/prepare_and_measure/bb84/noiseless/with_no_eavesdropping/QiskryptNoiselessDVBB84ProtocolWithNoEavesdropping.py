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

from src.quantum_regime.cryptography.key_exchange.quantum_key_distribution.discrete_variables \
    .prepare_and_measure.bb84.common.QiskryptDVBB84Protocol \
    import QiskryptDVBB84Protocol
"""
Import the Qiskrypt's DV (Discrete Variables) BB84 Protocol.
"""

from src.quantum_regime.cryptography.key_exchange.quantum_key_distribution.QiskryptQuantumKeyDistribution \
    import QUANTUM_KEY_DISTRIBUTION_DEFAULT_PARTIES_NAMES
"""
Import the default parties' names for the Qiskrypt's Quantum Key Distribution (QKD).
"""

from src.classical_regime.utils.geographic.QiskryptGeographicAddressEnumeration \
    import QiskryptGeographicAddressEnumeration
"""
Import the Qiskrypt's Geographic Address Enumeration.
"""

from src.quantum_regime.cryptography.QiskryptQuantumCryptographicPrimitive \
    import POSSIBLE_QUANTUM_CRYPTOGRAPHIC_PRIMITIVE_SCENARIOS
"""
Import the available Quantum Cryptographic Primitive scenarios for
the Qiskrypt's Quantum Cryptographic Primitives.
"""

from src.quantum_regime.cryptography.key_exchange.quantum_key_distribution \
    .discrete_variables.prepare_and_measure.bb84.common.QiskryptDVBB84Protocol \
    import DV_BB84_PROTOCOL_NUM_ROUNDS_FOR_QUANTUM_TRANSMISSION
"""
Import the default number of rounds for the Quantum Transmission of
the Qiskrypt's DV (Discrete Variable) BB84 Protocol.
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

        super().__init__(POSSIBLE_QUANTUM_CRYPTOGRAPHIC_PRIMITIVE_SCENARIOS[0],
                         quantum_key_exchange_protocol_num_rounds_for_quantum_transmission)
        """
        Call of the constructor of the super-class Qiskrypt's DV (Discrete Variable) BB84 Protocol.
        """
