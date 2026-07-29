# devops-starter-app

A tiny Flask API used as a practice project to walk through the full DevOps
lifecycle: Git → CI/CD → Docker → Terraform → Kubernetes → Prometheus → Grafana.

## Endpoints

- `GET /` — returns a hello message, hostname, and a request counter
- `GET /health` — returns `{"status": "ok"}`, used later for Kubernetes health checks

## Run locally

\`\`\`bash
python3 -m venv venv
source venv/bin/activate       # on Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
\`\`\`

Then visit http://localhost:5000 in your browser, or:

\`\`\`bash
curl http://localhost:5000
curl http://localhost:5000/health
\`\`\`