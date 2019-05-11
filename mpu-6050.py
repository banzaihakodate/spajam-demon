import smbus
import math
from time import sleep


class MPU6050:

	DEV_ADDR = 0x68

	ACCEL_XOUT = 0x3b
	ACCEL_YOUT = 0x3d
	ACCEL_ZOUT = 0x3f
	TEMP_OUT = 0x41
	GYRO_XOUT = 0x43
	GYRO_YOUT = 0x45
	GYRO_ZOUT = 0x47
	PWR_MGMT_1 = 0x6b
	PWR_MGMT_2 = 0x6c

	def __init__(self):
		self.bus = smbus.SMBus(1)
		self.bus.write_byte_data(MPU6050.DEV_ADDR, MPU6050.PWR_MGMT_1, 0)

	def read_byte(self, adr):
		return self.bus.read_byte_data(MPU6050.DEV_ADDR, adr)

	def __read_word(self, adr):
		high = self.bus.read_byte_data(MPU6050.DEV_ADDR, adr)
		low = self.bus.read_byte_data(MPU6050.DEV_ADDR, adr+1)
		val = (high << 8) + low
		return val

	def __read_word_sensor(self, adr):
		val = self.__read_word(adr)
		if (val >= 0x8000):
			return -((65535 -val) + 1)
		else:
			return val


	def get_accel_data_lsb(self):
		x = self.__read_word_sensor(MPU6050.ACCEL_XOUT)
		y = self.__read_word_sensor(MPU6050.ACCEL_YOUT)
		z = self.__read_word_sensor(MPU6050.ACCEL_ZOUT)
		return [x, y, z]

	def get_accel_data_g(self):
		x,y,z = self.get_accel_data_lsb()
		x = x / 16384.0
		y = y / 16384.0
		z = z / 16384.0
		return [x, y, z]


	def calc_angle(self, x, y, z):
			ang_x = math.atan2(x, z) * 360 / 2.0 / math.pi
			ang_y = math.atan2(y, z) * 360 / 2.0 / math.pi
			ang_z = math.atan2(x, y) * 360 / 2.0 / math.pi
			return [ang_x, ang_y, ang_z]


while True:
        mpu = MPU6050()
        acc_x, acc_y, acc_z = mpu.get_accel_data_g()
        ang_x, ang_y, ang_z = mpu.calc_angle(acc_x, acc_y, acc_z)
		if ang_y >= 0 or ang_y < -100:
			print '%3d' % (ang_z % 360),
		else:
			print '%3d' % (-1 * ang_z % 360),
        print
	sleep(1)
