#include<iostream>
#include<fstream>
#include<string>
#include<sstream>
#include<vector>
#include <cstring>
 

using namespace std;


class JG{
	string month;
	char des[100];
	int credit, debit, date;
	static int n;
	public:
		void setmonth ( string x){
			month = x;
		}
		string getmonth(){
			return month;
		}
		void setdes ( string x){
			for(int i = 0 ; i < x.size() ; i++){
				des[i] = x[i];
			}
		}
		string getdes(){
			return des;
		}
		void setcredit (int  x){
			credit = x;
		}
		int getcredit(){
			return credit;
		}
		void setdebit (int  x){
			debit = x;
		}
		int getdebit(){
			return debit;
		}
		void setdate (int  x){
			date = x;
		}
		int getdate(){
			return date;
		}
		int getn(){
			return n;
		}
		void setn(){
			ifstream xx;
			xx.open("No_of_entries.txt");
			if(xx){
				int no;
				xx>>no;
				n = no;
				xx.close();	
			}
		}
		JG(){
		}
		JG(string x, string y, int z){
			month.clear();
			month = x;
			date = z;
			memset(des,0,100);
			for(int i = 0 ; i < y.size() ; i++){
				
				des[i] = y[i];
				//strcpy(char arr,y.c_str();
			}
		}
		void cord(){
			int a;
			for(;;){
				cout<<"Is the transaction credit ( press 1) or debit ( press 2)"<<endl;
				a = 0;
				cin>>a;
				if (!cin) {
					cout<<"INVALID RE-ENTER"<<endl;
				    continue;
				}
				if(a==1){
					cout<<"enter amount:"<<endl;
					cin>>credit;
					debit = 0;
					break;
				}
				else if(a==2){
					cout<<"enter amount:"<<endl;
					cin>>debit;
					credit = 0;
					break;
				}
			}
		}

	friend class accountant;
};



int JG::n = 0;

class accountant {
	string password;
	public:
		accountant(){
		}
		accountant(string x):password(x){
			ofstream aa;
			aa.open("pass.txt");
			aa<<password;
			aa.close();
		}
		bool check(string x){
			string pass;
			ifstream aa;
			aa.open("pass.txt");
			aa>>pass;
			aa.close();
			
			if(pass == x){
				return true;
			}
			else{
				return false;
			}
		}
		void initializefile(JG j){
			ifstream jg;
			jg.open("general_journal.csv");
			if(jg){
				jg.close();
				ifstream xx;
				xx.open("No_of_entries.txt");
				if(xx){
					int no;
					xx>>no;
					j.n = no+1;
					xx.close();	
				}
				else{
					j.n++;
				}
				ofstream jh;
				jh.open("general_journal.csv",ios::app);
				if(j.debit != 0){     
					jh<<j.n<<","<<j.month<<" "<<j.date<<","<<j.des<<","<<" "<<","<<j.debit<<","<<" "<<","<<" "<<endl;
				}
				else{
					jh<<j.n<<","<<j.month<<" "<<j.date<<","<<" "<<","<<j.des<<","<<" "<<","<<j.credit<<","<<" "<<endl;
				}
				jh.close();
				ofstream aa;
				aa.open("No_of_entries.txt");
				aa<<j.n<<endl;;
				aa.close();
				ofstream obj;
				obj.open("gj.txt",ios::app);
				obj.write((char*)&j,sizeof(j));
				obj.close();
				return ;
			}
			else{
				jg.close();
				ifstream xx;
				xx.open("No_of_entries.txt");
				if(xx){
					int no;
					xx>>no;
					j.n = no+1;
					xx.close();	
				}
				else{
					j.n++;
				}
				ofstream gg;
				gg.open("general_journal.csv");
				gg<<"ENTRY NO"<<","<<"DATE"<<","<<"DESCRIPTION"<<","<<" "<<","<<"DR+"<<","<<"CR+"<<endl;
				if(j.debit != 0){
					gg<<j.n<<","<<j.month<<" "<<j.date<<","<<j.des<<","<<" "<<","<<j.debit<<endl;
				}
				else{
					gg<<j.n<<","<<j.month<<" "<<j.date<<","<<","<<j.des<<","<<" "<<","<<j.credit<<endl;
				}
				gg.close();
				ofstream aa;
				aa.open("No_of_entries.txt");
				aa<<j.n<<endl;
				aa.close();
				ofstream obj;
				obj.open("gj.txt");
				obj.write((char*)&j,sizeof(j));
				obj.close();
				return;
			} 
			return ;
		}
		
