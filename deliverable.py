"""
doomsday-network/bounty-guard: Fake GitHub Bounty Repo Reporter & DOOM Quickstart

This module provides:
1. A function to report a fake GitHub bounty repository by validating the repo URL and
   generating a report payload.
2. A 3-second DOOM Quickstart simulation function.

Constraints:
- Pure Python, no external dependencies.
- Secure: No use of subprocess, ctypes, socket, sys.exit, os.system, or eval.

Author: [Your Name]
"""

import re
import time
from typing import Dict, Optional


def is_valid_github_repo_url(url: str) -> bool:
    """
    Validates if the provided URL is a valid GitHub repository URL.

    Args:
        url (str): The GitHub repository URL to validate.

    Returns:
        bool: True if valid, False otherwise.
    """
    pattern = r"^https://github\.com/[\w\-]+/[\w\-]+/?$"
    return bool(re.match(pattern, url))


def report_fake_bounty_repo(
    repo_url: str,
    reporter: str,
    reason: Optional[str] = None
) -> Dict[str, str]:
    """
    Reports a fake GitHub bounty repository.

    Args:
        repo_url (str): The URL of the suspicious GitHub repository.
        reporter (str): The username or identifier of the reporter.
        reason (Optional[str]): Optional reason for the report.

    Returns:
        Dict[str, str]: A dictionary containing the report details.

    Raises:
        ValueError: If the repo_url is not a valid GitHub repository URL.
    """
    if not is_valid_github_repo_url(repo_url):
        raise ValueError("Invalid GitHub repository URL.")

    report = {
        "repo_url": repo_url,
        "reporter": reporter,
        "reason": reason or "Suspected fake bounty repository.",
        "status": "pending_review"
    }
    # In a real implementation, this would submit to a backend or database.
    # Here, we simply return the report payload.
    return report


def doom_quickstart(seconds: int = 3) -> None:
    """
    Simulates the 3-second DOOM Quickstart.

    Args:
        seconds (int): Number of seconds to simulate the quickstart. Default is 3.

    Returns:
        None
    """
    print("Starting DOOM Quickstart...")
    for i in range(seconds, 0, -1):
        print(f"DOOM Quickstart in {i}...")
        time.sleep(1)
    print("DOOM Quickstart complete! You're ready to guard bounties.")


# Example usage (for demonstration; remove or comment out in production)
if __name__ == "__main__":
    # Simulate reporting a fake repo
    try:
        report = report_fake_bounty_repo(
            repo_url="https://github.com/fakeuser/fakerepo",
            reporter="bounty_hunter_007",
            reason="Impersonating a legitimate bounty project."
        )
        print("Report submitted:", report)
    except ValueError as e:
        print("Error:", e)

    # Run the DOOM Quickstart
    doom_quickstart(3)