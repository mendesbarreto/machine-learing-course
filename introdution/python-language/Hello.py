class LogInformation:
    log: str
    logType: str

def printHelloAsync(information: LogInformation):
    print(information.log + information.logType)

info: LogInformation = LogInformation()
info.log = "Douglas"
info.logType = "[INFO]"

printHelloAsync(info)
