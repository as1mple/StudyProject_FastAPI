from pydantic import BaseModel


class UserLoginForm(BaseModel):
    email: str
    password: str


class ResponseUserLogin(BaseModel):
    name: str


class RequestDiaParams(BaseModel):
    Pregnancies: int
    Glucose: int
    BloodPressure: int
    SkinThickness: int
    Insulin: int
    BMI: int
    DiabetesPedigreeFunction: int
    Age: int


class ResponsePredict(BaseModel):
    probability: float
    predict: int
