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

from geopy.location import Location
"""
Import the Location Class from GeoPy.
"""

from geopy.distance import Distance
"""
Import the Distance Class from GeoPy.
"""

from geopy.distance import distance
"""
Import the function to compute distance between two locations from GeoPy.
"""

from inspect import getfullargspec as get_full_arguments_specifications
"""
Import the method to get the full arguments' specifications from the inspection module.
"""

from requests import get as http_get
"""
Import the HTTP Get method for requests based on Web Services.
"""

from json import loads as json_loads
"""
Import the Loading method for JSON objects.
"""

from src.classical_regime.common.QiskryptClassicalUtilities \
    import QiskryptClassicalUtilities
"""
Import the Qiskrypt's Classical Utilities.
"""

"""
Definition of Constants and Enumerations.
"""

OSMR_ROUTER_V1_LINK = "http://router.project-osrm.org/route/v1/"
"""
The link for the OSMR (Open Source Routing Machine) Router v1.
"""

OSMR_ROUTER_V1_PROFILES = ["CAR"]
"""
The profiles for the OSMR (Open Source Routing Machine) Router v1.
"""

KILOMETER_IN_METERS = 1000
"""
The ration of a KM (Kilometer) in Ms (Meters).
"""

METER_IN_KILOMETERS = 0.001
"""
The ration of a M (Meter) in KMs (Kilometers).
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
The default name of the Geocoder Service (Nominatim - Open Source) for the Qiskrypt's Geocoding.
"""

POSSIBLE_DEFAULT_GEOCODER_SERVICE_PARAMETERS[DEFAULT_GEOCODER_SERVICE_NAME]["user_agent"] = "my_request"
"""
Change the 'user_agent' parameter of the default Geocoder Service (Nominatim - Open Source)
for the Qiskrypt's Geocoding, to ensure a proper functionality.

NOTE: This parameter can be changed, if you wanted...
"""

DEFAULT_GEOCODER_SERVICE_PARAMETERS = POSSIBLE_DEFAULT_GEOCODER_SERVICE_PARAMETERS[DEFAULT_GEOCODER_SERVICE_NAME]
"""
The default Geocoder Service (Nominatim) for the Qiskrypt's Geocoding.
"""

