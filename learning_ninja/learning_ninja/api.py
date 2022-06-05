from ninja import NinjaAPI, Schema, Path
import datetime

api = NinjaAPI()


@api.get('/hello')
def hello(request):
    return 'Hello!'


@api.get('/items/{int:some_id}')
def pass_parameter(request, some_id: int):
    return {'some_id': some_id}


@api.get('/items/{str:some_id}')
def pass_parameter(request, some_id: str):
    return {'some_id': some_id}


@api.get('/bmi/{name}/{weight}/{height}')
def many_arguments(request, name: str, weight: float, height: float):
    bmi = round(weight/height**2, 2)
    message = f'{name}, your BMI is {bmi}.'
    response = {
        'message': message,
        'data': [name, weight, height]
    }
    return response


class PathDate(Schema):
    year: int
    month: int
    day: int

    def value(self):
        return datetime.date(self.year, self.month, self.day)


@api.get('/events/{year}/{month}/{day}/')
def events(request, date: PathDate = Path(...)):
    return {'date': date.value()}
