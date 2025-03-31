# Serverless Student Data Management

## 0. Introduction

This project is a serverless application built using AWS Lambda, API Gateway, DynamoDB, and S3. It allows users to store and retrieve student data through a web interface.

## 1. Project Overview

This project implements a simple student data management system with the following features:

- Add Student Data: Allows users to submit student information through a form, which is then stored in DynamoDB.
- View Student Data: Allows users to view all stored student data from DynamoDB in a dynamic table.

## 2. Features

### 2.1 Add Student Data
This feature allows users to enter the following details for a student:
- **Student ID**: A unique identifier for each student.
- **Name**: The student's name.
- **Class**: The class in which the student is enrolled.
- **Age**: The age of the student.

The data is collected via an HTML form on the frontend (`index.html`). When the user submits the form, the data is sent to the backend (AWS Lambda) via an API call. The backend processes this data and stores it in the DynamoDB database using the `inserstudentsdata.py` Lambda function.

The data submission process is handled using AJAX in `script.js`, which makes an asynchronous request to the API Gateway that triggers the Lambda function to store the data.

### 2.2 View Student Data
This feature allows users to view all stored student data from the DynamoDB database. When a user clicks the "View All Students" button, an AJAX GET request is sent to the API Gateway. This request triggers the `getstudent.py` Lambda function, which scans the DynamoDB table for all student records.

Once the data is retrieved, it is displayed in an HTML table within the frontend. Each student's details (ID, name, class, and age) are displayed in rows. The table is dynamically populated with the data retrieved from DynamoDB.

The continuous scanning of DynamoDB ensures that if more data is added over time, users will always have access to the most up-to-date student records.

## 3. Serverless Deployment
This project uses serverless architecture, meaning that there is no need to manage the underlying infrastructure. The key serverless components include:

- **AWS Lambda**: This serverless compute service runs your code without provisioning or managing servers. The backend logic is handled by two Lambda functions:
  - `getstudent.py`: Retrieves all student data from DynamoDB.
  - `inserstudentsdata.py`: Inserts student data into DynamoDB.

- **Amazon API Gateway**: API Gateway acts as a gateway to connect the frontend with the Lambda functions. It exposes RESTful API endpoints (such as `/insertStudent` and `/getStudents`) that the frontend uses to interact with the backend.

Since these services are serverless, there is no need to provision or manage servers, reducing complexity and costs, and allowing for automatic scaling based on the number of requests.

## 4. File Structure

- **`getstudent.py`**: This Lambda function is responsible for retrieving all student data from the DynamoDB database.
- **`inserstudentsdata.py`**: This Lambda function handles the insertion of new student data into the DynamoDB database.
- **`index.html`**: The HTML file that provides the user interface for adding and displaying student data.
- **`script.js`**: A JavaScript file that makes AJAX calls to the API Gateway, triggering Lambda functions to insert or retrieve student data.



## 5. Setup and Deployment

### Step 1: Create an S3 Bucket
1. Upload `index.html` and `script.js` to Amazon S3.
2. Enable static website hosting for the S3 bucket.

### Step 2: Create a DynamoDB Table
1. **Table Name**: `studentData`
2. **Primary Key**: `studentid` (String)

### Step 3: Create Lambda Functions
1. Deploy `getstudent.py` and `inserstudentsdata.py` as AWS Lambda functions.
2. Assign them appropriate IAM permissions to access DynamoDB.

### Step 4: Configure API Gateway
1. Create an API with:
   - **POST /insertStudent** → Inserts Student Data.
   - **GET /getStudents** → Retrieves All Students.
2. Link the API Gateway to the Lambda functions.

### Step 5: Update Frontend
1. Replace `API_ENDPOIND_PASTE_HERE` in `script.js` with your API Gateway endpoint.

### Step 6: Test the Application
1. Open `index.html` in the browser.
2. Add student data and retrieve it by clicking the appropriate button.

## 6. API Endpoints

| Method | Endpoint         | Description          |
|--------|------------------|----------------------|
| POST   | /insertStudent   | Inserts a new student|
| GET    | /getStudents     | Retrieves all students|

## 7. Technologies Used

- **AWS Lambda**
- **Amazon API Gateway**
- **Amazon DynamoDB**
- **Amazon S3**
- **JavaScript (AJAX, jQuery)**
- **HTML/CSS**

## 8. Future Enhancements

- Add user authentication using AWS Cognito.
- Implement data validation in Lambda functions.
- Improve UI with React or Vue.js.

## 9. Author

Priyannka Santoki


