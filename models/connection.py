from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from .base_model import BaseModel 

class Connection(BaseModel):
    __tablename__ = "connection"
    
    id = Column(Integer, primary_key=True)
    robot_id = Column(Integer, ForeignKey("robot.id"))

    token = Column(String,nullable=True)
    ip = Column(String,nullable=True)

    update_date = Column(DateTime,nullable=True)
    created_date = Column(DateTime, default=datetime.utcnow)

    robot = relationship("Robot", back_populates="connection")
