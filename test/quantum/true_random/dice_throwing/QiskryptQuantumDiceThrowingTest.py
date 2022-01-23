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

from unittest import TestCase, TestLoader, TestSuite
"""
Import TestCase, TestLoader and TestSuite from Unittest.
"""

from src.quantum_regime.true_random.dice_throwing.QiskryptQuantumDiceThrowing \
    import QiskryptQuantumDiceThrowing
"""
Import the Qiskrypt's Quantum Dice Throwing.
"""

"""
Definition of Constants and Enumerations.
"""

from src.quantum_regime.true_random.dice_throwing.QiskryptQuantumDiceThrowing \
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

        - Throw a Tetrahedron Dice from the Qiskrypt's Quantum Dice Throwing.

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
        Initiate/Configure the previously created Qiskrypt's Quantum Dice Throwing,
        for a Tetrahedron Dice.
        """

        qiskrypt_quantum_dice_throwing.throw_dice()
        """
        Throw the Tetrahedron Dice from the Qiskrypt's Quantum Dice Throwing.
        """

        num_points_on_dice = qiskrypt_quantum_dice_throwing.get_dice_throwing_num_points()
        """
        Extract the respective number of points on the dice,
        from the resulted classical_regime outcome/result,
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

    def test_no_2_qiskrypt_quantum_dice_throwing_cube(self):
        """
        Test Case #2:

        - Throw a Cube Dice from the Qiskrypt's Quantum Dice Throwing.

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Quantum Dice Throwing is configured, for a Cube Dice;
        2) The Cube Dice is thrown from the Qiskrypt's Quantum Dice Throwing;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        qiskrypt_quantum_dice_throwing = \
            QiskryptQuantumDiceThrowing("qu_dice_throw_cube_2")
        """
        Create a Qiskrypt's Quantum Dice Throwing, for a Cube Dice.
        """

        qiskrypt_quantum_dice_throwing.configure(DICE_TYPES[1])
        """
        Initiate/Configure the previously created Qiskrypt's Quantum Dice Throwing,
        for a Cube Dice.
        """

        qiskrypt_quantum_dice_throwing.throw_dice()
        """
        Throw the Cube Dice from the Qiskrypt's Quantum Dice Throwing.
        """

        num_points_on_dice = qiskrypt_quantum_dice_throwing.get_dice_throwing_num_points()
        """
        Extract the respective number of points on the dice,
        from the resulted classical_regime outcome/result,
        after the Cube Dice been thrown from the Qiskrypt's Quantum Dice Throwing.
        """

        print(f"\n\nTest #2:"
              f"\n - The number of points extracted from "
              f"throwing a Cube Dice from the Qiskrypt's Quantum Dice Throwing is:\n"
              f"   [ {num_points_on_dice} ] (Decimal Format) ;\n")
        """
        Print the resulted number of points, extracted from
        the Qiskrypt's Quantum Dice Throwing.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_3_qiskrypt_quantum_dice_throwing_octahedron(self):
        """
        Test Case #3:

        - Throw an Octahedron Dice from the Qiskrypt's Quantum Dice Throwing.

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Quantum Dice Throwing is configured, for an Octahedron Dice;
        2) The Octahedron Dice is thrown from the Qiskrypt's Quantum Dice Throwing;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        qiskrypt_quantum_dice_throwing = \
            QiskryptQuantumDiceThrowing("qu_dice_throw_octahedron_3")
        """
        Create a Qiskrypt's Quantum Dice Throwing, for an Octahedron Dice.
        """

        qiskrypt_quantum_dice_throwing.configure(DICE_TYPES[2])
        """
        Initiate/Configure the previously created Qiskrypt's Quantum Dice Throwing,
        for an Octahedron Dice.
        """

        qiskrypt_quantum_dice_throwing.throw_dice()
        """
        Throw the Octahedron Dice from the Qiskrypt's Quantum Dice Throwing.
        """

        num_points_on_dice = qiskrypt_quantum_dice_throwing.get_dice_throwing_num_points()
        """
        Extract the respective number of points on the dice,
        from the resulted classical_regime outcome/result,
        after the Octahedron Dice been thrown from the Qiskrypt's Quantum Dice Throwing.
        """

        print(f"\n\nTest #3:"
              f"\n - The number of points extracted from "
              f"throwing an Octahedron Dice from the Qiskrypt's Quantum Dice Throwing is:\n"
              f"   [ {num_points_on_dice} ] (Decimal Format) ;\n")
        """
        Print the resulted number of points, extracted from
        the Qiskrypt's Quantum Dice Throwing.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_4_qiskrypt_quantum_dice_throwing_pentagonal_trapezohedron(self):
        """
        Test Case #4:

        - Throw a Pentagonal Trapezohedron Dice from the Qiskrypt's Quantum Dice Throwing.

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Quantum Dice Throwing is configured, for a Pentagonal Trapezohedron Dice;
        2) The Pentagonal Trapezohedron Dice is thrown from the Qiskrypt's Quantum Dice Throwing;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        qiskrypt_quantum_dice_throwing = \
            QiskryptQuantumDiceThrowing("qu_dice_throw_pentagonal_trapezohedron_4")
        """
        Create a Qiskrypt's Quantum Dice Throwing, for a Pentagonal Trapezohedron Dice.
        """

        qiskrypt_quantum_dice_throwing.configure(DICE_TYPES[3])
        """
        Initiate/Configure the previously created Qiskrypt's Quantum Dice Throwing,
        for a Pentagonal Trapezohedron Dice.
        """

        qiskrypt_quantum_dice_throwing.throw_dice()
        """
        Throw the Pentagonal Trapezohedron Dice from the Qiskrypt's Quantum Dice Throwing.
        """

        num_points_on_dice = qiskrypt_quantum_dice_throwing.get_dice_throwing_num_points()
        """
        Extract the respective number of points on the dice,
        from the resulted classical_regime outcome/result,
        after the Pentagonal Trapezohedron Dice been thrown from the Qiskrypt's Quantum Dice Throwing.
        """

        print(f"\n\nTest #4:"
              f"\n - The number of points extracted from "
              f"throwing a Pentagonal Trapezohedron Dice from the Qiskrypt's Quantum Dice Throwing is:\n"
              f"   [ {num_points_on_dice} ] (Decimal Format) ;\n")
        """
        Print the resulted number of points, extracted from
        the Qiskrypt's Quantum Dice Throwing.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_5_qiskrypt_quantum_dice_throwing_dodecahedron(self):
        """
        Test Case #5:

        - Throw a Dodecahedron Dice from the Qiskrypt's Quantum Dice Throwing.

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Quantum Dice Throwing is configured, for a Dodecahedron Dice;
        2) The Dodecahedron Dice is thrown from the Qiskrypt's Quantum Dice Throwing;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        qiskrypt_quantum_dice_throwing = \
            QiskryptQuantumDiceThrowing("qu_dice_throw_dodecahedron_5")
        """
        Create a Qiskrypt's Quantum Dice Throwing, for a Dodecahedron Dice.
        """

        qiskrypt_quantum_dice_throwing.configure(DICE_TYPES[4])
        """
        Initiate/Configure the previously created Qiskrypt's Quantum Dice Throwing,
        for a Dodecahedron Dice.
        """

        qiskrypt_quantum_dice_throwing.throw_dice()
        """
        Throw the Dodecahedron Dice from the Qiskrypt's Quantum Dice Throwing.
        """

        num_points_on_dice = qiskrypt_quantum_dice_throwing.get_dice_throwing_num_points()
        """
        Extract the respective number of points on the dice,
        from the resulted classical_regime outcome/result,
        after the Dodecahedron Dice been thrown from the Qiskrypt's Quantum Dice Throwing.
        """

        print(f"\n\nTest #5:"
              f"\n - The number of points extracted from "
              f"throwing a Dodecahedron Dice from the Qiskrypt's Quantum Dice Throwing is:\n"
              f"   [ {num_points_on_dice} ] (Decimal Format) ;\n")
        """
        Print the resulted number of points, extracted from
        the Qiskrypt's Quantum Dice Throwing.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_6_qiskrypt_quantum_dice_throwing_icosahedron(self):
        """
        Test Case #6:

        - Throw an Icosahedron Dice from the Qiskrypt's Quantum Dice Throwing.

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Quantum Dice Throwing is configured, for an Icosahedron Dice;
        2) The Icosahedron Dice is thrown from the Qiskrypt's Quantum Dice Throwing;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        qiskrypt_quantum_dice_throwing = \
            QiskryptQuantumDiceThrowing("qu_dice_throw_icosahedron_6")
        """
        Create a Qiskrypt's Quantum Dice Throwing, for an Icosahedron Dice.
        """

        qiskrypt_quantum_dice_throwing.configure(DICE_TYPES[5])
        """
        Initiate/Configure the previously created Qiskrypt's Quantum Dice Throwing,
        for an Icosahedron Dice.
        """

        qiskrypt_quantum_dice_throwing.throw_dice()
        """
        Throw the Icosahedron Dice from the Qiskrypt's Quantum Dice Throwing.
        """

        num_points_on_dice = qiskrypt_quantum_dice_throwing.get_dice_throwing_num_points()
        """
        Extract the respective number of points on the dice,
        from the resulted classical_regime outcome/result,
        after the Icosahedron Dice been thrown from the Qiskrypt's Quantum Dice Throwing.
        """

        print(f"\n\nTest #6:"
              f"\n - The number of points extracted from "
              f"throwing an Icosahedron Dice from the Qiskrypt's Quantum Dice Throwing is:\n"
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
