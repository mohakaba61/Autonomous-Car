import { Button } from "@/components/ui/button";
import { ChevronDown, ChevronLeft, ChevronRight, ChevronUp } from "lucide-react";
import { memo } from "react";

const JoystickDirection = ({ onChange, isMoving }) => {

    return (
        <div className="w-[336px] h-[336px] flex flex-col gap-4">
            <div className="flex items-center justify-center">
                <Button className="w-[100px] h-[100px]" onClick={() => onChange("forward")} disabled={isMoving}>
                    <ChevronUp />
                </Button>
            </div>
            <div className="flex items-center justify-between">
                <Button className="w-[100px] h-[100px]" onClick={() => onChange("left")} disabled={isMoving}>
                    <ChevronLeft />
                </Button>
                <Button className="w-[100px] h-[100px]" onClick={() => onChange("right")} disabled={isMoving}>
                    <ChevronRight />
                </Button>    
            </div>
            <div className="flex items-center justify-center">
                <Button className="w-[100px] h-[100px]" onClick={() => onChange("backward")} disabled={isMoving}>
                    <ChevronDown />
                </Button>
            </div>
        </div>
    )

}

export default memo(JoystickDirection);