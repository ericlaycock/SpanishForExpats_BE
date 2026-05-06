"""Generate iCalendar (.ics) payloads for cohort confirmations.

VCALENDAR is plain text, so we hand-roll it to avoid pulling in a new
dependency. Each cohort produces one VCALENDAR with three VEVENTs (one
per session). UIDs are token-derived so re-importing the same .ics
updates the same calendar entries instead of duplicating them.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Iterable


@dataclass
class IcsEvent:
    uid: str
    start_utc: datetime
    end_utc: datetime
    summary: str
    description: str
    location: str


def _fmt(dt: datetime) -> str:
    # iCalendar UTC format: 20260507T170000Z
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def _escape(s: str) -> str:
    # RFC 5545: backslash, semicolon, comma, newline must be escaped in TEXT props.
    return (
        s.replace("\\", "\\\\")
        .replace(";", "\\;")
        .replace(",", "\\,")
        .replace("\r\n", "\\n")
        .replace("\n", "\\n")
    )


def build_calendar(events: Iterable[IcsEvent]) -> str:
    now_stamp = _fmt(datetime.now(timezone.utc))
    lines: list[str] = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//Spanish for Expats//Cohort//EN",
        "CALSCALE:GREGORIAN",
        "METHOD:PUBLISH",
    ]
    for ev in events:
        lines.extend(
            [
                "BEGIN:VEVENT",
                f"UID:{ev.uid}",
                f"DTSTAMP:{now_stamp}",
                f"DTSTART:{_fmt(ev.start_utc)}",
                f"DTEND:{_fmt(ev.end_utc)}",
                f"SUMMARY:{_escape(ev.summary)}",
                f"DESCRIPTION:{_escape(ev.description)}",
                f"LOCATION:{_escape(ev.location)}",
                "END:VEVENT",
            ]
        )
    lines.append("END:VCALENDAR")
    # RFC 5545 requires CRLF line endings.
    return "\r\n".join(lines) + "\r\n"
