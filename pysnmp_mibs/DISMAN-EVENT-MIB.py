# PySNMP SMI module. Autogenerated from smidump -f python DISMAN-EVENT-MIB
# by libsmi2pysnmp-0.0.7-alpha at Wed Feb  7 16:12:48 2007,
# Python version (2, 4, 3, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( SnmpAdminString, ) = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
( SnmpTagValue, ) = mibBuilder.importSymbols("SNMP-TARGET-MIB", "SnmpTagValue")
( ModuleCompliance, NotificationGroup, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
( sysUpTime, ) = mibBuilder.importSymbols("SNMPv2-MIB", "sysUpTime")
( Bits, Counter32, Gauge32, Integer32, Integer32, ModuleIdentity, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, mib_2, zeroDotZero, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Gauge32", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "mib-2", "zeroDotZero")
( RowStatus, TextualConvention, TruthValue, ) = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "TruthValue")

# Types

class FailureReason(Integer):
    subtypeSpec = Integer.subtypeSpec+constraint.SingleValueConstraint(18,8,13,7,6,15,11,0,17,3,5,-1,9,4,14,10,-6,-2,-4,2,-3,12,16,1,-5,)
    namedValues = namedval.NamedValues(("localResourceLack", -1), ("badDestination", -2), ("destinationUnreachable", -3), ("noResponse", -4), ("badType", -5), ("sampleOverrun", -6), ("noError", 0), ("tooBig", 1), ("wrongValue", 10), ("noCreation", 11), ("inconsistentValue", 12), ("resourceUnavailable", 13), ("commitFailed", 14), ("undoFailed", 15), ("authorizationError", 16), ("notWritable", 17), ("inconsistentName", 18), ("noSuchName", 2), ("badValue", 3), ("readOnly", 4), ("genErr", 5), ("noAccess", 6), ("wrongType", 7), ("wrongLength", 8), ("wrongEncoding", 9), )
    pass


# Objects

sysUpTimeInstance = MibIdentifier((1, 3, 6, 1, 2, 1, 1, 3, 0))
dismanEventMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 88)).setRevisions(("2000-10-16 00:00",))
dismanEventMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 88, 1))
mteResource = MibIdentifier((1, 3, 6, 1, 2, 1, 88, 1, 1))
mteResourceSampleMinimum = MibScalar((1, 3, 6, 1, 2, 1, 88, 1, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 2147483647L))).setMaxAccess("readwrite").setUnits("seconds")
mteResourceSampleInstanceMaximum = MibScalar((1, 3, 6, 1, 2, 1, 88, 1, 1, 2), Unsigned32()).setMaxAccess("readwrite").setUnits("instances")
mteResourceSampleInstances = MibScalar((1, 3, 6, 1, 2, 1, 88, 1, 1, 3), Gauge32()).setMaxAccess("readonly").setUnits("instances")
mteResourceSampleInstancesHigh = MibScalar((1, 3, 6, 1, 2, 1, 88, 1, 1, 4), Gauge32()).setMaxAccess("readonly").setUnits("instances")
mteResourceSampleInstanceLacks = MibScalar((1, 3, 6, 1, 2, 1, 88, 1, 1, 5), Counter32()).setMaxAccess("readonly").setUnits("instances")
mteTrigger = MibIdentifier((1, 3, 6, 1, 2, 1, 88, 1, 2))
mteTriggerFailures = MibScalar((1, 3, 6, 1, 2, 1, 88, 1, 2, 1), Counter32()).setMaxAccess("readonly").setUnits("failures")
mteTriggerTable = MibTable((1, 3, 6, 1, 2, 1, 88, 1, 2, 2))
mteTriggerEntry = MibTableRow((1, 3, 6, 1, 2, 1, 88, 1, 2, 2, 1)).setIndexNames((0, "DISMAN-EVENT-MIB", "mteOwner"), (1, "DISMAN-EVENT-MIB", "mteTriggerName"))
mteOwner = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 2, 1, 1), SnmpAdminString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 32))).setMaxAccess("noaccess")
mteTriggerName = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 2, 1, 2), SnmpAdminString().subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 32))).setMaxAccess("noaccess")
mteTriggerComment = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 2, 1, 3), SnmpAdminString().clone('')).setMaxAccess("readcreate")
mteTriggerTest = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 2, 1, 4), Bits().subtype(namedValues=namedval.NamedValues(("existence", 0), ("boolean", 1), ("threshold", 2), )).clone(("boolean",))).setMaxAccess("readcreate")
mteTriggerSampleType = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 2, 1, 5), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,2,)).subtype(namedValues=namedval.NamedValues(("absoluteValue", 1), ("deltaValue", 2), )).clone(1)).setMaxAccess("readcreate")
mteTriggerValueID = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 2, 1, 6), ObjectIdentifier().clone((0, 0))).setMaxAccess("readcreate")
mteTriggerValueIDWildcard = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 2, 1, 7), TruthValue().clone('false')).setMaxAccess("readcreate")
mteTriggerTargetTag = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 2, 1, 8), SnmpTagValue().clone('')).setMaxAccess("readcreate")
mteTriggerContextName = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 2, 1, 9), SnmpAdminString().clone('')).setMaxAccess("readcreate")
mteTriggerContextNameWildcard = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 2, 1, 10), TruthValue().clone('false')).setMaxAccess("readcreate")
mteTriggerFrequency = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 2, 1, 11), Unsigned32().clone(600)).setMaxAccess("readcreate")
mteTriggerObjectsOwner = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 2, 1, 12), SnmpAdminString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 32)).clone('')).setMaxAccess("readcreate")
mteTriggerObjects = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 2, 1, 13), SnmpAdminString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 32)).clone('')).setMaxAccess("readcreate")
mteTriggerEnabled = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 2, 1, 14), TruthValue().clone('false')).setMaxAccess("readcreate")
mteTriggerEntryStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 2, 1, 15), RowStatus()).setMaxAccess("readcreate")
mteTriggerDeltaTable = MibTable((1, 3, 6, 1, 2, 1, 88, 1, 2, 3))
mteTriggerDeltaEntry = MibTableRow((1, 3, 6, 1, 2, 1, 88, 1, 2, 3, 1)).setIndexNames((0, "DISMAN-EVENT-MIB", "mteOwner"), (1, "DISMAN-EVENT-MIB", "mteTriggerName"))
mteTriggerDeltaDiscontinuityID = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 3, 1, 1), ObjectIdentifier().clone((1, 3, 6, 1, 2, 1, 1, 3, 0))).setMaxAccess("readwrite")
mteTriggerDeltaDiscontinuityIDWildcard = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 3, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
mteTriggerDeltaDiscontinuityIDType = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 3, 1, 3), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,3,)).subtype(namedValues=namedval.NamedValues(("timeTicks", 1), ("timeStamp", 2), ("dateAndTime", 3), )).clone(1)).setMaxAccess("readwrite")
mteTriggerExistenceTable = MibTable((1, 3, 6, 1, 2, 1, 88, 1, 2, 4))
mteTriggerExistenceEntry = MibTableRow((1, 3, 6, 1, 2, 1, 88, 1, 2, 4, 1)).setIndexNames((0, "DISMAN-EVENT-MIB", "mteOwner"), (1, "DISMAN-EVENT-MIB", "mteTriggerName"))
mteTriggerExistenceTest = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 4, 1, 1), Bits().subtype(namedValues=namedval.NamedValues(("present", 0), ("absent", 1), ("changed", 2), )).clone(("present","absent",))).setMaxAccess("readwrite")
mteTriggerExistenceStartup = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 4, 1, 2), Bits().subtype(namedValues=namedval.NamedValues(("present", 0), ("absent", 1), )).clone(("present","absent",))).setMaxAccess("readwrite")
mteTriggerExistenceObjectsOwner = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 4, 1, 3), SnmpAdminString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 32)).clone('')).setMaxAccess("readwrite")
mteTriggerExistenceObjects = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 4, 1, 4), SnmpAdminString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 32)).clone('')).setMaxAccess("readwrite")
mteTriggerExistenceEventOwner = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 4, 1, 5), SnmpAdminString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 32)).clone('')).setMaxAccess("readwrite")
mteTriggerExistenceEvent = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 4, 1, 6), SnmpAdminString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 32)).clone('')).setMaxAccess("readwrite")
mteTriggerBooleanTable = MibTable((1, 3, 6, 1, 2, 1, 88, 1, 2, 5))
mteTriggerBooleanEntry = MibTableRow((1, 3, 6, 1, 2, 1, 88, 1, 2, 5, 1)).setIndexNames((0, "DISMAN-EVENT-MIB", "mteOwner"), (1, "DISMAN-EVENT-MIB", "mteTriggerName"))
mteTriggerBooleanComparison = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 5, 1, 1), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(4,1,5,3,2,6,)).subtype(namedValues=namedval.NamedValues(("unequal", 1), ("equal", 2), ("less", 3), ("lessOrEqual", 4), ("greater", 5), ("greaterOrEqual", 6), )).clone(1)).setMaxAccess("readwrite")
mteTriggerBooleanValue = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 5, 1, 2), Integer32().clone(0)).setMaxAccess("readwrite")
mteTriggerBooleanStartup = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 5, 1, 3), TruthValue().clone('true')).setMaxAccess("readwrite")
mteTriggerBooleanObjectsOwner = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 5, 1, 4), SnmpAdminString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 32)).clone('')).setMaxAccess("readwrite")
mteTriggerBooleanObjects = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 5, 1, 5), SnmpAdminString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 32)).clone('')).setMaxAccess("readwrite")
mteTriggerBooleanEventOwner = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 5, 1, 6), SnmpAdminString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 32)).clone('')).setMaxAccess("readwrite")
mteTriggerBooleanEvent = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 5, 1, 7), SnmpAdminString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 32)).clone('')).setMaxAccess("readwrite")
mteTriggerThresholdTable = MibTable((1, 3, 6, 1, 2, 1, 88, 1, 2, 6))
mteTriggerThresholdEntry = MibTableRow((1, 3, 6, 1, 2, 1, 88, 1, 2, 6, 1)).setIndexNames((0, "DISMAN-EVENT-MIB", "mteOwner"), (1, "DISMAN-EVENT-MIB", "mteTriggerName"))
mteTriggerThresholdStartup = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 6, 1, 1), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,3,)).subtype(namedValues=namedval.NamedValues(("rising", 1), ("falling", 2), ("risingOrFalling", 3), )).clone(3)).setMaxAccess("readwrite")
mteTriggerThresholdRising = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 6, 1, 2), Integer32().clone(0)).setMaxAccess("readwrite")
mteTriggerThresholdFalling = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 6, 1, 3), Integer32().clone(0)).setMaxAccess("readwrite")
mteTriggerThresholdDeltaRising = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 6, 1, 4), Integer32().clone(0)).setMaxAccess("readwrite")
mteTriggerThresholdDeltaFalling = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 6, 1, 5), Integer32().clone(0)).setMaxAccess("readwrite")
mteTriggerThresholdObjectsOwner = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 6, 1, 6), SnmpAdminString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 32)).clone('')).setMaxAccess("readwrite")
mteTriggerThresholdObjects = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 6, 1, 7), SnmpAdminString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 32)).clone('')).setMaxAccess("readwrite")
mteTriggerThresholdRisingEventOwner = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 6, 1, 8), SnmpAdminString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 32)).clone('')).setMaxAccess("readwrite")
mteTriggerThresholdRisingEvent = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 6, 1, 9), SnmpAdminString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 32)).clone('')).setMaxAccess("readwrite")
mteTriggerThresholdFallingEventOwner = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 6, 1, 10), SnmpAdminString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 32)).clone('')).setMaxAccess("readwrite")
mteTriggerThresholdFallingEvent = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 6, 1, 11), SnmpAdminString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 32)).clone('')).setMaxAccess("readwrite")
mteTriggerThresholdDeltaRisingEventOwner = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 6, 1, 12), SnmpAdminString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 32)).clone('')).setMaxAccess("readwrite")
mteTriggerThresholdDeltaRisingEvent = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 6, 1, 13), SnmpAdminString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 32)).clone('')).setMaxAccess("readwrite")
mteTriggerThresholdDeltaFallingEventOwner = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 6, 1, 14), SnmpAdminString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 32)).clone('')).setMaxAccess("readwrite")
mteTriggerThresholdDeltaFallingEvent = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 6, 1, 15), SnmpAdminString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 32)).clone('')).setMaxAccess("readwrite")
mteObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 88, 1, 3))
mteObjectsTable = MibTable((1, 3, 6, 1, 2, 1, 88, 1, 3, 1))
mteObjectsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 88, 1, 3, 1, 1)).setIndexNames((0, "DISMAN-EVENT-MIB", "mteOwner"), (0, "DISMAN-EVENT-MIB", "mteObjectsName"), (0, "DISMAN-EVENT-MIB", "mteObjectsIndex"))
mteObjectsName = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 3, 1, 1, 1), SnmpAdminString().subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 32))).setMaxAccess("noaccess")
mteObjectsIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 3, 1, 1, 2), Unsigned32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 4294967295L))).setMaxAccess("noaccess")
mteObjectsID = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 3, 1, 1, 3), ObjectIdentifier().clone((0, 0))).setMaxAccess("readcreate")
mteObjectsIDWildcard = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 3, 1, 1, 4), TruthValue().clone('false')).setMaxAccess("readcreate")
mteObjectsEntryStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 3, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
mteEvent = MibIdentifier((1, 3, 6, 1, 2, 1, 88, 1, 4))
mteEventFailures = MibScalar((1, 3, 6, 1, 2, 1, 88, 1, 4, 1), Counter32()).setMaxAccess("readonly")
mteEventTable = MibTable((1, 3, 6, 1, 2, 1, 88, 1, 4, 2))
mteEventEntry = MibTableRow((1, 3, 6, 1, 2, 1, 88, 1, 4, 2, 1)).setIndexNames((0, "DISMAN-EVENT-MIB", "mteOwner"), (1, "DISMAN-EVENT-MIB", "mteEventName"))
mteEventName = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 4, 2, 1, 1), SnmpAdminString().subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 32))).setMaxAccess("noaccess")
mteEventComment = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 4, 2, 1, 2), SnmpAdminString().clone('')).setMaxAccess("readcreate")
mteEventActions = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 4, 2, 1, 3), Bits().subtype(namedValues=namedval.NamedValues(("notification", 0), ("set", 1), )).clone(())).setMaxAccess("readcreate")
mteEventEnabled = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 4, 2, 1, 4), TruthValue().clone('false')).setMaxAccess("readcreate")
mteEventEntryStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 4, 2, 1, 5), RowStatus()).setMaxAccess("readcreate")
mteEventNotificationTable = MibTable((1, 3, 6, 1, 2, 1, 88, 1, 4, 3))
mteEventNotificationEntry = MibTableRow((1, 3, 6, 1, 2, 1, 88, 1, 4, 3, 1)).setIndexNames((0, "DISMAN-EVENT-MIB", "mteOwner"), (1, "DISMAN-EVENT-MIB", "mteEventName"))
mteEventNotification = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 4, 3, 1, 1), ObjectIdentifier().clone((0, 0))).setMaxAccess("readwrite")
mteEventNotificationObjectsOwner = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 4, 3, 1, 2), SnmpAdminString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 32)).clone('')).setMaxAccess("readwrite")
mteEventNotificationObjects = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 4, 3, 1, 3), SnmpAdminString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 32)).clone('')).setMaxAccess("readwrite")
mteEventSetTable = MibTable((1, 3, 6, 1, 2, 1, 88, 1, 4, 4))
mteEventSetEntry = MibTableRow((1, 3, 6, 1, 2, 1, 88, 1, 4, 4, 1)).setIndexNames((0, "DISMAN-EVENT-MIB", "mteOwner"), (1, "DISMAN-EVENT-MIB", "mteEventName"))
mteEventSetObject = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 4, 4, 1, 1), ObjectIdentifier().clone((0, 0))).setMaxAccess("readwrite")
mteEventSetObjectWildcard = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 4, 4, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
mteEventSetValue = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 4, 4, 1, 3), Integer32().clone(0)).setMaxAccess("readwrite")
mteEventSetTargetTag = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 4, 4, 1, 4), SnmpTagValue().clone('')).setMaxAccess("readwrite")
mteEventSetContextName = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 4, 4, 1, 5), SnmpAdminString().clone('')).setMaxAccess("readwrite")
mteEventSetContextNameWildcard = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 4, 4, 1, 6), TruthValue().clone('false')).setMaxAccess("readwrite")
dismanEventMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 2, 1, 88, 2))
dismanEventMIBNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 88, 2, 0))
dismanEventMIBNotificationObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 88, 2, 1))
mteHotTrigger = MibScalar((1, 3, 6, 1, 2, 1, 88, 2, 1, 1), SnmpAdminString()).setMaxAccess("notifyonly")
mteHotTargetName = MibScalar((1, 3, 6, 1, 2, 1, 88, 2, 1, 2), SnmpAdminString()).setMaxAccess("notifyonly")
mteHotContextName = MibScalar((1, 3, 6, 1, 2, 1, 88, 2, 1, 3), SnmpAdminString()).setMaxAccess("notifyonly")
mteHotOID = MibScalar((1, 3, 6, 1, 2, 1, 88, 2, 1, 4), ObjectIdentifier()).setMaxAccess("notifyonly")
mteHotValue = MibScalar((1, 3, 6, 1, 2, 1, 88, 2, 1, 5), Integer32()).setMaxAccess("notifyonly")
mteFailedReason = MibScalar((1, 3, 6, 1, 2, 1, 88, 2, 1, 6), FailureReason()).setMaxAccess("notifyonly")
dismanEventMIBConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 88, 3))
dismanEventMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 88, 3, 1))
dismanEventMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 88, 3, 2))

