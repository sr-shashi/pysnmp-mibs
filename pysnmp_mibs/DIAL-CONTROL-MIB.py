# PySNMP SMI module. Autogenerated from smidump -f python DIAL-CONTROL-MIB
# by libsmi2pysnmp-0.0.7-alpha at Wed Feb  7 16:12:47 2007,
# Python version (2, 4, 3, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( IANAifType, ) = mibBuilder.importSymbols("IANAifType-MIB", "IANAifType")
( InterfaceIndex, InterfaceIndexOrZero, ifIndex, ifOperStatus, ) = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "InterfaceIndexOrZero", "ifIndex", "ifOperStatus")
( transmission, ) = mibBuilder.importSymbols("RFC1213-MIB", "transmission")
( ModuleCompliance, NotificationGroup, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
( Bits, Integer32, Integer32, ModuleIdentity, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32")
( DisplayString, RowStatus, TextualConvention, TimeStamp, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention", "TimeStamp")

# Types

class AbsoluteCounter32(Unsigned32):
    pass


# Objects

dialControlMib = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 21)).setRevisions(("1996-09-23 15:44",))
dialControlMibObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 21, 1))
dialCtlConfiguration = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 21, 1, 1))
dialCtlAcceptMode = MibScalar((1, 3, 6, 1, 2, 1, 10, 21, 1, 1, 1), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,3,)).subtype(namedValues=namedval.NamedValues(("acceptNone", 1), ("acceptAll", 2), ("acceptKnown", 3), ))).setMaxAccess("readwrite")
dialCtlTrapEnable = MibScalar((1, 3, 6, 1, 2, 1, 10, 21, 1, 1, 2), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("enabled", 1), ("disabled", 2), )).clone(2)).setMaxAccess("readwrite")
dialCtlPeer = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 21, 1, 2))
dialCtlPeerCfgTable = MibTable((1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 1))
dialCtlPeerCfgEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 1, 1)).setIndexNames((0, "DIAL-CONTROL-MIB", "dialCtlPeerCfgId"), (0, "IF-MIB", "ifIndex"))
dialCtlPeerCfgId = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 2147483647L))).setMaxAccess("noaccess")
dialCtlPeerCfgIfType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 1, 1, 2), IANAifType().clone('other')).setMaxAccess("readcreate")
dialCtlPeerCfgLowerIf = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 1, 1, 3), InterfaceIndexOrZero().clone(0)).setMaxAccess("readcreate")
dialCtlPeerCfgOriginateAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 1, 1, 4), DisplayString()).setMaxAccess("readcreate")
dialCtlPeerCfgAnswerAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 1, 1, 5), DisplayString().clone('')).setMaxAccess("readcreate")
dialCtlPeerCfgSubAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 1, 1, 6), DisplayString().clone('')).setMaxAccess("readcreate")
dialCtlPeerCfgClosedUserGroup = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 1, 1, 7), DisplayString().clone('')).setMaxAccess("readcreate")
dialCtlPeerCfgSpeed = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 2147483647L)).clone(0)).setMaxAccess("readcreate")
dialCtlPeerCfgInfoType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 1, 1, 9), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(10,3,4,7,5,6,1,2,9,8,)).subtype(namedValues=namedval.NamedValues(("other", 1), ("fax", 10), ("speech", 2), ("unrestrictedDigital", 3), ("unrestrictedDigital56", 4), ("restrictedDigital", 5), ("audio31", 6), ("audio7", 7), ("video", 8), ("packetSwitched", 9), )).clone(1)).setMaxAccess("readcreate")
dialCtlPeerCfgPermission = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 1, 1, 10), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(3,5,1,4,2,)).subtype(namedValues=namedval.NamedValues(("originate", 1), ("answer", 2), ("both", 3), ("callback", 4), ("none", 5), )).clone(3)).setMaxAccess("readcreate")
dialCtlPeerCfgInactivityTimer = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 1, 1, 11), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 2147483647L)).clone(0)).setMaxAccess("readcreate")
dialCtlPeerCfgMinDuration = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 1, 1, 12), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 2147483647L)).clone(0)).setMaxAccess("readcreate")
dialCtlPeerCfgMaxDuration = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 1, 1, 13), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 2147483647L)).clone(0)).setMaxAccess("readcreate")
dialCtlPeerCfgCarrierDelay = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 1, 1, 14), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 2147483647L)).clone(0)).setMaxAccess("readcreate")
dialCtlPeerCfgCallRetries = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 1, 1, 15), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 2147483647L)).clone(0)).setMaxAccess("readcreate")
dialCtlPeerCfgRetryDelay = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 1, 1, 16), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 2147483647L)).clone(0)).setMaxAccess("readcreate")
dialCtlPeerCfgFailureDelay = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 1, 1, 17), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 2147483647L)).clone(0)).setMaxAccess("readcreate")
dialCtlPeerCfgTrapEnable = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 1, 1, 18), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("enabled", 1), ("disabled", 2), )).clone(2)).setMaxAccess("readcreate")
dialCtlPeerCfgStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 1, 1, 19), RowStatus()).setMaxAccess("readcreate")
dialCtlPeerStatsTable = MibTable((1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 2))
dialCtlPeerStatsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 2, 1))
dialCtlPeerStatsConnectTime = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 2, 1, 1), AbsoluteCounter32()).setMaxAccess("readonly")
dialCtlPeerStatsChargedUnits = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 2, 1, 2), AbsoluteCounter32()).setMaxAccess("readonly")
dialCtlPeerStatsSuccessCalls = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 2, 1, 3), AbsoluteCounter32()).setMaxAccess("readonly")
dialCtlPeerStatsFailCalls = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 2, 1, 4), AbsoluteCounter32()).setMaxAccess("readonly")
dialCtlPeerStatsAcceptCalls = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 2, 1, 5), AbsoluteCounter32()).setMaxAccess("readonly")
dialCtlPeerStatsRefuseCalls = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 2, 1, 6), AbsoluteCounter32()).setMaxAccess("readonly")
dialCtlPeerStatsLastDisconnectCause = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 2, 1, 7), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 4))).setMaxAccess("readonly")
dialCtlPeerStatsLastDisconnectText = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 2, 1, 8), DisplayString()).setMaxAccess("readonly")
dialCtlPeerStatsLastSetupTime = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 2, 1, 9), TimeStamp()).setMaxAccess("readonly")
callActive = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 21, 1, 3))
callActiveTable = MibTable((1, 3, 6, 1, 2, 1, 10, 21, 1, 3, 1))
callActiveEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 21, 1, 3, 1, 1)).setIndexNames((0, "DIAL-CONTROL-MIB", "callActiveSetupTime"), (0, "DIAL-CONTROL-MIB", "callActiveIndex"))
callActiveSetupTime = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 3, 1, 1, 1), TimeStamp()).setMaxAccess("noaccess")
callActiveIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 2147483647L))).setMaxAccess("noaccess")
callActivePeerAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 3, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
callActivePeerSubAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 3, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
callActivePeerId = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 2147483647L))).setMaxAccess("readonly")
callActivePeerIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 3, 1, 1, 6), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 2147483647L))).setMaxAccess("readonly")
callActiveLogicalIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 3, 1, 1, 7), InterfaceIndexOrZero()).setMaxAccess("readonly")
callActiveConnectTime = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 3, 1, 1, 8), TimeStamp()).setMaxAccess("readonly")
callActiveCallState = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 3, 1, 1, 9), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,3,4,2,)).subtype(namedValues=namedval.NamedValues(("unknown", 1), ("connecting", 2), ("connected", 3), ("active", 4), ))).setMaxAccess("readonly")
callActiveCallOrigin = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 3, 1, 1, 10), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,3,)).subtype(namedValues=namedval.NamedValues(("originate", 1), ("answer", 2), ("callback", 3), ))).setMaxAccess("readonly")
callActiveChargedUnits = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 3, 1, 1, 11), AbsoluteCounter32()).setMaxAccess("readonly")
callActiveInfoType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 3, 1, 1, 12), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(10,3,4,7,5,6,1,2,9,8,)).subtype(namedValues=namedval.NamedValues(("other", 1), ("fax", 10), ("speech", 2), ("unrestrictedDigital", 3), ("unrestrictedDigital56", 4), ("restrictedDigital", 5), ("audio31", 6), ("audio7", 7), ("video", 8), ("packetSwitched", 9), ))).setMaxAccess("readonly")
callActiveTransmitPackets = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 3, 1, 1, 13), AbsoluteCounter32()).setMaxAccess("readonly")
callActiveTransmitBytes = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 3, 1, 1, 14), AbsoluteCounter32()).setMaxAccess("readonly")
callActiveReceivePackets = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 3, 1, 1, 15), AbsoluteCounter32()).setMaxAccess("readonly")
callActiveReceiveBytes = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 3, 1, 1, 16), AbsoluteCounter32()).setMaxAccess("readonly")
callHistory = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 21, 1, 4))
callHistoryTableMaxLength = MibScalar((1, 3, 6, 1, 2, 1, 10, 21, 1, 4, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 2147483647L))).setMaxAccess("readwrite")
callHistoryRetainTimer = MibScalar((1, 3, 6, 1, 2, 1, 10, 21, 1, 4, 2), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 2147483647L))).setMaxAccess("readwrite").setUnits("minutes")
callHistoryTable = MibTable((1, 3, 6, 1, 2, 1, 10, 21, 1, 4, 3))
callHistoryEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 21, 1, 4, 3, 1)).setIndexNames((0, "DIAL-CONTROL-MIB", "callActiveSetupTime"), (0, "DIAL-CONTROL-MIB", "callActiveIndex"))
callHistoryPeerAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 4, 3, 1, 1), DisplayString()).setMaxAccess("readonly")
callHistoryPeerSubAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 4, 3, 1, 2), DisplayString()).setMaxAccess("readonly")
callHistoryPeerId = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 4, 3, 1, 3), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 2147483647L))).setMaxAccess("readonly")
callHistoryPeerIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 4, 3, 1, 4), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 2147483647L))).setMaxAccess("readonly")
callHistoryLogicalIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 4, 3, 1, 5), InterfaceIndex()).setMaxAccess("readonly")
callHistoryDisconnectCause = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 4, 3, 1, 6), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 4))).setMaxAccess("readonly")
callHistoryDisconnectText = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 4, 3, 1, 7), DisplayString()).setMaxAccess("readonly")
callHistoryConnectTime = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 4, 3, 1, 8), TimeStamp()).setMaxAccess("readonly")
callHistoryDisconnectTime = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 4, 3, 1, 9), TimeStamp()).setMaxAccess("readonly")
callHistoryCallOrigin = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 4, 3, 1, 10), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,3,)).subtype(namedValues=namedval.NamedValues(("originate", 1), ("answer", 2), ("callback", 3), ))).setMaxAccess("readonly")
callHistoryChargedUnits = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 4, 3, 1, 11), AbsoluteCounter32()).setMaxAccess("readonly")
callHistoryInfoType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 4, 3, 1, 12), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(10,3,4,7,5,6,1,2,9,8,)).subtype(namedValues=namedval.NamedValues(("other", 1), ("fax", 10), ("speech", 2), ("unrestrictedDigital", 3), ("unrestrictedDigital56", 4), ("restrictedDigital", 5), ("audio31", 6), ("audio7", 7), ("video", 8), ("packetSwitched", 9), ))).setMaxAccess("readonly")
callHistoryTransmitPackets = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 4, 3, 1, 13), AbsoluteCounter32()).setMaxAccess("readonly")
callHistoryTransmitBytes = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 4, 3, 1, 14), AbsoluteCounter32()).setMaxAccess("readonly")
callHistoryReceivePackets = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 4, 3, 1, 15), AbsoluteCounter32()).setMaxAccess("readonly")
callHistoryReceiveBytes = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 4, 3, 1, 16), AbsoluteCounter32()).setMaxAccess("readonly")
dialControlMibTrapPrefix = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 21, 2))
dialControlMibTraps = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 21, 2, 0))
dialControlMibConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 21, 3))
dialControlMibCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 21, 3, 1))
dialControlMibGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 21, 3, 2))

