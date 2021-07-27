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

from src.true_random.random_generator.binary.QiskryptQuantumRandomBinaryGenerator import \
    QiskryptQuantumRandomBinaryGenerator
"""
Import the Qiskrypt's Quantum Random Binary Generator.
"""


class QiskryptQuantumRandomBinaryGeneratorTests(TestCase):
    """
    Object Class of the Unitary Tests for the Qiskrypt's Quantum Random Binary Generator.
    """

    def test_no_1_qiskrypt_quantum_random_binary_generator_tests_length_10(self):
        """
        Test Case #1:

        - Initialise the Qiskrypt's Quantum Random Binary Generator, with a given size of 10,
          and generate a random binary string.

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Quantum Random Binary Generator is initialised, with a size of 10;
        2) The binary string is generated from the Qiskrypt's Quantum Random Binary Generator;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        length_binary_string = 10
        """
        Set the length of the binary string generated from
        the Qiskrypt's Quantum Random Binary Generator, as 10.
        """

        qiskrypt_quantum_random_binary_generator = \
            QiskryptQuantumRandomBinaryGenerator("qu_rnd_bin_gen_1")
        """
        Create a Qiskrypt's Quantum Random Binary Generator.
        """

        qiskrypt_quantum_random_binary_generator.configure(length_binary_string)
        """
        Configure the previously created Qiskrypt's Quantum Random Binary Generator.
        """

        binary_string = qiskrypt_quantum_random_binary_generator.generate_binary_string()
        """
        Generate the binary string from the Qiskrypt's Quantum Random Binary Generator.
        """

        print(f"\n\nTest #1:"
              f"\n - The Binary String generated from "
              f"the Qiskrypt's Quantum Random Binary Generator is:\n"
              f"   [ {binary_string} ] (Binary Format) ;\n")
        """
        Print the resulted binary string of size 10, extracted from
        the Qiskrypt's Quantum Random Binary Generator.
        """

        assert(len(binary_string) == (length_binary_string + 2))
        """
        Assertion for the length of the binary string generated from
        the Qiskrypt's Quantum Random Binary Generator, considering '0b' binary prefix.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_2_qiskrypt_quantum_random_binary_generator_tests_length_20(self):
        """
        Test Case #2:

        - Initialise the Qiskrypt's Quantum Random Binary Generator, with a given size of 20,
          and generate a random binary string.

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Quantum Random Binary Generator is initialised, with a size of 20;
        2) The binary string is generated from the Qiskrypt's Quantum Random Binary Generator;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        length_binary_string = 20
        """
        Set the length of the binary string generated from
        the Qiskrypt's Quantum Random Binary Generator, as 20.
        """

        qiskrypt_quantum_random_binary_generator = \
            QiskryptQuantumRandomBinaryGenerator("qu_rnd_bin_gen_2")
        """
        Create a Qiskrypt's Quantum Random Binary Generator.
        """

        qiskrypt_quantum_random_binary_generator.configure(length_binary_string)
        """
        Configure the previously created Qiskrypt's Quantum Random Binary Generator.
        """

        binary_string = qiskrypt_quantum_random_binary_generator.generate_binary_string()
        """
        Generate the binary string from the Qiskrypt's Quantum Random Binary Generator.
        """

        print(f"\n\nTest #2:"
              f"\n - The Binary String generated from "
              f"the Qiskrypt's Quantum Random Binary Generator is:\n"
              f"   [ {binary_string} ] (Binary Format) ;\n")
        """
        Print the resulted binary string of size 20, extracted from
        the Qiskrypt's Quantum Random Binary Generator.
        """

        assert (len(binary_string) == (length_binary_string + 2))
        """
        Assertion for the length of the binary string generated from
        the Qiskrypt's Quantum Random Binary Generator, considering '0b' binary prefix.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_3_qiskrypt_quantum_random_binary_generator_tests_length_40(self):
        """
        Test Case #3:

        - Initialise the Qiskrypt's Quantum Random Binary Generator, with a given size of 40,
          and generate a random binary string.

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Quantum Random Binary Generator is initialised, with a size of 40;
        2) The binary string is generated from the Qiskrypt's Quantum Random Binary Generator;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        length_binary_string = 40
        """
        Set the length of the binary string generated from
        the Qiskrypt's Quantum Random Binary Generator, as 40.        
        """

        qiskrypt_quantum_random_binary_generator = \
            QiskryptQuantumRandomBinaryGenerator("qu_rnd_bin_gen_3")
        """
        Create a Qiskrypt's Quantum Random Binary Generator.
        """

        qiskrypt_quantum_random_binary_generator.configure(length_binary_string)
        """
        Configure the previously created Qiskrypt's Quantum Random Binary Generator.
        """

        binary_string = qiskrypt_quantum_random_binary_generator.generate_binary_string()
        """
        Generate the binary string from the Qiskrypt's Quantum Random Binary Generator.
        """

        print(f"\n\nTest #3:"
              f"\n - The Binary String generated from "
              f"the Qiskrypt's Quantum Random Binary Generator is:\n"
              f"   [ {binary_string} ] (Binary Format) ;\n")
        """
        Print the resulted binary string of size 40, extracted from
        the Qiskrypt's Quantum Random Binary Generator.
        """

        assert(len(binary_string) == (length_binary_string + 2))
        """
        Assertion for the length of the binary string generated from
        the Qiskrypt's Quantum Random Binary Generator, considering '0b' binary prefix.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_4_qiskrypt_quantum_random_binary_generator_tests_length_80(self):
        """
        Test Case #4:

        - Initialise the Qiskrypt's Quantum Random Binary Generator, with a given size of 80,
          and generate a random binary string.

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Quantum Random Binary Generator is initialised, with a size of 80;
        2) The binary string is generated from the Qiskrypt's Quantum Random Binary Generator;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        length_binary_string = 80
        """
        Set the length of the binary string generated from
        the Qiskrypt's Quantum Random Binary Generator, as 80.        
        """

        qiskrypt_quantum_random_binary_generator = \
            QiskryptQuantumRandomBinaryGenerator("qu_rnd_bin_gen_4")
        """
        Create a Qiskrypt's Quantum Random Binary Generator.
        """

        qiskrypt_quantum_random_binary_generator.configure(length_binary_string)
        """
        Configure the previously created Qiskrypt's Quantum Random Binary Generator.        
        """

        binary_string = qiskrypt_quantum_random_binary_generator.generate_binary_string()
        """
        Generate the binary string from the Qiskrypt's Quantum Random Binary Generator.        
        """

        print(f"\n\nTest #4:"
              f"\n - The Binary String generated from "
              f"the Qiskrypt's Quantum Random Binary Generator is:\n"
              f"   [ {binary_string} ] (Binary Format) ;\n")
        """
        Print the resulted binary string of size 80, extracted from
        the Qiskrypt's Quantum Random Binary Generator.        
        """

        assert(len(binary_string) == (length_binary_string + 2))
        """
        Assertion for the length of the binary string generated from
        the Qiskrypt's Quantum Random Binary Generator, considering '0b' binary prefix.        
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_5_qiskrypt_quantum_random_binary_generator_tests_length_120(self):
        """
        Test Case #5:

        - Initialise the Qiskrypt's Quantum Random Binary Generator, with a given size of 120,
          and generate a random binary string.

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Quantum Random Binary Generator is initialised, with a size of 120;
        2) The binary string is generated from the Qiskrypt's Quantum Random Binary Generator;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        length_binary_string = 120
        """
        Set the length of the binary string generated from
        the Qiskrypt's Quantum Random Binary Generator, as 120.
        """

        qiskrypt_quantum_random_binary_generator = \
            QiskryptQuantumRandomBinaryGenerator("qu_rnd_bin_gen_5")
        """
        Create a Qiskrypt's Quantum Random Binary Generator.
        """

        qiskrypt_quantum_random_binary_generator.configure(length_binary_string)
        """
        Configure the previously created Qiskrypt's Quantum Random Binary Generator.        
        """

        binary_string = qiskrypt_quantum_random_binary_generator.generate_binary_string()
        """
        Generate the binary string from the Qiskrypt's Quantum Random Binary Generator.
        """

        print(f"\n\nTest #5:"
              f"\n - The Binary String generated from "
              f"the Qiskrypt's Quantum Random Binary Generator is:\n"
              f"   [ {binary_string} ] (Binary Format) ;\n")
        """
        Print the resulted binary string of size 120, extracted from
        the Qiskrypt's Quantum Random Binary Generator.
        """

        assert(len(binary_string) == (length_binary_string + 2))
        """
        Assertion for the length of the binary string generated from
        the Qiskrypt's Quantum Random Binary Generator, considering '0b' binary prefix.        
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_6_qiskrypt_quantum_random_binary_generator_tests_length_260(self):
        """
        Test Case #6:

        - Initialise the Qiskrypt's Quantum Random Binary Generator, with a given size of 260,
          and generate a random binary string.

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Quantum Random Binary Generator is initialised, with a size of 260;
        2) The binary string is generated from the Qiskrypt's Quantum Random Binary Generator;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        length_binary_string = 260
        """
        Set the length of the binary string generated from
        the Qiskrypt's Quantum Random Binary Generator, as 260.
        """

        qiskrypt_quantum_random_binary_generator = \
            QiskryptQuantumRandomBinaryGenerator("qu_rnd_bin_gen_6")
        """
        Create a Qiskrypt's Quantum Random Binary Generator.        
        """

        qiskrypt_quantum_random_binary_generator.configure(length_binary_string)
        """
        Configure the previously created Qiskrypt's Quantum Random Binary Generator.        
        """

        binary_string = qiskrypt_quantum_random_binary_generator.generate_binary_string()
        """
        Generate the binary string from the Qiskrypt's Quantum Random Binary Generator.
        """

        print(f"\n\nTest #6:"
              f"\n - The Binary String generated from "
              f"the Qiskrypt's Quantum Random Binary Generator is:\n"
              f"   [ {binary_string} ] (Binary Format) ;\n")
        """
        Print the resulted binary string of size 260, extracted from
        the Qiskrypt's Quantum Random Binary Generator.
        """

        assert(len(binary_string) == (length_binary_string + 2))
        """
        Assertion for the length of the binary string generated from
        the Qiskrypt's Quantum Random Binary Generator, considering '0b' binary prefix.        
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)


if __name__ == "__main__":
    """
    The Main Method for the Unitary Test.
    """

    qiskrypt_quantum_random_binary_generator_test_cases = \
        TestLoader().loadTestsFromTestCase(QiskryptQuantumRandomBinaryGeneratorTests)
    """
    Load the Test Cases from the Unitary Tests for the Qiskrypt's Quantum Random Binary Generator.
    """

    qiskrypt_quantum_random_binary_generator_test_suite = \
        TestSuite([qiskrypt_quantum_random_binary_generator_test_cases])
    """
    Load the Test Suite with all the Test Cases for the Qiskrypt's Quantum Random Binary Generator.
    """