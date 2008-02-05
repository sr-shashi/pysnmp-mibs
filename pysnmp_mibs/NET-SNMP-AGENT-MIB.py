# PySNMP SMI module. Autogenerated from smidump -f python NET-SNMP-AGENT-MIB
# by libsmi2pysnmp-0.0.8-alpha at Tue Feb  5 21:05:14 2008,
# Python version (2, 4, 4, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( netSnmpGroups, netSnmpModuleIDs, netSnmpNotifications, netSnmpObjects, ) = mibBuilder.importSymbols("NET-SNMP-MIB", "netSnmpGroups", "netSnmpModuleIDs", "netSnmpNotifications", "netSnmpObjects")
( SnmpAdminString, ) = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
( NotificationGroup, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup")
( Bits, Integer32, Integer32, ModuleIdentity, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32")
( DisplayString, RowStatus, TextualConvention, TruthValue, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention", "TruthValue")

# Types

class NetsnmpCacheStatus(Integer):
    subtypeSpec = Integer.subtypeSpec+constraint.SingleValueConstraint(4,1,2,5,3,)
    namedValues = namedval.NamedValues(("enabled", 1), ("disabled", 2), ("empty", 3), ("cached", 4), ("expired", 5), )
    pass


# Objects

nsVersion = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 1, 1))
nsMibRegistry = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 1, 2))
nsModuleTable = MibTable((1, 3, 6, 1, 4, 1, 8072, 1, 2, 1))
if mibBuilder.loadTexts: nsModuleTable.setDescription("A table displaying all the oid's registered by mib modules in\nthe agent.  Since the agent is modular in nature, this lists\neach module's OID it is responsible for and the name of the module")
nsModuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8072, 1, 2, 1, 1)).setIndexNames((0, "NET-SNMP-AGENT-MIB", "nsmContextName"), (0, "NET-SNMP-AGENT-MIB", "nsmRegistrationPoint"), (0, "NET-SNMP-AGENT-MIB", "nsmRegistrationPriority"))
if mibBuilder.loadTexts: nsModuleEntry.setDescription("An entry containing a registered mib oid.")
nsmContextName = MibTableColumn((1, 3, 6, 1, 4, 1, 8072, 1, 2, 1, 1, 1), SnmpAdminString()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: nsmContextName.setDescription("The context name the module is registered under.")
nsmRegistrationPoint = MibTableColumn((1, 3, 6, 1, 4, 1, 8072, 1, 2, 1, 1, 2), ObjectIdentifier()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: nsmRegistrationPoint.setDescription("The registry OID of a mib module.")
nsmRegistrationPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 8072, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(-2147483648L, 2147483647L))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: nsmRegistrationPriority.setDescription("The priority of the registered mib module.")
nsModuleName = MibTableColumn((1, 3, 6, 1, 4, 1, 8072, 1, 2, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsModuleName.setDescription("The module name that registered this OID.")
nsModuleModes = MibTableColumn((1, 3, 6, 1, 4, 1, 8072, 1, 2, 1, 1, 5), Bits().subtype(namedValues=namedval.NamedValues(("getAndGetNext", 0), ("set", 1), ("getBulk", 2), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsModuleModes.setDescription("The modes that the particular lower level handler can cope\nwith directly.")
nsModuleTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 8072, 1, 2, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsModuleTimeout.setDescription("The registered timeout.  This is only meaningful for handlers\nthat expect to return results at a later date (subagents,\netc)")
nsExtensions = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 1, 3))
nsDLMod = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 1, 4))
nsCache = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 1, 5))
nsCacheDefaultTimeout = MibScalar((1, 3, 6, 1, 4, 1, 8072, 1, 5, 1), Integer32().clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nsCacheDefaultTimeout.setDescription("Default cache timeout value (unless overridden\nfor a particular cache entry).")
nsCacheEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8072, 1, 5, 2), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nsCacheEnabled.setDescription("Whether data caching is active overall.")
nsCacheTable = MibTable((1, 3, 6, 1, 4, 1, 8072, 1, 5, 3))
if mibBuilder.loadTexts: nsCacheTable.setDescription("A table of individual MIB module data caches.")
nsCacheEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8072, 1, 5, 3, 1)).setIndexNames((1, "NET-SNMP-AGENT-MIB", "nsCachedOID"))
if mibBuilder.loadTexts: nsCacheEntry.setDescription("A conceptual row within the cache table.")
nsCachedOID = MibTableColumn((1, 3, 6, 1, 4, 1, 8072, 1, 5, 3, 1, 1), ObjectIdentifier()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: nsCachedOID.setDescription("The root OID of the data being cached.")
nsCacheTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 8072, 1, 5, 3, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nsCacheTimeout.setDescription("The length of time (?in seconds) for which the data in\nthis particular cache entry will remain valid.")
nsCacheStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 8072, 1, 5, 3, 1, 3), NetsnmpCacheStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nsCacheStatus.setDescription("The current status of this particular cache entry.\nAcceptable values for Set requests are 'enabled(1)',\n'disabled(2)' or 'empty(3)' (to clear all cached data).\nRequests to read the value of such an object will\nreturn 'disabled(2)' through to 'expired(5)'.")
nsErrorHistory = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 1, 6))
nsConfiguration = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 1, 7))
nsConfigDebug = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 1, 7, 1))
nsDebugEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8072, 1, 7, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nsDebugEnabled.setDescription("Whether the agent is configured to generate debugging output")
nsDebugOutputAll = MibScalar((1, 3, 6, 1, 4, 1, 8072, 1, 7, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nsDebugOutputAll.setDescription("Whether the agent is configured to display all debugging output\nrather than filtering on individual debug tokens.  Nothing will\nbe generated unless nsDebugEnabled is also true(1)")
nsDebugDumpPdu = MibScalar((1, 3, 6, 1, 4, 1, 8072, 1, 7, 1, 3), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nsDebugDumpPdu.setDescription("Whether the agent is configured to display raw packet dumps.\nThis is unrelated to the nsDebugEnabled setting.")
nsDebugTokenTable = MibTable((1, 3, 6, 1, 4, 1, 8072, 1, 7, 1, 4))
if mibBuilder.loadTexts: nsDebugTokenTable.setDescription("A table of individual debug tokens, used to control the selection\nof what debugging output should be produced.  This table is only\neffective if nsDebugOutputAll is false(2), and nothing will\nbe generated unless nsDebugEnabled is also true(1)")
nsDebugTokenEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8072, 1, 7, 1, 4, 1)).setIndexNames((1, "NET-SNMP-AGENT-MIB", "nsDebugTokenPrefix"))
if mibBuilder.loadTexts: nsDebugTokenEntry.setDescription("A conceptual row within the debug token table.")
nsDebugTokenPrefix = MibTableColumn((1, 3, 6, 1, 4, 1, 8072, 1, 7, 1, 4, 1, 2), DisplayString()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: nsDebugTokenPrefix.setDescription("A token prefix for which to generate the corresponding\ndebugging output.  Note that debug output will be generated\nfor all registered debug statements sharing this prefix\n(rather than an exact match).  Nothing will be generated\nunless both nsDebuggingEnabled is set true(1) and the\ncorresponding nsDebugTokenStatus value is active(1).")
nsDebugTokenStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 8072, 1, 7, 1, 4, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nsDebugTokenStatus.setDescription("Whether to generate debug output for the corresponding debug\ntoken prefix.  Nothing will be generated unless both\nnsDebuggingEnabled is true(1) and this instance is active(1).\nNote that is valid for an instance to be left with the value\nnotInService(2) indefinitely - i.e. the meaning of 'abnormally\nlong' (see RFC 2579, RowStatus) for this table is infinite.")
nsConfigLogging = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 1, 7, 2))
nsLoggingTable = MibTable((1, 3, 6, 1, 4, 1, 8072, 1, 7, 2, 1))
if mibBuilder.loadTexts: nsLoggingTable.setDescription("A table of individual logging output destinations, used to control\nwhere various levels of output from the agent should be directed.")
nsLoggingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8072, 1, 7, 2, 1, 1)).setIndexNames((0, "NET-SNMP-AGENT-MIB", "nsLogLevel"), (1, "NET-SNMP-AGENT-MIB", "nsLogToken"))
if mibBuilder.loadTexts: nsLoggingEntry.setDescription("A conceptual row within the logging table.")
nsLogLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 8072, 1, 7, 2, 1, 1, 1), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(6,5,0,1,4,2,3,7,)).subtype(namedValues=namedval.NamedValues(("emergency", 0), ("alert", 1), ("critical", 2), ("error", 3), ("warning", 4), ("notice", 5), ("info", 6), ("debug", 7), ))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: nsLogLevel.setDescription("The (minimum) priority level for which this logging entry\nshould be applied.")
nsLogToken = MibTableColumn((1, 3, 6, 1, 4, 1, 8072, 1, 7, 2, 1, 1, 2), DisplayString()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: nsLogToken.setDescription("A token for which to generate logging entries.\nDepending on the style of logging, this may either\nbe simply an arbitrary token, or may have some\nparticular meaning (such as the filename to log to).")
nsLogType = MibTableColumn((1, 3, 6, 1, 4, 1, 8072, 1, 7, 2, 1, 1, 3), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,4,5,3,)).subtype(namedValues=namedval.NamedValues(("stdout", 1), ("stderr", 2), ("file", 3), ("syslog", 4), ("callback", 5), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nsLogType.setDescription("The type of logging for this entry.")
nsLogMaxLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 8072, 1, 7, 2, 1, 1, 4), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(6,5,0,1,4,2,3,7,)).subtype(namedValues=namedval.NamedValues(("emergency", 0), ("alert", 1), ("critical", 2), ("error", 3), ("warning", 4), ("notice", 5), ("info", 6), ("debug", 7), )).clone(0)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nsLogMaxLevel.setDescription("The maximum priority level for which this logging entry\nshould be applied.")
nsLogStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 8072, 1, 7, 2, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nsLogStatus.setDescription("Whether to generate logging output for this entry.\nNote that is valid for an instance to be left with the value\nnotInService(2) indefinitely - i.e. the meaning of 'abnormally\nlong' (see RFC 2579, RowStatus) for this table is infinite.")
nsTransactions = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 1, 8))
nsTransactionTable = MibTable((1, 3, 6, 1, 4, 1, 8072, 1, 8, 1))
if mibBuilder.loadTexts: nsTransactionTable.setDescription("Lists currently outstanding transactions in the net-snmp agent.\nThis includes requests to AgentX subagents, or proxied SNMP agents.")
nsTransactionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8072, 1, 8, 1, 1)).setIndexNames((0, "NET-SNMP-AGENT-MIB", "nsTransactionID"))
if mibBuilder.loadTexts: nsTransactionEntry.setDescription("A row describing a given transaction.")
nsTransactionID = MibTableColumn((1, 3, 6, 1, 4, 1, 8072, 1, 8, 1, 1, 1), Unsigned32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 4294967295L))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: nsTransactionID.setDescription("The internal identifier for a given transaction.")
nsTransactionMode = MibTableColumn((1, 3, 6, 1, 4, 1, 8072, 1, 8, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsTransactionMode.setDescription("The mode number for the current operation being performed.")
netSnmpAgentMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 8072, 3, 1, 2)).setRevisions(("2005-02-07 00:00","2002-02-09 00:00",))
if mibBuilder.loadTexts: netSnmpAgentMIB.setOrganization("www.net-snmp.org")
if mibBuilder.loadTexts: netSnmpAgentMIB.setContactInfo("postal:   Wes Hardaker\nP.O. Box 382\nDavis CA  95617\n\nemail:    net-snmp-coders@lists.sourceforge.net")
if mibBuilder.loadTexts: netSnmpAgentMIB.setDescription("Defines control and monitoring structures for the Net-SNMP agent.")
nsConfigGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 5, 2, 7))