# Augmentions

# Notifications

mteEventSetFailure = NotificationType((1, 3, 6, 1, 2, 1, 88, 2, 0, 5)).setObjects(("DISMAN-EVENT-MIB", "mteFailedReason"), ("DISMAN-EVENT-MIB", "mteHotTargetName"), ("DISMAN-EVENT-MIB", "mteHotContextName"), ("DISMAN-EVENT-MIB", "mteHotTrigger"), ("DISMAN-EVENT-MIB", "mteHotOID"), )
mteTriggerRising = NotificationType((1, 3, 6, 1, 2, 1, 88, 2, 0, 2)).setObjects(("DISMAN-EVENT-MIB", "mteHotTargetName"), ("DISMAN-EVENT-MIB", "mteHotValue"), ("DISMAN-EVENT-MIB", "mteHotContextName"), ("DISMAN-EVENT-MIB", "mteHotTrigger"), ("DISMAN-EVENT-MIB", "mteHotOID"), )
mteTriggerFailure = NotificationType((1, 3, 6, 1, 2, 1, 88, 2, 0, 4)).setObjects(("DISMAN-EVENT-MIB", "mteFailedReason"), ("DISMAN-EVENT-MIB", "mteHotTargetName"), ("DISMAN-EVENT-MIB", "mteHotContextName"), ("DISMAN-EVENT-MIB", "mteHotTrigger"), ("DISMAN-EVENT-MIB", "mteHotOID"), )
mteTriggerFalling = NotificationType((1, 3, 6, 1, 2, 1, 88, 2, 0, 3)).setObjects(("DISMAN-EVENT-MIB", "mteHotTargetName"), ("DISMAN-EVENT-MIB", "mteHotValue"), ("DISMAN-EVENT-MIB", "mteHotContextName"), ("DISMAN-EVENT-MIB", "mteHotTrigger"), ("DISMAN-EVENT-MIB", "mteHotOID"), )
mteTriggerFired = NotificationType((1, 3, 6, 1, 2, 1, 88, 2, 0, 1)).setObjects(("DISMAN-EVENT-MIB", "mteHotTargetName"), ("DISMAN-EVENT-MIB", "mteHotValue"), ("DISMAN-EVENT-MIB", "mteHotContextName"), ("DISMAN-EVENT-MIB", "mteHotTrigger"), ("DISMAN-EVENT-MIB", "mteHotOID"), )

