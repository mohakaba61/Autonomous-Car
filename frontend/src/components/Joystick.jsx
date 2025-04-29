"use client"

import JoystickDirection from "@/components/JoystickDirection";
import JoystickControl from "@/components/JoystickControl";
import { useEffect, useState } from "react";
import axios from "axios";

const POWER_SLIDER_MIN = 10;
const POWER_SLIDER_MAX = 100;
const POWER_SLIDER_STEP = 10;

const TIME_SLIDER_MIN = 0.1;
const TIME_SLIDER_MAX = 2;
const TIME_SLIDER_STEP = 0.1;

const Container = ({ children }) => {
  return (
    <div className="flex flex-col gap-4">
      {children}
    </div>
  )
}

const Joystick = () => {

  const [direction, setDirection] = useState("parked");
  const [isMoving, setIsMoving] = useState(false);
  const [power, setPower] = useState((POWER_SLIDER_MAX + POWER_SLIDER_MIN + POWER_SLIDER_STEP) / 2 - POWER_SLIDER_STEP);
  const [time, setTime] = useState((TIME_SLIDER_MAX + TIME_SLIDER_MIN + TIME_SLIDER_STEP) / 2 - TIME_SLIDER_STEP);

  useEffect(() => {

    const move = async (direction) => {

      setIsMoving(true);

      const response = await axios({
        method: "POST",
        url: `http://192.168.10.52:5000/move-${direction}`,
        data: {
          power,
          time
        }
      });
  
      console.log(response.data);

      setIsMoving(false);
      setDirection("parked");

    }

    if (direction === "parked") {
      return;
    }

    move(direction);

  }, [direction])

  return (
    <div className="flex flex-col gap-8">
      <JoystickDirection onChange={setDirection} isMoving={isMoving} />
      <Container>
        <p>Power: {power} / {POWER_SLIDER_MAX}</p>
        <JoystickControl onChange={setPower} min={POWER_SLIDER_MIN} max={POWER_SLIDER_MAX} step={POWER_SLIDER_STEP} />
      </Container>
      <Container>
        <p>Time: {time} / {TIME_SLIDER_MAX}</p>
        <JoystickControl onChange={setTime} min={TIME_SLIDER_MIN} max={TIME_SLIDER_MAX} step={TIME_SLIDER_STEP} />
      </Container>
    </div>
  );
}

export default Joystick;
