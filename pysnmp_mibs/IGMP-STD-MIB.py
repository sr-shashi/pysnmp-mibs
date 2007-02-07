# PySNMP SMI module. Autogenerated from smidump -f python IGMP-STD-MIB
# by libsmi2pysnmp-0.0.7-alpha at Wed Feb  7 16:12:58 2007,
# Python version (2, 4, 3, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( InterfaceIndex, InterfaceIndexOrZero, ) = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "InterfaceIndexOrZero")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Counter32, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, TimeTicks, Unsigned32, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "TimeTicks", "Unsigned32", "mib-2")
( RowStatus, TruthValue, ) = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TruthValue")

# Objects

igmpStdMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 85)).setRevisions(("2000-09-28 00:00",))
igmpMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 85, 1))
igmpInterfaceTable = MibTable((1, 3, 6, 1, 2, 1, 85, 1, 1))
igmpInterfaceEntry = MibTableRow((1, 3, 6, 1, 2, 1, 85, 1, 1, 1)).setIndexNames((0, "IGMP-STD-MIB", "igmpInterfaceIfIndex"))
igmpInterfaceIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 85, 1, 1, 1, 1), InterfaceIndex()).setMaxAccess("noaccess")
igmpInterfaceQueryInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 85, 1, 1, 1, 2), Unsigned32().clone(125)).setMaxAccess("readcreate")
igmpInterfaceStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 85, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
igmpInterfaceVersion = MibTableColumn((1, 3, 6, 1, 2, 1, 85, 1, 1, 1, 4), Unsigned32().clone(2)).setMaxAccess("readcreate")
igmpInterfaceQuerier = MibTableColumn((1, 3, 6, 1, 2, 1, 85, 1, 1, 1, 5), IpAddress()).setMaxAccess("readonly")
igmpInterfaceQueryMaxResponseTime = MibTableColumn((1, 3, 6, 1, 2, 1, 85, 1, 1, 1, 6), Unsigned32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 255)).clone(100)).setMaxAccess("readcreate")
igmpInterfaceQuerierUpTime = MibTableColumn((1, 3, 6, 1, 2, 1, 85, 1, 1, 1, 7), TimeTicks()).setMaxAccess("readonly")
igmpInterfaceQuerierExpiryTime = MibTableColumn((1, 3, 6, 1, 2, 1, 85, 1, 1, 1, 8), TimeTicks()).setMaxAccess("readonly")
igmpInterfaceVersion1QuerierTimer = MibTableColumn((1, 3, 6, 1, 2, 1, 85, 1, 1, 1, 9), TimeTicks()).setMaxAccess("readonly")
igmpInterfaceWrongVersionQueries = MibTableColumn((1, 3, 6, 1, 2, 1, 85, 1, 1, 1, 10), Counter32()).setMaxAccess("readonly")
igmpInterfaceJoins = MibTableColumn((1, 3, 6, 1, 2, 1, 85, 1, 1, 1, 11), Counter32()).setMaxAccess("readonly")
igmpInterfaceProxyIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 85, 1, 1, 1, 12), InterfaceIndexOrZero().clone(0)).setMaxAccess("readcreate")
igmpInterfaceGroups = MibTableColumn((1, 3, 6, 1, 2, 1, 85, 1, 1, 1, 13), Gauge32()).setMaxAccess("readonly")
igmpInterfaceRobustness = MibTableColumn((1, 3, 6, 1, 2, 1, 85, 1, 1, 1, 14), Unsigned32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 255)).clone(2)).setMaxAccess("readcreate")
igmpInterfaceLastMembQueryIntvl = MibTableColumn((1, 3, 6, 1, 2, 1, 85, 1, 1, 1, 15), Unsigned32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 255)).clone(10)).setMaxAccess("readcreate")
igmpCacheTable = MibTable((1, 3, 6, 1, 2, 1, 85, 1, 2))
igmpCacheEntry = MibTableRow((1, 3, 6, 1, 2, 1, 85, 1, 2, 1)).setIndexNames((0, "IGMP-STD-MIB", "igmpCacheAddress"), (0, "IGMP-STD-MIB", "igmpCacheIfIndex"))
igmpCacheAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 85, 1, 2, 1, 1), IpAddress()).setMaxAccess("noaccess")
igmpCacheIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 85, 1, 2, 1, 2), InterfaceIndex()).setMaxAccess("noaccess")
igmpCacheSelf = MibTableColumn((1, 3, 6, 1, 2, 1, 85, 1, 2, 1, 3), TruthValue().clone('true')).setMaxAccess("readcreate")
igmpCacheLastReporter = MibTableColumn((1, 3, 6, 1, 2, 1, 85, 1, 2, 1, 4), IpAddress()).setMaxAccess("readonly")
igmpCacheUpTime = MibTableColumn((1, 3, 6, 1, 2, 1, 85, 1, 2, 1, 5), TimeTicks()).setMaxAccess("readonly")
igmpCacheExpiryTime = MibTableColumn((1, 3, 6, 1, 2, 1, 85, 1, 2, 1, 6), TimeTicks()).setMaxAccess("readonly")
igmpCacheStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 85, 1, 2, 1, 7), RowStatus()).setMaxAccess("readcreate")
igmpCacheVersion1HostTimer = MibTableColumn((1, 3, 6, 1, 2, 1, 85, 1, 2, 1, 8), TimeTicks()).setMaxAccess("readonly")
igmpMIBConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 85, 2))
igmpMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 85, 2, 1))
igmpMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 85, 2, 2))