# Augmentions
dialCtlPeerCfgEntry.registerAugmentions(("DIAL-CONTROL-MIB", "dialCtlPeerStatsEntry"))
apply(dialCtlPeerStatsEntry.setIndexNames, dialCtlPeerCfgEntry.getIndexNames())

# Notifications

dialCtlPeerCallSetup = NotificationType((1, 3, 6, 1, 2, 1, 10, 21, 2, 0, 2)).setObjects(("DIAL-CONTROL-MIB", "callActivePeerAddress"), ("DIAL-CONTROL-MIB", "callActivePeerId"), ("DIAL-CONTROL-MIB", "callActivePeerSubAddress"), ("DIAL-CONTROL-MIB", "callActivePeerIfIndex"), ("DIAL-CONTROL-MIB", "callActiveLogicalIfIndex"), ("DIAL-CONTROL-MIB", "callActiveInfoType"), ("DIAL-CONTROL-MIB", "callActiveCallOrigin"), ("IF-MIB", "ifOperStatus"), )
dialCtlPeerCallInformation = NotificationType((1, 3, 6, 1, 2, 1, 10, 21, 2, 0, 1)).setObjects(("DIAL-CONTROL-MIB", "callHistoryDisconnectCause"), ("DIAL-CONTROL-MIB", "callHistoryCallOrigin"), ("DIAL-CONTROL-MIB", "callHistoryLogicalIfIndex"), ("DIAL-CONTROL-MIB", "callHistoryInfoType"), ("DIAL-CONTROL-MIB", "callHistoryPeerSubAddress"), ("DIAL-CONTROL-MIB", "callHistoryPeerIfIndex"), ("DIAL-CONTROL-MIB", "callHistoryPeerAddress"), ("DIAL-CONTROL-MIB", "callHistoryDisconnectTime"), ("DIAL-CONTROL-MIB", "callHistoryPeerId"), ("DIAL-CONTROL-MIB", "callHistoryConnectTime"), ("IF-MIB", "ifOperStatus"), )

