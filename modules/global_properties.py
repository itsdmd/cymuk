# Holds Global Properties That Shares Across Modules

from pkg_resources import require
from os import environ

version = require("cymuk")[0].version


def init():
    environ["CYMUK_VERBOSE"] = "False"


def set_verbose():
    environ["CYMUK_VERBOSE"] = "True"


def get_verbose():
    return environ.get("CYMUK_VERBOSE")


def get_version():
    return version
