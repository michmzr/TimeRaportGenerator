# Project Raport API Documentation

Welcome, engineers. This document will guide you through the Raport API endpoint. The project aims to provide a way for engineers outsourced to a client to generate and obtain a report of their outsourced activities. The API is built with Python 3 and Flask.

## Endpoint: Generate Report

The API exposes an endpoint that accepts a `POST` request to generate a report based on the provided details.

- **URL**: `/raport`
- **Method**: `POST`
- **Host**: `http://127.0.0.1:5000`

### Request Payload

The request should contain a JSON payload with the following fields:

| Field            | Type    | Description                            | Format (if applicable) |
|------------------|---------|----------------------------------------|------------------------|
| `year`           | Integer | The year of the report                 | YYYY                   |
| `month`          | Integer | The month of the report (1 to 12)      | -                      |
| `out_days`       | List    | List of out-of-office days             | `%d-%m-%Y`             |
| `output_file_path`| String  | The desired output file path           | -                      |
| `project_name`   | String  | The name of the project                | -                      |
| `contractor_name`| String  | The name of the contractor             | -                      |
| `nip`            | String  | Polish company NIP number              | -                      |
| `position`       | String  | Position of the engineer               | -                      |
| `client_name`    | String  | The name of the client company         | -                      |

#### Example Payload

```json
{
    "year": 2023,
    "month": 6,
    "out_days": ["23-06-2023"],
    "output_file_path": "raport_june2023.xlsx",
    "project_name": "Super app",
    "contractor_name": "Michal Mazur",
    "nip": "9322839380",
    "position": "Java Developer",
    "client_name": "ACME Corporation"
}
```

### Response

On successful report generation, it returns the generated report as an attachment.

- **Status Code**: `200 OK`
In case of validation errors in the payload, it returns a `400 Bad Request` with error messages.
