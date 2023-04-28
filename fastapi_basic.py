from fastapi import FastAPI, status, Response
from pydantic import BaseModel
import uvicorn
import logging
from pathlib import Path
from dotenv import load_dotenv

logging.basicConfig(level=logging.DEBUG)
# logging.disable()    # uncomment this for deployment or change aboce to CRITICAL or ERROR
logger = logging.getLogger(__name__)

try:  # for testing
    env_path = Path('.') / '.env'
    load_dotenv(dotenv_path=env_path)
except KeyError:  # for deployment implement env variables
    pass

app = FastAPI()

"""class used to provide input to the post method"""


class BasicInput(BaseModel):
    firstname: str
    lastname: str
    age: int
    email: str


"""Post method, gets input from basicInput and returns whatever is programmed to do. Sets status either 202 or 400"""


@app.post("/get_user_info")
async def get_user_info(userinput: BasicInput, response: Response):

    if "@" not in userinput.email:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"error": f'{userinput.email} is not a proper mail format.'}
    else:
        response.status_code = status.HTTP_202_ACCEPTED
        return {"full_name": userinput.firstname + " " + userinput.lastname, "email": userinput.email}


"""get method, does not expect any input, but returns whatever is programmed to do. Sets status 202"""


@app.get("/get_message")
async def get_message(response: Response):
    response.status_code = status.HTTP_202_ACCEPTED
    return {"message": "This is the message you were waiting for."}


if __name__ == '__main__':
    uvicorn.run('fastapi_basic:app', port=8080, reload=True)