		void updatefile(int x, JG j){
			int num;
			ifstream xx;
			xx.open("No_of_entries.txt");
			if(xx){
				int no;
				xx>>no;
				num = no;
				xx.close();	
			}
			
			JG g[num];
			
			ifstream obj;
			obj.open("gj.txt");
			obj.read((char*)&g,sizeof(g));
			obj.close();
			
			g[x-1].month = j.month;
			strcpy(g[x-1].des,j.des);
			g[x-1].credit = j.credit;
			g[x-1].debit = j.debit;
			g[x-1].date = j.date;
			
			ofstream gg;
			gg.open("general_journal.csv");
			gg<<"ENTRY NO"<<","<<"DATE"<<","<<"DESCRIPTION"<<","<<" "<<","<<"DR+"<<","<<"CR+"<<endl;
			for(int i = 0 ; i < num ; i++ ){
				if(g[i].debit != 0){
					gg<<i+1<<","<<g[i].month<<" "<<g[i].date<<","<<g[i].des<<","<<" "<<","<<g[i].debit<<endl;
				}
				else{
					gg<<i+1<<","<<g[i].month<<" "<<g[i].date<<","<<","<<g[i].des<<","<<" "<<","<<g[i].credit<<endl;
				}
				
			}
			gg.close();
			
		}
		
		void display(){
			int num;
			ifstream xx;
			xx.open("No_of_entries.txt");
			if(xx){
				int no;
				xx>>no;
				num = no;
				xx.close();	
			}
			
			JG g[num];
			
			ifstream obj;
			obj.open("gj.txt");
			obj.read((char*)&g,sizeof(g));
			obj.close();
			
			cout<<"ENTRY NO"<<","<<"DATE"<<","<<"DESCRIPTION"<<","<<" "<<","<<"DR+"<<","<<"CR+"<<endl;
			for(int i = 0 ; i < num ; i++ ){
				if(g[i].debit != 0){
					cout<<i+1<<","<<g[i].month<<" "<<g[i].date<<","<<g[i].des<<","<<" "<<","<<g[i].debit<<endl;
				}
				else{
					cout<<i+1<<","<<g[i].month<<" "<<g[i].date<<","<<","<<g[i].des<<","<<" "<<","<<g[i].credit<<endl;
				}
				
			}
		}
		
};

class  Taccount : public JG{
	public:
		Taccount(){
			
		}
		void create(){
			
			JG g[getn()];
			int deb[getn()],cre[getn()], sum =0 , z =0 , no2 = 0, x =1 ;
			int idk[getn()];
			for(int j = 0 ; j<getn() ; j++){
					idk[j] = -1;
					deb[j] = 0;
					cre[j] = 0;
				}
			
			
			ifstream obj;
			obj.open("gj.txt");
			obj.read((char*)&g,sizeof(g));
			obj.close();
			
			for(int i = 0 ;i < getn(); i++ ){
				cout<<g[i].getdes()<<endl;
				
			}
			
			ofstream oj;
			oj.open("Taccounts.csv");
			jump:	
			for(int i = no2 ; i < getn()-1 ; i ++){
				for(int j = 0 ; j < getn() ; j++){
					if(i == idk[j]){
						no2 = i+1;
						goto jump;
					}
				}
				for(int j = i+1 ; j<getn() ; j++){	
					if(g[i].getdes()==g[j].getdes()){
						idk[z] = j;
						z++;
					}
				}
				oj<<","<<g[i].getdes()<<endl;
				oj<<"Dr+"<<","<<","<<"Cr+"<<endl;
				oj<<g[i].getdebit()<<","<<","<<g[i].getcredit()<<endl;
				deb[0]=g[i].getdebit();
				cre[0]=g[i].getcredit();
				
				for(int j = i+1 ; j<getn() ; j++){
					if(g[i].getdes()==g[j].getdes()){
						oj<<g[j].getdebit()<<","<<","<<g[j].getcredit()<<endl;
						deb[x]=g[j].getdebit();
						cre[x]=g[j].getcredit();
						x++;
					}
					else{
						deb[x]=0;
						cre[x]=0;
						x++;
					}
				}
				for(int j = 0 ; j<getn() ; j++){
					sum += deb[j];
					sum -= cre[j];
				}
				if(sum>0){
					oj<<sum<<endl;
				}
				else{
					oj<<","<<","<<sum-sum-sum<<endl;
				}
				oj<<endl;
				sum = 0;
				x = 1;
			}
			oj.close();
		}

};

