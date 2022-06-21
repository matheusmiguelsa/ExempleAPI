Clients API

- Clients API is a way to request a new budget of your project in Example
- All the data will be posted as a public API in https://api-client-sa.herokuapp.com/api/clients/

How to use it (Online Example)

- To GET this as API you need to use the endpoint: https://api-client-sa.herokuapp.com/api/clients/?format=api 
To GET this as json you need to use the endpoint: https://api-client-sa.herokuapp.com/api/clients/?format=json
- To POST in this API you might login and fill the form in http://api-client-sa.herokuapp.com/
- It is impossible to DELETE what was posted.
- You can also PATCH what was posted filling the form in the endpoint https://api-client-sa.herokuapp.com/api/clients/

How to use if (In your localhost)
- To GET this as API you need to use the endpoint http://localhost:8000/api/clients/?format=api
To GET this API as json format you need to use the endpoint: http://localhost:8000/api/clients/?format=json
- To POST in this API you might login and fill the form in http://localhost:8000/
- It is impossible to DELETE what was posted.
- You can also PATCH in what was posted by filling in the form in the endpoint http://localhost:8000/api/clients/

How to run this

Type the code below in your terminal

git clone https://github.com/matheusmiguelsa/ExempleAPI.git

After clone this repository, you might install the virtual machine(venv) and the libs before run this:

In Linux:
1. python3 -m venv venv
2. source venv/bin/activate
3. pip install -r requirements.txt
4. python manage.py migrate
5. python manage.py makemigrations
6. python manage.py runserver

So, access in your favorite browser: https://localhost:8000

In Windows:
1. python -m venv venv
2. cd venv/Scripts && activate
3. cd .. && cd ..
4. pip install -r requirements.txt
5. python manage.py migrate
6. python manage.py makemigrations
7. python manage.py runserver

So, access in your favorite browser: https://localhost:8000