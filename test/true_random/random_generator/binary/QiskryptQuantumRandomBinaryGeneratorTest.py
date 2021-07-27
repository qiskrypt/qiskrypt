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


class QiskryptQuantumRandomBinaryGeneratorTests(TestCase):
    """
    Object Class of the Unitary Tests for the Qiskrypt's Quantum Random Binary Generator.
    """

    def test_no_1_qiskrypt_quantum_random_binary_generator_tests_length_10(self):
        """


        :return:
        """

        length_binary_string = 10
        """
        
        """

        qiskrypt_quantum_random_binary_generator = \
            QiskryptQuantumRandomBinaryGenerator("qu_rnd_bin_gen_1")
        """
        
        """

        qiskrypt_quantum_random_binary_generator.configure(length_binary_string)
        """
        
        """

        binary_string = qiskrypt_quantum_random_binary_generator.generate_binary_string()
        """
        
        """

        print(f"\n\nTest #1:"
              f"\n - The Binary String generated from "
              f"the Qiskrypt's Quantum Random Binary Generator is:\n"
              f"   [ {binary_string} ] (Binary Format) ;\n")
        """
        
        """

        assert(len(binary_string) == (length_binary_string + 2))
        """
        
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_2_qiskrypt_quantum_random_binary_generator_tests_length_20(self):
        """


        :return:
        """

        length_binary_string = 20
        """

        """

        qiskrypt_quantum_random_binary_generator = \
            QiskryptQuantumRandomBinaryGenerator("qu_rnd_bin_gen_2")
        """

        """

        qiskrypt_quantum_random_binary_generator.configure(length_binary_string)
        """

        """

        binary_string = qiskrypt_quantum_random_binary_generator.generate_binary_string()
        """

        """

        print(f"\n\nTest #2:"
              f"\n - The Binary String generated from "
              f"the Qiskrypt's Quantum Random Binary Generator is:\n"
              f"   [ {binary_string} ] (Binary Format) ;\n")
        """

        """

        assert (len(binary_string) == (length_binary_string + 2))
        """

        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_3_qiskrypt_quantum_random_binary_generator_tests_length_40(self):
        """


        :return:
        """

        length_binary_string = 40
        """
        
        """

        qiskrypt_quantum_random_binary_generator = \
            QiskryptQuantumRandomBinaryGenerator("qu_rnd_bin_gen_3")
        """
        
        """

        qiskrypt_quantum_random_binary_generator.configure(length_binary_string)
        """
        
        """

        binary_string = qiskrypt_quantum_random_binary_generator.generate_binary_string()
        """
        
        """

        print(f"\n\nTest #3:"
              f"\n - The Binary String generated from "
              f"the Qiskrypt's Quantum Random Binary Generator is:\n"
              f"   [ {binary_string} ] (Binary Format) ;\n")
        """
        
        """

        assert(len(binary_string) == (length_binary_string + 2))
        """
        
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_4_qiskrypt_quantum_random_binary_generator_tests_length_80(self):
        """


        :return:
        """

        length_binary_string = 80
        """
        
        """

        qiskrypt_quantum_random_binary_generator = \
            QiskryptQuantumRandomBinaryGenerator("qu_rnd_bin_gen_4")
        """
        
        """

        qiskrypt_quantum_random_binary_generator.configure(length_binary_string)
        """
        
        """

        binary_string = qiskrypt_quantum_random_binary_generator.generate_binary_string()
        """
        
        """

        print(f"\n\nTest #4:"
              f"\n - The Binary String generated from "
              f"the Qiskrypt's Quantum Random Binary Generator is:\n"
              f"   [ {binary_string} ] (Binary Format) ;\n")
        """
        
        """

        assert(len(binary_string) == (length_binary_string + 2))
        """
        
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_5_qiskrypt_quantum_random_binary_generator_tests_length_120(self):
        """


        :return:
        """

        length_binary_string = 120
        """
        
        """

        qiskrypt_quantum_random_binary_generator = \
            QiskryptQuantumRandomBinaryGenerator("qu_rnd_bin_gen_5")
        """
        
        """

        qiskrypt_quantum_random_binary_generator.configure(length_binary_string)
        """
        
        """

        binary_string = qiskrypt_quantum_random_binary_generator.generate_binary_string()
        """
        
        """

        print(f"\n\nTest #5:"
              f"\n - The Binary String generated from "
              f"the Qiskrypt's Quantum Random Binary Generator is:\n"
              f"   [ {binary_string} ] (Binary Format) ;\n")
        """
        
        """

        assert(len(binary_string) == (length_binary_string + 2))
        """
        
        """

        """
        Dummy Assert Equal for the Unittest.
        """
        self.assertEqual(True, True)

    def test_no_6_qiskrypt_quantum_random_binary_generator_tests_length_260(self):
        """


        :return:
        """

        length_binary_string = 260
        """
        
        """

        qiskrypt_quantum_random_binary_generator = \
            QiskryptQuantumRandomBinaryGenerator("qu_rnd_bin_gen_6")
        """
        
        """

        qiskrypt_quantum_random_binary_generator.configure(length_binary_string)
        """
        
        """

        binary_string = qiskrypt_quantum_random_binary_generator.generate_binary_string()
        """
        
        """

        print(f"\n\nTest #6:"
              f"\n - The Binary String generated from "
              f"the Qiskrypt's Quantum Random Binary Generator is:\n"
              f"   [ {binary_string} ] (Binary Format) ;\n")
        """
        
        """

        assert(len(binary_string) == (length_binary_string + 2))
        """
        
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