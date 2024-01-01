"""Satellite events."""
from dataclasses import dataclass

from .event import Event, Eventable
from typing import Optional

_RUN_SATELLITE_TYPE = "run-satellite"
_STREAMING_STARTED_TYPE = "streaming-started"
_STREAMING_STOPPED_TYPE = "streaming-stopped"
_VOLUME_SET_TYPE = "set-volume"
_VOLUME_ADJUSTED_TYPE = "volume-adjusted"
_MIC_MUTE_TYPE = "mute-mic"
_MIC_MUTED_TYPE = "mic-muted"


@dataclass
class RunSatellite(Eventable):
    """Tell satellite to start running."""

    @staticmethod
    def is_type(event_type: str) -> bool:
        return event_type == _RUN_SATELLITE_TYPE

    def event(self) -> Event:
        return Event(type=_RUN_SATELLITE_TYPE)

    @staticmethod
    def from_event(event: Event) -> "RunSatellite":
        return RunSatellite()


@dataclass
class StreamingStarted(Eventable):
    """Satellite has started streaming audio to server."""

    @staticmethod
    def is_type(event_type: str) -> bool:
        return event_type == _STREAMING_STARTED_TYPE

    def event(self) -> Event:
        return Event(type=_STREAMING_STARTED_TYPE)

    @staticmethod
    def from_event(event: Event) -> "StreamingStarted":
        return StreamingStarted()


@dataclass
class StreamingStopped(Eventable):
    """Satellite has stopped streaming audio to server."""

    @staticmethod
    def is_type(event_type: str) -> bool:
        return event_type == _STREAMING_STOPPED_TYPE

    def event(self) -> Event:
        return Event(type=_STREAMING_STOPPED_TYPE)

    @staticmethod
    def from_event(event: Event) -> "StreamingStopped":
        return StreamingStopped()

@dataclass
class SetVolume(Eventable):
    """Request to increase/decrease/set absolute volume."""

    volume: Optional[str] = None
    """Volume in percentage, if began with + on - then adjust, otherwise set absolute value, in case of no value - return current volume"""

    @staticmethod
    def is_type(event_type: str) -> bool:
        return event_type == _VOLUME_SET_TYPE

    def event(self) -> Event:
        return Event(
            type=_VOLUME_SET_TYPE,
            data={"volume": self.volume},
        )

    @staticmethod
    def from_event(event: Event) -> "SetVolume":
        return SetVolume(volume=event.data.get("volume"))

@dataclass
class VolumeAdjusted(Eventable):
    """Response to increase/decrease/set absolute volume request."""

    volume: Optional[str] = None
    """Volume in percentage, absolute value"""

    @staticmethod
    def is_type(event_type: str) -> bool:
        return event_type == _VOLUME_ADJUSTED_TYPE

    def event(self) -> Event:
        return Event(
            type=_VOLUME_ADJUSTED_TYPE,
            data={"volume": self.volume},
        )

    @staticmethod
    def from_event(event: Event) -> "VolumeAdjusted":
        return VolumeAdjusted(volume=event.data.get("volume"))

@dataclass
class MuteMic(Eventable):
    """Request to mute mic."""

    mute: Optional[bool] = None
    """Set mic mute value, in case of no value - toggle"""

    @staticmethod
    def is_type(event_type: str) -> bool:
        return event_type == _MIC_MUTE_TYPE

    def event(self) -> Event:
        return Event(
            type=_MIC_MUTE_TYPE,
            data={"mute": self.mute},
        )

    @staticmethod
    def from_event(event: Event) -> "MuteMic":
        return MuteMic(mute=event.data.get("mute"))

@dataclass
class MicMuted(Eventable):
    """Response for mute mic request."""

    mute: Optional[bool] = None
    """Current mic mute status"""

    @staticmethod
    def is_type(event_type: str) -> bool:
        return event_type == _MIC_MUTED_TYPE

    def event(self) -> Event:
        return Event(
            type=_MIC_MUTED_TYPE,
            data={"mute": self.mute},
        )

    @staticmethod
    def from_event(event: Event) -> "MicMuted":
        return MicMuted(mute=event.data.get("mute"))
