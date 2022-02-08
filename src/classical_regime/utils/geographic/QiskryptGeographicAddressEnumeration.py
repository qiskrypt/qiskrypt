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
- NOVA LINCS, Portugal.
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

from enum import Enum as Enumeration
"""
Import the Enum Class from the enum module of the Python's Library.
"""


class QiskryptGeographicAddressEnumeration(Enumeration):
    """
    Object class for the Qiskrypt's Geographic Address Enumeration.
    """

    """
    A. Addresses in Portugal
    """

    """
    1) Colleges in Lisbon, Portugal.
    """

    NOVA_SCHOOL_OF_SCIENCE_AND_TECHNOLOGY_PORTUGAL = \
        "NOVA School of Science and Technology, Portugal"
    """
    The short address of 'NOVA School of Science and Technology, Portugal'.
    """

    INSTITUTO_SUPERIOR_TECNICO_PORTUGAL = \
        "Instituto Superior Tecnico, Portugal"
    """
    The short address of 'Instituto Superior Tecnico, Portugal'.
    """

    FACULTY_SCIENCES_OF_UNIVERSITY_OF_LISBON_PORTUGAL = \
        "Faculdade de Ciencias da Universidade de Lisboa, Portugal"
    """
    The short address of 'Faculdade de Ciencias da Universidade de Lisboa, Portugal'.
    """

    ISEL_INSTITUTO_SUPERIOR_DE_ENGENHARIA_DE_LISBOA_PORTUGAL = \
        "Instituto Superior de Engenharia de Lisboa, Portugal"
    """
    The short address of 'Instituto Superior de Engenharia de Lisboa, Portugal'.
    """

    ISCTE_INSTITUTO_UNIVERSITARIO_DE_LISBOA_PORTUGAL = \
        "Instituto Universitario de Lisboa, Portugal"
    """
    The short address of 'ISCTE - Instituto Universitario de Lisboa, Portugal'.
    """

    """
    2) Colleges in Porto, Portugal.
    """

    FACULTY_ENGINEERING_OF_UNIVERSITY_OF_PORTO_PORTUGAL = \
        "Faculdade de Engenharia da Universidade do Porto, Portugal"
    """
    The short address of 'Faculdade de Engenharia da Universidade do Porto, Portugal'.
    """

    FACULTY_SCIENCES_OF_UNIVERSITY_OF_PORTO_PORTUGAL = \
        "Faculdade de Ciencias da Universidade do Porto, Portugal"
    """
    The short address of 'Faculdade de Ciencias da Universidade do Porto, Portugal'.
    """

    ISEP_INSTITUTO_SUPERIOR_DE_ENGENHARIA_DO_PORTO_PORTUGAL = \
        "Instituto Superior de Engenharia do Porto, Portugal"
    """
    The short address of 'ISEP - Instituto Superior de Engenharia do Porto, Portugal'.
    """
