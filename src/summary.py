
class Summary:
    def __init__(self, sNum, sRange, tNum=None):
        self.sensorNum = sNum
        self.sensorRange = sRange
        self.targetNum = tNum

        #Log message containing number of currently active sensors and percentage of monitored area

    def create_log_file(self, name):
        print("logfile")

    def simulation_log_message_area(self, sensors, fileName, subset):

        with open("Logs/" + str(fileName), "a") as file:
            activeSensorNum = 0
            for sensor in sensors:
                if sensor.isActive:
                    activeSensorNum += 1
            file.write("Subset:" + str(subset) + "\n" + "Active sensors: " + str(activeSensorNum) + "/" + str(self.sensorNum) + ". " + "Monitored area: " + str(activeSensorNum*(self.sensorRange/2)**2 * 3.14/10000) + "%\n")

    def simulation_log_message_target(self, sensors, targets, fileName, subset):
        with open("Logs/" + str(fileName), "a") as file:
            activeSensorNum = 0
            monitoredTargetsNum = 0
            for sensor in sensors:
                if sensor.isActive:
                    activeSensorNum += 1
            for target in targets:
                if target.monitored:
                    monitoredTargetsNum += 1
            file.write("Subset:" + str(subset) + "\n" + "Active sensors: " + str(activeSensorNum) + "/" + str(self.sensorNum) + ". " + "Monitored targets: " + str(monitoredTargetsNum) + "/" + str(self.targetNum) + "\n")
