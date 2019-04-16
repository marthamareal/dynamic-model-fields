# Dynamic Model Fields

[![Build Status](https://travis-ci.com/marthamareal/dynamic-model-fields.svg?branch=develop)](https://travis-ci.com/marthamareal/dynamic-model-fields)
[![Coverage Status](https://coveralls.io/repos/github/marthamareal/dynamic-model-fields/badge.svg?branch=develop)](https://coveralls.io/github/marthamareal/dynamic-model-fields?branch=develop)

This project enables insurers to create risk types with custom fields of different types, For example Name, Address, Age, and so on. It is built using Python/Django and hosted using heroku. Check the hotsed app [here](https://dynamic-modal-fields.herokuapp.com/api/v1/).

#### Solution approach
In order to enable insurers add their custom fields with relevant field type when creating a risk type, This project creates three models `FieldType`, `Field` and `RiskType`. The `Field` model relates to the `FieldType` and `RiskType` with a `Many-To-Many` relationship. The available views enable a user to create risk types with a list of fields and the fields must refer to a field-type. A field type has a name and options if it's of select type.

Example of post data when creating a risk type:

POST `api/v1/risk-type/`:
```
{
	"name": "Prize Policy",
	"description": "This is my description feild which can not be empty",
	"fields": [{
		"name": "first name",
		"field_type": "6611f2ca-3569-4f54-a50a-f9be73cdd3ab" # FieldType Id
	},
	{
		"name": "Age",
		"field_type": "4511f2ca-3569-4f54-a50a-f9be73cdd3a9" # FieldType Id
	}
	]	
}
```

#### Setup

Clone the repository with:

```
$ git clone https://github.com/marthamareal/dynamic-model-fields.git
$ cd dynamic-model-fields
```

Create and activate a virtual enviroment with:
```
$ virtualenv -p python3 venv
$ source venv/bin/activate
```
Rename the `.env.sample` file to `.env` and modify the variables with your credentials.
Source the variables with
```
$ source .env
```

Install dependencies with:
```
$ pip install -r requirements.txt
```

Apply migrations and run the server:
```
$ python manage.py migrate
$ python manage.py loaddevelopmentdata
$ python manage.py runserver
```
#### Tests

To test the app:
```
$ python manage.py test
```
with coverage:
```
$ coverage run --source='.' ./manage.py test
```

The following are the activities that can be performed in the application.
```
- Create a Risk type
- List Risk types
- Retieve a single Risk type
- Update and delete a Risk type
- List Field types
```
