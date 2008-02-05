# PySNMP SMI module. Autogenerated from smidump -f python PPP-LCP-MIB
# by libsmi2pysnmp-0.0.8-alpha at Tue Feb  5 21:05:17 2008,
# Python version (2, 4, 4, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( ifIndex, transmission, ) = mibBuilder.importSymbols("RFC1213-MIB", "ifIndex", "transmission")
( Bits, Counter32, Integer32, Integer32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Integer32", "Integer32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")

# Objects

ppp = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 23))
pppLcp = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 23, 1))
pppLink = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 23, 1, 1))
pppLinkStatusTable = MibTable((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1))
if mibBuilder.loadTexts: pppLinkStatusTable.setDescription("A table containing PPP-link specific variables\nfor this PPP implementation.")
pppLinkStatusEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1)).setIndexNames((0, "RFC1213-MIB", "ifIndex"))
if mibBuilder.loadTexts: pppLinkStatusEntry.setDescription("Management information about a particular PPP\nLink.")
pppLinkStatusPhysicalIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 2147483647L))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pppLinkStatusPhysicalIndex.setDescription("The value of ifIndex that identifies the\nlower-level interface over which this PPP Link\nis operating. This interface would usually be\nan HDLC or RS-232 type of interface. If there\nis no lower-layer interface element, or there\nis no ifEntry for the element, or the element\ncan not be identified, then the value of this\nobject is 0.  For example, suppose that PPP is\noperating over a serial port. This would use\ntwo entries in the ifTable. The PPP could be\nrunning over `interface' number 123 and the\nserial port could be running over `interface'\nnumber 987.  Therefore, ifSpecific.123 would\ncontain the OBJECT IDENTIFIER ppp\npppLinkStatusPhysicalIndex.123 would contain\n987, and ifSpecific.987 would contain the\nOBJECT IDENTIFIER for the serial-port's media-\nspecific MIB.")
pppLinkStatusBadAddresses = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pppLinkStatusBadAddresses.setDescription("The number of packets received with an\nincorrect Address Field. This counter is a\ncomponent of the ifInErrors variable that is\nassociated with the interface that represents\nthis PPP Link.")
pppLinkStatusBadControls = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pppLinkStatusBadControls.setDescription("The number of packets received on this link\nwith an incorrect Control Field. This counter\nis a component of the ifInErrors variable that\nis associated with the interface that\nrepresents this PPP Link.")
pppLinkStatusPacketTooLongs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pppLinkStatusPacketTooLongs.setDescription("The number of received packets that have been\ndiscarded because their length exceeded the\nMRU. This counter is a component of the\nifInErrors variable that is associated with the\ninterface that represents this PPP Link. NOTE,\npackets which are longer than the MRU but which\nare successfully received and processed are NOT\nincluded in this count.")
pppLinkStatusBadFCSs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pppLinkStatusBadFCSs.setDescription("The number of received packets that have been\ndiscarded due to having an incorrect FCS. This\ncounter is a component of the ifInErrors\nvariable that is associated with the interface\nthat represents this PPP Link.")
pppLinkStatusLocalMRU = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 2147483647L))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pppLinkStatusLocalMRU.setDescription("The current value of the MRU for the local PPP\nEntity. This value is the MRU that the remote\nentity is using when sending packets to the\nlocal PPP entity. The value of this object is\nmeaningful only when the link has reached the\nopen state (ifOperStatus is up).")
pppLinkStatusRemoteMRU = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 2147483647L))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pppLinkStatusRemoteMRU.setDescription("The current value of the MRU for the remote\nPPP Entity. This value is the MRU that the\nlocal entity is using when sending packets to\nthe remote PPP entity. The value of this object\nis meaningful only when the link has reached\nthe open state (ifOperStatus is up).")
pppLinkStatusLocalToPeerACCMap = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 8), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readonly")
if mibBuilder.loadTexts: pppLinkStatusLocalToPeerACCMap.setDescription("The current value of the ACC Map used for\nsending packets from the local PPP entity to\nthe remote PPP entity. The value of this object\nis meaningful only when the link has reached\nthe open state (ifOperStatus is up).")
pppLinkStatusPeerToLocalACCMap = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 9), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readonly")
if mibBuilder.loadTexts: pppLinkStatusPeerToLocalACCMap.setDescription("The ACC Map used by the remote PPP entity when\ntransmitting packets to the local PPP entity.\nThe value of this object is meaningful only\nwhen the link has reached the open state\n(ifOperStatus is up).")
pppLinkStatusLocalToRemoteProtocolCompression = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 10), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("enabled", 1), ("disabled", 2), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pppLinkStatusLocalToRemoteProtocolCompression.setDescription("Indicates whether the local PPP entity will\nuse Protocol Compression when transmitting\npackets to the remote PPP entity. The value of\nthis object is meaningful only when the link\nhas reached the open state (ifOperStatus is\nup).")
pppLinkStatusRemoteToLocalProtocolCompression = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 11), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("enabled", 1), ("disabled", 2), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pppLinkStatusRemoteToLocalProtocolCompression.setDescription("Indicates whether the remote PPP entity will\nuse Protocol Compression when transmitting\npackets to the local PPP entity. The value of\nthis object is meaningful only when the link\nhas reached the open state (ifOperStatus is\nup).")
pppLinkStatusLocalToRemoteACCompression = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 12), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("enabled", 1), ("disabled", 2), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pppLinkStatusLocalToRemoteACCompression.setDescription("Indicates whether the local PPP entity will\nuse Address and Control Compression when\ntransmitting packets to the remote PPP entity.\nThe value of this object is meaningful only\nwhen the link has reached the open state\n(ifOperStatus is up).")
pppLinkStatusRemoteToLocalACCompression = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 13), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("enabled", 1), ("disabled", 2), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pppLinkStatusRemoteToLocalACCompression.setDescription("Indicates whether the remote PPP entity will\nuse Address and Control Compression when\ntransmitting packets to the local PPP entity.\nThe value of this object is meaningful only\nwhen the link has reached the open state\n(ifOperStatus is up).")
pppLinkStatusTransmitFcsSize = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 14), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pppLinkStatusTransmitFcsSize.setDescription("The size of the Frame Check Sequence (FCS) in\nbits that the local node will generate when\nsending packets to the remote node. The value\nof this object is meaningful only when the link\nhas reached the open state (ifOperStatus is\nup).")
pppLinkStatusReceiveFcsSize = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 15), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pppLinkStatusReceiveFcsSize.setDescription("The size of the Frame Check Sequence (FCS) in\nbits that the remote node will generate when\nsending packets to the local node. The value of\nthis object is meaningful only when the link\nhas reached the open state (ifOperStatus is\nup).")
pppLinkConfigTable = MibTable((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 2))
if mibBuilder.loadTexts: pppLinkConfigTable.setDescription("A table containing the LCP configuration\nparameters for this PPP Link. These variables\nrepresent the initial configuration of the PPP\nLink. The actual values of the parameters may\nbe changed when the link is brought up via the\nLCP options negotiation mechanism.")
pppLinkConfigEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 2, 1)).setIndexNames((0, "RFC1213-MIB", "ifIndex"))
if mibBuilder.loadTexts: pppLinkConfigEntry.setDescription("Configuration information about a particular\nPPP Link.")
pppLinkConfigInitialMRU = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 2147483647L)).clone(1500)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pppLinkConfigInitialMRU.setDescription("The initial Maximum Receive Unit (MRU) that\nthe local PPP entity will advertise to the\nremote entity. If the value of this variable is\n0 then the local PPP entity will not advertise\nany MRU to the remote entity and the default\nMRU will be assumed. Changing this object will\nhave effect when the link is next restarted.")
pppLinkConfigReceiveACCMap = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 2, 1, 2), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(4, 4)).setFixedLength(4).clone('\xff\xff\xff\xff')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pppLinkConfigReceiveACCMap.setDescription("The Asynchronous-Control-Character-Map (ACC)\nthat the local PPP entity requires for use on\nits receive side. In effect, this is the ACC\nMap that is required in order to ensure that\nthe local modem will successfully receive all\ncharacters. The actual ACC map used on the\nreceive side of the link will be a combination\nof the local node's pppLinkConfigReceiveACCMap\nand the remote node's\npppLinkConfigTransmitACCMap. Changing this\nobject will have effect when the link is next\nrestarted.")
pppLinkConfigTransmitACCMap = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 2, 1, 3), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(4, 4)).setFixedLength(4).clone('\xff\xff\xff\xff')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pppLinkConfigTransmitACCMap.setDescription("The Asynchronous-Control-Character-Map (ACC)\nthat the local PPP entity requires for use on\nits transmit side. In effect, this is the ACC\nMap that is required in order to ensure that\nall characters can be successfully transmitted\nthrough the local modem.  The actual ACC map\nused on the transmit side of the link will be a\ncombination of the local node's\npppLinkConfigTransmitACCMap and the remote\nnode's pppLinkConfigReceiveACCMap. Changing\nthis object will have effect when the link is\nnext restarted.")
pppLinkConfigMagicNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 2, 1, 4), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("false", 1), ("true", 2), )).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pppLinkConfigMagicNumber.setDescription("If true(2) then the local node will attempt to\nperform Magic Number negotiation with the\nremote node. If false(1) then this negotiation\nis not performed. In any event, the local node\nwill comply with any magic number negotiations\nattempted by the remote node, per the PPP\nspecification. Changing this object will have\neffect when the link is next restarted.")
pppLinkConfigFcsSize = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 128)).clone(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pppLinkConfigFcsSize.setDescription("The size of the FCS, in bits, the local node\nwill attempt to negotiate for use with the\nremote node. Regardless of the value of this\nobject, the local node will comply with any FCS\nsize negotiations initiated by the remote node,\nper the PPP specification. Changing this object\nwill have effect when the link is next\nrestarted.")
pppLqr = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 23, 1, 2))
pppLqrTable = MibTable((1, 3, 6, 1, 2, 1, 10, 23, 1, 2, 1))
if mibBuilder.loadTexts: pppLqrTable.setDescription("Table containing the LQR parameters and\nstatistics for the local PPP entity.")
pppLqrEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 23, 1, 2, 1, 1)).setIndexNames((0, "RFC1213-MIB", "ifIndex"))
if mibBuilder.loadTexts: pppLqrEntry.setDescription("LQR information for a particular PPP link. A\nPPP link will have an entry in this table if\nand only if LQR Quality Monitoring has been\nsuccessfully negotiated for said link.")
pppLqrQuality = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 2, 1, 1, 1), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,3,)).subtype(namedValues=namedval.NamedValues(("good", 1), ("bad", 2), ("not-determined", 3), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pppLqrQuality.setDescription("The current quality of the link as declared by\nthe local PPP entity's Link-Quality Management\nmodules. No effort is made to define good or\nbad, nor the policy used to determine it. The\nnot-determined value indicates that the entity\ndoes not actually evaluate the link's quality.\nThis value is used to disambiguate the\n`determined to be good' case from the `no\ndetermination made and presumed to be good'\ncase.")
pppLqrInGoodOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 2, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pppLqrInGoodOctets.setDescription("The LQR InGoodOctets counter for this link.")
pppLqrLocalPeriod = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 2147483647L))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pppLqrLocalPeriod.setDescription("The LQR reporting period, in hundredths of a\nsecond that is in effect for the local PPP\nentity.")
pppLqrRemotePeriod = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 2147483647L))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pppLqrRemotePeriod.setDescription("The LQR reporting period, in hundredths of a\nsecond, that is in effect for the remote PPP\nentity.")
pppLqrOutLQRs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 2, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pppLqrOutLQRs.setDescription("The value of the OutLQRs counter on the local\nnode for the link identified by ifIndex.")
pppLqrInLQRs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 2, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pppLqrInLQRs.setDescription("The value of the InLQRs counter on the local\nnode for the link identified by ifIndex.")
pppLqrConfigTable = MibTable((1, 3, 6, 1, 2, 1, 10, 23, 1, 2, 2))
if mibBuilder.loadTexts: pppLqrConfigTable.setDescription("Table containing the LQR Configuration\nparameters for the local PPP entity.")
pppLqrConfigEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 23, 1, 2, 2, 1)).setIndexNames((0, "RFC1213-MIB", "ifIndex"))
if mibBuilder.loadTexts: pppLqrConfigEntry.setDescription("LQR configuration information for a particular\nPPP link.")
pppLqrConfigPeriod = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 2147483647L)).clone(0)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pppLqrConfigPeriod.setDescription("The LQR Reporting Period that the local PPP\nentity will attempt to negotiate with the\nremote entity, in units of hundredths of a\nsecond. Changing this object will have effect\nwhen the link is next restarted.")
pppLqrConfigStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 2, 2, 1, 2), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,2,)).subtype(namedValues=namedval.NamedValues(("disabled", 1), ("enabled", 2), )).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pppLqrConfigStatus.setDescription("If enabled(2) then the local node will attempt\nto perform LQR negotiation with the remote\nnode. If disabled(1) then this negotiation is\nnot performed. In any event, the local node\nwill comply with any magic number negotiations\nattempted by the remote node, per the PPP\nspecification. Changing this object will have\neffect when the link is next restarted.\nSetting this object to the value disabled(1)\nhas the effect of invalidating the\ncorresponding entry in the pppLqrConfigTable\nobject. It is an implementation-specific matter\nas to whether the agent removes an invalidated\nentry from the table. Accordingly, management\nstations must be prepared to receive tabular\ninformation from agents that corresponds to\nentries not currently in use.")
pppLqrExtnsTable = MibTable((1, 3, 6, 1, 2, 1, 10, 23, 1, 2, 3))
if mibBuilder.loadTexts: pppLqrExtnsTable.setDescription("Table containing additional LQR information\nfor the local PPP entity.")
pppLqrExtnsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 23, 1, 2, 3, 1)).setIndexNames((0, "RFC1213-MIB", "ifIndex"))
if mibBuilder.loadTexts: pppLqrExtnsEntry.setDescription("Extended LQR information for a particular PPP\nlink. Assuming that this group has been\nimplemented, a PPP link will have an entry in\nthis table if and only if LQR Quality\nMonitoring has been successfully negotiated for\nsaid link.")
pppLqrExtnsLastReceivedLqrPacket = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 2, 3, 1, 1), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(68, 68)).setFixedLength(68)).setMaxAccess("readonly")
if mibBuilder.loadTexts: pppLqrExtnsLastReceivedLqrPacket.setDescription("This object contains the most recently\nreceived LQR packet.  The format of the packet\nis as described in the LQM Protocol\nspecificiation. All fields of the packet,\nincluding the `save' fields, are stored in this\nobject.\n\nThe LQR packet is stored in network byte order.\nThe LAP-B and PPP headers are not stored in\nthis object; the first four octets of this\nvariable contain the Magic-Number field, the\nsecond four octets contain the LastOutLQRs\nfield and so on. The last four octets of this\nobject contain the SaveInOctets field of the\nLQR packet.")
pppTests = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 23, 1, 3))
pppEchoTest = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 23, 1, 3, 1))
pppDiscardTest = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 23, 1, 3, 2))

