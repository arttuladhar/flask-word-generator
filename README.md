## Getting Started

#### Create Virtual Env

```
virtualenv venv
```

#### Activate Virtual Env

```
source venv/bin/activate
```

#### Install Requirements

```
pip install -r requirements.txt
```

### Running Application

```
python app.py
```

-----

## Deployment


```
# Build Docker Image
docker build -t flask-word-generator .

# Run Docker Image
docker run flask-word-generator:latest

```