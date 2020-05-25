#!/usr/bin/env python3

# Description: Perform a DNS zone transfer
# Usage: dns-axfr.py domain nameserver

import dns.query
import dns.zone
import sys

if len(sys.argv) < 3:
    print("Usage: dns-axfr.py domain nameserver")
    sys.exit(1)

z = dns.zone.from_xfr(dns.query.xfr(sys.argv[2], sys.argv[1]))
for n in z.nodes.keys():
    print(z[n].to_text(n))
