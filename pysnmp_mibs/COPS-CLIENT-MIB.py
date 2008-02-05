# PySNMP SMI module. Autogenerated from smidump -f python COPS-CLIENT-MIB
# by libsmi2pysnmp-0.0.8-alpha at Tue Feb  5 21:05:00 2008,
# Python version (2, 4, 4, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( InetAddress, InetAddressType, ) = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Counter32, Integer32, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "mib-2")
( RowStatus, TextualConvention, TimeInterval, TimeStamp, ) = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "TimeInterval", "TimeStamp")

# Types

class CopsAuthType(Integer):
    subtypeSpec = Integer.subtypeSpec+constraint.SingleValueConstraint(2,4,3,5,1,0,)
    namedValues = namedval.NamedValues(("authNone", 0), ("authOther", 1), ("authIpSecAh", 2), ("authIpSecEsp", 3), ("authTls", 4), ("authCopsIntegrity", 5), )
    pass

class CopsClientState(Integer):
    subtypeSpec = Integer.subtypeSpec+constraint.SingleValueConstraint(5,2,3,4,1,6,)
    namedValues = namedval.NamedValues(("copsClientInvalid", 1), ("copsClientTcpconnected", 2), ("copsClientAuthenticating", 3), ("copsClientSecAccepted", 4), ("copsClientAccepted", 5), ("copsClientTimingout", 6), )
    pass

class CopsErrorCode(Integer):
    subtypeSpec = Integer.subtypeSpec+constraint.SingleValueConstraint(15,14,12,6,7,5,2,3,11,0,4,1,8,10,9,13,)
    namedValues = namedval.NamedValues(("errorOther", 0), ("errorBadHandle", 1), ("errorUnspecified", 10), ("errorShuttingDown", 11), ("errorRedirectToPreferredServer", 12), ("errorUnknownCopsObject", 13), ("errorAuthenticationFailure", 14), ("errorAuthenticationMissing", 15), ("errorInvalidHandleReference", 2), ("errorBadMessageFormat", 3), ("errorUnableToProcess", 4), ("errorMandatoryClientSiMissing", 5), ("errorUnsupportedClientType", 6), ("errorMandatoryCopsObjectMissing", 7), ("errorClientFailure", 8), ("errorCommunicationFailure", 9), )
    pass

class CopsServerEntryType(Integer):
    subtypeSpec = Integer.subtypeSpec+constraint.SingleValueConstraint(2,1,)
    namedValues = namedval.NamedValues(("copsServerStatic", 1), ("copsServerRedirect", 2), )
    pass

class CopsTcpPort(Integer32):
    subtypeSpec = Integer32.subtypeSpec+constraint.ValueRangeConstraint(0,65535)
    pass


# Objects

copsClientMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 89)).setRevisions(("2000-09-28 00:00",))
if mibBuilder.loadTexts: copsClientMIB.setOrganization("IETF RSVP Admission Policy Working Group")
if mibBuilder.loadTexts: copsClientMIB.setContactInfo("       Andrew Smith (WG co-chair)\nPhone: +1 408 579 2821\nEmail: ah_smith@pacbell.net\n\n       Mark Stevens (WG co-chair)\nPhone: +1 978 287 9102\nEmail: markstevens@lucent.com\n\nEditor: Andrew Smith\nPhone: +1 408 579 2821\nEmail: ah_smith@pacbell.net\n\nEditor: David Partain\nPhone: +46 13 28 41 44\nEmail: David.Partain@ericsson.com\n\nEditor: John Seligson\nPhone: +1 408 495 2992\nEmail: jseligso@nortelnetworks.com")
if mibBuilder.loadTexts: copsClientMIB.setDescription("The COPS Client MIB module")
copsClientMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 89, 1))
copsClientCapabilitiesGroup = MibIdentifier((1, 3, 6, 1, 2, 1, 89, 1, 1))
copsClientCapabilities = MibScalar((1, 3, 6, 1, 2, 1, 89, 1, 1, 1), Bits().subtype(namedValues=namedval.NamedValues(("copsClientVersion1", 0), ("copsClientAuthIpSecAh", 1), ("copsClientAuthIpSecEsp", 2), ("copsClientAuthTls", 3), ("copsClientAuthInteg", 4), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: copsClientCapabilities.setDescription("A list of the optional capabilities that this COPS client\nsupports.")
copsClientStatusGroup = MibIdentifier((1, 3, 6, 1, 2, 1, 89, 1, 2))
copsClientServerCurrentTable = MibTable((1, 3, 6, 1, 2, 1, 89, 1, 2, 1))
if mibBuilder.loadTexts: copsClientServerCurrentTable.setDescription("A table of information regarding COPS servers as seen from the\npoint of view of a COPS client. This table contains entries\nfor both statically-configured and dynamically-learned servers\n(from a PDP Redirect operation). One entry exists in this table\nfor each COPS Client-Type served by the COPS server. In addition,\nan entry will exist with copsClientServerClientType 0 (zero)\nrepresenting information about the underlying connection itself:\nthis is consistent with the COPS specification which reserves\nthis value for this purpose.")
copsClientServerCurrentEntry = MibTableRow((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1)).setIndexNames((0, "COPS-CLIENT-MIB", "copsClientServerAddressType"), (0, "COPS-CLIENT-MIB", "copsClientServerAddress"), (0, "COPS-CLIENT-MIB", "copsClientServerClientType"))
if mibBuilder.loadTexts: copsClientServerCurrentEntry.setDescription("A set of information regarding a single COPS server serving\na single COPS Client-Type from the point of view of a COPS\nclient.")
copsClientServerAddressType = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 1), InetAddressType()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: copsClientServerAddressType.setDescription("The type of address in copsClientServerAddress.")
copsClientServerAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 2), InetAddress()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: copsClientServerAddress.setDescription("The IPv4, IPv6 or DNS address of a COPS Server. Note that,\nsince this is an index to the table, the DNS name must be\nshort enough to fit into the maximum length of indices allowed\nby the management protocol in use.")
copsClientServerClientType = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: copsClientServerClientType.setDescription("The COPS protocol Client-Type for which this entry\napplies. Multiple Client-Types can be served by a single\nCOPS server. The value 0 (zero) indicates that this\nentry contains information about the underlying connection\nitself.")
copsClientServerTcpPort = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 4), CopsTcpPort()).setMaxAccess("readonly")
if mibBuilder.loadTexts: copsClientServerTcpPort.setDescription("The TCP port number on the COPS server to which the\nclient should connect/is connected.")
copsClientServerType = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 5), CopsServerEntryType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: copsClientServerType.setDescription("Indicator of the source of this COPS server information.\nCOPS servers may be configured by network management\ninto copsClientServerConfigTable and appear in this entry\nwith type copsServerStatic(1). Alternatively, the may be\nnotified from another COPS server by means of the COPS\nPDP-Redirect mechanism and appear as copsServerRedirect(2).")
copsClientServerAuthType = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 6), CopsAuthType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: copsClientServerAuthType.setDescription("Indicator of the current security mode in use between\nclient and this COPS server.")
copsClientServerLastConnAttempt = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 7), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: copsClientServerLastConnAttempt.setDescription("Timestamp of the last time that this client attempted to\nconnect to this COPS server.")
copsClientState = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 8), CopsClientState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: copsClientState.setDescription("The state of the connection and COPS protocol with respect\n\n\nto this COPS server.")
copsClientServerKeepaliveTime = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 9), TimeInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: copsClientServerKeepaliveTime.setDescription("The value of the COPS protocol Keepalive timeout, in\ncentiseconds, currently in use by this client, as\nspecified by this COPS server in the Client-Accept operation.\nA value of zero indicates no keepalive activity is expected.")
copsClientServerAccountingTime = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 10), TimeInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: copsClientServerAccountingTime.setDescription("The value of the COPS protocol Accounting timeout, in\ncentiseconds, currently in use by this client, as specified\nby the COPS server in the Client-Accept operation. A value\nof zero indicates no accounting activity is to be performed.")
copsClientInPkts = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: copsClientInPkts.setDescription("A count of the total number of COPS messages that this client\nhas received from this COPS server marked for this Client-Type.\nThis value is cumulative since agent restart and is not zeroed\non new connections.")
copsClientOutPkts = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: copsClientOutPkts.setDescription("A count of the total number of COPS messages that this client\nhas sent to this COPS server marked for this Client-Type. This\nvalue is cumulative since agent restart and is not zeroed on new\n\n\nconnections.")
copsClientInErrs = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: copsClientInErrs.setDescription("A count of the total number of COPS messages that this client\nhas received from this COPS server marked for this Client-Type\nthat contained errors in syntax. This value is cumulative since\nagent restart and is not zeroed on new connections.")
copsClientLastError = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 14), CopsErrorCode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: copsClientLastError.setDescription("The code contained in the last COPS protocol Error Object\nreceived by this client from this COPS server marked for this\nClient-Type. This value is not zeroed on COPS Client-Open\noperations.")
copsClientTcpConnectAttempts = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: copsClientTcpConnectAttempts.setDescription("A count of the number of times that this COPS client has tried\n(successfully or otherwise) to open an TCP connection to a COPS\nserver. This value is cumulative  since agent restart and is not\nzeroed on new connections. This value is not incremented for\nentries representing a non-zero Client-Type.")
copsClientTcpConnectFailures = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: copsClientTcpConnectFailures.setDescription("A count of the number of times that this COPS client has failed\nto open an TCP connection to a COPS server. This value is\ncumulative since agent restart and is not zeroed on new\nconnections. This value is not incremented for\n\n\nentries representing a non-zero Client-Type.")
copsClientOpenAttempts = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: copsClientOpenAttempts.setDescription("A count of the number of times that this COPS client has tried\nto perform a COPS Client-Open to a COPS server for this\nClient-Type. This value is cumulative since agent restart and is\nnot zeroed on new connections.")
copsClientOpenFailures = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: copsClientOpenFailures.setDescription("A count of the number of times that this COPS client has failed\nto perform a COPS Client-Open to a COPS server for this\nClient-Type. This value is cumulative since agent restart and is\nnot zeroed on new connections.")
copsClientErrUnsupportClienttype = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: copsClientErrUnsupportClienttype.setDescription("A count of the total number of COPS messages that this client\nhas received from COPS servers that referred to Client-Types\nthat are unsupported by this client. This value is cumulative\nsince agent restart and is not zeroed on new connections. This\nvalue is not incremented for entries representing a non-zero\nClient-Type.")
copsClientErrUnsupportedVersion = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: copsClientErrUnsupportedVersion.setDescription("A count of the total number of COPS messages that this client\nhas received from COPS servers marked for this Client-Type that\nhad a COPS protocol Version number that is unsupported by this\nclient. This value is cumulative since agent restart and is not\nzeroed on new connections.")
copsClientErrLengthMismatch = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: copsClientErrLengthMismatch.setDescription("A count of the total number of COPS messages that this client\nhas received from COPS servers marked for this Client-Type that\nhad a COPS protocol Message Length that did not match the actual\nreceived message. This value is cumulative since agent restart\nand is not zeroed on new connections.")
copsClientErrUnknownOpcode = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: copsClientErrUnknownOpcode.setDescription("A count of the total number of COPS messages that this client\nhas received from COPS servers marked for this Client-Type that\nhad a COPS protocol Op Code that was unrecognised by this\nclient. This value is cumulative since agent restart and is not\nzeroed on new connections.")
copsClientErrUnknownCnum = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: copsClientErrUnknownCnum.setDescription("A count of the total number of COPS messages that this client\nhas received from COPS servers marked for this Client-Type that\ncontained a COPS protocol object C-Num that was unrecognised by\nthis client. This value is cumulative since agent restart and is\nnot zeroed on new connections.")
copsClientErrBadCtype = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: copsClientErrBadCtype.setDescription("A count of the total number of COPS messages that this client\nhas received from COPS servers marked for this Client-Type that\ncontained a COPS protocol object C-Type that was not defined for\nthe C-Nums known by this client. This value is cumulative since\nagent restart and is not zeroed on new connections.")
copsClientErrBadSends = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: copsClientErrBadSends.setDescription("A count of the total number of COPS messages that this client\nattempted to send to COPS servers marked for this Client-Type\nthat resulted in a transmit error. This value is cumulative\nsince agent restart and is not zeroed on new connections.")
copsClientErrWrongObjects = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 26), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: copsClientErrWrongObjects.setDescription("A count of the total number of COPS messages that this client\nhas received from COPS servers marked for this Client-Type that\ndid not contain a permitted set of COPS protocol objects. This\nvalue is cumulative since agent restart and is not zeroed on new\nconnections.")
copsClientErrWrongOpcode = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 27), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: copsClientErrWrongOpcode.setDescription("A count of the total number of COPS messages that this client\nhas received from COPS servers marked for this Client-Type that\nhad a COPS protocol Op Code that should not have been sent to a\nCOPS client e.g. Open-Requests. This value is cumulative since\nagent restart and is not zeroed on new connections.")
copsClientKaTimedoutClients = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 28), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: copsClientKaTimedoutClients.setDescription("A count of the total number of times that this client has\nbeen shut down for this Client-Type by COPS servers that had\ndetected a COPS protocol Keepalive timeout. This value is\ncumulative since agent restart and is not zeroed on new\nconnections.")
copsClientErrAuthFailures = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 29), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: copsClientErrAuthFailures.setDescription("A count of the total number of times that this client has\nreceived a COPS message marked for this Client-Type which\ncould not be authenticated using the authentication mechanism\nused by this client.")
copsClientErrAuthMissing = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 30), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: copsClientErrAuthMissing.setDescription("A count of the total number of times that this client has\nreceived a COPS message marked for this Client-Type which did not\ncontain authentication information.")
copsClientConfigGroup = MibIdentifier((1, 3, 6, 1, 2, 1, 89, 1, 3))
copsClientServerConfigTable = MibTable((1, 3, 6, 1, 2, 1, 89, 1, 3, 1))
if mibBuilder.loadTexts: copsClientServerConfigTable.setDescription("Table of possible COPS servers to try to connect to in order\nof copsClientServerConfigPriority. There may be multiple\nentries in this table for the same server and client-type which\nspecify different security mechanisms: these mechanisms will\nbe attempted by the client in the priority order given. Note\nthat a server learned by means of PDPRedirect always takes\npriority over any of these configured entries.")
copsClientServerConfigEntry = MibTableRow((1, 3, 6, 1, 2, 1, 89, 1, 3, 1, 1)).setIndexNames((0, "COPS-CLIENT-MIB", "copsClientServerConfigAddrType"), (0, "COPS-CLIENT-MIB", "copsClientServerConfigAddress"), (0, "COPS-CLIENT-MIB", "copsClientServerConfigClientType"), (0, "COPS-CLIENT-MIB", "copsClientServerConfigAuthType"))
if mibBuilder.loadTexts: copsClientServerConfigEntry.setDescription("A set of configuration information regarding a single\n\n\nCOPS server from the point of view of a COPS client.")
copsClientServerConfigAddrType = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 3, 1, 1, 1), InetAddressType()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: copsClientServerConfigAddrType.setDescription("The type of address in copsClientServerConfigAddress.")
copsClientServerConfigAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 3, 1, 1, 2), InetAddress()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: copsClientServerConfigAddress.setDescription("The IPv4, IPv6 or DNS address of a COPS Server. Note that,\nsince this is an index to the table, the DNS name must be\nshort enough to fit into the maximum length of indices allowed\nby the management protocol in use.")
copsClientServerConfigClientType = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: copsClientServerConfigClientType.setDescription("The COPS protocol Client-Type for which this entry\napplies and for which this COPS server is capable\nof serving. Multiple Client-Types can be served by a\nsingle COPS server.")
copsClientServerConfigAuthType = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 3, 1, 1, 4), CopsAuthType()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: copsClientServerConfigAuthType.setDescription("The type of authentication mechanism for this COPS client\nto request when negotiating security at the start of a\nconnection to a COPS server.")
copsClientServerConfigTcpPort = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 3, 1, 1, 5), CopsTcpPort()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: copsClientServerConfigTcpPort.setDescription("The TCP port number on the COPS server to which the\nclient should connect.")
copsClientServerConfigPriority = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 3, 1, 1, 6), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: copsClientServerConfigPriority.setDescription("The priority of this entry relative to other entries.\nCOPS client will attempt to contact COPS servers for the\nappropriate Client-Type. Higher numbers are tried first. The\norder to be used amongst server entries with the same priority\nis undefined. COPS servers that are notified to the client using\nthe COPS protocol PDP-Redirect mechanism are always used in\npreference to any entries in this table.")
copsClientServerConfigRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 3, 1, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: copsClientServerConfigRowStatus.setDescription("State of this entry in the table.")
copsClientServerConfigRetryAlgrm = MibScalar((1, 3, 6, 1, 2, 1, 89, 1, 3, 2), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(3,1,2,)).subtype(namedValues=namedval.NamedValues(("other", 1), ("sequential", 2), ("roundRobin", 3), )).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: copsClientServerConfigRetryAlgrm.setDescription("The algorithm by which the client should retry when it\nfails to connect to a COPS server.")
copsClientServerConfigRetryCount = MibScalar((1, 3, 6, 1, 2, 1, 89, 1, 3, 3), Unsigned32().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: copsClientServerConfigRetryCount.setDescription("A retry count for use by the retry algorithm.  Each retry\nalgorithm needs to specify how it uses this value.\n\nFor the 'sequential(2)' algorithm, this value is the\nnumber of times the client should retry to connect\nto one COPS server before moving on to another.\nFor the 'roundRobin(3)' algorithm, this value is not used.")
copsClientServerConfigRetryIntvl = MibScalar((1, 3, 6, 1, 2, 1, 89, 1, 3, 4), TimeInterval().clone(1000)).setMaxAccess("readwrite").setUnits("centi-seconds")
if mibBuilder.loadTexts: copsClientServerConfigRetryIntvl.setDescription("A retry interval for use by the retry algorithm.  Each retry\nalgorithm needs to specify how it uses this value.\n\nFor the 'sequential(2)' algorithm, this value is the time to\nwait between retries of a connection to the same COPS server.\n\nFor the 'roundRobin(3)' algorithm, the client always attempts\nto connect to each Server in turn, until one succeeds or they\nall fail; if they all fail, then the client waits for the value\nof this interval before restarting the algorithm.")
copsClientConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 89, 2))
copsClientGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 89, 2, 1))
copsClientCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 89, 2, 2))

