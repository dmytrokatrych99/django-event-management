
# Django Event Management API

This project provides a RESTful API for managing events, user registrations, and authentication using JWT.

---

## Project Setup with Docker

### 1️⃣ **Prerequisites**
- [Docker](https://docs.docker.com/get-docker/) (v20+ recommended)
- [Docker Compose](https://docs.docker.com/compose/install/)

---

### **2. Environment Configuration**

1. **Create `.env` file** in the project root:

```ini
# Django settings
SECRET_KEY=your_secret_key_here


# PostgreSQL database settings
POSTGRES_DB=event_db
POSTGRES_USER=event_user
POSTGRES_PASSWORD=event_pass
DB_HOST=db
DB_PORT=5432
```

---

### **3. Docker Setup**

1. **Build Docker images:**

```bash
docker-compose build
```

2. **Start Docker containers:**

```bash
docker-compose up -d
```

---

**4. Access Application**
---

## **API Endpoints**

- **API Root:** [http://localhost:8000/api/](http://localhost:8000/api/)
- **Swagger Docs:** [http://localhost:8000/swagger/](http://localhost:8000/swagger/)  
- **Redoc Docs:** [http://localhost:8000/redoc/](http://localhost:8000/redoc/)


## **Basic User Credentials**

- **Username:** `admin`  
- **Password:** `adminpass`

---

## **Authentication for Swagger**

To authenticate in Swagger:
1. Obtain a token from `/api/token/` endpoint.
2. Go to **Authorize** in Swagger.
3. Use the token in the format:

```
Bearer <your_token_here>
```

---

##   **Postman Setup for Automatic Token**

To automatically generate a valid token before each request in Postman:

1. **Set up Pre-request Script:**  
   In Postman's **Pre-request Script** tab, paste the following:

```javascript
pm.sendRequest({
    url: "http://127.0.0.1:8000/api/token/",
    method: "POST",
    header: {
        "Content-Type": "application/json"
    },
    body: {
        mode: "raw",
        raw: JSON.stringify({
            "username": "admin",
            "password": "adminpass"
        })
    }
}, function (err, res) {
    if (!err && res.code === 200) {
        let token = res.json().access;
        pm.environment.set("auth_token", token);
    } else {
        console.log("Failed to get token:", err);
    }
});
```

2. **Set Authorization in Request:**  
   In Postman's **Authorization** tab:
   - Choose **Bearer Token**.
   - Set the token value as:

```
{{auth_token}}
```

---
Now, each request will automatically fetch a valid token before execution.


---

### **5. Manage Docker**

**Stop Containers:**

```bash
docker-compose down
```

**Check Logs:**

```bash
docker-compose logs -f
```

---

## **6. App Features**

1.  **Authentication:** User registration and JWT-based login.  
2.  **Events:** CRUD operations for events.  
3.  **Email:** Notifications for user and event registration.  
4.  **Filtering:** Search and filter events.  
5.  **API Docs:** Swagger. Redoc

