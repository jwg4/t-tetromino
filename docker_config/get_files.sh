. details.sh

STORAGE_KEY=$(az storage account keys list --resource-group $RES_GROUP --account-name $ACI_STORAGE_ACCOUNT_NAME --query "[0].value" --output tsv)

az storage file list --share-name $ACI_SHARE_NAME --account-name $ACI_STORAGE_ACCOUNT_NAME --account-key=$STORAGE_KEY --output tsv | cut -f2 | while read -r filename ; do
    if [ -f "results/$filename" ]; then
        echo "$filename exists"
    else
        echo "Downloading $filename"
        az storage file download --share-name $ACI_SHARE_NAME --account-name $ACI_STORAGE_ACCOUNT_NAME --account-key=$STORAGE_KEY --path "$filename" --dest "results/$filename" --output none
        ID=$(echo $filename | sed -e 's/^output_//' -e 's/.txt$//')
        if [ -f "tasks/holding/${ID}.py" ]; then
            mv "tasks/holding/${ID}.py" tasks/done
        fi
    fi
done
