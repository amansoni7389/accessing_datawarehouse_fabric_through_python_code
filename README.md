# Microsoft Fabric Data Warehouse Access Setup Guide

## Objective
This guide provides a comprehensive walkthrough for setting up programmatic access to a Microsoft Fabric Data Warehouse using a Service Principal.

## Step 1: Prepare Your Environment
### Prerequisites
- Microsoft 365 Account with Azure Administrator Access
- Access to Microsoft Fabric
- Python 3.7+ installed
- Internet connection
- Administrative access to Azure Portal

## Step 2: Azure Active Directory (Entra ID) Configuration
### Create Service Principal
1. Open Azure Portal (https://portal.azure.com/)
2. Navigate to Microsoft Entra ID (formerly Azure AD)
3. Click on "App registrations"
4. Select "New registration"
5. Fill in registration details:
   - Name: `FabricDataWarehouseAccess`
   - Account type: "Accounts in this organizational directory only"
   - Redirect URI: Leave blank (not needed for this use case)
6. Click "Register"

## Step 3: Obtain Necessary Credentials
### Retrieve Credentials
1. After registration, you'll see an "Overview" page
2. Copy and save the following details:
   - Application (Client) ID
   - Directory (Tenant) ID

### Generate Client Secret
1. In the left sidebar, click "Certificates & secrets"
2. Under "Client secrets" section, click "New client secret"
3. Set secret description (e.g., "Fabric Data Warehouse Access")
4. Choose expiration (recommended: 12 months)
5. Click "Add"
6. IMPORTANT: Immediately copy the generated secret value
   - This will be shown only once - do not close the page without copying

## Step 4: Configure Microsoft Fabric Permissions
### Enable Service Principal Access
1. Open Microsoft Fabric Admin Portal
2. Navigate to Tenant settings
3. Enable "Service principals can use Fabric APIs"

### Grant Workspace Access
1. Open Microsoft Fabric
2. Navigate to your specific Workspace
3. Click "Manage access"
4. Add the service principal(add name of your App)
5. Assign appropriate role (Contributor or Viewer)

### Grant Data Warehouse Access
1. Open your Data Warehouse in Microsoft Fabric
2. Click "Manage permissions"
3. Add the service principal
4. Assign appropriate role (Reader or Contributor)

## Step 5: Prepare Development Environment
### Software Requirements
1. Install Python libraries
   ```bash
   pip install pyodbc python-dotenv
   ```

2. Install ODBC Driver
   - Download and install "ODBC Driver 17 or 18 for SQL Server"
   - Available from Microsoft's official download page

## Step 6: Create Connection Configuration
### Prepare .env File
Create a file named `.env` with the following structure:
```
TENANT_ID=your-tenant-id
CLIENT_ID=your-client-id
CLIENT_SECRET=your-client-secret
SERVER=your-datawarehouse-server.datawarehouse.fabric.microsoft.com
DATABASE=your-database-name
```

## Step 7: Develop Connection Script
### Python Script Template
```python
import pyodbc
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Retrieve credentials
TENANT_ID = os.getenv("TENANT_ID")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
SERVER = os.getenv("SERVER")
DATABASE = os.getenv("DATABASE")

# Construct connection string
conn_str = (
    f'DRIVER={{ODBC Driver 17 for SQL Server}};'
    f'SERVER={SERVER};'
    f'DATABASE={DATABASE};'
    f'UID={CLIENT_ID}@{TENANT_ID};'
    f'PWD={CLIENT_SECRET};'
    f'Authentication=ActiveDirectoryServicePrincipal'
)

try:
    # Establish connection
    print("Attempting to connect to Microsoft Fabric Data Warehouse...")
    cnxn = pyodbc.connect(conn_str)
    
    # If connection is successful
    print("✅ Connection Successful!")
    print(f"Connected to Database: {DATABASE}")
    print(f"Server: {SERVER}")

except pyodbc.Error as ex:
    # Detailed error handling
    print("❌ Connection Failed!")
    print("\nDetailed Error Information:")
    print("-" * 50)
    print(f"Error Code: {ex.args[0]}")
    print(f"Error Message: {ex.args[1]}")
    
    # Additional troubleshooting tips
    print("\nTroubleshooting Tips:")
    print("1. Verify all credentials in .env file")
    print("2. Check network connectivity")
    print("3. Ensure ODBC Driver is installed")
    print("4. Confirm service principal permissions")

finally:
    # Close connection if it exists
    if 'cnxn' in locals():
        cnxn.close()
        print("\nDatabase connection closed.")
```

## Security Recommendations
- Never share your `.env` file
- Rotate client secrets every 6-12 months
- Use least privilege principle for role assignments
- Store secrets in secure vault if possible

## Troubleshooting Common Issues
1. Connection Failures
   - Verify all credentials are correct
   - Check network connectivity
   - Ensure ODBC driver is installed

2. Permission Errors
   - Confirm service principal has correct roles
   - Verify Fabric and Azure AD settings

3. Python Library Issues
   - Reinstall `pyodbc` and `python-dotenv`
   - Use virtual environments

## Estimated Setup Time
- First-time setup: 30-60 minutes
- Subsequent setups: 10-15 minutes

## Support
For persistent issues, contact:
- Azure Support
- Microsoft Fabric Support Team
- Your Organization's IT Department
