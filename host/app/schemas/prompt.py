from pydantic import BaseModel

class PromptResponse(BaseModel):
    response : str
    
    
class PromptRequest(BaseModel):
    db : bool = False
    file : bool = False
    monitor : bool = False
    prompt : str