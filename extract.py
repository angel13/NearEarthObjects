"""Extract data on near-Earth objects and close approaches from CSV and
JSONfiles.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at
the command line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about
    near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    # Load NEO data from the given CSV file.
    neos1 = []
    with open(csv_path, 'r') as infile:
        reader = csv.DictReader(infile)
        i = 0
        for row in reader:
            # designation = full_name, cd = name, dia = diameter, velocity
            # designation`: The primary designation for this `NearEarthObject
            # 'full_name
            # `name`: The IAU name for this `NearEarthObject`. name
            # `diameter`: The diameter, in kilometers, of this
            # `NearEarthObject`. diameter
            # 'hazardous`: Whether or not this `NearEarthObject` is
            # potentially hazardous.  pha
            # `approaches`: A collection of this `NearEarthObject`s close
            # approaches to Earth.

            obj1 = NearEarthObject(row['pdes'], row['name'], row['diameter'],
                                   row['pha'], **row)
            neos1.append(obj1)
    return neos1


def load_approaches(json_path):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close
     approaches.
    :return: A collection of `CloseApproaches.
    """
    approaches = []

    # def __init__(self, designation, cd=None, dist = 0.0,velocity = 0.0,
    # **info):
    """Create a new `CloseApproach`.

    :param designation: A String Primary designation of the asteroid or comet
    (e.g., 443, 2000 SG344)
    :param cd (time) time of close-approach (formatted calendar date/time,
    : in UTC)
    :param dist (float)  nominal approach distance (au)
    :param v_rel (float) velocity relative to the approach body at close
     approach (km/s)
    :param info: A dictionary of excess keyword arguments supplied to the
    constructor.
    """

    # Extract data into Python
    with open(json_path, 'r') as infile:
        data = json.load(infile)  # Parse JSON data into a Python object. (A)II
        approaches_data = data['data']
        fields = (data['fields'])
        # zip fields and index values into dictionary
        # des_idx = fields.index('des')

        i = 0
        for appr in approaches_data:

            item_dict = dict(zip(fields, [appr[x] for x in
                                          range(len(fields))]))
            b = item_dict["dist"]
            # print(f" dict {b}")

            obj = CloseApproach(item_dict["des"], item_dict['cd'],
                                item_dict['dist'], item_dict['v_rel'],
                                **item_dict)
            # print(obj)
            approaches.append(obj)

    # print (len(approaches))
    return approaches
