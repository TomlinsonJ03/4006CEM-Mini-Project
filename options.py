"""A dictonary containing every option/button in the map.
xStart, yStart, xEnd, yEnd are all percentiles, which are later multipled by the total width and
height of the map.
Activated is a boolean which changes when the button is placed on the screen.
Ending is a boolean which determines if that option/button is the final child.
Children define all the options that option is a parent to/is linked to."""

options = {

    # //////////////////// LAYER 1 ////////////////////

    'Start': {
        'xStart': 0.475,
        'yStart': 0.05,
        'xEnd': 0.525,
        'yEnd': 0.1,
        'activated': False,
        'ending': False,
        'children': ['Lounge', 'Basement', 'Office', 'Kitchen', 'Nursery']
    },

    # //////////////////// LAYER 2 ////////////////////

    'Lounge': {
        'xStart': 0.110,
        'yStart': 0.15,
        'xEnd': 0.170,
        'yEnd': 0.2,
        'activated': False,
        'ending': False,
        'children': ['Truth', 'Lie']
    },
    'Basement': {
        'xStart': 0.287,
        'yStart': 0.15,
        'xEnd': 0.363,
        'yEnd': 0.2,
        'activated': False,
        'ending': False,
        'children': ['Help', "Don't help"]
    },
    'Office': {
        'xStart': 0.475,
        'yStart': 0.15,
        'xEnd': 0.525,
        'yEnd': 0.2,
        'activated': False,
        'ending': False,
        'children': ['Steal', 'Talk']
    },
    'Kitchen': {
        'xStart': 0.650,
        'yStart': 0.15,
        'xEnd': 0.710,
        'yEnd': 0.2,
        'activated': False,
        'ending': False,
        'children': ['Escape', 'Fight']
    },
    'Nursery': {
        'xStart': 0.830,
        'yStart': 0.15,
        'xEnd': 0.890,
        'yEnd': 0.2,
        'activated': False,
        'ending': False,
        'children': ['Listen', 'Hack']
    },

    # //////////////////// LAYER 3 ////////////////////

    'Truth': {
        'xStart': 0.065,
        'yStart': 0.25,
        'xEnd': 0.115,
        'yEnd': 0.3,
        'activated': False,
        'ending': False,
        'children': ['Coffee', 'No Coffee']
    },
    'Lie': {
        'xStart': 0.165,
        'yStart': 0.25,
        'xEnd': 0.215,
        'yEnd': 0.3,
        'activated': False,
        'ending': True,
        'children': [None]
    },
    'Help': {
        'xStart': 0.245,
        'yStart': 0.25,
        'xEnd': 0.295,
        'yEnd': 0.3,
        'activated': False,
        'ending': True,
        'children': [None]
    },
    "Don't help": {
        'xStart': 0.330,
        'yStart': 0.25,
        'xEnd': 0.410,
        'yEnd': 0.3,
        'activated': False,
        'ending': True,
        'children': [None]
    },
    'Steal': {
        'xStart': 0.425,
        'yStart': 0.25,
        'xEnd': 0.475,
        'yEnd': 0.3,
        'activated': False,
        'ending': True,
        'children': [None]
    },
    'Talk': {
        'xStart': 0.525,
        'yStart': 0.25,
        'xEnd': 0.575,
        'yEnd': 0.3,
        'activated': False,
        'ending': True,
        'children': [None]
    },
    'Escape': {
        'xStart': 0.602,
        'yStart': 0.25,
        'xEnd': 0.658,
        'yEnd': 0.3,
        'activated': False,
        'ending': True,
        'children': [None]
    },
    'Fight': {
        'xStart': 0.705,
        'yStart': 0.25,
        'xEnd': 0.755,
        'yEnd': 0.3,
        'activated': False,
        'ending': True,
        'children': [None]
    },
    'Listen': {
        'xStart': 0.785,
        'yStart': 0.25,
        'xEnd': 0.835,
        'yEnd': 0.3,
        'activated': False,
        'ending': True,
        'children': [None]
    },
    'Hack': {
        'xStart': 0.885,
        'yStart': 0.25,
        'xEnd': 0.935,
        'yEnd': 0.3,
        'activated': False,
        'ending': True,
        'children': [None]
    },

    # //////////////////// LAYER 4 ////////////////////

    'Coffee': {
        'xStart': 0.015,
        'yStart': 0.35,
        'xEnd': 0.065,
        'yEnd': 0.4,
        'activated': False,
        'ending': False,
        'children': ['Chat', "Don't chat"]
    },
    'No Coffee': {
        'xStart': 0.100,
        'yStart': 0.35,
        'xEnd': 0.170,
        'yEnd': 0.4,
        'activated': False,
        'ending': False,
        'children': ['Chat', "Don't chat"]
    },

    # //////////////////// LAYER 5 ////////////////////

    'Chat': {
        'xStart': 0.015,
        'yStart': 0.45,
        'xEnd': 0.065,
        'yEnd': 0.5,
        'activated': False,
        'ending': False,
        'children': ['Reasons']
    },
    "Don't chat": {
        'xStart': 0.100,
        'yStart': 0.45,
        'xEnd': 0.180,
        'yEnd': 0.5,
        'activated': False,
        'ending': False,
        'children': ['Reasons']
    },

    # //////////////////// LAYER 6 ////////////////////

    'Reasons': {
        'xStart': 0.060,
        'yStart': 0.55,
        'xEnd': 0.120,
        'yEnd': 0.6,
        'activated': False,
        'ending': False,
        'children': ['Flee', 'Stay']
    },

    # //////////////////// LAYER 7 ////////////////////

    'Flee': {
        'xStart': 0.065,
        'yStart': 0.65,
        'xEnd': 0.115,
        'yEnd': 0.7,
        'activated': False,
        'ending': False,
        'children': ['Window', 'Stay']
    },

    # //////////////////// LAYER 8 ////////////////////

    'Window': {
        'xStart': 0.060,
        'yStart': 0.75,
        'xEnd': 0.120,
        'yEnd': 0.8,
        'activated': False,
        'ending': False,
        'children': ['Jump', 'Climb']
    },
    'Stay': {
        'xStart': 0.245,
        'yStart': 0.75,
        'xEnd': 0.295,
        'yEnd': 0.8,
        'activated': False,
        'ending': False,
        'children': ['Struggle', 'Knife']
    },

    # //////////////////// LAYER 8 ////////////////////

    'Jump': {
        'xStart': 0.015,
        'yStart': 0.85,
        'xEnd': 0.065,
        'yEnd': 0.9,
        'activated': False,
        'ending': True,
        'children': [None]
    },
    'Climb': {
        'xStart': 0.115,
        'yStart': 0.85,
        'xEnd': 0.165,
        'yEnd': 0.9,
        'activated': False,
        'ending': True,
        'children': [None]
    },
    'Struggle': {
        'xStart': 0.190,
        'yStart': 0.85,
        'xEnd': 0.250,
        'yEnd': 0.9,
        'activated': False,
        'ending': True,
        'children': [None]
    },
    'Knife': {
        'xStart': 0.295,
        'yStart': 0.85,
        'xEnd': 0.345,
        'yEnd': 0.9,
        'activated': False,
        'ending': True,
        'children': [None]
    },
}
