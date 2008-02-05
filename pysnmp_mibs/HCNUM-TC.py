# PySNMP SMI module. Autogenerated from smidump -f python HCNUM-TC
# by libsmi2pysnmp-0.0.8-alpha at Tue Feb  5 21:05:07 2008,
# Python version (2, 4, 4, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( Bits, Counter64, Integer32, ModuleIdentity, MibIdentifier, TimeTicks, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter64", "Integer32", "ModuleIdentity", "MibIdentifier", "TimeTicks", "mib-2")
( TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention")

# Types

class CounterBasedGauge64(Counter64):
    pass

class ZeroBasedCounter64(Counter64):
    pass


# Objects

hcnumTC = ModuleIdentity((1, 3, 6, 1, 2, 1, 78)).setRevisions(("2000-06-08 00:00",))
if mibBuilder.loadTexts: hcnumTC.setOrganization("IETF OPS Area")
if mibBuilder.loadTexts: hcnumTC.setContactInfo("        E-mail: mibs@ops.ietf.org\nSubscribe: majordomo@psg.com\n  with msg body: subscribe mibs\n\nAndy Bierman\nCisco Systems Inc.\n170 West Tasman Drive\nSan Jose, CA 95134 USA\n+1 408-527-3711\nabierman@cisco.com\n\nKeith McCloghrie\nCisco Systems Inc.\n170 West Tasman Drive\nSan Jose, CA 95134 USA\n+1 408-526-5260\nkzm@cisco.com\n\nRandy Presuhn\nBMC Software, Inc.\nOffice 1-3141\n2141 North First Street\nSan Jose,  California 95131 USA\n+1 408 546-1006\nrpresuhn@bmc.com")
if mibBuilder.loadTexts: hcnumTC.setDescription("A MIB module containing textual conventions\nfor high capacity data types. This module\naddresses an immediate need for data types not directly\nsupported in the SMIv2. This short-term solution\nis meant to be deprecated as a long-term solution\nis deployed.")

# Augmentions

# Exports

# Module identity
mibBuilder.exportSymbols("HCNUM-TC", PYSNMP_MODULE_ID=hcnumTC)

# Types
mibBuilder.exportSymbols("HCNUM-TC", CounterBasedGauge64=CounterBasedGauge64, ZeroBasedCounter64=ZeroBasedCounter64)

# Objects
mibBuilder.exportSymbols("HCNUM-TC", hcnumTC=hcnumTC)

