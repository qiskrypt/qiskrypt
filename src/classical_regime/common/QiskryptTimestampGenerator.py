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

from datetime import datetime as date_time
"""
Import DateTime object class from
the DateTime module from Python's Library.
"""

from datetime import timedelta as time_delta
"""
Import TimeDelta object class from
the DateTime module from Python's Library.
"""

from random import randrange as random_range
"""
Import RandRange object class from
the Random module from Python's Library.
"""


class QiskryptTimestampGenerator:
    """
    Object class for the Qiskrypt's Timestamp Generator.
    """

    def __init__(self, timestamp_generator_name: str):
        """
        Constructor of the Qiskrypt's Timestamp Generator.

        :param timestamp_generator_name: the name for the Qiskrypt's Timestamp Generator.
        """

        self.timestamp_generator_name = timestamp_generator_name
        """
        Set the name for the Qiskrypt's Timestamp Generator.
        """

        self.date_and_time_initialisation = date_time.now()
        """
        Set the date and time of initialisation of
        the Qiskrypt's Timestamp Generator.
        """

    def get_date_and_time_initialisation(self) -> date_time:
        """
        Return the date and time of initialisation of the Qiskrypt's Timestamp Generator.

        :return self.date_and_time_initialisation: the date and time of initialisation of
                                                   the Qiskrypt's Timestamp Generator.
        """

        """
        Return the date and time of initialisation of
        the Qiskrypt's Timestamp Generator.
        """
        return self.date_and_time_initialisation

    def get_date_and_time_initialisation_customised_format(self) -> date_time:
        """
        Return the date and time of initialisation of
        the Qiskrypt's Timestamp Generator, as a customised Date and Time format.

        :return date_and_time_initialisation_customised_format: the date and time of initialisation of
                                                                the Qiskrypt's Timestamp Generator,
                                                                as a customised Date and Time format.
        """

        date_and_time_initialisation = \
            self.get_date_and_time_initialisation()
        """
        Retrieve the date and time of initialisation of
        the Qiskrypt's Timestamp Generator.
        """

        date_and_time_initialisation_customised_format = \
            date_time(date_and_time_initialisation.year, date_and_time_initialisation.month,
                      date_and_time_initialisation.day, date_and_time_initialisation.hour,
                      date_and_time_initialisation.minute, date_and_time_initialisation.second)
        """
        Retrieve the date and time of initialisation of
        the Qiskrypt's Timestamp Generator, as a customised Date and Time format.
        """

        """
        Return the date and time of initialisation of
        the Qiskrypt's Timestamp Generator, as a customised Date and Time format.
        """
        return date_and_time_initialisation_customised_format

    def get_date_and_time_initialisation_timestamp(self) -> float:
        """
        Return the date and time of initialisation of the Qiskrypt's Timestamp Generator,
        as a Timestamp representation.

        :return date_and_time_initialisation_timestamp: the date and time of initialisation of
                                                        the Qiskrypt's Timestamp Generator,
                                                        as a Timestamp representation.
        """

        date_and_time_initialisation_timestamp = \
            date_time.timestamp(self.date_and_time_initialisation)
        """
        Retrieve the date and time of initialisation of the Qiskrypt's Timestamp Generator,
        as a Timestamp representation.
        """

        """
        Return the date and time of initialisation of the Qiskrypt's Timestamp Generator,
        as a Timestamp representation.
        """
        return date_and_time_initialisation_timestamp

    def get_date_and_time_initialisation_plus_delta(self, weeks_delta, days_delta, hours_delta, minutes_delta,
                                                    seconds_delta, milliseconds_delta,
                                                    microseconds_delta) -> date_time:
        """
        Return the date and time of initialisation of the Qiskrypt's Timestamp Generator,
        with a given delta Date and Time, considering deltas for the number of weeks, days,
        hours, minutes, seconds, milliseconds and microseconds.

        :param weeks_delta: the delta number for weeks.
        :param days_delta: the delta number for days.
        :param hours_delta: the delta number for hours.
        :param minutes_delta: the delta number for minutes.
        :param seconds_delta: the delta number for seconds.
        :param milliseconds_delta: the delta number for milliseconds.
        :param microseconds_delta: the delta number for microseconds.

        :return date_and_time_initialisation_plus_delta: the date and time of initialisation of
                                                         the Qiskrypt's Timestamp Generator,
                                                         with a given delta Date and Time,
                                                         considering weeks, days, hours, minutes,
                                                         seconds, milliseconds and microseconds.
        """

        date_and_time_initialisation_plus_delta = self.get_date_and_time_initialisation() + \
            time_delta(weeks=weeks_delta, days=days_delta, hours=hours_delta, minutes=minutes_delta,
                       seconds=seconds_delta, milliseconds=milliseconds_delta, microseconds=microseconds_delta)
        """
        Compute the date and time of initialisation of the Qiskrypt's Timestamp Generator,
        with a given delta Date and Time, considering weeks, days, hours, minutes,
        seconds, milliseconds and microseconds.
        """

        """
        Return the date and time of initialisation of the Qiskrypt's Timestamp Generator,
        with a given delta Date and Time, considering weeks, days, hours, minutes,
        seconds, milliseconds and microseconds.
        """
        return date_and_time_initialisation_plus_delta

    def get_date_and_time_initialisation_plus_delta_customised_format(self, weeks_delta, days_delta,
                                                                      hours_delta, minutes_delta,
                                                                      seconds_delta, milliseconds_delta,
                                                                      microseconds_delta) -> date_time:
        """
        Return the date and time of initialisation of the Qiskrypt's Timestamp Generator,
        with a given delta Date and Time, considering deltas for the number of weeks, days,
        hours, minutes, seconds, milliseconds and microseconds, as a customised Date and Time format.

        :param weeks_delta: the delta number for weeks.
        :param days_delta: the delta number for days.
        :param hours_delta: the delta number for hours.
        :param minutes_delta: the delta number for minutes.
        :param seconds_delta: the delta number for seconds.
        :param milliseconds_delta: the delta number for milliseconds.
        :param microseconds_delta: the delta number for microseconds.

        :return date_and_time_initialisation_plus_delta_customised_format: the date and time of initialisation of
                                                                           the Qiskrypt's Timestamp Generator,
                                                                           as a customised Date and Time format.
        """

        date_and_time_initialisation_plus_delta = \
            self.get_date_and_time_initialisation_plus_delta(weeks_delta, days_delta,
                                                             hours_delta, minutes_delta,
                                                             seconds_delta, milliseconds_delta, microseconds_delta)
        """
        Retrieve the date and time of initialisation of the Qiskrypt's Timestamp Generator,
        with a given delta Date and Time, considering weeks, days, hours, minutes,
        seconds, milliseconds and microseconds.
        """

        date_and_time_initialisation_plus_delta_customised_format = \
            date_time(date_and_time_initialisation_plus_delta.year,
                      date_and_time_initialisation_plus_delta.month,
                      date_and_time_initialisation_plus_delta.day,
                      date_and_time_initialisation_plus_delta.hour,
                      date_and_time_initialisation_plus_delta.minute,
                      date_and_time_initialisation_plus_delta.second)
        """
        Retrieve the date and time of initialisation of the Qiskrypt's Timestamp Generator,
        with a given delta Date and Time, considering weeks, days, hours, minutes,
        seconds, milliseconds and microseconds, as a customised Date and Time format.
        """

        """
        Return the date and time of initialisation of the Qiskrypt's Timestamp Generator,
        with a given delta Date and Time, considering weeks, days, hours, minutes,
        seconds, milliseconds and microseconds, as a customised Date and Time format.
        """
        return date_and_time_initialisation_plus_delta_customised_format

    def get_date_and_time_initialisation_plus_delta_timestamp(self, weeks_delta, days_delta,
                                                              hours_delta, minutes_delta,
                                                              seconds_delta, milliseconds_delta,
                                                              microseconds_delta) -> float:
        """
        Return the date and time of initialisation of the Qiskrypt's Timestamp Generator,
        with a given delta Date and Time, considering deltas for the number of weeks, days,
        hours, minutes, seconds, milliseconds and microseconds, as a Timestamp representation.

        :param weeks_delta: the delta number for weeks.
        :param days_delta: the delta number for days.
        :param hours_delta: the delta number for hours.
        :param minutes_delta: the delta number for minutes.
        :param seconds_delta: the delta number for seconds.
        :param milliseconds_delta: the delta number for milliseconds.
        :param microseconds_delta: the delta number for microseconds.

        :return date_and_time_initialisation_plus_delta_timestamp: the date and time of initialisation of
                                                                   the Qiskrypt's Timestamp Generator,
                                                                   with a given delta Date and Time,
                                                                   considering weeks, days, hours, minutes,
                                                                   seconds, milliseconds and microseconds.
        """

        date_and_time_initialisation_plus_delta = \
            self.get_date_and_time_initialisation_plus_delta(weeks_delta, days_delta,
                                                             hours_delta, minutes_delta,
                                                             seconds_delta, milliseconds_delta, microseconds_delta)
        """
        Compute the date and time of initialisation of the Qiskrypt's Timestamp Generator,
        with a given delta Date and Time, considering deltas for the number of weeks, days,
        hours, minutes, seconds, milliseconds and microseconds.
        """

        date_and_time_initialisation_plus_delta_timestamp = \
            date_time.timestamp(date_and_time_initialisation_plus_delta)
        """
        Retrieve the date and time of initialisation of the Qiskrypt's Timestamp Generator,
        with a given delta Date and Time, considering deltas for the number of weeks, days,
        hours, minutes, seconds, milliseconds and microseconds, as a Timestamp representation.
        """

        """
        Return the date and time of initialisation of the Qiskrypt's Timestamp Generator,
        with a given delta Date and Time, considering deltas for the number of weeks, days,
        hours, minutes, seconds, milliseconds and microseconds, as a Timestamp representation.
        """
        return date_and_time_initialisation_plus_delta_timestamp

    def generate_pseudo_random_dates_and_times(self, num_pseudo_random_dates_and_times_to_generate: int,
                                               weeks_max_delta: int, days_max_delta: int, hours_max_delta: int,
                                               minutes_max_delta: int, seconds_max_delta: int,
                                               milliseconds_max_delta: int, microseconds_max_delta: int) -> list:
        """
        Generate and return a given number of Pseudo-Random Dates and Times,
        starting from a given delta Date and Time, for a generator/list.

        :param num_pseudo_random_dates_and_times_to_generate: the number of Pseudo-Random
                                                              Dates and Times to be generated.
        :param weeks_max_delta: the delta number for weeks.
        :param days_max_delta: the delta number for days.
        :param hours_max_delta: the delta number for hours.
        :param minutes_max_delta: the delta number for minutes.
        :param seconds_max_delta: the delta number for seconds.
        :param milliseconds_max_delta: the delta number for milliseconds.
        :param microseconds_max_delta: the delta number for microseconds.

        :return date_and_time_initialisation_plus_pseudo_random_delta: the Pseudo-Random Timestamps,
                                                                       starting from a given delta Date and Time,
                                                                       for a generator/list.
        """

        date_and_time_initialisation = \
            self.get_date_and_time_initialisation()
        """
        Retrieve the date and time of initialisation of the Qiskrypt's Timestamp Generator.
        """

        while num_pseudo_random_dates_and_times_to_generate > 0:
            """
            While there are still Pseudo-Random Dates and Times to be generated.
            """

            if weeks_max_delta == 0:
                """
                If the maximum delta number for weeks is not set up,
                will not be defined any pseudo-random delta for weeks.
                """

                weeks_random_delta = 0
                """
                Set the pseudo-random delta for weeks as zero (0).
                """

            else:
                """
                If the maximum delta number for weeks is set up,
                will be defined a pseudo-random delta for the number of weeks.
                """

                weeks_random_delta = random_range(weeks_max_delta)
                """
                Set the pseudo-random delta for the number of weeks,
                between zero (0) and the maximum delta number for weeks.
                """

            if days_max_delta == 0:
                """
                If the maximum delta number for days is not set up,
                will not be defined any pseudo-random delta for days.
                """

                days_random_delta = 0
                """
                Set the pseudo-random delta for days as zero (0).
                """

            else:
                """
                If the maximum delta number for days is set up,
                will be defined a pseudo-random delta for the number of days.
                """

                days_random_delta = random_range(days_max_delta)
                """
                Set the pseudo-random delta for the number of days,
                between zero (0) and the maximum delta number for days.
                """

            if hours_max_delta == 0:
                """
                If the maximum delta number for hours is not set up,
                will not be defined any pseudo-random delta for hours.
                """

                hours_random_delta = 0
                """
                Set the pseudo-random delta for hours as zero (0).
                """

            else:
                """
                If the maximum delta number for hours is set up,
                will be defined a pseudo-random delta for the number of hours.
                """

                hours_random_delta = random_range(days_max_delta)
                """
                Set the pseudo-random delta for the number of hours,
                between zero (0) and the maximum delta number for hours.
                """

            if minutes_max_delta == 0:
                """
                If the maximum delta number for minutes is not set up,
                will not be defined any pseudo-random delta for minutes.
                """

                minutes_random_delta = 0
                """
                Set the pseudo-random delta for minutes as zero (0).
                """

            else:
                """
                If the maximum delta number for minutes is set up,
                will be defined a pseudo-random delta for the number of minutes.
                """

                minutes_random_delta = random_range(minutes_max_delta)
                """
                Set the pseudo-random delta for the number of minutes,
                between zero (0) and the maximum delta number for minutes.
                """

            if seconds_max_delta == 0:
                """
                If the maximum delta number for seconds is not set up,
                will not be defined any pseudo-random delta for seconds.
                """

                seconds_random_delta = 0
                """
                Set the pseudo-random delta for seconds as zero (0).
                """

            else:
                """
                If the maximum delta number for seconds is set up,
                will be defined a pseudo-random delta for the number of seconds.
                """

                seconds_random_delta = random_range(seconds_max_delta)
                """
                Set the pseudo-random delta for the number of seconds,
                between zero (0) and the maximum delta number for seconds.
                """

            if milliseconds_max_delta == 0:
                """
                If the maximum delta number for milliseconds is not set up,
                will not be defined any pseudo-random delta for milliseconds.
                """

                milliseconds_random_delta = 0
                """
                Set the pseudo-random delta for milliseconds as zero (0).
                """

            else:
                """
                If the maximum delta number for milliseconds is set up,
                will be defined a pseudo-random delta for the number of milliseconds.
                """

                milliseconds_random_delta = random_range(milliseconds_max_delta)
                """
                Set the pseudo-random delta for the number of milliseconds,
                between zero (0) and the maximum delta number for milliseconds.
                """

            if microseconds_max_delta == 0:
                """
                If the maximum delta number for microseconds is not set up,
                will not be defined any pseudo-random delta for microseconds.
                """

                microseconds_random_delta = 0
                """
                Set the pseudo-random delta for microseconds as zero (0).
                """

            else:
                """
                If the maximum delta number for microseconds is set up,
                will be defined a pseudo-random delta for the number of microseconds.
                """

                microseconds_random_delta = random_range(microseconds_max_delta)
                """
                Set the pseudo-random delta for the number of microseconds,
                between zero (0) and the maximum delta number for microseconds.
                """

            date_and_time_initialisation_plus_pseudo_random_delta = date_and_time_initialisation + \
                time_delta(weeks=weeks_random_delta, days=days_random_delta, hours=hours_random_delta,
                           minutes=minutes_random_delta, seconds=seconds_random_delta,
                           milliseconds=milliseconds_random_delta, microseconds=microseconds_random_delta)
            """
            Compute the current date and time of initialisation of the Qiskrypt's Timestamp Generator,
            with a given delta Date and Time, considering the pseudo-random
            weeks, days, hours, minutes, seconds, milliseconds and microseconds computed previously.
            """

            yield date_and_time_initialisation_plus_pseudo_random_delta
            """
            Yield the current date and time of initialisation of the Qiskrypt's Timestamp Generator,
            with a given delta Date and Time, considering the pseudo-random 
            weeks, days, hours, minutes, seconds, milliseconds and microseconds computed previously,
            for a generator/list.
            """

            num_pseudo_random_dates_and_times_to_generate -= 1
            """
            Decrease the counting for the remaining Pseudo-Random Dates and Times to be generated.
            """

    def generate_pseudo_random_dates_and_times_customised_format(
        self, num_pseudo_random_dates_and_times_to_generate: int, weeks_max_delta: int,
        days_max_delta: int, hours_max_delta: int, minutes_max_delta: int, seconds_max_delta: int,
            milliseconds_max_delta: int, microseconds_max_delta: int) -> list:
        """
        Generate and return a given number of Pseudo-Random Dates and Times,
        starting from a given delta Date and Time, with a customised format, for a generator/list.

        :param num_pseudo_random_dates_and_times_to_generate: the number of Pseudo-Random
                                                              Dates and Times to be generated.
        :param weeks_max_delta: the delta number for weeks.
        :param days_max_delta: the delta number for days.
        :param hours_max_delta: the delta number for hours.
        :param minutes_max_delta: the delta number for minutes.
        :param seconds_max_delta: the delta number for seconds.
        :param milliseconds_max_delta: the delta number for milliseconds.
        :param microseconds_max_delta: the delta number for microseconds.

        :return pseudo_random_dates_and_times_customised_format: the Pseudo-Random Timestamps,
                                                                 starting from a given delta Date and Time,
                                                                 with a customised format, for a generator/list.
        """

        pseudo_random_dates_and_times = \
            self.generate_pseudo_random_dates_and_times(num_pseudo_random_dates_and_times_to_generate,
                                                        weeks_max_delta, days_max_delta, hours_max_delta,
                                                        minutes_max_delta, seconds_max_delta,
                                                        milliseconds_max_delta, microseconds_max_delta)
        """
        Generate and retrieve the given number of Pseudo-Random Dates and Times,
        starting from a given delta Date and Time.
        """

        pseudo_random_dates_and_times_customised_format = list()
        """
        Create an empty list for the Pseudo-Random Dates and Times,
        starting from a given delta Date and Time, with a customised format.
        """

        for current_pseudo_random_date_and_time in pseudo_random_dates_and_times:
            """
            For each Pseudo-Random Date and Time generated.
            """

            if isinstance(current_pseudo_random_date_and_time, date_time):
                """
                If the current Pseudo-Random Date and Time generated is really a Date and Time.
                """

                current_pseudo_random_date_and_time_customised_format = \
                    date_time(current_pseudo_random_date_and_time.year,
                              current_pseudo_random_date_and_time.month,
                              current_pseudo_random_date_and_time.day,
                              current_pseudo_random_date_and_time.hour,
                              current_pseudo_random_date_and_time.minute,
                              current_pseudo_random_date_and_time.second)
                """
                Retrieve the current Pseudo-Random Date and Time generated,
                starting from a given delta Date and Time, with a customised format.
                """

                pseudo_random_dates_and_times_customised_format\
                    .append(current_pseudo_random_date_and_time_customised_format)
                """
                Append the current Pseudo-Random Date and Time generated to
                the list for the Pseudo-Random Dates and Times,
                starting from a given delta Date and Time, with a customised format.
                """

            else:
                """
                If the current Pseudo-Random Date and Time generated is not a Date and Time.
                """

                # TODO Throw - Exception

        """
        Return the list for the Pseudo-Random Dates and Times,
        starting from a given delta Date and Time, with a customised format.
        """
        return pseudo_random_dates_and_times_customised_format

    def generate_pseudo_random_dates_and_times_timestamp(
        self, num_pseudo_random_dates_and_times_to_generate: int, weeks_max_delta: int,
        days_max_delta: int, hours_max_delta: int, minutes_max_delta: int, seconds_max_delta: int,
            milliseconds_max_delta: int, microseconds_max_delta: int) -> list:
        """
        Generate and return a given number of Pseudo-Random Dates and Times,
        starting from a given delta Date and Time, as Timestamps' representations, for a generator/list.

        :param num_pseudo_random_dates_and_times_to_generate: the number of Pseudo-Random
                                                              Dates and Times to be generated.
        :param weeks_max_delta: the delta number for weeks.
        :param days_max_delta: the delta number for days.
        :param hours_max_delta: the delta number for hours.
        :param minutes_max_delta: the delta number for minutes.
        :param seconds_max_delta: the delta number for seconds.
        :param milliseconds_max_delta: the delta number for milliseconds.
        :param microseconds_max_delta: the delta number for microseconds.

        :return pseudo_random_dates_and_times_timestamps: the Pseudo-Random Timestamps,
                                                          starting from a given delta Date and Time,
                                                          as Timestamps' representations, for a generator/list.
        """

        pseudo_random_dates_and_times = \
            self.generate_pseudo_random_dates_and_times(num_pseudo_random_dates_and_times_to_generate,
                                                        weeks_max_delta, days_max_delta, hours_max_delta,
                                                        minutes_max_delta, seconds_max_delta,
                                                        milliseconds_max_delta, microseconds_max_delta)
        """
        Generate and retrieve the given number of Pseudo-Random Dates and Times,
        starting from a given delta Date and Time.
        """

        pseudo_random_dates_and_times_timestamps = list()
        """
        Create an empty list for the Pseudo-Random Dates and Times,
        starting from a given delta Date and Time, as Timestamps' representations.
        """

        for current_pseudo_random_date_and_time in pseudo_random_dates_and_times:
            """
            For each Pseudo-Random Date and Time generated.
            """

            if isinstance(current_pseudo_random_date_and_time, date_time):
                """
                If the current Pseudo-Random Date and Time generated is really a Date and Time.
                """

                current_pseudo_random_date_and_time_timestamp = \
                    date_time.timestamp(current_pseudo_random_date_and_time)
                """
                Retrieve the current Pseudo-Random Date and Time generated,
                starting from a given delta Date and Time, as a Timestamp representation.
                """

                pseudo_random_dates_and_times_timestamps\
                    .append(current_pseudo_random_date_and_time_timestamp)
                """
                Append the current Pseudo-Random Date and Time generated to
                the list for the Pseudo-Random Dates and Times,
                starting from a given delta Date and Time, as a Timestamp representation.
                """

            else:
                """
                If the current Pseudo-Random Date and Time generated is not a Date and Time.
                """

                # TODO Throw - Exception

        """
        Return the list for the Pseudo-Random Dates and Times,
        starting from a given delta Date and Time, as Timestamps' representations.
        """
        return pseudo_random_dates_and_times_timestamps

    @staticmethod
    def get_current_data_and_time() -> date_time:
        """
        Return the current date and time of the Qiskrypt's Timestamp Generator.

        :return current_data_and_time: the current date and time of
                                       the Qiskrypt's Timestamp Generator.
        """

        current_data_and_time = date_time.now()
        """
        Retrieve the current date and time of the Qiskrypt's Timestamp Generator.
        """

        """
        Return the current date and time of the Qiskrypt's Timestamp Generator.
        """
        return current_data_and_time
