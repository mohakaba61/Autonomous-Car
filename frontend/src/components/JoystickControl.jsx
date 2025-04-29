import { Slider } from "@/components/ui/slider";
import { memo } from "react";

const JoystickControl = ({ onChange, min, max, step }) => {
    return (
        <Slider defaultValue={[(max + min + step) / 2 - step]} min={min} max={max} step={step} onValueChange={(value) => onChange(value[0])} />
    );
}

export default memo(JoystickControl);