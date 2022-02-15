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

from src.classical_regime.common.QiskryptMessageColorsEnumeration \
    import QiskryptMessageColorsEnumeration
"""
Import the Qiskrypt's Message Colors Enumeration.
"""

from src.quantum_regime.cryptography.key_exchange\
    .quantum_key_distribution.discrete_variables.prepare_and_measure\
    .bb84.noiseless.with_no_eavesdropping.QiskryptNoiselessDVBB84ProtocolWithNoEavesdropping \
    import QiskryptNoiselessDVBB84ProtocolWithNoEavesdropping
"""
Import the Qiskrypt's Noiseless DV (Discrete Variables) BB84 Protocol with No Eavesdropping.
"""


class QiskryptDVBB84ProtocolExecutor:
    """
    Object class for the Qiskrypt's DV (Discrete Variables) BB84 Protocol Executor.
    """

    def __init__(self, with_noise: bool, with_eavesdropping: bool, verbose=True):
        """
        Constructor of the Qiskrypt's DV (Discrete Variables) BB84 Protocol Executor.

        :param with_noise: the boolean flag to keep information about if
                           the Qiskrypt's DV (Discrete Variables) BB84 Protocol
                           is executing with noise.
        :param with_eavesdropping: the boolean flag to keep information about if
                                   the Qiskrypt's DV (Discrete Variables) BB84 Protocol
                                   is executing with eavesdropping.
        :param verbose: the boolean flag to show the runtime information about
                        the Qiskrypt's DV (Discrete Variables) BB84 Protocol.
        """

        self.with_noise = with_noise
        """
        Set the boolean flag to keep information about if
        the Qiskrypt's DV (Discrete Variables) BB84 Protocol is executing with noise.
        """

        self.with_eavesdropping = with_eavesdropping
        """
        Set the boolean flag to keep information about if
        the Qiskrypt's DV (Discrete Variables) BB84 Protocol is executing with eavesdropping.
        """

        self.verbose = verbose
        """
        Set the boolean flag to show the runtime information about
        the Qiskrypt's DV (Discrete Variables) BB84 Protocol execution.
        """

    def is_with_noise(self) -> bool:
        """
        Return the boolean flag to keep information about if
        the Qiskrypt's DV (Discrete Variables) BB84 Protocol is executing with noise.

        :return self.with_noise: the boolean flag to keep information about if
                                 the Qiskrypt's DV (Discrete Variables) BB84 Protocol is
                                 executing with noise.
        """

        """
        Return the boolean flag to keep information about if
        the Qiskrypt's DV (Discrete Variables) BB84 Protocol is executing with noise.
        """
        return self.with_noise

    def is_with_eavesdropping(self) -> bool:
        """
        Return the boolean flag to keep information about if
        the Qiskrypt's DV (Discrete Variables) BB84 Protocol is executing with eavesdropping.

        :return self.with_eavesdropping: the boolean flag to keep information about if
                                         the Qiskrypt's DV (Discrete Variables) BB84 Protocol is
                                         executing with eavesdropping.
        """

        """
        Return the boolean flag to keep information about if
        the Qiskrypt's DV (Discrete Variables) BB84 Protocol is executing with eavesdropping.
        """
        return self.with_eavesdropping

    def is_verbose(self) -> bool:
        """
        Return the boolean flag to show the runtime information about
        the Qiskrypt's DV (Discrete Variables) BB84 Protocol execution.

        :return self.verbose: the boolean flag to show the runtime information about
                              the Qiskrypt's DV (Discrete Variables) BB84 Protocol execution.
        """

        """
        Return the boolean flag to show the runtime information about
        the Qiskrypt's DV (Discrete Variables) BB84 Protocol execution.
        """
        return self.verbose

    def execute(self) -> None:
        """
        Execute the Qiskrypt's DV (Discrete Variables) BB84 Protocol Executor.
        """

        if not self.is_with_noise() and not self.is_with_eavesdropping():
            """
            1) If the Qiskrypt's DV (Discrete Variables) BB84 Protocol is
               executing with no noise and with no eavesdropping.
            """

            print("{}{}".format(QiskryptMessageColorsEnumeration.HEADER.value,
                                "\nExecuting the Qiskrypt's DV (Discrete Variables) BB84 Protocol\n"
                                "with no noise and no eavesdropping...\n"))
            """
            Print the initial message.
            """

            noiseless_dv_bb84_protocol_with_no_eavesdropping = \
                QiskryptNoiselessDVBB84ProtocolWithNoEavesdropping()
            """
            Create a Qiskrypt's Noiseless DV (Discrete Variables)
            BB84 Protocol with No Eavesdropping.
            """

            noiseless_dv_bb84_protocol_with_no_eavesdropping.configure()
            """
            Configure the Qiskrypt's Noiseless DV (Discrete Variables)
            BB84 Protocol with No Eavesdropping.
            """

            # TODO
            #noiseless_dv_bb84_protocol_with_no_eavesdropping.run()
            """
            Run the Qiskrypt's Noiseless DV (Discrete Variables)
            BB84 Protocol with No Eavesdropping.
            """

        elif not self.is_with_noise() and self.is_with_eavesdropping():
            """
            2) If the Qiskrypt's DV (Discrete Variables) BB84 Protocol is
               executing with no noise and with eavesdropping.
            """

        elif self.is_with_noise() and not self.is_with_eavesdropping():
            """
            3) If the Qiskrypt's DV (Discrete Variables) BB84 Protocol is
               executing with noise and with no eavesdropping.
            """

        elif self.is_with_noise() and self.is_with_eavesdropping():
            """
            4) If the Qiskrypt's DV (Discrete Variables) BB84 Protocol is
               executing with noise and with eavesdropping.
            """


def main():
    dv_bb84_protocol_executor = QiskryptDVBB84ProtocolExecutor(False, False, verbose=True)
    dv_bb84_protocol_executor.execute()


if __name__ == "__main__":
    main()
