import mpu6050
import fs
import math
from time import sleep


db = fs.firestore_init()

try:
    while True:
        doc1, doc2 = '', ''
        docs = db.collection('rooms').where('IsHoi', '==', True).get()
        for doc in docs:
            doc1 = doc.id

        if not doc1 is '':
            mpu = mpu6050.MPU6050()
            acc_x, acc_y, acc_z = mpu.get_accel_data_g()
            ang_x, ang_y, ang_z = mpu.calc_angle(acc_x, acc_y, acc_z)
            if ang_y >= 0 or ang_y < -100:
                val = ang_z % 360 
            else:
                val =  -1 * ang_z % 360
            print '%3d' % (val)
            val = math.floor(val)
 
            docs = db.collection('rooms').document(doc1).collection('users').where('IsEvil', '==', True).get()
        for doc in docs:
            doc2 = doc.id
            break

        if not doc1 is '' and not doc2 is '':
            db.collection('rooms').document(doc1).collection('users').document(doc2).update({
                "Gyro": val
            })

        if not doc1 is '':
            while True:
                flag = db.collection('rooms').document(doc1).get().to_dict()['IsHoi']
                if not flag:
                    break


                
	sleep(1)


except KeyboardInterrupt:
        print("finished")
