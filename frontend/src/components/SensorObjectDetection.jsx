"use client"

import useFetchSensorData from "@/hooks/useFetchSensorData";

const SensorObjectDetection = () => {

    const objectDetection = useFetchSensorData({ sensorEndpoint: "object-detection" });

    return (
        <div className="flex flex-col justify-center">
            <p>Object Detection</p>
            <ul className="flex flex-col gap-2">
                {objectDetection && objectDetection.map((detection) => (
                    <li key={detection}>
                        <p>{detection}</p>
                    </li>
                ))}
            </ul>
        </div>
    )

}

export default SensorObjectDetection;