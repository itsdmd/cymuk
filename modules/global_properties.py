# Holds Global Properties That Shares Across Modules

from pkg_resources import require

verbose = False
version = require("cymuk")[0].version


def set_verbose():
    global verbose
    verbose = True


def get_version():
    return version
