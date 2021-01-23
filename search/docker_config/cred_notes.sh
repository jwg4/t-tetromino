# Create SP
az ad sp create-for-rbac
# The output includes credentials that you must protect. Be sure that you do not include these credentials in your code or check the credentials into your source control. For more information, see https://aka.ms/azadsp-cli
# {
#   "appId": "...",
#   "displayName": "azure-cli-2021-01-03-01-58-27",
#   "name": "http://azure-cli-2021-01-03-01-58-27",
#   "password": "...",
#   "tenant": "..."
# }
ACR_NAME=ttdocker
ACR_REGISTRY_ID=$(az acr show --name $ACR_NAME --query id --output tsv)
echo $ACR_REGISTRY_ID
# /subscriptions/.../resourceGroups/t-tetromino/providers/Microsoft.ContainerRegistry/registries/ttdocker
# 
# appId from above
SERVICE_PRINCIPAL_ID="..."
az role assignment create --assignee $SERVICE_PRINCIPAL_ID --scope $ACR_REGISTRY_ID --role acrpush
