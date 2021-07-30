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

from src.true_random.random_generator.alphabetic.QiskryptQuantumRandomAlphabeticGenerator \
    import QiskryptQuantumRandomAlphabeticGenerator
"""
Import the Qiskrypt's Quantum Random Alphabetic Generator.
"""


class QiskryptQuantumRandomAlphabeticGeneratorTests(TestCase):
    """
    Object Class of the Unitary Tests for the Qiskrypt's Quantum Random Alphabetic Generator.
    """

    def test_no_1_qiskrypt_quantum_random_alphabetic_generator_length_10_lowercase(self):
        """
        Test Case #1:

        - Initialise the Qiskrypt's Quantum Random Alphabetic Generator, with a given size of 10,
          and generate a random alphabetic string, only with lowercase characters.

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Quantum Random Alphabetic Generator is initialised, with a size of 10;
        2) The alphabetic string, only with lowercase characters,
           is generated from the Qiskrypt's Quantum Random Alphabetic Generator;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        length_alphabetic_string = 10
        """
        Set the length of the alphabetic string generated from
        the Qiskrypt's Quantum Random Alphabetic Generator, as 10.
        """

        qiskrypt_quantum_random_alphabetic_generator = \
            QiskryptQuantumRandomAlphabeticGenerator("qu_rnd_alpha_gen_1",
                                                     lowercase=True, uppercase=False,
                                                     punctuation=False)
        """
        Create a Qiskrypt's Quantum Random Alphabetic Generator.
        """

        qiskrypt_quantum_random_alphabetic_generator.initiate(length_alphabetic_string)
        """
        Initiate/Configure the previously created Qiskrypt's Quantum Random Alphabetic Generator.
        """

        alphabetic_string = qiskrypt_quantum_random_alphabetic_generator\
            .generate_alphabetic_string()
        """
        Generate the alphabetic string from the Qiskrypt's Quantum Random Alphabetic Generator,
        just for lowercase characters.
        """

        print(f"\n\nTest #1:"
              f"\n - The Alphabetic String generated from "
              f"the Qiskrypt's Quantum Random Alphabetic Generator is:\n"
              f"   [ {alphabetic_string} ]\n"
              f"   (Alphabetic Format with lowercase characters) ;\n")
        """
        Print the resulted alphabetic string of size 10, extracted from
        the Qiskrypt's Quantum Random Alphabetic Generator,
        only with lowercase characters.
        """

        assert(len(alphabetic_string) == length_alphabetic_string)
        """
        Assertion for the length of the alphabetic string generated from
        the Qiskrypt's Quantum Random Alphabetic Generator.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_2_qiskrypt_quantum_random_alphabetic_generator_length_10_lowercase_and_uppercase(self):
        """
        Test Case #2:

        - Initialise the Qiskrypt's Quantum Random Alphabetic Generator, with a given size of 10,
          and generate a random alphabetic string, only with lowercase characters and uppercase characters.

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Quantum Random Alphabetic Generator is initialised, with a size of 10;
        2) The alphabetic string, with lowercase characters and uppercase characters,
           is generated from the Qiskrypt's Quantum Random Alphabetic Generator;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        length_alphabetic_string = 10
        """
        Set the length of the alphabetic string generated from
        the Qiskrypt's Quantum Random Alphabetic Generator, as 10.
        """

        qiskrypt_quantum_random_alphabetic_generator = \
            QiskryptQuantumRandomAlphabeticGenerator("qu_rnd_alpha_gen_2",
                                                     lowercase=True, uppercase=True,
                                                     punctuation=False)
        """
        Create a Qiskrypt's Quantum Random Alphabetic Generator.
        """

        qiskrypt_quantum_random_alphabetic_generator.initiate(length_alphabetic_string)
        """
        Initiate/Configure the previously created Qiskrypt's Quantum Random Alphabetic Generator.
        """

        alphabetic_string = qiskrypt_quantum_random_alphabetic_generator\
            .generate_alphabetic_string()
        """
        Generate the alphabetic string from the Qiskrypt's Quantum Random Alphabetic Generator,
        just for lowercase characters and uppercase characters.
        """

        print(f"\n\nTest #2:"
              f"\n - The Alphabetic String generated from "
              f"the Qiskrypt's Quantum Random Alphabetic Generator is:\n"
              f"   [ {alphabetic_string} ]\n"
              f"   (Alphabetic Format with lowercase characters and uppercase characters) ;\n")
        """
        Print the resulted alphabetic string of size 10, extracted from
        the Qiskrypt's Quantum Random Alphabetic Generator,
        only with lowercase characters and uppercase characters.
        """

        assert(len(alphabetic_string) == length_alphabetic_string)
        """
        Assertion for the length of the alphabetic string generated from
        the Qiskrypt's Quantum Random Alphabetic Generator.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_3_qiskrypt_quantum_random_alphabetic_generator_length_10_lowercase_uppercase_and_punctuation(self):
        """
        Test Case #3:

        - Initialise the Qiskrypt's Quantum Random Alphabetic Generator, with a given size of 10,
          and generate a random alphabetic string, with lowercase characters, uppercase characters
          and punctuation.

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Quantum Random Alphabetic Generator is initialised, with a size of 10;
        2) The alphabetic string, with lowercase characters, uppercase characters and punctuation,
           is generated from the Qiskrypt's Quantum Random Alphabetic Generator;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        length_alphabetic_string = 10
        """
        Set the length of the alphabetic string generated from
        the Qiskrypt's Quantum Random Alphabetic Generator, as 10.
        """

        qiskrypt_quantum_random_alphabetic_generator = \
            QiskryptQuantumRandomAlphabeticGenerator("qu_rnd_alpha_gen_3",
                                                     lowercase=True, uppercase=True,
                                                     punctuation=True)
        """
        Create a Qiskrypt's Quantum Random Alphabetic Generator.
        """

        qiskrypt_quantum_random_alphabetic_generator.initiate(length_alphabetic_string)
        """
        Initiate/Configure the previously created Qiskrypt's Quantum Random Alphabetic Generator.
        """

        alphabetic_string = qiskrypt_quantum_random_alphabetic_generator\
            .generate_alphabetic_string()
        """
        Generate the alphabetic string from the Qiskrypt's Quantum Random Alphabetic Generator,
        just for lowercase characters, uppercase characters and punctuation.
        """

        print(f"\n\nTest #3:"
              f"\n - The Alphabetic String generated from "
              f"the Qiskrypt's Quantum Random Alphabetic Generator is:\n"
              f"   [ {alphabetic_string} ]\n"
              f"   (Alphabetic Format with lowercase characters, uppercase characters and punctuation) ;\n")
        """
        Print the resulted alphabetic string of size 10, extracted from
        the Qiskrypt's Quantum Random Alphabetic Generator,
        only with lowercase characters, uppercase characters and punctuation.
        """

        assert(len(alphabetic_string) == length_alphabetic_string)
        """
        Assertion for the length of the alphabetic string generated from
        the Qiskrypt's Quantum Random Alphabetic Generator.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_4_qiskrypt_quantum_random_alphabetic_generator_length_20_lowercase(self):
        """
        Test Case #4:

        - Initialise the Qiskrypt's Quantum Random Alphabetic Generator, with a given size of 20,
          and generate a random alphabetic string, only with lowercase characters.

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Quantum Random Alphabetic Generator is initialised, with a size of 20;
        2) The alphabetic string, only with lowercase characters,
           is generated from the Qiskrypt's Quantum Random Alphabetic Generator;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        length_alphabetic_string = 20
        """
        Set the length of the alphabetic string generated from
        the Qiskrypt's Quantum Random Alphabetic Generator, as 20.
        """

        qiskrypt_quantum_random_alphabetic_generator = \
            QiskryptQuantumRandomAlphabeticGenerator("qu_rnd_alpha_gen_4",
                                                     lowercase=True, uppercase=False,
                                                     punctuation=False)
        """
        Create a Qiskrypt's Quantum Random Alphabetic Generator.
        """

        qiskrypt_quantum_random_alphabetic_generator.initiate(length_alphabetic_string)
        """
        Initiate/Configure the previously created Qiskrypt's Quantum Random Alphabetic Generator.
        """

        alphabetic_string = qiskrypt_quantum_random_alphabetic_generator\
            .generate_alphabetic_string()
        """
        Generate the alphabetic string from the Qiskrypt's Quantum Random Alphabetic Generator,
        just for lowercase characters.
        """

        print(f"\n\nTest #4:"
              f"\n - The Alphabetic String generated from "
              f"the Qiskrypt's Quantum Random Alphabetic Generator is:\n"
              f"   [ {alphabetic_string} ]\n"
              f"   (Alphabetic Format with lowercase characters) ;\n")
        """
        Print the resulted alphabetic string of size 20, extracted from
        the Qiskrypt's Quantum Random Alphabetic Generator,
        only with lowercase characters.
        """

        assert(len(alphabetic_string) == length_alphabetic_string)
        """
        Assertion for the length of the alphabetic string generated from
        the Qiskrypt's Quantum Random Alphabetic Generator.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_5_qiskrypt_quantum_random_alphabetic_generator_length_20_lowercase_and_uppercase(self):
        """
        Test Case #5:

        - Initialise the Qiskrypt's Quantum Random Alphabetic Generator, with a given size of 20,
          and generate a random alphabetic string, only with lowercase characters and uppercase characters.

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Quantum Random Alphabetic Generator is initialised, with a size of 20;
        2) The alphabetic string, with lowercase characters and uppercase characters,
           is generated from the Qiskrypt's Quantum Random Alphabetic Generator;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        length_alphabetic_string = 20
        """
        Set the length of the alphabetic string generated from
        the Qiskrypt's Quantum Random Alphabetic Generator, as 20.
        """

        qiskrypt_quantum_random_alphabetic_generator = \
            QiskryptQuantumRandomAlphabeticGenerator("qu_rnd_alpha_gen_5",
                                                     lowercase=True, uppercase=True,
                                                     punctuation=False)
        """
        Create a Qiskrypt's Quantum Random Alphabetic Generator.
        """

        qiskrypt_quantum_random_alphabetic_generator.initiate(length_alphabetic_string)
        """
        Initiate/Configure the previously created Qiskrypt's Quantum Random Alphabetic Generator.
        """

        alphabetic_string = qiskrypt_quantum_random_alphabetic_generator\
            .generate_alphabetic_string()
        """
        Generate the alphabetic string from the Qiskrypt's Quantum Random Alphabetic Generator,
        just for lowercase characters and uppercase characters.
        """

        print(f"\n\nTest #5:"
              f"\n - The Alphabetic String generated from "
              f"the Qiskrypt's Quantum Random Alphabetic Generator is:\n"
              f"   [ {alphabetic_string} ]\n"
              f"   (Alphabetic Format with lowercase characters and uppercase characters) ;\n")
        """
        Print the resulted alphabetic string of size 20, extracted from
        the Qiskrypt's Quantum Random Alphabetic Generator,
        only with lowercase characters and uppercase characters.
        """

        assert(len(alphabetic_string) == length_alphabetic_string)
        """
        Assertion for the length of the alphabetic string generated from
        the Qiskrypt's Quantum Random Alphabetic Generator.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_6_qiskrypt_quantum_random_alphabetic_generator_length_20_lowercase_uppercase_and_punctuation(self):
        """
        Test Case #6:

        - Initialise the Qiskrypt's Quantum Random Alphabetic Generator, with a given size of 20,
          and generate a random alphabetic string, with lowercase characters, uppercase characters
          and punctuation.

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Quantum Random Alphabetic Generator is initialised, with a size of 20;
        2) The alphabetic string, with lowercase characters, uppercase characters and punctuation,
           is generated from the Qiskrypt's Quantum Random Alphabetic Generator;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        length_alphabetic_string = 20
        """
        Set the length of the alphabetic string generated from
        the Qiskrypt's Quantum Random Alphabetic Generator, as 20.
        """

        qiskrypt_quantum_random_alphabetic_generator = \
            QiskryptQuantumRandomAlphabeticGenerator("qu_rnd_alpha_gen_6",
                                                     lowercase=True, uppercase=True,
                                                     punctuation=True)
        """
        Create a Qiskrypt's Quantum Random Alphabetic Generator.
        """

        qiskrypt_quantum_random_alphabetic_generator.initiate(length_alphabetic_string)
        """
        Initiate/Configure the previously created Qiskrypt's Quantum Random Alphabetic Generator.
        """

        alphabetic_string = qiskrypt_quantum_random_alphabetic_generator\
            .generate_alphabetic_string()
        """
        Generate the alphabetic string from the Qiskrypt's Quantum Random Alphabetic Generator,
        just for lowercase characters, uppercase characters and punctuation.
        """

        print(f"\n\nTest #6:"
              f"\n - The Alphabetic String generated from "
              f"the Qiskrypt's Quantum Random Alphabetic Generator is:\n"
              f"   [ {alphabetic_string} ]\n"
              f"   (Alphabetic Format with lowercase characters, uppercase characters and punctuation) ;\n")
        """
        Print the resulted alphabetic string of size 20, extracted from
        the Qiskrypt's Quantum Random Alphabetic Generator,
        only with lowercase characters, uppercase characters and punctuation.
        """

        assert(len(alphabetic_string) == length_alphabetic_string)
        """
        Assertion for the length of the alphabetic string generated from
        the Qiskrypt's Quantum Random Alphabetic Generator.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_7_qiskrypt_quantum_random_alphabetic_generator_length_30_lowercase(self):
        """
        Test Case #7:

        - Initialise the Qiskrypt's Quantum Random Alphabetic Generator, with a given size of 30,
          and generate a random alphabetic string, only with lowercase characters.

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Quantum Random Alphabetic Generator is initialised, with a size of 30;
        2) The alphabetic string, only with lowercase characters,
           is generated from the Qiskrypt's Quantum Random Alphabetic Generator;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        length_alphabetic_string = 30
        """
        Set the length of the alphabetic string generated from
        the Qiskrypt's Quantum Random Alphabetic Generator, as 30.
        """

        qiskrypt_quantum_random_alphabetic_generator = \
            QiskryptQuantumRandomAlphabeticGenerator("qu_rnd_alpha_gen_7",
                                                     lowercase=True, uppercase=False,
                                                     punctuation=False)
        """
        Create a Qiskrypt's Quantum Random Alphabetic Generator.
        """

        qiskrypt_quantum_random_alphabetic_generator.initiate(length_alphabetic_string)
        """
        Initiate/Configure the previously created Qiskrypt's Quantum Random Alphabetic Generator.
        """

        alphabetic_string = qiskrypt_quantum_random_alphabetic_generator\
            .generate_alphabetic_string()
        """
        Generate the alphabetic string from the Qiskrypt's Quantum Random Alphabetic Generator,
        just for lowercase characters.
        """

        print(f"\n\nTest #7:"
              f"\n - The Alphabetic String generated from "
              f"the Qiskrypt's Quantum Random Alphabetic Generator is:\n"
              f"   [ {alphabetic_string} ]\n"
              f"   (Alphabetic Format with lowercase characters) ;\n")
        """
        Print the resulted alphabetic string of size 30, extracted from
        the Qiskrypt's Quantum Random Alphabetic Generator,
        only with lowercase characters.
        """

        assert(len(alphabetic_string) == length_alphabetic_string)
        """
        Assertion for the length of the alphabetic string generated from
        the Qiskrypt's Quantum Random Alphabetic Generator.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_8_qiskrypt_quantum_random_alphabetic_generator_length_30_lowercase_and_uppercase(self):
        """
        Test Case #8:

        - Initialise the Qiskrypt's Quantum Random Alphabetic Generator, with a given size of 30,
          and generate a random alphabetic string, only with lowercase characters and uppercase characters.

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Quantum Random Alphabetic Generator is initialised, with a size of 30;
        2) The alphabetic string, with lowercase characters and uppercase characters,
           is generated from the Qiskrypt's Quantum Random Alphabetic Generator;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        length_alphabetic_string = 30
        """
        Set the length of the alphabetic string generated from
        the Qiskrypt's Quantum Random Alphabetic Generator, as 30.
        """

        qiskrypt_quantum_random_alphabetic_generator = \
            QiskryptQuantumRandomAlphabeticGenerator("qu_rnd_alpha_gen_8",
                                                     lowercase=True, uppercase=True,
                                                     punctuation=False)
        """
        Create a Qiskrypt's Quantum Random Alphabetic Generator.
        """

        qiskrypt_quantum_random_alphabetic_generator.initiate(length_alphabetic_string)
        """
        Initiate/Configure the previously created Qiskrypt's Quantum Random Alphabetic Generator.
        """

        alphabetic_string = qiskrypt_quantum_random_alphabetic_generator\
            .generate_alphabetic_string()
        """
        Generate the alphabetic string from the Qiskrypt's Quantum Random Alphabetic Generator,
        just for lowercase characters and uppercase characters.
        """

        print(f"\n\nTest #8:"
              f"\n - The Alphabetic String generated from "
              f"the Qiskrypt's Quantum Random Alphabetic Generator is:\n"
              f"   [ {alphabetic_string} ]\n"
              f"   (Alphabetic Format with lowercase characters and uppercase characters) ;\n")
        """
        Print the resulted alphabetic string of size 30, extracted from
        the Qiskrypt's Quantum Random Alphabetic Generator,
        only with lowercase characters and uppercase characters.
        """

        assert(len(alphabetic_string) == length_alphabetic_string)
        """
        Assertion for the length of the alphabetic string generated from
        the Qiskrypt's Quantum Random Alphabetic Generator.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_9_qiskrypt_quantum_random_alphabetic_generator_length_30_lowercase_uppercase_and_punctuation(self):
        """
        Test Case #9:

        - Initialise the Qiskrypt's Quantum Random Alphabetic Generator, with a given size of 30,
          and generate a random alphabetic string, with lowercase characters, uppercase characters
          and punctuation.

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Quantum Random Alphabetic Generator is initialised, with a size of 30;
        2) The alphabetic string, with lowercase characters, uppercase characters and punctuation,
           is generated from the Qiskrypt's Quantum Random Alphabetic Generator;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        length_alphabetic_string = 30
        """
        Set the length of the alphabetic string generated from
        the Qiskrypt's Quantum Random Alphabetic Generator, as 30.
        """

        qiskrypt_quantum_random_alphabetic_generator = \
            QiskryptQuantumRandomAlphabeticGenerator("qu_rnd_alpha_gen_9",
                                                     lowercase=True, uppercase=True,
                                                     punctuation=True)
        """
        Create a Qiskrypt's Quantum Random Alphabetic Generator.
        """

        qiskrypt_quantum_random_alphabetic_generator.initiate(length_alphabetic_string)
        """
        Initiate/Configure the previously created Qiskrypt's Quantum Random Alphabetic Generator.
        """

        alphabetic_string = qiskrypt_quantum_random_alphabetic_generator\
            .generate_alphabetic_string()
        """
        Generate the alphabetic string from the Qiskrypt's Quantum Random Alphabetic Generator,
        just for lowercase characters, uppercase characters and punctuation.
        """

        print(f"\n\nTest #9:"
              f"\n - The Alphabetic String generated from "
              f"the Qiskrypt's Quantum Random Alphabetic Generator is:\n"
              f"   [ {alphabetic_string} ]\n"
              f"   (Alphabetic Format with lowercase characters, uppercase characters and punctuation) ;\n")
        """
        Print the resulted alphabetic string of size 30, extracted from
        the Qiskrypt's Quantum Random Alphabetic Generator,
        only with lowercase characters, uppercase characters and punctuation.
        """

        assert(len(alphabetic_string) == length_alphabetic_string)
        """
        Assertion for the length of the alphabetic string generated from
        the Qiskrypt's Quantum Random Alphabetic Generator.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)


if __name__ == "__main__":
    """
    The Main Method for the Unitary Test.
    """

    qiskrypt_quantum_random_alphabetic_generator_test_cases = \
        TestLoader().loadTestsFromTestCase(QiskryptQuantumRandomAlphabeticGeneratorTests)
    """
    Load the Test Cases from the Unitary Tests for the Qiskrypt's Quantum Random Alphabetic Generator.
    """

    qiskrypt_quantum_random_alphabetic_generator_test_suite = \
        TestSuite([qiskrypt_quantum_random_alphabetic_generator_test_cases])
    """
    Load the Test Suite with all the Test Cases for the Qiskrypt's Quantum Random Alphabetic Generator.
    """
