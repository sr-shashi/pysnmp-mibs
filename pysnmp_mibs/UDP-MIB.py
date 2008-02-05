# PySNMP SMI module. Autogenerated from smidump -f python UDP-MIB
# by libsmi2pysnmp-0.0.8-alpha at Tue Feb  5 21:05:23 2008,
# Python version (2, 4, 4, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( InetAddress, InetAddressType, InetPortNumber, ) = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType", "InetPortNumber")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Counter32, Counter64, Integer32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Integer32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "mib-2")

# Objects

udp = MibIdentifier((1, 3, 6, 1, 2, 1, 7))
udpInDatagrams = MibScalar((1, 3, 6, 1, 2, 1, 7, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: udpInDatagrams.setDescription("The total number of UDP datagrams delivered to UDP\nusers.\n\n\n\n\n\nDiscontinuities in the value of this counter can occur\nat re-initialization of the management system, and at\nother times as indicated by discontinuities in the\nvalue of sysUpTime.")
udpNoPorts = MibScalar((1, 3, 6, 1, 2, 1, 7, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: udpNoPorts.setDescription("The total number of received UDP datagrams for which\nthere was no application at the destination port.\n\nDiscontinuities in the value of this counter can occur\nat re-initialization of the management system, and at\nother times as indicated by discontinuities in the\nvalue of sysUpTime.")
udpInErrors = MibScalar((1, 3, 6, 1, 2, 1, 7, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: udpInErrors.setDescription("The number of received UDP datagrams that could not be\ndelivered for reasons other than the lack of an\napplication at the destination port.\n\nDiscontinuities in the value of this counter can occur\nat re-initialization of the management system, and at\nother times as indicated by discontinuities in the\nvalue of sysUpTime.")
udpOutDatagrams = MibScalar((1, 3, 6, 1, 2, 1, 7, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: udpOutDatagrams.setDescription("The total number of UDP datagrams sent from this\nentity.\n\nDiscontinuities in the value of this counter can occur\nat re-initialization of the management system, and at\nother times as indicated by discontinuities in the\nvalue of sysUpTime.")
udpTable = MibTable((1, 3, 6, 1, 2, 1, 7, 5))
if mibBuilder.loadTexts: udpTable.setDescription("A table containing IPv4-specific UDP listener\ninformation.  It contains information about all local\nIPv4 UDP end-points on which an application is\ncurrently accepting datagrams.  This table has been\ndeprecated in favor of the version neutral\nudpEndpointTable.")
udpEntry = MibTableRow((1, 3, 6, 1, 2, 1, 7, 5, 1)).setIndexNames((0, "UDP-MIB", "udpLocalAddress"), (0, "UDP-MIB", "udpLocalPort"))
if mibBuilder.loadTexts: udpEntry.setDescription("Information about a particular current UDP listener.")
udpLocalAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 7, 5, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: udpLocalAddress.setDescription("The local IP address for this UDP listener.  In the\ncase of a UDP listener that is willing to accept\ndatagrams for any IP interface associated with the\nnode, the value 0.0.0.0 is used.")
udpLocalPort = MibTableColumn((1, 3, 6, 1, 2, 1, 7, 5, 1, 2), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: udpLocalPort.setDescription("The local port number for this UDP listener.")
udpEndpointTable = MibTable((1, 3, 6, 1, 2, 1, 7, 7))
if mibBuilder.loadTexts: udpEndpointTable.setDescription("A table containing information about this entity's UDP\nendpoints on which a local application is currently\naccepting or sending datagrams.\n\n\n\n\n\nThe address type in this table represents the address\ntype used for the communication, irrespective of the\nhigher-layer abstraction.  For example, an application\nusing IPv6 'sockets' to communicate via IPv4 between\n::ffff:10.0.0.1 and ::ffff:10.0.0.2 would use\nInetAddressType ipv4(1).\n\nUnlike the udpTable in RFC 2013, this table also allows\nthe representation of an application that completely\nspecifies both local and remote addresses and ports.  A\nlistening application is represented in three possible\nways:\n\n1) An application that is willing to accept both IPv4\n   and IPv6 datagrams is represented by a\n   udpEndpointLocalAddressType of unknown(0) and a\n   udpEndpointLocalAddress of ''h (a zero-length\n   octet-string).\n\n2) An application that is willing to accept only IPv4\n   or only IPv6 datagrams is represented by a\n   udpEndpointLocalAddressType of the appropriate\n   address type and a udpEndpointLocalAddress of\n   '0.0.0.0' or '::' respectively.\n\n3) An application that is listening for datagrams only\n   for a specific IP address but from any remote\n   system is represented by a\n   udpEndpointLocalAddressType of the appropriate\n   address type, with udpEndpointLocalAddress\n   specifying the local address.\n\nIn all cases where the remote is a wildcard, the\nudpEndpointRemoteAddressType is unknown(0), the\nudpEndpointRemoteAddress is ''h (a zero-length\noctet-string), and the udpEndpointRemotePort is 0.\n\nIf the operating system is demultiplexing UDP packets\nby remote address and port, or if the application has\n'connected' the socket specifying a default remote\naddress and port, the udpEndpointRemote* values should\nbe used to reflect this.")
udpEndpointEntry = MibTableRow((1, 3, 6, 1, 2, 1, 7, 7, 1)).setIndexNames((0, "UDP-MIB", "udpEndpointLocalAddressType"), (0, "UDP-MIB", "udpEndpointLocalAddress"), (0, "UDP-MIB", "udpEndpointLocalPort"), (0, "UDP-MIB", "udpEndpointRemoteAddressType"), (0, "UDP-MIB", "udpEndpointRemoteAddress"), (0, "UDP-MIB", "udpEndpointRemotePort"), (0, "UDP-MIB", "udpEndpointInstance"))
if mibBuilder.loadTexts: udpEndpointEntry.setDescription("Information about a particular current UDP endpoint.\n\nImplementers need to be aware that if the total number\nof elements (octets or sub-identifiers) in\nudpEndpointLocalAddress and udpEndpointRemoteAddress\nexceeds 111, then OIDs of column instances in this table\nwill have more than 128 sub-identifiers and cannot be\naccessed using SNMPv1, SNMPv2c, or SNMPv3.")
udpEndpointLocalAddressType = MibTableColumn((1, 3, 6, 1, 2, 1, 7, 7, 1, 1), InetAddressType()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: udpEndpointLocalAddressType.setDescription("The address type of udpEndpointLocalAddress.  Only\nIPv4, IPv4z, IPv6, and IPv6z addresses are expected, or\nunknown(0) if datagrams for all local IP addresses are\naccepted.")
udpEndpointLocalAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 7, 7, 1, 2), InetAddress()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: udpEndpointLocalAddress.setDescription("The local IP address for this UDP endpoint.\n\nThe value of this object can be represented in three\n\n\n\npossible ways, depending on the characteristics of the\nlistening application:\n\n1. For an application that is willing to accept both\n   IPv4 and IPv6 datagrams, the value of this object\n   must be ''h (a zero-length octet-string), with\n   the value of the corresponding instance of the\n   udpEndpointLocalAddressType object being unknown(0).\n\n2. For an application that is willing to accept only IPv4\n   or only IPv6 datagrams, the value of this object\n   must be '0.0.0.0' or '::', respectively, while the\n   corresponding instance of the\n   udpEndpointLocalAddressType object represents the\n   appropriate address type.\n\n3. For an application that is listening for data\n   destined only to a specific IP address, the value\n   of this object is the specific IP address for which\n   this node is receiving packets, with the\n   corresponding instance of the\n   udpEndpointLocalAddressType object representing the\n   appropriate address type.\n\nAs this object is used in the index for the\nudpEndpointTable, implementors of this table should be\ncareful not to create entries that would result in OIDs\nwith more than 128 subidentifiers; else the information\ncannot be accessed using SNMPv1, SNMPv2c, or SNMPv3.")
udpEndpointLocalPort = MibTableColumn((1, 3, 6, 1, 2, 1, 7, 7, 1, 3), InetPortNumber()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: udpEndpointLocalPort.setDescription("The local port number for this UDP endpoint.")
udpEndpointRemoteAddressType = MibTableColumn((1, 3, 6, 1, 2, 1, 7, 7, 1, 4), InetAddressType()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: udpEndpointRemoteAddressType.setDescription("The address type of udpEndpointRemoteAddress.  Only\nIPv4, IPv4z, IPv6, and IPv6z addresses are expected, or\nunknown(0) if datagrams for all remote IP addresses are\naccepted.  Also, note that some combinations of\n\n\n\nudpEndpointLocalAdressType and\nudpEndpointRemoteAddressType are not supported.  In\nparticular, if the value of this object is not\nunknown(0), it is expected to always refer to the\nsame IP version as udpEndpointLocalAddressType.")
udpEndpointRemoteAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 7, 7, 1, 5), InetAddress()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: udpEndpointRemoteAddress.setDescription("The remote IP address for this UDP endpoint.  If\ndatagrams from any remote system are to be accepted,\nthis value is ''h (a zero-length octet-string).\nOtherwise, it has the type described by\nudpEndpointRemoteAddressType and is the address of the\nremote system from which datagrams are to be accepted\n(or to which all datagrams will be sent).\n\nAs this object is used in the index for the\nudpEndpointTable, implementors of this table should be\ncareful not to create entries that would result in OIDs\nwith more than 128 subidentifiers; else the information\ncannot be accessed using SNMPv1, SNMPv2c, or SNMPv3.")
udpEndpointRemotePort = MibTableColumn((1, 3, 6, 1, 2, 1, 7, 7, 1, 6), InetPortNumber()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: udpEndpointRemotePort.setDescription("The remote port number for this UDP endpoint.  If\ndatagrams from any remote system are to be accepted,\nthis value is zero.")
udpEndpointInstance = MibTableColumn((1, 3, 6, 1, 2, 1, 7, 7, 1, 7), Unsigned32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 4294967295L))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: udpEndpointInstance.setDescription("The instance of this tuple.  This object is used to\ndistinguish among multiple processes 'connected' to\nthe same UDP endpoint.  For example, on a system\nimplementing the BSD sockets interface, this would be\nused to support the SO_REUSEADDR and SO_REUSEPORT\nsocket options.")
udpEndpointProcess = MibTableColumn((1, 3, 6, 1, 2, 1, 7, 7, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: udpEndpointProcess.setDescription("The system's process ID for the process associated with\nthis endpoint, or zero if there is no such process.\nThis value is expected to be the same as\nHOST-RESOURCES-MIB::hrSWRunIndex or SYSAPPL-MIB::\nsysApplElmtRunIndex for some row in the appropriate\ntables.")
udpHCInDatagrams = MibScalar((1, 3, 6, 1, 2, 1, 7, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: udpHCInDatagrams.setDescription("The total number of UDP datagrams delivered to UDP\nusers, for devices that can receive more than 1\nmillion UDP datagrams per second.\n\nDiscontinuities in the value of this counter can occur\nat re-initialization of the management system, and at\nother times as indicated by discontinuities in the\nvalue of sysUpTime.")
udpHCOutDatagrams = MibScalar((1, 3, 6, 1, 2, 1, 7, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: udpHCOutDatagrams.setDescription("The total number of UDP datagrams sent from this\nentity, for devices that can transmit more than 1\nmillion UDP datagrams per second.\n\nDiscontinuities in the value of this counter can occur\nat re-initialization of the management system, and at\nother times as indicated by discontinuities in the\nvalue of sysUpTime.")
udpMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 50)).setRevisions(("2005-05-20 00:00","1994-11-01 00:00","1991-03-31 00:00",))
if mibBuilder.loadTexts: udpMIB.setOrganization("IETF IPv6 Working Group\nhttp://www.ietf.org/html.charters/ipv6-charter.html")
if mibBuilder.loadTexts: udpMIB.setContactInfo("Bill Fenner (editor)\n\nAT&T Labs -- Research\n75 Willow Rd.\nMenlo Park, CA 94025\n\nPhone: +1 650 330-7893\nEmail: <fenner@research.att.com>\n\nJohn Flick (editor)\n\nHewlett-Packard Company\n8000 Foothills Blvd. M/S 5557\nRoseville, CA 95747\n\nPhone: +1 916 785 4018\nEmail: <john.flick@hp.com>\n\nSend comments to <ipv6@ietf.org>")
if mibBuilder.loadTexts: udpMIB.setDescription("The MIB module for managing UDP implementations.\nCopyright (C) The Internet Society (2005).  This\nversion of this MIB module is part of RFC 4113;\nsee the RFC itself for full legal notices.")
udpMIBConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 50, 2))
udpMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 50, 2, 1))
udpMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 50, 2, 2))

# Augmentions

# Groups

udpHCGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 50, 2, 2, 3)).setObjects(("UDP-MIB", "udpHCInDatagrams"), ("UDP-MIB", "udpHCOutDatagrams"), )
udpEndpointGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 50, 2, 2, 4)).setObjects(("UDP-MIB", "udpEndpointProcess"), )
udpGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 50, 2, 2, 1)).setObjects(("UDP-MIB", "udpLocalAddress"), ("UDP-MIB", "udpOutDatagrams"), ("UDP-MIB", "udpLocalPort"), ("UDP-MIB", "udpInDatagrams"), ("UDP-MIB", "udpNoPorts"), ("UDP-MIB", "udpInErrors"), )
udpBaseGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 50, 2, 2, 2)).setObjects(("UDP-MIB", "udpOutDatagrams"), ("UDP-MIB", "udpNoPorts"), ("UDP-MIB", "udpInErrors"), ("UDP-MIB", "udpInDatagrams"), )

