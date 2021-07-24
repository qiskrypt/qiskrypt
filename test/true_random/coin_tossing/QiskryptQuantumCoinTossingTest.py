"""

Copyrights:\n
- © Qiskrypt, 2021 - All rights reserved.\n

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

"""

"""
Import required Libraries and Packages.
"""

from unittest import TestCase, TestLoader, TestSuite
"""
Import TestCase, TestLoader and TestSuite from Unittest.
"""

from src.true_random.coin_tossing.QiskryptQuantumCoinTossing import QiskryptQuantumCoinTossing


class QiskryptQuantumCoinTossingTests(TestCase):

    def test_no_1_single_qiskrypt_quantum_coin_tossing(self):

        qiskrypt_quantum_coin_tossing = QiskryptQuantumCoinTossing("qu_coin_toss")
        """
        Create the Qiskrypt's Quantum Coin Tossing.
        """

        qiskrypt_quantum_coin_tossing.initialise_qiskrypt_quantum_circuit()
        """
        Initialise the Qiskrypt's Quantum Circuit for the Qiskrypt's Quantum Coin Tossing.
        """

        qiskrypt_quantum_coin_tossing.toss_coin()
        """
        Toss a Coin, through the previously created Qiskrypt's Quantum Coin Tossing.
        """

        coin_tossing_outcome_bit = qiskrypt_quantum_coin_tossing.get_coin_tossing_outcome_bit()
        """
        Retrieve the classical outcome (i.e., the observation) from the Coin Tossing,
        through the execution of the respective Qiskrypt's Quantum Circuit,
        in a binary digit format (i.e., a bit).
        """

        if coin_tossing_outcome_bit == "0b0":
            """
            If the classical outcome (i.e., the observation) from the Coin Tossing is |0⟩.
            """

            self.assertEqual(qiskrypt_quantum_coin_tossing.get_coin_tossing_outcome_bit_as_int_base_2(), 0)
            """
            Assert if the classical outcome (i.e., the observation) from the Coin Tossing,
            in an integer base-2 format is 0.
            """

            self.assertEqual(qiskrypt_quantum_coin_tossing.get_coin_tossing_outcome_bit_as_head_or_tails(), "HEADS")
            """
            Assert if the classical outcome (i.e., the observation) from the Coin Tossing,
            in an anatomic part format is 'HEADS'.
            """

        if coin_tossing_outcome_bit == "0b1":
            """
            If the classical outcome (i.e., the observation) from the Coin Tossing is |1⟩.
            """

            self.assertEqual(qiskrypt_quantum_coin_tossing.get_coin_tossing_outcome_bit_as_int_base_2(), 1)
            """
            Assert if the classical outcome (i.e., the observation) from the Coin Tossing,
            in an integer base-2 format is 1.
            """

            self.assertEqual(qiskrypt_quantum_coin_tossing.get_coin_tossing_outcome_bit_as_head_or_tails(), "TAILS")
            """
            Assert if the classical outcome (i.e., the observation) from the Coin Tossing,
            in an anatomic part format is 'TAILS'.
            """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)


if __name__ == "__main__":
    """
    The Main Method for the Unitary Test.
    """

    qiskrypt_quantum_coin_tossing_test_cases = \
        TestLoader().loadTestsFromTestCase(QiskryptQuantumCoinTossingTests)
    """
    Load the Test Cases from the Unitary Tests for the Qiskrypt's Quantum Coin Tossing.
    """

    qiskrypt_quantum_coin_tossing_test_suite = \
        TestSuite([qiskrypt_quantum_coin_tossing_test_cases])
    """
    Load the Test Suite with all the Test Cases for the Qiskrypt's Quantum Coin Tossing.
    """
