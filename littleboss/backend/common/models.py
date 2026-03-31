# backend/common/models.py

from dataclasses import dataclass, field, asdict
from typing import Optional, List, Dict, Any


@dataclass
class Deadline:
    date: str
    description: str
    urgency: str = "normal"

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class ChecklistItem:
    name: str
    description: str = ""
    completed: bool = False
    due_date: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class CalendarEvent:
    title: str
    date: str
    time: str = "23:59"
    description: str = ""
    location: str = ""
    google_event_id: str = ""
    status: str = "created"

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class AnalysisResult:
    document_type: str = ""
    summary: str = ""
    deadlines: List[Deadline] = field(default_factory=list)
    checklist_items: List[ChecklistItem] = field(default_factory=list)
    calendar_events: List[CalendarEvent] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "document_type": self.document_type,
            "summary": self.summary,
            "deadlines": [deadline.to_dict() for deadline in self.deadlines],
            "checklist_items": [item.to_dict() for item in self.checklist_items],
            "calendar_events": [event.to_dict() for event in self.calendar_events],
        }


@dataclass
class Document:
    doc_id: str
    user_id: str
    original_file_name: str
    s3_key: str
    status: str
    mime_type: str = ""
    raw_text: str = ""
    analysis_result: Optional[Dict[str, Any]] = None
    error_message: str = ""
    created_at: str = ""
    updated_at: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class User:
    user_id: str
    email: str
    calendar_access_token: str = ""
    calendar_refresh_token: str = ""
    token_expiry: str = ""
    created_at: str = ""
    updated_at: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)