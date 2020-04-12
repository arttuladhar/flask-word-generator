## Getting Started

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Running Application

```bash
python app.py
```

-----

## Deployment


```bash
# Build Docker Image
docker build -t flask-word-generator .

# Run Docker Image
docker run flask-word-generator:latest
```
