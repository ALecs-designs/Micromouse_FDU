from .hardware_setup import i2c
import adafruit_lis3mdl, adafruit_lsm6ds

def init_imu_and_mag():
            imu = None
            mag = None
            try:
                imu = adafruit_lsm6ds.lsm6dsox.LSM6DSOX(i2c, address=0x6B)
                print("✅ LSM6DSOX IMU initialized at 0x6B")
            except Exception as e:
                print(f"❌ IMU init failed: {e}")
                imu = None
            try:
                mag = adafruit_lis3mdl.LIS3MDL(i2c, address=0x1E)
                print("✅ LIS3MDL magnetometer initialized at 0x1E")
            except Exception as e:
                print(f"❌ Magnetometer init failed: {e}")
                mag = None
            return imu, mag