# Augmentions

# Groups

igmpV2ProxyMIBGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 85, 2, 2, 6)).setObjects(("IGMP-STD-MIB", "igmpInterfaceProxyIfIndex"), )
igmpHostOptMIBGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 85, 2, 2, 4)).setObjects(("IGMP-STD-MIB", "igmpInterfaceQuerier"), ("IGMP-STD-MIB", "igmpCacheLastReporter"), )
igmpBaseMIBGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 85, 2, 2, 1)).setObjects(("IGMP-STD-MIB", "igmpInterfaceStatus"), ("IGMP-STD-MIB", "igmpCacheSelf"), ("IGMP-STD-MIB", "igmpCacheStatus"), )
igmpV2RouterMIBGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 85, 2, 2, 5)).setObjects(("IGMP-STD-MIB", "igmpInterfaceLastMembQueryIntvl"), ("IGMP-STD-MIB", "igmpInterfaceQueryMaxResponseTime"), ("IGMP-STD-MIB", "igmpCacheVersion1HostTimer"), ("IGMP-STD-MIB", "igmpInterfaceWrongVersionQueries"), ("IGMP-STD-MIB", "igmpInterfaceQuerier"), ("IGMP-STD-MIB", "igmpInterfaceVersion"), ("IGMP-STD-MIB", "igmpInterfaceRobustness"), )
igmpRouterMIBGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 85, 2, 2, 2)).setObjects(("IGMP-STD-MIB", "igmpCacheExpiryTime"), ("IGMP-STD-MIB", "igmpInterfaceQueryInterval"), ("IGMP-STD-MIB", "igmpCacheLastReporter"), ("IGMP-STD-MIB", "igmpInterfaceJoins"), ("IGMP-STD-MIB", "igmpInterfaceQuerierExpiryTime"), ("IGMP-STD-MIB", "igmpInterfaceQuerierUpTime"), ("IGMP-STD-MIB", "igmpCacheUpTime"), ("IGMP-STD-MIB", "igmpInterfaceGroups"), )
igmpV2HostMIBGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 85, 2, 2, 3)).setObjects(("IGMP-STD-MIB", "igmpInterfaceVersion1QuerierTimer"), )

# Exports

# Module identity
mibBuilder.exportSymbols("IGMP-STD-MIB", PYSNMP_MODULE_ID=igmpStdMIB)

# Objects
mibBuilder.exportSymbols("IGMP-STD-MIB", igmpStdMIB=igmpStdMIB, igmpMIBObjects=igmpMIBObjects, igmpInterfaceTable=igmpInterfaceTable, igmpInterfaceEntry=igmpInterfaceEntry, igmpInterfaceIfIndex=igmpInterfaceIfIndex, igmpInterfaceQueryInterval=igmpInterfaceQueryInterval, igmpInterfaceStatus=igmpInterfaceStatus, igmpInterfaceVersion=igmpInterfaceVersion, igmpInterfaceQuerier=igmpInterfaceQuerier, igmpInterfaceQueryMaxResponseTime=igmpInterfaceQueryMaxResponseTime, igmpInterfaceQuerierUpTime=igmpInterfaceQuerierUpTime, igmpInterfaceQuerierExpiryTime=igmpInterfaceQuerierExpiryTime, igmpInterfaceVersion1QuerierTimer=igmpInterfaceVersion1QuerierTimer, igmpInterfaceWrongVersionQueries=igmpInterfaceWrongVersionQueries, igmpInterfaceJoins=igmpInterfaceJoins, igmpInterfaceProxyIfIndex=igmpInterfaceProxyIfIndex, igmpInterfaceGroups=igmpInterfaceGroups, igmpInterfaceRobustness=igmpInterfaceRobustness, igmpInterfaceLastMembQueryIntvl=igmpInterfaceLastMembQueryIntvl, igmpCacheTable=igmpCacheTable, igmpCacheEntry=igmpCacheEntry, igmpCacheAddress=igmpCacheAddress, igmpCacheIfIndex=igmpCacheIfIndex, igmpCacheSelf=igmpCacheSelf, igmpCacheLastReporter=igmpCacheLastReporter, igmpCacheUpTime=igmpCacheUpTime, igmpCacheExpiryTime=igmpCacheExpiryTime, igmpCacheStatus=igmpCacheStatus, igmpCacheVersion1HostTimer=igmpCacheVersion1HostTimer, igmpMIBConformance=igmpMIBConformance, igmpMIBCompliances=igmpMIBCompliances, igmpMIBGroups=igmpMIBGroups)

# Groups
mibBuilder.exportSymbols("IGMP-STD-MIB", igmpV2ProxyMIBGroup=igmpV2ProxyMIBGroup, igmpHostOptMIBGroup=igmpHostOptMIBGroup, igmpBaseMIBGroup=igmpBaseMIBGroup, igmpV2RouterMIBGroup=igmpV2RouterMIBGroup, igmpRouterMIBGroup=igmpRouterMIBGroup, igmpV2HostMIBGroup=igmpV2HostMIBGroup)
