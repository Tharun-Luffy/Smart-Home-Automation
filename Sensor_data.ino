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
    Serial.println("Temp,AccX,AccY,AccZ,GyroX,GyroY,GyroZ,AccAngleX,AccAngleY,GyroAngleX,GyroAngleY,GyroAngleZ,AngleX,AngleY,AngleZ");
}

void loop()
{
    mpu6050.update();

    // Output data as CSV
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
    Serial.println(mpu6050.getAngleZ()); // Ensure a new line is sent
    delay(200);                          // Delay between readings
}