# Groups

dismanEventNotificationGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 88, 3, 2, 6)).setObjects(("DISMAN-EVENT-MIB", "mteEventSetFailure"), ("DISMAN-EVENT-MIB", "mteTriggerRising"), ("DISMAN-EVENT-MIB", "mteTriggerFailure"), ("DISMAN-EVENT-MIB", "mteTriggerFalling"), ("DISMAN-EVENT-MIB", "mteTriggerFired"), )
dismanEventObjectsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 88, 3, 2, 3)).setObjects(("DISMAN-EVENT-MIB", "mteObjectsIDWildcard"), ("DISMAN-EVENT-MIB", "mteObjectsID"), ("DISMAN-EVENT-MIB", "mteObjectsEntryStatus"), )
dismanEventResourceGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 88, 3, 2, 1)).setObjects(("DISMAN-EVENT-MIB", "mteResourceSampleInstancesHigh"), ("DISMAN-EVENT-MIB", "mteResourceSampleInstanceLacks"), ("DISMAN-EVENT-MIB", "mteResourceSampleMinimum"), ("DISMAN-EVENT-MIB", "mteResourceSampleInstanceMaximum"), ("DISMAN-EVENT-MIB", "mteResourceSampleInstances"), )
dismanEventEventGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 88, 3, 2, 4)).setObjects(("DISMAN-EVENT-MIB", "mteEventNotificationObjects"), ("DISMAN-EVENT-MIB", "mteEventSetObject"), ("DISMAN-EVENT-MIB", "mteEventActions"), ("DISMAN-EVENT-MIB", "mteEventSetContextNameWildcard"), ("DISMAN-EVENT-MIB", "mteEventNotificationObjectsOwner"), ("DISMAN-EVENT-MIB", "mteEventSetContextName"), ("DISMAN-EVENT-MIB", "mteEventSetObjectWildcard"), ("DISMAN-EVENT-MIB", "mteEventSetValue"), ("DISMAN-EVENT-MIB", "mteEventEnabled"), ("DISMAN-EVENT-MIB", "mteEventSetTargetTag"), ("DISMAN-EVENT-MIB", "mteEventFailures"), ("DISMAN-EVENT-MIB", "mteEventComment"), ("DISMAN-EVENT-MIB", "mteEventEntryStatus"), ("DISMAN-EVENT-MIB", "mteEventNotification"), )
dismanEventTriggerGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 88, 3, 2, 2)).setObjects(("DISMAN-EVENT-MIB", "mteTriggerValueID"), ("DISMAN-EVENT-MIB", "mteTriggerBooleanObjects"), ("DISMAN-EVENT-MIB", "mteTriggerThresholdObjects"), ("DISMAN-EVENT-MIB", "mteTriggerTargetTag"), ("DISMAN-EVENT-MIB", "mteTriggerThresholdFallingEventOwner"), ("DISMAN-EVENT-MIB", "mteTriggerBooleanValue"), ("DISMAN-EVENT-MIB", "mteTriggerContextNameWildcard"), ("DISMAN-EVENT-MIB", "mteTriggerDeltaDiscontinuityIDType"), ("DISMAN-EVENT-MIB", "mteTriggerContextName"), ("DISMAN-EVENT-MIB", "mteTriggerExistenceObjects"), ("DISMAN-EVENT-MIB", "mteTriggerObjectsOwner"), ("DISMAN-EVENT-MIB", "mteTriggerExistenceEvent"), ("DISMAN-EVENT-MIB", "mteTriggerFailures"), ("DISMAN-EVENT-MIB", "mteTriggerThresholdDeltaRising"), ("DISMAN-EVENT-MIB", "mteTriggerThresholdDeltaFalling"), ("DISMAN-EVENT-MIB", "mteTriggerThresholdRisingEventOwner"), ("DISMAN-EVENT-MIB", "mteTriggerEnabled"), ("DISMAN-EVENT-MIB", "mteTriggerDeltaDiscontinuityIDWildcard"), ("DISMAN-EVENT-MIB", "mteTriggerThresholdStartup"), ("DISMAN-EVENT-MIB", "mteTriggerThresholdDeltaFallingEvent"), ("DISMAN-EVENT-MIB", "mteTriggerThresholdRisingEvent"), ("DISMAN-EVENT-MIB", "mteTriggerThresholdFalling"), ("DISMAN-EVENT-MIB", "mteTriggerThresholdFallingEvent"), ("DISMAN-EVENT-MIB", "mteTriggerExistenceTest"), ("DISMAN-EVENT-MIB", "mteTriggerSampleType"), ("DISMAN-EVENT-MIB", "mteTriggerValueIDWildcard"), ("DISMAN-EVENT-MIB", "mteTriggerThresholdDeltaRisingEvent"), ("DISMAN-EVENT-MIB", "mteTriggerComment"), ("DISMAN-EVENT-MIB", "mteTriggerExistenceEventOwner"), ("DISMAN-EVENT-MIB", "mteTriggerBooleanEventOwner"), ("DISMAN-EVENT-MIB", "mteTriggerThresholdDeltaFallingEventOwner"), ("DISMAN-EVENT-MIB", "mteTriggerDeltaDiscontinuityID"), ("DISMAN-EVENT-MIB", "mteTriggerObjects"), ("DISMAN-EVENT-MIB", "mteTriggerExistenceObjectsOwner"), ("DISMAN-EVENT-MIB", "mteTriggerBooleanStartup"), ("DISMAN-EVENT-MIB", "mteTriggerFrequency"), ("DISMAN-EVENT-MIB", "mteTriggerBooleanEvent"), ("DISMAN-EVENT-MIB", "mteTriggerExistenceStartup"), ("DISMAN-EVENT-MIB", "mteTriggerTest"), ("DISMAN-EVENT-MIB", "mteTriggerEntryStatus"), ("DISMAN-EVENT-MIB", "mteTriggerBooleanComparison"), ("DISMAN-EVENT-MIB", "mteTriggerThresholdObjectsOwner"), ("DISMAN-EVENT-MIB", "mteTriggerBooleanObjectsOwner"), ("DISMAN-EVENT-MIB", "mteTriggerThresholdDeltaRisingEventOwner"), ("DISMAN-EVENT-MIB", "mteTriggerThresholdRising"), )
dismanEventNotificationObjectGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 88, 3, 2, 5)).setObjects(("DISMAN-EVENT-MIB", "mteHotTargetName"), ("DISMAN-EVENT-MIB", "mteHotTrigger"), ("DISMAN-EVENT-MIB", "mteHotContextName"), ("DISMAN-EVENT-MIB", "mteHotValue"), ("DISMAN-EVENT-MIB", "mteHotOID"), ("DISMAN-EVENT-MIB", "mteFailedReason"), )

