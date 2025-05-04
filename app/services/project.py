from sqlmodel import Session

from app.db.models import Project
from app.schemas.project import ProjectCreate

def create_project(db: Session, project: ProjectCreate, owner_id: int):
    db_project = Project(**project.dict(), owner_id=owner_id)
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

def get_projects(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Project).offset(skip).limit(limit).all()

def get_project(db: Session, project_id: int):
    return db.query(Project).filter(Project.id == project_id).first()

def update_project(db: Session, project_id: int, project_data: dict):
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        return None
    for key, value in project_data.items():
        setattr(project, key, value)
    db.commit()
    db.refresh(project)
    return project

def delete_project(db: Session, project_id: int):
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        return None
    db.delete(project)
    db.commit()
    return project