# Augmentions

# Groups

copsDeviceConfigGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 89, 2, 1, 2)).setObjects(("COPS-CLIENT-MIB", "copsClientServerConfigPriority"), ("COPS-CLIENT-MIB", "copsClientServerConfigRetryIntvl"), ("COPS-CLIENT-MIB", "copsClientServerConfigTcpPort"), ("COPS-CLIENT-MIB", "copsClientServerConfigRetryAlgrm"), ("COPS-CLIENT-MIB", "copsClientServerConfigRowStatus"), ("COPS-CLIENT-MIB", "copsClientServerConfigRetryCount"), )
copsDeviceStatusGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 89, 2, 1, 1)).setObjects(("COPS-CLIENT-MIB", "copsClientOutPkts"), ("COPS-CLIENT-MIB", "copsClientServerType"), ("COPS-CLIENT-MIB", "copsClientErrAuthFailures"), ("COPS-CLIENT-MIB", "copsClientErrUnknownCnum"), ("COPS-CLIENT-MIB", "copsClientErrLengthMismatch"), ("COPS-CLIENT-MIB", "copsClientServerKeepaliveTime"), ("COPS-CLIENT-MIB", "copsClientServerLastConnAttempt"), ("COPS-CLIENT-MIB", "copsClientErrAuthMissing"), ("COPS-CLIENT-MIB", "copsClientInErrs"), ("COPS-CLIENT-MIB", "copsClientTcpConnectFailures"), ("COPS-CLIENT-MIB", "copsClientErrUnknownOpcode"), ("COPS-CLIENT-MIB", "copsClientTcpConnectAttempts"), ("COPS-CLIENT-MIB", "copsClientErrBadCtype"), ("COPS-CLIENT-MIB", "copsClientOpenFailures"), ("COPS-CLIENT-MIB", "copsClientLastError"), ("COPS-CLIENT-MIB", "copsClientServerAuthType"), ("COPS-CLIENT-MIB", "copsClientErrWrongObjects"), ("COPS-CLIENT-MIB", "copsClientInPkts"), ("COPS-CLIENT-MIB", "copsClientCapabilities"), ("COPS-CLIENT-MIB", "copsClientState"), ("COPS-CLIENT-MIB", "copsClientKaTimedoutClients"), ("COPS-CLIENT-MIB", "copsClientErrUnsupportedVersion"), ("COPS-CLIENT-MIB", "copsClientServerTcpPort"), ("COPS-CLIENT-MIB", "copsClientErrBadSends"), ("COPS-CLIENT-MIB", "copsClientErrWrongOpcode"), ("COPS-CLIENT-MIB", "copsClientErrUnsupportClienttype"), ("COPS-CLIENT-MIB", "copsClientOpenAttempts"), ("COPS-CLIENT-MIB", "copsClientServerAccountingTime"), )

