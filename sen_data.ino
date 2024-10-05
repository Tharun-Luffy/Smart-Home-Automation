#include <MPU6050_tockn.h>
#include <Wire.h>

MPU6050 mpu6050(Wire);

void setup()
{
    Serial.begin(9600);
    Wire.begin();
    mpu6050.begin();
    mpu6050.calcGyroOffsets(true);

    // Print CSV header
    //     Serial.println("temp,accX,accY,accZ,gyroX,gyroY,gyroZ,accAngleX,accAngleY,gyroAngleX,gyroAngleY,gyroAngleZ,angleX,angleY,angleZ");
}

void loop()
{
    mpu6050.update();

    // Output data as CSV without time delay
    Serial.print(mpu6050.getTemp());
    Serial.print(",");
    Serial.print(mpu6050.getAccX());
    Serial.print(",");
    Serial.print(mpu6050.getAccY());
    Serial.print(",");
    Serial.print(mpu6050.getAccZ());
    Serial.print(",");
    Serial.print(mpu6050.getGyroX());
    Serial.print(",");
    Serial.print(mpu6050.getGyroY());
    Serial.print(",");
    Serial.print(mpu6050.getGyroZ());
    Serial.print(",");
    Serial.print(mpu6050.getAccAngleX());
    Serial.print(",");
    Serial.print(mpu6050.getAccAngleY());
    Serial.print(",");
    Serial.print(mpu6050.getGyroAngleX());
    Serial.print(",");
    Serial.print(mpu6050.getGyroAngleY());
    Serial.print(",");
    Serial.print(mpu6050.getGyroAngleZ());
    Serial.print(",");
    Serial.print(mpu6050.getAngleX());
    Serial.print(",");
    Serial.print(mpu6050.getAngleY());
    Serial.print(",");
    Serial.println(mpu6050.getAngleZ());
}