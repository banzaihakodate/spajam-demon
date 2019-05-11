import mpu6050
import fs
import math



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
