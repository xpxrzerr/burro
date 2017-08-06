
# RC Control

THROTTLE_CHANNEL = 2
YAW_CHANNEL = 0
ARM_CHANNEL = 4

# Recording

THROTTLE_RECORD_LIMIT = 0.010
SESSION_DIR = "home/pi/burro/sessions"

# Sensors

CAMERA_RESOLUTION = (132, 99)
CAMERA_FRAMERATE = 30
CAMERA_HORIZONTAL_FOV = 120.
CAMERA_OUTPUT_RANGE = (0, 255)

# Vehicle - General

REVERSE_STEERING = False
CAR_MAX_STEERING_ANGLE = 30.
DRIFT_GAIN = 0.15

# Vehicle - Differential

LEFT_MOTOR_TERMINAL = 1
RIGHT_MOTOR_TERMINAL = 2
LEFT_MOTOR_MULT = 1.0
RIGHT_MOTOR_MULT = 1.0
LEFT_MOTOR_REVERSE = False
RIGHT_MOTOR_REVERSE = False

# Models

MODEL_INPUT_RANGE = (0, 255)
MODEL_OUTPUT_SIZE = 15
KERAS_AVERAGE_FACTOR = 0.8
MODELS_DIR = "../models"
LOGS_DIR = "../logs"
