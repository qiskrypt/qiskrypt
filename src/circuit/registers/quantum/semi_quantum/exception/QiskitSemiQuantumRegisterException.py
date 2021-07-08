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
- Security and Quantum Information Group, Portugal.
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

MESSAGE_UNSUPPORTED_OPERATIONS_EXCEPTION = "Unsupported operation for the Semi-Quantum Registers...\n"\
                                           "The Semi-Quantum Registers only supports the operations:\n" \
                                           "   (i)            Z-MEASUREMENT: Measurement of the Qubit in Computational Basis.\n" \
                                           "  (ii)                  REFLECT: Reflection of the Qubit.\n" \
                                           " (iii) CLASSICAL-STATE-CREATION: Creation of a Qubit in a Classical State.\n"
"""
The custom defined message for the Unsupported Operation Error for
the IBM's Qiskit Semi-Quantum Register.
"""


class QiskitSemiQuantumRegisterUnsupportedOperationError(Exception):
    """
    Object Class of the Unsupported Operation Error for
    the IBM's Qiskit Semi-Quantum Register.
    """

    def __init__(self, message=MESSAGE_UNSUPPORTED_OPERATIONS_EXCEPTION):
        """
        Constructor for the Unsupported Operation Error for
        the IBM's Qiskit Semi-Quantum Register.
        :param message: The custom message for the Unsupported Operation Error for
                        the IBM's Qiskit Semi-Quantum Register.
        """
        self.message = message
        """
        Set the custom message for the Unsupported Operation Error for
        the IBM's Qiskit Semi-Quantum Register.
        """

        super().__init__(self.message)
        """
        Calls the constructor of the super-class Exception.
        """