# Groups

callActiveGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 21, 3, 2, 2)).setObjects(("DIAL-CONTROL-MIB", "callActiveReceivePackets"), ("DIAL-CONTROL-MIB", "callActiveCallState"), ("DIAL-CONTROL-MIB", "callActivePeerAddress"), ("DIAL-CONTROL-MIB", "callActiveTransmitPackets"), ("DIAL-CONTROL-MIB", "callActiveReceiveBytes"), ("DIAL-CONTROL-MIB", "callActivePeerId"), ("DIAL-CONTROL-MIB", "callActiveInfoType"), ("DIAL-CONTROL-MIB", "callActivePeerSubAddress"), ("DIAL-CONTROL-MIB", "callActivePeerIfIndex"), ("DIAL-CONTROL-MIB", "callActiveLogicalIfIndex"), ("DIAL-CONTROL-MIB", "callActiveTransmitBytes"), ("DIAL-CONTROL-MIB", "callActiveChargedUnits"), ("DIAL-CONTROL-MIB", "callActiveCallOrigin"), ("DIAL-CONTROL-MIB", "callActiveConnectTime"), )
callHistoryGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 21, 3, 2, 3)).setObjects(("DIAL-CONTROL-MIB", "callHistoryReceiveBytes"), ("DIAL-CONTROL-MIB", "callHistoryDisconnectCause"), ("DIAL-CONTROL-MIB", "callHistoryCallOrigin"), ("DIAL-CONTROL-MIB", "callHistoryReceivePackets"), ("DIAL-CONTROL-MIB", "callHistoryLogicalIfIndex"), ("DIAL-CONTROL-MIB", "callHistoryInfoType"), ("DIAL-CONTROL-MIB", "callHistoryTransmitPackets"), ("DIAL-CONTROL-MIB", "callHistoryDisconnectText"), ("DIAL-CONTROL-MIB", "callHistoryPeerSubAddress"), ("DIAL-CONTROL-MIB", "callHistoryPeerIfIndex"), ("DIAL-CONTROL-MIB", "callHistoryRetainTimer"), ("DIAL-CONTROL-MIB", "callHistoryPeerAddress"), ("DIAL-CONTROL-MIB", "callHistoryTableMaxLength"), ("DIAL-CONTROL-MIB", "callHistoryTransmitBytes"), ("DIAL-CONTROL-MIB", "callHistoryDisconnectTime"), ("DIAL-CONTROL-MIB", "callHistoryPeerId"), ("DIAL-CONTROL-MIB", "callHistoryConnectTime"), ("DIAL-CONTROL-MIB", "callHistoryChargedUnits"), )
dialControlGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 21, 3, 2, 1)).setObjects(("DIAL-CONTROL-MIB", "dialCtlPeerCfgIfType"), ("DIAL-CONTROL-MIB", "dialCtlPeerCfgPermission"), ("DIAL-CONTROL-MIB", "dialCtlPeerCfgClosedUserGroup"), ("DIAL-CONTROL-MIB", "dialCtlPeerCfgCarrierDelay"), ("DIAL-CONTROL-MIB", "dialCtlPeerCfgLowerIf"), ("DIAL-CONTROL-MIB", "dialCtlPeerCfgOriginateAddress"), ("DIAL-CONTROL-MIB", "dialCtlPeerCfgRetryDelay"), ("DIAL-CONTROL-MIB", "dialCtlPeerStatsLastDisconnectText"), ("DIAL-CONTROL-MIB", "dialCtlPeerCfgMaxDuration"), ("DIAL-CONTROL-MIB", "dialCtlTrapEnable"), ("DIAL-CONTROL-MIB", "dialCtlAcceptMode"), ("DIAL-CONTROL-MIB", "dialCtlPeerStatsConnectTime"), ("DIAL-CONTROL-MIB", "dialCtlPeerStatsAcceptCalls"), ("DIAL-CONTROL-MIB", "dialCtlPeerCfgSpeed"), ("DIAL-CONTROL-MIB", "dialCtlPeerStatsSuccessCalls"), ("DIAL-CONTROL-MIB", "dialCtlPeerStatsRefuseCalls"), ("DIAL-CONTROL-MIB", "dialCtlPeerCfgCallRetries"), ("DIAL-CONTROL-MIB", "dialCtlPeerStatsChargedUnits"), ("DIAL-CONTROL-MIB", "dialCtlPeerCfgStatus"), ("DIAL-CONTROL-MIB", "dialCtlPeerStatsLastSetupTime"), ("DIAL-CONTROL-MIB", "dialCtlPeerCfgMinDuration"), ("DIAL-CONTROL-MIB", "dialCtlPeerCfgSubAddress"), ("DIAL-CONTROL-MIB", "dialCtlPeerCfgAnswerAddress"), ("DIAL-CONTROL-MIB", "dialCtlPeerStatsFailCalls"), ("DIAL-CONTROL-MIB", "dialCtlPeerStatsLastDisconnectCause"), ("DIAL-CONTROL-MIB", "dialCtlPeerCfgInactivityTimer"), ("DIAL-CONTROL-MIB", "dialCtlPeerCfgTrapEnable"), ("DIAL-CONTROL-MIB", "dialCtlPeerCfgFailureDelay"), ("DIAL-CONTROL-MIB", "dialCtlPeerCfgInfoType"), )
callNotificationsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 21, 3, 2, 4)).setObjects(("DIAL-CONTROL-MIB", "dialCtlPeerCallSetup"), ("DIAL-CONTROL-MIB", "dialCtlPeerCallInformation"), )

