from dataclasses import dataclass, field
from datetime import datetime

from db import mapper_registry, Base
from sqlalchemy import Column, Integer, DateTime, String, JSON


@mapper_registry.mapped
@dataclass
class Pokemon(Base):
    id: int = field(metadata={"sa": Column(Integer, primary_key=True)})
    name: str = field(metadata={"sa": Column(String)})
    abilities: str = field(metadata={"sa": Column(JSON)})
    weight: int = field(metadata={"sa": Column(Integer)})
    location_area_encounters: str = field(metadata={"sa": Column(String)})
    captured: datetime = field(default=datetime.utcnow(), metadata={"sa": Column(DateTime(timezone=True))})
