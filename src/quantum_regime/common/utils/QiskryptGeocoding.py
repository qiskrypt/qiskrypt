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

from geopy.geocoders import get_geocoder_for_service
"""
Import the function which tries to return a Geocoder Class from GeoPy,
for the name of the service provided.
"""

from inspect import getfullargspec as get_full_arguments_specifications
"""
Import the method to get the full arguments' specifications from the inspection module.
"""


"""
Auxiliary methods.
"""


def get_geocoder_service_by_name(geocoder_service_name: str):
    """
    Return the Geocoder Service, from the given name of a Geocoder Service.

    :param geocoder_service_name: the name of the Geocoder Service to be found.

    :return get_geocoder_for_service(geocoder_service_name.lower()): the Geocoder Service, from the given name of
                                                                     a Geocoder Service.
    """

    if geocoder_service_name.upper() in POSSIBLE_GEOCODER_SERVICE_NAMES:
        """
        If the given name of a Geocoder Service is valid.
        """

        """
        Return the Geocoder Service, from the given name of a Geocoder Service.
        """
        return get_geocoder_for_service(geocoder_service_name.lower())

    else:
        """
        If the given name of a Geocoder Service is not valid.
        """

        # TODO Throw - Exception


def get_all_available_geocoder_services() -> list:
    """
    Return a list with all the available Geocoder Services for the Qiskrypt's Geocoding.

    :return all_geocoder_services_list: the list for all the available Geocoder Services for
                                        the Qiskrypt's Geocoding.
    """

    all_geocoder_services_list = list()
    """
    Initialise an empty list for all the available Geocoder Services for
    the Qiskrypt's Geocoding.
    """

    for current_geocoder_service_index in range(NUM_POSSIBLE_GEOCODER_SERVICE_NAMES):
        """
        For each index of an available Geocoder Service for the Qiskrypt's Geocoding.
        """

        current_geocoder_service = \
            get_geocoder_service_by_name(POSSIBLE_GEOCODER_SERVICE_NAMES[current_geocoder_service_index])
        """
        Retrieve the current available Geocoder Service for the Qiskrypt's Geocoding.
        """

        all_geocoder_services_list.append(current_geocoder_service)
        """
        Append the current available Geocoder Service for the Qiskrypt's Geocoding
        to the list for all the available Geocoder Services for the Qiskrypt's Geocoding.
        """

    return all_geocoder_services_list


def get_geocoder_service_arguments_and_parameters_by_name(geocoder_service_name):
    """
    Return the dictionary of parameters and arguments for the constructor of a Geocoder Service,
    from the given name of a Geocoder Service.

    :param geocoder_service_name: the name of the Geocoder Service for which will be listed
                                  the parameters and arguments of its constructor.

    :return geocoder_service_arguments_and_parameters_dictionary: the dictionary of parameters and arguments for
                                                                  the constructor of a Geocoder Service,
                                                                  from the given name of a Geocoder Service.
    """

    geocoder_service = get_geocoder_service_by_name(geocoder_service_name)
    """
    Retrieve the Geocoder Service, from the given name of a Geocoder Service.
    """

    geocoder_service_full_argument_specifications = \
        get_full_arguments_specifications(geocoder_service)
    """
    Retrieve the full arguments' specifications from the retrieved Geocoder Service.
    """

    geocoder_service_arguments_and_parameters_dictionary = dict()
    """
    Initialise an empty dictionary for all the arguments and parameters
    for the constructor of a Geocoder Services for the Qiskrypt's Geocoding found.
    """

    geocoder_service_required_arguments = \
        geocoder_service_full_argument_specifications.args
    """
    Retrieve the list of required arguments and parameters
    for the constructor of a Geocoder Services for the Qiskrypt's Geocoding found.
    """

    geocoder_service_required_arguments.remove("self")
    """
    Remove the 'self' argument from the required arguments and parameters
    for the constructor of a Geocoder Services for the Qiskrypt's Geocoding found.
    """

    if geocoder_service_required_arguments is not None:
        """
        If there is some required argument or parameter for the constructor
        of a Geocoder Services for the Qiskrypt's Geocoding found.
        """

        for current_geocoder_service_required_argument in \
                geocoder_service_required_arguments:
            """
            For each required argument or parameter for the constructor
            of a Geocoder Services for the Qiskrypt's Geocoding found.
            """

            geocoder_service_arguments_and_parameters_dictionary \
                [current_geocoder_service_required_argument] = None
            """
            Insert the current required argument or parameter for the constructor
            of a Geocoder Services for the Qiskrypt's Geocoding found as a key, with a None value.
            """

    geocoder_service_required_keyword_only_arguments = \
        geocoder_service_full_argument_specifications.kwonlydefaults
    """
    Retrieve the dictionary of 'keyword-only' arguments and parameters,
    with the default values, for the constructor of a Geocoder Services for
    the Qiskrypt's Geocoding found.
    """

    if geocoder_service_required_keyword_only_arguments is not None:
        """
        If there is some 'keyword-only' argument or parameter for the constructor
        of a Geocoder Services for the Qiskrypt's Geocoding found.
        """

        for current_geocoder_service_required_argument_key, \
            current_geocoder_service_required_argument_value in \
                zip(geocoder_service_required_keyword_only_arguments.keys(),
                    geocoder_service_required_keyword_only_arguments.values()):
            """
            For each 'keyword-only' argument or parameter for the constructor
            of a Geocoder Services for the Qiskrypt's Geocoding found.
            """

            geocoder_service_arguments_and_parameters_dictionary \
                [current_geocoder_service_required_argument_key] = \
                current_geocoder_service_required_argument_value
            """
            Insert the current 'keyword-only' argument or parameter for the constructor
            of a Geocoder Services for the Qiskrypt's Geocoding found as a key, with a None value.
            """

    """
    Return the list of parameters and arguments for the constructor
    of a Geocoder Service, from the given name of a Geocoder Service.
    """
    return geocoder_service_arguments_and_parameters_dictionary


