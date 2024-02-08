#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdbool.h>

void red();
void reset (); 
void purple();
void login();
void menu();
int balcheck(int bal);
int repeat(char choose);
int deposit(int bal);
int Withdraw(int bal);
void errormsg();

/* structure is called out of the main function to store the attributes that are gonna be used. */

 struct cust{
 	int id;
 	float money;
 	char name[30];
 };
 /*an array is assigned already with some data. Another pointer is also created to be used later for storing data.*/
 struct cust a[4] = {{2991,12000.0,"Ghufran"},{1223,22400.0,"Ali"},{1313,2000.0,"Saba"},{2456,30000.0,"Aamir"}};
 struct cust k, *p = &k;
 

int main(int argc, char *argv[]) {
	
	
	
	
int option = 0;
char choose;
float bal = 0,m;
/*variables are set to run the options for switch case statements and balance is also initialised.*/
system("COLOR F2");
 /*Filing is used to select data from the array and store in a loop in the .txt file  on windows. Fread and fwrite is used to take out data from the file and put in data respectively.*/
 FILE *fp;
 int p;
 int i,n;
 char path[100];
 
 printf("Enter the path of txt file: ");
 scanf("%s", path);
 
 fp = fopen(path, "w+");
 /*syntax for fwrite and fread*/
 fwrite(a, sizeof(struct cust), 4, fp);
 rewind(fp);
 
 for(i=0; i<4; i++){
 	fread(p, sizeof(struct cust), 1, fp);
 //	printf("id=%d, money=%0.2f, name=%s\n", a[i].id, a[i].money, a[i].name);
 }
 printf("Enter id: ");
 scanf("%d", &p);
 for(i= 0; i<4; i++){
 	if( p == a[i].id){
 		bal = a[i].money;
 		i = n;
	 }
}/* idea of using id from the user and taking that user's money to be set as new balance value to be used further in code*/


 /*Menu code is displayed as in the function menu().Options are listed below for what you need to perform.*/
menu();
do {
	purple();
	printf("\t\t\t\t=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n\n");
	if(choose == 'Y'){
	printf("\t\t\t\t1) ;  Check Balance\n");
    printf("\t\t\t\t2) ;  Deposit\n");
    printf("\t\t\t\t3) ;  Withdraw\n");
    printf("\t\t\t\t4) ;  Exit\n\n");	
	}
	printf("\t\t\t\t=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n\n");
	printf("SELECT:\t");
	scanf("%d", &option);
		
	// Switch statement use structure share and whenvhe someomed odd 
	
	switch(option){
		
		case 1 :
		// value of bal is returned to the given function whereever it is being updated
			bal = balcheck(bal);
			//system("CLS");
			break;
	
		case 2 :
		
			bal = deposit(bal);
			//system("CLS");	
			break;
	
		case 3 :
		
			bal = Withdraw(bal);
			//system("CLS");
			break;
	
		case 4 :
			printf("\t\t\t********************Thank you for Banking with us !!!********************\n");
			printf("\t\t\t************For more help call at service line: 111-111-124 *****************\n");
			//system("CLS");
			break;
	
		default :
			errormsg();
			//system("CLS");
			break;
	}
	
	printf("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n");
	printf("Would you like another transaction : \n");
	printf("Y = Yes\n");
	printf("N = No\n");
	scanf("%s", &choose);
	
} // if the value of character choosing for more transactions is no the program is ended. 
while(choose == 'Y');

if(choose == 'N') {
		printf("\t\t\t********************Thank you for Banking with us !!!********************\n");
			printf("\t\t\t************For more help call at service line: 111-111-124 *****************\n");
	}	
	
	return 0;
}
// when transaction is repeated this list of selection of numbers is displayed again.
int repeat(char choose){
	printf("\t\t\t\t1) ;  Check Balance\n");
    printf("\t\t\t\t2) ;  Deposit\n");
    printf("\t\t\t\t3) ;  Withdraw\n");
    printf("\t\t\t\t4) ;  Exit\n\n");
    
    return 0;
}

void menu(){
	purple();
	printf("\t\t\t\t********************Hello!********************\n");
	printf("\t\t\t\t***********Welcome to ATM Banking*************\n\n\n");
    printf("\t\t\t\t1) ;  Check Balance\n");
    printf("\t\t\t\t2) ;  Deposit\n");
    printf("\t\t\t\t3) ;  Withdraw\n");
    printf("\t\t\t\t4) ;  Exit\n\n");
	
}

int balcheck(int bal){
	purple();
	printf("You chose to see your balance\n");
	printf("\n\n Your Balance is :  $%d\n\n", bal);
	return bal;
}

// function used to deposit money in the variable balance and updates it
int deposit(int bal){
	int n=4,i;
	int dep; 
	purple();
    printf("You chose to deposit money\n");
    printf("\n\n Your Balance is :  $%d\n\n", bal);
    printf("Enter the amount of money you want to deposit\n");
    
    scanf("%d", &dep);
	bal += dep;
	
    printf("\n\n Your New Balance is :  $%d\n\n", bal);
	return bal;
}
// function used to withdraw from the amount of variable balance that has been updated
int Withdraw(int  bal){
	purple();
	int withdraw;
	printf("You chose to withdraw\n");
	printf("\n\n Your Balance is :  $%d\n\n", bal);
	
	printf("Enter the amount of money you want to withdraw\n");
	scanf("%d", &withdraw);
	
	if(withdraw < bal){
		bal -= withdraw;
		printf("\n\nThe withdraw amount is %d\n\n", withdraw);
		printf("\n\n Your New Balance is :  $%d\n\n", bal);
	}
// there is an error in the output seen when withdraw amount is more then the cash you have	
	else{
		red();
		printf("You dont have that much cash in the bank\n");
		printf("*********Contact Bank Services***********\n");
		printf("\n\n Your Balance is :  $%d\n\n", bal);
		
	}
	
	return bal;
}
// numbers 1 to 4 are the one to be used if not there is error messsage to reselect the option from 1-4.
void errormsg(){
	red();
	printf("\t\t********************Choose from the options above 1-4********************\n");
}
//colours are used to represent theme such as errors represent red while normal atm stuff is in purple and background colour is white to make the console output look cleaner.
void red(){
  printf("\033[1;31m");
}

void reset () {
  printf("\033[0m");
}
void purple(){
   printf(" \033[1;35m"); 
}

 
 