NUM_DECIMAL_PLACES_FOR_FLOAT_NUMBERS = 3
"""
The number of decimal places for Float numbers.
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

        self.geocoder_service_initialised = False
        """
        Set the boolean flag to keep information about if the Qiskrypt's Geocoding
        is initialised or not, initially, as False.
        """

    def initialise_with_default_geocoder_service(self):
        """
        Initialise the Geocoder Service for the Qiskrypt's Geocoding in use,
        with the default Geocoder Service defined.
        """

        if not self.is_geocoder_service_initialised():
            """
            If the Geocoder Service for the Qiskrypt's Geocoding in use, is not initialised yet.
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

            self.geocoder_service_initialised = True
            """
            Set the boolean flag to keep information about if the Qiskrypt's Geocoding is
            initialised or not, as True.
            """

        else:
            """
            If the Geocoder Service for the Qiskrypt's Geocoding in use, is already initialised.
            """

            # TODO Throw - Exception

    def initialise_with_geocoder_service_name(self, geocoder_service_name: str):
        """
        Initialise the Geocoder Service for the Qiskrypt's Geocoding in use,
        with a given name for the Geocoder Service.
        """

        if not self.is_geocoder_service_initialised():
            """
            If the Geocoder Service for the Qiskrypt's Geocoding in use, is not initialised yet.
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

            self.geocoder_service_initialised = True
            """
            Set the boolean flag to keep information about if the Qiskrypt's Geocoding is
            initialised or not, as True.
            """

        else:
            """
            If the Geocoder Service for the Qiskrypt's Geocoding in use, is already initialised.
            """

            # TODO Throw - Exception

    def reset(self):
        """
        Reset the Geocoder Service for the Qiskrypt's Geocoding in use.
        """

        if self.is_geocoder_service_initialised():
            """
            If the Geocoder Service for the Qiskrypt's Geocoding in use, is already initialised.
            """

            self.geocoder_service_in_use = None
            """
            Set the Geocoder Service for the Qiskrypt's Geocoding in use, as None.
            """

            self.geocoder_service_initialised = False
            """
            Set the boolean flag to keep information about if the Qiskrypt's Geocoding is
            initialised or not, as False.
            """

        else:
            """
            If the Geocoder Service for the Qiskrypt's Geocoding in use, is not initialised yet.
            """

            # TODO Throw - Exception

    def is_geocoder_service_initialised(self) -> bool:
        """
        Return the boolean flag to keep information about if the Qiskrypt's Geocoding is initialised or not.

        :return self.geocoder_service_initialised: the boolean flag to keep information about if
                                                   the Qiskrypt's Geocoding is initialised or not.
        """

        """
        Return the boolean flag to keep information about if the Qiskrypt's Geocoding is initialised or not.
        """
        return self.geocoder_service_initialised

    def get_geocoder_service_in_use(self):
        """
        Return the Geocoder Service for the Qiskrypt's Geocoding in use.

        :return self.geocoder_service: the Geocoder Service for the Qiskrypt's Geocoding in use.
        """

        """
        Return the Geocoder Service for the Qiskrypt's Geocoding in use.
        """
        return self.geocoder_service_in_use

    def get_location_from_address(self, location_address: str) -> Location:
        """
        Return the location of the given address from the Qiskrypt's Geocoding in use.

        :param location_address: the address from which the location will be extracted.

        :return location: the location of the given address from the Qiskrypt's Geocoding in use.
        """

        if self.is_geocoder_service_initialised():
            """
            If the Geocoder Service of the Qiskrypt's Geocoding is already initialised.
            """

            location = self.geocoder_service_in_use.geocode(location_address)
            """
            Retrieve the location of the given address from the Qiskrypt's Geocoding in use.
            """

            """
            Return the location of the given address from the Qiskrypt's Geocoding in use.
            """
            return location

        else:
            """
            If the Geocoder Service of the Qiskrypt's Geocoding is not initialised yet.
            """

            # TODO Throw - Exception

    def get_location_display_name_from_address(self, location_address: str) -> str:
        """
        Return the display name of the location of the given address from
        the Qiskrypt's Geocoding in use.

        :param location_address: the address from which the location will be extracted.

        :return location_display_name: the display name of the location of the given address from
                                       the Qiskrypt's Geocoding in use.
        """

        if self.is_geocoder_service_initialised():
            """
            If the Geocoder Service of the Qiskrypt's Geocoding is already initialised.
            """

            location_display_name = self.geocoder_service_in_use.geocode(location_address).display_name
            """
            Retrieve the display name of the location of the given address from
            the Qiskrypt's Geocoding in use.
            """

            """
            Return the display name of the location of the given address from
            the Qiskrypt's Geocoding in use.
            """
            return location_display_name

        else:
            """
            If the Geocoder Service of the Qiskrypt's Geocoding is not initialised yet.
            """

            # TODO Throw - Exception

    def get_location_point_from_address(self, location_address: str) -> str:
        """
        Return the point of the location of the given address from
        the Qiskrypt's Geocoding in use.

        :param location_address: the address from which the location will be extracted.

        :return location_point: the point of the location of the given address from
                                the Qiskrypt's Geocoding in use.
        """

        if self.is_geocoder_service_initialised():
            """
            If the Geocoder Service of the Qiskrypt's Geocoding is already initialised.
            """

            location_point = self.geocoder_service_in_use.geocode(location_address).point
            """
            Retrieve the point of the location of the given address from
            the Qiskrypt's Geocoding in use.
            """

            """
            Return the point of the location of the given address from
            the Qiskrypt's Geocoding in use.
            """
            return location_point

        else:
            """
            If the Geocoder Service of the Qiskrypt's Geocoding is not initialised yet.
            """

            # TODO Throw - Exception

    def get_location_coordinates_from_address(self, location_address: str) -> (str, str):
        """
        Return the coordinates of the location of the given address from
        the Qiskrypt's Geocoding in use.

        :param location_address: the address from which the location will be extracted.

        :return location_coordinates: the coordinates of the location of the given address from
                                      the Qiskrypt's Geocoding in use.
        """

        if self.is_geocoder_service_initialised():
            """
            If the Geocoder Service of the Qiskrypt's Geocoding is already initialised.
            """

            location = self.geocoder_service_in_use.geocode(location_address)
            """
            Retrieve the location of the given address from
            the Qiskrypt's Geocoding in use.
            """

            location_coordinates = (location.latitude, location.longitude)
            """
            Retrieve the coordinates of the location of the given address from
            the Qiskrypt's Geocoding in use.
            """

            """
            Return the coordinates of the location of the given address from
            the Qiskrypt's Geocoding in use.
            """
            return location_coordinates

        else:
            """
            If the Geocoder Service of the Qiskrypt's Geocoding is not initialised yet.
            """

            # TODO Throw - Exception

    def get_location_latitude_from_address(self, location_address: str) -> str:
        """
        Return the latitude of the location of the given address from
        the Qiskrypt's Geocoding in use.

        :param location_address: the address from which the location will be extracted.

        :return location_latitude: the latitude of the location of the given address from
                                   the Qiskrypt's Geocoding in use.
        """

        if self.is_geocoder_service_initialised():
            """
            If the Geocoder Service of the Qiskrypt's Geocoding is already initialised.
            """

            location_latitude = self.geocoder_service_in_use.geocode(location_address).latitude
            """
            Retrieve the latitude of the location of the given address from
            the Qiskrypt's Geocoding in use.
            """

            """
            Return the latitude of the location of the given address from
            the Qiskrypt's Geocoding in use.
            """
            return location_latitude

        else:
            """
            If the Geocoder Service of the Qiskrypt's Geocoding is not initialised yet.
            """

            # TODO Throw - Exception

    def get_location_longitude_from_address(self, location_address: str) -> str:
        """
        Return the longitude of the location of the given address from
        the Qiskrypt's Geocoding in use.

        :param location_address: the address from which the location will be extracted.

        :return location_longitude: the longitude of the location of the given address from
                                    the Qiskrypt's Geocoding in use.
        """

        if self.is_geocoder_service_initialised():
            """
            If the Geocoder Service of the Qiskrypt's Geocoding is already initialised.
            """

            location_longitude = self.geocoder_service_in_use.geocode(location_address).longitude
            """
            Retrieve the longitude of the location of the given address from
            the Qiskrypt's Geocoding in use.
            """

            """
            Return the longitude of the location of the given address from
            the Qiskrypt's Geocoding in use.
            """
            return location_longitude

        else:
            """
            If the Geocoder Service of the Qiskrypt's Geocoding is not initialised yet.
            """

            # TODO Throw - Exception

    def get_location_altitude_from_address(self, location_address: str) -> str:
        """
        Return the altitude of the location of the given address from
        the Qiskrypt's Geocoding in use.

        :param location_address: the address from which the location will be extracted.

        :return location_altitude: the altitude of the location of the given address from
                                   the Qiskrypt's Geocoding in use.
        """

        if self.is_geocoder_service_initialised():
            """
            If the Geocoder Service of the Qiskrypt's Geocoding is already initialised.
            """

            location_altitude = self.geocoder_service_in_use.geocode(location_address).altitude
            """
            Retrieve the altitude of the location of the given address from
            the Qiskrypt's Geocoding in use.
            """

            """
            Return the altitude of the location of the given address from
            the Qiskrypt's Geocoding in use.
            """
            return location_altitude

        else:
            """
            If the Geocoder Service of the Qiskrypt's Geocoding is not initialised yet.
            """

            # TODO Throw - Exception

    def compute_distance_between_locations_from_addresses_using_geopy(self, location_address_1: str,
                                                                      location_address_2: str) -> Distance:
        """
        Return the distance between two locations of given addresses from
        the Qiskrypt's Geocoding in use, using GeoPy.

        :param location_address_1: the address from which the 1st location will be extracted.
        :param location_address_2: the address from which the 2nd location will be extracted.

        :return distance_between_locations: the distance between two locations of given addresses from
                                            the Qiskrypt's Geocoding in use, using GeoPy.
        """

        location_coordinates_1 = \
            self.get_location_coordinates_from_address(location_address_1)
        """
        Retrieve the coordinates for the 1st location from
        the Qiskrypt's Geocoding in use, using GeoPy.
        """

        location_coordinates_2 = \
            self.get_location_coordinates_from_address(location_address_2)
        """
        Retrieve the coordinates for the 2nd location from
        the Qiskrypt's Geocoding in use, using GeoPy.
        """

        distance_between_locations = \
            distance(location_coordinates_1, location_coordinates_2)
        """
        Compute the distance between the two locations from
        the Qiskrypt's Geocoding in use, using GeoPy.
        """

        """
        Return the distance between two locations of given addresses from
        the Qiskrypt's Geocoding in use, using GeoPy.
        """
        return distance_between_locations

    def compute_distance_between_locations_from_addresses_in_kms_using_geopy(self, location_address_1: str,
                                                                             location_address_2: str) -> float:
        """
        Return the distance between two locations of given addresses from
        the Qiskrypt's Geocoding in use, given in KMs (Kilometers), using GeoPy.

        :param location_address_1: the address from which the 1st location will be extracted.
        :param location_address_2: the address from which the 2nd location will be extracted.

        :return distance_between_locations_in_kms: the distance between two locations of given addresses from
                                                   the Qiskrypt's Geocoding in use, given in KMs (Kilometers),
                                                   using GeoPy.
        """

        distance_between_locations = \
            self.compute_distance_between_locations_from_addresses_using_geopy(location_address_1,
                                                                               location_address_2)
        """
        Compute the distance between two locations of given addresses from
        the Qiskrypt's Geocoding in use, using GeoPy.
        """

        distance_between_locations_in_kms = distance_between_locations.km
        """
        Retrieve the distance between two locations of given addresses from
        the Qiskrypt's Geocoding in use, given in KMs (Kilometers), using GeoPy.
        """

        """
        Return the distance between two locations of given addresses from
        the Qiskrypt's Geocoding in use, given in KMs (Kilometers), using GeoPy.
        """
        return distance_between_locations_in_kms

    def compute_distance_between_locations_from_addresses_in_ms_using_geopy(self, location_address_1: str,
                                                                            location_address_2: str) -> float:
        """
        Return the distance between two locations of given addresses from
        the Qiskrypt's Geocoding in use, given in Ms (Meters), using GeoPy.

        :param location_address_1: the address from which the 1st location will be extracted.
        :param location_address_2: the address from which the 2nd location will be extracted.

        :return distance_between_locations_in_ms: the distance between two locations of given addresses from
                                                  the Qiskrypt's Geocoding in use, given in Ms (Meters), using GeoPy.
        """

        distance_between_locations = \
            self.compute_distance_between_locations_from_addresses_using_geopy(location_address_1,
                                                                               location_address_2)
        """
        Compute the distance between two locations of given addresses from
        the Qiskrypt's Geocoding in use, using GeoPy.
        """

        distance_between_locations_in_ms = distance_between_locations.m
        """
        Retrieve the distance between two locations of given addresses from
        the Qiskrypt's Geocoding in use, given in Ms (Meters), using GeoPy.
        """

        """
        Return the distance between two locations of given addresses from
        the Qiskrypt's Geocoding in use, given in Ms (Meters), using GeoPy.
        """
        return distance_between_locations_in_ms

    def compute_distance_between_locations_from_addresses_in_ft_using_geopy(self, location_address_1: str,
                                                                            location_address_2: str) -> float:
        """
        Return the distance between two locations of given addresses from
        the Qiskrypt's Geocoding in use, given in FT (Feet), using GeoPy.

        :param location_address_1: the address from which the 1st location will be extracted.
        :param location_address_2: the address from which the 2nd location will be extracted.

        :return distance_between_locations_in_nms: the distance between two locations of given addresses from
                                                   the Qiskrypt's Geocoding in use, given in FT (Feet), using GeoPy.
        """

        distance_between_locations = \
            self.compute_distance_between_locations_from_addresses_using_geopy(location_address_1,
                                                                               location_address_2)
        """
        Compute the distance between two locations of given addresses from
        the Qiskrypt's Geocoding in use, using GeoPy.
        """

        distance_between_locations_in_ft = distance_between_locations.ft
        """
        Retrieve the distance between two locations of given addresses from
        the Qiskrypt's Geocoding in use, given in FT (Feet), using GeoPy.
        """

        """
        Return the distance between two locations of given addresses from
        the Qiskrypt's Geocoding in use, given in FT (Feet), using GeoPy.
        """
        return distance_between_locations_in_ft

    def compute_distance_between_locations_from_addresses_in_mis_using_geopy(self, location_address_1: str,
                                                                             location_address_2: str) -> float:
        """
        Return the distance between two locations of given addresses from
        the Qiskrypt's Geocoding in use, given in MIs (Miles), using GeoPy.

        :param location_address_1: the address from which the 1st location will be extracted.
        :param location_address_2: the address from which the 2nd location will be extracted.

        :return distance_between_locations_in_kms: the distance between two locations of given addresses from
                                                   the Qiskrypt's Geocoding in use, given in MIs (Miles), using GeoPy.
        """

        distance_between_locations = \
            self.compute_distance_between_locations_from_addresses_using_geopy(location_address_1,
                                                                               location_address_2)
        """
        Compute the distance between two locations of given addresses from
        the Qiskrypt's Geocoding in use, using GeoPy.
        """

        distance_between_locations_in_mis = distance_between_locations.mi
        """
        Retrieve the distance between two locations of given addresses from
        the Qiskrypt's Geocoding in use, given in MIs (Miles), using GeoPy.
        """

        """
        Return the distance between two locations of given addresses from
        the Qiskrypt's Geocoding in use, given in MIs (Miles), using GeoPy.
        """
        return distance_between_locations_in_mis

    def compute_distance_between_locations_from_addresses_in_nmis_using_geopy(self, location_address_1: str,
                                                                              location_address_2: str) -> float:
        """
        Return the distance between two locations of given addresses from
        the Qiskrypt's Geocoding in use, given in NMIs (Nautical Miles), using GeoPy.

        :param location_address_1: the address from which the 1st location will be extracted.
        :param location_address_2: the address from which the 2nd location will be extracted.

        :return distance_between_locations_in_nms: the distance between two locations of given addresses from
                                                   the Qiskrypt's Geocoding in use, given in NMIs (Nautical Miles),
                                                   using GeoPy.
        """

        distance_between_locations = \
            self.compute_distance_between_locations_from_addresses_using_geopy(location_address_1,
                                                                               location_address_2)
        """
        Compute the distance between two locations of given addresses from
        the Qiskrypt's Geocoding in use, using GeoPy.
        """

        distance_between_locations_in_nmis = distance_between_locations.nm
        """
        Retrieve the distance between two locations of given addresses from
        the Qiskrypt's Geocoding in use, given in NMIs (Nautical Miles), using GeoPy.
        """

        """
        Return the distance between two locations of given addresses from
        the Qiskrypt's Geocoding in use, given in NMIs (Nautical Miles), using GeoPy.
        """
        return distance_between_locations_in_nmis

    def compute_distance_between_locations_from_addresses_in_ms_using_osmr(self, location_address_1: str,
                                                                           location_address_2: str) -> float:
        """
        Return the distance between two locations of given addresses from
        the Qiskrypt's Geocoding in use, given in Ms (Meters), using OSMR (Open Source Routing Machine).

        :param location_address_1: the address from which the 1st location will be extracted.
        :param location_address_2: the address from which the 2nd location will be extracted.

        :return distance_between_locations_in_kms: the distance between two locations of given addresses from
                                                   the Qiskrypt's Geocoding in use, given in Ms (Meters),
                                                   using OSMR (Open Source Routing Machine).
        """

        osmr_http_get_request_string = OSMR_ROUTER_V1_LINK + OSMR_ROUTER_V1_PROFILES[0].lower() + "/" + \
            "{},{};{},{}".format(self.get_location_longitude_from_address(location_address_1),
                                 self.get_location_latitude_from_address(location_address_1),
                                 self.get_location_longitude_from_address(location_address_2),
                                 self.get_location_latitude_from_address(location_address_2))
        """
        Set the string for the HTTP Get Request for the OSMR (Open Source Routing Machine) from
        the Qiskrypt's Geocoding in use.
        """

        osmr_http_get_request = http_get(osmr_http_get_request_string)
        """
        Perform the HTTP Get Request for the OSMR (Open Source Routing Machine) from
        the Qiskrypt's Geocoding in use, to obtain the route.
        """

        osmr_http_get_response_json_content = \
            json_loads(osmr_http_get_request.content)
        """
        Load the JSON content from the HTTP Get Response for the OSMR (Open Source Routing Machine) from
        the Qiskrypt's Geocoding in use, for which was obtained the routes.
        """

        osmr_result_routes_dictionary = osmr_http_get_response_json_content.get("routes")
        """
        Retrieve the dictionary of routes in the JSON content from the HTTP Get Response
        for the OSMR (Open Source Routing Machine) from the Qiskrypt's Geocoding in use,
        for which was obtained the routes.
        """

        osmr_route_1 = osmr_result_routes_dictionary[0]
        """
        Extract the 1st route in the dictionary of routes in the JSON content from the HTTP Get Response
        for the OSMR (Open Source Routing Machine) from the Qiskrypt's Geocoding in use,
        for which was obtained the routes.
        """

        osmr_route_distance_meters_1 = \
            QiskryptClassicalUtilities.truncate_float_number_with_decimal_places(osmr_route_1["distance"],
                                                                                 NUM_DECIMAL_PLACES_FOR_FLOAT_NUMBERS)
        """
        Retrieve the distance in Ms (Meters) from the 1st route extracted in
        the dictionary of routes in the JSON content from the HTTP Get Response
        for the OSMR (Open Source Routing Machine) from the Qiskrypt's Geocoding in use,
        for which was obtained the routes.
        """

        """
        Return the distance in Ms (Meters) from the 1st route extracted in
        the dictionary of routes in the JSON content from the HTTP Get Response
        for the OSMR (Open Source Routing Machine) from the Qiskrypt's Geocoding in use,
        for which was obtained the routes.
        """
        return osmr_route_distance_meters_1

    def compute_distance_between_locations_from_addresses_in_kms_using_osmr(self, location_address_1: str,
                                                                            location_address_2: str) -> float:
        """
        Return the distance between two locations of given addresses from
        the Qiskrypt's Geocoding in use, given in KMs (Kilometers), using OSMR (Open Source Routing Machine).

        :param location_address_1: the address from which the 1st location will be extracted.
        :param location_address_2: the address from which the 2nd location will be extracted.

        :return distance_between_locations_in_kms: the distance between two locations of given addresses from
                                                   the Qiskrypt's Geocoding in use, given in KMs (Kilometers),
                                                   using OSMR (Open Source Routing Machine).
        """

        distance_between_locations_from_addresses_in_ms_using_osmr = \
            self.compute_distance_between_locations_from_addresses_in_ms_using_osmr(location_address_1,
                                                                                    location_address_2)
        """
        Compute the distance between two locations of given addresses from
        the Qiskrypt's Geocoding in use, given in Ms (Meters), using OSMR (Open Source Routing Machine).
        """

        distance_between_locations_from_addresses_in_kms_using_osmr = \
            QiskryptClassicalUtilities.truncate_float_number_with_decimal_places\
            ((distance_between_locations_from_addresses_in_ms_using_osmr / KILOMETER_IN_METERS),
             NUM_DECIMAL_PLACES_FOR_FLOAT_NUMBERS)
        """
        Compute the distance between two locations of given addresses from
        the Qiskrypt's Geocoding in use, given in KMs (Kilometers), using OSMR (Open Source Routing Machine).
        """

        return distance_between_locations_from_addresses_in_kms_using_osmr