# Exports

# Module identity
mibBuilder.exportSymbols("COPS-CLIENT-MIB", PYSNMP_MODULE_ID=copsClientMIB)

# Types
mibBuilder.exportSymbols("COPS-CLIENT-MIB", CopsAuthType=CopsAuthType, CopsClientState=CopsClientState, CopsErrorCode=CopsErrorCode, CopsServerEntryType=CopsServerEntryType, CopsTcpPort=CopsTcpPort)

# Objects
mibBuilder.exportSymbols("COPS-CLIENT-MIB", copsClientMIB=copsClientMIB, copsClientMIBObjects=copsClientMIBObjects, copsClientCapabilitiesGroup=copsClientCapabilitiesGroup, copsClientCapabilities=copsClientCapabilities, copsClientStatusGroup=copsClientStatusGroup, copsClientServerCurrentTable=copsClientServerCurrentTable, copsClientServerCurrentEntry=copsClientServerCurrentEntry, copsClientServerAddressType=copsClientServerAddressType, copsClientServerAddress=copsClientServerAddress, copsClientServerClientType=copsClientServerClientType, copsClientServerTcpPort=copsClientServerTcpPort, copsClientServerType=copsClientServerType, copsClientServerAuthType=copsClientServerAuthType, copsClientServerLastConnAttempt=copsClientServerLastConnAttempt, copsClientState=copsClientState, copsClientServerKeepaliveTime=copsClientServerKeepaliveTime, copsClientServerAccountingTime=copsClientServerAccountingTime, copsClientInPkts=copsClientInPkts, copsClientOutPkts=copsClientOutPkts, copsClientInErrs=copsClientInErrs, copsClientLastError=copsClientLastError, copsClientTcpConnectAttempts=copsClientTcpConnectAttempts, copsClientTcpConnectFailures=copsClientTcpConnectFailures, copsClientOpenAttempts=copsClientOpenAttempts, copsClientOpenFailures=copsClientOpenFailures, copsClientErrUnsupportClienttype=copsClientErrUnsupportClienttype, copsClientErrUnsupportedVersion=copsClientErrUnsupportedVersion, copsClientErrLengthMismatch=copsClientErrLengthMismatch, copsClientErrUnknownOpcode=copsClientErrUnknownOpcode, copsClientErrUnknownCnum=copsClientErrUnknownCnum, copsClientErrBadCtype=copsClientErrBadCtype, copsClientErrBadSends=copsClientErrBadSends, copsClientErrWrongObjects=copsClientErrWrongObjects, copsClientErrWrongOpcode=copsClientErrWrongOpcode, copsClientKaTimedoutClients=copsClientKaTimedoutClients, copsClientErrAuthFailures=copsClientErrAuthFailures, copsClientErrAuthMissing=copsClientErrAuthMissing, copsClientConfigGroup=copsClientConfigGroup, copsClientServerConfigTable=copsClientServerConfigTable, copsClientServerConfigEntry=copsClientServerConfigEntry, copsClientServerConfigAddrType=copsClientServerConfigAddrType, copsClientServerConfigAddress=copsClientServerConfigAddress, copsClientServerConfigClientType=copsClientServerConfigClientType, copsClientServerConfigAuthType=copsClientServerConfigAuthType, copsClientServerConfigTcpPort=copsClientServerConfigTcpPort, copsClientServerConfigPriority=copsClientServerConfigPriority, copsClientServerConfigRowStatus=copsClientServerConfigRowStatus, copsClientServerConfigRetryAlgrm=copsClientServerConfigRetryAlgrm, copsClientServerConfigRetryCount=copsClientServerConfigRetryCount, copsClientServerConfigRetryIntvl=copsClientServerConfigRetryIntvl, copsClientConformance=copsClientConformance, copsClientGroups=copsClientGroups, copsClientCompliances=copsClientCompliances)

# Groups
mibBuilder.exportSymbols("COPS-CLIENT-MIB", copsDeviceConfigGroup=copsDeviceConfigGroup, copsDeviceStatusGroup=copsDeviceStatusGroup)
