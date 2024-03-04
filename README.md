# flask-api-starter

This is a Flask API starter serves as a foundation for building new software applications, provides basic structure and functionality to help developer to get started quickly.

## Getting Started

```bash
cp .env.example .env
```

```bash
python -c 'import os; print(os.urandom(8))'
# Update SECRET_KEY= in .env file
```

```bash
pip install -r requirements.txt
```

```bash
$ make
clean                Remove Python file artifacts.
mvenv                Create virtual environment.
install              Install dependencies.
upgrade              Upgrade dependencies.
lint                 Lint project.
pretty               Prettify project.
run                  Run application.
debug                Debug application.
test                 Run tests.
```

```bash
$ make run
* Serving Flask app 'src/app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment.
Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

```bash
curl -X GET localhost:5000

curl -X POST -H "Content-Type: application/json" \
  -d '{"hello": "request"}' localhost:5000/health
```

## Happy Coding

> @cham11ng
