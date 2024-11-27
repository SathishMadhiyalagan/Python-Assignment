Here’s a `README` file that explains the setup and usage for both the **ETL process** and **fetching jokes from JokeAPI** functionalities:

---

# **Project Name: Sales Data ETL & Joke Fetcher**

## **Overview**

This project consists of two main functionalities:
1. **Sales Data ETL (Extract, Transform, Load)** – This functionality reads sales data from CSV files, processes it, and loads it into a database.
2. **Joke Fetcher** – This functionality fetches jokes from the JokeAPI, processes them, and stores them in the database.

---

## **Technologies Used**

- **Django**: Web framework used for building the API.
- **Django REST Framework**: Used for building RESTful APIs.
- **Pandas**: For data manipulation and processing.
- **SQLite (or any other database)**: Used for storing processed data.
- **Requests**: For calling external APIs (JokeAPI).

---

## **Project Setup**

### **1. Clone the Repository**

```bash
git clone https://github.com/SathishMadhiyalagan/Python-Assignment.git
cd project-name
```

### **2. Create a Virtual Environment**

```bash
python -m venv venv
source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
```

### **3. Install Dependencies**

```bash
pip install -r requirements.txt
```

Ensure you have the following dependencies in your `requirements.txt` file:

```
Django>=5.0.0
djangorestframework
pandas
requests
```

### **4. Database Setup**

Run the following commands to set up the database:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## **API Endpoints**

### **1. ETL Process for Sales Data**

- **URL**: `/sales/etl-process/`
- **Method**: `GET`
- **Description**: This endpoint reads sales data from CSV files for two regions (`order_region_a.csv` and `order_region_b.csv`), processes the data (calculates total sales, net sales, and other required transformations), and loads it into the database.

#### **CSV Files Required**:
Ensure the CSV files are placed in the `csvFiles/` directory, with the following columns:
- `OrderId`
- `OrderItemId`
- `QuantityOrdered`
- `ItemPrice`
- `PromotionDiscount`
- Other required columns.

- **Example Usage**: Visit `http://127.0.0.1:8000/sales/etl-process/` to trigger the ETL process.

---

### **2. Retrieve Processed Sales Data**

- **URL**: `/sales/retrieve-data/`
- **Method**: `GET`
- **Description**: This endpoint fetches processed sales data from the database, including:
  - Total records in the sales data table.
  - Total sales by region.
  - Average sales across all records.
  - Count of duplicate orders based on `OrderId`.

- **Example Usage**: Visit `http://127.0.0.1:8000/sales/retrieve-data/` to retrieve the summary data.

---

### **3. Fetch and Store Jokes from JokeAPI**

- **URL**: `/jokes/fetch/`
- **Method**: `GET`
- **Description**: This endpoint fetches jokes from the JokeAPI and stores them in the database. The jokes are categorized as either "single" (one joke string) or "twopart" (setup and delivery). It also processes and stores information such as `category`, `type`, `flags`, and `language`.

- **Example Usage**: Visit `http://127.0.0.1:8000/jokes/fetch/` to fetch and store jokes from JokeAPI.

---

## **Database Models**

### **SalesData Model**
```python
class SalesData(models.Model):
       order_id = models.CharField(max_length=50, unique=True)
       order_item_id = models.CharField(max_length=50)
       quantity_ordered = models.IntegerField()
       item_price = models.FloatField()
       promotion_discount = models.FloatField()
       total_sales = models.FloatField()
       region = models.CharField(max_length=1)
       net_sales = models.FloatField()
    
```

### **Joke Model**
```python
class Joke(models.Model):
    category = models.CharField(max_length=100)
    type = models.CharField(max_length=10)
    joke = models.TextField(blank=True, null=True)  # For "single" type
    flags_nsfw = models.BooleanField()
    flags_political = models.BooleanField()
    flags_sexist = models.BooleanField()
    safe = models.BooleanField()
    lang = models.CharField(max_length=10)
```

---

## **Running the Server**

Start the Django development server with the following command:

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to test the API endpoints.

---

## **Error Handling**

- If the CSV files are missing or contain invalid data, the ETL process may raise errors related to missing columns or invalid values. Ensure the CSV files are correctly formatted.
- For external API calls to JokeAPI, ensure that the JokeAPI service is up and running. If the service is down, the joke fetcher will return an error message.

---

## **Troubleshooting**

- **Missing CSV files**: Ensure that `order_region_a.csv` and `order_region_b.csv` are present in the `csvFiles/` directory.
- **Database Errors**: If you encounter issues with database migrations, run `python manage.py migrate` to ensure your database schema is up to date.

---
