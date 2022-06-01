#Development by Teerapon Meesuk
- Full Stack website landing
- Postgres Database in .env file

# Deploy Landing
### Start Run Landing Page

- Command to Landing Folder

```bash
    cd Landing/
```
- You will see docker-compose.yml this path
```
.
├── Landing 
│   ├── backend
│   ├── docker-compose.yml
│   ├── .env
│   ├── .gitignore
│   └── start-django.sh
└── ...
```
- Command to Landing/ Folder

```bash
    cd Landing/
```
- Command.. Run Docker Compose **First Time
```bash
    docker compose up --build
```
- Command Run docker compose **Next Time

```bash
    docker compose up 
```

### Open new terminal

- Command exec to service
```
    docker compose exec backend bash
```
- Create SuperUser (admin)
```
    python manage.py creatsuperuser
```

### Add data to database 

- Open localhost on browser.
```
    http://localhost:8001
```