"""
Definition of Constants and Enumerations.
"""

POSSIBLE_GEOCODER_SERVICE_NAMES = ["ALGOLIA", "ARCGIS", "AZURE", "BAIDU", "BAIDUV3", "BANFRANCE",
                                   "BING", "DATABC", "GEOCODEEARTH", "GEOCODIO", "GEONAMES",
                                   "GOOGLE", "GOOGLEV3", "GEOLAKE", "HERE", "HEREV7", "IGNFRANCE",
                                   "LIVEADDRESS", "MAPBOX", "MAPQUEST", "MAPTILER", "NOMINATIM",
                                   "OPENCAGE", "OPENMAPQUEST", "PICKPOINT", "PELIAS", "PHOTON",
                                   "TOMTOM", "WHAT3WORDS", "WHAT3WORDSV3", "YANDEX"]
"""
The available names of the Geocoder Services for the Qiskrypt's Geocoding.
"""

POSSIBLE_DEFAULT_GEOCODER_SERVICE_PARAMETERS =\
    {
      "ALGOLIA": get_geocoder_service_arguments_and_parameters_by_name("ALGOLIA"),
      "ARCGIS": get_geocoder_service_arguments_and_parameters_by_name("ARCGIS"),
      "AZURE": get_geocoder_service_arguments_and_parameters_by_name("AZURE"),
      "BAIDU": get_geocoder_service_arguments_and_parameters_by_name("BAIDU"),
      "BAIDUV3": get_geocoder_service_arguments_and_parameters_by_name("BAIDUV3"),
      "BANFRANCE": get_geocoder_service_arguments_and_parameters_by_name("BANFRANCE"),
      "BING": get_geocoder_service_arguments_and_parameters_by_name("BING"),
      "DATABC": get_geocoder_service_arguments_and_parameters_by_name("DATABC"),
      "GEOCODEEARTH": get_geocoder_service_arguments_and_parameters_by_name("GEOCODEEARTH"),
      "GEOCODIO": get_geocoder_service_arguments_and_parameters_by_name("GEOCODIO"),
      "GEONAMES": get_geocoder_service_arguments_and_parameters_by_name("GEONAMES"),
      "GOOGLE": get_geocoder_service_arguments_and_parameters_by_name("GOOGLE"),
      "GOOGLEV3": get_geocoder_service_arguments_and_parameters_by_name("GOOGLEV3"),
      "GEOLAKE": get_geocoder_service_arguments_and_parameters_by_name("GEOLAKE"),
      "HERE": get_geocoder_service_arguments_and_parameters_by_name("HERE"),
      "HEREV7": get_geocoder_service_arguments_and_parameters_by_name("HEREV7"),
      "IGNFRANCE": get_geocoder_service_arguments_and_parameters_by_name("IGNFRANCE"),
      "LIVEADDRESS": get_geocoder_service_arguments_and_parameters_by_name("LIVEADDRESS"),
      "MAPBOX": get_geocoder_service_arguments_and_parameters_by_name("MAPBOX"),
      "MAPQUEST": get_geocoder_service_arguments_and_parameters_by_name("MAPQUEST"),
      "MAPTILER": get_geocoder_service_arguments_and_parameters_by_name("MAPTILER"),
      "NOMINATIM": get_geocoder_service_arguments_and_parameters_by_name("NOMINATIM"),
      "OPENCAGE": get_geocoder_service_arguments_and_parameters_by_name("OPENCAGE"),
      "OPENMAPQUEST": get_geocoder_service_arguments_and_parameters_by_name("OPENMAPQUEST"),
      "PICKPOINT": get_geocoder_service_arguments_and_parameters_by_name("PICKPOINT"),
      "PELIAS": get_geocoder_service_arguments_and_parameters_by_name("PELIAS"),
      "PHOTON": get_geocoder_service_arguments_and_parameters_by_name("PHOTON"),
      "TOMTOM": get_geocoder_service_arguments_and_parameters_by_name("TOMTOM"),
      "WHAT3WORDS": get_geocoder_service_arguments_and_parameters_by_name("WHAT3WORDS"),
      "WHAT3WORDSV3": get_geocoder_service_arguments_and_parameters_by_name("WHAT3WORDSV3"),
      "YANDEX": get_geocoder_service_arguments_and_parameters_by_name("YANDEX"),
    }
