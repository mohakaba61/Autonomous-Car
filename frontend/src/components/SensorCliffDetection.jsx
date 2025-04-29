"use client"

import useFetchSensorData from "@/hooks/useFetchSensorData";

const SensorCliffDetection = () => {

    const cliff = useFetchSensorData({ sensorEndpoint: "cliff-detection" });

    return (
        <p>Cliff Detection: {cliff ? "Yes" : "No"}</p>
    )

}

export default SensorCliffDetection;