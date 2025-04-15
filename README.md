# 🛡️ Privacy Logging Infra

A simulated backend infrastructure for secure and privacy-aware logging — built with **FastAPI**, and designed to showcase core principles like **purpose tagging**, **encryption**, **access control**, and **compliance-aware architecture**.

> ⚙️ Inspired by privacy infrastructure challenges at scale.
---

## 🚀 Features

- 🔐 **Token-based API authentication** (simulated with JWT-style tokens)
- 🧾 **Purpose-tagged event logging** (e.g., `security_audit`)
- 🔒 **Field-level encryption** (simulated using Base64 encoding)
- 🛡️ **Governance utilities** for tagging, redaction, and data purpose
- 🐳 **Docker-ready**, deployable via **Kubernetes**
- 🧪 **Unit tests** for log handling logic
- 📈 **Load testing script** to simulate real traffic

---

## 🧱 Project Structure

```bash
privacy_logging_system_advanced/
├── app/
│   ├── main.py              # API endpoint
│   ├── services/            # Business logic (log_event)
│   └── utils/               # Auth, encryption, governance modules
├── config/                  # Configs (token, logging level)
├── infra/k8s/               # Kubernetes deployment files
├── scripts/                 # Load test scripts
├── tests/                   # Unit test for services
├── Dockerfile
├── requirements.txt
└── README.md
```


## 🔧 Getting Started

### ✅ Install & Run

```bash
git clone https://github.com/likhithsj/privacy-logging-infra.git
cd privacy-logging-infra
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## 🧪 Test the Logging API

You can test the secure logging with:

```bash
python scripts/load_test.py
```
