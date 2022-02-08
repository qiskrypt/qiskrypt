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


class QiskryptDVBB84ProtocolExecutor:
    """
    Object class for the Qiskrypt's DV (Discrete Variables) BB84 Protocol Executor.
    """

    def __init__(self, with_noise: bool, with_eavesdropping: bool):
        """
        Constructor of the Qiskrypt's DV (Discrete Variables) BB84 Protocol Executor.

        :param with_noise: the boolean flag to keep information about if
                           the Qiskrypt's DV (Discrete Variables) BB84 Protocol
                           is executing with noise.
        :param with_eavesdropping: the boolean flag to keep information about if
                                   the Qiskrypt's DV (Discrete Variables) BB84 Protocol
                                   is executing with eavesdropping.
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

    def run(self) -> None:
        """
        Run the Qiskrypt's DV (Discrete Variables) BB84 Protocol Executor.
        """

        if not self.is_with_noise() and not self.is_with_eavesdropping():
            """
            1) If the Qiskrypt's DV (Discrete Variables) BB84 Protocol is
               executing with no noise and with no eavesdropping.
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
