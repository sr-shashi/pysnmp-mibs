# PySNMP SMI module. Autogenerated from smidump -f python HC-ALARM-MIB
# by libsmi2pysnmp-0.0.7-alpha at Wed Feb  7 16:12:55 2007,
# Python version (2, 4, 3, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( CounterBasedGauge64, ) = mibBuilder.importSymbols("HCNUM-TC", "CounterBasedGauge64")
( OwnerString, rmon, rmonEventGroup, ) = mibBuilder.importSymbols("RMON-MIB", "OwnerString", "rmon", "rmonEventGroup")
( ModuleCompliance, NotificationGroup, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
( Bits, Counter32, Integer32, Integer32, ModuleIdentity, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32")
( RowStatus, StorageType, TextualConvention, VariablePointer, ) = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "StorageType", "TextualConvention", "VariablePointer")

# Types

class HcValueStatus(Integer):
    subtypeSpec = Integer.subtypeSpec+constraint.SingleValueConstraint(1,2,3,)
    namedValues = namedval.NamedValues(("valueNotAvailable", 1), ("valuePositive", 2), ("valueNegative", 3), )
    pass


# Objects

hcAlarmMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 16, 29)).setRevisions(("2002-12-16 00:00",))
hcAlarmObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 29, 1))
hcAlarmControlObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 29, 1, 1))
hcAlarmTable = MibTable((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1))
hcAlarmEntry = MibTableRow((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1)).setIndexNames((0, "HC-ALARM-MIB", "hcAlarmIndex"))
hcAlarmIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 65535))).setMaxAccess("noaccess")
hcAlarmInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 2147483647L))).setMaxAccess("readcreate")
hcAlarmVariable = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 3), VariablePointer()).setMaxAccess("readcreate")
hcAlarmSampleType = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 4), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,2,)).subtype(namedValues=namedval.NamedValues(("absoluteValue", 1), ("deltaValue", 2), ))).setMaxAccess("readcreate")
hcAlarmAbsValue = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 5), CounterBasedGauge64()).setMaxAccess("readonly")
hcAlarmValueStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 6), HcValueStatus()).setMaxAccess("readonly")
hcAlarmStartupAlarm = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 7), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,3,)).subtype(namedValues=namedval.NamedValues(("risingAlarm", 1), ("fallingAlarm", 2), ("risingOrFallingAlarm", 3), ))).setMaxAccess("readcreate")
hcAlarmRisingThreshAbsValueLo = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 8), Unsigned32()).setMaxAccess("readcreate")
hcAlarmRisingThreshAbsValueHi = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 9), Unsigned32()).setMaxAccess("readcreate")
hcAlarmRisingThresholdValStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 10), HcValueStatus()).setMaxAccess("readcreate")
hcAlarmFallingThreshAbsValueLo = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 11), Unsigned32()).setMaxAccess("readcreate")
hcAlarmFallingThreshAbsValueHi = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 12), Unsigned32()).setMaxAccess("readcreate")
hcAlarmFallingThresholdValStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 13), HcValueStatus()).setMaxAccess("readcreate")
hcAlarmRisingEventIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 14), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
hcAlarmFallingEventIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 15), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
hcAlarmValueFailedAttempts = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 16), Counter32()).setMaxAccess("readonly")
hcAlarmOwner = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 17), OwnerString()).setMaxAccess("readcreate")
hcAlarmStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 18), StorageType()).setMaxAccess("readcreate")
hcAlarmStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 19), RowStatus()).setMaxAccess("readcreate")
hcAlarmCapabilitiesObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 29, 1, 2))
hcAlarmCapabilities = MibScalar((1, 3, 6, 1, 2, 1, 16, 29, 1, 2, 1), Bits().subtype(namedValues=namedval.NamedValues(("hcAlarmCreation", 0), ("hcAlarmNvStorage", 1), ))).setMaxAccess("readonly")
hcAlarmNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 29, 2))
hcAlarmNotifPrefix = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 29, 2, 0))
hcAlarmConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 29, 3))
hcAlarmCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 29, 3, 1))
hcAlarmGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 29, 3, 2))

# Augmentions

# Notifications

hcRisingAlarm = NotificationType((1, 3, 6, 1, 2, 1, 16, 29, 2, 0, 1)).setObjects(("HC-ALARM-MIB", "hcAlarmRisingThreshAbsValueLo"), ("HC-ALARM-MIB", "hcAlarmValueStatus"), ("HC-ALARM-MIB", "hcAlarmRisingThreshAbsValueHi"), ("HC-ALARM-MIB", "hcAlarmRisingEventIndex"), ("HC-ALARM-MIB", "hcAlarmAbsValue"), ("HC-ALARM-MIB", "hcAlarmVariable"), ("HC-ALARM-MIB", "hcAlarmRisingThresholdValStatus"), ("HC-ALARM-MIB", "hcAlarmSampleType"), )
hcFallingAlarm = NotificationType((1, 3, 6, 1, 2, 1, 16, 29, 2, 0, 2)).setObjects(("HC-ALARM-MIB", "hcAlarmFallingThresholdValStatus"), ("HC-ALARM-MIB", "hcAlarmFallingThreshAbsValueHi"), ("HC-ALARM-MIB", "hcAlarmValueStatus"), ("HC-ALARM-MIB", "hcAlarmFallingEventIndex"), ("HC-ALARM-MIB", "hcAlarmAbsValue"), ("HC-ALARM-MIB", "hcAlarmVariable"), ("HC-ALARM-MIB", "hcAlarmFallingThreshAbsValueLo"), ("HC-ALARM-MIB", "hcAlarmSampleType"), )

