import SensorDistance from "./SensorDistance";
import SensorCliffDetection from "./SensorCliffDetection";
import SensorObjectDetection from "./SensorObjectDetection";

const Sensor = () => {

    return (
        <div className="flex flex-col justify-center gap-5"> 
            <SensorDistance />
            <SensorCliffDetection />
            <SensorObjectDetection />
        </div>
    )

}

export default Sensor;