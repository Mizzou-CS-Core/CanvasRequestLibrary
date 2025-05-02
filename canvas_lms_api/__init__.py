import logging

from .client import CanvasClient
from .models.group import Group
from .models.person import Person
from .models.assignment import Assignment
from .models.submission import Submission
from .models.course import Course, Calendar, BlueprintRestrictions

logger = logging.getLogger(__name__)

# Module‐level storage
_client: CanvasClient | None = None


def init(url_base: str, token: str) -> None:
    """
    Call once at startup with your Canvas base URL and API token.
    Subsequent calls are no-ops (or you can warn if different creds are passed).
    """
    global _client
    if _client is not None:
        # optional: warn if url_base/token differ
        logger.debug("CanvasClient already initialized; skipping.")
        return

    logger.debug(f"Initializing CanvasClient for {url_base!r}")
    _client = CanvasClient(url_base=url_base, token=token)
    logger.info("CanvasClient ready")


def get_client() -> CanvasClient:
    """
    Returns the one and only CanvasClient. Raises if init() was never called.
    """
    if _client is None:
        raise RuntimeError("CanvasClient not initialized!  Call canvas_lms_api.init() first.")
    return _client


__all__ = [
    "CanvasClient",
    "Group",
    "Person",
    "Assignment",
    "Submission",
    "Course",
    "Calendar",
    "BlueprintRestrictions",
    "get_client"
]
