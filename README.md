# Microsoft Fabric Data Warehouse Python Connection

## Project Overview
This repository contains a Python script (`accessingwarehouse.py`) for connecting to and retrieving data from a Microsoft Fabric Data Warehouse using a Service Principal authentication method.

## Prerequisites

### Requirements
- Python 3.7+
- Microsoft Fabric Account
- Azure Administrator Access
- pyodbc library
- python-dotenv library
- ODBC Driver 17 or 18 for SQL Server

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://your-repository-url.git
cd your-repository-name
```

### 2. Install Required Libraries
```bash
pip install pyodbc python-dotenv
```

### 3. Configure Environment Variables
Create a `.env` file in the project root with the following content:

```
# Tenant ID for authentication  
TENANT_ID=your-tenant-id  

# Client ID for authentication  
CLIENT_ID=your-client-id  

# Client Secret (Keep this secure and do not expose it)  
CLIENT_SECRET=your-client-secret  

# SQL Server address (SQL Connection String)  
SERVER=your-datawarehouse-server.datawarehouse.fabric.microsoft.com  

# Database name (Your Warehouse Name)  
DATABASE=your-database-name  
```

### 4. Python Script Explanation

#### Script: `accessingwarehouse.py`
This script demonstrates how to:
- Load environment variables securely
- Establish a connection to Microsoft Fabric Data Warehouse
- Retrieve employee data

Key components:
- Uses `pyodbc` for database connection
- Utilizes `python-dotenv` for secure credential management
- Implements Active Directory Service Principal authentication
- Fetches and prints employee data from the warehouse

### 5. Running the Script
```bash
python accessingwarehouse.py
```

## Authentication Process

### Create Service Principal in Microsoft Entra ID
1. Go to Azure Portal → Microsoft Entra ID
2. Navigate to App Registrations → New Registration
3. Create a new app registration:
   - Choose a name (e.g., FabricPythonAccess)
   - Select Single tenant
   - Click Register

### Obtain Credentials
- Collect Application (Client) ID
- Collect Directory (Tenant) ID
- Generate and copy Client Secret

## Permissions Setup

### In Microsoft Fabric
1. Enable Service Principal API access in Tenant settings
2. Grant access to your Workspace:
   - Navigate to Workspace
   - Click "Manage access"
   - Add service principal
   - Assign Viewer/Contributor role

### In Data Warehouse
1. Open Microsoft Fabric → Data Warehouse
2. Click More options (⋮) → Manage Permissions
3. Add service principal
4. Assign appropriate role (Reader or Contributor)

## Security Considerations
- Never commit `.env` file to version control
- Add `.env` to `.gitignore`
- Treat Client Secret as a sensitive credential
- Rotate credentials periodically

## Troubleshooting
- Verify all environment variables are set correctly
- Check network and firewall settings
- Ensure ODBC driver is installed
- Validate service principal permissions

## Common Errors
- Authentication failures
- Connection string issues
- Missing environment variables

## Contributing
Contributions and improvements are welcome! Please open an issue or submit a pull request.

