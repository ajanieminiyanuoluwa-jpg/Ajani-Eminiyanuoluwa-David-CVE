Ajani Eminiyanuoluwa David RUN/CYB/23/15379 CYB 401
CVE-2026-96951 (Windows Shell Command Injection)
Description: Improper neutralisation of special elements used in a command ('command injection') in Windows Shell allows an unauthorised attacker to bypass a security feature over a network.
Severity: CVSS 8.8, rated Important by Microsoft. CWE-77 (command injection). Actively exploited zero-day, added to CISA KEV on Oct 13, 2026, with a federal fix deadline of Oct 16.
What it does: A crafted file sent by email, chat or a malicious download evades Mark of the Web protections, so Windows doesn’t warn the user before it runs.
Affected: Windows 10, Windows 11 (23H2 to 26H1), Windows Server 2012 R2 to 2025, and Visual Studio 2026 18.10.
Patch: The October 2026 Patch Tuesday cumulative update, published Oct 13. Example fixed builds: Win 11 24H2 at 10.0.26100.9711 and Win 10 22H2 at 10.0.19044.7807. I couldn’t confirm the exact KB numbers, so check the MSRC or NVD page for CVE-2026-96951.
Kill chain:
Delivery: Phishing email, chat message or malicious website.
Exploitation: The user opens the file, MOTW is bypassed, and no warning appears.
Post-exploitation: Payload execution, persistence and C2 (my inference, typical for MOTW bypasses).
Expert response: Tenable’s Satnam Narang noted it is the third exploited Windows Shell flaw this year, and it is unclear whether it is linked to APT28 or is another incomplete fix. Experts urge triaging by exploitability, so patch this first. Also block risky attachments, hunt for suspicious child processes spawned from Explorer, and warn users about unexpected files.                                                          
