from fastapi import APIRouter, BackgroundTasks, UploadFile, File, Form
from starlette.responses import JSONResponse
from starlette.requests import Request
from fastapi_mail import FastMail, MessageSchema,ConnectionConfig
from pydantic import BaseModel, EmailStr
from typing import List


class EmailSchema(BaseModel):
    email: List[EmailStr]




conf = ConnectionConfig(
    MAIL_USERNAME = "Harman singh",
    MAIL_PASSWORD = "rajharman",
    MAIL_FROM = "itsofficialharman@gmail.com",
    MAIL_PORT = 587,
    MAIL_SERVER = "itsofficialharman@gmail.com",
    MAIL_TLS = True,
    MAIL_SSL = False,
    USE_CREDENTIALS = True,
    VALIDATE_CERTS = True
)

router = APIRouter()


async def simple_send(email ,token, username) -> JSONResponse:

    message = MessageSchema(
        subject="Fastapi-Mail module",
        recipients=email.dict().get("email"),  # List of recipients, as many as you can pass 
        body=html,
        subtype=f"""\
<html>
  <head>
    <title>Document</title>
  </head>
  <body>
    <div id="box">
      <h2>Hallo ,{username}</h2> 
        <p> Bevor du die Seite nutzen kannst, klicke 
            <a href="http://localhost:8000/verify/{token}">
                hier
            </a> um deine registrierung zu bestätigen
        </p>
      </form>
    </div>
  </body>
</html>
<style>
  #box {{
    margin: 0 auto;
    max-width: 500px;
    border: 1px solid black;
    height: 200px;
    text-align: center;
    background: lightgray;
  }}
  p {{
    padding: 10px 10px;
    font-size: 18px;
  }}
  .inline {{
    display: inline;
  }}
  .link-button {{
    background: none;
    border: none;
    color: blue;
    font-size: 22px;
    text-decoration: underline;
    cursor: pointer;
    font-family: serif;
  }}
  .link-button:focus {{
    outline: none;
  }}
  .link-button:active {{
    color: red;
  }}
</style>
    """
        )

    fm = FastMail(conf)
    await fm.send_message(message)
    return JSONResponse(status_code=200, content={"message": "email has been sent"})  


