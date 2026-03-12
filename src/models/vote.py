from dataclasses import dataclass

@dataclass
class Vote:
    vote_id: str
    poll_id: int
    position_id: int
    candidate_id: int | None
    voter_id: int
    station_id: int
    timestamp: str
    abstained: bool
