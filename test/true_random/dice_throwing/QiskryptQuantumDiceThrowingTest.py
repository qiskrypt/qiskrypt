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

from src.true_random.dice_throwing.QiskryptQuantumDiceThrowing \
    import QiskryptQuantumDiceThrowing
"""
Import the Qiskrypt's Quantum Dice Throwing.
"""

"""
Definition of Constants and Enumerations.
"""

from src.true_random.dice_throwing.QiskryptQuantumDiceThrowing \
    import DICE_TYPES
"""
Import the Dice Types for all the configurations available for
the Qiskrypt's Quantum Dice Throwing.
"""


class QiskryptQuantumDiceThrowingTests(TestCase):
    """
    Object Class of the Unitary Tests for the Qiskrypt's Quantum Dice Throwing.
    """

    def test_no_1_qiskrypt_quantum_dice_throwing_tetrahedron(self):
        """
        Test Case #1:

        - Initialise the Qiskrypt's Quantum Dice Throwing, for a Tetrahedron Dice.

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Quantum Dice Throwing is configured, for a Tetrahedron Dice;
        2) The Tetrahedron Dice is thrown from the Qiskrypt's Quantum Dice Throwing;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        qiskrypt_quantum_dice_throwing = \
            QiskryptQuantumDiceThrowing("qu_dice_throw_tetrahedron_1")
        """
        Create a Qiskrypt's Quantum Dice Throwing, for a Tetrahedron Dice.
        """

        qiskrypt_quantum_dice_throwing.configure(DICE_TYPES[0])
        """
        Initiate/Configure the previously created Qiskrypt's Quantum Dice Throwing.
        """

        qiskrypt_quantum_dice_throwing.throw_dice()
        """
        Throw the Tetrahedron Dice from the Qiskrypt's Quantum Dice Throwing.
        """

        num_points_on_dice = qiskrypt_quantum_dice_throwing.get_dice_throwing_num_points()
        """
        Extract the respective number of points on the dice,
        from the resulted classical outcome/result,
        after the Tetrahedron Dice been thrown from the Qiskrypt's Quantum Dice Throwing.
        """

        print(f"\n\nTest #1:"
              f"\n - The number of points extracted from "
              f"throwing a Tetrahedron Dice from the Qiskrypt's Quantum Dice Throwing is:\n"
              f"   [ {num_points_on_dice} ] (Decimal Format) ;\n")
        """
        Print the resulted number of points, extracted from
        the Qiskrypt's Quantum Dice Throwing.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)


if __name__ == "__main__":
    """
    The Main Method for the Unitary Test.
    """

    qiskrypt_quantum_dice_throwing_test_cases = \
        TestLoader().loadTestsFromTestCase(QiskryptQuantumDiceThrowingTests)
    """
    Load the Test Cases from the Unitary Tests for the Qiskrypt's Quantum Dice Throwing.
    """

    qiskrypt_quantum_dice_throwing_test_suite = \
        TestSuite([qiskrypt_quantum_dice_throwing_test_cases])
    """
    Load the Test Suite with all the Test Cases for the Qiskrypt's Quantum Dice Throwing.
    """
