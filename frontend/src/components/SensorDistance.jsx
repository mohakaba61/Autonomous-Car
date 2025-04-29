"use client"

import useFetchSensorData from "@/hooks/useFetchSensorData";

const SensorDistance = () => {

    const distance = useFetchSensorData({ sensorEndpoint: "distance" });

    return (
       <p>Distance: {distance}</p>
    )

}

export default SensorDistance;