"""
The available parameters for the Geocoder Services for the Qiskrypt's Geocoding.
"""

NUM_POSSIBLE_GEOCODER_SERVICE_NAMES = len(POSSIBLE_GEOCODER_SERVICE_NAMES)
"""
The number of available names of the Geocoder Services for the Qiskrypt's Geocoding.
"""

DEFAULT_GEOCODER_SERVICE_NAME = POSSIBLE_GEOCODER_SERVICE_NAMES[21]
"""
The default name of the Geocoder Service (Nominatim) for the Qiskrypt's Geocoding.
"""

POSSIBLE_DEFAULT_GEOCODER_SERVICE_PARAMETERS[DEFAULT_GEOCODER_SERVICE_NAME]["user_agent"] = "my_request"
"""
Change the 'user_agent' parameter of the default Geocoder Service (Nominatim)
for the Qiskrypt's Geocoding, to ensure a proper functionality.

NOTE: This parameter can be changed, if you wanted...
"""

DEFAULT_GEOCODER_SERVICE_PARAMETERS = POSSIBLE_DEFAULT_GEOCODER_SERVICE_PARAMETERS[DEFAULT_GEOCODER_SERVICE_NAME]
"""
The default Geocoder Service (Nominatim) for the Qiskrypt's Geocoding.
"""


class QiskryptGeocoding:
    """
    Object class for the Qiskrypt's Geocoding.
    """

    def __init__(self):
        """
        Constructor of the Qiskrypt's Geocoding.
        """

        self.geocoder_service_in_use = None
        """
        Set the Geocoder Service for the Qiskrypt's Geocoding in use, initially, as None.
        """

    def initialise_with_default_geocoder_service(self):
        """
        Initialise the Geocoder Service for the Qiskrypt's Geocoding in use,
        with the default Geocoder Service defined.
        """

        geocoder_service = get_geocoder_service_by_name(DEFAULT_GEOCODER_SERVICE_NAME)
        """
        Retrieve the default Geocoder Service for the Qiskrypt's Geocoding.
        """

        self.geocoder_service_in_use = geocoder_service(**DEFAULT_GEOCODER_SERVICE_PARAMETERS)
        """
        Set the Geocoder Service for the Qiskrypt's Geocoding in use,
        with the default Geocoder Service defined and respective default parameters/arguments.
        """

    def initialise_with_geocoder_service_name(self, geocoder_service_name: str):
        """
        Initialise the Geocoder Service for the Qiskrypt's Geocoding in use,
        with a given name for the Geocoder Service.
        """

        geocoder_service = get_geocoder_service_by_name(geocoder_service_name)
        """
        Retrieve the default Geocoder Service for the Qiskrypt's Geocoding.
        """

        self.geocoder_service_in_use = geocoder_service(**DEFAULT_GEOCODER_SERVICE_PARAMETERS)
        """
        Set the Geocoder Service for the Qiskrypt's Geocoding in use,
        with the default Geocoder Service defined and respective default parameters/arguments.
        """

    def reset(self):
        """
        Reset the Geocoder Service for the Qiskrypt's Geocoding in use.
        """

        """
        Set the Geocoder Service for the Qiskrypt's Geocoding in use, as None.
        """
        self.geocoder_service_in_use = None

    def get_geocoder_service_in_use(self):
        """
        Return the Geocoder Service for the Qiskrypt's Geocoding in use.

        :return self.geocoder_service: the Geocoder Service for the Qiskrypt's Geocoding in use.
        """

        """
        Return the Geocoder Service for the Qiskrypt's Geocoding in use.
        """
        return self.geocoder_service_in_use

    def initialise_geocoder_service_in_use(self):
        """
        Return the Geocoder Service for the Qiskrypt's Geocoding in use.

        :return self.geocoder_service: the Geocoder Service for the Qiskrypt's Geocoding in use.
        """

        """
        Return the Geocoder Service for the Qiskrypt's Geocoding in use.
        """
        return self.geocoder_service_in_use