# Augmentions

# Notifications

nsNotifyShutdown = NotificationType((1, 3, 6, 1, 4, 1, 8072, 4, 0, 2)).setObjects()
nsNotifyRestart = NotificationType((1, 3, 6, 1, 4, 1, 8072, 4, 0, 3)).setObjects()
nsNotifyStart = NotificationType((1, 3, 6, 1, 4, 1, 8072, 4, 0, 1)).setObjects()

# Groups

nsAgentNotifyGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8072, 5, 2, 9)).setObjects(("NET-SNMP-AGENT-MIB", "nsNotifyShutdown"), ("NET-SNMP-AGENT-MIB", "nsNotifyRestart"), ("NET-SNMP-AGENT-MIB", "nsNotifyStart"), )
nsDebugGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8072, 5, 2, 7, 1)).setObjects(("NET-SNMP-AGENT-MIB", "nsDebugTokenStatus"), ("NET-SNMP-AGENT-MIB", "nsDebugOutputAll"), ("NET-SNMP-AGENT-MIB", "nsDebugEnabled"), ("NET-SNMP-AGENT-MIB", "nsDebugDumpPdu"), )
nsTransactionGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8072, 5, 2, 8)).setObjects(("NET-SNMP-AGENT-MIB", "nsTransactionMode"), )
nsLoggingGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8072, 5, 2, 7, 2)).setObjects(("NET-SNMP-AGENT-MIB", "nsLogType"), ("NET-SNMP-AGENT-MIB", "nsLogStatus"), ("NET-SNMP-AGENT-MIB", "nsLogMaxLevel"), )
nsModuleGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8072, 5, 2, 2)).setObjects(("NET-SNMP-AGENT-MIB", "nsModuleName"), ("NET-SNMP-AGENT-MIB", "nsModuleTimeout"), ("NET-SNMP-AGENT-MIB", "nsModuleModes"), )
nsCacheGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8072, 5, 2, 4)).setObjects(("NET-SNMP-AGENT-MIB", "nsCacheTimeout"), ("NET-SNMP-AGENT-MIB", "nsCacheEnabled"), ("NET-SNMP-AGENT-MIB", "nsCacheDefaultTimeout"), ("NET-SNMP-AGENT-MIB", "nsCacheStatus"), )