# Augmentions

# Exports

# Objects
mibBuilder.exportSymbols("PPP-LCP-MIB", ppp=ppp, pppLcp=pppLcp, pppLink=pppLink, pppLinkStatusTable=pppLinkStatusTable, pppLinkStatusEntry=pppLinkStatusEntry, pppLinkStatusPhysicalIndex=pppLinkStatusPhysicalIndex, pppLinkStatusBadAddresses=pppLinkStatusBadAddresses, pppLinkStatusBadControls=pppLinkStatusBadControls, pppLinkStatusPacketTooLongs=pppLinkStatusPacketTooLongs, pppLinkStatusBadFCSs=pppLinkStatusBadFCSs, pppLinkStatusLocalMRU=pppLinkStatusLocalMRU, pppLinkStatusRemoteMRU=pppLinkStatusRemoteMRU, pppLinkStatusLocalToPeerACCMap=pppLinkStatusLocalToPeerACCMap, pppLinkStatusPeerToLocalACCMap=pppLinkStatusPeerToLocalACCMap, pppLinkStatusLocalToRemoteProtocolCompression=pppLinkStatusLocalToRemoteProtocolCompression, pppLinkStatusRemoteToLocalProtocolCompression=pppLinkStatusRemoteToLocalProtocolCompression, pppLinkStatusLocalToRemoteACCompression=pppLinkStatusLocalToRemoteACCompression, pppLinkStatusRemoteToLocalACCompression=pppLinkStatusRemoteToLocalACCompression, pppLinkStatusTransmitFcsSize=pppLinkStatusTransmitFcsSize, pppLinkStatusReceiveFcsSize=pppLinkStatusReceiveFcsSize, pppLinkConfigTable=pppLinkConfigTable, pppLinkConfigEntry=pppLinkConfigEntry, pppLinkConfigInitialMRU=pppLinkConfigInitialMRU, pppLinkConfigReceiveACCMap=pppLinkConfigReceiveACCMap, pppLinkConfigTransmitACCMap=pppLinkConfigTransmitACCMap, pppLinkConfigMagicNumber=pppLinkConfigMagicNumber, pppLinkConfigFcsSize=pppLinkConfigFcsSize, pppLqr=pppLqr, pppLqrTable=pppLqrTable, pppLqrEntry=pppLqrEntry, pppLqrQuality=pppLqrQuality, pppLqrInGoodOctets=pppLqrInGoodOctets, pppLqrLocalPeriod=pppLqrLocalPeriod, pppLqrRemotePeriod=pppLqrRemotePeriod, pppLqrOutLQRs=pppLqrOutLQRs, pppLqrInLQRs=pppLqrInLQRs, pppLqrConfigTable=pppLqrConfigTable, pppLqrConfigEntry=pppLqrConfigEntry, pppLqrConfigPeriod=pppLqrConfigPeriod, pppLqrConfigStatus=pppLqrConfigStatus, pppLqrExtnsTable=pppLqrExtnsTable, pppLqrExtnsEntry=pppLqrExtnsEntry, pppLqrExtnsLastReceivedLqrPacket=pppLqrExtnsLastReceivedLqrPacket, pppTests=pppTests, pppEchoTest=pppEchoTest, pppDiscardTest=pppDiscardTest)

