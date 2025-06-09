# neutron_reaction

This repository contains a very small demonstration of serving a home page and an isotope selection page.

Two Python scripts are provided:

- `home.py` - starts a small Flask web application. The home page links to the [NUBASE](https://www-nds.iaea.org/nubase/nubase2020.htm) dataset and shows that isotope properties can be obtained from NUBASE.
- `select_nuclides.py` - provides the helper function `load_isotopes()` that reads `web/isotopes.json` to determine the list of isotopes that can be selected.

Running `python home.py` will start a local server with two routes:

- `/` for the main page with the NUBASE link.
- `/isotopes` which lists all isotopes from `isotopes.json`.

The list of available isotopes can be changed by editing `web/isotopes.json`.