# Exports

# Module identity
mibBuilder.exportSymbols("DISMAN-EVENT-MIB", PYSNMP_MODULE_ID=dismanEventMIB)

# Types
mibBuilder.exportSymbols("DISMAN-EVENT-MIB", FailureReason=FailureReason)

# Objects
mibBuilder.exportSymbols("DISMAN-EVENT-MIB", sysUpTimeInstance=sysUpTimeInstance, dismanEventMIB=dismanEventMIB, dismanEventMIBObjects=dismanEventMIBObjects, mteResource=mteResource, mteResourceSampleMinimum=mteResourceSampleMinimum, mteResourceSampleInstanceMaximum=mteResourceSampleInstanceMaximum, mteResourceSampleInstances=mteResourceSampleInstances, mteResourceSampleInstancesHigh=mteResourceSampleInstancesHigh, mteResourceSampleInstanceLacks=mteResourceSampleInstanceLacks, mteTrigger=mteTrigger, mteTriggerFailures=mteTriggerFailures, mteTriggerTable=mteTriggerTable, mteTriggerEntry=mteTriggerEntry, mteOwner=mteOwner, mteTriggerName=mteTriggerName, mteTriggerComment=mteTriggerComment, mteTriggerTest=mteTriggerTest, mteTriggerSampleType=mteTriggerSampleType, mteTriggerValueID=mteTriggerValueID, mteTriggerValueIDWildcard=mteTriggerValueIDWildcard, mteTriggerTargetTag=mteTriggerTargetTag, mteTriggerContextName=mteTriggerContextName, mteTriggerContextNameWildcard=mteTriggerContextNameWildcard, mteTriggerFrequency=mteTriggerFrequency, mteTriggerObjectsOwner=mteTriggerObjectsOwner, mteTriggerObjects=mteTriggerObjects, mteTriggerEnabled=mteTriggerEnabled, mteTriggerEntryStatus=mteTriggerEntryStatus, mteTriggerDeltaTable=mteTriggerDeltaTable, mteTriggerDeltaEntry=mteTriggerDeltaEntry, mteTriggerDeltaDiscontinuityID=mteTriggerDeltaDiscontinuityID, mteTriggerDeltaDiscontinuityIDWildcard=mteTriggerDeltaDiscontinuityIDWildcard, mteTriggerDeltaDiscontinuityIDType=mteTriggerDeltaDiscontinuityIDType, mteTriggerExistenceTable=mteTriggerExistenceTable, mteTriggerExistenceEntry=mteTriggerExistenceEntry, mteTriggerExistenceTest=mteTriggerExistenceTest, mteTriggerExistenceStartup=mteTriggerExistenceStartup, mteTriggerExistenceObjectsOwner=mteTriggerExistenceObjectsOwner, mteTriggerExistenceObjects=mteTriggerExistenceObjects, mteTriggerExistenceEventOwner=mteTriggerExistenceEventOwner, mteTriggerExistenceEvent=mteTriggerExistenceEvent, mteTriggerBooleanTable=mteTriggerBooleanTable, mteTriggerBooleanEntry=mteTriggerBooleanEntry, mteTriggerBooleanComparison=mteTriggerBooleanComparison, mteTriggerBooleanValue=mteTriggerBooleanValue, mteTriggerBooleanStartup=mteTriggerBooleanStartup, mteTriggerBooleanObjectsOwner=mteTriggerBooleanObjectsOwner, mteTriggerBooleanObjects=mteTriggerBooleanObjects, mteTriggerBooleanEventOwner=mteTriggerBooleanEventOwner, mteTriggerBooleanEvent=mteTriggerBooleanEvent, mteTriggerThresholdTable=mteTriggerThresholdTable, mteTriggerThresholdEntry=mteTriggerThresholdEntry, mteTriggerThresholdStartup=mteTriggerThresholdStartup, mteTriggerThresholdRising=mteTriggerThresholdRising, mteTriggerThresholdFalling=mteTriggerThresholdFalling, mteTriggerThresholdDeltaRising=mteTriggerThresholdDeltaRising, mteTriggerThresholdDeltaFalling=mteTriggerThresholdDeltaFalling, mteTriggerThresholdObjectsOwner=mteTriggerThresholdObjectsOwner, mteTriggerThresholdObjects=mteTriggerThresholdObjects, mteTriggerThresholdRisingEventOwner=mteTriggerThresholdRisingEventOwner, mteTriggerThresholdRisingEvent=mteTriggerThresholdRisingEvent, mteTriggerThresholdFallingEventOwner=mteTriggerThresholdFallingEventOwner, mteTriggerThresholdFallingEvent=mteTriggerThresholdFallingEvent, mteTriggerThresholdDeltaRisingEventOwner=mteTriggerThresholdDeltaRisingEventOwner, mteTriggerThresholdDeltaRisingEvent=mteTriggerThresholdDeltaRisingEvent, mteTriggerThresholdDeltaFallingEventOwner=mteTriggerThresholdDeltaFallingEventOwner, mteTriggerThresholdDeltaFallingEvent=mteTriggerThresholdDeltaFallingEvent, mteObjects=mteObjects, mteObjectsTable=mteObjectsTable, mteObjectsEntry=mteObjectsEntry, mteObjectsName=mteObjectsName, mteObjectsIndex=mteObjectsIndex, mteObjectsID=mteObjectsID, mteObjectsIDWildcard=mteObjectsIDWildcard, mteObjectsEntryStatus=mteObjectsEntryStatus, mteEvent=mteEvent, mteEventFailures=mteEventFailures, mteEventTable=mteEventTable, mteEventEntry=mteEventEntry, mteEventName=mteEventName, mteEventComment=mteEventComment, mteEventActions=mteEventActions, mteEventEnabled=mteEventEnabled, mteEventEntryStatus=mteEventEntryStatus, mteEventNotificationTable=mteEventNotificationTable, mteEventNotificationEntry=mteEventNotificationEntry, mteEventNotification=mteEventNotification, mteEventNotificationObjectsOwner=mteEventNotificationObjectsOwner, mteEventNotificationObjects=mteEventNotificationObjects, mteEventSetTable=mteEventSetTable, mteEventSetEntry=mteEventSetEntry, mteEventSetObject=mteEventSetObject, mteEventSetObjectWildcard=mteEventSetObjectWildcard, mteEventSetValue=mteEventSetValue, mteEventSetTargetTag=mteEventSetTargetTag, mteEventSetContextName=mteEventSetContextName, mteEventSetContextNameWildcard=mteEventSetContextNameWildcard, dismanEventMIBNotificationPrefix=dismanEventMIBNotificationPrefix, dismanEventMIBNotifications=dismanEventMIBNotifications, dismanEventMIBNotificationObjects=dismanEventMIBNotificationObjects, mteHotTrigger=mteHotTrigger, mteHotTargetName=mteHotTargetName, mteHotContextName=mteHotContextName, mteHotOID=mteHotOID, mteHotValue=mteHotValue, mteFailedReason=mteFailedReason, dismanEventMIBConformance=dismanEventMIBConformance, dismanEventMIBCompliances=dismanEventMIBCompliances, dismanEventMIBGroups=dismanEventMIBGroups)

# Notifications
mibBuilder.exportSymbols("DISMAN-EVENT-MIB", mteEventSetFailure=mteEventSetFailure, mteTriggerRising=mteTriggerRising, mteTriggerFailure=mteTriggerFailure, mteTriggerFalling=mteTriggerFalling, mteTriggerFired=mteTriggerFired)

# Groups
mibBuilder.exportSymbols("DISMAN-EVENT-MIB", dismanEventNotificationGroup=dismanEventNotificationGroup, dismanEventObjectsGroup=dismanEventObjectsGroup, dismanEventResourceGroup=dismanEventResourceGroup, dismanEventEventGroup=dismanEventEventGroup, dismanEventTriggerGroup=dismanEventTriggerGroup, dismanEventNotificationObjectGroup=dismanEventNotificationObjectGroup)
