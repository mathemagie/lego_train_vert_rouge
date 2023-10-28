from curio import sleep
from bricknil import attach, start
from bricknil.hub import PoweredUpHub
from bricknil.sensor import TrainMotor
import logging


@attach(TrainMotor, name="motor")
class Train(PoweredUpHub):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.file_vitesse = "speed.txt"

    async def run(self):
        start_vitesse = 0

        self.message_info("Running")

        while True:
            try:
                with open(self.file_vitesse, "r") as f:
                    vitesse = int(f.read())
                self.message_info("vitesse {}".format(vitesse))
                if vitesse != start_vitesse:
                    self.message_info("change speed")
                    start_vitesse = vitesse
                    await self.motor.set_speed(vitesse)
                await sleep(0.1)
            except Exception as e:
                logging.error(f"Error: {e}")
                pass


async def system():
    Train("My train")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    start(system)