class trailbal : public JG{
	public:
		void create(){
			JG g[getn()];
			int deb[getn()],cre[getn()], sum =0 , z =0, no2 = 0 , x =1;
			int idk[getn()];
			for(int j = 0 ; j<getn() ; j++){
					idk[j] = -1;
					deb[j] = 0;
					cre[j] = 0;
				}
			
			
			ifstream obj;
			obj.open("gj.txt");
			obj.read((char*)&g,sizeof(g));
			obj.close();
			

			
			
			ofstream oj;
			oj.open("Trial-Balance.csv");
			oj<<","<<"Trial"<<","<<"Balance"<<endl;
			oj<<"Des"<<","<<"Dr+"<<","<<"Cr+"<<endl;
			
			jump:	
			for(int i = no2 ; i < getn() ; i ++){
				for(int j = 0 ; j < getn() ; j++){
					if(i == idk[j]){
						no2 = i+1;
						goto jump;
					}
				}
				for(int j = i+1 ; j<getn() ; j++){	
					if(g[i].getdes()==g[j].getdes()){
						idk[z] = j;
						z++;
					}
				}
				deb[0]=g[i].getdebit();
				cre[0]=g[i].getcredit();
				for(int j = i+1 ; j<getn() ; j++){
					if(g[i].getdes()==g[j].getdes()){
						deb[x]=g[j].getdebit();
						cre[x]=g[j].getcredit();
						x++;
					}
				}
				for(int j = 0 ; j<getn() ; j++){
					sum += deb[j];
					sum -= cre[j];
				}
				if(sum>0){
					oj<<g[i].getdes()<<","<<sum<<endl;
				}
				else{
					oj<<g[i].getdes()<<","<<","<<sum-sum-sum<<endl;
				}
				sum = 0;
				x = 1;
			}
			oj.close();
		}
			
};

