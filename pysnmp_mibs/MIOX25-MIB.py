# PySNMP SMI module. Autogenerated from smidump -f python MIOX25-MIB
# by libsmi2pysnmp-0.0.8-alpha at Tue Feb  5 21:05:12 2008,
# Python version (2, 4, 4, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( ifIndex, transmission, ) = mibBuilder.importSymbols("RFC1213-MIB", "ifIndex", "transmission")
( InstancePointer, ) = mibBuilder.importSymbols("RFC1316-MIB", "InstancePointer")
( PositiveInteger, ) = mibBuilder.importSymbols("RFC1381-MIB", "PositiveInteger")
( X121Address, ) = mibBuilder.importSymbols("RFC1382-MIB", "X121Address")
( Bits, Counter32, Integer32, Integer32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, TimeTicks, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Integer32", "Integer32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "TimeTicks")
( DisplayString, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString")

# Objects

miox = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 38))
mioxPle = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 38, 1))
mioxPleTable = MibTable((1, 3, 6, 1, 2, 1, 10, 38, 1, 1))
if mibBuilder.loadTexts: mioxPleTable.setDescription("This table contains information relative to\nan interface to an X.25 Packet Level Entity\n(PLE).")
mioxPleEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 38, 1, 1, 1)).setIndexNames((0, "RFC1213-MIB", "ifIndex"))
if mibBuilder.loadTexts: mioxPleEntry.setDescription("These objects manage the encapsulation of\nother protocols within X.25.")
mioxPleMaxCircuits = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 38, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 2147483647L))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mioxPleMaxCircuits.setDescription("The maximum number of X.25 circuits that\ncan be open at one time for this interface.\nA value of zero indicates the interface will\nnot allow any additional circuits (as it may\nsoon be shutdown).  A value of 2147483647\nallows an unlimited number of circuits.")
mioxPleRefusedConnections = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 38, 1, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mioxPleRefusedConnections.setDescription("The number of X.25 calls from a remote\nsystems to this system that were cleared by\nthis system.  The interface instance should\nidentify the X.25 interface the call came in\non.")
mioxPleEnAddrToX121LkupFlrs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 38, 1, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mioxPleEnAddrToX121LkupFlrs.setDescription("The number of times a translation from an\nEncapsulated Address to an X.121 address\nfailed to find a corresponding X.121\naddress.  Encapsulated addresses can be\nlooked up in the mioxPeerTable or translated\nvia an algorithm as for the DDN.  Addresses\nthat are successfully recognized do not\nincrement this counter.  Addresses that are\nnot recognized (reflecting an abnormal\npacket delivery condition) increment this\ncounter.\n\nIf an address translation fails, it may be\ndifficult to determine which PLE entry\nshould count the failure.  In such cases the\nfirst likely entry in this table should be\nselected.  Agents should record the failure\neven if they are unsure which PLE should be\nassociated with the failure.")
mioxPleLastFailedEnAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 38, 1, 1, 1, 4), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(2, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mioxPleLastFailedEnAddr.setDescription("The last Encapsulated address that failed\nto find a corresponding X.121 address and\ncaused mioxPleEnAddrToX121LkupFlrs to be\nincremented.  The first octet of this object\ncontains the encapsulation type, the\nremaining octets contain the address of that\ntype that failed.  Thus for an IP address,\nthe length will be five octets, the first\noctet will contain 204 (hex CC), and the\nlast four octets will contain the IP\naddress.  For a snap encapsulation, the\nfirst byte would be 128 (hex 80) and the\nrest of the octet string would have the snap\nheader.")
mioxPleEnAddrToX121LkupFlrTime = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 38, 1, 1, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mioxPleEnAddrToX121LkupFlrTime.setDescription("The most recent value of sysUpTime when the\ntranslation from an Encapsulated Address to\nX.121 address failed to find a corresponding\nX.121 address.")
mioxPleX121ToEnAddrLkupFlrs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 38, 1, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mioxPleX121ToEnAddrLkupFlrs.setDescription("The number of times the translation from an\nX.121 address to an Encapsulated Address\nfailed to find a corresponding Encapsulated\nAddress.  Addresses successfully recognized\nby an algorithm do not increment this\ncounter.  This counter reflects the number\nof times call acceptance encountered the\nabnormal condition of not recognizing the\npeer.")
mioxPleLastFailedX121Address = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 38, 1, 1, 1, 7), X121Address()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mioxPleLastFailedX121Address.setDescription("The last X.121 address that caused\nmioxPleX121ToEnAddrLkupFlrs to increase.")
mioxPleX121ToEnAddrLkupFlrTime = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 38, 1, 1, 1, 8), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mioxPleX121ToEnAddrLkupFlrTime.setDescription("The most recent value of sysUpTime when the\ntranslation from an X.121 address to an\nEncapsulated Address failed to find a\ncorresponding Encapsulated Address.")
mioxPleQbitFailures = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 38, 1, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mioxPleQbitFailures.setDescription("The number of times a connection was closed\nbecause of a Q-bit failure.")
mioxPleQbitFailureRemoteAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 38, 1, 1, 1, 10), X121Address()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mioxPleQbitFailureRemoteAddress.setDescription("The remote address of the most recent\n(last) connection that was closed because of\na Q-bit failure.")
mioxPleQbitFailureTime = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 38, 1, 1, 1, 11), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mioxPleQbitFailureTime.setDescription("The most recent value of sysUpTime when a\nconnection was closed because of a Q-bit\nfailure.  This will also be the last time\nthat mioxPleQbitFailures was incremented.")
mioxPleMinimumOpenTimer = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 38, 1, 1, 1, 12), PositiveInteger().clone(0)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mioxPleMinimumOpenTimer.setDescription("The minimum time in milliseconds this\ninterface will keep a connection open before\nallowing it to be closed.  A value of zero\nindicates no timer.")
mioxPleInactivityTimer = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 38, 1, 1, 1, 13), PositiveInteger().clone(10000)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mioxPleInactivityTimer.setDescription("The amount of time time in milliseconds\nthis interface will keep an idle connection\nopen before closing it.  A value of\n2147483647 indicates no timer.")
mioxPleHoldDownTimer = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 38, 1, 1, 1, 14), PositiveInteger().clone(0)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mioxPleHoldDownTimer.setDescription("The hold down timer in milliseconds.  This\nis the minimum amount of time to wait before\ntrying another call to a host that was\npreviously unsuccessful.  A value of\n2147483647 indicates the host will not be\nretried.")
mioxPleCollisionRetryTimer = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 38, 1, 1, 1, 15), PositiveInteger().clone(0)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mioxPleCollisionRetryTimer.setDescription("The Collision Retry Timer in milliseconds.\nThe time to delay between call attempts when\nthe maximum number of circuits is exceeded\nin a call attempt.")
mioxPleDefaultPeerId = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 38, 1, 1, 1, 16), InstancePointer()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mioxPleDefaultPeerId.setDescription("This identifies the instance of the index\nin the mioxPeerTable for the default\nparameters to use with this interface.\n\nThe entry identified by this object may have\na zero length Encapsulation address and a\nzero length X.121 address.\n\nThese default parameters are used with\nconnections to hosts that do not have\nentries in the mioxPeerTable.  Such\nconnections occur when using ddn-x25 IP-X.25\naddress mapping or when accepting\nconnections from other hosts not in the\nmioxPeerTable.\n\nThe mioxPeerEncTable entry with the same\nindex as the mioxPeerTable entry specifies\nthe call encapsulation types this PLE will\naccept for peers not in the mioxPeerTable.\nIf the mioxPeerEncTable doesn't contain any\nentries, this PLE will not accept calls from\nentries not in the mioxPeerTable.")
mioxPeer = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 38, 2))
mioxPeerTable = MibTable((1, 3, 6, 1, 2, 1, 10, 38, 2, 1))
if mibBuilder.loadTexts: mioxPeerTable.setDescription("This table contains information about the\npossible peers this machine may exchange\npackets with.")
mioxPeerEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 38, 2, 1, 1)).setIndexNames((0, "MIOX25-MIB", "mioxPeerIndex"))
if mibBuilder.loadTexts: mioxPeerEntry.setDescription("Per peer information.")
mioxPeerIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 38, 2, 1, 1, 1), PositiveInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mioxPeerIndex.setDescription("An index value that distinguished one entry\nfrom another.  This index is independent of\nany other index.")
mioxPeerStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 38, 2, 1, 1, 2), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(5,6,4,3,2,1,)).subtype(namedValues=namedval.NamedValues(("valid", 1), ("createRequest", 2), ("underCreation", 3), ("invalid", 4), ("clearCall", 5), ("makeCall", 6), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mioxPeerStatus.setDescription("This reports the status of a peer entry.\nA value of valid indicates a normal entry\nthat is in use by the agent.  A value of\nunderCreation indicates a newly created\nentry which isn't yet in use because the\ncreating management station is still setting\nvalues.\n\nThe value of invalid indicates the entry is\nno longer in use and the agent is free to\ndelete the entry at any time.  A management\nstation is also free to use an entry in the\ninvalid state.\n\nEntries are created by setting a value of\ncreateRequest.  Only non-existent or invalid\nentries can be set to createRequest.  Upon\nreceiving a valid createRequest, the agent\nwill create an entry in the underCreation\nstate.  This object can not be set to a\nvalue of underCreation directly, entries can\nonly be created by setting a value of\ncreateRequest.  Entries that exist in other\nthan the invalid state can not be set to\ncreateRequest.\n\nEntries with a value of underCreation are\nnot used by the system and the management\nstation can change the values of other\nobjects in the table entry.  Management\nstations should also remember to configure\nvalues in the mioxPeerEncTable with the same\npeer index value as this peer entry.\n\nAn entry in the underCreation state can be\nset to valid or invalid.  Entries in the\nunderCreation state will stay in that state\nuntil 1) the agent times them out, 2) they\nare set to valid, 3) they are set to\ninvalid.  If an agent notices an entry has\nbeen in the underCreation state for an\nabnormally long time, it may decide the\nmanagement station has failed and invalidate\nthe entry.  A prudent agent will understand\nthat the management station may need to wait\nfor human input and will allow for that\npossibility in its determination of this\nabnormally long period.\n\nOnce a management station has completed all\nfields of an entry, it will set a value of\nvalid.  This causes the entry to be\nactivated.\n\nEntries in the valid state may also be set\nto makeCall or clearCall to make or clear\nX.25 calls to the peer.  After such a set\nrequest the entry will still be in the valid\nstate.  Setting a value of makeCall causes\nthe agent to initiate an X.25 call request\nto the peer specified by the entry.  Setting\na value of clearCall causes the agent to\ninitiate clearing one X.25 call present to\nthe peer.  Each set request will initiate\nanother call or clear request (up to the\nmaximum allowed); this means that management\nstations that fail to get a response to a\nset request should query to see if a call\nwas in fact placed or cleared before\nretrying the request.  Entries not in the\nvalid state can not be set to makeCall or\nclearCall.\n\nThe values of makeCall and clearCall provide\nfor circuit control on devices which perform\nEthernet Bridging using static circuit\nassignment without address recognition;\nother devices which dynamically place calls\nbased on destination addresses may reject\nsuch requests.\n\nAn agent that (re)creates a new entry\nbecause of a set with createRequest, should\nalso (re)create a mioxPeerEncTable entry\nwith a mioxPeerEncIndex of 1, and a\nmioxPeerEncType of 204 (hex CC).")
mioxPeerMaxCircuits = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 38, 2, 1, 1, 3), PositiveInteger().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mioxPeerMaxCircuits.setDescription("The maximum number of X.25 circuits allowed\nto this peer.")
mioxPeerIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 38, 2, 1, 1, 4), PositiveInteger().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mioxPeerIfIndex.setDescription("The value of the ifIndex object for the\ninterface to X.25 to use to call the peer.")
mioxPeerConnectSeconds = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 38, 2, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mioxPeerConnectSeconds.setDescription("The number of seconds a call to this peer\nwas active.  This counter will be\nincremented by one for every second a\nconnection to a peer was open.  If two calls\nare open at the same time, one second of\nelapsed real time will results in two\nseconds of connect time.")
mioxPeerX25CallParamId = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 38, 2, 1, 1, 6), InstancePointer()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mioxPeerX25CallParamId.setDescription("The instance of the index object in the\nx25CallParmTable from RFC 1382 for the X.25\ncall parameters used to communicate with the\nremote host.  The well known value {0 0}\nindicates no call parameters specified.")
mioxPeerEnAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 38, 2, 1, 1, 7), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 128)).clone('')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mioxPeerEnAddr.setDescription("The Encapsulation address of the remote\nhost mapped by this table entry.  A length\nof zero indicates the remote IP address is\nunknown or unspecified for use as a PLE\ndefault.\n\nThe first octet of this object contains the\nencapsulation type, the remaining octets\ncontain an address of that type.  Thus for\nan IP address, the length will be five\noctets, the first octet will contain 204\n(hex CC), and the last four octets will\ncontain the IP address.  For a snap\nencapsulation, the first byte would be 128\n(hex 80) and the rest of the octet string\nwould have the snap header.")
mioxPeerX121Address = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 38, 2, 1, 1, 8), X121Address().clone('')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mioxPeerX121Address.setDescription("The X.25 address of the remote host mapped\nby this table entry.  A zero length string\nindicates the X.25 address is unspecified\nfor use as the PLE default.")
mioxPeerX25CircuitId = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 38, 2, 1, 1, 9), InstancePointer()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mioxPeerX25CircuitId.setDescription("This object identifies the instance of the\nindex for the X.25 circuit open to the peer\nmapped by this table entry.  The well known\nvalue {0 0} indicates no connection\ncurrently active.  For multiple connections,\nthis identifies the index of a multiplexing\ntable entry for the connections.  This can\nonly be written to configure use of PVCs\nwhich means the identified circuit table\nentry for a write must be a PVC.")
mioxPeerDescr = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 38, 2, 1, 1, 10), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 255)).clone('')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mioxPeerDescr.setDescription("This object returns any identification\ninformation about the peer.  An agent may\nsupply the comment information found in the\nconfiguration file entry for this peer.  A\nzero length string indicates no information\navailable.")
mioxPeerEncTable = MibTable((1, 3, 6, 1, 2, 1, 10, 38, 2, 2))
if mibBuilder.loadTexts: mioxPeerEncTable.setDescription("This table contains the list of\nencapsulations used to communicate with a\npeer.  This table has two indexes, the first\nidentifies the peer, the second\ndistinguishes encapsulation types.\n\nThe first index identifies the corresponding\nentry in the mioxPeerTable.  The second\nindex gives the priority of the different\nencapsulations.\n\nThe encapsulation types are ordered in\npriority order.  For calling a peer, the\nfirst entry (mioxPeerEncIndex of 1) is tried\nfirst.  If the call doesn't succeed because\nthe remote host clears the call due to\nincompatible call user data, the next entry\nin the list is tried.  Each entry is tried\nuntil the list is exhausted.\n\nFor answering a call, the encapsulation type\nrequested by the peer must be found the list\nor the call will be refused.  If there are\nno entries in this table for a peer, all\ncall requests from the peer will be refused.\n\nObjects in this table can only be set when\nthe mioxPeerStatus object with the same\nindex has a value of underCreation.  When\nthat status object is set to invalid and\ndeleted, the entry in this table with that\npeer index must also be deleted.")
mioxPeerEncEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 38, 2, 2, 1)).setIndexNames((0, "MIOX25-MIB", "mioxPeerIndex"), (0, "MIOX25-MIB", "mioxPeerEncIndex"))
if mibBuilder.loadTexts: mioxPeerEncEntry.setDescription("Per connection information.")
mioxPeerEncIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 38, 2, 2, 1, 1), PositiveInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mioxPeerEncIndex.setDescription("The second index in the table which\ndistinguishes different encapsulation\ntypes.")
mioxPeerEncType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 38, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 256))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mioxPeerEncType.setDescription("The value of the encapsulation type.  For\nIP encapsulation this will have a value of\n204 (hex CC).  For SNAP encapsulated\npackets, this will have a value of 128 (hex\n80).  For CLNP, ISO 8473, this will have a\nvalue of 129 (hex 81).  For ES-ES, ISO 9542,\nthis will have a value of 130 (hex 82).  A\nvalue of 197 (hex C5) identifies the Blacker\nX.25 encapsulation.  A value of 0,\nidentifies the Null encapsulation.\n\nThis value can only be written when the\nmioxPeerStatus object with the same\nmioxPeerIndex has a value of underCreation.\nSetting this object to a value of 256\ndeletes the entry.  When deleting an entry,\nall other entries in the mioxPeerEncTable\nwith the same mioxPeerIndex and with an\nmioxPeerEncIndex higher then the deleted\nentry, will all have their mioxPeerEncIndex\nvalues decremented by one.")

