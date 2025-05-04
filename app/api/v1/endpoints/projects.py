from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from app.db.models import Role, User
from app.db.session import get_db
from app.schemas.project import ProjectCreate, ProjectRead
from app.services.auth import get_current_active_user
from app.services.project import create_project, delete_project, get_projects, update_project

router = APIRouter()

@router.get("/", response_model=List[ProjectRead])
def read_projects(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
):
    return get_projects(db, skip=skip, limit=limit)

@router.post("/", response_model=ProjectRead)
def create_new_project(
    project: ProjectCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
):
    if current_user.role != Role.ADMIN:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only admin users can create projects",
        )
    return create_project(db=db, project=project, owner_id=current_user.id)

@router.put("/{project_id}", response_model=ProjectRead)
def update_existing_project(
    project_id: int,
    project: ProjectCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
):
    if current_user.role != Role.ADMIN:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only admin users can update projects",
        )
    db_project = update_project(db=db, project_id=project_id, project_data=project.dict())
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return db_project

@router.delete("/{project_id}")
def delete_existing_project(
    project_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
):
    if current_user.role != Role.ADMIN:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only admin users can delete projects",
        )
    db_project = delete_project(db=db, project_id=project_id)
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return {"message": "Project deleted successfully"}