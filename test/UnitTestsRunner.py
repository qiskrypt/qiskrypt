"""

Copyrights:\n
- © Qiskrypt, 2022 - All rights reserved.\n

Powered by:\n
- IBM
- IBM Quantum
- IBM Qiskit


Description:\n
- The Qiskrypt is a software suite of protocols of
  quantum cryptography, quantum_regime communication and
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

from unittest import TestLoader, TextTestRunner
"""
Import TestLoader and TextTestRunner from Unittest.
"""


"""
Import required Constants and Enumerations.
"""

UNITARY_TESTS_ROOT_FOLDER = "./"
"""
The root folder for the Unitary Tests.
"""

UNITARY_TESTS_FILES_PATTERN = "*Test.py"
"""
The pattern to be used in the Discovery method of the Unitary Tests files.
"""

VERBOSITY_TEST_RUNNER_FLAG = 1
"""
The Flag for the Verbosity parameter of the Test Runner of the Unitary Tests files.
"""


def run_unit_tests():
    """
    Method to run all the Unitary Tests, available in the root folder,
    extracted from the Discovery method, providing also their final results.
    """

    unitary_tests_suite = TestLoader().discover(UNITARY_TESTS_ROOT_FOLDER,
                                                pattern=UNITARY_TESTS_FILES_PATTERN)
    """
    Call the Discovery method to extract all the Unitary Tests, available in the root folder.
    """

    tests_results = TextTestRunner(verbosity=VERBOSITY_TEST_RUNNER_FLAG).run(unitary_tests_suite)
    """
    Run all the
    """

    if (tests_results.errors is True) or (tests_results.failures is True):
        """
        If occurred some error or failure during the running of
        all the Unitary Tests extracted from the Discovery method.
        """

        exit(1)
        """
        Exiting with code "1", since happened some issue, error or problem.
        """

    else:
        """
        If does not occurred no error or failure during the running of
        all the Unitary Tests extracted from the Discovery method. 
        """

        exit(0)
        """
        Exiting with code "0", since does not happened no issue, error or problem.
        """


if __name__ == '__main__':
    """
    The Main Method for the Unitary Tests Runner.
    """

    run_unit_tests()
    """
    Run all the Unitary Tests, available in the root folder,
    extracted from the Discovery method, providing also their final results.
    """