# Exports

# Module identity
mibBuilder.exportSymbols("UDP-MIB", PYSNMP_MODULE_ID=udpMIB)

# Objects
mibBuilder.exportSymbols("UDP-MIB", udp=udp, udpInDatagrams=udpInDatagrams, udpNoPorts=udpNoPorts, udpInErrors=udpInErrors, udpOutDatagrams=udpOutDatagrams, udpTable=udpTable, udpEntry=udpEntry, udpLocalAddress=udpLocalAddress, udpLocalPort=udpLocalPort, udpEndpointTable=udpEndpointTable, udpEndpointEntry=udpEndpointEntry, udpEndpointLocalAddressType=udpEndpointLocalAddressType, udpEndpointLocalAddress=udpEndpointLocalAddress, udpEndpointLocalPort=udpEndpointLocalPort, udpEndpointRemoteAddressType=udpEndpointRemoteAddressType, udpEndpointRemoteAddress=udpEndpointRemoteAddress, udpEndpointRemotePort=udpEndpointRemotePort, udpEndpointInstance=udpEndpointInstance, udpEndpointProcess=udpEndpointProcess, udpHCInDatagrams=udpHCInDatagrams, udpHCOutDatagrams=udpHCOutDatagrams, udpMIB=udpMIB, udpMIBConformance=udpMIBConformance, udpMIBCompliances=udpMIBCompliances, udpMIBGroups=udpMIBGroups)

# Groups
mibBuilder.exportSymbols("UDP-MIB", udpHCGroup=udpHCGroup, udpEndpointGroup=udpEndpointGroup, udpGroup=udpGroup, udpBaseGroup=udpBaseGroup)
