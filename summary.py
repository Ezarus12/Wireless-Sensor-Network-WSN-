
class Summary:
    def __init__(self, sNum, sRange, tNum=None):
        self.sensorNum = sNum
        self.sensorRange = sRange
        self.targetNum = tNum

        #Log message containing number of currently active sensors and percentage of monitored area
    def simulation_log_message_area(self, sensors):
        activeSensorNum = 0
        for sensor in sensors:
            if sensor.isActive:
                activeSensorNum += 1
        
        print("Active sensors: ", activeSensorNum, "/", self.sensorNum, ". ", "Monitored area: ", (activeSensorNum*(self.sensorRange/2)**2 * 3.14/10000), "%",)

    def simulation_log_message_target(self, sensors, targets):
        activeSensorNum = 0
        monitoredTargetsNum = 0
        for sensor in sensors:
            if sensor.isActive:
                activeSensorNum += 1
        for target in targets:
            if target.monitored:
                monitoredTargetsNum += 1
        print("Subset:", subset)
        print("Active sensors: ", activeSensorNum, "/", self.sensorNum, ". ", "Monitored targets: ", monitoredTargetsNum, "/", self.targetNum)