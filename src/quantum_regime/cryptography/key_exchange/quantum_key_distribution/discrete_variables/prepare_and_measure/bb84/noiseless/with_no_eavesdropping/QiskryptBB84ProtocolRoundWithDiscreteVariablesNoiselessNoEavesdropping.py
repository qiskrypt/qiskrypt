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
Import required Libraries and Packages.
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

from src.quantum_regime.cryptography.key_exchange.quantum_key_distribution.discrete_variables \
    .prepare_and_measure.bb84.common.QiskryptBB84ProtocolRoundWithDiscreteVariables \
    import QiskryptBB84ProtocolRoundWithDiscreteVariables
"""
Import the Qiskrypt's Quantum Key Distribution (QKD) Round.
"""

from src.quantum_regime.utils.parties_and_agents.quantum.fully_quantum.QiskryptFullyQuantumParty \
    import QiskryptFullyQuantumParty
"""
Import the Qiskrypt's Fully-Quantum Party.
"""

from src.quantum_regime.utils.user_client.QiskryptUserClient \
    import QiskryptUserClient
"""
Import the Qiskrypt's User Client.
"""

from src.quantum_regime.circuit.registers.quantum.fully_quantum.QiskryptFullyQuantumRegister \
    import QiskryptFullyQuantumRegister
"""
Import the Qiskrypt's Fully-Quantum Register.
"""

from src.quantum_regime.circuit.QiskryptQuantumCircuit \
    import QiskryptQuantumCircuit
"""
Import the Qiskrypt's Quantum Circuit.
"""


class QiskryptBB84ProtocolRoundWithDiscreteVariablesForNoiselessScenariosAndNoEavesdropping \
            (QiskryptBB84ProtocolRoundWithDiscreteVariables):
    """
    Object class for the Qiskrypt's BB84 Protocol Round
    with Discrete Variables (DVs) for Noiseless Scenarios and no Eavesdropping.
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
    def create_quantum_circuit_for_bb84_protocol_with_discrete_variables_for_noiseless_scenarios_and_no_eavesdropping():

        user_clients_list = []
        """
        Create an empty list for the Qiskrypt's User Clients for the Qiskrypt's BB84 Protocol Round
        with Discrete Variables (DVs) for Noiseless Scenarios and no Eavesdropping.
        """

        for current_num_party in range(QUANTUM_KEY_DISTRIBUTION_NUM_PARTIES):
            """
            For each respective party for the Qiskrypt's BB84 Protocol Round
            with Discrete Variables (DVs) for Noiseless Scenarios and no Eavesdropping.
            """

            current_fully_quantum_party = \
                QiskryptFullyQuantumParty(current_num_party,
                                          QUANTUM_KEY_DISTRIBUTION_DEFAULT_PARTIES_NAMES[current_num_party])
            """
            Create the Qiskrypt's Fully-Quantum Party for the current party in the Qiskrypt's BB84 Protocol Round
            with Discrete Variables (DVs) for Noiseless Scenarios and no Eavesdropping. 
            """

            current_user_client = QiskryptUserClient(current_fully_quantum_party)
            """
            Create the current Qiskrypt's User Client in the Qiskrypt's BB84 Protocol Round
            with Discrete Variables (DVs) for Noiseless Scenarios and no Eavesdropping. 
            """

            fully_quantum_register_name_for_current_user_client = \
                "fully_qu_reg_{}".format(QUANTUM_KEY_DISTRIBUTION_DEFAULT_PARTIES_NAMES[current_num_party].lower())
            """
            Set the name for the Qiskrypt's Fully-Quantum Register for the current Qiskrypt's User Client.
            """

            fully_quantum_register_for_current_user_client = \
                QiskryptFullyQuantumRegister(name=fully_quantum_register_name_for_current_user_client,
                                             num_qubits=1, qiskit_quantum_register=None)
            """
            Create a Qiskrypt's Fully-Quantum Register for the current Qiskrypt's User Client.
            """

            current_user_client.add_fully_quantum_register(fully_quantum_register_for_current_user_client)
            """
            Add the Qiskrypt's Fully-Quantum Register to the list of Qiskrypt's Registers in
            the possession of the current Qiskrypt's User Client.
            """

            user_clients_list.append(current_user_client)
            """
            Append the current Qiskrypt's User Client to the Qiskrypt's User Clients for
            the Qiskrypt's BB84 Protocol Round with Discrete Variables (DVs) for Noiseless Scenarios
            and no Eavesdropping.
            """

