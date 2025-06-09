VMware AVI Load Balancer - POST Tenant Task

🎯 Objective
Create a new tenant named "J. Hariharan" via:
- Postman
- Python automation

🔗 Controller
- URL: https://35.200.176.139/
- Time Window: 7–11 PM only
- Credentials: `hiring-2` / `hiring-2`

🧪 Postman Steps
1. POST `/login` to get session cookie
2. POST `/api/tenant` with `"name": "J. Hariharan"`

🤖 Python Automation
```bash
pip install requests urllib3
python post_tenant.py
