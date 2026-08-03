# BGP Troubleshooting Runbook

Version: 1.0

When a BGP neighbor is not Established, first verify the peer address, local and remote AS numbers, reachability to the neighbor, and the state of the interface or routed path used to reach the peer.

If the neighbor is Idle and receiving zero prefixes, do not assume the BGP policy is the root cause. Check transport reachability and interface state before moving to policy review.

Record the observed neighbor state, peer address, prefix count, interface evidence, and any recent change information used during the investigation.

This runbook is guidance only. It does not authorize configuration changes or session resets.