# Exports

# Module identity
mibBuilder.exportSymbols("NET-SNMP-AGENT-MIB", PYSNMP_MODULE_ID=netSnmpAgentMIB)

# Types
mibBuilder.exportSymbols("NET-SNMP-AGENT-MIB", NetsnmpCacheStatus=NetsnmpCacheStatus)

# Objects
mibBuilder.exportSymbols("NET-SNMP-AGENT-MIB", nsVersion=nsVersion, nsMibRegistry=nsMibRegistry, nsModuleTable=nsModuleTable, nsModuleEntry=nsModuleEntry, nsmContextName=nsmContextName, nsmRegistrationPoint=nsmRegistrationPoint, nsmRegistrationPriority=nsmRegistrationPriority, nsModuleName=nsModuleName, nsModuleModes=nsModuleModes, nsModuleTimeout=nsModuleTimeout, nsExtensions=nsExtensions, nsDLMod=nsDLMod, nsCache=nsCache, nsCacheDefaultTimeout=nsCacheDefaultTimeout, nsCacheEnabled=nsCacheEnabled, nsCacheTable=nsCacheTable, nsCacheEntry=nsCacheEntry, nsCachedOID=nsCachedOID, nsCacheTimeout=nsCacheTimeout, nsCacheStatus=nsCacheStatus, nsErrorHistory=nsErrorHistory, nsConfiguration=nsConfiguration, nsConfigDebug=nsConfigDebug, nsDebugEnabled=nsDebugEnabled, nsDebugOutputAll=nsDebugOutputAll, nsDebugDumpPdu=nsDebugDumpPdu, nsDebugTokenTable=nsDebugTokenTable, nsDebugTokenEntry=nsDebugTokenEntry, nsDebugTokenPrefix=nsDebugTokenPrefix, nsDebugTokenStatus=nsDebugTokenStatus, nsConfigLogging=nsConfigLogging, nsLoggingTable=nsLoggingTable, nsLoggingEntry=nsLoggingEntry, nsLogLevel=nsLogLevel, nsLogToken=nsLogToken, nsLogType=nsLogType, nsLogMaxLevel=nsLogMaxLevel, nsLogStatus=nsLogStatus, nsTransactions=nsTransactions, nsTransactionTable=nsTransactionTable, nsTransactionEntry=nsTransactionEntry, nsTransactionID=nsTransactionID, nsTransactionMode=nsTransactionMode, netSnmpAgentMIB=netSnmpAgentMIB, nsConfigGroups=nsConfigGroups)

# Notifications
mibBuilder.exportSymbols("NET-SNMP-AGENT-MIB", nsNotifyShutdown=nsNotifyShutdown, nsNotifyRestart=nsNotifyRestart, nsNotifyStart=nsNotifyStart)

# Groups
mibBuilder.exportSymbols("NET-SNMP-AGENT-MIB", nsAgentNotifyGroup=nsAgentNotifyGroup, nsDebugGroup=nsDebugGroup, nsTransactionGroup=nsTransactionGroup, nsLoggingGroup=nsLoggingGroup, nsModuleGroup=nsModuleGroup, nsCacheGroup=nsCacheGroup)
