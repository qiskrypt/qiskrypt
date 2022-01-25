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
Definition of Constants and Enumerations.
"""

BINARY_FORMAT_START_OFFSET = 2
"""
The offset for the start of the Python's binary format.
"""


class QiskryptClassicalUtilities:
    """
    Object class for the Qiskrypt's Classical Utilities.
    """

    @staticmethod
    def compute_hamming_weight(binary_string_bits: bin):
        """
        Return the Hamming Weight of the bits of a given binary string.

        :param binary_string_bits: the bits of a given binary string.

        :return hamming_weight: the Hamming Weight of the bits of a given binary string.
        """

        hamming_weight = 0
        """
        Initialise the counter for the Hamming Weight, as zero (0).
        """

        for current_bit in range(len(binary_string_bits[BINARY_FORMAT_START_OFFSET:])):
            """
            For each bit of the of the given binary string.
            """

            if binary_string_bits[(BINARY_FORMAT_START_OFFSET + current_bit)] == "1":
                """
                If the current bit of the given binary string is one (1).
                """

                hamming_weight += 1
                """
                Increase the counter for the Hamming Weight.
                """

        """
        Return the Hamming Weight of the bits of a given binary string.
        """
        return hamming_weight
