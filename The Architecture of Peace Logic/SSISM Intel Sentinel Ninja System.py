#!/usr/bin/env python3
"""
SSISM Intel Sentinel Ninja System
TAIE-78 / SSISM-PEACE-LOGIC-02
The Mathematics of Life-Saving
2026-10-04

Research prototype for peace-oriented analytical reasoning.

IMPORTANT:
This is a conceptual model, NOT a validated predictor of war or casualties.
It requires empirical indicators, parameter calibration, historical data, and
out-of-sample validation before predictive claims are made.

Core doctrine:
Reality Before Narrative.
Intelligence Before Reaction.
Samadhi Before Escalation.
Panna Before Judgment.
Metta Before Conflict.

Pipeline:
SIGNAL -> VERIFY -> PAUSE -> UNDERSTAND -> DE-ESCALATE -> PRESERVE LIFE
"""

from dataclasses import dataclass, asdict
from enum import Enum
import hashlib
import json
import math
from typing import Optional


ENGINE_NAME = "SSISM Intel Sentinel Ninja System"
ENGINE_VERSION = "0.1.0"
MODULE_CODE = "TAIE-78 / SSISM-PEACE-LOGIC-02"
DATE = "2026-10-04"


class EvidenceState(str, Enum):
    OBSERVED = "OBSERVED"
    CALCULATED = "CALCULATED"
    SOURCED = "SOURCED"
    INFERRED = "INFERRED"
    UNKNOWN = "UNKNOWN"


class VerificationStatus(str, Enum):
    VERIFIED = "VERIFIED"
    SUPPORTED = "SUPPORTED"
    PLAUSIBLE = "PLAUSIBLE"
    UNCONFIRMED = "UNCONFIRMED"
    CONTRADICTED = "CONTRADICTED"
    UNKNOWN = "UNKNOWN"


@dataclass
class PeaceInputs:
    """All normalized inputs must be in [0,1]."""
    dosa: float
    metta: float
    temporal_pressure: float
    uncertainty: float
    harm_potential: float
    information_velocity: float
    immediate_safety_need: float = 0.0


@dataclass
class PeaceAssessment:
    conflict_index: float
    risk_band: str
    recommended_pause_hours: float
    action_mode: str
    scientific_status: str


def clamp01(x: float) -> float:
    return max(0.0, min(1.0, float(x)))


def _validate_inputs(x: PeaceInputs) -> None:
    for name, value in asdict(x).items():
        if not 0.0 <= value <= 1.0:
            raise ValueError(f"{name} must be between 0 and 1")


def logistic(x: float) -> float:
    if x >= 0:
        e = math.exp(-x)
        return 1.0 / (1.0 + e)
    e = math.exp(x)
    return e / (1.0 + e)


def conflict_index(
    x: PeaceInputs,
    k: float = 5.0,
    alpha: float = 1.0,
) -> float:
    """
    Conceptual SSISM logistic index:

    Z = sigmoid(k * (Dosa - Metta + alpha*TemporalPressure))

    This is an INDEX, not a validated probability until calibrated.
    """
    _validate_inputs(x)
    raw = k * (x.dosa - x.metta + alpha * x.temporal_pressure)
    return logistic(raw)


def adaptive_pause_hours(x: PeaceInputs) -> float:
    """
    Replaces a universal 24-hour rule with an adaptive verification window.

    More uncertainty, harm potential and information velocity increase
    the pause. Immediate safety need reduces the delay.
    """
    _validate_inputs(x)
    hours = (
        2.0
        + 18.0 * x.uncertainty
        + 12.0 * x.harm_potential
        + 10.0 * x.information_velocity
        - 18.0 * x.immediate_safety_need
    )
    return max(0.0, min(48.0, hours))


def assess_peace(x: PeaceInputs) -> PeaceAssessment:
    z = conflict_index(x)
    pause = adaptive_pause_hours(x)

    if z >= 0.80:
        band = "HIGH_ESCALATION_SIGNAL"
        mode = "PAUSE_VERIFY_DEESCALATE"
    elif z >= 0.60:
        band = "ELEVATED_ESCALATION_SIGNAL"
        mode = "VERIFY_BEFORE_REACTION"
    elif z >= 0.40:
        band = "INTERMEDIATE_SIGNAL"
        mode = "CONTINUE_VERIFICATION"
    else:
        band = "LOWER_ESCALATION_SIGNAL"
        mode = "MONITOR_AND_VERIFY"

    return PeaceAssessment(
        conflict_index=round(z, 6),
        risk_band=band,
        recommended_pause_hours=round(pause, 2),
        action_mode=mode,
        scientific_status=(
            "CONCEPTUAL RESEARCH PROTOTYPE; "
            "empirical calibration required before predictive use"
        ),
    )


