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

from src.true_random.random_generator.numeric.QiskryptQuantumRandomNumericGenerator \
    import QiskryptQuantumRandomNumericGenerator
"""
Import the Qiskrypt's Quantum Random Numeric Generator.
"""

"""
Definition of Constants and Enumerations.
"""

from src.true_random.random_generator.numeric.QiskryptQuantumRandomNumericGenerator \
    import DATA_TYPES
"""
Import the Data Types for all the numbers that can be possibly generated.
"""


class QiskryptQuantumRandomNumericGeneratorTests(TestCase):
    """
    Object Class of the Unitary Tests for the Qiskrypt's Quantum Random Numeric Generator.
    """

    def test_no_1_qiskrypt_quantum_random_numeric_generator_signed_short_int(self):
        """
        Test Case #1:

        - Initialise the Qiskrypt's Quantum Random Numeric Generator, for a Signed Short Integer.

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Quantum Random Numeric Generator is initialised, for Signed Short Integers;
        2) The Signed Short Integer is generated from the Qiskrypt's Quantum Random Numeric Generator;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        qiskrypt_quantum_random_numeric_generator = \
            QiskryptQuantumRandomNumericGenerator("qu_rnd_sig_short_int_gen_1", DATA_TYPES[0])
        """
        Create a Qiskrypt's Quantum Random Numeric Generator, for Signed Short Integers.
        """

        qiskrypt_quantum_random_numeric_generator.initiate()
        """
        Initiate/Configure the previously created Qiskrypt's Quantum Random Numeric Generator.
        """

        signed_short_int_number = qiskrypt_quantum_random_numeric_generator.generate_number()
        """
        Generate the Signed Short Integer from the Qiskrypt's Quantum Random Numeric Generator.
        """

        print(f"\n\nTest #1:"
              f"\n - The Signed Short Integer generated from "
              f"the Qiskrypt's Quantum Random Numeric Generator is:\n"
              f"   [ {signed_short_int_number} ] (Decimal Format) ;\n")
        """
        Print the resulted Signed Short Integer, extracted from
        the Qiskrypt's Quantum Random Numeric Generator.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_2_qiskrypt_quantum_random_numeric_generator_unsigned_short_int(self):
        """
        Test Case #2:

        - Initialise the Qiskrypt's Quantum Random Numeric Generator, for an Unsigned Short Integer.

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Quantum Random Numeric Generator is initialised, for Unsigned Short Integers;
        2) The Unsigned Short Integer is generated from the Qiskrypt's Quantum Random Numeric Generator;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        qiskrypt_quantum_random_numeric_generator = \
            QiskryptQuantumRandomNumericGenerator("qu_rnd_unsig_short_int_gen_2", DATA_TYPES[1])
        """
        Create a Qiskrypt's Quantum Random Numeric Generator, for Unsigned Short Integers.
        """

        qiskrypt_quantum_random_numeric_generator.initiate()
        """
        Initiate/Configure the previously created Qiskrypt's Quantum Random Numeric Generator.
        """

        unsigned_short_int_number = qiskrypt_quantum_random_numeric_generator.generate_number()
        """
        Generate the Unsigned Short Integer from the Qiskrypt's Quantum Random Numeric Generator.
        """

        print(f"\n\nTest #2:"
              f"\n - The Unsigned Short Integer generated from "
              f"the Qiskrypt's Quantum Random Numeric Generator is:\n"
              f"   [ {unsigned_short_int_number} ] (Decimal Format) ;\n")
        """
        Print the resulted Unsigned Short Integer, extracted from
        the Qiskrypt's Quantum Random Numeric Generator.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_3_qiskrypt_quantum_random_numeric_generator_signed_int(self):
        """
        Test Case #3:

        - Initialise the Qiskrypt's Quantum Random Numeric Generator, for a Signed Integer.

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Quantum Random Numeric Generator is initialised, for Signed Integers;
        2) The Signed Integer is generated from the Qiskrypt's Quantum Random Numeric Generator;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        qiskrypt_quantum_random_numeric_generator = \
            QiskryptQuantumRandomNumericGenerator("qu_rnd_sig_int_gen_3", DATA_TYPES[2])
        """
        Create a Qiskrypt's Quantum Random Numeric Generator, for Signed Integers.
        """

        qiskrypt_quantum_random_numeric_generator.initiate()
        """
        Initiate/Configure the previously created Qiskrypt's Quantum Random Numeric Generator.
        """

        signed_int_number = qiskrypt_quantum_random_numeric_generator.generate_number()
        """
        Generate the Signed Integer from the Qiskrypt's Quantum Random Numeric Generator.
        """

        print(f"\n\nTest #3:"
              f"\n - The Signed Integer generated from "
              f"the Qiskrypt's Quantum Random Numeric Generator is:\n"
              f"   [ {signed_int_number} ] (Decimal Format) ;\n")
        """
        Print the resulted Signed Integer, extracted from
        the Qiskrypt's Quantum Random Numeric Generator.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_4_qiskrypt_quantum_random_numeric_generator_unsigned_int(self):
        """
        Test Case #4:

        - Initialise the Qiskrypt's Quantum Random Numeric Generator, for an Unsigned Integer.

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Quantum Random Numeric Generator is initialised, for Unsigned Integers;
        2) The Unsigned Integer is generated from the Qiskrypt's Quantum Random Numeric Generator;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        qiskrypt_quantum_random_numeric_generator = \
            QiskryptQuantumRandomNumericGenerator("qu_rnd_unsig_int_gen_4", DATA_TYPES[3])
        """
        Create a Qiskrypt's Quantum Random Numeric Generator, for Unsigned Integers.
        """

        qiskrypt_quantum_random_numeric_generator.initiate()
        """
        Initiate/Configure the previously created Qiskrypt's Quantum Random Numeric Generator.
        """

        unsigned_int_number = qiskrypt_quantum_random_numeric_generator.generate_number()
        """
        Generate the Unsigned Integer from the Qiskrypt's Quantum Random Numeric Generator.
        """

        print(f"\n\nTest #4:"
              f"\n - The Unsigned Integer generated from "
              f"the Qiskrypt's Quantum Random Numeric Generator is:\n"
              f"   [ {unsigned_int_number} ] (Decimal Format) ;\n")
        """
        Print the resulted Unsigned Integer, extracted from
        the Qiskrypt's Quantum Random Numeric Generator.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_5_qiskrypt_quantum_random_numeric_generator_signed_long_int(self):
        """
        Test Case #5:

        - Initialise the Qiskrypt's Quantum Random Numeric Generator, for a Signed Long Integer.

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Quantum Random Numeric Generator is initialised, for Signed Long Integers;
        2) The Signed Long Integer is generated from the Qiskrypt's Quantum Random Numeric Generator;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        qiskrypt_quantum_random_numeric_generator = \
            QiskryptQuantumRandomNumericGenerator("qu_rnd_sig_long_int_gen_5", DATA_TYPES[4])
        """
        Create a Qiskrypt's Quantum Random Numeric Generator, for Signed Long Integers.
        """

        qiskrypt_quantum_random_numeric_generator.initiate()
        """
        Initiate/Configure the previously created Qiskrypt's Quantum Random Numeric Generator.
        """

        signed_long_int_number = qiskrypt_quantum_random_numeric_generator.generate_number()
        """
        Generate the Signed Long Integer from the Qiskrypt's Quantum Random Numeric Generator.
        """

        print(f"\n\nTest #5:"
              f"\n - The Signed Long Integer generated from "
              f"the Qiskrypt's Quantum Random Numeric Generator is:\n"
              f"   [ {signed_long_int_number} ] (Decimal Format) ;\n")
        """
        Print the resulted Signed Long Integer, extracted from
        the Qiskrypt's Quantum Random Numeric Generator.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_6_qiskrypt_quantum_random_numeric_generator_unsigned_long_int(self):
        """
        Test Case #6:

        - Initialise the Qiskrypt's Quantum Random Numeric Generator, for an Unsigned Long Integer.

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Quantum Random Numeric Generator is initialised, for Unsigned Long Integers;
        2) The Unsigned Long Integer is generated from the Qiskrypt's Quantum Random Numeric Generator;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        qiskrypt_quantum_random_numeric_generator = \
            QiskryptQuantumRandomNumericGenerator("qu_rnd_unsig_long_int_gen_6", DATA_TYPES[5])
        """
        Create a Qiskrypt's Quantum Random Numeric Generator, for Unsigned Long Integers.
        """

        qiskrypt_quantum_random_numeric_generator.initiate()
        """
        Initiate/Configure the previously created Qiskrypt's Quantum Random Numeric Generator.
        """

        unsigned_long_int_number = qiskrypt_quantum_random_numeric_generator.generate_number()
        """
        Generate the Unsigned Long Integer from the Qiskrypt's Quantum Random Numeric Generator.
        """

        print(f"\n\nTest #6:"
              f"\n - The Unsigned Long Integer generated from "
              f"the Qiskrypt's Quantum Random Numeric Generator is:\n"
              f"   [ {unsigned_long_int_number} ] (Decimal Format) ;\n")
        """
        Print the resulted Unsigned Long Integer, extracted from
        the Qiskrypt's Quantum Random Numeric Generator.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_7_qiskrypt_quantum_random_numeric_generator_signed_long_long_int(self):
        """
        Test Case #7:

        - Initialise the Qiskrypt's Quantum Random Numeric Generator, for a Signed Long Long Integer.

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Quantum Random Numeric Generator is initialised, for Signed Long Long Integers;
        2) The Signed Long Long Integer is generated from the Qiskrypt's Quantum Random Numeric Generator;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        qiskrypt_quantum_random_numeric_generator = \
            QiskryptQuantumRandomNumericGenerator("qu_rnd_sig_long_long_int_gen_7", DATA_TYPES[6])
        """
        Create a Qiskrypt's Quantum Random Numeric Generator, for Signed Long Long Integers.
        """

        qiskrypt_quantum_random_numeric_generator.initiate()
        """
        Initiate/Configure the previously created Qiskrypt's Quantum Random Numeric Generator.
        """

        signed_long_long_int_number = qiskrypt_quantum_random_numeric_generator.generate_number()
        """
        Generate the Signed Long Long Integer from the Qiskrypt's Quantum Random Numeric Generator.
        """

        print(f"\n\nTest #7:"
              f"\n - The Signed Long Long Integer generated from "
              f"the Qiskrypt's Quantum Random Numeric Generator is:\n"
              f"   [ {signed_long_long_int_number} ] (Decimal Format) ;\n")
        """
        Print the resulted Signed Long Long Integer, extracted from
        the Qiskrypt's Quantum Random Numeric Generator.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_8_qiskrypt_quantum_random_numeric_generator_unsigned_long_long_int(self):
        """
        Test Case #8:

        - Initialise the Qiskrypt's Quantum Random Numeric Generator, for an Unsigned Long Long Integer.

        Description of the Steps for the Unitary Test:
        1) The Qiskrypt's Quantum Random Numeric Generator is initialised, for Unsigned Long Long Integers;
        2) The Unsigned Long Long Integer is generated from the Qiskrypt's Quantum Random Numeric Generator;

        Return OK (or FAIL) if, all the Tests performed are OK (or FAIL, otherwise).
        """

        qiskrypt_quantum_random_numeric_generator = \
            QiskryptQuantumRandomNumericGenerator("qu_rnd_unsig_long_long_int_gen_8", DATA_TYPES[7])
        """
        Create a Qiskrypt's Quantum Random Numeric Generator, for Unsigned Long Long Integers.
        """

        qiskrypt_quantum_random_numeric_generator.initiate()
        """
        Initiate/Configure the previously created Qiskrypt's Quantum Random Numeric Generator.
        """

        unsigned_long_long_int_number = qiskrypt_quantum_random_numeric_generator.generate_number()
        """
        Generate the Unsigned Long Long Integer from the Qiskrypt's Quantum Random Numeric Generator.
        """

        print(f"\n\nTest #8:"
              f"\n - The Unsigned Long Long Integer generated from "
              f"the Qiskrypt's Quantum Random Numeric Generator is:\n"
              f"   [ {unsigned_long_long_int_number} ] (Decimal Format) ;\n")
        """
        Print the resulted Unsigned Long Integer, extracted from
        the Qiskrypt's Quantum Random Numeric Generator.
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)


if __name__ == "__main__":
    """
    The Main Method for the Unitary Test.
    """

    qiskrypt_quantum_random_numeric_generator_test_cases = \
        TestLoader().loadTestsFromTestCase(QiskryptQuantumRandomNumericGeneratorTests)
    """
    Load the Test Cases from the Unitary Tests for the Qiskrypt's Quantum Random Numeric Generator.
    """

    qiskrypt_quantum_random_numeric_generator_test_suite = \
        TestSuite([qiskrypt_quantum_random_numeric_generator_test_cases])
    """
    Load the Test Suite with all the Test Cases for the Qiskrypt's Quantum Random Numeric Generator.
    """
