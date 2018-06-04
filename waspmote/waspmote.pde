

#include <WaspSensorAgr_v30.h>
#include <WaspFrame.h>
#include <WaspXBee900HP.h>

#define TELE_COM XBEE_900
#define NODE_ID "node_01"

watermarkClass wmSensor1(SOCKET_E); // soil mosture
watermarkClass wmSensor2(SOCKET_C); // soil mosture
radiationClass radSensor; // solar radiation meter


// Destination MAC address
//////////////////////////////////////////
char RX_ADDRESS[] = "0013A200414847FE";
//////////////////////////////////////////

// Define the Waspmote ID

// define variable
uint8_t error;


void setup()
{
  // init USB port
  USB.ON();
  USB.println(F("Sending packets example"));
  Agriculture.ON();

  // store Waspmote identifier in EEPROM memory
  frame.setID( NODE_ID );

  // init XBee
  xbee900HP.ON();

}


void loop()
{
  ///////////////////////////////////////////
  // 1. Create ASCII frame
  ///////////////////////////////////////////

  // create new frame
  frame.createFrame(ASCII);

  // add frame fields
  frame.addSensor(SENSOR_BAT, PWR.getBatteryLevel());
  frame.addSensor(SENSOR_AGR_SOIL_E, (float) wmSensor1.readWatermark());
  frame.addSensor(SENSOR_AGR_SOIL_C, (float) wmSensor2.readWatermark());
  frame.addSensor(SENSOR_AGR_TC, (float) Agriculture.getTemperature());
  frame.addSensor(SENSOR_AGR_HUM, (float) Agriculture.getHumidity());
  frame.addSensor(SENSOR_AGR_PRES, (float) Agriculture.getPressure());
  frame.addSensor(SENSOR_AGR_PAR, (float) (radSensor.readRadiation()) / 0.0002);

  // show frame to send
  frame.showFrame();


  ///////////////////////////////////////////
  // 2. Send packet
  ///////////////////////////////////////////

  // send XBee packet
  error = xbee900HP.send( RX_ADDRESS, frame.buffer, frame.length );

  // check TX flag
  if ( error == 0 )
  {
    USB.println(F("send ok"));

    // blink green LED
    Utils.blinkGreenLED();

  }
  else
  {
    USB.println(F("send error"));

    // blink red LED
    Utils.blinkRedLED();
  }

  PWR.deepSleep("00:00:05:00", RTC_OFFSET, RTC_ALM1_MODE1, ALL_OFF);
  USB.println(F("wake up"));
  Agriculture.ON();
  xbee900HP.ON();
}



