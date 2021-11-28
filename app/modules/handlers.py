from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse
from app.modules.forms import UserLoginForm, ResponseUserLogin, ResponsePredict, RequestDiaParams
from loguru import logger
import pandas as pd

import pickle

logger.add('debug.log', format="{time} {level} {message}", level="DEBUG", rotation="1 weeks", compression='zip')

router = APIRouter()

router.modelRandomForest = pickle.load(open("app/modules/train/model_rf.pkl", "rb"))
router.modelLog = pickle.load(open("app/modules/train/model_log.pkl", "rb"))


@router.get('/status')
def index():
    return {'status': 'OK'}


@router.post('/login', response_model=ResponseUserLogin, name='user:login')
def index(user_form: UserLoginForm = Body(..., embed=True)):
    return ResponseUserLogin(name=user_form.email)


@router.post("/predict/RandomForest", response_model=ResponsePredict, name='predict:RandomForest')
def predict_RF(features: RequestDiaParams):
    logger.info('Run /predict/RandomForest')
    try:
        test_data = get_testData(features)
        predict = router.modelRandomForest.predict(test_data)[0]
        predict_proba = max(router.modelRandomForest.predict_proba(test_data)[0])

        return ResponsePredict(predict=predict, probability=predict_proba)
    except Exception as e:
        logger.exception(str(e))
        return JSONResponse(status_code=500, content={'message': str(e)})


@router.post("/predict/LogisticRegression", response_model=ResponsePredict, name='predict:LogisticRegression')
def predict_LR(features: RequestDiaParams):
    logger.info('Run /predict/LogisticRegression')
    try:
        test_data = get_testData(features)
        predict = router.modelLog.predict(test_data)[0]
        predict_proba = max(router.modelLog.predict_proba(test_data)[0])

        return ResponsePredict(probability=predict_proba, predict=predict)

    except Exception as e:
        logger.exception(str(e))
        return JSONResponse(status_code=500, content={'message': str(e)})


def get_testData(features):
    features_names = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
                      'BMI', 'DiabetesPedigreeFunction', 'Age']
    features_values = [features.Pregnancies,
                       features.Glucose,
                       features.BloodPressure,
                       features.SkinThickness,
                       features.Insulin,
                       features.BMI,
                       features.DiabetesPedigreeFunction,
                       features.Age]
    return pd.DataFrame({k: [v] for k, v in zip(features_names, features_values)})
