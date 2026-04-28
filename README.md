# CRM Lost Mary (versión limpia)

## IMPORTANTE

NO subir credentials.json

## Configuración en Streamlit Cloud

Ve a Settings → Secrets y pega:

[google_credentials]
type = "service_account"
project_id = "crm-lostmary"
private_key_id = "TU_KEY_ID"
private_key = "-----BEGIN PRIVATE KEY-----\nTU_KEY\n-----END PRIVATE KEY-----\n"
client_email = "crm-lostmary-service@crm-lostmary.iam.gserviceaccount.com"
client_id = "TU_CLIENT_ID"

## Ejecutar local
streamlit run streamlit_app.py
