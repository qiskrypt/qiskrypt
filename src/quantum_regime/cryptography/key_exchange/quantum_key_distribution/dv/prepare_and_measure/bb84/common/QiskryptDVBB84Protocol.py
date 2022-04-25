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

from src.quantum_regime.cryptography.key_exchange\
    .quantum_key_distribution.QiskryptQuantumKeyDistribution \
    import QiskryptQuantumKeyDistribution
"""
Import the Qiskrypt's Quantum Key Distribution (QKD).
"""

from src.quantum_regime.cryptography.QiskryptQuantumCryptographicPrimitive \
    import POSSIBLE_QUANTUM_CRYPTOGRAPHIC_PRIMITIVE_SIGNAL_VARIABLE_TYPES
"""
Import the available Quantum Cryptographic Primitive signal variable types for
the Qiskrypt's Quantum Cryptographic Primitives.
"""

from src.quantum_regime.cryptography.QiskryptQuantumCryptographicPrimitive \
    import POSSIBLE_QUANTUM_CRYPTOGRAPHIC_PRIMITIVE_SCENARIOS
"""
Import the available Quantum Cryptographic Primitive scenarios for
the Qiskrypt's Quantum Cryptographic Primitives.
"""

from src.quantum_regime.cryptography.key_exchange.quantum_key_distribution.QiskryptQuantumKeyDistribution \
    import POSSIBLE_QUANTUM_KEY_DISTRIBUTION_TYPES
"""
Import the available Quantum Key Distribution (QKD) types for
the Qiskrypt's Quantum Key Distribution (QKD).
"""

from src.quantum_regime.cryptography.key_exchange.quantum_key_distribution\
    .dv.prepare_and_measure.bb84.common.QiskryptDVBB84ProtocolRound \
    import POSSIBLE_DV_BB84_PROTOCOL_ROUND_TYPES_QUANTUM_TRANSMISSION_PHASE
"""
Import the available DV (Discrete Variables) BB84 Protocol Round types for
the Qiskrypt's DV (Discrete Variables) BB84 Protocol.
"""

"""
Definition of Constants and Enumerations.
"""

DV_BB84_PROTOCOL_NAME = "DV (DISCRETE VARIABLES) BB84 PROTOCOL"
"""
The name of the DV (Discrete Variables) BB84 Protocol.
"""

DV_BB84_PROTOCOL_DEFAULT_NUM_ROUNDS_FOR_QUANTUM_TRANSMISSION_PHASE = 1024
"""
The default number of rounds for the Quantum Transmission Phase of
the Qiskrypt's DV (Discrete Variable) BB84 Protocol.
"""

DV_BB84_PROTOCOL_DEFAULT_FACTOR_FOR_NUM_ROUNDS_OF_PARAMETER_ESTIMATION_SAMPLE = 0.5
"""
The default factor for the number of rounds for the Parameter Estimation Sample of
the Qiskrypt's DV (Discrete Variable) BB84 Protocol.
"""


