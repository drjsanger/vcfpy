# -*- coding: utf-8 -*-

try:
    from cyordereddict import OrderedDict
except ImportError:
    from collections import OrderedDict

from .exceptions import VCFPyException, InvalidHeaderException, \
    InvalidRecordException, IncorrectVCFFormat, HeaderNotFound

from .header import Header, HeaderLine, SimpleHeaderLine, \
    AltAlleleHeaderLine, ContigHeaderLine, FilterHeaderLine, MetaHeaderLine, \
    PedigreeHeaderLine, SampleHeaderLine, CompoundHeaderLine, InfoHeaderLine, \
    FormatHeaderLine, SamplesInfos, FieldInfo, header_without_lines

from .record import Record, Call, AltRecord, Substitution, BreakEnd, \
    SingleBreakEnd, SymbolicAllele

from .record import SNV, MNV, DEL, INS, INDEL, SV, BND, SYMBOLIC, MIXED
from .record import HOM_REF, HET, HOM_ALT
from .record import FIVE_PRIME, THREE_PRIME, FORWARD, REVERSE

from .reader import Reader

from .writer import Writer

__version__ = '0.6.0'
