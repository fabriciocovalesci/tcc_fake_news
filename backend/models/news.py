from pydantic import BaseModel, validator

class News(BaseModel):
    author: str
    date: str
    domain: str
    status: str
    text: str
    title: str
    url: str
    
    
class Domain(BaseModel):
    domain: str
    
    @validator("domain")
    def validate_domain(value):
        domains = {
            "uol": "https://www.uol.com.br/",
            "portalr7": "https://www.portalbr7.com/"
        }
        return domains.get(value)