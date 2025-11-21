"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional, Literal

# Example schemas (replace with your own):

class User(BaseModel):
    """
    Users collection schema
    Collection name: "user" (lowercase of class name)
    """
    name: str = Field(..., description="Full name")
    email: str = Field(..., description="Email address")
    address: str = Field(..., description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")

class Product(BaseModel):
    """
    Products collection schema
    Collection name: "product" (lowercase of class name)
    """
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in dollars")
    category: str = Field(..., description="Product category")
    in_stock: bool = Field(True, description="Whether product is in stock")

# Video editing agency lead/inquiry schema
class Inquiry(BaseModel):
    """
    Inquiries from the website contact form
    Collection name: "inquiry"
    """
    name: str = Field(..., min_length=2, max_length=100, description="Numele complet")
    email: EmailStr = Field(..., description="Adresa de email")
    service: Literal[
        "Editare YouTube",
        "Reels/TikTok",
        "Ads/Promo",
        "Evenimente",
        "Corporate",
        "Altceva"
    ] = Field(..., description="Tipul de serviciu dorit")
    budget: Optional[str] = Field(None, description="Interval de buget orientativ")
    message: str = Field(..., min_length=10, max_length=2000, description="Detalii proiect")
    source: Optional[str] = Field("website", description="Sursa lead-ului")
    status: Optional[Literal["new", "contacted", "won", "lost"]] = Field("new", description="Status lead")

# Add your own schemas here:
# --------------------------------------------------

# Note: The Flames database viewer will automatically:
# 1. Read these schemas from GET /schema endpoint
# 2. Use them for document validation when creating/editing
# 3. Handle all database operations (CRUD) directly
# 4. You don't need to create any database endpoints!
