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
- Prof. Antonio Ravara (NOVA School of Science and Technology, NOVA University of Lisbon, Portugal).

"""

"""
Import required Libraries and Packages.
"""

from unittest import TestCase, TestLoader, TestSuite
"""
Import TestCase, TestLoader and TestSuite from Unittest.
"""

from src.quantum.true_random.password_generator.QiskryptQuantumRandomPasswordGenerator \
    import QiskryptQuantumRandomPasswordGenerator
"""
Import the Qiskrypt's Quantum Random Password Generator.
"""


class QiskryptQuantumRandomPasswordGeneratorTests(TestCase):
    """
    Object Class of the Unitary Tests for the Qiskrypt's Quantum Random Password Generator.
    """

    def test_no_1_qiskrypt_quantum_random_password_generator_length_10(self):
        """
        Test Case #1:

        - Initialise the Qiskrypt's Quantum Random Password Generator, with a given size of 10,
          and generate a random password string, without the given exceptions of characters.

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Quantum Random Password Generator is initialised, with a size of 10;
        2) The password string is generated from the Qiskrypt's Quantum Random Password Generator,
           according to the specified exceptions of characters;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        length_password_string = 10
        """
        Set the length of the password string generated from
        the Qiskrypt's Quantum Random Password Generator, as 10.
        """

        qiskrypt_quantum_random_password_generator = \
            QiskryptQuantumRandomPasswordGenerator("qu_rnd_pwd_gen_1",
                                                   characters_exceptions="0 3 6 9 a d g j m p s v z "
                                                                         "A D G J M P S V Z ? { } [ ] ( ) % @")
        """
        Create a Qiskrypt's Quantum Random Password Generator,
        with the given exceptions of characters.
        """

        qiskrypt_quantum_random_password_generator.initiate(length_password_string)
        """
        Initiate/Configure the previously created Qiskrypt's Quantum Random Password Generator.
        """

        password_string = qiskrypt_quantum_random_password_generator\
            .generate_password_string()
        """
        Generate the password string from the Qiskrypt's Quantum Random Password Generator.
        """

        print(f"\n\nTest #1:"
              f"\n - The Password String generated from "
              f"the Qiskrypt's Quantum Random Password Generator is:\n"
              f"   [ {password_string} ] ;\n")
        """
        Print the resulted password string of size 10, extracted from
        the Qiskrypt's Quantum Random Password Generator,
        with the given exceptions of characters.
        """

        assert(len(password_string) == length_password_string)
        """
        Assertion for the length of the password string generated from
        the Qiskrypt's Quantum Random Password Generator.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_2_qiskrypt_quantum_random_password_generator_length_20(self):
        """
        Test Case #2:

        - Initialise the Qiskrypt's Quantum Random Password Generator, with a given size of 20,
          and generate a random password string, without the given exceptions of characters.

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Quantum Random Password Generator is initialised, with a size of 20;
        2) The password string is generated from the Qiskrypt's Quantum Random Password Generator,
           according to the specified exceptions of characters;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        length_password_string = 20
        """
        Set the length of the password string generated from
        the Qiskrypt's Quantum Random Password Generator, as 20.
        """

        qiskrypt_quantum_random_password_generator = \
            QiskryptQuantumRandomPasswordGenerator("qu_rnd_pwd_gen_2",
                                                   characters_exceptions="0 3 6 9 a d g j m p s v z "
                                                                         "A D G J M P S V Z ? { } [ ] ( ) % @")
        """
        Create a Qiskrypt's Quantum Random Password Generator,
        with the given exceptions of characters.
        """

        qiskrypt_quantum_random_password_generator.initiate(length_password_string)
        """
        Initiate/Configure the previously created Qiskrypt's Quantum Random Password Generator.
        """

        password_string = qiskrypt_quantum_random_password_generator \
            .generate_password_string()
        """
        Generate the password string from the Qiskrypt's Quantum Random Password Generator.
        """

        print(f"\n\nTest #2:"
              f"\n - The Password String generated from "
              f"the Qiskrypt's Quantum Random Password Generator is:\n"
              f"   [ {password_string} ] ;\n")
        """
        Print the resulted password string of size 20, extracted from
        the Qiskrypt's Quantum Random Password Generator,
        with the given exceptions of characters.
        """

        assert (len(password_string) == length_password_string)
        """
        Assertion for the length of the password string generated from
        the Qiskrypt's Quantum Random Password Generator.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_3_qiskrypt_quantum_random_password_generator_length_30(self):
        """
        Test Case #3:

        - Initialise the Qiskrypt's Quantum Random Password Generator, with a given size of 30,
          and generate a random password string, without the given exceptions of characters.

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Quantum Random Password Generator is initialised, with a size of 30;
        2) The password string is generated from the Qiskrypt's Quantum Random Password Generator,
           according to the specified exceptions of characters;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        length_password_string = 30
        """
        Set the length of the password string generated from
        the Qiskrypt's Quantum Random Password Generator, as 30.
        """

        qiskrypt_quantum_random_password_generator = \
            QiskryptQuantumRandomPasswordGenerator("qu_rnd_pwd_gen_3",
                                                   characters_exceptions="0 3 6 9 a d g j m p s v z "
                                                                         "A D G J M P S V Z ? { } [ ] ( ) % @")
        """
        Create a Qiskrypt's Quantum Random Password Generator,
        with the given exceptions of characters.
        """

        qiskrypt_quantum_random_password_generator.initiate(length_password_string)
        """
        Initiate/Configure the previously created Qiskrypt's Quantum Random Password Generator.
        """

        password_string = qiskrypt_quantum_random_password_generator \
            .generate_password_string()
        """
        Generate the password string from the Qiskrypt's Quantum Random Password Generator.
        """

        print(f"\n\nTest #3:"
              f"\n - The Password String generated from "
              f"the Qiskrypt's Quantum Random Password Generator is:\n"
              f"   [ {password_string} ] ;\n")
        """
        Print the resulted password string of size 30, extracted from
        the Qiskrypt's Quantum Random Password Generator,
        with the given exceptions of characters.
        """

        assert (len(password_string) == length_password_string)
        """
        Assertion for the length of the password string generated from
        the Qiskrypt's Quantum Random Password Generator.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)


if __name__ == "__main__":
    """
    The Main Method for the Unitary Test.
    """

    qiskrypt_quantum_random_password_generator_test_cases = \
        TestLoader().loadTestsFromTestCase(QiskryptQuantumRandomPasswordGeneratorTests)
    """
    Load the Test Cases from the Unitary Tests for the Qiskrypt's Quantum Random Password Generator.
    """

    qiskrypt_quantum_random_password_generator_test_suite = \
        TestSuite([qiskrypt_quantum_random_password_generator_test_cases])
    """
    Load the Test Suite with all the Test Cases for the Qiskrypt's Quantum Random Password Generator.
    """
