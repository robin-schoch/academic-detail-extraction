from pydantic import BaseModel, Field

class EducationRequirementOutput(BaseModel):
    high_school: str = Field(description="If High School education is sufficient", alias="High School")
    apprenticeship: str = Field(description="If Apprenticeship education is sufficient", alias="Apprenticeship")
    bachelor: str = Field(description="If Bachelor education is sufficient", alias="Bachelor")
    master: str = Field(description="If Master education is sufficient", alias="Master")
    phd: str = Field(description="If PhD education is sufficient", alias="PhD")
