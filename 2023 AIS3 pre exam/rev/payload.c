/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>

int main()
{
    int init_values[36] = {138, 80, 146, 200, 6, 61, 91, 149, 182, 82, 27, 53, 130, 90, 234, 248, 148, 40, 114, 221, 212, 93, 227, 41, 186, 88, 82, 168, 100, 53, 129, 172, 10, 100, 0};
    unsigned char enc[36];

    for (int i = 0; i < 36; i++) {
        enc[i] = (char)init_values[i];
    }
    
    for (int i=0;i<35;i++) {
        
        for (char j=0;j<255;j++){
            
            unsigned char guess = ((i^j) << ((i^9) & 3)|(i^j) >> (8-((i^9) & 3)))+8;
            
            if(enc[i] == guess){
                printf("%c",j);
                break;
            }
        }
        
    }
   
    return 0;
}
