import Joystick from "@/components/Joystick";
import Sensor from "@/components/Sensor";

export default function Home() {

  return (
    <div className="flex items-center justify-center gap-20">
      <Joystick />
      <Sensor />
    </div>
  )

}
