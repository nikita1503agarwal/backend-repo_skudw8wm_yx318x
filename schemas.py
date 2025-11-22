from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class Lead(BaseModel):
    """
    Leads collection schema
    Collection name: "lead" (lowercase of class name)
    """
    first_name: str = Field(..., description="Customer first name")
    last_name: str = Field(..., description="Customer last name")
    email: EmailStr = Field(..., description="Email address")
    phone: str = Field(..., description="Phone number")
    service: str = Field(..., description="Requested service type")
    message: Optional[str] = Field(None, description="Additional details from customer")
    zip_code: Optional[str] = Field(None, description="Service area ZIP code")
