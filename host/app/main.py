from fastapi import FastAPI
from app.schemas.prompt import PromptRequest, PromptResponse
from app.utils.host import MCPHost

app = FastAPI()

@app.post("/")
async def promt_recive( request: PromptRequest) -> PromptResponse :
    if __name__ == "__main__":
        host = MCPHost()
        host.run()
    return