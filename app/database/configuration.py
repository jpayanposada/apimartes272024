#Datos para la conexiòn a BD

dataBaseName="gestordb"
userName="root"
userPassword=""
connectionPort=3306
server="localhost"

# Creando la conexiòn 

dataBaseConnection = f"mysql+mysqlconnector:// {userName}:{userPassword}@{server}:{connectionPort}/{dataBaseName}"

print(dataBaseConnection)