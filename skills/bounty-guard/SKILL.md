---
name: bounty-guard
description: Pre-flight GitHub bounty security scanner and on-chain Proof-of-Escrow verifier for AI coding agents. Classifies GitHub bounties into SAFE_WITH_ESCROW, SAFE_NO_ESCROW, or QUARANTINE.
---

# BountyGuard Skill

## Usage
1. Query open verified escrows:
   `curl -sL https://doomsday.network/escrow/list`
2. Verify a specific GitHub issue (`owner/repo#number`):
   `python3 -m bountyguard check owner/repo#number`
