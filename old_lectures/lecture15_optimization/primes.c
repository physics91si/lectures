#include <stdio.h>
#include <time.h>

int isPrime(int num, int primes[], int length) {
    for(int i = 0; i < length; i++){
        if( (num%primes[i]==0) && (primes[i]!= 1))
            return 0;  //FALSE , not a prime!
    }
    return 1; //TRUE
}

/* Find p */
void find_primes(int n){
    int primes[n];  //array to hold primes in
                    //Note that it is initialized to the final size,
                    //not increasing as we find more primes
    
    primes[0] = 1;  // Set first value
    
    int length = 1;  // in we need to keep track of what indexes are used since the primes array is size n already

    int num = 2;  // Number being checked if is prime
    while(length < n){
        if(isPrime(num, primes, length)){
            primes[length] = num;  // Setting value in array to a prime number
            length++;
        }
        num++;
    }
    
   /* 
    for(int i = 0; i < n ; i++){
        printf("%d\n",primes[i]);
    }
   */
    
}

/* Main function */
int main(){
    clock_t t;
    int n = 1000;  // n is the number of primes to find
    t = clock();
    find_primes(n);
    t = clock() -t;
    printf("Time taken is: %f\n", (double)t/CLOCKS_PER_SEC);

    return 0;
}
