from fastapi import APIRouter, Body
from app.modules.forms import UserLoginForm, ResponseUserLogin

router = APIRouter()


@router.get('/status')
def index():
    return {'status': 'OK'}


@router.post('/login', response_model=ResponseUserLogin, name='user:login')
def index(user_form: UserLoginForm = Body(..., embed=True)):
    return ResponseUserLogin(name=user_form.email)