# Augmentions

# Exports

# Objects
mibBuilder.exportSymbols("MIOX25-MIB", miox=miox, mioxPle=mioxPle, mioxPleTable=mioxPleTable, mioxPleEntry=mioxPleEntry, mioxPleMaxCircuits=mioxPleMaxCircuits, mioxPleRefusedConnections=mioxPleRefusedConnections, mioxPleEnAddrToX121LkupFlrs=mioxPleEnAddrToX121LkupFlrs, mioxPleLastFailedEnAddr=mioxPleLastFailedEnAddr, mioxPleEnAddrToX121LkupFlrTime=mioxPleEnAddrToX121LkupFlrTime, mioxPleX121ToEnAddrLkupFlrs=mioxPleX121ToEnAddrLkupFlrs, mioxPleLastFailedX121Address=mioxPleLastFailedX121Address, mioxPleX121ToEnAddrLkupFlrTime=mioxPleX121ToEnAddrLkupFlrTime, mioxPleQbitFailures=mioxPleQbitFailures, mioxPleQbitFailureRemoteAddress=mioxPleQbitFailureRemoteAddress, mioxPleQbitFailureTime=mioxPleQbitFailureTime, mioxPleMinimumOpenTimer=mioxPleMinimumOpenTimer, mioxPleInactivityTimer=mioxPleInactivityTimer, mioxPleHoldDownTimer=mioxPleHoldDownTimer, mioxPleCollisionRetryTimer=mioxPleCollisionRetryTimer, mioxPleDefaultPeerId=mioxPleDefaultPeerId, mioxPeer=mioxPeer, mioxPeerTable=mioxPeerTable, mioxPeerEntry=mioxPeerEntry, mioxPeerIndex=mioxPeerIndex, mioxPeerStatus=mioxPeerStatus, mioxPeerMaxCircuits=mioxPeerMaxCircuits, mioxPeerIfIndex=mioxPeerIfIndex, mioxPeerConnectSeconds=mioxPeerConnectSeconds, mioxPeerX25CallParamId=mioxPeerX25CallParamId, mioxPeerEnAddr=mioxPeerEnAddr, mioxPeerX121Address=mioxPeerX121Address, mioxPeerX25CircuitId=mioxPeerX25CircuitId, mioxPeerDescr=mioxPeerDescr, mioxPeerEncTable=mioxPeerEncTable, mioxPeerEncEntry=mioxPeerEncEntry, mioxPeerEncIndex=mioxPeerEncIndex, mioxPeerEncType=mioxPeerEncType)

