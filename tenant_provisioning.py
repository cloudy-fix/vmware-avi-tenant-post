import os
import sys

import requests
import urllib3


def required_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value


def create_session(base_url: str, username: str, password: str, verify_tls: bool) -> requests.Session:
    session = requests.Session()
    response = session.post(
        f"{base_url}/login",
        json={"username": username, "password": password},
        verify=verify_tls,
        timeout=20,
    )
    response.raise_for_status()

    csrf_token = session.cookies.get("csrftoken")
    if not session.cookies.get("avi-sessionid") or not csrf_token:
        raise RuntimeError("AVI login did not return the expected session cookies.")

    session.headers.update(
        {
            "Content-Type": "application/json",
            "X-CSRFToken": csrf_token,
            "Referer": base_url,
        }
    )
    return session


def create_tenant(session: requests.Session, base_url: str, tenant_name: str, verify_tls: bool) -> dict:
    response = session.post(
        f"{base_url}/api/tenant",
        json={"name": tenant_name},
        verify=verify_tls,
        timeout=20,
    )
    response.raise_for_status()
    return response.json()


def main() -> int:
    base_url = required_env("AVI_CONTROLLER_URL").rstrip("/")
    username = required_env("AVI_USERNAME")
    password = required_env("AVI_PASSWORD")
    tenant_name = os.getenv("AVI_TENANT_NAME", "Hariharan Demo Tenant")
    verify_tls = os.getenv("AVI_VERIFY_TLS", "true").lower() == "true"

    if not verify_tls:
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    try:
        session = create_session(base_url, username, password, verify_tls)
        tenant = create_tenant(session, base_url, tenant_name, verify_tls)
    except (requests.RequestException, RuntimeError) as exc:
        print(f"Tenant provisioning failed: {exc}", file=sys.stderr)
        return 1

    print(f"Tenant created successfully: {tenant.get('name', tenant_name)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

