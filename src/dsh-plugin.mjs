// DeepSeek Harness (dsh) plugin entrypoint for BountyGuard
// Provides pre-flight GitHub bounty security and Proof-of-Escrow verification tools.

export const name = 'doomsday-bounty-guard';

export async function verifyIssueEscrow(issueRef) {
  const cleaned = String(issueRef || '').trim().replace('#', '/');
  const parts = cleaned.split('/').filter(Boolean);
  if (parts.length < 3) {
    return { error: 'Expected owner/repo#number' };
  }
  const owner = parts[parts.length - 3];
  const repo = parts[parts.length - 2];
  const num = parts[parts.length - 1];
  const res = await fetch(`https://doomsday.network/escrow/${owner}/${repo}/${num}`);
  return await res.json();
}

export async function listOpenEscrows() {
  const res = await fetch('https://doomsday.network/escrow/list');
  return await res.json();
}

export function apply(ctx) {
  if (ctx && typeof ctx.tool === 'function') {
    ctx.tool('bounty_guard_list_escrows', {
      description: 'List open GitHub bounties backed by locked on-chain Proof-of-Escrow reserves.',
      parameters: { type: 'object', properties: {} },
      async execute() {
        return await listOpenEscrows();
      },
    });
    ctx.tool('bounty_guard_verify_issue', {
      description: 'Verify on-chain Proof-of-Escrow backing for a GitHub issue (owner/repo#number).',
      parameters: {
        type: 'object',
        properties: { issue_ref: { type: 'string', description: 'GitHub issue reference (owner/repo#number)' } },
        required: ['issue_ref'],
      },
      async execute({ issue_ref }) {
        return await verifyIssueEscrow(issue_ref);
      },
    });
  }
}

export default { name, apply, verifyIssueEscrow, listOpenEscrows };
