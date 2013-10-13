#include <whitedb/dbapi.h>
#include <stdlib.h>
#include <stdio.h>

int main(int argc, char **argv) {
  void *db;
  char *name="1";
  int i,j;
  for(i=0;i<1;i++) { // 100000
    db = malloc(1000000000);  // 10000000
    for(j=0;j<50000000;j++) {
      *((int*)db+j)=0;
    }    
    free(db);    
  }  
  printf("i %d\n", i);
  return 0;
}