# Exports

# Module identity
mibBuilder.exportSymbols("DIAL-CONTROL-MIB", PYSNMP_MODULE_ID=dialControlMib)

# Types
mibBuilder.exportSymbols("DIAL-CONTROL-MIB", AbsoluteCounter32=AbsoluteCounter32)

# Objects
mibBuilder.exportSymbols("DIAL-CONTROL-MIB", dialControlMib=dialControlMib, dialControlMibObjects=dialControlMibObjects, dialCtlConfiguration=dialCtlConfiguration, dialCtlAcceptMode=dialCtlAcceptMode, dialCtlTrapEnable=dialCtlTrapEnable, dialCtlPeer=dialCtlPeer, dialCtlPeerCfgTable=dialCtlPeerCfgTable, dialCtlPeerCfgEntry=dialCtlPeerCfgEntry, dialCtlPeerCfgId=dialCtlPeerCfgId, dialCtlPeerCfgIfType=dialCtlPeerCfgIfType, dialCtlPeerCfgLowerIf=dialCtlPeerCfgLowerIf, dialCtlPeerCfgOriginateAddress=dialCtlPeerCfgOriginateAddress, dialCtlPeerCfgAnswerAddress=dialCtlPeerCfgAnswerAddress, dialCtlPeerCfgSubAddress=dialCtlPeerCfgSubAddress, dialCtlPeerCfgClosedUserGroup=dialCtlPeerCfgClosedUserGroup, dialCtlPeerCfgSpeed=dialCtlPeerCfgSpeed, dialCtlPeerCfgInfoType=dialCtlPeerCfgInfoType, dialCtlPeerCfgPermission=dialCtlPeerCfgPermission, dialCtlPeerCfgInactivityTimer=dialCtlPeerCfgInactivityTimer, dialCtlPeerCfgMinDuration=dialCtlPeerCfgMinDuration, dialCtlPeerCfgMaxDuration=dialCtlPeerCfgMaxDuration, dialCtlPeerCfgCarrierDelay=dialCtlPeerCfgCarrierDelay, dialCtlPeerCfgCallRetries=dialCtlPeerCfgCallRetries, dialCtlPeerCfgRetryDelay=dialCtlPeerCfgRetryDelay, dialCtlPeerCfgFailureDelay=dialCtlPeerCfgFailureDelay, dialCtlPeerCfgTrapEnable=dialCtlPeerCfgTrapEnable, dialCtlPeerCfgStatus=dialCtlPeerCfgStatus, dialCtlPeerStatsTable=dialCtlPeerStatsTable, dialCtlPeerStatsEntry=dialCtlPeerStatsEntry, dialCtlPeerStatsConnectTime=dialCtlPeerStatsConnectTime, dialCtlPeerStatsChargedUnits=dialCtlPeerStatsChargedUnits, dialCtlPeerStatsSuccessCalls=dialCtlPeerStatsSuccessCalls, dialCtlPeerStatsFailCalls=dialCtlPeerStatsFailCalls, dialCtlPeerStatsAcceptCalls=dialCtlPeerStatsAcceptCalls, dialCtlPeerStatsRefuseCalls=dialCtlPeerStatsRefuseCalls, dialCtlPeerStatsLastDisconnectCause=dialCtlPeerStatsLastDisconnectCause, dialCtlPeerStatsLastDisconnectText=dialCtlPeerStatsLastDisconnectText, dialCtlPeerStatsLastSetupTime=dialCtlPeerStatsLastSetupTime, callActive=callActive, callActiveTable=callActiveTable, callActiveEntry=callActiveEntry, callActiveSetupTime=callActiveSetupTime, callActiveIndex=callActiveIndex, callActivePeerAddress=callActivePeerAddress, callActivePeerSubAddress=callActivePeerSubAddress, callActivePeerId=callActivePeerId, callActivePeerIfIndex=callActivePeerIfIndex, callActiveLogicalIfIndex=callActiveLogicalIfIndex, callActiveConnectTime=callActiveConnectTime, callActiveCallState=callActiveCallState, callActiveCallOrigin=callActiveCallOrigin, callActiveChargedUnits=callActiveChargedUnits, callActiveInfoType=callActiveInfoType, callActiveTransmitPackets=callActiveTransmitPackets, callActiveTransmitBytes=callActiveTransmitBytes, callActiveReceivePackets=callActiveReceivePackets, callActiveReceiveBytes=callActiveReceiveBytes, callHistory=callHistory, callHistoryTableMaxLength=callHistoryTableMaxLength, callHistoryRetainTimer=callHistoryRetainTimer, callHistoryTable=callHistoryTable, callHistoryEntry=callHistoryEntry, callHistoryPeerAddress=callHistoryPeerAddress, callHistoryPeerSubAddress=callHistoryPeerSubAddress, callHistoryPeerId=callHistoryPeerId, callHistoryPeerIfIndex=callHistoryPeerIfIndex, callHistoryLogicalIfIndex=callHistoryLogicalIfIndex, callHistoryDisconnectCause=callHistoryDisconnectCause, callHistoryDisconnectText=callHistoryDisconnectText, callHistoryConnectTime=callHistoryConnectTime, callHistoryDisconnectTime=callHistoryDisconnectTime, callHistoryCallOrigin=callHistoryCallOrigin, callHistoryChargedUnits=callHistoryChargedUnits, callHistoryInfoType=callHistoryInfoType, callHistoryTransmitPackets=callHistoryTransmitPackets, callHistoryTransmitBytes=callHistoryTransmitBytes, callHistoryReceivePackets=callHistoryReceivePackets, callHistoryReceiveBytes=callHistoryReceiveBytes, dialControlMibTrapPrefix=dialControlMibTrapPrefix, dialControlMibTraps=dialControlMibTraps, dialControlMibConformance=dialControlMibConformance, dialControlMibCompliances=dialControlMibCompliances, dialControlMibGroups=dialControlMibGroups)

# Notifications
mibBuilder.exportSymbols("DIAL-CONTROL-MIB", dialCtlPeerCallSetup=dialCtlPeerCallSetup, dialCtlPeerCallInformation=dialCtlPeerCallInformation)

# Groups
mibBuilder.exportSymbols("DIAL-CONTROL-MIB", callActiveGroup=callActiveGroup, callHistoryGroup=callHistoryGroup, dialControlGroup=dialControlGroup, callNotificationsGroup=callNotificationsGroup)
