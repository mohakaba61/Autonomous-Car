import { useState, useEffect } from "react";

const useFetchSensorData = ({ sensorEndpoint }) => {
    
    const [sensorData, setSensorData] = useState();

    useEffect(() => {
        
        const fetchSensorData = async () => {
            const response = await fetch(`http://192.168.10.52:5000/${sensorEndpoint}`);
            const data = await response.json();
            console.log(data[sensorEndpoint]);
            setSensorData(data[sensorEndpoint]);
        }

        fetchSensorData();

        const intervalId = setInterval(fetchSensorData, 10 * 1000); 

        return () => clearInterval(intervalId);

    }, []);
    
    return sensorData;
        
}

export default useFetchSensorData;