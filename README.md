mta-station-entrance-turnstile
==============================

A project to relate MTA subway station, entrance, and turnstile IDs.

Concepts:

* Platform - An area from which one can board a single train at a time. You always must pass through a turnstile or emergency exit to reach a platform.
* Station - A collection of platforms.
* Entrance - The interface between non-MTA and MTA property. Typically a door, though not always.
* Vestibule - MTA property one doesn't need to pay to reach.
** AKA "fare control area"
* Turnstile - The only way to get into a station. Typically between a vestibule and a station.
** Control Area - AKA "Booth", "fare control area", a vestibule.
** Unit - AKA "Remote", "Remote Unit". Up to 4 turnstiles.
* Corridor - Passageway between stations or vestibules.
* Complex - A big adjacent glom of stations and vestibules.

Data sources:

* Stations - http://www.mta.info/developers/data/nyct/subway/google_transit.zip
* Turnstiles - http://www.mta.info/developers/resources/nyct/turnstile/Remote-Booth-Station.xls
* Entrances - http://www.mta.info/developers/data/nyct/subway/StationEntrances.csv
