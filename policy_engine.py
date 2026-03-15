import yaml
from pydantic import BaseModel, Field
from typing import List

class ProvenanceConfig(BaseModel):
    require_execution_id_binding: bool
    max_token_age_seconds: int

class FirewallPolicy(BaseModel):
    version: str
    enforcement_mode: str = Field(pattern="^(blocking|monitoring)$")
    provenance_layer: ProvenanceConfig
    # ... (Raj and Anuroop's configs nested here)

def load_policy(filepath: str) -> FirewallPolicy:
    """Dynamically loads and strictly validates the YAML via Pydantic."""
    with open(filepath, 'r') as f:
        data = yaml.safe_load(f)
    policy = FirewallPolicy(**data)
    print(f"[*] Loaded Policy Version: {policy.version}")
    return policy