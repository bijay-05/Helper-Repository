# Inventory Batch Pipeline

#### All scripts, code snippets and useful stuff for the success of project **Batch Pipeline for Inventory Management Dashboard**

## Some of the miscellaneous commands and tricks encountered during project
### Remote Virtual Machine
```
$eval $(ssh-agent -s) # starts ssh-agent and checks status

$ssh-add .ssh/key_file.pem # adds key file to the ssh-agent
$ssh-add -D #delete all files from agent

$ssh user@ip_address
$ssh -i .ssh/key_file.pem user@ip_address

```

### Connecting with database (psql)
```
$psql --username db_admin --dbname inventory-database --host some_address --port 5432 -p

# -p argument prompts terminal to ask for password of database
```


### Writing out pandas dataframe to CSV
![image](https://github.com/bijay-05/Helper-Repository/assets/86017045/59fec491-7de0-435b-a924-f2979124961b)
