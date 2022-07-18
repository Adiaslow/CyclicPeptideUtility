#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
This program is intended to automate the production process of peptide libraries (cyclic or linear) in silico.

Peptide libraries can be created by putting .csv file in the input folder. Single peptides can be made in the
text-based user interface or by putting .csv file with only a single row of subunits in the input folder.
"""

from scripts import header as h

__author__ = 'Adam Murray'
__contact__ = "admmurra@ucsc.edu"
__credits__ = ['']
__date__ = "2022/07/17"
__version__ = '0.1.0'
__maintainer__ = 'Developer'
__email__ = 'admmurra@ucsc.edu'
__status__ = 'Development'


if __name__ == '__main__':
    h.ui.ui_loop({})

# References
# Peptide Annotation
# https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6149970/

# SMILES Guide
# https://www.epa.gov/sites/production/files/2015-05/documents/appendf.pdf

# Amino Acids
# https://www.peptide.com/resources/solid-phase-peptide-synthesis/amino-acid-derivatives-for-peptide-synthesis/amino-acid-abbreviations/