# Groups

hcAlarmCapabilitiesGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 16, 29, 3, 2, 2)).setObjects(("HC-ALARM-MIB", "hcAlarmCapabilities"), )
hcAlarmControlGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 16, 29, 3, 2, 1)).setObjects(("HC-ALARM-MIB", "hcAlarmRisingEventIndex"), ("HC-ALARM-MIB", "hcAlarmRisingThreshAbsValueLo"), ("HC-ALARM-MIB", "hcAlarmFallingThreshAbsValueHi"), ("HC-ALARM-MIB", "hcAlarmOwner"), ("HC-ALARM-MIB", "hcAlarmValueStatus"), ("HC-ALARM-MIB", "hcAlarmRisingThreshAbsValueHi"), ("HC-ALARM-MIB", "hcAlarmStorageType"), ("HC-ALARM-MIB", "hcAlarmFallingThreshAbsValueLo"), ("HC-ALARM-MIB", "hcAlarmAbsValue"), ("HC-ALARM-MIB", "hcAlarmFallingThresholdValStatus"), ("HC-ALARM-MIB", "hcAlarmVariable"), ("HC-ALARM-MIB", "hcAlarmStartupAlarm"), ("HC-ALARM-MIB", "hcAlarmValueFailedAttempts"), ("HC-ALARM-MIB", "hcAlarmInterval"), ("HC-ALARM-MIB", "hcAlarmRisingThresholdValStatus"), ("HC-ALARM-MIB", "hcAlarmSampleType"), ("HC-ALARM-MIB", "hcAlarmStatus"), ("HC-ALARM-MIB", "hcAlarmFallingEventIndex"), )
hcAlarmNotificationsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 16, 29, 3, 2, 3)).setObjects(("HC-ALARM-MIB", "hcRisingAlarm"), ("HC-ALARM-MIB", "hcFallingAlarm"), )

# Exports

# Module identity
mibBuilder.exportSymbols("HC-ALARM-MIB", PYSNMP_MODULE_ID=hcAlarmMIB)

# Types
mibBuilder.exportSymbols("HC-ALARM-MIB", HcValueStatus=HcValueStatus)

# Objects
mibBuilder.exportSymbols("HC-ALARM-MIB", hcAlarmMIB=hcAlarmMIB, hcAlarmObjects=hcAlarmObjects, hcAlarmControlObjects=hcAlarmControlObjects, hcAlarmTable=hcAlarmTable, hcAlarmEntry=hcAlarmEntry, hcAlarmIndex=hcAlarmIndex, hcAlarmInterval=hcAlarmInterval, hcAlarmVariable=hcAlarmVariable, hcAlarmSampleType=hcAlarmSampleType, hcAlarmAbsValue=hcAlarmAbsValue, hcAlarmValueStatus=hcAlarmValueStatus, hcAlarmStartupAlarm=hcAlarmStartupAlarm, hcAlarmRisingThreshAbsValueLo=hcAlarmRisingThreshAbsValueLo, hcAlarmRisingThreshAbsValueHi=hcAlarmRisingThreshAbsValueHi, hcAlarmRisingThresholdValStatus=hcAlarmRisingThresholdValStatus, hcAlarmFallingThreshAbsValueLo=hcAlarmFallingThreshAbsValueLo, hcAlarmFallingThreshAbsValueHi=hcAlarmFallingThreshAbsValueHi, hcAlarmFallingThresholdValStatus=hcAlarmFallingThresholdValStatus, hcAlarmRisingEventIndex=hcAlarmRisingEventIndex, hcAlarmFallingEventIndex=hcAlarmFallingEventIndex, hcAlarmValueFailedAttempts=hcAlarmValueFailedAttempts, hcAlarmOwner=hcAlarmOwner, hcAlarmStorageType=hcAlarmStorageType, hcAlarmStatus=hcAlarmStatus, hcAlarmCapabilitiesObjects=hcAlarmCapabilitiesObjects, hcAlarmCapabilities=hcAlarmCapabilities, hcAlarmNotifications=hcAlarmNotifications, hcAlarmNotifPrefix=hcAlarmNotifPrefix, hcAlarmConformance=hcAlarmConformance, hcAlarmCompliances=hcAlarmCompliances, hcAlarmGroups=hcAlarmGroups)

# Notifications
mibBuilder.exportSymbols("HC-ALARM-MIB", hcRisingAlarm=hcRisingAlarm, hcFallingAlarm=hcFallingAlarm)

# Groups
mibBuilder.exportSymbols("HC-ALARM-MIB", hcAlarmCapabilitiesGroup=hcAlarmCapabilitiesGroup, hcAlarmControlGroup=hcAlarmControlGroup, hcAlarmNotificationsGroup=hcAlarmNotificationsGroup)