class QiskryptDVBB84Protocol(QiskryptQuantumKeyDistribution):
    """
    Object class for the Qiskrypt's DV (Discrete Variables) BB84 Protocol.

    Reference(s):
    1) Quantum cryptography: Public key distribution and coin tossing:
       - Authors: Charles Bennet and Gilles Brassard
       - Year: 1984
       - Link: https://arxiv.org/abs/2003.06557v1
    """

    def __init__(self, primitive_scenario: str,
                 num_rounds_for_quantum_transmission_phase=DV_BB84_PROTOCOL_DEFAULT_NUM_ROUNDS_FOR_QUANTUM_TRANSMISSION_PHASE,
                 verbose=True):
        """
        Constructor of the Qiskrypt's DV (Discrete Variables) BB84 Protocol.

        :param primitive_scenario: the scenario of the Qiskrypt's
                                                         Quantum Cryptographic Primitive.
        :param num_rounds_for_quantum_transmission_phase: the number of rounds for the Quantum Transmission Phase in
                                                          the Qiskrypt's Quantum Key Exchange Protocol.
        :param verbose: the boolean flag to show the runtime information about
                        the Qiskrypt's Quantum Cryptographic Primitive.
        """

        if primitive_scenario in POSSIBLE_QUANTUM_CRYPTOGRAPHIC_PRIMITIVE_SCENARIOS:
            """
            If the scenario of the Qiskrypt's Quantum Cryptographic Primitive is valid.
            """

            primitive_properties = list()
            """
            Create an empty list of properties of the Qiskrypt's
            Quantum Cryptographic Primitive.
            """

            super().__init__(DV_BB84_PROTOCOL_NAME,
                             POSSIBLE_QUANTUM_CRYPTOGRAPHIC_PRIMITIVE_SIGNAL_VARIABLE_TYPES[0],
                             primitive_properties, primitive_scenario, num_rounds_for_quantum_transmission_phase,
                             POSSIBLE_QUANTUM_KEY_DISTRIBUTION_TYPES[0], verbose)
            """
            Call of the constructor of the super-class Qiskrypt's Quantum Key Distribution (QKD).
            """

            self.quantum_bit_error_rates = \
                [0.0] * len(POSSIBLE_DV_BB84_PROTOCOL_ROUND_TYPES_QUANTUM_TRANSMISSION_PHASE)
            """
            Initialise the list of QBERs (Quantum Bit Error Rates) to be
            estimated during the Parameter Estimation of
            the Qiskrypt's Noiseless DV (Discrete Variables) 
            BB84 Protocol with No Eavesdropping.
            """

        else:
            """
            If the scenario of the Qiskrypt's Quantum Cryptographic Primitive is not valid.
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

        super().set_as_configured()
        """
        Set the boolean flag to determine if the Qiskrypt's Key Exchange Protocol
        is configured, as True.
        """

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
        the Qiskrypt's Quantum Key Distribution (QKD) not discarded from the Key Sifting.

        :return super().get_quantum_transmission_phase_rounds_not_discarded_from_key_sifting():
                the list of the rounds for the Quantum Transmission Phase of
                the Qiskrypt's Quantum Key Distribution (QKD) not discarded from the Key Sifting.
        """

        """
        Return the list of the rounds for the Quantum Transmission Phase of
        the Qiskrypt's Quantum Key Distribution (QKD) not discarded from the Key Sifting.
        """
        return super().get_quantum_transmission_phase_rounds_not_discarded_from_key_sifting()

    def get_quantum_transmission_phase_rounds_not_discarded_from_parameter_estimation(self) -> list:
        """
        Return the list of the rounds for the Quantum Transmission Phase of
        the Qiskrypt's Quantum Key Distribution (QKD) not discarded from the Parameter Estimation.

        :return super().get_quantum_transmission_phase_rounds_not_discarded_from_parameter_estimation():
                the list of the rounds for the Quantum Transmission Phase of
                the Qiskrypt's Quantum Key Distribution (QKD) not discarded from the Parameter Estimation.
        """

        """
        Return the list of the rounds for the Quantum Transmission Phase of
        the Qiskrypt's Quantum Key Distribution (QKD) not discarded from the Parameter Estimation.
        """
        return super().get_quantum_transmission_phase_rounds_not_discarded_from_parameter_estimation()

    def get_quantum_bit_error_rate_z_basis(self) -> float:
        """
        Return the QBER (Quantum Bit Error Rate) of the Z-Basis (Standard Computational Basis) Rounds
        estimated during the Parameter Estimation of the Qiskrypt's DV (Discrete Variables) BB84 Protocol.

        :return self.quantum_bit_error_rates[0]: the QBER (Quantum Bit Error Rate) of
                                                 the Z-Basis (Standard Computational Basis) Rounds
                                                 estimated during the Parameter Estimation of
                                                 the Qiskrypt's DV (Discrete Variables) BB84 Protocol.
        """

        if self.is_configured():
            """
            If the Qiskrypt's Key Exchange Protocol is already configured.
            """

            """
            Return the QBER (Quantum Bit Error Rate) of the Z-Basis (Standard Computational Basis) Rounds
            estimated during the Parameter Estimation of the Qiskrypt's DV (Discrete Variables) BB84 Protocol.
            """
            return self.quantum_bit_error_rates[0]

        else:
            """
            If the Qiskrypt's Key Exchange Protocol is not configured yet.
            """

            # TODO Throw - Exception

    def get_quantum_bit_error_rate_x_basis(self) -> float:
        """
        Return the QBER (Quantum Bit Error Rate) of the X-Basis (Hadamard Basis) Rounds
        estimated during the Parameter Estimation of the Qiskrypt's DV (Discrete Variables) BB84 Protocol.

        :return self.quantum_bit_error_rates[1]: the QBER (Quantum Bit Error Rate) of
                                                 the X-Basis (Hadamard Basis) Rounds
                                                 estimated during the Parameter Estimation of
                                                 the Qiskrypt's DV (Discrete Variables) BB84 Protocol.
        """

        if self.is_configured():
            """
            If the Qiskrypt's Key Exchange Protocol is already configured.
            """

            """
            Return the QBER (Quantum Bit Error Rate) of the X-Basis (Hadamard Basis) Rounds
            estimated during the Parameter Estimation of the Qiskrypt's DV (Discrete Variables) BB84 Protocol.
            """
            return self.quantum_bit_error_rates[1]

        else:
            """
            If the Qiskrypt's Key Exchange Protocol is not configured yet.
            """

            # TODO Throw - Exception

    def get_global_quantum_bit_error_rate(self) -> float:
        """
        Return the global QBER (Quantum Bit Error Rate) of the rounds estimated during
        the Parameter Estimation of the Qiskrypt's DV (Discrete Variables) BB84 Protocol.

        :return global_quantum_bit_error_rate: the global QBER (Quantum Bit Error Rate) of
                                               the rounds estimated during the Parameter Estimation of
                                               the Qiskrypt's DV (Discrete Variables) BB84 Protocol.
        """

        global_quantum_bit_error_rate = \
            self.get_quantum_bit_error_rate_z_basis() + \
            self.get_quantum_bit_error_rate_x_basis()
        """
        Retrieve the global QBER (Quantum Bit Error Rate) of the rounds estimated during
        the Parameter Estimation of the Qiskrypt's DV (Discrete Variables) BB84 Protocol.
        """

        """
        Return the global QBER (Quantum Bit Error Rate) of the rounds estimated during
        the Parameter Estimation of the Qiskrypt's DV (Discrete Variables) BB84 Protocol.
        """
        return global_quantum_bit_error_rate

    def update_quantum_bit_error_rate_z_basis(self, quantum_bit_error_rate_z_basis: float) -> None:
        """
        Update the QBER (Quantum Bit Error Rate) of the Z-Basis (Standard Computational Basis) Rounds
        estimated during the Parameter Estimation of the Qiskrypt's DV (Discrete Variables) BB84 Protocol.

        :param quantum_bit_error_rate_z_basis: the QBER (Quantum Bit Error Rate) of
                                               the Z-Basis (Standard Computational Basis) Rounds
                                               estimated during the Parameter Estimation of
                                               the Qiskrypt's DV (Discrete Variables) BB84 Protocol.
        """

        if self.is_configured():
            """
            If the Qiskrypt's Key Exchange Protocol is already configured.
            """

            """
            Update the QBER (Quantum Bit Error Rate) of the Z-Basis (Standard Computational Basis) Rounds
            estimated during the Parameter Estimation of the Qiskrypt's DV (Discrete Variables) BB84 Protocol.
            """
            self.quantum_bit_error_rates[0] = quantum_bit_error_rate_z_basis

        else:
            """
            If the Qiskrypt's Key Exchange Protocol is not configured yet.
            """

            # TODO Throw - Exception

    def update_quantum_bit_error_rate_x_basis(self, quantum_bit_error_rate_x_basis: float) -> None:
        """
        Update the QBER (Quantum Bit Error Rate) of the X-Basis (Hadamard Basis) Rounds
        estimated during the Parameter Estimation of the Qiskrypt's DV (Discrete Variables) BB84 Protocol.

        :param quantum_bit_error_rate_x_basis: the QBER (Quantum Bit Error Rate) of
                                               the X-Basis (Hadamard Basis) Rounds
                                               estimated during the Parameter Estimation of
                                               the Qiskrypt's DV (Discrete Variables) BB84 Protocol.
        """

        if self.is_configured():
            """
            If the Qiskrypt's Key Exchange Protocol is already configured.
            """

            """
            Update the QBER (Quantum Bit Error Rate) of the X-Basis (Hadamard Basis) Rounds
            estimated during the Parameter Estimation of the Qiskrypt's DV (Discrete Variables) BB84 Protocol.
            """
            self.quantum_bit_error_rates[1] = quantum_bit_error_rate_x_basis

        else:
            """
            If the Qiskrypt's Key Exchange Protocol is not configured yet.
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

    def start_quantum_transmission_phase(self):
        """
        Start the Quantum Transmission Phase of the
        Qiskrypt's Quantum Key Exchange Protocol.
        """

        """
        Start the Quantum Transmission Phase of the
        Qiskrypt's Quantum Key Exchange Protocol.
        """
        super().start_quantum_transmission_phase()

    def start_classical_post_processing_phase(self):
        """
        Start the Classical Post-Processing Phase of the
        Qiskrypt's Quantum Key Exchange Protocol.
        """

        """
        Start the Classical Post-Processing Phase of the
        Qiskrypt's Quantum Key Exchange Protocol.
        """
        super().start_classical_post_processing_phase()

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
        Qiskrypt's Quantum Key Distribution (QKD).
        """

        """
        Prepare the Quantum States for the
        Qiskrypt's Quantum Key Distribution (QKD).
        """
        super().prepare_quantum_states()

    def transmit_quantum_states(self):
        """
        Transmit the Quantum States for the
        Qiskrypt's Quantum Key Distribution (QKD).
        """

        """
        Transmit the Quantum States for the
        Qiskrypt's Quantum Key Distribution (QKD).
        """
        super().transmit_quantum_states()

    def measure_quantum_states(self):
        """
        Measure the Quantum States for the
        Qiskrypt's Quantum Key Distribution (QKD).
        """

        """
        Measure the Quantum States for the
        Qiskrypt's Quantum Key Distribution (QKD).
        """
        super().measure_quantum_states()

    def sift_raw_key(self):
        """
        Sift the Secret Key for the
        Qiskrypt's Quantum Key Distribution (QKD).
        """

        """
        Sift the Secret Key for the
        Qiskrypt's Quantum Key Distribution (QKD).
        """
        super().sift_raw_key()

    def estimate_parameters(self):
        """
        Estimate the Parameters for the
        Qiskrypt's Quantum Key Distribution (QKD).
        """

        """
        Estimate the Parameters for the
        Qiskrypt's Quantum Key Distribution (QKD).
        """
        super().estimate_parameters()

    def reconcile_information(self):
        """
        Reconcile the Information for the
        Qiskrypt's Quantum Key Distribution (QKD).
        """

        """
        Reconcile the Information for the
        Qiskrypt's Quantum Key Distribution (QKD).
        """
        super().reconcile_information()

    def amplify_privacy(self):
        """
        Amplify the Privacy for the
        Qiskrypt's Quantum Key Distribution (QKD).
        """

        """
        Amplify the Privacy for the
        Qiskrypt's Quantum Key Distribution (QKD).
        """
        super().amplify_privacy()
