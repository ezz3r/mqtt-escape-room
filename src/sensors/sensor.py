import pygame, math
from enum import Enum, auto

class SensorState(Enum):
    IDLE = auto()
    ACTIVE = auto()
    ERROR = auto()

class SensorValue(Enum):
    VALUE_1 = auto()

SensorStateDescriptions = {
    SensorState.IDLE: "The sensor is idle.",
    SensorState.ACTIVE: "The sensor is active.",
    SensorState.ERROR: "The sensor has an error."
}