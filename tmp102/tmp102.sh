#! /bin/bash
i2cget -y 1 0x48 0x00 w | \
awk '{printf( "%.2f\n", ( a=( \
"0x" substr( $1,5,2)substr($1,3,1))*0.0625 \
)>128?a-256:a)}'
