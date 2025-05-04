from pydantic import BaseModel

class ProjectBase(BaseModel):
    name: str
    description: str

class ProjectCreate(ProjectBase):
    pass

class ProjectRead(ProjectBase):
    id: int
    owner_id: int