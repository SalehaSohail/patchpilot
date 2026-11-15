#fastapi is being used here so that external systems(github) can communicate with the python application or code  we are developing right now through http request as in fastapi we can use decorators to create route that handle incoming request and execute corresponding python function 
from fastapi import FastAPI,APIRouter
#pydantic is used to validate data and BaseModel is a cass we can inherit to define what data types do we need 
from pydantic import BaseModel
class WebhookPayload(BaseModel):
    commit_id:str
    repo_id:int

    
app=FastAPI(title="Autonomus code fixing agent")
#The purpose of the API router is to organize the endpoints if we have too many endpoints we can organize every endpoint inti seaprate files also (so that our main.py dont become messy)
v1_router=APIRouter(prefix="/api/v1")
#In faaapi decorators are used to create routes
@v1_router.get("/health")
#it suggest that when a get request is called on health endpoint , execute the below function
def health():
    return {"status":"OK"}

@v1_router.post("/webhook")
def webhook(payload:WebhookPayload):
    return {"status":"ok"}

#we have created api but how do browser access it so we need a server(uvicorn) which runs fastapi application 
#so server(uvicorn) will recieve request on port 8000
app.include_router(v1_router)
if __name__=="__main__": #we are using this to make sure that server only starts when we run main.py directly not when it is imported in another file
    import uvicorn
    uvicorn.run("main:app",app_dir="src",port=8000,reload=True)