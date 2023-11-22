AuthCon
=======

AuthCon is a RESTful API Python connector to OpenAM.

    :copyright:     (c) 2014 by Alvaro Soto
    :license:       GPL v2, see LICENSE for more details.
    :contact info:  https://headup.ws / alsotoes@gmail.com


Functionality implemented so far.
=======
- Authenticate an user
- Validate token
- Logout token


Code in process
=======
- Get user information = be able to fetch user internal information
- User in group = be able to validate if an user is part of a group


Setting the environment
=======
- Install Virtual Environments ( http://docs.python-guide.org/en/latest/dev/virtualenvs/ )
- Create the venv and activate ( )
- Install the requeriments ( pip install -r requirements.txt )
- Execute $ python authcon.py ( by default the service starts on 0.0.0.0:5000 )


Let's see how it works
=======

* Authenticate an user:

	- Correct login data:

	Query:

		$ curl -k -X 'POST' http://0.0.0.0:5000/v1.0/tokens -d '{"auth":{"passwordCredentials":{"username": "alvaro", "password":"1qaz2wsx3edc"} }}' -H 'Content-type: application/json'

	Response: < HTTP/1.0 200 OK

		{
		  "access": {
			"token": {
			  "id": "AQIC5wM2LY4SfcwxawY2IQsFzwzVLN3m1Ub92IFmsN7zO9g.*AAJTSQACMDEAAlNLABMtMjc4MDc4NTI5NzcwNDc1NDEw*"
			}
		  }
		}

	- Incorrect login data:

	Query:

		$ curl -k -X 'POST' http://0.0.0.0:5000/v1.0/tokens -d '{"auth":{"passwordCredentials":{"username": "alvaro", "password":"1234567890"} }}' -H 'Content-type: application/json'

	Response: < HTTP/1.0 401 UNAUTHORIZED

		{
		  "message": "Unauthorized."
		}

	- Bad request: 

	Query:

		$ curl -k -X 'POST' http://0.0.0.0:5000/v1.0/tokens -d '{"auth":{"passwordCredentials":{"}}}' -H 'Content-type: application/json'

	Response: < HTTP/1.0 400 BAD REQUEST

		{
		  "message": "The request cannot be fulfilled due to bad syntax."
		}

* Validate token:

	- Token OK:

	Query: 

		$ curl -k -X 'GET' http://0.0.0.0:5000/v1.0/tokens/AQIC5wM2LY4SfcwxawY2IQsFzwzVLN3m1Ub92IFmsN7zO9g.*AAJTSQACMDEAAlNLABMtMjc4MDc4NTI5NzcwNDc1NDEw

	Response: < HTTP/1.0 200 OK

		{}

	- Token FAIL:

	Query:

		$ curl -k -X 'GET' http://0.0.0.0:5000/v1.0/tokens/AQIC5wM2LY4SfcxT_B7s4OzCcGb1LcgORTCCIAPTuoqBsFw.*AAJTSQACMDEAAlNLABQtOTEzMzk1NjM0NDU5ODMxNDg5OQ..*

	Response: < HTTP/1.0 203 NON AUTHORITATIVE INFORMATION

		{}

* Logout token:

	- Token OK:

	Query:

		$ curl -k -X 'DELETE' http://0.0.0.0:5000/v1.0/tokens/AQIC5wM2LY4SfcxT_B7s4OzCcGb1LcgORTCCIAPTuoqBsFw.*AAJTSQACMDEAAlNLABQtOTEzMzk1NjM0NDU5ODMxNDg5OQ..*

	Response: < HTTP/1.0 200 OK

		{}

	- Token FAIL:

	Query: 

		$ curl -k -X 'DELETE' http://0.0.0.0:5000/v1.0/tokens/AQIC5wM2LY4SfcxT_B7s4OzCcGb1LcgORTCCIAPTuoqBsFw
		
	Response: < HTTP/1.0 202 ACCEPTED

		{}
