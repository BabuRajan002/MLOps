# HTTP Methods and Headers

## **HTTP Methods**

HTTP methods define the type of action to be performed on a resource in a web server.

| **Method** | **Purpose** | **Simple Definition** |
|-------------|--------------|------------------------|
| **GET** | Retrieve data from the server. | Used to **fetch or read** information (no data modification). |
| **POST** | Create a new resource on the server. | Used to **send or submit** data, such as form inputs or JSON payloads. |
| **PUT** | Update or replace an existing resource. | Used to **completely update** an existing record with new data. |
| **PATCH** | Partially update an existing resource. | Used to **modify only specific fields** of a resource. |
| **DELETE** | Remove a resource from the server. | Used to **delete** existing data or entries. |
| **HEAD** | Retrieve metadata about a resource. | Similar to GET but **returns only headers**, not the response body. |
| **OPTIONS** | Describe the communication options for a resource. | Used to **check which HTTP methods** are allowed on a server or endpoint. |

---

## **HTTP Headers**

Headers are **metadata** sent along with requests and responses in the form of **key–value pairs**.  
They help the client and server exchange additional information like content type, authentication, and caching rules.

### **Common HTTP Headers**
1. **Content-Type** – Specifies the **format of the data** being sent (e.g., `application/json`, `text/html`).
2. **Authorization** – Contains credentials (like tokens or API keys) used for **authentication**.
3. **User-Agent** – Identifies the **client software** (browser, app, or tool) making the request.
4. **Accept** – Tells the server what **response formats** the client can handle (e.g., JSON, XML).
5. **Cache-Control** – Defines **caching behavior** (e.g., `no-cache`, `max-age=3600`).
6. **Host** – Specifies the **domain name** of the server being contacted.
7. **Cookie** – Sends stored **session or tracking data** between client and server.
 

## Streamlit
- Streamlit is an open-source Python library designed to simplify the creation and sharing of custom web applications, particularly for data science, machine learning, and data visualization. It allows users to transform Python scripts into interactive web apps with minimal code and without requiring expertise in web development technologies like HTML, CSS, or JavaScript. 

## Flask 
- Lightweight web application framework written in Python. 

## Stateless: 
- Client request has to contain all required informations to process. Server will not store! 

# Fast API
- FAST API is a modern, fast(high performance), web framework for building APIs with Python 3.7+s. 