def life_preservation_constraint(
    finite_objective: bool = True,
    irreversible_harm: bool = True,
) -> str:
    """
    Normative rule inspired by TAIE-78.

    Human life is deliberately NOT assigned a monetary or 'infinite'
    numerical price. Avoidable irreversible harm is treated as a
    decision constraint requiring human review.
    """
    if finite_objective and irreversible_harm:
        return "FINITE_OBJECTIVE_MUST_NOT_JUSTIFY_AVOIDABLE_IRREVERSIBLE_HARM"
    return "HUMAN_LIFE_PRESERVATION_REVIEW_REQUIRED"


def comparative_life_review(
    finite_objective_value: float,
    lives_at_risk: int,
) -> dict:
    """Ethical review only; never calculates a price for human life."""
    if finite_objective_value < 0 or lives_at_risk < 0:
        raise ValueError("Inputs must be non-negative")

    return {
        "finite_objective_value": finite_objective_value,
        "lives_at_risk": lives_at_risk,
        "human_life_price": "NOT_CALCULATED",
        "constraint": life_preservation_constraint(),
        "status": "HUMAN_REVIEW_REQUIRED",
    }


def root_error_discipline(root_error_present: bool) -> dict:
    if root_error_present:
        return {
            "root": "E0_ERROR_PRESENT",
            "downstream": "DECISIONS_AT_RISK",
            "action": "STOP_PROPAGATION_AND_VERIFY_E0",
        }
    return {
        "root": "NO_ROOT_ERROR_IDENTIFIED",
        "downstream": "CONTINUE_CORROBORATION",
        "action": "VERIFY_BEFORE_JUDGMENT",
    }


def canonical_sha256(data) -> str:
    raw = json.dumps(
        data, ensure_ascii=False, sort_keys=True,
        separators=(",", ":")
    ).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def file_sha256(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def self_test() -> dict:
    x = PeaceInputs(
        dosa=0.85,
        metta=0.20,
        temporal_pressure=0.60,
        uncertainty=0.75,
        harm_potential=0.90,
        information_velocity=0.80,
        immediate_safety_need=0.10,
    )

    result = assess_peace(x)

    assert 0.0 <= result.conflict_index <= 1.0
    assert 0.0 <= result.recommended_pause_hours <= 48.0
    assert result.action_mode == "PAUSE_VERIFY_DEESCALATE"
    assert root_error_discipline(True)["action"] == "STOP_PROPAGATION_AND_VERIFY_E0"
    assert comparative_life_review(100.0, 5)["human_life_price"] == "NOT_CALCULATED"

    return {
        "status": "PASS",
        "engine": ENGINE_NAME,
        "version": ENGINE_VERSION,
        "module": MODULE_CODE,
        "conflict_index": result.conflict_index,
        "pause_hours": result.recommended_pause_hours,
        "risk_band": result.risk_band,
    }


def demo() -> dict:
    x = PeaceInputs(
        dosa=0.70,
        metta=0.35,
        temporal_pressure=0.45,
        uncertainty=0.65,
        harm_potential=0.80,
        information_velocity=0.75,
        immediate_safety_need=0.05,
    )
    return {
        "engine": ENGINE_NAME,
        "module": MODULE_CODE,
        "date": DATE,
        "pipeline": [
            "SIGNAL", "VERIFY", "PAUSE",
            "UNDERSTAND", "DE-ESCALATE", "PRESERVE LIFE"
        ],
        "assessment": asdict(assess_peace(x)),
        "root_error": root_error_discipline(True),
        "life_review": comparative_life_review(100.0, 3),
        "note": "Demonstration only; not a real-world conflict forecast.",
    }


if __name__ == "__main__":
    print("=" * 72)
    print(ENGINE_NAME)
    print(MODULE_CODE)
    print("=" * 72)
    print(json.dumps(self_test(), indent=2))
    print("\nDEMO")
    print(json.dumps(demo(), indent=2))
    print("\nFILE SHA-256")
    print(file_sha256(__file__))
