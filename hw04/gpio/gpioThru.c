// From : http://stackoverflow.com/questions/13124271/driving-beaglebone-gpio-through-dev-mem
//
// Read one gpio pin and write it out to another using mmap.
// Be sure to set -O3 when compiling.
// Modified by Mark A. Yoder  26-Sept-2013
#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <signal.h>    // Defines signal-handling functions (i.e. trap Ctrl-C)
#include "beaglebone_gpio.h"

/****************************************************************
 * Global variables
 ****************************************************************/
int keepgoing = 1;    // Set to 0 when ctrl-c is pressed

/****************************************************************
 * signal_handler
 ****************************************************************/
void signal_handler(int sig);
// Callback called when SIGINT is sent to the process (Ctrl-C)
void signal_handler(int sig)
{
    printf( "\nCtrl-C pressed, cleaning up and exiting...\n" );
	keepgoing = 0;
    printf("keepgoing = 0\n");
}

int main(int argc, char *argv[]) {
    volatile void *gpio_button_addr;
    volatile unsigned int *gpio_button_oe_addr;
    volatile unsigned int *gpio_button_datain;
    volatile unsigned int *gpio_button_setdataout_addr;
    volatile unsigned int *gpio_button_cleardataout_addr;
    unsigned int reg;

    volatile void *gpio_led_addr;
    volatile unsigned int *gpio_led_oe_addr;
    volatile unsigned int *gpio_led_datain;
    volatile unsigned int *gpio_led_setdataout_addr;
    volatile unsigned int *gpio_led_cleardataout_addr;

    // Set the signal callback for Ctrl-C
    signal(SIGINT, signal_handler);

    int fd = open("/dev/mem", O_RDWR);

    // printf("Mapping %X - %X (size: %X)\n", GPIO0_START_ADDR, GPIO0_END_ADDR,
    //                                        GPIO0_SIZE);

    gpio_button_addr = mmap(0, GPIO3_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd,
                        GPIO3_START_ADDR);

    gpio_button_oe_addr           = gpio_button_addr + GPIO_OE;
    gpio_button_datain            = gpio_button_addr + GPIO_DATAIN;
    gpio_button_setdataout_addr   = gpio_button_addr + GPIO_SETDATAOUT;
    gpio_button_cleardataout_addr = gpio_button_addr + GPIO_CLEARDATAOUT;


    gpio_led_addr = mmap(0, GPIO3_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd,
                        GPIO3_START_ADDR);

    gpio_led_oe_addr           = gpio_led_addr + GPIO_OE;
    gpio_led_datain            = gpio_led_addr + GPIO_DATAIN;
    gpio_led_setdataout_addr   = gpio_led_addr + GPIO_SETDATAOUT;
    gpio_led_cleardataout_addr = gpio_led_addr + GPIO_CLEARDATAOUT;


    if((gpio_button_addr == MAP_FAILED) | (gpio_led_addr == MAP_FAILED)) {
        printf("Unable to map GPIO\n");
        exit(1);
    }
    // printf("GPIO mapped to %p\n", gpio_addr);
    // printf("GPIO OE mapped to %p\n", gpio_oe_addr);
    // printf("GPIO SETDATAOUTADDR mapped to %p\n", gpio_setdataout_addr);
    // printf("GPIO CLEARDATAOUT mapped to %p\n", gpio_cleardataout_addr);

    printf("Start copying\n");
    while(keepgoing) {
    	if(*gpio_button_datain & GPIO3_17) {
            *gpio_led_setdataout_addr= GPIO3_1;
            printf("Mapping 17 to 1\n");
    	} else {
            *gpio_led_cleardataout_addr = GPIO3_1;
            printf("Clearing 1\n");
    	}
        if(!(*gpio_button_datain & GPIO3_20)) {
            *gpio_led_setdataout_addr= GPIO3_2;
            printf("Mapping 20 to 2\n");
    	} else {
            *gpio_led_cleardataout_addr = GPIO3_2;
            printf("Clearing 2\n");
    	}
        usleep(100000);
    }

    // munmap((void *)gpio_addr, GPIO0_SIZE);
    printf("Exiting\n");
    close(fd);
    return 0;
}
