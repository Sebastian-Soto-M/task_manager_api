from datetime import datetime
from typing import Any, Callable, Dict, Optional

from pydantic import BaseModel, validator

date_to_str: Callable[[datetime], str] = lambda v: v.strftime(
    '%Y-%m-%dT%H:%M:%S.%fZ')


class TaskModel(BaseModel):
    id: int
    project_id: int
    section_id: int = 0
    title: str
    description: Optional[str]
    creation_date: datetime = datetime.utcnow()
    completion_date: Optional[datetime]
    due_date: Optional[datetime]
    priority: int = 0
    archived = False

    class Config:
        json_encoders: Dict[type, Any] = {
            datetime: date_to_str
        }

    @validator('priority', pre=True)
    def priority_validate(cls, v: Any) -> int:
        return int(v.split(' ')[1]) if isinstance(v, str) else v

    # @validator('creation_date', 'due_date', pre=True)
    # def due_date_validate(cls, v):
    #     # June 2, 2021 at 08:32PM
    #     return datetime.strptime(v, '%B %m, %Y')

    # @validator('completion_date', pre=True)
    # def completed_at_validate(cls, v):
    #     # June 2, 2021 at 08:32PM
    #     return datetime.strptime(v, '%B %m, %Y at %I:%M%p')
