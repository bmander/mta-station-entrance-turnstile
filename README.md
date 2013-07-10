mta-station-entrance-turnstile
==============================

A project to relate MTA subway station, entrance, and turnstile IDs.

Concepts
--------

* Platform - An area from which one can board a single train at a time. You always must pass through a turnstile or emergency exit to reach a platform.
* Station - A collection of platforms.
* Entrance - The interface between non-MTA and MTA property. Typically a door, though not always.
* Vestibule - MTA property one doesn't need to pay to reach. A kind of lobby between the street and the paid area.
  AKA "fare control area".
* Turnstile - The only way to get into a station. Typically between a vestibule and a station.
* Turnstile :: Control Area - AKA "Booth", "fare control area", a vestibule.
* Turnstile :: Unit - AKA "Remote", "Remote Unit". Up to 4 turnstiles.
* Corridor - Passageway between stations or vestibules.
* Complex - A big adjacent glom of stations and vestibules.

Data sources
------------

### Stations

* Source: http://www.mta.info/developers/data/nyct/subway/google_transit.zip
* Each station has an entry in the stops.txt file in google_transit.zip. Each station has a unique id "stop_id".
  Stations also have a descriptive string "stop_name" which serves as a kind of sloppy foreign key.

### Turnstiles

* Source: http://www.mta.info/developers/resources/nyct/turnstile/Remote-Booth-Station.xls
* Turnstiles cannot be individually identified. Counts are grouped by "booth" or "control area". These control
  areas are associated with a ("station","line name","division") triple, though some control areas are equidistant
  from platforms in different stations, it is sometimes a challenge to deduce where these control areas are.
* It appears that the "remote unit" part of the identifier is useless, as it purports to identify a single bank of
  about 4 turnstiles, but different control areas share "remote unit" ids, which can't be right.

### Entrances

* Sources: http://www.mta.info/developers/data/nyct/subway/StationEntrances.csv
* Entrances do not have a foreign key, though each one references a (lat,lon) of a station, in addition to a station name.
  In reality each entrance is adjacent to one or more control areas, which can take different amounts of time to reach
  from the entrance. In turn each control area is adjacent to one or more platforms at different removes, each of which 
  is identified with a single station. The relationship between entrance and station is therefore sometimes a bit fuzzy.

Project Strategy
----------------

### Import data

Import patchwork of data into three geojson datasets.

### Identify location of booths

Could involve a lot of guesswork, and groundwork.

### Relate

Relate entrances to control areas, and control areas to stations.

### Compile 

Compile geojson-normalized source data sets and join tables into a geojson file showing unconnected entrances and control areas.