int main(){
	string pass;
	accountant* a = new accountant[1];
	JG* jg = new JG[2];
	Taccount t;
	trailbal b;
	int c, c1, c2;
	string month, des;
	int credit, debit, date, num, num2;
	for(;;){
		cout<<"1=Sign up as new accountant"<<endl<<"2=Login"<<endl<<"3=exit"<<endl;
		cin.clear();
		cin>>c;
		if (!cin) {
			cout<<"INVALID RE-ENTER"<<endl;
			continue;
		}
		switch(c){
			case 1:
				for(;;){
					cout<<"Enter password as new accountant"<<endl;
					cin.clear();
					cin>>pass;
					a[0] = accountant(pass);
					for(;;){
						cout<<"Create new general Journal ,Press 1"<<endl<<"if gerneral journal exist ,Press 2 "<<endl<<"exit press any number"<<endl;
						cin.clear();
						cin>>c1;
						if (!cin) {
							cout<<"INVALID RE-ENTER"<<endl;
							continue;
						}
						switch(c1){
							case 1:
								cout<<"Enter number of entries"<<endl;
								cin>>num;
								for(int i = 0 ; i < num ; i++){
									cout<<"Enter month of entry"<<i+1<<endl;
									cin>>month;
									cout<<"Enter day of the month(number) of entry"<<i+1<<endl;
									cin>>date;
									cout<<"Enter description of entry"<<i+1<<endl;
									cin>>des;
									jg[0] = JG(month,des,date);
									jg[0].cord();
									a[0].initializefile(jg[0]);
									des.clear();
									month.clear();
								}
								
								for(;;){
									cout<<"Press 1, to adjust entry General Journal"<<endl<<"Press 2, to create Taccount"<<endl<<"Press 3, to create trail balance"<<endl<<"Press 4, to go back"<<endl<<"Press any number to exit"<<endl;
									cin.clear();
									cin>>c2;
									
									if (!cin) {
										cout<<"INVALID RE-ENTER"<<endl;
										continue;
									}	
									
									switch(c2){
										case 1:
											cout<<"Enter entry number:"<<endl;
											cin>>num2;
											cout<<"Enter month of entry"<<endl;
											cin>>month;
											cout<<"Enter day of the month(number) of entry"<<endl;
											cin>>date;
											cout<<"Enter description of entry"<<endl;
											cin>>des;
											jg[1] = JG(month,des,date);
											jg[1].cord();
											a[0].updatefile(num2, jg[1]);
											des.clear();
											month.clear();
											continue;
										
										case 2:
											t.create();
											continue;
											
										case 3:
											b.create();
											continue;
											
										case 4:
											break;
										
										default:
											return 0;
													
									}
								}
									
								continue;
								
							case 2:
								jg[0].setn();
								for(;;){
									cout<<"Press 1, to adjust entry General Journal"<<endl<<"Press 2, to create Taccount"<<endl<<"Press 3, to create trail balance"<<endl<<"Press 4, to go back"<<endl<<"Press any number to exit"<<endl;
									cin.clear();
									cin>>c2;
									if (!cin) {
										cout<<"INVALID RE-ENTER"<<endl;
										continue;
									}
									
									switch(c2){
										case 1:
											cout<<"Enter entry number:"<<endl;
											cin>>num2;
											cout<<"Enter month of entry"<<endl;
											cin>>month;
											cout<<"Enter day of the month(number) of entry"<<endl;
											cin>>date;
											cout<<"Enter description of entry"<<endl;
											cin>>des;
											jg[1] = JG(month,des,date);
											jg[1].cord();
											a[0].updatefile(num2, jg[1]);
											des.clear();
											month.clear();
											continue;
										
										case 2:
											t.create();
											continue;
											
										case 3:
											b.create();
											continue;
											
										case 4:
											break;
										
										default:
											return 0;
													
									}	
								}
								continue;
							
							default:
								return 0;
								
					}
			}	
				break;
			case 2:
				cout<<"Enter password as new accountant"<<endl;
				cin>>pass;
				if(a[0].check(pass)){
					cout<<"Valid password"<<endl;
				}
				else{
					cout<<"Invalid password"<<endl;
					continue;
				}
				for(;;){
						cout<<"Create new general Journal ,Press 1"<<endl<<"if gerneral journal exist ,Press 2 "<<endl<<"exit press any number"<<endl;
						cin.clear();
						cin>>c1;
						if (!cin) {
							cout<<"INVALID RE-ENTER"<<endl;
							continue;
						}
						switch(c1){
							case 1:
								cout<<"Enter number of entries"<<endl;
								cin>>num;
								for(int i = 0 ; i < num ; i++){
									cout<<"Enter month of entry"<<i+1<<endl;
									cin>>month;
									cout<<"Enter day of the month(number) of entry"<<i+1<<endl;
									cin>>date;
									cout<<"Enter description of entry"<<i+1<<endl;
									cin>>des;
									jg[0] = JG(month,des,date);
									jg[0].cord();
									a[0].initializefile(jg[0]);
									des.clear();
									month.clear();
								}
								
								for(;;){
									cout<<"Press 1, to adjust entry General Journal"<<endl<<"Press 2, to create Taccount"<<endl<<"Press 3, to create trail balance"<<endl<<"Press 4, to go back"<<endl<<"Press any number to exit"<<endl;
									cin.clear();
									cin>>c2;
									if (!cin) {
										cout<<"INVALID RE-ENTER"<<endl;
										continue;
									}
									
									switch(c2){
										case 1:
											cout<<"Enter entry number:"<<endl;
											cin>>num2;
											cout<<"Enter month of entry"<<endl;
											cin>>month;
											cout<<"Enter day of the month(number) of entry"<<endl;
											cin>>date;
											cout<<"Enter description of entry"<<endl;
											cin>>des;
											jg[1] = JG(month,des,date);
											jg[1].cord();
											a[0].updatefile(num2, jg[1]);
											des.clear();
											month.clear();
											continue;
										
										case 2:
											t.create();
											continue;
											
										case 3:
											b.create();
											continue;
											
										case 4:
											break;
										
										default:
											return 0;
													
									}
								}
									
								continue;
								
							case 2:
								jg[0].setn();
								for(;;){
									cout<<"Press 1, to adjust entry General Journal"<<endl<<"Press 2, to create Taccount"<<endl<<"Press 3, to create trail balance"<<endl<<"Press 4, to go back"<<endl<<"Press any number to exit"<<endl;
									cin.clear();
									cin>>c2;
									if (!cin) {
										cout<<"INVALID RE-ENTER"<<endl;
										continue;
									}
									
									switch(c2){
										case 1:
											cout<<"Enter entry number:"<<endl;
											cin>>num2;
											cout<<"Enter month of entry"<<endl;
											cin>>month;
											cout<<"Enter day of the month(number) of entry"<<endl;
											cin>>date; 
											cout<<"Enter description of entry"<<endl;
											cin>>des;
											jg[1] = JG(month,des,date);
											jg[1].cord();
											a[0].updatefile(num2, jg[1]);
											des.clear();
											month.clear();
											continue;
										
										case 2:
											t.create();
											continue;
											
										case 3:
											b.create();
											continue;
											
										case 4:
											break;
										
										default:
											return 0;
													
									}	
								}
								continue;
							
							default:
								return 0;
								
					}
			}
				break;
			case 3:
				break;
			default:
				continue;
				
				
		}
		break;
	}
	
	}

}
